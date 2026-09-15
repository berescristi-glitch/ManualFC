import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILOT_DIR = ROOT / "docs" / "field-pilot"
PROTOCOL = PILOT_DIR / "MANUALFC_PRIVATE_PILOT_PROTOCOL.md"
COACH_PACK = PILOT_DIR / "PRIVATE_PILOT_COACH_PACK.md"
OBSERVATION_TEMPLATE = PILOT_DIR / "PRIVATE_PILOT_OBSERVATION_TEMPLATE.md"

FORBIDDEN_FABRICATED_EVIDENCE_PHRASES = [
    "toți copiii au reușit", "copilul a spus", "s-a observat că",
    "rezultatele arată", "100% dintre copii", "pilotarea a confirmat",
    "antrenorul a spus", "antrenorii au raportat",
]


class Task3713PilotDocsExistTests(unittest.TestCase):
    def test_all_three_pilot_documents_exist(self):
        for path in (PROTOCOL, COACH_PACK, OBSERVATION_TEMPLATE):
            self.assertTrue(path.exists(), path)

    def test_execplan_exists(self):
        self.assertTrue((ROOT / "plans" / "TASK-3713-private-pilot-setup.md").exists())


class Task3713NoFabricatedEvidenceTests(unittest.TestCase):
    def test_protocol_contains_no_fabricated_results(self):
        text = PROTOCOL.read_text(encoding="utf-8").lower()
        for phrase in FORBIDDEN_FABRICATED_EVIDENCE_PHRASES:
            self.assertNotIn(phrase, text, phrase)

    def test_coach_pack_contains_no_fabricated_results(self):
        text = COACH_PACK.read_text(encoding="utf-8").lower()
        for phrase in FORBIDDEN_FABRICATED_EVIDENCE_PHRASES:
            self.assertNotIn(phrase, text, phrase)

    def test_observation_template_contains_no_prefilled_answers(self):
        # The template itself must stay empty/instructional, never a filled-in
        # example that could be mistaken for real field data.
        text = OBSERVATION_TEMPLATE.read_text(encoding="utf-8")
        start = text.index("```\n") + len("```\n")
        end = text.index("```", start)
        block = text[start:end]
        for line in block.splitlines():
            if ":" not in line:
                continue
            value = line.split(":", 1)[1].strip()
            if not value:
                continue
            is_placeholder = "/" in value or value.startswith("(")
            self.assertTrue(is_placeholder, msg=f"Line appears pre-filled: {line!r}")

    def test_protocol_declares_field_input_required(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("FIELD_INPUT_REQUIRED", text)

    def test_protocol_explicitly_states_no_result_exists_yet(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        self.assertIn("nu se inventează sau se simulează", text)


class Task3713PrivacyBoundaryTests(unittest.TestCase):
    def test_protocol_forbids_child_personal_data(self):
        text = PROTOCOL.read_text(encoding="utf-8").lower()
        self.assertIn("fără date despre copii", text)

    def test_protocol_forbids_audio_video_without_separate_authorization(self):
        text = PROTOCOL.read_text(encoding="utf-8").lower()
        self.assertIn("audio", text)
        self.assertIn("autorizare separată", text)

    def test_protocol_uses_deidentified_coach_codes(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        for code in ("A1", "A2", "A3"):
            self.assertIn(code, text)

    def test_coach_pack_explains_no_child_data_collection(self):
        text = COACH_PACK.read_text(encoding="utf-8").lower()
        self.assertIn("copiii", text)
        self.assertIn("nu cerem", text)

    def test_coach_pack_explains_no_account_no_server_storage(self):
        text = COACH_PACK.read_text(encoding="utf-8").lower()
        self.assertTrue("cont" in text and "server" in text)

    def test_observation_template_has_privacy_checklist(self):
        text = OBSERVATION_TEMPLATE.read_text(encoding="utf-8").lower()
        self.assertIn("confidentialitate", text)
        self.assertIn("nume de copii", text)


class Task3713NoResearchJargonInCoachFacingDocs(unittest.TestCase):
    def test_coach_pack_has_no_research_jargon(self):
        text = COACH_PACK.read_text(encoding="utf-8")
        for token in ("SRC-", "CLM-", "CIT-", "RQ-", "epistemic", "FAIL_CLOSED"):
            self.assertNotIn(token, text)


class Task3713RequiredProtocolSectionsTests(unittest.TestCase):
    def setUp(self):
        self.text = PROTOCOL.read_text(encoding="utf-8")

    def test_required_sections_present(self):
        required_headings = [
            "Profilul participantului", "recrutare", "Participare informată",
            "Durata pilotului", "Sarcini obligatorii", "mobil și desktop",
            "online și offline", "Metoda de observare", "debrief",
            "Dovezi comportamentale", "spun antrenorii", "succes",
            "oprire", "severității", "prioritizare", "MUST FIX",
        ]
        for heading in required_headings:
            self.assertIn(heading, self.text, heading)

    def test_all_nine_task_scenarios_present(self):
        scenarios = [
            "problemă de joc", "Decision Engine", "telefon", "ședință completă",
            "trebuie să observe", "Revine", "conexiune limitată",
            "transferul în meci", "reflecție",
        ]
        for scenario in scenarios:
            self.assertIn(scenario, self.text, scenario)

    def test_severity_table_has_four_levels(self):
        for level in ("CRITICĂ", "MAJORĂ", "MODERATĂ", "MINORĂ"):
            self.assertIn(level, self.text)

    def test_triage_table_has_four_decisions(self):
        for decision in ("MUST FIX", "SHOULD FIX", "NOT NOW", "IGNORE"):
            self.assertIn(decision, self.text)

    def test_references_existing_round1_precedent_honestly(self):
        self.assertIn("TASK-2301", self.text)
        self.assertIn("rămâne, la rândul lui, neexecutat", self.text)


class Task3713CoachPackCoversAllScenariosTests(unittest.TestCase):
    def test_coach_pack_lists_nine_numbered_tasks(self):
        text = COACH_PACK.read_text(encoding="utf-8")
        for n in range(1, 10):
            self.assertIn(f"**{n}.", text, f"task {n}")

    def test_coach_pack_references_observation_template(self):
        text = COACH_PACK.read_text(encoding="utf-8")
        self.assertIn("PRIVATE_PILOT_OBSERVATION_TEMPLATE.md", text)

    def test_coach_pack_allows_opting_out(self):
        text = COACH_PACK.read_text(encoding="utf-8").lower()
        self.assertIn("renunța", text)


if __name__ == "__main__":
    unittest.main()
