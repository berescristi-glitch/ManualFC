import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProductionHygieneTests(unittest.TestCase):
    INTERNAL_SOURCES = (
        "app/src/internal-pages/design-system.astro",
        "app/src/internal-pages/fixture-mdx.mdx",
        "app/src/internal-pages/exercitii/[slug].astro",
        "app/src/internal-pages/probleme/[slug].astro",
    )
    INTERNAL_OUTPUTS = (
        "design-system/index.html",
        "fixture-mdx/index.html",
        "exercitii/2v1-unghi-de-suport/index.html",
        "probleme/lipsa-unghi-de-pasa/index.html",
        "principii/orientare-corporala-scanare/index.html",
    )

    def test_internal_sources_are_preserved_outside_public_pages(self):
        for rel in self.INTERNAL_SOURCES:
            self.assertTrue((ROOT / rel).exists(), rel)
        public_pages = ROOT / "app/src/pages"
        self.assertFalse((public_pages / "design-system.astro").exists())
        self.assertFalse((public_pages / "fixture-mdx.mdx").exists())
        self.assertFalse((public_pages / "exercitii/[slug].astro").exists())
        self.assertFalse((public_pages / "probleme/[slug].astro").exists())

    def test_internal_routes_are_absent_from_public_build(self):
        dist = ROOT / "dist/web"
        for rel in self.INTERNAL_OUTPUTS:
            self.assertFalse((dist / rel).exists(), rel)

    def test_public_system_404_is_preserved(self):
        self.assertTrue((ROOT / "app/src/pages/404.astro").exists())
        self.assertTrue((ROOT / "dist/web/404.html").exists())

    def test_principle_route_filters_development_fixtures(self):
        route = (ROOT / "app/src/pages/principii/[slug].astro").read_text(encoding="utf-8")
        self.assertIn("getCanonicalProductionContent(getAllPrinciples())", route)


if __name__ == "__main__":
    unittest.main()
