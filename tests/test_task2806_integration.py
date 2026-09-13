import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TouchTargetRegressionTests(unittest.TestCase):
    def test_add_session_button_meets_44px_minimum(self):
        # Found via live browser measurement (getBoundingClientRect), not from
        # reading CSS: the TASK-2805 "Adauga sedinta canonica" button was never
        # added to the shared 44px rule, rendering at 19px actual height.
        source = (ROOT / "app/src/pages/spatiul-meu/sedinta.astro").read_text(encoding="utf-8")
        self.assertIn("[data-add],[data-add-session],.save{min-height:44px", source)


class DecisionEngineToWorkspaceIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.source = (ROOT / "app/src/components/CoachActions.astro").read_text(encoding="utf-8")

    def test_problem_context_from_decision_engine_survives_into_workspace(self):
        # Exercise/problem pages are fully static-prerendered (getStaticPaths), so
        # Astro.url.searchParams is never available server-side for a ?problema=
        # deep link from the Decision Engine. Without reading it client-side, the
        # "+ Sedinta" quick-add silently drops which observed problem justified
        # adding this exercise -- a broken cross-feature reference, found only by
        # walking the full Decision Engine -> Workspace journey end to end.
        self.assertIn("problemIdFromContext()", self.source)
        self.assertIn("new URLSearchParams(location.search).get('problema')", self.source)

    def test_new_session_created_via_quick_add_carries_problem_id(self):
        self.assertIn("if(problemId)session={...session,problemId}", self.source)

    def test_existing_active_session_without_a_problem_gets_one_filled_in(self):
        # Must not clobber a problemId the coach already chose explicitly in the builder.
        self.assertIn("if(!session.problemId&&problemId)", self.source)


if __name__ == "__main__":
    unittest.main()
