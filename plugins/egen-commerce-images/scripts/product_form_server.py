#!/usr/bin/env python3
"""Local browser form server for ecommerce product image tasks."""

from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
FORM_PATH = PLUGIN_ROOT / "assets" / "product-task-form.html"
DEFAULT_OUTPUT = (
    Path(tempfile.gettempdir())
    / "egen-commerce-images"
    / "latest-product-task.json"
)
SCHEMA_VERSION = 1


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def with_meta(payload: dict[str, Any]) -> dict[str, Any]:
    payload = dict(payload)
    meta = dict(payload.get("meta") or {})
    meta["schemaVersion"] = SCHEMA_VERSION
    meta["savedAt"] = utc_now()
    payload["meta"] = meta
    return payload


def make_handler(output_path: Path) -> type[BaseHTTPRequestHandler]:
    class ProductFormHandler(BaseHTTPRequestHandler):
        server_version = "EgenProductForm/0.4"

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

        def do_OPTIONS(self) -> None:
            self._send_bytes(204, b"", "text/plain")

        def do_GET(self) -> None:
            path = self.path.split("?", 1)[0]
            if path in ("", "/"):
                if not FORM_PATH.exists():
                    self._send_json(500, {"error": "form_not_found", "path": str(FORM_PATH)})
                    return
                body = FORM_PATH.read_bytes()
                self._send_bytes(200, body, "text/html; charset=utf-8")
                return

            if path == "/config":
                self._send_json(
                    200,
                    {
                        "schemaVersion": SCHEMA_VERSION,
                        "outputPath": str(output_path),
                    },
                )
                return

            if path == "/latest":
                if not output_path.exists():
                    self._send_json(
                        404,
                        {
                            "error": "no_saved_form",
                            "path": str(output_path),
                        },
                    )
                    return
                self._send_bytes(
                    200,
                    output_path.read_bytes(),
                    "application/json; charset=utf-8",
                )
                return

            if path == "/health":
                self._send_json(200, {"ok": True, "outputPath": str(output_path)})
                return

            self._send_json(404, {"error": "not_found"})

        def do_POST(self) -> None:
            path = self.path.split("?", 1)[0]
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

            output_path.parent.mkdir(parents=True, exist_ok=True)
            saved_payload = with_meta(payload)
            output_path.write_text(
                json.dumps(saved_payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            self._send_json(
                200,
                {
                    "ok": True,
                    "outputPath": str(output_path),
                    "savedAt": saved_payload["meta"]["savedAt"],
                    "payload": saved_payload,
                },
            )

    return ProductFormHandler


def bind_server(host: str, port: int, output_path: Path) -> ThreadingHTTPServer:
    handler = make_handler(output_path)
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
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.output.expanduser().resolve()
    try:
        server = bind_server(args.host, args.port, output_path)
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
    print(f"JSON_PATH={output_path}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
