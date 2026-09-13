# MANUALFC — REAL PRODUCT & VISUAL ACCEPTANCE AUDIT V1.0

Browser-first forensic review of the actual rendered ManualFC web product, run against the live `npm run dev` server (Astro v5.18.2) at repository root `E:\ManualFC`. Read-only. No source files, styles, or content were modified during this audit.

CURRENT_HEAD: `b109920` — audit(TASK-2402,2403): independent re-audit finds and closes one real defect

CURRENT_BRANCH: `main`

BROWSER_URL: `http://localhost:4323/` (Astro auto-selected this port; 4321 and 4322 were already occupied by other dev-server instances serving identical working-tree content)

BROWSER_VERSION: **WORKING_TREE**

UNCOMMITTED_PRODUCT/VISUAL_FILES:
- Modified: `app/src/components/AppFooter.astro`, `AppHeader.astro`, `ChildMessage.astro`, `CoachMessage.astro`, `EvidenceBadge.astro`, `QuickModePattern.astro`, `app/src/layouts/BaseLayout.astro`, `app/src/pages/design-system.astro`, `app/src/pages/incepe-aici.astro`, `app/src/pages/index.astro`, `app/src/pages/principii/[slug].astro`, `app/src/styles/global.css`, `app/src/styles/print.css`, `app/src/styles/tokens.css`, `astro.config.mjs`, `config/visual-tokens.json`
- Untracked (new): `app/src/components/HeroBallFlight.astro`, `HomepageHero.astro`, `ManualFCLogo.astro`, `TacticalMotif.astro`, `plans/MANUALFC-visual-identity-v1.md`, `public/`
- Net diff: 16 tracked files changed, 431 insertions / 959 deletions

The rendered homepage (new hero, ball-flight motif, new logo mark) only exists because of these uncommitted files — HEAD alone would not produce what is currently in the browser. This is a live, uncommitted visual-identity pass layered on top of the last committed navigation-repair baseline.

---

## EXECUTIVE VERDICT

PRODUCT_STATUS: `REPAIR_REQUIRED`

VISUAL_STATUS: `ACCEPTABLE_WITH_FRICTION` — the new hero/brand pass (`HomepageHero`, `ManualFCLogo`, `HeroBallFlight`) is a genuine, professional-looking upgrade over a plain content site, but it ships with one universal layout bug and coexists with an internal-only "Brand Lab" page wired straight into primary navigation.

PRODUCT_COHERENCE: The editorial system (principles → chapters → Gold Standard → exercises → sessions) is written with real discipline and a consistent voice. But the product is not fully "assembled": one entire pillar (assessment) has no page at all, the primary curriculum (Volumes) is invisible from navigation, and the flagship field-pilot content (all 5 exercises) contains an unfixed authoring placeholder. This reads as a strong content system with an incompletely wired interface, not a fragmented "many prototypes" product — the fragmentation is structural/wiring, not stylistic.

FIELD_PILOT_GATE: `PAUSE_FOR_PRODUCT_REPAIRS`

---

## CORE TESTS

NEW_COACH_UNDERSTANDING: **YES** — homepage value proposition, audience (U11), and the "learn deeply vs. solve now" split are immediately clear without any repository knowledge.

NAVIGATION: **PARTLY** — top-level sections (Începe aici, Principii, Am nevoie acum, Gold Standard) are reachable and labeled in plain Romanian. But Volumes (the actual curriculum spine) are not in navigation at all, and "Resurse" in the same nav bar is an internal dev tool, not a coach resource.

IMMEDIATE_HELP: **YES** — the exact scenario in this brief ("copiii se ascund în spatele adversarului") is answered directly and fast by `/gold-standard/rapid`, hitting all six required questions (see §17). Caveat: this works because it happens to be the one problem currently built, not because a search/lookup exists.

DEEP_LEARNING: **PARTLY** — chapter content is substantive and well-argued, but body text periodically breaks into raw internal citation codes and bare `.md` filenames that a coach cannot act on.

GOLD_STANDARD_BROWSER_ONLY: **PARTLY** — Quick Mode is excellent and fully self-contained. Deep Mode explains the concept and evidence but its "Evaluare și transfer" section is text-only; the actual ASM-0001 assessment has no page to visit.

SES0001_BROWSER_ONLY: **PARTLY** — the session plan is strong and genuinely runnable (timed blocks, exact coaching lines, observation focus, closing reflection). It is missing an at-a-glance equipment/headcount/logistics summary, forcing the coach to open three separate exercise pages to assemble a kit list.

