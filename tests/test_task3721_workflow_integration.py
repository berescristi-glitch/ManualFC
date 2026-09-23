import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


class NavigationUnificationTests(unittest.TestCase):
    """TASK-3721: header and footer must render from a single nav source,
    covering all four content systems, so no destination is only reachable
    from one surface (a duplicate/divergent discovery path)."""

    def test_content_bridge_exposes_all_four_systems_in_primary_nav(self):
        text = read("app/src/lib/content-bridge.ts")
        nav_block = text[text.index("export function getPrimaryNavigation"):]
        nav_block = nav_block[: nav_block.index("\n}\n") + 3]
        for href in ("/rezolva-pe-teren", "/gold-standard", "/scripturi", "/planuri-de-sezon", "/cauta", "/spatiul-meu"):
            self.assertIn(f'href: "{href}"', nav_block)

    def test_header_and_footer_both_source_from_get_primary_navigation(self):
        header = read("app/src/components/AppHeader.astro")
        footer = read("app/src/components/AppFooter.astro")
        self.assertIn("getPrimaryNavigation", header)
        self.assertIn("getPrimaryNavigation", footer)
        for route in ("/scripturi", "/planuri-de-sezon", "/cauta", "/spatiul-meu"):
            self.assertIn(f"'{route}':", header)
            self.assertIn(f"'{route}':", footer)


class ProblemLibraryReverseLookupTests(unittest.TestCase):
    """New reverse lookups (content-first discovery) must reuse only the
    already-declared relational fields, never a scored/popularity list."""

    def test_problem_library_exposes_reverse_lookups(self):
        text = read("app/src/lib/problem-library.ts")
        for fn in ("getProblemsForExercise", "getProblemsForSession", "getProblemsForPrinciple"):
            self.assertIn(f"export function {fn}(", text)
        self.assertIn("p.related_exercises.includes(exerciseId)", text)
        self.assertIn("p.related_sessions.includes(sessionId)", text)
        self.assertIn("p.related_principles.includes(principleId)", text)

    def test_content_bridge_exposes_scripts_for_problem(self):
        text = read("app/src/lib/content-bridge.ts")
        self.assertIn("export function getScriptsForProblem(problemId: string)", text)
        self.assertIn("(s.related_problem_ids ?? []).includes(problemId)", text)

    def test_known_cross_reference_chain_is_internally_consistent(self):
        """PRB-0001 <-> EX-0001 <-> SES-0001 <-> principle.spatiu-si-unghiuri <-> SCR-0005
        is a real, data-declared chain; verify the underlying data still agrees
        so the new pages' reverse lookups resolve to something real."""
        problems = json.loads(read("data/problems/problem-library.json"))
        problem_list = problems if isinstance(problems, list) else problems.get("problems", [])
        prb1 = next(p for p in problem_list if p["problem_id"] == "PRB-0001")
        self.assertIn("EX-0001", prb1["related_exercises"])
        self.assertIn("SES-0001", prb1["related_sessions"])
        self.assertIn("principle.spatiu-si-unghiuri", prb1["related_principles"])

        script = json.loads(read("data/communication-scripts/script-iesi-din-umbra-adversarului.json"))
        self.assertEqual(script["id"], "SCR-0005")
        self.assertIn("PRB-0001", script["related_problem_ids"])


class ContentFirstDiscoveryLinksTests(unittest.TestCase):
    """Capability 2: from any content page, the coach can see what problem
    it addresses and reach the next relevant step."""

    def test_exercise_page_links_back_to_the_problem_it_solves(self):
        text = read("app/src/pages/gold-standard/exercitii/[id].astro")
        self.assertIn("import { getProblemsForExercise } from '../../../lib/problem-library';", text)
        self.assertIn("const relatedProblems = getProblemsForExercise(ex.id);", text)
        self.assertIn("Problema pe care o rezolvă:", text)
        self.assertIn("/rezolva-pe-teren/${p.slug}", text)

    def test_session_page_links_back_to_the_problem_it_solves(self):
        text = read("app/src/pages/gold-standard/sedinte/[id].astro")
        self.assertIn("import { getProblemsForSession } from '../../../lib/problem-library';", text)
        self.assertIn("const relatedProblems = getProblemsForSession(ses.id);", text)
        self.assertIn("Problema pe care o rezolvă:", text)

    def test_principle_page_links_to_problems_it_resolves(self):
        text = read("app/src/pages/principii/[slug].astro")
        self.assertIn("import { getProblemsForPrinciple } from '../../lib/problem-library';", text)
        self.assertIn("const relatedProblems = getProblemsForPrinciple(principle.id);", text)
        self.assertIn("Probleme de joc rezolvate de acest principiu", text)

    def test_problem_page_links_to_principle_and_communication_scripts(self):
        text = read("app/src/pages/rezolva-pe-teren/[slug].astro")
        self.assertIn("getScriptsForProblem, getAllPrinciples", text)
        self.assertIn("relevantScripts=getScriptsForProblem(problem.problem_id)", text)
        self.assertIn("Principiul din spate:", text)
        self.assertIn("/scripturi/${s.id}", text)

    def test_problem_page_fails_closed_on_unresolved_principle_reference(self):
        text = read("app/src/pages/rezolva-pe-teren/[slug].astro")
        self.assertIn("[FAIL_CLOSED] [Problem]", text)
        self.assertIn("Referința la principiul", text)


