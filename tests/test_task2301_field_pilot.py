import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHEET = ROOT / "docs/field-pilot/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_SHEET_R1.md"
TEMPLATE = ROOT / "docs/field-pilot/PHASE23_FIELD_RETURN_TEMPLATE_R1.md"


class Task2301FieldPilotTests(unittest.TestCase):
    def test_field_sheet_exists(self):
        self.assertTrue(SHEET.exists())

    def test_return_template_exists(self):
        self.assertTrue(TEMPLATE.exists())

    def test_field_sheet_scoped_to_round1_slice_only(self):
        text = SHEET.read_text(encoding="utf-8")
        for ex_id in ("EX-0001", "EX-0002", "EX-0003", "SES-0001"):
            self.assertIn(ex_id, text)
        # SES-0002 is a later round entirely; not referenced at all in Round 1.
        self.assertNotIn("SES-0002", text)
        # EX-0004/EX-0005 may only appear once, in the explicit C4/C5 deferral note.
        self.assertEqual(text.count("EX-0004"), 1)
        self.assertEqual(text.count("EX-0005"), 1)

    def test_field_sheet_no_research_jargon(self):
        text = SHEET.read_text(encoding="utf-8")
        for token in ("SRC-", "CLM-", "CIT-", "RQ-", "epistemic"):
            self.assertNotIn(token, text)

    def test_field_sheet_defers_asm0001_c4_c5(self):
        text = SHEET.read_text(encoding="utf-8")
        self.assertIn("C4", text)
        self.assertIn("nu se evaluează în Runda 1", text)

    def test_field_sheet_does_not_modify_asm0001(self):
        text = SHEET.read_text(encoding="utf-8")
        self.assertIn("Nu modifica ASM-0001", text)

    def test_field_sheet_contains_no_fabricated_results(self):
        text = SHEET.read_text(encoding="utf-8").lower()
        forbidden = [
            "toți copiii au reușit", "copilul a spus", "s-a observat că",
            "rezultatele arată", "100% dintre copii", "pilotarea a confirmat",
        ]
        for phrase in forbidden:
            self.assertNotIn(phrase, text)

    def test_field_sheet_explicit_no_assumption_rule(self):
        text = SHEET.read_text(encoding="utf-8")
        self.assertIn("nu completa cu presupuneri", text)

    def test_return_template_covers_required_sections(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        for section in (
            "## CONTEXT", "## PRE-SEDINTA", "## OBSERVATII EXERCITIU",
            "## LIMBAJ PENTRU COPIL", "## QUICK MODE", "## INSTRUMENTE DE TEREN",
            "## TRANZITII", "## LOGICA SEDINTEI", "## TRANSFER", "## ASM-0001",
            "## REVIZUIRE ANTRENOR",
        ):
            self.assertIn(section, text)

    def test_return_template_instructs_no_rewriting_of_raw_data(self):
        text = TEMPLATE.read_text(encoding="utf-8")
        self.assertIn("nu se rescrie", text)
        self.assertIn("nu se", text)

    def test_return_template_contains_no_prefilled_answers(self):
        # Every field in the fenced template block must end at the colon (empty) or
        # list bare option choices (e.g. "DA/NU") -- never a single answer already
        # picked/filled in by the assistant.
        text = TEMPLATE.read_text(encoding="utf-8")
        start = text.index("```\n") + len("```\n")
        end = text.index("```", start)
        block = text[start:end]
        for line in block.splitlines():
            if ":" not in line:
                continue
            value = line.split(":", 1)[1].strip()
            if not value:
                continue
            # A bare option list ("DA/PARTIAL/NU") or an instructional placeholder
            # ("rating + nota") is not a filled-in answer.
            is_placeholder = "/" in value or "+" in value
            self.assertTrue(is_placeholder, msg=f"Line appears pre-filled with a single answer: {line!r}")

    def test_registry_task2301_exists_and_done(self):
        import json
        registry = json.loads((ROOT / "TASK_REGISTRY.json").read_text(encoding="utf-8"))
        task = next(t for t in registry["tasks"] if t["task_id"] == "TASK-2301")
        self.assertEqual(task["status"], "DONE")
        self.assertEqual(task["phase"], "PHASE-23")

    def test_registry_no_premature_field_pilot_analysis_task(self):
        # No FIELD PILOT task beyond TASK-2301 (i.e. no analysis/remediation task for
        # real field data that hasn't arrived yet) may be READY while
        # FIELD_INPUT_REQUIRED is in effect. Other, unrelated workstreams (e.g. a
        # later PHASE-24 product-implementation-parity audit) may legitimately have
        # their own READY tasks without violating the field-pilot wait -- this test
        # only guards against inventing autonomous field-analysis work.
        import json
        registry = json.loads((ROOT / "TASK_REGISTRY.json").read_text(encoding="utf-8"))
        ready_field_pilot = [
            t["task_id"] for t in registry["tasks"]
            if t["status"] == "READY" and t["phase"] == "PHASE-23"
        ]
        self.assertEqual(ready_field_pilot, [])


if __name__ == "__main__":
    unittest.main()