VISUAL_EXTERNAL_PILOT_QUALITY: **PARTLY** — first impression is strong, but the same empty band artifact appears above the hero at every tested breakpoint (1440/1280/768/390), and the primary nav's 5th item points at an internal lab page.

ONE_COHERENT_PRODUCT: **PARTLY** — one voice, one visual language, one component system throughout. The break is architectural: some pillars (exercises, sessions, chapters, principles) are fully wired into pages; one pillar (assessment) exists only as data; navigation exposes an internal tool and omits a real one (Volumes).

---

## VISUAL AUDIT

FIRST_IMPRESSION: Homepage at 1440px is genuinely strong — full-bleed photographic hero, confident headline ("Înțelege copilul. Antrenează jocul."), two clearly differentiated CTAs (learn / solve now), a real principle excerpt, a 6-item value list, and a closing CTA band. This does not read as an internal prototype. It reads as a funded product's marketing homepage.

BRAND_CONSISTENCY: Logo, navy/gold/cream palette, and card system are consistent across homepage, Începe aici, Principii, Volumes, Gold Standard, exercises, and sessions. One real exception: `/design-system` uses the same visual chrome (header/footer) but its content is an internal brand/motion lab, explicitly labeled on-page "INTERNAL / DEVELOPMENT ONLY — Laborator intern de brand și interfață; nu este conținut editorial public" — and it is reachable from the same global nav as every real page (as "Resurse").

TYPOGRAPHY: Heading hierarchy is clear and confident (large serif-weight display headings, readable body sizes). Romanian diacritics render correctly everywhere sampled. No orphaned all-caps walls; eyebrow labels use small-caps sparingly and consistently.

SPACING: Section rhythm on content pages (chapters, exercises, sessions) is generous and consistent — clear visual separation between "Ce le spui," "Desfășurare," "Reguli," etc. No cramped or overlapping text was found in body content at any breakpoint.

COLOR/CONTRAST: Navy-on-cream and white-on-navy body text both read as high contrast on inspection. Gold is reserved for accents/CTAs, not used for body text (good — would fail contrast). No contrast violations observed in sampled pages.

COMPONENT_CONSISTENCY: Evidence badges ("DOVEZI · Moderate/Limitate/Practică profesională") are visually consistent wherever they appear as the styled badge component. The break is that not all evidence citations use this component — see CONTENT_PRESENTATION findings below.

RESPONSIVE: See dedicated section. One defect (ball-flight band) reproduces at every breakpoint tested.

MOBILE: Layout stacks cleanly, text stays readable, CTAs remain full-width and tappable, the `<details>/<summary>`-based hamburger menu is a robust, keyboard-accessible native pattern and lists all 5 nav items correctly. Minor polish gap: the open menu has no backdrop and visually overlaps the still-visible hero heading behind it.

VISUAL_FRAGMENTATION: No "two different design generations" visible to the user in content pages — `VISUAL_SYSTEM_A` vs `VISUAL_SYSTEM_B` as feared in the brief was **not confirmed** as a user-facing split. The actual fragmentation is that `/design-system` is a *third*, explicitly internal system that leaks into primary nav, not a rival consumer-facing design language.

---

## PRODUCT AUDIT

HOMEPAGE: Strong, complete, on-brand. Two clear entry paths. No placeholder or dev content visible on the page itself.

INCEPE_AICI: Clear orientation page; explains the "two speeds" model (deep learning vs. field intervention) and the 5-step O→I→A→E→R-style working model in plain language. No repository knowledge required.

VREAU_SA_INVAT: Reachable from homepage and Începe aici. Leads to Principii, not directly to Volumes — see Volume discoverability finding.

AM_NEVOIE_ACUM: Both homepage buttons ("Am nevoie acum" and "Caută o problemă") and the nav item all point to the single `/gold-standard/rapid` page. There is no search or picker — the CTA implies a lookup tool across problems, but only one problem currently exists.

VOLUME_01–04: All four exist, render correctly (`/volum/01`…`/volum/04`, all HTTP 200, correct distinct titles), and chain forward via a "Volumul 0X →" link. **None are linked from primary or footer navigation.** The only entry point into the entire Volume system is one inline text link ("volumele complete") inside a paragraph on `/principii`. There is no `/volum` index page.

