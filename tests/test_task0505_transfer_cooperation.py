import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
load = lambda p: json.loads((ROOT / p).read_text(encoding="utf-8"))


class Task0505Tests(unittest.TestCase):
    def test_chapter_reconciles_architecture_and_registry(self):
        text = (ROOT / "content/volume-01/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0105"', text)
        for term in ("transfer", "Cooperarea", "Apartenența", "Diferențiere"):
            self.assertIn(term, text)

    def test_claim_chains_and_limits(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {x["source_id"] for x in load("research/sources.json")["sources"]}
        for cid in ("CLM-0036", "CLM-0037"):
            links = [x for x in citations if x["claim_id"] == cid]
            self.assertTrue(links and claims[cid]["limitations"])
            self.assertIn(claims[cid]["u11_applicability"], {"PARTIAL", "INDIRECT"})
            self.assertTrue(all(x["source_id"] in sources for x in links))

    def test_grid_separates_opportunity_from_behavior(self):
        text = (ROOT / "docs/content/CH_0105_MATCH_TRANSFER_GRID.md").read_text(encoding="utf-8")
        for level in ("NO_OPPORTUNITY", "PROMPTED", "EMERGING", "AUTONOMOUS", "ADAPTIVE"):
            self.assertIn(level, text)
        self.assertIn("nu produce un scor de talent", text)

    def test_cooperation_is_observable(self):
        p = load("data/principles/principle-transfer-autonom-cooperare.json")
        self.assertIn("opțiune", p["child_message"])
        self.assertGreaterEqual(len(p["observable_behaviours"]), 4)
        self.assertTrue(p["understanding_check"] and p["match_transfer"])
        self.assertEqual(len(p["rationales"]), 7)

    def test_dossier_declares_no_tactical_transfer_evidence(self):
        text = (ROOT / "research/dossiers/ch-0105-transfer-cooperation.md").read_text(encoding="utf-8")
        self.assertIn("Fluența într-un exercițiu nu dovedește transfer", text)
        self.assertIn("Citation map", text)

    def test_audits_are_separate(self):
        self.assertTrue((ROOT / "reports/audits/TASK-0505-factual-pedagogical-audit.md").exists())
        self.assertTrue((ROOT / "reports/audits/TASK-0505-editorial-audit.md").exists())

    def test_field_tool_is_non_diagnostic(self):
        text = (ROOT / "docs/content/CH_0105_MATCH_TRANSFER_GRID.md").read_text(encoding="utf-8")
        for forbidden in ("caracter", "apartenență"):
            self.assertIn(forbidden, text)


if __name__ == "__main__":
    unittest.main()
