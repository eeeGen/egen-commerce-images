#!/usr/bin/env python3
"""Local browser form server for ecommerce product image tasks."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import tempfile
import threading
import time
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
ASSETS_ROOT = PLUGIN_ROOT / "assets"
FORM_PATH = PLUGIN_ROOT / "assets" / "product-task-form.html"
DEFAULT_OUTPUT_DIR = (
    Path(tempfile.gettempdir())
    / "egen-commerce-images"
    / "tasks"
)
SCHEMA_VERSION = 2


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def filename_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def with_meta(
    payload: dict[str, Any],
    task_id: str,
    form_started_at: str,
    save_count: int,
) -> dict[str, Any]:
    payload = dict(payload)
    meta = dict(payload.get("meta") or {})
    meta["schemaVersion"] = SCHEMA_VERSION
    meta["taskId"] = task_id
    meta["formStartedAt"] = form_started_at
    meta["savedAt"] = utc_now()
    meta["saveCount"] = save_count
    payload["meta"] = meta
    return payload


def make_output_path(output_dir: Path, task_id: str, save_count: int) -> Path:
    name = f"product-task-{filename_timestamp()}-{task_id}-{save_count:02d}.json"
    return output_dir / name


def resolve_asset_path(request_path: str) -> Path | None:
    relative_path = request_path.removeprefix("/assets/").replace("/", os.sep)
    if not relative_path or relative_path.startswith((".", os.sep)):
        return None
    candidate = (ASSETS_ROOT / relative_path).resolve()
    assets_root = ASSETS_ROOT.resolve()
    if not candidate.is_relative_to(assets_root):
        return None
    if not candidate.is_file():
        return None
    return candidate


def content_type_for(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    return guessed or "application/octet-stream"


def make_handler(
    output_dir: Path,
    task_id: str,
    form_started_at: str,
) -> type[BaseHTTPRequestHandler]:
    saved_condition = threading.Condition()
    saved_state: dict[str, Any] = {
        "saveCount": 0,
        "jsonPath": None,
        "payload": None,
        "savedAt": None,
    }

    class ProductFormHandler(BaseHTTPRequestHandler):
        server_version = "EgenProductForm/0.6.0"

        def log_message(self, format: str, *args: Any) -> None:
            return

        def _send_bytes(
            self,
            status: int,
            body: bytes,
            content_type: str,
        ) -> None:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()
            self.wfile.write(body)

        def _send_json(self, status: int, payload: Any) -> None:
            body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self._send_bytes(status, body, "application/json; charset=utf-8")

        def _schedule_shutdown(self) -> None:
            threading.Thread(target=self.server.shutdown, daemon=True).start()

        def _current_saved_response(self) -> dict[str, Any] | None:
            if not saved_state["payload"] or not saved_state["jsonPath"]:
                return None
            return {
                "ok": True,
                "taskId": task_id,
                "jsonPath": str(saved_state["jsonPath"]),
                "savedAt": saved_state["savedAt"],
                "payload": saved_state["payload"],
            }

        def _wait_for_save(self, timeout_seconds: float) -> dict[str, Any] | None:
            deadline = time.monotonic() + timeout_seconds
            with saved_condition:
                while not saved_state["payload"]:
                    remaining = deadline - time.monotonic()
                    if remaining <= 0:
                        return None
                    saved_condition.wait(timeout=remaining)
                return self._current_saved_response()

        def do_OPTIONS(self) -> None:
            self._send_bytes(204, b"", "text/plain")

        def do_GET(self) -> None:
            parsed_url = urlparse(self.path)
            path = parsed_url.path
            if path in ("", "/"):
                if not FORM_PATH.exists():
                    self._send_json(500, {"error": "form_not_found", "path": str(FORM_PATH)})
                    return
                body = FORM_PATH.read_bytes()
                self._send_bytes(200, body, "text/html; charset=utf-8")
                return

            if path.startswith("/assets/"):
                asset_path = resolve_asset_path(path)
                if asset_path is None:
                    self._send_json(404, {"error": "asset_not_found"})
                    return
                self._send_bytes(200, asset_path.read_bytes(), content_type_for(asset_path))
                return

            if path == "/config":
                self._send_json(
                    200,
                    {
                        "schemaVersion": SCHEMA_VERSION,
                        "taskId": task_id,
                        "formStartedAt": form_started_at,
                    },
                )
                return

            if path == "/latest":
                response = self._current_saved_response()
                if response is None:
                    self._send_json(
                        404,
                        {
                            "error": "no_saved_form",
                            "taskId": task_id,
                        },
                    )
                    return
                self._send_json(200, response)
                return

            if path == "/wait":
                query = parse_qs(parsed_url.query)
                try:
                    timeout_seconds = float((query.get("timeout") or ["300"])[0])
                except ValueError:
                    timeout_seconds = 300
                timeout_seconds = max(1, min(timeout_seconds, 1800))
                response = self._wait_for_save(timeout_seconds)
                if response is None:
                    self._send_json(
                        408,
                        {
                            "ok": False,
                            "error": "wait_timeout",
                            "taskId": task_id,
                        },
                    )
                    return
                self._send_json(200, response)
                return

            if path == "/health":
                self._send_json(
                    200,
                    {
                        "ok": True,
                        "taskId": task_id,
                        "formStartedAt": form_started_at,
                        "saved": bool(saved_state["payload"]),
                        "jsonPath": (
                            str(saved_state["jsonPath"])
                            if saved_state["jsonPath"]
                            else None
                        ),
                    },
                )
                return

            if path == "/shutdown":
                self._send_json(200, {"ok": True, "message": "server shutting down"})
                self._schedule_shutdown()
                return

            self._send_json(404, {"error": "not_found"})

        def do_POST(self) -> None:
            path = self.path.split("?", 1)[0]
            if path == "/shutdown":
                self._send_json(200, {"ok": True, "message": "server shutting down"})
                self._schedule_shutdown()
                return

            if path != "/save":
                self._send_json(404, {"error": "not_found"})
                return

            content_length = int(self.headers.get("Content-Length", "0") or "0")
            raw_body = self.rfile.read(content_length)
            try:
                payload = json.loads(raw_body.decode("utf-8"))
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                self._send_json(400, {"error": "invalid_json", "message": str(exc)})
                return

            if not isinstance(payload, dict):
                self._send_json(400, {"error": "payload_must_be_object"})
                return

            output_dir.mkdir(parents=True, exist_ok=True)
            with saved_condition:
                saved_state["saveCount"] += 1
                output_path = make_output_path(
                    output_dir,
                    task_id,
                    int(saved_state["saveCount"]),
                )
                saved_payload = with_meta(
                    payload,
                    task_id,
                    form_started_at,
                    int(saved_state["saveCount"]),
                )
            output_path.write_text(
                json.dumps(saved_payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            with saved_condition:
                saved_state["jsonPath"] = output_path
                saved_state["payload"] = saved_payload
                saved_state["savedAt"] = saved_payload["meta"]["savedAt"]
                saved_condition.notify_all()
                response_payload = {
                    "ok": True,
                    "taskId": task_id,
                    "jsonPath": str(output_path),
                    "savedAt": saved_payload["meta"]["savedAt"],
                    "payload": saved_payload,
                }
            self._send_json(200, response_payload)

    return ProductFormHandler


def bind_server(
    host: str,
    port: int,
    output_dir: Path,
    task_id: str,
    form_started_at: str,
) -> ThreadingHTTPServer:
    handler = make_handler(output_dir, task_id, form_started_at)
    if port == 0:
        return ThreadingHTTPServer((host, 0), handler)

    last_error: OSError | None = None
    for candidate in range(port, port + 25):
        try:
            return ThreadingHTTPServer((host, candidate), handler)
        except OSError as exc:
            last_error = exc
    raise RuntimeError(f"Could not bind {host}:{port}-{port + 24}: {last_error}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Serve the ecommerce product task form and save JSON locally."
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir.expanduser().resolve()
    task_id = uuid.uuid4().hex[:8]
    form_started_at = utc_now()
    try:
        server = bind_server(args.host, args.port, output_dir, task_id, form_started_at)
    except (OSError, RuntimeError) as exc:
        print(
            f"ERROR: could not start local form server on {args.host}:{args.port}: {exc}",
            file=sys.stderr,
            flush=True,
        )
        return 1
    host, port = server.server_address[:2]
    print(f"FORM_URL=http://{host}:{port}/", flush=True)
    print(f"LATEST_URL=http://{host}:{port}/latest", flush=True)
    print(f"WAIT_URL=http://{host}:{port}/wait?timeout=600", flush=True)
    print(f"JSON_DIR={output_dir}", flush=True)
    print(f"TASK_ID={task_id}", flush=True)
    print(f"PID={os.getpid()}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
