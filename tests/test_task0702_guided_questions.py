import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class Task0702Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-03/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0302"', text)
        self.assertGreater(len(text), 6000)
        for marker in ("Ce știm din cercetare", "Ce le spun și de ce", "Transferul în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_illusion_of_understanding_present(self):
        text = (ROOT / "content/volume-03/chapter-02.mdx").read_text(encoding="utf-8")
        self.assertIn("nu-și detectează fiabil propria neînțelegere", text)
        self.assertIn("supraîncrezători", text)
        self.assertIn('Renunță la „Ați înțeles?”', text)

    def test_claim_chain_and_no_withdrawn_source(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0069", "CLM-0070", "CLM-0071", "CLM-0072"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-intrebari-si-verificarea-intelegerii.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_behaviour_not_verbal_confirmation(self):
        text = (ROOT / "content/volume-03/chapter-02.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0302_GUIDED_QUESTIONING_CARD.md").read_text(encoding="utf-8")
        self.assertIn("comportament", text.lower())
        self.assertIn('nu accepta „da, am înțeles” ca răspuns final'.lower(), card.lower())

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-intrebari-si-verificarea-intelegerii.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0302_GUIDED_QUESTIONING_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