PRINCIPII: `/principii` lists all 25 canonical principles, grouped under 6 category headings, each with title + one-sentence summary linking to a full principle page. Two of the six categories ("Comunicare" and a separate "Comunicare și feedback") look like an unresolved split — the second contains a single item that reads as though it belongs in the first.

GOLD_STANDARD_QUICK: Excellent. See §Field Pilot Journey.

GOLD_STANDARD_DEEP: Strong concept + evidence overview, clean exercise/session tables. Undercut by a raw internal-status paragraph at the very bottom exposing a file path and a status enum verbatim (see Internal Terminology Leakage).

EXERCISES: All 5 (EX-0001…EX-0005) render, are well structured (setup, exact coaching line, sequence, rules + rationale, a 7-dimension pedagogical justification grid, common-error diagnosis, regression/progression, phrases to avoid, transfer signal). All 5 also contain the literal unreplaced string `EXERCISE_SPECIFIC_PARAMETER` in visible body text — this is a systemic content bug, not a one-off typo.

SESSIONS: SES-0001 is genuinely excellent as a runnable plan — timed blocks, exact lines to say, "why now," and observation focus per block, closing reflection questions, and a match-transfer theme. Missing an equipment/headcount-at-a-glance summary.

ASSESSMENT: **No page exists.** `/gold-standard` only lists the 5 evaluation criteria as plain text. The underlying data (`data/assessments/assessment-sprijin-si-unghi-de-pasa.json`) exists but there is no Astro route rendering ASM-0001 as a product page (confirmed: only `index.astro`, `rapid.astro`, `sedinte/[id].astro`, `exercitii/[id].astro` exist under `app/src/pages/gold-standard/`).

FIELD_TOOLS: The "Quick Field Card" pattern shown on `/design-system` (internal lab) does not appear to have a corresponding public-facing route; field tools as such are not separately discoverable in the real product outside of exercise/session pages themselves.

---

## FIELD PILOT JOURNEY

CAN_PREPARE_SES0001_WITH_BROWSER_ONLY: **PARTLY**

What works: `/gold-standard` → SES-0001 → EX-0001/0002/0003 gives a coach the full running order, timing, exact coaching language, and what to watch for. This alone is enough to walk onto the pitch.

MISSING_INFORMATION:
- No single "what to bring" list (balls, cones/vests, numbers needed) — has to be pieced together from three separate exercise pages.
- No rendered tactical diagram anywhere — visual specs exist only as an internal markdown reference ("niciun fișier grafic produs încă"), so setup has to be inferred entirely from prose.
- The assessment referenced in "Evaluare și transfer" (used to judge whether the session worked) is not a real page a coach can open on the pitch.

FRICTION:
- `EXERCISE_SPECIFIC_PARAMETER` sitting inside the "Reguli și motivul lor" rationale on every exercise page reads as broken/unfinished, undermining confidence at the exact moment a coach is deciding whether to trust the rule.
- Bare citation codes (`CLM-0097`, `CLM-0099/CLM-0100`) and a literal file reference (`CONCEPT_MODEL.md, secțiunea 3`) inside SES-0001's own rationale text.

---

## RESPONSIVE FINDINGS

DESKTOP (1440 / 1280): Hero and content render cleanly; one universal defect — see below.

TABLET (768): Full nav stays inline (no hamburger needed); same universal defect reproduces; no overflow, clipping, or broken stacks found elsewhere.

MOBILE (390): Layout stacks correctly, CTAs full-width and tappable, hamburger menu functions and is keyboard-accessible (native `<details>/<summary>`, not a JS-only div). Same universal defect reproduces; open-menu panel has no backdrop and visually overlaps hero text behind it (cosmetic).

**Universal defect — confirmed at all four breakpoints (1440/1280/768/390):** an empty ~44–52px band, colored by the page's cream background, appears between the header and the hero banner on the homepage. Root cause: `app/src/pages/index.astro:12` renders `<HeroBallFlight />` as an independent full-width block *before* `<HomepageHero />` rather than positioning it as an overlay within the hero. `HeroBallFlight.astro` sets `.ball-flight { position: relative; height: 52px }` (44px under `@media (max-width:700px)`), so it always occupies its own visible strip in normal document flow instead of being absorbed into the dark hero background.

---

## ACCESSIBILITY FINDINGS

