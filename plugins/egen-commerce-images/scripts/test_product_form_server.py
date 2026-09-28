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


if __name__ == "__main__":
    unittest.main()
