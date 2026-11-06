"""Discover and bind a single local image library for customer reference styles."""

from __future__ import annotations

import ctypes
import json
import os
import stat
import uuid
from collections import deque
from pathlib import Path
from typing import Any, Iterable


MARKER_FILE = ".imglib.json"
MAX_DEPTH = 5
SKIP_DIRECTORIES = {".git", "node_modules"}
CONFIG_PATH = Path.home() / ".codex" / "skills" / "image-library" / "config.json"
IMAGE_EXTENSIONS = {".jpeg", ".jpg", ".png", ".webp"}


def clean_manual_path(value: str) -> str:
    """Remove outer whitespace and one complete pair of ASCII double quotes."""
    if not isinstance(value, str):
        raise ValueError("path_must_be_string")
    cleaned = value.strip()
    return cleaned[1:-1] if len(cleaned) >= 2 and cleaned[0] == cleaned[-1] == '"' else cleaned


def _path_key(path: Path) -> str:
    return os.path.normcase(os.path.abspath(path))


def _is_directory_link(path: Path) -> bool:
    try:
        metadata = path.stat(follow_symlinks=False)
    except OSError:
        return True
    return path.is_symlink() or bool(
        getattr(metadata, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def _safe_directories(root: Path, *, skip_ignored: bool = True) -> list[Path]:
    try:
        with os.scandir(root) as entries:
            children = [
                Path(entry.path)
                for entry in entries
                if (not skip_ignored or entry.name.casefold() not in SKIP_DIRECTORIES)
                and entry.is_dir(follow_symlinks=False)
                and not _is_directory_link(Path(entry.path))
            ]
    except OSError:
        return []
    return sorted(children, key=lambda path: path.name.casefold())


def scan_for_libraries(roots: Iterable[Path], max_depth: int = MAX_DEPTH) -> list[Path]:
    """Search every local candidate root through depth five, without directory links."""
    found: list[Path] = []
    visited: set[str] = set()
    for root in roots:
        root = Path(root).expanduser()
        if _is_directory_link(root) or not root.is_dir():
            continue
        queue = deque([(root, 0)])
        while queue:
            directory, depth = queue.popleft()
            key = _path_key(directory)
            if key in visited:
                continue
            visited.add(key)
            try:
                if (directory / MARKER_FILE).is_file():
                    found.append(directory)
            except OSError:
                pass
            if depth < max_depth:
                queue.extend((child, depth + 1) for child in _safe_directories(directory))
    return found


def local_drives() -> list[Path]:
    if os.name != "nt":
        return []
    kernel32 = ctypes.windll.kernel32
    mask = kernel32.GetLogicalDrives()
    return [
        Path(f"{chr(ord('A') + index)}:/")
        for index in range(26)
        if mask & (1 << index)
        and kernel32.GetDriveTypeW(f"{chr(ord('A') + index)}:\\") in (2, 3)
    ]


def _local_root(path: Path) -> bool:
    if os.name != "nt":
        return True
    if str(path).startswith("\\\\") or not path.anchor:
        return False
    return ctypes.windll.kernel32.GetDriveTypeW(path.anchor) in (2, 3)


def user_directories() -> list[Path]:
    home = Path.home()
    defaults = [home / "Pictures", home / "Documents", home / "Desktop"]
    if os.name != "nt":
        return defaults
    try:
        import winreg

        with winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders",
        ) as key:
            redirected = []
            for name in ("My Pictures", "Personal", "Desktop"):
                try:
                    redirected.append(Path(os.path.expandvars(winreg.QueryValueEx(key, name)[0])))
                except OSError:
                    continue
        return redirected + defaults
    except (OSError, ValueError):
        return defaults


def volume_label(drive: Path) -> str:
    if os.name != "nt":
        return ""
    label = ctypes.create_unicode_buffer(256)
    success = ctypes.windll.kernel32.GetVolumeInformationW(
        str(drive), label, len(label), None, None, None, None, 0
    )
    return label.value if success else ""


def read_config(config_path: Path = CONFIG_PATH) -> dict[str, Any]:
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return config if isinstance(config, dict) else {}


def _marker_id(root: Path) -> str:
    try:
        data = json.loads((root / MARKER_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return ""
    marker_id = data.get("libraryId") if isinstance(data, dict) else None
    return marker_id if isinstance(marker_id, str) else ""


def _configured_candidates(config: dict[str, Any], drives: Iterable[Path]) -> list[Path]:
    last_known = config.get("last_known")
    if not isinstance(last_known, dict):
        return []
    wanted_label = last_known.get("volume_label")
    relative_hint = last_known.get("relative_hint")
    wanted_id = last_known.get("library_id")
    if not isinstance(wanted_label, str) or not wanted_label or not isinstance(relative_hint, str):
        return []
    parts = Path(relative_hint.replace("/", os.sep))
    if parts.is_absolute() or ".." in parts.parts:
        return []
    candidates = []
    for drive in drives:
        try:
            if volume_label(drive) == wanted_label:
                candidate = drive / parts
                if (candidate / MARKER_FILE).is_file() and (
                    not wanted_id or _marker_id(candidate) == wanted_id
                ):
                    candidates.append(candidate)
        except OSError:
            continue
    return candidates


def discover_library(
    workspace: Path,
    *,
    config_path: Path = CONFIG_PATH,
    environ: dict[str, str] | None = None,
    scan_roots: Iterable[Path] | None = None,
    drives: Iterable[Path] | None = None,
) -> dict[str, Any]:
    """Return candidates from the first successful priority, never picking a tie."""
    environment = os.environ if environ is None else environ
    if "IMG_LIB" in environment:
        location = clean_manual_path(environment["IMG_LIB"])
        root = Path(location).expanduser() if location else None
        if root and (root / MARKER_FILE).is_file():
            return {"status": "found", "source": "environment", "candidates": [root]}
        return {"status": "invalid_environment", "source": "environment", "candidates": []}

    available_drives = list(local_drives() if drives is None else drives)
    configured = _configured_candidates(read_config(config_path), available_drives)
    if configured:
        return {"status": "found" if len(configured) == 1 else "multiple", "source": "config", "candidates": configured}

    roots = list(scan_roots) if scan_roots is not None else [workspace, *user_directories(), *available_drives]
    found = scan_for_libraries(root for root in roots if _local_root(Path(root)))
    return {"status": "found" if len(found) == 1 else "multiple" if found else "missing", "source": "scan", "candidates": found}


def bind_library(root: Path, config_path: Path = CONFIG_PATH) -> Path:
    root = Path(clean_manual_path(str(root))).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("library_directory_not_found")
    marker = root / MARKER_FILE
    if not marker.exists():
        marker.write_text(json.dumps({"libraryId": uuid.uuid4().hex}, indent=2), encoding="utf-8")
    elif not marker.is_file():
        raise ValueError("invalid_library_marker")
    elif not _marker_id(root):
        try:
            marker_data = json.loads(marker.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            marker_data = None
        if isinstance(marker_data, dict):
            marker_data["libraryId"] = uuid.uuid4().hex
            marker.write_text(json.dumps(marker_data, ensure_ascii=False, indent=2), encoding="utf-8")

    config = read_config(config_path)
    label = volume_label(Path(root.anchor)) if root.anchor else ""
    config["marker_file"] = MARKER_FILE
    config["max_depth"] = MAX_DEPTH
    config["last_known"] = {
        "volume_label": label,
        "relative_hint": root.relative_to(root.anchor).as_posix() if root.anchor else "",
        "library_id": _marker_id(root),
    }
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")
    return root


def list_styles(root: Path) -> list[dict[str, Any]]:
    if not (root / MARKER_FILE).is_file():
        raise ValueError("library_marker_missing")
    styles = []
    for folder in _safe_directories(root, skip_ignored=False):
        try:
            image_count = sum(
                1 for image in folder.iterdir()
                if image.is_file() and not image.is_symlink() and image.suffix.lower() in IMAGE_EXTENSIONS
            )
        except OSError:
            image_count = 0
        styles.append({
            "name": folder.name,
            "imageCount": image_count,
            "disabledReason": "没有直属的可用图片" if image_count == 0 else "",
        })
    return styles


def pick_library_folder() -> Path | None:
    """Open a native folder dialog; raise RuntimeError when no desktop is available."""
    if os.name != "nt" and not (os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY")):
        raise RuntimeError("no_desktop")
    try:
        import tkinter as tk
        from tkinter import filedialog
    except ImportError as exc:
        raise RuntimeError("no_desktop") from exc
    try:
        window = tk.Tk()
        window.withdraw()
        window.attributes("-topmost", True)
        try:
            selected = filedialog.askdirectory(title="请选择参考图库根目录", mustexist=True, parent=window)
        finally:
            window.destroy()
    except (tk.TclError, RuntimeError, OSError) as exc:
        raise RuntimeError("no_desktop") from exc
    return Path(selected) if selected else None
