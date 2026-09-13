import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class CH0101Batch1Tests(unittest.TestCase):
    def test_01_canonical_principle_file_exists_and_valid(self):
        principle_file = ROOT_DIR / "data" / "principles" / "principle-variabilitatea-dezvoltarii-u11.json"
        self.assertTrue(principle_file.exists(), "Fișierul principiu canonic nu există.")
        with open(principle_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("id"), "principle.variabilitatea-dezvoltarii-u11")
        self.assertEqual(data.get("slug"), "variabilitatea-dezvoltarii-u11")
        self.assertFalse(data.get("development_fixture"), "Entitatea de conținut canonic nu trebuie să fie marked ca fixture.")
        self.assertIn("CLM-0022", data.get("evidence_claim_ids", []))

    def test_02_research_dossier_exists(self):
        dossier = ROOT_DIR / "research" / "dossiers" / "ch-0101-development-variability.md"
        self.assertTrue(dossier.exists())
        content = dossier.read_text(encoding="utf-8")
        self.assertIn("RQ-0501-01", content)
        self.assertIn("LIMITATIONS", content)

    def test_03_sources_and_claims_registered(self):
        sources_file = ROOT_DIR / "research" / "sources.json"
        with open(sources_file, "r", encoding="utf-8") as f:
            sources_data = json.load(f)
        source_ids = [s["source_id"] for s in sources_data.get("sources", [])]
        self.assertIn("SRC-0021", source_ids)
        self.assertIn("SRC-0024", source_ids)

        claims_file = ROOT_DIR / "research" / "claims.json"
        with open(claims_file, "r", encoding="utf-8") as f:
            claims_data = json.load(f)
        claim_ids = [c["claim_id"] for c in claims_data.get("claims", [])]
        self.assertIn("CLM-0022", claim_ids)
        self.assertIn("CLM-0025", claim_ids)

    def test_04_claim_citation_source_chain_and_metadata(self):
        principle = json.loads((ROOT_DIR / "data/principles/principle-variabilitatea-dezvoltarii-u11.json").read_text(encoding="utf-8"))
        claims = {item["claim_id"]: item for item in json.loads((ROOT_DIR / "research/claims.json").read_text(encoding="utf-8"))["claims"]}
        citations = json.loads((ROOT_DIR / "research/citations.json").read_text(encoding="utf-8"))["citations"]
        sources = {item["source_id"] for item in json.loads((ROOT_DIR / "research/sources.json").read_text(encoding="utf-8"))["sources"]}
        required = {"epistemic_level", "population", "participant_age", "context", "u11_applicability", "limitations", "practical_implication"}
        for claim_id in principle["evidence_claim_ids"]:
            claim = claims[claim_id]
            self.assertTrue(required <= claim.keys())
            linked = [item for item in citations if item["claim_id"] == claim_id]
            self.assertTrue(linked, claim_id)
            self.assertTrue(all(item["source_id"] in sources for item in linked))
            self.assertTrue(all(item["source_id"] in claim["source_ids"] for item in linked))

    def test_05_web_template_resolves_canonical_evidence(self):
        page = (ROOT_DIR / "app/src/pages/principii/[slug].astro").read_text(encoding="utf-8")
        bridge = (ROOT_DIR / "app/src/lib/content-bridge.ts").read_text(encoding="utf-8")
        self.assertIn("resolveEvidenceClaims(principle)", page)
        self.assertNotIn('level="HIGH"', page)
        self.assertNotIn("CLM-001", page)
        self.assertIn("research/claims.json", bridge)
        self.assertIn("research/citations.json", bridge)
        self.assertIn("research/sources.json", bridge)

if __name__ == "__main__":
    unittest.main()
