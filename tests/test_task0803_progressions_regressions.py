import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0803Tests(unittest.TestCase):
    def test_chapter_mdx_exists_and_contains_pedagogical_loop(self):
        path = ROOT / "content/volume-04/chapter-03.mdx"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0403"', text)
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "verificare", "înțelegerii", "Transferul în joc"):
            self.assertIn(marker.lower(), text.lower())

    def test_no_fabricated_passos_2016_source(self):
        text = (ROOT / "content/volume-04/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertNotIn("Passos et al. 2016", text)
        self.assertNotIn("Passos et al. (2016)", text)

    def test_no_unsupported_success_rate_threshold(self):
        text = (ROOT / "content/volume-04/chapter-03.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0403_PROGRESSION_REGRESSION_CARD.md").read_text(encoding="utf-8")
        principle = load("data/principles/principle-progresie-si-regresie-cu-conservarea-intentiei.json")
        for bad in ("< 50%", "sub 50%", "> 80%", "peste 80%", "Rată de succes"):
            self.assertNotIn(bad, card)
        self.assertNotIn("70%", " ".join(principle["task_risks"]))
        self.assertIn("nu există un prag procentual de rată de succes validat științific", text.lower())

    def test_old_claim_replaced_not_silently_dropped(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0061"]["status"], "REPLACED")
        self.assertEqual(claims["CLM-0061"]["replacement_claim_id"], "CLM-0093")
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        self.assertTrue(sources["SRC-0060"]["withdrawn"])

    def test_claim_chain_and_no_withdrawn_source_in_use(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0092", "CLM-0093"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-progresie-si-regresie-cu-conservarea-intentiei.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-progresie-si-regresie-cu-conservarea-intentiei.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0403_PROGRESSION_REGRESSION_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
