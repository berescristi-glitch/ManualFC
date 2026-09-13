import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class Task0503DecisionErrorTests(unittest.TestCase):
    def test_chapter_is_canonical_and_publishable(self):
        text = (ROOT / "content/volume-01/chapter-03.mdx").read_text(encoding="utf-8")
        self.assertIn('chapter_id: "CH-0103"', text)
        self.assertIn("## Ce știm", text)
        self.assertIn("## Ce nu putem concluziona", text)
        self.assertIn("## Verificarea transferului", text)

    def test_claim_chain_is_complete(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        citations = load("research/citations.json")["citations"]
        sources = {x["source_id"] for x in load("research/sources.json")["sources"]}
        for claim_id in ("CLM-0030", "CLM-0031", "CLM-0032", "CLM-0033"):
            claim = claims[claim_id]
            linked = [c for c in citations if c["claim_id"] == claim_id]
            self.assertTrue(linked)
            self.assertTrue(all(c["source_id"] in sources for c in linked))
            self.assertTrue({c["source_id"] for c in linked}.issubset(set(claim["source_ids"])))

    def test_evidence_metadata_and_u11_directness(self):
        claims = {x["claim_id"]: x for x in load("research/claims.json")["claims"]}
        required = {"epistemic_level", "population", "participant_age", "context", "u11_applicability", "limitations", "practical_implication"}
        for claim_id in ("CLM-0030", "CLM-0031", "CLM-0032", "CLM-0033"):
            claim = claims[claim_id]
            self.assertTrue(required.issubset(claim))
            self.assertIn(claim["u11_applicability"], {"DIRECT", "PARTIAL", "INDIRECT"})
            self.assertTrue(claim["limitations"])
            self.assertTrue(claim["practical_implication"])

    def test_error_matrix_distinguishes_intervene_and_retry(self):
        text = (ROOT / "docs/content/CH_0103_ERROR_RESPONSE_MATRIX.md").read_text(encoding="utf-8")
        for marker in ("OPREȘTE ACUM", "CLARIFICĂ ACUM", "MODIFICĂ SARCINA", "MAI LASĂ O ÎNCERCARE", "NU ETICHETA"):
            self.assertIn(marker, text)
        self.assertIn("Nu este test psihologic", text)

    def test_child_language_has_full_foundation(self):
        principle = load("data/principles/principle-eroarea-ca-informatie.json")
        self.assertEqual(principle["child_message"], "Spune-mi ce ai văzut. Apoi încearcă din nou.")
        for key in ("coach_meaning", "why_this_message", "information_children_must_notice", "decision_children_must_learn", "understanding_check", "response_if_not_understood", "match_transfer"):
            self.assertTrue(principle[key])
        self.assertEqual(set(principle["rationales"]), {"tactical", "perceptual", "decisional", "cognitive", "psychological", "technical", "social"})

    def test_dossier_declares_non_support_and_open_questions(self):
        text = (ROOT / "research/dossiers/ch-0103-decision-error.md").read_text(encoding="utf-8")
        for section in ("## What the evidence supports", "## What the evidence does NOT support", "## U11 applicability", "## Limitations", "## Open questions", "## Citation map"):
            self.assertIn(section, text)

    def test_separate_audits_exist(self):
        factual = ROOT / "reports/audits/TASK-0503-factual-pedagogical-audit.md"
        editorial = ROOT / "reports/audits/TASK-0503-editorial-audit.md"
        self.assertTrue(factual.exists())
        self.assertTrue(editorial.exists())
        self.assertIn("PASS", factual.read_text(encoding="utf-8"))
        self.assertIn("PASS", editorial.read_text(encoding="utf-8"))

    def test_no_visual_files_declared_in_task_outputs(self):
        registry = load("TASK_REGISTRY.json")
        task = next(t for t in registry["tasks"] if t["task_id"] == "TASK-0503")
        self.assertEqual(task["outputs"], ["content/volume-01/chapter-03.mdx", "reports/task-reports/TASK-0503.md"])


if __name__ == "__main__":
    unittest.main()