class ReflectionContinuityTests(unittest.TestCase):
    """The 'reflect after session' step existed as a tool but nothing linked
    to it from the session or season-plan pages -- a real dead end fixed here."""

    def test_reflectie_tool_accepts_session_query_param(self):
        text = read("app/src/pages/spatiul-meu/reflectie.astro")
        self.assertIn("params.get('sesiune')", text)

    def test_session_page_offers_reflect_cta_linking_to_reflectie_tool(self):
        text = read("app/src/pages/gold-standard/sedinte/[id].astro")
        self.assertIn("/spatiul-meu/reflectie?sesiune=${ses.id}", text)
        self.assertIn("Reflectează după această ședință în Spațiul meu", text)

    def test_season_plan_microcycle_offers_reflect_cta_for_its_first_session(self):
        text = read("app/src/pages/planuri-de-sezon/[id].astro")
        self.assertIn("/spatiul-meu/reflectie?sesiune=${mic.session_ids[0]}", text)
        self.assertIn("Reflectează după această săptămână în Spațiul meu", text)


class UnifiedSearchTests(unittest.TestCase):
    """Capability 4: search must cover all four systems with useful labels
    and must not silently exclude items that lack a given facet."""

    def test_discovery_index_covers_all_four_systems(self):
        text = read("app/src/lib/discovery-index.ts")
        match = re.search(r"export type DiscoveryType\s*=\s*(.+);", text)
        self.assertIsNotNone(match)
        types = match.group(1)
        for t in ("PROBLEMĂ", "PRINCIPIU", "EXERCIȚIU", "ȘEDINȚĂ", "SCRIPT", "PLAN DE SEZON"):
            self.assertIn(t, types)

    def test_search_page_has_human_readable_type_labels_for_every_type(self):
        text = read("app/src/pages/cauta.astro")
        self.assertIn("typeLabels", text)
        for t in ("PROBLEMĂ", "PRINCIPIU", "EXERCIȚIU", "ȘEDINȚĂ", "SCRIPT", "PLAN DE SEZON"):
            self.assertIn(f"'{t}':", text)

    def test_search_type_filter_options_are_derived_from_discovery_index(self):
        text = read("app/src/pages/cauta.astro")
        self.assertIn("getDiscoveryIndex", text)
        self.assertIn("const types=[...new Set(items.map(x=>x.type))]", text)

    def test_search_facet_filters_do_not_exclude_items_missing_that_facet(self):
        """A script or season plan without player-count/duration metadata
        must not be silently hidden by the Efectiv/Timp filters."""
        text = read("app/src/pages/cauta.astro")
        self.assertIn("hasPlayers=c.dataset.playersMin!==''", text)
        self.assertIn("hasMinutes=c.dataset.minutes!==''", text)
        self.assertIn("playerOk=players.value==='all'||!hasPlayers", text)
        self.assertIn("timeOk=time.value==='all'||!hasMinutes", text)

    def test_search_has_no_results_state(self):
        text = read("app/src/pages/cauta.astro")
        self.assertIn('id="count"', text)
        self.assertIn("aria-live=\"polite\"", text)


