import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class PresentationLayerV2Tests(unittest.TestCase):
    def test_reusable_components_exist(self):
        for name in ("FieldSummary.astro", "SectionNavigator.astro"):
            self.assertTrue((ROOT / "app/src/components" / name).exists(), name)

    def test_principle_has_practical_preview_and_progressive_sections(self):
        text = (ROOT / "app/src/pages/principii/[slug].astro").read_text(encoding="utf-8")
        for marker in ("practical-preview", "Spune exact", "Comportament observabil", "SectionNavigator", 'id="intelege"', 'id="dovezi"'):
            self.assertIn(marker, text)

    def test_exercise_has_field_summary_and_progressive_sections(self):
        text = (ROOT / "app/src/pages/gold-standard/exercitii/[id].astro").read_text(encoding="utf-8")
        for marker in ("FieldSummary", "players.total", "equipment.join", "safety_margin_m", 'id="organizare"', 'id="observa"', 'id="fundamentare"', 'id="transfer"'):
            self.assertIn(marker, text)

    def test_duration_and_missing_visual_are_honest(self):
        text = (ROOT / "app/src/pages/gold-standard/exercitii/[id].astro").read_text(encoding="utf-8")
        self.assertIn("total_minutes", text)
        self.assertIn("activul vizual canonic nu este încă disponibil și nu este simulat", text)

if __name__ == "__main__":
    unittest.main()
