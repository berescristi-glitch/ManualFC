import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class CH0101Batch2Tests(unittest.TestCase):
    CLAIM_IDS = {"CLM-0026", "CLM-0027", "CLM-0028", "CLM-0029"}

    def test_01_canonical_principle_adaptare_exists_and_valid(self):
        principle_file = ROOT_DIR / "data" / "principles" / "principle-adaptarea-sarcinii-u11.json"
        self.assertTrue(principle_file.exists(), "Fișierul principiu canonic pentru Batch 2 nu există.")
        with open(principle_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("id"), "principle.adaptarea-sarcinii-u11")
        self.assertEqual(data.get("slug"), "adaptarea-sarcinii-u11")
        self.assertEqual(data.get("category_id"), "cat.copilul-10-11")
        self.assertIn("CLM-0026", data.get("evidence_claim_ids", []))
        self.assertIn("CLM-0029", data.get("evidence_claim_ids", []))

    def test_02_task_adaptation_scale_resource_exists(self):
        resource = ROOT_DIR / "docs" / "content" / "CH_0101_TASK_ADAPTATION_SCALE.md"
        self.assertTrue(resource.exists())
        content = resource.read_text(encoding="utf-8")
        self.assertIn("Scara de Adaptare a Sarcinii", content)
        self.assertIn("Modelul Decizional al Antrenorului", content)
        self.assertIn("Quick Field Card", content)

    def test_03_research_dossier_batch2_exists(self):
        dossier = ROOT_DIR / "research" / "dossiers" / "ch-0101-motor-competence.md"
        self.assertTrue(dossier.exists())
        content = dossier.read_text(encoding="utf-8")
        self.assertIn("RQ-0507", content)
        self.assertIn("LIMITATIONS", content)

    def test_04_new_sources_and_claims_registered(self):
        sources_file = ROOT_DIR / "research" / "sources.json"
        with open(sources_file, "r", encoding="utf-8") as f:
            sources_data = json.load(f)
        source_ids = [s["source_id"] for s in sources_data.get("sources", [])]
        self.assertIn("SRC-0025", source_ids)
        self.assertIn("SRC-0028", source_ids)

        claims_file = ROOT_DIR / "research" / "claims.json"
        with open(claims_file, "r", encoding="utf-8") as f:
            claims_data = json.load(f)
        claim_ids = [c["claim_id"] for c in claims_data.get("claims", [])]
        self.assertIn("CLM-0026", claim_ids)
        self.assertIn("CLM-0029", claim_ids)

    def test_05_claim_citation_source_chain_and_metadata(self):
        principle = json.loads((ROOT_DIR / "data/principles/principle-adaptarea-sarcinii-u11.json").read_text(encoding="utf-8"))
        claims = {item["claim_id"]: item for item in json.loads((ROOT_DIR / "research/claims.json").read_text(encoding="utf-8"))["claims"]}
        citations = json.loads((ROOT_DIR / "research/citations.json").read_text(encoding="utf-8"))["citations"]
        sources = {item["source_id"] for item in json.loads((ROOT_DIR / "research/sources.json").read_text(encoding="utf-8"))["sources"]}
        required = {"epistemic_level", "population", "participant_age", "context", "u11_applicability", "limitations", "practical_implication"}
        self.assertEqual(set(principle["evidence_claim_ids"]), self.CLAIM_IDS)
        for claim_id in self.CLAIM_IDS:
            claim = claims[claim_id]
            self.assertTrue(required <= claim.keys(), claim_id)
            self.assertIn(claim["u11_applicability"], {"DIRECT", "PARTIAL", "INDIRECT"})
            self.assertTrue(claim["limitations"], claim_id)
            self.assertTrue(claim["practical_implication"].strip(), claim_id)
            linked = [item for item in citations if item["claim_id"] == claim_id]
            self.assertTrue(linked, claim_id)
            self.assertEqual({item["source_id"] for item in linked}, set(claim["source_ids"]))
            self.assertTrue(all(item["source_id"] in sources for item in linked))

    def test_06_no_unsupported_high_or_direct_u11_claims(self):
        claims = {item["claim_id"]: item for item in json.loads((ROOT_DIR / "research/claims.json").read_text(encoding="utf-8"))["claims"]}
        for claim_id in self.CLAIM_IDS:
            self.assertNotEqual(claims[claim_id]["epistemic_level"], "HIGH")
            self.assertNotEqual(claims[claim_id]["u11_applicability"], "DIRECT")

    def test_07_report_matches_real_registry_task(self):
        registry = json.loads((ROOT_DIR / "TASK_REGISTRY.json").read_text(encoding="utf-8"))
        task = next(item for item in registry["tasks"] if item["task_id"] == "TASK-0502")
        report = (ROOT_DIR / "reports/task-reports/TASK-0502.md").read_text(encoding="utf-8")
        self.assertIn(task["title"], report)
        self.assertIn("content/volume-01/chapter-02.mdx", report)

    def test_08_practical_output_is_non_diagnostic_and_single_variable(self):
        content = (ROOT_DIR / "docs/content/CH_0101_TASK_ADAPTATION_SCALE.md").read_text(encoding="utf-8")
        self.assertIn("MODIFICĂ O SINGURĂ VARIABILĂ", content)
        self.assertIn("nu test diagnostic", content)
        self.assertNotIn("Nivel Evidență / Sursă", content)

if __name__ == "__main__":
    unittest.main()
