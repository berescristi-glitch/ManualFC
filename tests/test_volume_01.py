import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class Volume01Tests(unittest.TestCase):
    def test_01_volume_01_manifest_valid(self):
        manifest_file = ROOT_DIR / "data" / "content" / "volumes" / "volume-01.json"
        self.assertTrue(manifest_file.exists(), "Manifestul volume-01.json nu există.")
        with open(manifest_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("schema_version"), "1.0.0")
        self.assertEqual(data.get("volume_id"), "VOLUME-01")
        self.assertIn("chapter_order", data)
        self.assertEqual(len(data["chapter_order"]), 10)
        self.assertEqual(len(data["chapters"]), 10)

        chapter_ids = [ch["chapter_id"] for ch in data["chapters"]]
        self.assertEqual(len(set(chapter_ids)), 10, "ID-urile capitolelor trebuie să fie unice.")
        self.assertEqual(data["chapter_order"], chapter_ids, "Ordinea capitolelor trebuie să corespundă.")

    def test_02_volume_01_architecture_doc_exists(self):
        arch_file = ROOT_DIR / "docs" / "content" / "VOLUME_01_ARCHITECTURE.md"
        self.assertTrue(arch_file.exists())
        content = arch_file.read_text(encoding="utf-8")
        self.assertIn("CH-0101", content)
        self.assertIn("CH-0102", content)
        self.assertIn("CH-0103", content)
        self.assertIn("CH-0104", content)
        self.assertIn("CH-0105", content)
        self.assertIn("WHAT WE CANNOT CONCLUDE", content)

    def test_03_chapter_template_exists(self):
        template_file = ROOT_DIR / "docs" / "content" / "CHAPTER_PRODUCTION_TEMPLATE.md"
        self.assertTrue(template_file.exists())
        content = template_file.read_text(encoding="utf-8")
        self.assertIn("WHAT WE CANNOT CONCLUDE", content)
        self.assertIn("child_wording", content)

    def test_04_regulations_recheck_dossier_exists(self):
        dossier = ROOT_DIR / "research" / "dossiers" / "regulations-u11-recheck.md"
        self.assertTrue(dossier.exists())

if __name__ == "__main__":
    unittest.main()
