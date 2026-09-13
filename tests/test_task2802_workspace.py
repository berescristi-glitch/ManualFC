import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WorkspaceContractTests(unittest.TestCase):
    def test_state_is_versioned_and_has_replaceable_port(self):
        source = (ROOT / "app/src/lib/coach-state.ts").read_text(encoding="utf-8")
        self.assertIn("manualfc.coach-state.v1", source)
        self.assertIn("interface CoachStatePort", source)
        self.assertNotIn("childName", source)
        self.assertNotIn("birthDate", source)

    def test_builder_reconciles_ids_and_rejects_invalid_totals(self):
        source = (ROOT / "app/src/pages/spatiul-meu/sedinta.astro").read_text(encoding="utf-8")
        self.assertIn("filter(x=>catalogFor(x.ref.kind).has(x.ref.id))", source)
        self.assertIn("total>duration", source)
        self.assertIn("cel puțin un reper canonic", source)
        self.assertIn("data-up", source)
        self.assertIn("data-down", source)

    def test_workspace_exposes_all_continuity_surfaces(self):
        source = (ROOT / "app/src/pages/spatiul-meu/index.astro").read_text(encoding="utf-8")
        for marker in ("data-saved", "data-favorites", "data-recents", "data-continue-link", "data-onboarding"):
            self.assertIn(marker, source)


if __name__ == "__main__":
    unittest.main()
