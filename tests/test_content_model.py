import json
import unittest
from pathlib import Path
import subprocess

ROOT_DIR = Path(__file__).resolve().parents[1]

class ContentModelTests(unittest.TestCase):
    def test_01_content_model_ts_exists_and_has_branded_types(self):
        ts_file = ROOT_DIR / "app" / "src" / "types" / "content-model.ts"
        self.assertTrue(ts_file.exists())
        content = ts_file.read_text(encoding="utf-8")
        self.assertIn("type CanonicalId = string &", content)
        self.assertIn("type EntitySlug = string &", content)
        self.assertIn("parseCanonicalId", content)
        self.assertIn("parseEntitySlug", content)
        self.assertIn("parseObservation", content)
        self.assertIn("parsePossibleCause", content)

    def test_02_json_boundary_file_exists(self):
        boundary = ROOT_DIR / "app" / "src" / "lib" / "json-boundary.ts"
        self.assertTrue(boundary.exists())
        content = boundary.read_text(encoding="utf-8")
        self.assertIn("validateAndParsePrinciple", content)
        self.assertIn("validateAndParseExercise", content)
        self.assertIn("validateAndParseProblem", content)

    def test_03_content_bridge_target_type_checking(self):
        bridge = ROOT_DIR / "app" / "src" / "lib" / "content-bridge.ts"
        self.assertTrue(bridge.exists())
        content = bridge.read_text(encoding="utf-8")
        self.assertIn("Expected entity type", content)
        self.assertIn("getCanonicalProductionContent", content)
        self.assertIn("getDevelopmentFixtures", content)

    def test_04_problem_semantic_types_in_fixtures(self):
        prob_file = ROOT_DIR / "data" / "fixtures" / "problems.json"
        with open(prob_file, "r", encoding="utf-8") as f:
            probs = json.load(f)
        for p in probs:
            self.assertTrue(isinstance(p.get("observation"), str))
            self.assertTrue(len(p.get("observation")) > 0)
            self.assertTrue(isinstance(p.get("possible_causes"), list))
            self.assertTrue(len(p.get("possible_causes")) > 0)
            self.assertIn("intervention", p)

    def test_05_claims_and_sources_real_ids_compatibility(self):
        claims_file = ROOT_DIR / "research" / "claims.json"
        with open(claims_file, "r", encoding="utf-8") as f:
            claims_data = json.load(f)
        for claim in claims_data.get("claims", []):
            cid = claim.get("claim_id")
            self.assertTrue(cid.startswith("CLM-"), f"ID de claim invalid: {cid}")

if __name__ == "__main__":
    unittest.main()
