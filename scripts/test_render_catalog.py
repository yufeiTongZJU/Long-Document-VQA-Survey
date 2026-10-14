"""Check local maintenance without access to the external manuscript."""

import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from render_catalog import render, validate_catalog

ROOT = Path(__file__).resolve().parents[1]


class RenderTests(unittest.TestCase):
    def test_existing_snapshot_renders_byte_identically(self):
        outputs, _ = render(ROOT)
        for relative, content in outputs.items():
            self.assertEqual(content, (ROOT / relative).read_bytes(), relative)

    def test_json_edit_changes_views_without_rewriting_source_provenance(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for directory in ("data", "papers"):
                shutil.copytree(ROOT / directory, root / directory)
            for name in ("references.bib", "reference_sources.json"):
                shutil.copyfile(ROOT / name, root / name)
            original_manifest = json.loads((root / "data/source_manifest.json").read_text("utf-8"))
            catalog_path = root / "data/direct-reading.json"
            catalog = json.loads(catalog_path.read_text("utf-8"))
            catalog["records"][0]["name"] += " (test correction)"
            catalog_path.write_text(json.dumps(catalog, ensure_ascii=False), encoding="utf-8")
            edited_bytes = catalog_path.read_bytes()
            outputs, _ = render(root)
            self.assertIn(b"(test correction)", outputs["papers/direct-reading.md"])
            self.assertIn(b"(test correction)", outputs["data/direct-reading.csv"])
            updated_manifest = json.loads(outputs["data/source_manifest.json"])
            self.assertEqual(original_manifest["sources"], updated_manifest["sources"])
            self.assertNotEqual(original_manifest["generated"], updated_manifest["generated"])
            self.assertEqual(edited_bytes, catalog_path.read_bytes())
            self.assertNotIn("data/direct-reading.json", outputs)
            self.assertNotIn("data/validation.json", outputs)

    def test_invalid_counts_groups_ids_and_citations_are_rejected(self):
        catalog = json.loads((ROOT / "data/direct-reading.json").read_text("utf-8"))
        bibliography = json.loads((ROOT / "data/bibliography.json").read_text("utf-8"))
        entries = {entry["citekey"]: entry for entry in bibliography["records"]}
        for error in ("count", "group", "id", "citekey"):
            with self.subTest(error=error):
                invalid = copy.deepcopy(catalog)
                if error == "count":
                    invalid["record_count"] += 1
                elif error == "group":
                    invalid["records"][0]["group"] = "Unexpected group"
                elif error == "id":
                    invalid["records"][1]["id"] = invalid["records"][0]["id"]
                else:
                    invalid["records"][0]["citekey"] = "missing-citation"
                with self.assertRaises(ValueError):
                    validate_catalog(invalid, "direct-reading", entries)


if __name__ == "__main__":
    unittest.main()
