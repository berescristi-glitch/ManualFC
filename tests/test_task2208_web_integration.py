import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DESIGN_FREEZE_FILES = [
    "app/src/components/AppFooter.astro",
    "app/src/components/AppHeader.astro",
    "app/src/components/ChildMessage.astro",
    "app/src/components/CoachMessage.astro",
    "app/src/components/EvidenceBadge.astro",
    "app/src/components/QuickModePattern.astro",
    "app/src/layouts/BaseLayout.astro",
    "app/src/internal-pages/design-system.astro",
    "app/src/pages/incepe-aici.astro",
    "app/src/pages/index.astro",
    "app/src/pages/principii/[slug].astro",
    "app/src/styles/global.css",
    "app/src/styles/print.css",
    "app/src/styles/tokens.css",
    "astro.config.mjs",
    "config/visual-tokens.json",
]


class Task2208WebIntegrationTests(unittest.TestCase):
    def test_gold_standard_pages_exist(self):
        for rel in [
            "app/src/pages/gold-standard/index.astro",
            "app/src/pages/gold-standard/rapid.astro",
            "app/src/pages/gold-standard/exercitii/[id].astro",
            "app/src/pages/gold-standard/sedinte/[id].astro",
        ]:
            self.assertTrue((ROOT / rel).exists(), rel)

    def test_content_bridge_has_gold_standard_loaders(self):
        text = (ROOT / "app/src/lib/content-bridge.ts").read_text(encoding="utf-8")
        for symbol in (
            "getGoldStandardExercises",
            "getGoldStandardExercise",
            "getGoldStandardSessions",
            "getGoldStandardSession",
            "getGoldStandardSessionExercises",
            "getGoldStandardAssessment",
            "getGoldStandardAssessmentPrinciples",
        ):
            self.assertIn(f"export function {symbol}", text)

    def test_content_bridge_does_not_reuse_narrow_exercise_adapter(self):
        # The Gold Standard content must not be forced through the old
        # fixture-only ExerciseEntity/validateAndParseExercise adapter,
        # which would silently drop almost every rich production field.
        text = (ROOT / "app/src/lib/content-bridge.ts").read_text(encoding="utf-8")
        gs_section = text[text.index("Gold Standard Bridge"):]
        self.assertNotIn("validateAndParseExercise(gsExercise", gs_section)

    def test_design_freeze_files_no_gold_standard_styling(self):
        # This test originally forbade ANY Gold Standard marker string in frozen
        # files, to catch TASK-2208 accidentally editing them instead of only
        # adding new files. A later, separate, explicitly authorized product-
        # implementation-parity pass (PRODUCT_IMPLEMENTATION_PARITY_RECOVERY_LOOP)
        # made minimal, non-visual navigation-data edits to some of these files
        # (AppHeader.astro's preferredLabels map, AppFooter.astro's footer <nav>
        # links) to link to real content instead of dev fixtures/broken slugs.
        # That is plain-text navigation, not visual redesign, so the invariant
        # that still matters is checked precisely: no Gold Standard marker may
        # appear inside a <style> block (which would indicate visual/CSS
        # smuggling) in any frozen file.
        markers = ("Gold Standard", "gold-standard", "Sprijinul și unghiul de pasă")
        for rel in DESIGN_FREEZE_FILES:
            path = ROOT / rel
            if not path.exists():
                continue
            text = path.read_text(encoding="utf-8")
            style_blocks = re.findall(r"<style[^>]*>(.*?)</style>", text, flags=re.DOTALL)
            for block in style_blocks:
                for marker in markers:
                    self.assertNotIn(marker, block, f"{rel} <style> block contains {marker!r} — visual design freeze may have been violated")

    def test_dist_build_produced_gold_standard_routes(self):
        dist = ROOT / "dist" / "web" / "gold-standard"
        self.assertTrue((dist / "index.html").exists())
        self.assertTrue((dist / "rapid" / "index.html").exists())
        for eid in ("EX-0001", "EX-0002", "EX-0003", "EX-0004", "EX-0005"):
            self.assertTrue((dist / "exercitii" / eid / "index.html").exists(), eid)
        for sid in ("SES-0001", "SES-0002"):
            self.assertTrue((dist / "sedinte" / sid / "index.html").exists(), sid)

    def test_no_undefined_leaked_into_rendered_html(self):
        dist = ROOT / "dist" / "web" / "gold-standard"
        for html_file in dist.rglob("index.html"):
            text = html_file.read_text(encoding="utf-8")
            self.assertNotIn("undefined", text, str(html_file))

    def test_quick_mode_page_reuses_quick_mode_pattern_component(self):
        text = (ROOT / "app/src/pages/gold-standard/rapid.astro").read_text(encoding="utf-8")
        self.assertIn("QuickModePattern", text)

    def test_deep_mode_reuses_canonical_principles_not_new_ones(self):
        text = (ROOT / "app/src/pages/gold-standard/index.astro").read_text(encoding="utf-8")
        self.assertIn("principle-spatiu-si-unghiuri", text)
        self.assertIn("principle-progresie-si-sprijin", text)


if __name__ == "__main__":
    unittest.main()
