import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0805Tests(unittest.TestCase):
    def test_chapter_mdx_exists_and_contains_pedagogical_loop(self):
        path = ROOT / "content/volume-04/chapter-05.mdx"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0405"', text)
        for marker in ("Formularea exactă", "Tactic", "Perceptiv", "Psihologic", "verificare", "înțelegerii", "Transferul în joc"):
            self.assertIn(marker.lower(), text.lower())

    def test_no_fabricated_scaglia_source_or_threshold(self):
        text = (ROOT / "content/volume-04/chapter-05.mdx").read_text(encoding="utf-8")
        card = (ROOT / "docs/content/CH_0405_ACTIVE_TIME_ORGANIZATION_CARD.md").read_text(encoding="utf-8")
        self.assertNotIn("Scaglia et al. 2021", text)
        for bad in ("peste 70%", "63 minute", "sub 10 secunde", "sub 3 secunde"):
            self.assertNotIn(bad, text)
            self.assertNotIn(bad, card)

    def test_three_separate_evidence_domains_present(self):
        text = (ROOT / "content/volume-04/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("**Timp activ.**", text)
        self.assertIn("**Organizare și rotații.**", text)
        self.assertIn("**Siguranță.**", text)

    def test_safety_uses_quantified_official_source(self):
        text = (ROOT / "content/volume-04/chapter-05.mdx").read_text(encoding="utf-8")
        self.assertIn("48%", text)
        self.assertIn("FIFA 11+ Kids", text)
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0097"]["epistemic_level"], "HIGH")
        self.assertEqual(claims["CLM-0097"]["u11_applicability"], "DIRECT")

    def test_organization_domain_honest_about_thin_evidence(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0096"]["epistemic_level"], "LOW")

    def test_old_claim_replaced_not_silently_dropped(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        self.assertEqual(claims["CLM-0063"]["status"], "REPLACED")
        self.assertEqual(claims["CLM-0063"]["replacement_claim_id"], "CLM-0095")
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        self.assertTrue(sources["SRC-0062"]["withdrawn"])

    def test_claim_chain_and_no_withdrawn_source_in_use(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {s["source_id"]: s for s in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0095", "CLM-0096", "CLM-0097", "CLM-0098"):
            self.assertEqual(claims[claim_id]["status"], "VERIFIED")
            self.assertTrue([c for c in citations if c["claim_id"] == claim_id])
            for sid in claims[claim_id]["source_ids"]:
                self.assertFalse(sources[sid]["withdrawn"], f"{sid} is withdrawn but still cited by {claim_id}")
        principle = load("data/principles/principle-maximizarea-timpului-activ-si-organizarea-sigura.json")
        withdrawn_ids = {s["source_id"] for s in load("research/sources.json")["sources"] if s["withdrawn"]}
        for sid in principle["sources"]:
            self.assertNotIn(sid, withdrawn_ids)

    def test_principle_json_exists(self):
        path = ROOT / "data/principles/principle-maximizarea-timpului-activ-si-organizarea-sigura.json"
        self.assertTrue(path.exists())

    def test_field_tool_card_exists(self):
        path = ROOT / "docs/content/CH_0405_ACTIVE_TIME_ORGANIZATION_CARD.md"
        self.assertTrue(path.exists())


if __name__ == "__main__":
    unittest.main()
