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
    def test_resolves_only_selected_material_ids_for_each_output(self) -> None:
        payload = {
            "taskOptions": {"styleSource": "customer-reference"},
            "referenceWorkflow": {
                "colorMasterId": "style-1",
                "outputs": [
                    {
                        "name": "晨光场景",
                        "productImageIds": ["product-1", "product-2"],
                        "styleReferenceId": "style-1",
                        "ratioOverride": "",
                    }
                ],
            },
        }
        material_catalog = {
            "product-1": {"kind": "product", "name": "front.jpg", "path": "C:/product/front.jpg"},
            "product-2": {"kind": "product", "name": "side.jpg", "path": "C:/product/side.jpg"},
            "style-1": {"kind": "style", "name": "scene.jpg", "path": "C:/style/scene.jpg"},
        }

        resolved = server.resolve_customer_reference_workflow(payload, material_catalog)

        output = resolved["referenceWorkflow"]["outputs"][0]
        self.assertEqual(output["productImagePaths"], ["C:/product/front.jpg", "C:/product/side.jpg"])
        self.assertEqual(output["styleReferencePath"], "C:/style/scene.jpg")
        self.assertEqual(resolved["referenceWorkflow"]["colorMasterPath"], "C:/style/scene.jpg")

    def test_rejects_more_than_four_product_images_for_an_output(self) -> None:
        payload = {
            "taskOptions": {"styleSource": "customer-reference"},
            "referenceWorkflow": {
                "colorMasterId": "style-1",
                "outputs": [
                    {
                        "name": "过多产品图",
                        "productImageIds": ["p1", "p2", "p3", "p4", "p5"],
                        "styleReferenceId": "style-1",
                    }
                ],
            },
        }
        material_catalog = {
            **{
                f"p{index}": {"kind": "product", "name": f"{index}.jpg", "path": f"C:/{index}.jpg"}
                for index in range(1, 6)
            },
            "style-1": {"kind": "style", "name": "scene.jpg", "path": "C:/style/scene.jpg"},
        }

        with self.assertRaises(ValueError):
            server.resolve_customer_reference_workflow(payload, material_catalog)


if __name__ == "__main__":
    unittest.main()
