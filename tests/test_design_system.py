import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class DesignSystemTests(unittest.TestCase):
    def test_visual_tokens_json_has_tokens_2_0(self):
        tokens_json = ROOT_DIR / "config" / "visual-tokens.json"
        self.assertTrue(tokens_json.exists())
        with open(tokens_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.assertIn("semantic_colors", data)
        self.assertIn("layout_widths", data)
        self.assertIn("epistemic_levels", data)
        
        epistemic = data["epistemic_levels"]
        for level in ["HIGH", "MODERATE", "LOW", "PRACTICE_ONLY", "UNRESOLVED"]:
            self.assertIn(level, epistemic)
            self.assertIn("label", epistemic[level])

    def test_print_stylesheet_exists_and_has_media_print(self):
        print_css = ROOT_DIR / "app" / "src" / "styles" / "print.css"
        self.assertTrue(print_css.exists())
        content = print_css.read_text(encoding="utf-8")
        self.assertIn("@media print", content)
        self.assertIn("break-inside: avoid", content)

    def test_pedagogical_block_primitive_exists(self):
        primitive = ROOT_DIR / "app" / "src" / "components" / "PedagogicalBlock.astro"
        self.assertTrue(primitive.exists())

    def test_specialized_pedagogical_wrappers_exist(self):
        comp_dir = ROOT_DIR / "app" / "src" / "components"
        wrappers = [
            "WhyThisMatters.astro",
            "ObserveThis.astro",
            "DecisionToLearn.astro",
            "CommonMistake.astro",
            "PhraseToAvoid.astro",
            "UnderstandingCheck.astro",
            "Adaptation.astro",
            "MatchTransfer.astro",
            "EvidenceNote.astro"
        ]
        for w in wrappers:
            self.assertTrue((comp_dir / w).exists(), f"Wrapperul {w} nu exista.")
            content = (comp_dir / w).read_text(encoding="utf-8")
            self.assertIn("PedagogicalBlock", content, f"Wrapperul {w} nu reutilizeaza PedagogicalBlock.")

    def test_child_and_coach_message_contract(self):
        child_comp = ROOT_DIR / "app" / "src" / "components" / "ChildMessage.astro"
        coach_comp = ROOT_DIR / "app" / "src" / "components" / "CoachMessage.astro"
        self.assertTrue(child_comp.exists())
        self.assertTrue(coach_comp.exists())

    def test_evidence_badge_maps_canonical_levels(self):
        badge_comp = ROOT_DIR / "app" / "src" / "components" / "EvidenceBadge.astro"
        self.assertTrue(badge_comp.exists())
        content = badge_comp.read_text(encoding="utf-8")
        for level in ["HIGH", "MODERATE", "LOW", "PRACTICE_ONLY", "UNRESOLVED"]:
            self.assertIn(level, content)

    test_evidence_badge_maps_canonical_levels.level_check = True

    def test_design_system_page_has_noindex_and_dev_only(self):
        ds_page = ROOT_DIR / "app" / "src" / "internal-pages" / "design-system.astro"
        self.assertTrue(ds_page.exists())
        content = ds_page.read_text(encoding="utf-8")
        self.assertIn("noindex,nofollow", content)
        self.assertIn("INTERNAL / DEVELOPMENT ONLY", content)
        self.assertFalse((ROOT_DIR / "app" / "src" / "pages" / "design-system.astro").exists())

    def test_no_forbidden_ui_frameworks_installed(self):
        pkg_json = ROOT_DIR / "package.json"
        with open(pkg_json, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}
        forbidden = ["tailwindcss", "bootstrap", "@mui/material", "@chakra-ui/react", "react", "vue", "svelte"]
        for lib in forbidden:
            self.assertNotIn(lib, deps, f"Framework-ul interzis {lib} este instalat.")

if __name__ == "__main__":
    unittest.main()
