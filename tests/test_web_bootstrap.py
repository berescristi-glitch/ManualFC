import json
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

class WebBootstrapTests(unittest.TestCase):
    def test_package_json_structure(self):
        pkg_path = ROOT_DIR / "package.json"
        self.assertTrue(pkg_path.exists(), "package.json nu exista.")
        with open(pkg_path, "r", encoding="utf-8") as f:
            pkg = json.load(f)
        
        self.assertIn("astro", pkg.get("dependencies", {}))
        self.assertIn("@astrojs/mdx", pkg.get("dependencies", {}))
        self.assertIn("@astrojs/check", pkg.get("devDependencies", {}))
        self.assertIn("typescript", pkg.get("devDependencies", {}))
        self.assertIn("build", pkg.get("scripts", {}))
        self.assertIn("check", pkg.get("scripts", {}))

    def test_astro_config_has_srcdir(self):
        astro_cfg_path = ROOT_DIR / "astro.config.mjs"
        self.assertTrue(astro_cfg_path.exists(), "astro.config.mjs nu exista.")
        content = astro_cfg_path.read_text(encoding="utf-8")
        self.assertIn("srcDir: './app/src'", content)
        self.assertIn("output: 'static'", content)

    def test_tsconfig_is_strict(self):
        tsconfig_path = ROOT_DIR / "tsconfig.json"
        self.assertTrue(tsconfig_path.exists(), "tsconfig.json nu exista.")
        with open(tsconfig_path, "r", encoding="utf-8") as f:
            ts_cfg = json.load(f)
        opts = ts_cfg.get("compilerOptions", {})
        self.assertTrue(opts.get("strict"))
        self.assertTrue(opts.get("noImplicitAny"))
        self.assertTrue(opts.get("strictNullChecks"))

    def test_web_src_structure_and_routes(self):
        app_src = ROOT_DIR / "app" / "src"
        self.assertTrue((app_src / "pages" / "index.astro").exists())
        self.assertTrue((app_src / "pages" / "incepe-aici.astro").exists())
        self.assertTrue((app_src / "pages" / "404.astro").exists())
        self.assertTrue((app_src / "internal-pages" / "fixture-mdx.mdx").exists())
        self.assertTrue((app_src / "layouts" / "BaseLayout.astro").exists())
        self.assertTrue((app_src / "styles" / "tokens.css").exists())
        self.assertTrue((app_src / "styles" / "global.css").exists())
        self.assertTrue((app_src / "content.config.ts").exists())

    def test_fixture_mdx_is_marked_as_fixture(self):
        fixture_path = ROOT_DIR / "app" / "src" / "internal-pages" / "fixture-mdx.mdx"
        content = fixture_path.read_text(encoding="utf-8")
        self.assertIn("isFixture: true", content)
        self.assertIn("AVERTISMENT DE FIXTURE", content)
        self.assertFalse((ROOT_DIR / "app" / "src" / "pages" / "fixture-mdx.mdx").exists())

    def test_base_layout_has_lang_ro(self):
        layout_path = ROOT_DIR / "app" / "src" / "layouts" / "BaseLayout.astro"
        content = layout_path.read_text(encoding="utf-8")
        self.assertIn('<html lang="ro">', content)
        self.assertIn('Site URL = unresolved', content)

if __name__ == "__main__":
    unittest.main()
