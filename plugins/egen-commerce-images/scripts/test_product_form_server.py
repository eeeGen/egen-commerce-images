"""Regression tests for local product task material scanning."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


SERVER_PATH = Path(__file__).with_name("product_form_server.py")
SPEC = importlib.util.spec_from_file_location("product_form_server", SERVER_PATH)
assert SPEC and SPEC.loader
server = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(server)


class ScanImageDirectoryTests(unittest.TestCase):
    def test_scans_only_top_level_supported_images_with_a_limit(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "01-product.jpg").write_bytes(b"jpg")
            (root / "02-style.PNG").write_bytes(b"png")
            (root / "notes.txt").write_text("not an image", encoding="utf-8")
            nested = root / "nested"
            nested.mkdir()
            (nested / "ignored.webp").write_bytes(b"webp")

            result = server.scan_image_directory(root, limit=1)

            self.assertEqual(result["directory"], str(root.resolve()))
            self.assertEqual([item["name"] for item in result["images"]], ["01-product.jpg"])
            self.assertTrue(result["truncated"])
            self.assertTrue(result["images"][0]["id"])

    def test_rejects_files_and_missing_directories(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            image = root / "product.jpg"
            image.write_bytes(b"jpg")

            with self.assertRaises(ValueError):
                server.scan_image_directory(image, limit=10)
            with self.assertRaises(ValueError):
                server.scan_image_directory(root / "missing", limit=10)


if __name__ == "__main__":
    unittest.main()
