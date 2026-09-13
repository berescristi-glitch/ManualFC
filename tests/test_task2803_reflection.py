import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReflectionContractTests(unittest.TestCase):
    def test_state_extends_v1_without_breaking_existing_fields(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("reflections: SessionReflection[]", source)
        self.assertIn("saved: [], favorites: [], recents: [], sessions: [], reflections: []", source)
        self.assertIn("sanitizeReflections(r.reflections)", source)

    def test_reflection_sanitizer_is_fail_closed(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("function sanitizeReflection(v: unknown): SessionReflection | null", source)
        self.assertIn("isObservedState(r.observedState)", source)
        self.assertIn("isTransferState(r.transferState) ? r.transferState : 'transfer_unconfirmed'", source)

    def test_next_action_is_deterministic_lookup_not_free_text(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("export function computeNextAction(observed: ObservedState, transfer: TransferState): string", source)
        for phrase in (
            "Reconsideră ipoteza",
            "Repetă sarcina cu același reper",
            "Repetă sau ajustează o singură variabilă",
            "Păstrează reperul și testează dacă apare și în joc mai liber",
            "Crește dificultatea sau verifică transferul într-un context diferit",
        ):
            self.assertIn(phrase, source)

    def test_transfer_distinct_from_task_performance(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("export type ObservedState = 'not_observed' | 'emerging' | 'partial' | 'consistent_in_task';", source)
        self.assertIn("export type TransferState = 'transfer_unconfirmed' | 'transfer_seen';", source)

    def test_no_child_pii_fields_introduced(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        for forbidden in ("childName", "birthDate", "childHealth", "parentContact"):
            self.assertNotIn(forbidden, source)

    def test_reflection_page_resolves_canonical_context_not_retyped(self):
        source = (ROOT / "app/src/pages/spatiul-meu/reflectie.astro").read_text(encoding="utf-8")
        self.assertIn("getGoldStandardSessionExercises", source)
        self.assertIn("getProblems", source)
        self.assertIn("data-context", source)
        self.assertIn("Reflecție liberă, fără context canonic legat", source)

    def test_reflection_page_gates_transfer_question_on_observed_state(self):
        source = (ROOT / "app/src/pages/spatiul-meu/reflectie.astro").read_text(encoding="utf-8")
        self.assertIn("needsTransfer=observed==='partial'||observed==='consistent_in_task'", source)
        self.assertIn("data-transfer-fieldset", source)

    def test_reflection_page_supports_edit_and_delete(self):
        source = (ROOT / "app/src/pages/spatiul-meu/reflectie.astro").read_text(encoding="utf-8")
        self.assertIn("deleteReflection", source)
        self.assertIn("editId", source)
        self.assertIn("saveReflection(", source)

    def test_reflection_page_has_decision_engine_reentry(self):
        source = (ROOT / "app/src/pages/spatiul-meu/reflectie.astro").read_text(encoding="utf-8")
        self.assertIn("data-reentry", source)
        self.assertIn("/rezolva-pe-teren/", source)

    def test_privacy_language_present_not_overclaiming_enforcement(self):
        source = (ROOT / "app/src/pages/spatiul-meu/reflectie.astro").read_text(encoding="utf-8")
        self.assertIn("Nu introduce nume, date medicale sau alte date personale despre copii.", source)
        self.assertNotIn("nu permite introducerea", source)

    def test_field_mode_handoff_replaces_dead_end(self):
        source = (ROOT / "app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro").read_text(encoding="utf-8")
        self.assertIn("Termină ședința → Reflecție", source)
        self.assertNotIn("Ședință încheiată", source)
        self.assertIn("/spatiul-meu/reflectie?", source)

    def test_workspace_exposes_reflection_history_and_continue_v2(self):
        source = (ROOT / "app/src/pages/spatiul-meu/index.astro").read_text(encoding="utf-8")
        self.assertIn("data-reflections", source)
        self.assertIn("findUnreflectedSession", source)
        self.assertIn("data-delete-session", source)
        self.assertIn("data-delete-reflection", source)

    def test_task2802_surfaces_still_present_no_regression(self):
        source = (ROOT / "app/src/pages/spatiul-meu/index.astro").read_text(encoding="utf-8")
        for marker in ("data-saved", "data-favorites", "data-recents", "data-continue-link", "data-onboarding", "data-sessions"):
            self.assertIn(marker, source)

    def test_architecture_doc_documents_migration_and_priority(self):
        source = (ROOT / "docs/architecture/ASSESSMENT_REFLECTION_LOOP.md").read_text(encoding="utf-8")
        self.assertIn("Continue V2", source)
        self.assertIn("fail-closed", source.lower())


if __name__ == "__main__":
    unittest.main()