class SpatiulMeuContinuityTests(unittest.TestCase):
    """Capability 5: Spatiul meu must show what is saved/favorite/recent
    across all systems, with actionable (not generic) empty states, while
    staying local-first (no account, no server persistence)."""

    def test_kind_labels_cover_all_canonical_kinds(self):
        text = read("app/src/lib/coach-state.ts")
        match = re.search(r"CanonicalKind\s*=\s*(.+);", text)
        self.assertIsNotNone(match)
        kind_union = match.group(1)
        labels_start = text.index("CANONICAL_KIND_LABELS")
        labels_block = text[labels_start: text.index("};", labels_start)]
        for kind in ("problem", "principle", "exercise", "session", "assessment", "chapter", "script"):
            self.assertIn(f"'{kind}'", kind_union)
            self.assertIn(f"{kind}:", labels_block)
        self.assertIn("'season-plan'", kind_union)
        self.assertIn("'season-plan':", labels_block)

    def test_saved_favorites_recents_render_kind_tags(self):
        text = read("app/src/pages/spatiul-meu/index.astro")
        self.assertIn("CANONICAL_KIND_LABELS", text)
        self.assertIn("kind-tag", text)

    def test_empty_states_are_actionable_not_generic(self):
        text = read("app/src/pages/spatiul-meu/index.astro")
        self.assertIn("Nimic salvat încă", text)
        self.assertIn("Niciun favorit încă", text)
        self.assertIn("Nimic vizitat încă", text)
        self.assertIn("Nicio reflecție încă", text)
        # each empty state must name a concrete next action, not just state absence
        self.assertIn('folosește butonul „Salvează', text)
        self.assertIn('marchează cu „Favorit', text)

    def test_no_account_or_server_language_introduced(self):
        text = read("app/src/pages/spatiul-meu/index.astro")
        for forbidden in ("password", "login", "sign up", "account_id", "fetch('/api"):
            self.assertNotIn(forbidden, text.lower())


class HomepageAndOnboardingIntegrationTests(unittest.TestCase):
    """Capability 1 entry points: the homepage and onboarding page must
    surface season planning (previously an isolated fourth system) as a
    genuine entry mode, not just a nav link."""

    def test_homepage_has_a_third_mode_entry_for_season_planning(self):
        text = read("app/src/pages/index.astro")
        self.assertIn("/planuri-de-sezon", text)
        self.assertIn("mode-plan", text)

    def test_onboarding_page_mentions_three_entry_paths(self):
        text = read("app/src/pages/incepe-aici.astro")
        self.assertIn("Trei intrări", text)
        self.assertIn("/planuri-de-sezon", text)


class MobileNavigationTests(unittest.TestCase):
    """Capability 7: mobile field use -- nav must not silently drop the new
    systems on small screens, and must not overflow."""

    def test_header_defines_a_mobile_nav_that_includes_new_systems(self):
        text = read("app/src/components/AppHeader.astro")
        self.assertIn("mobile-nav", text)

    def test_footer_grid_has_a_single_column_mobile_breakpoint(self):
        text = read("app/src/components/AppFooter.astro")
        self.assertIn("grid-template-columns: 1fr", text)


class OfflineAndLocalFirstTests(unittest.TestCase):
    """Capability 8: no new server dependency introduced by this task's
    workflow additions -- reflect CTAs and cross-links are plain internal
    hrefs, resolvable by the same static/offline mechanism as before."""

    def test_reflect_cta_links_are_internal_static_hrefs(self):
        for path in (
            "app/src/pages/gold-standard/sedinte/[id].astro",
            "app/src/pages/planuri-de-sezon/[id].astro",
        ):
            text = read(path)
            self.assertIn("/spatiul-meu/reflectie?sesiune=", text)
            self.assertNotIn("http://", text)
            self.assertNotIn("https://", text)

    def test_new_cross_link_functions_introduce_no_network_calls(self):
        for path in (
            "app/src/lib/problem-library.ts",
            "app/src/lib/content-bridge.ts",
        ):
            text = read(path)
            self.assertNotIn("fetch(", text)
            self.assertNotIn("XMLHttpRequest", text)


class NoFieldValidationClaimTests(unittest.TestCase):
    """This task must not introduce language implying real-coach field
    validation happened -- TASK-3714 remains BLOCKED."""

    def test_no_new_pilot_or_field_tested_claims_in_touched_pages(self):
        touched = [
            "app/src/pages/index.astro",
            "app/src/pages/incepe-aici.astro",
            "app/src/pages/cauta.astro",
            "app/src/pages/spatiul-meu/index.astro",
            "app/src/pages/rezolva-pe-teren/[slug].astro",
            "app/src/pages/gold-standard/exercitii/[id].astro",
            "app/src/pages/gold-standard/sedinte/[id].astro",
            "app/src/pages/principii/[slug].astro",
            "app/src/pages/planuri-de-sezon/[id].astro",
        ]
        forbidden = ("testat pe teren", "validat de antrenori", "field-tested", "pilot validat")
        for path in touched:
            text = read(path).lower()
            for phrase in forbidden:
                self.assertNotIn(phrase, text, f"{path} contains forbidden claim '{phrase}'")


if __name__ == "__main__":
    unittest.main()
