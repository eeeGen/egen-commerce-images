"""Regression tests for local product task material scanning."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


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


class CustomerReferenceWorkflowTests(unittest.TestCase):
    def setUp(self) -> None:
        self.catalog = {
            **{
                f"p{index}": {"kind": "product", "name": f"{index}.jpg", "path": f"C:/product/{index}.jpg"}
                for index in range(1, 7)
            },
            "s1": {"kind": "style", "name": "first.jpg", "path": "C:/style/first.jpg"},
            "s2": {"kind": "style", "name": "second.jpg", "path": "C:/style/second.jpg"},
            "master": {"kind": "style", "name": "palette.jpg", "path": "C:/style/palette.jpg"},
        }

    def payload(self, **overrides: object) -> dict:
        workflow = {
            "productImageIds": ["p1", "p2", "p3", "p4", "p5"],
            "styleReferenceIds": ["s2", "s1"],
            "colorMasterId": "master",
            "colorPriority": "auto",
        }
        workflow.update(overrides)
        return {
            "taskOptions": {"styleSource": "customer-reference"},
            "referenceWorkflow": workflow,
        }

    def test_resolves_all_product_paths_and_ordered_style_paths(self) -> None:
        payload = self.payload(
            productImagePaths=["C:/forged-product.jpg"],
            styleReferencePaths=["C:/forged-style.jpg"],
            colorMasterPath="C:/forged-master.jpg",
        )
        resolved = server.resolve_customer_reference_workflow(payload, self.catalog)
        workflow = resolved["referenceWorkflow"]
        self.assertEqual(workflow["productImagePaths"], [f"C:/product/{index}.jpg" for index in range(1, 6)])
        self.assertEqual(workflow["styleReferencePaths"], ["C:/style/second.jpg", "C:/style/first.jpg"])
        self.assertEqual(workflow["colorMasterPath"], "C:/style/palette.jpg")
        self.assertNotIn("C:/style/palette.jpg", workflow["styleReferencePaths"])

    def test_rejects_missing_duplicate_or_wrong_kind_materials(self) -> None:
        invalid_workflows = [
            {"productImageIds": []},
            {"styleReferenceIds": []},
            {"colorMasterId": ""},
            {"productImageIds": ["p1", "p1"]},
            {"styleReferenceIds": ["s1", "s1"]},
            {"productImageIds": ["s1"]},
            {"styleReferenceIds": ["p1"]},
            {"colorMasterId": "p1"},
            {"styleReferenceIds": ["unknown"]},
            {"colorPriority": "invalid"},
        ]
        for overrides in invalid_workflows:
            with self.subTest(overrides=overrides), self.assertRaises(ValueError):
                server.resolve_customer_reference_workflow(self.payload(**overrides), self.catalog)

    def test_builtin_payload_is_unchanged(self) -> None:
        payload = {"taskOptions": {"styleSource": "builtin"}, "referenceWorkflow": None}
        self.assertIs(server.resolve_customer_reference_workflow(payload, self.catalog), payload)

    def test_customer_paths_are_cleaned_without_changing_resolved_image_paths(self) -> None:
        payload = self.payload(
            productMaterialsDirectory='  "C:/product photos"  ',
            styleMaterialsDirectory='  "C:/style photos"  ',
        )
        payload["productInfo"] = {"productInfoPath": '  "C:/docs/info sheet.pdf"  '}
        workflow = server.resolve_customer_reference_workflow(payload, self.catalog)
        self.assertEqual(workflow["referenceWorkflow"]["productMaterialsDirectory"], "C:/product photos")
        self.assertEqual(workflow["referenceWorkflow"]["styleMaterialsDirectory"], "C:/style photos")
        self.assertEqual(workflow["productInfo"]["productInfoPath"], "C:/docs/info sheet.pdf")
        self.assertEqual(workflow["referenceWorkflow"]["styleReferencePaths"][0], "C:/style/second.jpg")


class PickerConcurrencyTests(unittest.TestCase):
    def test_parallel_pick_requests_open_only_one_folder_dialog(self) -> None:
        picker_started = threading.Event()
        release_picker = threading.Event()
        call_count = 0
        count_lock = threading.Lock()

        def fake_picker() -> None:
            nonlocal call_count
            with count_lock:
                call_count += 1
            picker_started.set()
            release_picker.wait(timeout=3)
            return None

        handler = server.make_handler(Path(tempfile.gettempdir()), "task", "start", "test-token")
        http_server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        serving_thread = threading.Thread(target=http_server.serve_forever, daemon=True)
        serving_thread.start()
        url = f"http://127.0.0.1:{http_server.server_port}/library/pick?token=test-token"

        def request_picker() -> str:
            request = Request(url, method="POST")
            try:
                response = urlopen(request, timeout=4)
            except HTTPError as error:
                response = error
            with response:
                result = json.load(response)
                return result.get("status") or result.get("error")

        try:
            with patch.object(server, "pick_library_folder", side_effect=fake_picker):
                with ThreadPoolExecutor(max_workers=5) as executor:
                    first = executor.submit(request_picker)
                    self.assertTrue(picker_started.wait(timeout=2))
                    others = [executor.submit(request_picker) for _ in range(4)]
                    time.sleep(0.2)
                    release_picker.set()
                    results = [future.result(timeout=4) for future in [first, *others]]
            self.assertEqual(call_count, 1)
            self.assertEqual(results.count("cancelled"), 1)
            self.assertEqual(results.count("picker_busy"), 4)
        finally:
            release_picker.set()
            http_server.shutdown()
            http_server.server_close()
            serving_thread.join(timeout=2)


class LibraryStyleImageTests(unittest.TestCase):
    def test_library_style_endpoint_returns_every_direct_image(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            library_root = Path(temporary_directory)
            (library_root / ".imglib.json").write_text("{}", encoding="utf-8")
            style = library_root / "many-images"
            style.mkdir()
            for index in range(35):
                (style / f"image-{index:02d}.png").write_bytes(b"png")
            nested = style / "nested"
            nested.mkdir()
            (nested / "nested.png").write_bytes(b"png")

            handler = server.make_handler(library_root, "task", "start", "test-token")
            http_server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
            serving_thread = threading.Thread(target=http_server.serve_forever, daemon=True)
            serving_thread.start()
            base = f"http://127.0.0.1:{http_server.server_port}"
            discovery = {"status": "found", "source": "scan", "candidates": [library_root]}
            try:
                with patch.object(server, "discover_library", return_value=discovery):
                    with urlopen(f"{base}/library/discover?token=test-token") as response:
                        self.assertEqual(json.load(response)["status"], "found")
                with urlopen(f"{base}/library/images?style=many-images&token=test-token") as response:
                    result = json.load(response)
                manual_query = urlencode({"kind": "style", "directory": str(style), "token": "test-token"})
                with urlopen(f"{base}/scan?{manual_query}") as response:
                    manual_result = json.load(response)
                with urlopen(f"{base}{result['images'][-1]['previewUrl']}") as response:
                    self.assertEqual(response.read(), b"png")
            finally:
                http_server.shutdown()
                http_server.server_close()
                serving_thread.join(timeout=2)

            self.assertEqual(len(result["images"]), 35)
            self.assertFalse(result["truncated"])
            self.assertEqual(result["images"][-1]["name"], "image-34.png")
            self.assertEqual(len(manual_result["images"]), 35)
            self.assertFalse(manual_result["truncated"])


if __name__ == "__main__":
    unittest.main()