- Mobile nav toggle uses a native `<details>/<summary>` element with an explicit `aria-label` — a robust, keyboard-operable pattern; no defect found here.
- Skip-to-content link present on every page ("Sari la conținutul principal").
- Heading order in sampled pages (h1 → h2 → h3) is sequential and logical; no skipped levels observed.
- No obvious color-contrast violations found on sampled pages (navy/cream/white combinations all read as high contrast).
- Astro's built-in dev toolbar (fixed unlabeled buttons, bottom of viewport) is a development-only artifact of `npm run dev` — it does not ship in a production build (`astro build`) and should not be scored against the product, but it does visually intrude into full-page screenshots taken during this audit.

---

## TECHNICAL BROWSER FINDINGS

CONSOLE_ERRORS: None from actual product navigation. The single 404 logged during this audit was a self-inflicted wrong-case URL guess (`/gold-standard/exercitii/ex-0001` lowercase) made before discovering the real link casing (`EX-0001`); all real in-product links use consistent casing and were not affected.

BROKEN_LINKS: None found. All 25 principle slugs linked from `/principii` return 200. All 4 volume routes return 200. All 5 exercise routes and both session routes return 200.

FAILED_RESOURCES: None observed beyond the self-inflicted 404 above.

STALE/DEV ARTIFACTS: Dev-mode HTML includes `data-astro-source-file` / `data-astro-source-loc` attributes and the Astro Dev Toolbar — both exclusive to `astro dev` and absent from production builds; noted for completeness, not scored as product defects.

---

## CRITICAL FINDINGS

1. **Internal "Brand/UI Lab" page is wired into primary global navigation and footer on every page.**
   USER-VISIBLE SYMPTOM: The nav item "Resurse" and footer link "Metodologie și resurse" both lead to `/design-system`, a page whose own banner reads "INTERNAL / DEVELOPMENT ONLY — Laborator intern de brand și interfață; nu este conținut editorial public." A real coach clicking the most rightward, differently-colored nav item lands on an internal styleguide, not a coaching resource.
   LIKELY IMPLEMENTATION CAUSE: Nav/footer links hard-coded to the design-system route instead of a real resources page (or omitted entirely pending one).
   FILES INVOLVED: `app/src/components/AppHeader.astro:27,38`, `app/src/components/AppFooter.astro` (equivalent footer link), `app/src/pages/design-system.astro`.

2. **All 5 field-pilot exercise pages contain an unreplaced content placeholder, `EXERCISE_SPECIFIC_PARAMETER`, in visible body text.**
   USER-VISIBLE SYMPTOM: On EX-0001 through EX-0005, the "Reguli și motivul lor" and "Dimensiuni teren" rationale text reads, e.g., "Dimensiuni EXERCISE_SPECIFIC_PARAMETER, nu prag validat de cercetare." — a literal unfilled template token shown to the coach as if it were an explanation.
   LIKELY IMPLEMENTATION CAUSE: Content-authoring omission at the data layer — the placeholder is baked directly into the source JSON, not a template bug.
   FILES INVOLVED: `data/exercises/exercise-recunoasterea-umbrei-defensive.json:37,97` and the equivalent field in `exercise-creeaza-optiunea-sub-presiune.json`, `exercise-primeste-gata-sa-continui.json`, `exercise-sprijin-cu-doi-coechipieri.json`, `exercise-transferul-in-joc-mic.json`; rendered as-is by `app/src/pages/gold-standard/exercitii/[id].astro`.

3. **The ASM-0001 assessment has no product page.**
   USER-VISIBLE SYMPTOM: `/gold-standard`'s "Evaluare și transfer" section only lists 5 criteria as plain bullet text tied to exercise numbers; there is no page a coach can open to actually use the assessment.
   LIKELY IMPLEMENTATION CAUSE: Assessment content exists only as data (`data/assessments/assessment-sprijin-si-unghi-de-pasa.json`, referenced in `plans/TASK-2206-evaluare-si-transfer.md` and its tests) with no corresponding Astro route ever built — `app/src/pages/gold-standard/` contains only `index.astro`, `rapid.astro`, `sedinte/[id].astro`, and `exercitii/[id].astro`, no assessment route.
   FILES INVOLVED: `data/assessments/assessment-sprijin-si-unghi-de-pasa.json`; missing: `app/src/pages/gold-standard/evaluare/[id].astro` (or equivalent).

---

## MAJOR FINDINGS

