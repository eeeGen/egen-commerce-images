"""Focused checks for portable customer-reference library discovery."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import image_library as library


class LibraryDiscoveryTests(unittest.TestCase):
    def test_manual_path_cleanup_changes_only_outer_whitespace_and_quotes(self) -> None:
        self.assertEqual(library.clean_manual_path('  "D:\\图库\\a b.png"  '), 'D:\\图库\\a b.png')
        self.assertEqual(library.clean_manual_path("  'D:\\图库\\a.png'  "), "'D:\\图库\\a.png'")
        self.assertEqual(library.clean_manual_path('  "D:\\图库\\a.png  '), '"D:\\图库\\a.png')
        self.assertEqual(library.clean_manual_path('  " a b "  '), ' a b ')

    def test_depth_five_is_found_but_six_is_not(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            depth_five = root.joinpath(*[f"level{index}" for index in range(1, 6)])
            depth_six = depth_five / "level6"
            depth_six.mkdir(parents=True)
            (depth_five / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            (depth_six / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            self.assertEqual(library.scan_for_libraries([root]), [depth_five])

    def test_discovery_skips_git_node_modules_and_directory_links(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for name in (".git", "node_modules", "visible"):
                folder = root / name
                folder.mkdir()
                (folder / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            self.assertEqual(library.scan_for_libraries([root]), [root / "visible"])
            link = root / "linked"
            try:
                link.symlink_to(root / "visible", target_is_directory=True)
            except OSError:
                return
            self.assertEqual(library.scan_for_libraries([root]), [root / "visible"])

    def test_invalid_environment_never_falls_through(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            result = library.discover_library(
                root,
                environ={"IMG_LIB": str(root / "missing")},
                scan_roots=[root],
                drives=[],
                config_path=root / "config.json",
            )
            self.assertEqual(result["status"], "invalid_environment")
            self.assertEqual(result["candidates"], [])

    def test_stale_config_falls_through_to_workspace_scan_and_preserves_ties(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            first = root / "first"
            second = root / "second"
            for folder in (first, second):
                folder.mkdir()
                (folder / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            config_path = root / "config.json"
            config_path.write_text(json.dumps({"last_known": {"volume_label": "old", "relative_hint": "gone"}}), encoding="utf-8")
            result = library.discover_library(
                root,
                environ={},
                scan_roots=[root],
                drives=[],
                config_path=config_path,
            )
            self.assertEqual(result["source"], "scan")
            self.assertEqual(result["status"], "multiple")
            self.assertEqual(result["candidates"], [first, second])

    def test_configured_rule_takes_priority_over_scan(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            configured = root / "chosen"
            other = root / "other"
            for folder in (configured, other):
                folder.mkdir()
                (folder / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            config_path = root / "config.json"
            config_path.write_text(json.dumps({"last_known": {"volume_label": "LIB", "relative_hint": "chosen"}}), encoding="utf-8")
            with patch.object(library, "volume_label", return_value="LIB"):
                result = library.discover_library(
                    root,
                    environ={},
                    scan_roots=[root],
                    drives=[root],
                    config_path=config_path,
                )
            self.assertEqual(result["source"], "config")
            self.assertEqual(result["candidates"], [configured])

    def test_marker_identity_resolves_same_label_and_relative_hint(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            drives = [root / "drive-one", root / "drive-two"]
            for index, drive in enumerate(drives):
                folder = drive / "library"
                folder.mkdir(parents=True)
                (folder / library.MARKER_FILE).write_text(
                    json.dumps({"libraryId": f"library-{index}"}), encoding="utf-8"
                )
            config_path = root / "config.json"
            config_path.write_text(json.dumps({"last_known": {
                "volume_label": "LIB",
                "relative_hint": "library",
                "library_id": "library-1",
            }}), encoding="utf-8")
            with patch.object(library, "volume_label", return_value="LIB"):
                result = library.discover_library(
                    root,
                    environ={},
                    scan_roots=[root],
                    drives=drives,
                    config_path=config_path,
                )
            self.assertEqual(result["candidates"], [drives[1] / "library"])

    def test_binding_creates_marker_and_portable_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "图库"
            root.mkdir()
            config_path = root.parent / "config.json"
            with patch.object(library, "volume_label", return_value="LIB"):
                library.bind_library(root, config_path)
            self.assertTrue((root / library.MARKER_FILE).is_file())
            config = json.loads(config_path.read_text(encoding="utf-8"))
            self.assertEqual(config["last_known"]["volume_label"], "LIB")
            self.assertEqual(
                config["last_known"]["library_id"],
                json.loads((root / library.MARKER_FILE).read_text(encoding="utf-8"))["libraryId"],
            )
            self.assertFalse(Path(config["last_known"]["relative_hint"]).is_absolute())
            self.assertNotIn(str(root), config_path.read_text(encoding="utf-8"))

    def test_style_menu_includes_empty_folder_and_only_direct_images(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / library.MARKER_FILE).write_text("{}", encoding="utf-8")
            filled = root / "暖色 秋季"
            empty = root / "空风格"
            filled.mkdir()
            empty.mkdir()
            (filled / "cover.PNG").write_bytes(b"png")
            (filled / "notes.txt").write_text("notes", encoding="utf-8")
            nested = empty / "nested"
            nested.mkdir()
            (nested / "ignored.jpg").write_bytes(b"jpg")
            styles = {style["name"]: style for style in library.list_styles(root)}
            self.assertEqual(styles["暖色 秋季"]["imageCount"], 1)
            self.assertEqual(styles["暖色 秋季"]["disabledReason"], "")
            self.assertEqual(styles["空风格"]["imageCount"], 0)
            self.assertTrue(styles["空风格"]["disabledReason"])


if __name__ == "__main__":
    unittest.main()
