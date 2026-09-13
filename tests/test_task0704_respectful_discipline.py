import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0704Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-03/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0304"', text)
        self.assertGreater(len(text), 6500)
        for marker in ("Ce știm din cercetare", "Ce le spun și de ce", "Transferul în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_three_layer_separation_present(self):
        text = (ROOT / "content/volume-03/chapter-04.mdx").read_text(encoding="utf-8")
        self.assertIn("Trei straturi, nu unul", text)
        self.assertIn("cerința de safeguarding", text.lower())
        self.assertIn("euristică practică ManualFC", text)

    def test_logical_consequences_not_overclaimed(self):
        text = (ROOT / "content/volume-03/chapter-04.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0304_RESPECTFUL_DISCIPLINE_CARD.md").read_text(encoding="utf-8")
        self.assertIn("nascentă", text)
        self.assertIn("nu prezintă „consecințele logice” ca metodă validată științific", text)
        self.assertIn("nevalidată", card.lower())

    def test_claim_chain_and_no_withdrawn_source(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0078", "CLM-0079", "CLM-0080", "CLM-0081", "CLM-0082", "CLM-0083"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-disciplina-fara-umilire.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_no_unsupported_time_number(self):
        card = (ROOT / "docs/content/CH_0304_RESPECTFUL_DISCIPLINE_CARD.md").read_text(encoding="utf-8")
        principle = load("data/principles/principle-disciplina-fara-umilire.json")
        for bad in ("1-2 minute", "1–2 minute", "de 1 minut"):
            self.assertNotIn(bad, card)
            self.assertNotIn(bad, " ".join(principle["response_if_not_understood"]))

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-disciplina-fara-umilire.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0304_RESPECTFUL_DISCIPLINE_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
