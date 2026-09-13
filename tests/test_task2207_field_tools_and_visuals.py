import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Task2207FieldToolsAndVisualsTests(unittest.TestCase):
    def test_field_tools_doc_exists_and_covers_quick_mode(self):
        path = ROOT / "docs/gold-standard/FIELD_TOOLS.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        self.assertIn("Am nevoie acum", text)
        self.assertIn("Ce observi", text)
        self.assertIn("Ce NU presupui", text)

    def test_field_tools_no_hidden_numeric_thresholds(self):
        text = (ROOT / "docs/gold-standard/FIELD_TOOLS.md").read_text(encoding="utf-8")
        self.assertIn("Niciun prag numeric", text)

    def test_visual_specs_doc_exists_and_covers_all_five_exercises(self):
        path = ROOT / "docs/gold-standard/TACTICAL_VISUAL_SPECS.md"
        self.assertTrue(path.exists())
        text = path.read_text(encoding="utf-8")
        for i in range(1, 6):
            self.assertIn(f"VIS-EX-000{i}", text)

    def test_visual_specs_reject_fixed_angle_geometry(self):
        text = (ROOT / "docs/gold-standard/TACTICAL_VISUAL_SPECS.md").read_text(encoding="utf-8")
        self.assertIn("45°", text)  # appears once, as the explicitly-rejected example
        self.assertIn("nu susține un unghi universal", text)

    def test_visual_specs_confirm_design_freeze_untouched(self):
        text = (ROOT / "docs/gold-standard/TACTICAL_VISUAL_SPECS.md").read_text(encoding="utf-8")
        self.assertIn("DESIGN_FREEZE = YES", text)
        self.assertIn("nu a fost atins de acest task", text)

    def test_no_actual_visual_asset_files_created(self):
        # Design freeze: this task must not produce real SVG/animation files.
        gold_standard_dir = ROOT / "docs" / "gold-standard"
        svg_files = list(gold_standard_dir.glob("*.svg"))
        self.assertEqual(svg_files, [])

    def test_animation_use_is_justified_not_automatic(self):
        text = (ROOT / "docs/gold-standard/TACTICAL_VISUAL_SPECS.md").read_text(encoding="utf-8")
        self.assertIn("nu se animează doar pentru că platforma permite", text)


if __name__ == "__main__":
    unittest.main()
