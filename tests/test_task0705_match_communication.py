import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0705Tests(unittest.TestCase):
    def test_chapter_publishable(self):
        text = (ROOT / "content/volume-03/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0305"', text)
        self.assertGreater(len(text), 6000)
        for marker in ("Ce știm din cercetare", "Ce le spun și de ce", "Transferul în meci", "Ce nu putem concluziona"):
            self.assertIn(marker, text)

    def test_no_fabricated_ford_2012_source(self):
        text = (ROOT / "content/volume-03/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertNotIn("Ford et al. 2012", text)
        self.assertNotIn("Ford et al. (2012)", text)

    def test_avoids_both_dogmas(self):
        text = (ROOT / "content/volume-03/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("nu este susținută ca superioară", text)
        self.assertIn("Nu putem concluziona că orice comunicare de pe margine e dăunătoare", text)

    def test_joystick_coaching_framed_as_vernacular(self):
        text = (ROOT / "content/volume-03/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("nu este un rezultat de cercetare", text)
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0088"]["claim_type"], "METHODOLOGICAL_SYNTHESIS")

    def test_old_claim_replaced_not_silently_dropped(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0057"]["status"], "REPLACED")
        self.assertEqual(claims["CLM-0057"]["replacement_claim_id"], "CLM-0088")
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        self.assertTrue(sources["SRC-0056"]["withdrawn"])

    def test_claim_chain_and_no_withdrawn_source_in_use(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0084", "CLM-0085", "CLM-0086", "CLM-0087", "CLM-0088"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-tacet-si-observa-fara-joystick.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-tacet-si-observa-fara-joystick.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0305_MATCH_COMMUNICATION_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