1. **Internal terminology leaks into body copy across multiple page types.** Raw evidence codes (`CLM-0022`, `CLM-0038`, `CLM-0097`, …) and bare `.md` filenames (`CH_0101_TASK_ADAPTATION_SCALE.md`, `CH_0101_VARIABILITY_GRID.md`, `docs/gold-standard/TACTICAL_VISUAL_SPECS.md`, `CONCEPT_MODEL.md`) appear as plain inline text in chapter (`/volum/01/ch-0101`), exercise, Gold Standard, and session pages — none of these are links or explained; a coach cannot act on them. Files: `app/src/pages/volum/01/ch-0101.astro` (or its content source), `app/src/pages/gold-standard/index.astro`, `data/exercises/*.json`, session data behind `sedinte/[id].astro`.

2. **The Volume curriculum (V01–V04) is invisible from navigation.** Not present in the header or footer nav; the only path in is one inline text link on `/principii`, then sequential "next volume" links. No `/volum` index exists. A coach who trusts the main nav will never find it. Files: `app/src/components/AppHeader.astro`, `AppFooter.astro`, `app/src/pages/principii/index.astro` (or equivalent).

3. **Universal empty band between header and hero at every tested breakpoint.** See Responsive Findings above for full root-cause detail (`app/src/pages/index.astro:12`, `app/src/components/HeroBallFlight.astro`).

4. **No tactical diagrams are actually rendered anywhere in the product.** Every exercise and the Gold Standard overview state visuals are "specificate semantic," with zero graphic files produced. Section 36 of this audit's own brief expected inspectable visuals; there are currently none to inspect — setup must be inferred entirely from prose. This is a legitimate, honestly-disclosed gap, not a rendering bug, but it materially reduces field-readiness of the exercise library.

---

## MODERATE FINDINGS

1. Session pages (SES-0001, and by pattern SES-0002) do not summarize equipment/headcount/logistics in one place; a coach must open each linked exercise to assemble a kit list before training.
2. "Justificarea pe 7 dimensiuni" grid on exercise pages leaves a visibly empty 8th cell (odd count in a 2-column layout) — reads as a missing or broken card, not intentional whitespace.
3. `/principii` has two adjacent categories, "Comunicare" (5 items) and "Comunicare și feedback" (1 item), that read as an unresolved content split rather than a deliberate taxonomy.
4. "Caută o problemă" / "Am nevoie acum" nav and CTA labeling implies a searchable problem library; currently there is exactly one problem ("sprijinul și unghiul de pasă"). Not misleading once visited, but sets an expectation the current build can't fulfill.

---

## MINOR FINDINGS

1. Mobile hamburger menu panel has no backdrop/dimming and visually overlaps the hero heading behind it while open.

## COSMETIC FINDINGS

1. Astro Dev Toolbar (fixed unlabeled buttons) intrudes into full-page screenshots during `npm run dev`; absent from production builds, informational only.
2. Dev-only `data-astro-source-file`/`data-astro-source-loc` attributes present in rendered HTML during `npm run dev`; absent from production builds.

---

## TOP 10 PRODUCT IMPROVEMENTS

Ranked by impact × urgency × field usefulness.

1. **Remove or gate `/design-system` out of primary nav/footer.**
   Why it matters: an internal-only page is one click away from every real page, undermining "professional product" perception instantly.
   User impact: high — first thing a skeptical new coach might click.
   Likely area: `AppHeader.astro`, `AppFooter.astro`.
   Severity: CRITICAL.
   Recommended action: replace with a real resources page, or remove the nav item until one exists.

2. **Fill the `EXERCISE_SPECIFIC_PARAMETER` placeholder in all 5 exercise JSON files.**
   Why it matters: it's on the exact content (rules and rationale) a coach is trusting on the pitch tomorrow.
   User impact: high — trust-breaking, appears in the flagship field-pilot content.
   Likely area: `data/exercises/*.json`.
   Severity: CRITICAL.
   Recommended action: content-authoring pass to replace with the real per-exercise parameter description.

3. **Build the ASM-0001 assessment page.**
   Why it matters: assessment is one of the four pillars this audit brief itself treats as mandatory (§22); it currently doesn't exist as a product surface at all.
   User impact: high for anyone trying to close the loop on a training block.
   Likely area: new route under `app/src/pages/gold-standard/`.
   Severity: CRITICAL.

4. **Surface Volumes in primary navigation and add a `/volum` index.**
   Why it matters: this is the actual deep-learning curriculum the homepage promises ("Vreau să învăț"); it's currently undiscoverable.
   User impact: high for the "deep learning" persona.
   Likely area: `AppHeader.astro`, new `app/src/pages/volum/index.astro`.
   Severity: MAJOR.

