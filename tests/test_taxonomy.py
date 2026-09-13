import json
import unittest
from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parents[1]

class TaxonomyTests(unittest.TestCase):
    def test_01_taxonomy_registry_valid(self):
        reg_file = ROOT_DIR / "data" / "taxonomy" / "registry.json"
        self.assertTrue(reg_file.exists())
        with open(reg_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertEqual(data.get("schema_version"), "1.0.0")
        self.assertIn("categories", data)
        self.assertEqual(len(data["categories"]), 16)
        self.assertIn("entity_classes", data)
        self.assertEqual(len(data["entity_classes"]), 5)
        self.assertIn("entity_contracts", data)

    def test_02_slug_contract_ascii_kebab_case(self):
        reg_file = ROOT_DIR / "data" / "taxonomy" / "registry.json"
        with open(reg_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        slug_pattern = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
        for cat in data["categories"]:
            slug = cat["slug"]
            self.assertTrue(slug_pattern.match(slug), f"Slug-ul de categorie {slug} nu este lowercase ASCII kebab-case.")

    def test_03_development_fixtures_marked(self):
        fixtures_dir = ROOT_DIR / "data" / "fixtures"
        for name in ["principles.json", "exercises.json", "problems.json"]:
            path = fixtures_dir / name
            self.assertTrue(path.exists(), f"Fișierul fixture {name} nu există.")
            with open(path, "r", encoding="utf-8") as f:
                items = json.load(f)
            self.assertTrue(len(items) > 0)
            for item in items:
                self.assertTrue(item.get("development_fixture"), f"Elementul {item.get('id')} din {name} nu are development_fixture: true.")
                self.assertEqual(item.get("fixture_type"), "DEVELOPMENT FIXTURE")

    def test_04_problem_semantic_separation(self):
        prob_file = ROOT_DIR / "data" / "fixtures" / "problems.json"
        with open(prob_file, "r", encoding="utf-8") as f:
            items = json.load(f)
        for prob in items:
            self.assertIn("observation", prob)
            self.assertIn("possible_causes", prob)
            self.assertIn("intervention", prob)
            interv = prob["intervention"]
            self.assertIn("things_to_check", interv)
            self.assertIn("what_to_say", interv)
            self.assertIn("why_explanation", interv)
            self.assertIn("exercise_ids", interv)

    def test_05_dynamic_routes_exist(self):
        pages_dir = ROOT_DIR / "app" / "src" / "pages"
        internal_dir = ROOT_DIR / "app" / "src" / "internal-pages"
        self.assertTrue((pages_dir / "principii" / "[slug].astro").exists())
        self.assertTrue((internal_dir / "probleme" / "[slug].astro").exists())
        self.assertTrue((internal_dir / "exercitii" / "[slug].astro").exists())
        self.assertFalse((pages_dir / "probleme" / "[slug].astro").exists())
        self.assertFalse((pages_dir / "exercitii" / "[slug].astro").exists())

if __name__ == "__main__":
    unittest.main()
