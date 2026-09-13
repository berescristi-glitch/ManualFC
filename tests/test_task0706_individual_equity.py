import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0706Tests(unittest.TestCase):
    def test_chapter_mdx_exists_and_contains_pedagogical_loop(self):
        path = ROOT / "content/volume-03/chapter-06.mdx"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0306"', text)
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "verificare", "înțelegerii", "Transferul în joc"):
            self.assertIn(marker.lower(), text.lower())

    def test_no_unsupported_hard_number_presented_as_evidence(self):
        text = (ROOT / "content/volume-03/chapter-06.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0306_INDIVIDUAL_CONVERSATIONS_CARD.md").read_text(encoding="utf-8")
        self.assertIn("euristică practică ManualFC", text)
        self.assertIn("euristică practică ManualFC", card)
        self.assertNotIn("15 secunde", card)
        self.assertNotIn("30 secunde", card)

    def test_theoretical_model_not_overclaimed_as_empirical(self):
        text = (ROOT / "content/volume-03/chapter-06.mdx").read_text(encoding="utf-8")
        self.assertIn("model teoretic", text.lower())
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        clm = claims["CLM-0058"]
        self.assertEqual(clm["claim_type"], "CONSENSUS")
        self.assertEqual(clm["epistemic_level"], "MODERATE")
        self.assertEqual(clm["u11_applicability"], "PARTIAL")

    def test_claim_chain_and_no_withdrawn_source(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        clm = claims["CLM-0058"]
        self.assertEqual(clm["status"], "VERIFIED")
        self.assertTrue([c for c in citations if c["claim_id"] == "CLM-0058"])
        for sid in clm["source_ids"]:
            self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by CLM-0058")
        principle = load("data/principles/principle-conversatii-individuale-si-echitate.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-conversatii-individuale-si-echitate.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0306_INDIVIDUAL_CONVERSATIONS_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