5. **Fix the empty header-to-hero band (reposition `HeroBallFlight` as an in-hero overlay).**
   Why it matters: visible on literally every homepage load at every screen size — the single most repeatable visual defect found.
   User impact: medium-high — first impression, but not blocking.
   Likely area: `index.astro`, `HeroBallFlight.astro`.
   Severity: MAJOR.

6. **Strip or translate raw `CLM-xxxx` codes and `.md` filenames out of body copy.**
   Why it matters: breaks the "written for a coach" voice at exactly the moments meant to build trust (evidence, rationale).
   User impact: medium — confusing, not blocking.
   Likely area: chapter/exercise/session content source and the components rendering evidence citations (compare with the working `EvidenceBadge` component already used elsewhere).
   Severity: MAJOR.

7. **Add a one-glance logistics/equipment summary to session pages.**
   Why it matters: directly serves "can I leave for training now" (§21).
   User impact: medium — real friction, workaround exists (open each exercise).
   Likely area: `sedinte/[id].astro` template + session data.
   Severity: MODERATE.

8. **Resolve the "Comunicare" vs "Comunicare și feedback" category split on `/principii`.**
   Why it matters: makes the 25-principle index feel curated rather than partially sorted.
   User impact: low-medium.
   Likely area: principle category metadata.
   Severity: MODERATE.

9. **Reconcile the "Caută o problemă" CTA with actual current scope (one problem).**
   Why it matters: sets an expectation ("search") the product can't yet meet; low-cost relabel avoids future disappointment as more problems ship.
   User impact: low-medium.
   Likely area: homepage copy, `AppHeader.astro` nav label.
   Severity: MODERATE.

10. **Add a backdrop behind the open mobile nav menu.**
    Why it matters: pure polish, but cheap to fix and improves perceived quality on the device most coaches will actually use pitch-side.
    User impact: low.
    Likely area: mobile nav CSS in `AppHeader.astro`/`global.css`.
    Severity: MINOR.

---

## CURRENT VISUAL BASELINE

WORKING_TREE_DIFFERS_FROM_HEAD: **YES** — substantially; see file list at top of this report.

SHOULD_CURRENT_VISUAL_VERSION_BECOME_BASELINE: **YES_AFTER_TARGETED_REPAIRS**

WHY: The uncommitted visual-identity pass (new hero, new logo mark, ball-flight motif, refreshed header/footer/card styling) is a real quality improvement over what HEAD alone renders, and it introduces no regressions in the pages it touches beyond the one universal band bug. It should become the baseline once (a) the band bug is fixed, and (b) the `/design-system` internal-lab nav link is removed or replaced — both are small, targeted, and don't require redesigning anything already working.

---

## PRODUCT MATURITY

`FUNCTIONAL_PROTOTYPE`

Reasoning: navigation works, no broken links, five field-pilot exercises and two sessions are content-complete and largely well written, and the "Am nevoie acum" flow genuinely solves a real coach's problem in under a minute. But a mandatory pillar (assessment) has zero product surface, the primary curriculum (Volumes) is undiscoverable, and the flagship field content contains an unfixed authoring placeholder on every single exercise page. That combination — real strength in what's wired up, real gaps in what's missing or mis-wired — is squarely "functional prototype," not yet "field pilot product."

---

## FINAL RECOMMENDATION

### B — `RUN_TARGETED_PRODUCT_REPAIR_BEFORE_FIELD_PILOT`

The content quality, voice, and pedagogical discipline are already at a level worth protecting — this is not a case for broader rework or a visual reconciliation project. The three CRITICAL findings (internal lab in nav, placeholder text in every exercise, missing assessment page) are each narrow and mechanical to fix, not design problems. Repairing them, plus the universal hero-band bug and the Volume-discoverability gap, would very plausibly move this to `GO` or `GO_WITH_MINOR_FRICTION` for PHASE-23 Round 1 without touching anything currently working well.

---

## NEXT TASK

Smallest coherent next task (not executed — diagnosis only, per this audit's scope):

**"Field-pilot blocker repair pass"** — fix, in one pass: (1) remove/replace the `/design-system` nav+footer link, (2) replace `EXERCISE_SPECIFIC_PARAMETER` in all 5 exercise JSON files with real content, (3) reposition `HeroBallFlight` so it no longer produces the empty header-to-hero band. Treat the ASM-0001 page and Volume-navigation-surfacing as a follow-up task, since both are net-new page/nav work rather than repairs to existing pages.
