# MANUALFC — MASTER FINAL-PRODUCT GAP AUDIT V2

**Statut:** READ-ONLY audit · runtime neschimbat · **Data:** 2026-08-31
**Companion document:** `docs/product/MANUALFC_FINAL_PRODUCT_FEATURE_LEDGER_V2.md` (item-by-item evidence)

---

## Method note

This audit was produced by dispatching 7 independent read-only research agents across non-overlapping domains (knowledge/education, decision-support/practice/coach-development, content-breadth/targets, multimedia deep-dive, field-validation/offline/workspace, accounts/commercial/academy/scale, governance/history), each required to cite exact file paths, counts, and quotes rather than recall. All scoring, synthesis, and judgment calls below were made directly by the auditing assistant from that evidence — no agent was asked to score or rate anything itself, per the instruction that understanding may not be delegated.

---

## EXECUTIVE COMPLETION

| Score | Value | Basis |
|---|---:|---|
| KNOWLEDGE_COMPLETION | **68%** | Weighted: research/evidence architecture maturity (90%), Pedagogul/Antrenorul content maturity for what exists (~87%), competency framework product-linkage (31–45%), Knowledge Graph (explicitly non-engine, 35%), Theory-Practice Contract applied to 100% of a tiny corpus (40%) |
| PRODUCT_CAPABILITY_COMPLETION | **50%** | Decision Engine (85%), Practice/Gold Standard mechanism (85%), Reflection (45%), Workspace (82%), Offline for its declared scope (80%), Search (55%), Multimedia infrastructure (55%), Coach Development (18%), Accounts/Cloud (5%), Academy (0%) |
| CONTENT_COMPLETION | **30%** | Dominated by the two largest canonical targets: Exercises 5/60 (8.3%), Sessions 2/36 (5.6%), Scripts 0/50 (0%), Case studies 0/15 (0%); offset upward by mature Pedagogul/Antrenorul chapter corpus and Problems at its stated floor |
| COMMERCIAL_READINESS | **8%** | Zero accounts, zero billing, zero privacy/consent UX, zero analytics; only a working deploy pipeline and free-tier onboarding exist |
| **WEIGHTED_FINAL_PRODUCT_COMPLETION** | **≈ 41%** | `(68×0.25) + (50×0.30) + (30×0.25) + (8×0.20)` = 17 + 15 + 7.5 + 1.6 = **41.1%** |
| **ESTIMATED_RANGE** | **36% – 47%** | Judgment-based scoring; the range reflects genuine uncertainty in weighting Pedagogul/Antrenorul chapter maturity against raw exercise/session breadth, not false precision |
| CORE_SYSTEM_COMPLETENESS | **≈ 75%** | Research (90%), Pedagogul (85%), Antrenorul (85%), Decision Engine (80%), Gold Standard V2 mechanism (85%), Field Mode (85%), Reflection (55%), Workspace (80%), Knowledge Graph (35%), Offline foundations (75%) — averaged |
| PUBLIC_COMMERCIAL_READINESS | **≈ 6%** | Heavily penalized per instruction for missing accounts/cloud/billing/entitlements/privacy/analytics/content breadth/human validation/real multimedia — nearly all absent simultaneously |

### Why core-system completeness is high while final-product and commercial readiness are low

ManualFC's **engine** — the research/evidence pipeline, the Pedagogul/Antrenorul knowledge base, the Decision Engine, the Gold Standard V2 exercise/session data model, Field Mode, and local-first Workspace/offline foundations — is genuinely mature, well-tested, and self-correcting (it caught and repaired its own research fabrication in DEC-0040, its own H1-overflow regression in DEC-0077, its own contrast defect in DEC-0078). Measured as an *engine*, it is roughly three-quarters complete.

But a **final commercial product** is not an engine — it is an engine plus enough content to be useful (currently 5 of 60 exercises, 2 of 36 sessions, 0 of 50 scripts, 0 of 15 case studies), plus real demonstration media (currently zero real video/footage of any kind), plus the ability to actually sell and support it to real customers (currently zero accounts, zero billing, zero privacy UX, zero analytics), plus proof that any of it actually teaches coaches anything (`HUMAN_LEARNING_VALIDATION = NOT_YET_RUN`, unchanged since the concept was first named). Each of these four gaps is large and independent — none is masked by the others being strong. This is why the weighted score sits near 41% even though the underlying engine is much further along.

---

## MULTIMEDIA

| Score | Value |
|---|---:|
| MULTIMEDIA_OVERALL | **~20%** |
| STATIC_VISUAL (M1) | 75% (of current 5-exercise/8-problem corpus) |
| TACTICAL_MOTION (M2) | 50% (of current corpus) |
| EXERCISE_DEMONSTRATION (M3) | 20% (1 of 5 exercises has a full-cycle animation) |
| COACH_EDUCATION_DEMONSTRATION (M4) | 15% (3 text scripts exist, explicitly not recordings; 0 actual videos) |
| REAL_FIELD_VIDEO (M5) | **0%** |
| MATCH_TRANSFER_VIDEO (M6) | **0%** |
| **USER_CONCERN_VIDEO_GAP** | **CONFIRMED** |

### Evidence for USER_CONCERN_VIDEO_GAP = CONFIRMED

Exhaustive repository-wide search for video files (`.mp4/.webm/.mov/.avi/.mkv`) returned **zero results**. A search for `<video` tags in the codebase returned exactly one hit — a source-code comment stating a component is "ready to be swapped for a real `<video>`... later without changing the data shape," never an actual rendered video element. The product's own internal architecture documents (`docs/architecture/MULTIMEDIA_PRODUCTION_PIPELINE.md`, `MULTIMEDIA_FOUNDATION.md`, `PROBLEM_MULTIMEDIA_MAPPING.md`) independently and repeatedly state, in their own words, that no real footage exists, no consent process has ever been executed, and a fully-documented 9-stage real-footage production pipeline (consent → filming → editing → pedagogical review → anonymization → subtitling → transcription → poster → registry entry) has had **zero of its 9 stages executed**. Every "multimedia" asset that does exist is one of: hand-authored inline SVG (5 diagrams), CSS-keyframe SVG loop animations (4), one CSS full-cycle animation, or plain text "scripts" describing what a future recording would say (3, explicitly labeled on-page as "not a real recording"). The infrastructure to eventually hold real video (media registry schema, `REAL_FOOTAGE`/`REAL_FIELD_EXAMPLE`/`MATCH_TRANSFER_EXAMPLE` enum values) exists and is unusually well-built and honestly gated — but it currently holds zero instances of any of those types.

**Conclusion: the user's suspicion is not merely plausible — it is fully confirmed by direct, exhaustive evidence, and the project's own internal documentation says the same thing about itself.**

---

## CONTENT BREADTH

| Item | Current | Target | % | Evidence |
|---|---:|---:|---:|---|
| PROBLEMS | 8 | 8 (schema-stated minimum; no larger target found) | 100% of floor | `schemas/problem.schema.json` `minItems:8` |
| PRINCIPLES | 25 | no canonical target found | n/a (treated complete) | `data/principles/*.json` |
| EXERCISES | 5 | 60 | **8.3%** | `data/exercises/*.json`; `project.schema.json minimum_deliverables.exercises` |
| SESSIONS | 2 | 36 | **5.6%** | `data/sessions/*.json` |
| ASSESSMENTS | 1 | no canonical target found | n/a | `data/assessments/*.json` |
| PEDAGOGUL (lessons) | 10 | no larger canonical target found beyond current accepted V1 | ~88% (mature, accepted) | `content/volume-01/*.mdx` |
| ANTRENORUL (lessons) | 21 | no larger canonical target found beyond current accepted V1 | ~85% (mature, accepted) | `content/volume-03/04/*.mdx` |
| CASE_STUDIES | 0 | 15 | **0%** | `data/case-studies/README.md` (future-tense placeholder only) |
| COMMUNICATION_SCRIPTS | 0 | 50 | **0%** | `data/communication-scripts/README.md` (placeholder only) |
| MEDIA_OBJECTS (real/simulated, excl. video) | 15 registry entries | no canonical numeric target found | see Multimedia section for maturity breakdown | `data/media/media-registry.json` |

**Critical governance finding**: the canonical target line `"Planificat: 60 exerciții, 36 ședințe, 50 scripturi, 15 studii de caz"` printed by `scripts/validate_project.py` is computed by counting **planned task-batch titles** in `TASK_REGISTRY.json` (e.g. 15 tasks titled "Lot exerciții N — 4 exerciții," all currently `PENDING`), not by counting actual files in `data/`. This is exactly the kind of "task completion gaming" this audit was explicitly instructed to reject (§31/§56 of the master prompt) — the validator reports the *plan* as if reporting *progress*, and it is entirely legitimate for it to print "0 errors" while the real content behind that plan is 5/60 and 2/36. This is not a defect in the validator's job (it correctly checks that the registry is internally consistent) — but it is a real risk that reading "Planificat: 60 exerciții..." casually could be mistaken for a current-state claim. **All 15 exercise batches and all 18 session batches are `PENDING`, with zero attempts recorded.**

---

## CORE PRODUCT

| Component | Status | % | Note |
|---|---|---:|---|
| RESEARCH | MATURE | 90% | 361 sources / 380 claims / 408 citations, cross-referenced, self-correcting |
| PEDAGOGUL | BUILT | 88% | 10/10 chapters, substantive, accepted V1 |
| ANTRENORUL | BUILT | 85% | 21/21 chapters, substantive, accepted V1; one honestly-declared gap (COACH-C06 cueing, no dedicated chapter) |
| DECISION_ENGINE | MATURE | 85% | Real, working, honestly degrades when data is missing rather than fabricating |
| GOLD_STANDARD_V2 | FUNCTIONAL_BUT_PARTIAL | 85% mechanism / 7% breadth | The mechanism (schema, validator, product surfacing) is excellent; applied to only 5 exercises + 2 sessions |
| FIELD_MODE | MATURE | 85% | Fully built, V2-aware, one-segment-one-screen preserved |
| GROUP_CONFIGURATOR | MATURE | 85% | 6 player counts × 2 coach counts, fails closed honestly |
| WORKSPACE | MATURE | 82% | Session builder, saved/favorites/recents, continue-where-left-off all real |
| REFLECTION | FUNCTIONAL_BUT_PARTIAL | 45% | V1 tool mature; V2 dual-dimension data exists on sessions but is not yet wired into the personal reflection form itself |
| OFFLINE | FUNCTIONAL_BUT_PARTIAL | 75% (for its declared "prepared session" scope) | Real service worker, real manifest; explicitly never promises full-site offline |
| SEARCH | FUNCTIONAL_BUT_PARTIAL | 55% | Real client-side search over 6 categories; no competency search, no media search, no dedicated Pedagogul/Antrenorul category |

---

## COACH DEVELOPMENT

| Link in the desired loop (§20) | Present? | Evidence |
|---|---|---|
| COMPETENCY (definition) | YES | 13 PED-C + 18 COACH-C defined |
| → BASELINE | **NO** | Zero code/data anywhere measures a coach's starting competency level |
| → SESSION_FOCUS | YES | `coach_focus`/`coach_objectives` on all existing exercises/sessions |
| → OBSERVED_BEHAVIOUR | PARTIAL | `observation_focus`/`understanding_check` exist but describe the *child's* behavior, not the coach's own |
| → REFLECTION | PARTIAL | `coach_reflection`/`reflection_v2.coach_dimension` exist as data; not yet surfaced as a guided input in the actual reflection tool |
| → FEEDBACK | **NO** | No external/mentor feedback mechanism of any kind |
| → NEXT_DEVELOPMENT_GOAL | **NO** | Zero code |
| → RECOMMENDED_LEARNING/PRACTICE | **NO** | Zero code |
| → LONGITUDINAL_HISTORY | **NO** | Zero code (`grep "longitudinal"` = 0 hits repo-wide) |

**OVERALL: NOT_STARTED as an end-to-end loop (3 of 9 links present, all partial).** Per the master prompt's own explicit instruction, this audit does **not** count the presence of reflection data as "Coach Development complete" — it is one link among nine, and the four most differentiating links (baseline, feedback, next-goal, longitudinal history) are entirely absent.

---

## VALIDATION

| Type | Status |
|---|---|
| FIELD_VALIDATION | **BLOCKED, unchanged since DEC-0047 (PHASE-23).** Only two artifacts exist: a field-prep sheet and a blank return template. No filled-in pilot data has ever been recorded. Every subsequent phase (29 through 33) reconfirms this is unchanged. |
| HUMAN_LEARNING_VALIDATION | **NOT_YET_RUN.** A real test protocol exists (`docs/ux/MANUALFC_EDUCATIONAL_PAGE_USER_TEST_PROTOCOL.md`) but has never been executed against real coaches; explicitly distinguished in every acceptance report from the browser-based Learn/Recall/Apply UX audits, which measure structural correctness, not learning. |
| ROMANIAN_CONTEXT_VALIDATION | Unvalidated — research base is predominantly international/academy-level; this gap is honestly flagged inside individual PHASE-30/32 chapters, not hidden. |
| COMMUNITY_COACH_VALIDATION | Unvalidated — same as above; no community/grassroots-specific coach has used the product. |

---

## CLOUD / PERSONAL

| Item | Status | % |
|---|---|---:|
| ACCOUNTS | NOT_STARTED | 0% |
| PROFILE | Local-only | 20% |
| CLOUD_STATE | NOT_STARTED | 0% |
| SYNC | NOT_STARTED | 0% |
| CROSS_DEVICE | NOT_STARTED | 0% |
| BACKUP_RESTORE | NOT_STARTED | 0% |

---

## COMMERCIAL

| Item | Status | % |
|---|---|---:|
| ENTITLEMENTS | NOT_STARTED | 0% |
| BILLING | NOT_STARTED | 0% |
| SUBSCRIPTIONS | NOT_STARTED | 0% |
| PAYWALL | NOT_STARTED (by explicit design choice for v1) | 0% |
| PRICING | NOT_STARTED | 0% |
| TRIAL | NOT_STARTED | 0% |
| PUBLIC_LAUNCH_READINESS | **Very low** | see PUBLIC_COMMERCIAL_READINESS above |

---

## ACADEMY

| Item | Status | % |
|---|---|---:|
| ORG | NOT_STARTED | 0% |
| ROLES | NOT_STARTED | 0% |
| SHARED_CURRICULUM | NOT_STARTED | 0% |
| SHARED_SESSIONS | NOT_STARTED | 0% |
| COACH_DEVELOPMENT (org-level) | NOT_STARTED | 0% |
| ANALYTICS | NOT_STARTED | 0% |
| **OVERALL** | **NOT_STARTED** | **~1%** |

---

## SCALE

| Item | Status | % |
|---|---|---:|
| MULTI_AGE | Architecture only (`const` schema, provisional order document) — **product is U11-only** | 0% product / 12% architecture |
| MULTILINGUAL | NOT_STARTED | 0% |
| ANALYTICS | NOT_STARTED | 0% |
| OPERATIONS (CI/CD, monitoring, backups) | NOT_STARTED beyond a manual deploy pipeline | 10% |

---

## TOP 10 STRONGEST CAPABILITIES

1. **Evidence/research architecture** — 361 sources, 380 claims, 408 citations, cross-referenced, with a real self-caught-and-corrected fabrication incident (DEC-0040) proving the integrity process actually works under pressure, not just in theory.
2. **Decision Engine** — genuinely honest UI that shows "no exercise exists yet" rather than fabricating a link when data is missing; real observation-first workflow.
3. **Gold Standard V2 data model + validator** — a well-designed, fully additive, backward-compatible schema migration with a dedicated semantic validator that checks real ID existence, not just field presence.
4. **Field Mode** — a genuinely well-built, disciplined "one segment, one screen" live-coaching tool, now V2-aware (coach focus, non-intervention, verification per segment).
5. **Group Configurator + Surface Maps** — deterministic, honest-when-infeasible logistics engine with real generated SVG, avoiding the trap of hand-drawing ~60 static variants.
6. **Local-first Workspace** (saved/favorites/recents/continue/reflection/offline packs) — a mature, coherent personal tool with zero server dependency and zero PII risk.
7. **Offline/PWA foundations for prepared sessions** — a real, working service worker with a fail-closed, honestly-scoped ("prepared session," never "whole site") offline promise.
8. **Pedagogul + Antrenorul content corpus** — 31 substantive chapters, each following a strict evidentiary contract, each independently audited (including a full forensic re-audit after a fabrication scare in DEC-0040/41/42).
9. **Safeguarding content data** — unusually mature, real, citing actual Romanian/EU/FIFA/UEFA sources — a positive surprise, though currently invisible in the product UI (see Top 10 Invisible Gaps).
10. **Institutional self-honesty** — the project's own architecture documents state, in their own words, "no video file exists or is fabricated," "PHASE-23 = FIELD_INPUT_REQUIRED," "HUMAN_LEARNING_VALIDATION: NOT_YET_RUN" — repeatedly, across dozens of files, without prompting. This is a genuine, rare, and valuable engineering-culture asset that should be explicitly preserved going forward.

---

## TOP 20 GAPS (ranked by final-product impact × current gap size × dependency order)

1. **Exercise library breadth (5/60)** — WHY: the core practice system cannot function as a usable coaching manual with 5 exercises. CURRENT: 8.3%. TARGET: 60, matching the Gold Standard V2 mechanism already proven on the 5 that exist. NEXT ACTION: resume the 15 pending exercise batches, applying the already-validated V2 migration pattern to each new batch as it's authored (not as a separate retrofit).
2. **Session library breadth (2/36)** — WHY: same reasoning as #1, one level up. CURRENT: 5.6%. NEXT ACTION: resume the 18 pending session batches.
3. **Real video/demonstration media (0 of everything)** — WHY: this is the single most user-visible gap and the one the user explicitly suspected; confirmed. NEXT ACTION: execute Wave M1-M2 of a multimedia roadmap (below) before attempting real footage, which requires consent infrastructure that doesn't exist yet either.
4. **Human learning validation (NOT_YET_RUN)** — WHY: without this, no claim that ManualFC actually teaches anything can be made with confidence, regardless of how mature the content looks. NEXT ACTION: execute the already-written `MANUALFC_EDUCATIONAL_PAGE_USER_TEST_PROTOCOL.md` with real coaches.
5. **Field pilot (blocked since DEC-0047, PHASE-23)** — WHY: every practice heuristic, cue, and intervention rule in the product remains formally unvalidated by real use. NEXT ACTION: recruit a small controlled pilot (see §47-derived plan below) and actually run it.
6. **Coach Development loop (3 of 9 links present)** — WHY: this was named the "biggest real gap" as far back as DEC-0069 and remains unimplemented as a system, only researched. NEXT ACTION: build baseline + reflection-to-goal linkage as the minimum viable loop before attempting the full 9-link vision.
7. **Communication scripts (0/50) and case studies (0/15)** — WHY: two entire content categories with canonical targets are completely unstarted. NEXT ACTION: decide whether these remain premium-V1 requirements or are explicitly deferred; do not leave them silently at 0% without a decision.
8. **Accounts/cloud (0% implemented despite "architecture ready" framing)** — WHY: no cross-device continuity is possible; a coach who switches phones loses everything. NEXT ACTION: pick one auth/persistence provider and build a real (not just "ready") implementation, once commercial direction is set.
9. **Privacy/consent/GDPR surface (0% — no page exists)** — WHY: this becomes mandatory the moment any account or video-consent flow is built, and mature safeguarding data already exists but is invisible. NEXT ACTION: build a real privacy page and wire the existing safeguarding data into the product UI.
10. **Commercial layer (billing/entitlements/pricing, 0%)** — WHY: there is currently no way to charge anyone for this product. NEXT ACTION: explicitly deferred by the product's own roadmap until usage/WTP validation — correctly sequenced, but the gap remains real and total.
11. **Reflection V2 not wired into the personal tool** — WHY: the dual-dimension reflection model exists as session data but a coach using `/spatiul-meu/reflectie` still only sees the V1 form. NEXT ACTION: extend the reflection form to surface the session's `reflection_v2` prompts as guided input, not just static display on the session page.
12. **Knowledge Graph is a spec, not an engine** — WHY: the product's own specification explicitly declines to build a real graph; discovery/relationship-browsing is limited to whatever's hardcoded in `content-bridge.ts`. NEXT ACTION: decide if a lightweight, real graph data structure is worth building now or should stay deferred — currently undecided by omission.
13. **Search excludes competencies and media** — WHY: a coach cannot search for "COACH-C11" or find all media related to a topic. NEXT ACTION: extend `discovery-index.ts` to index competencies and media entries.
14. **Academy/Club (0%)** — WHY: no path exists to sell to clubs, which the commercialization roadmap itself lists as a monetization variant to test. NEXT ACTION: correctly deferred pending commercial validation; keep deferred.
15. **Multi-age product (0%, architecture only)** — WHY: the product is permanently U11-only until this is built; correctly and explicitly deferred by the product's own vision documents. NEXT ACTION: keep deferred; do not let "architecture ready" framing imply otherwise.
16. **Multilingual (0%)** — WHY: limits total addressable market to Romanian speakers only; correctly deferred. NEXT ACTION: keep deferred until commercial validation.
17. **Analytics/observability (0%)** — WHY: no visibility into what coaches actually use, no error monitoring in production. NEXT ACTION: add privacy-safe, minimal analytics before any real user growth, and basic error monitoring regardless of commercial timing.
18. **CI/CD (0%, no `.github` directory at all)** — WHY: every validation gate in this entire multi-phase project has been run manually by an AI assistant, with no automated enforcement on future changes. NEXT ACTION: add a basic GitHub Actions workflow running the existing validators (`validate_content.py`, `validate_gold_standard_v2.py`, `pytest`, `npm run check/build`) on every PR.
19. **Educational Page System applied to only 19/31 chapters** — WHY: 12 older Antrenorul chapters (volume-03 01-06, volume-04 01-06) lack the Learn/Recall/Apply components that the newer 19 chapters have, creating an inconsistent experience. NEXT ACTION: retrofit the remaining 12 chapters, a well-understood, low-risk mechanical task given the pattern is proven.
20. **`visual_assets` field stale/orphaned on all 5 exercises** — WHY: every exercise's own canonical JSON still says "PENDING — niciun fișier grafic produs" even though real diagrams/animations were built and are live on the page, hardcoded outside that field. This is a real data-consistency defect (not a missing feature) that could mislead a future auditor or developer. NEXT ACTION: update the field to reflect reality, or remove it if superseded.

---

## TOP 10 USER-VISIBLE GAPS (what a coach visiting ManualFC today would notice first)

1. **No video anywhere** — every "demonstration" is a diagram or a short looping animation; nothing moves like a real training session.
2. **Very few exercises and sessions** — 5 exercises and 2 sessions is not enough to plan a season; a coach would exhaust the content in one sitting.
3. **No account / no cross-device continuity** — close the browser on your phone, open it on your laptop, and your saved work isn't there.
4. **No visible sign of other coaches' experience** — no testimonials, no usage numbers, no community signal (there is no analytics or user base to draw on yet, honestly).
5. **No case studies or real-world scenarios** — the "studii de caz" category is entirely empty.
6. **No communication scripts** — a coach looking for ready-made phrases for parent conversations finds nothing (0/50).
7. **Inconsistent depth between chapters** — the 12 older Antrenorul chapters look and feel different (no Quick Recall, no compression toggle) from the 19 newer ones.
8. **No personalization or progress tracking** — nothing remembers what competencies a specific coach has focused on over time.
9. **No search for "what does COACH-C11 mean"** — competency IDs appear as raw unlabeled strings (e.g. "COACH-C01") on exercise/session pages with no glossary or lookup.
10. **Age is fixed at 10-11** — a coach of an 8-year-old or a 14-year-old team finds nothing usable.

---

## TOP 10 INVISIBLE BUT CRITICAL GAPS

1. **Human learning validation never run** — the entire product could be pedagogically ineffective and nothing in the current QA process would catch it, because QA measures structural correctness, not learning outcomes.
2. **Field pilot never run** — every intervention rule, cue, and practice heuristic is unvalidated by a single real training session.
3. **Zero cloud persistence** — a coach's entire history (sessions, reflections, saved content) can be permanently lost by clearing browser data, with no warning or backup path.
4. **Zero CI/CD** — nothing prevents a future change from silently breaking a validator or a test; every gate to date has depended on a human/AI remembering to run it manually.
5. **Zero privacy/consent architecture**, despite mature safeguarding *content* existing unused — the moment any video, account, or child-adjacent data flow is added, this becomes an urgent legal exposure, not just a UX gap.
6. **"Architecture readiness" claims for Accounts/Commercial/Academy are actually zero-code claims** — the existing ledger's `READY_WITH_MINOR_EXTENSION` framing risks understating how much real work remains, because it was assessed by absence-of-blockers rather than presence-of-implementation.
7. **The canonical "Planificat: 60/36/50/15" line is a plan, not a progress measurement** — anyone reading `validate_project.py`'s output casually could mistake registry-internal-consistency for actual content completion.
8. **`visual_assets` fields on all 5 exercises are stale**, self-declaring "PENDING" for assets that actually exist and are live — a latent data-integrity trap for any future automated tooling that trusts this field.
9. **Knowledge Graph is explicitly not a real graph** (self-declared in its own spec) — anyone assuming "Knowledge Graph = DONE" from the feature ledger's `DONE` status (justified by "no parallel graph, transitively surfaces links") could overestimate the system's actual relationship-discovery capability.
10. **Zero analytics/observability** — the team has no way to know which of the 5 exercises or 2 sessions coaches actually use, whether Field Mode is used on real pitches, or whether errors are occurring in production, at any point since launch.

---

## FORGOTTEN / DEFERRED FEATURES REGISTER

| Feature | When/where defined | Current status | Why it disappeared | Should it return now? |
|---|---|---|---|---|
| "Three engines" (Decision/Learning/Field) architecture framing | DEC-0054, premium audit | Superseded piecemeal (Decision Engine and Field Mode both built under different names) but the unifying "three engines" framing itself never formally re-adopted or rejected | Individual waves (27-33) picked off pieces without revisiting the framing explicitly | NOT_NEEDED — the pieces exist under clearer names; reviving the framing would add naming complexity without new capability |
| "Bibliotecă" (Library) navigation label | DEC-0057 | Never adopted | Deliberately withheld until a unified inventory/search/filter capability existed | RECONSIDER once Search (P1) covers competencies and media — the precondition may now be closer to met |
| Block pressing with fixed roles/triggers ("5-second rule") | DEC-0033 | Explicitly `PRACTICE_ONLY`, deferred for lack of evidence at U11 | No research ever found supporting it at any age | REMAIN_DEFERRED — correctly rejected, not forgotten |
| Coach reflection/self-evaluation/professional development research | DEC-0069 ("the biggest real gap") | Researched (PHASE-30 Wave-2) but never built as a system | Research-first discipline meant the finding (reflection alone doesn't improve practice) came before any implementation decision | SHOULD_RETURN — this is exactly the Coach Development gap (§20), now the #6 ranked gap above |
| Season/medium-term planning content (`season-plans`) | Schema exists since early phases; DEC-0077 reconfirms "fără conținut" | Schema-only, zero content | Deprioritized relative to single-session Gold Standard work | DEFER further until exercise/session breadth (#1/#2 gaps) is addressed — building season plans around a 2-session library is premature |
| An uncommitted visual redesign (new AppHeader/AppFooter/homepage) | DEC-0048, referenced `plans/MANUALFC-visual-identity-v1.md` | Sits in git HEAD, deliberately never committed, status never decided in any later DEC | Design-freeze discipline during content-integrity waves | NEEDS AN EXPLICIT DECISION — this has been silently unresolved for many phases; either commit it, formally shelve it, or discard it |
| Certification/CPD for coaches | Only in the final ledger (`RESEARCH_REQUIRED`) | Never mentioned in any DECISIONS.md entry as an implementation candidate | Appears to have been named once during premium-audit brainstorming and never revisited | REMAIN_DEFERRED — reasonable long-term idea, no urgency |
| Coach/parent scenario content | Mentioned in vision docs | Zero schema, zero data, zero code | Absorbed into the broader "case studies" placeholder without ever being separately scoped | CLARIFY — decide if this is the same thing as case studies (D4) or a distinct category before scoping further work |

---

## PRESERVE / DO NOT REBUILD

Based on direct evidence of maturity (not architecture-document promises):

- **Research/evidence architecture** (`research/sources.json`/`claims.json`/`citations.json` + dossiers) — mature, cross-referenced, self-correcting.
- **Pedagogul content** (`content/volume-01/*.mdx`) — mature, accepted, independently audited.
- **Antrenorul content** (`content/volume-03/04/*.mdx`) — mature, accepted, independently audited (including a full forensic remediation cycle that succeeded).
- **Educational Page System components** (`ChapterOrganizer`, `ExplanationToggle`, etc.) — mature, well-designed; the gap is retrofit coverage (19/31 chapters), not the components themselves.
- **Decision Engine** (`rezolva-pe-teren/`) — mature, honest, working.
- **Gold Standard V2 schema + validator** (`schemas/exercise.schema.json`, `session.schema.json`, `validate_gold_standard_v2.py`) — mature, additive, well-tested mechanism; extend, don't replace.
- **Field Mode** (`gold-standard/sedinte/[id]/mod-teren.astro`) — mature, disciplined, V2-aware.
- **Group Configurator + Surface Maps** — mature, deterministic, honest when infeasible.
- **Local-first Workspace/CoachState** (`coach-state.ts`) — mature, coherent; extend with cloud sync via the existing port abstraction rather than rewriting.
- **Offline/PWA foundations** (`sw.js`, `offline-pack.ts`) — mature, real, correctly and honestly scoped.

---

## LAUNCH GATES

| Gate | Condition |
|---|---|
| CONTROLLED_PILOT_READY | Exercise/session breadth reaches at least the intermediate milestone below (§46), the field-pilot templates are actually filled by 2-3 real coaches, and human-learning validation protocol is executed at small scale. **Not yet met** — currently only preparation artifacts exist. |
| PRIVATE_BETA_READY | Controlled pilot complete with documented findings + at least 15-20 exercises + 8-12 sessions + basic error monitoring in place. **Not yet met.** |
| PAID_COACH_BETA_READY | Private beta complete + real accounts/cloud persistence + a minimal privacy/consent page + at least one real coach-education video (Wave M3/M4 below) + basic entitlement gating (even if generous). **Not yet met — largest remaining distance.** |
| PUBLIC_PAID_LAUNCH_READY | Paid coach beta validated (retention/WTP data collected) + billing integration + CI/CD + full exercise/session library at or near target (60/36) + real field footage for at least the flagship problems. **Far from met.** |
| ACADEMY_PILOT_READY | Public paid launch stable + organization/roles data model + shared curriculum + club-level analytics. **Far from met.** |

---

## NEXT ROADMAP (5 waves, impact/dependency-derived, not mechanical phase-numbering)

**WAVE_1 — Field & Human Validation Pilot.** GOAL: run the first real controlled pilot (SES-0001, EX-0001-0003, Field Mode, Reflection) with 2-3 real coaches, and execute the existing human-learning-validation protocol at small scale. WHY_NOW: every other roadmap wave depends on knowing whether the current mechanism actually works for a real coach. DEPENDENCIES: none — the templates and protocol already exist. UNLOCKS: confidence to scale content and multimedia investment. DONE_CRITERIA: at least one filled `PHASE23_FIELD_RETURN_TEMPLATE_R1.md`-equivalent per coach, and human-learning-validation results recorded (even if the results are mixed or negative).

**WAVE_2 — Content Scale to Intermediate Milestone.** GOAL: grow to ~15-20 exercises and ~8-12 sessions (not the full 60/36 immediately), reusing the now-proven Gold Standard V2 pattern from day one of authoring (not retrofitted later). WHY_NOW: 5/2 is too thin for a controlled pilot to feel like a real product; jumping straight to 60/36 without Wave 1 feedback risks scaling the wrong thing. DEPENDENCIES: Wave 1 findings should inform which new exercises/sessions are prioritized. UNLOCKS: a private beta with enough content to retain a real user. DONE_CRITERIA: exercise/session counts hit the intermediate targets, each passing the same V2 validator gate EX-0001 did.

**WAVE_3 — Multimedia M1-M3 (synthetic, not real-footage yet).** GOAL: extend static diagrams + tactical loops + full-cycle animations to cover the Wave-2 exercise set; build the coach-education demonstration layer as *simulated* (not real) coaching-moment walkthroughs. WHY_NOW: this is buildable entirely with existing synthetic techniques (proven safe and honest by the current 5-exercise implementation) without needing consent/filming infrastructure yet. DEPENDENCIES: Wave 2's new exercises need diagrams/loops as they're authored. UNLOCKS: a materially more convincing product demo for beta recruitment. DONE_CRITERIA: every new exercise has at minimum a static diagram; problems with real transfer relevance get a loop.

**WAVE_4 — Coach Development Loop (minimum viable).** GOAL: build baseline + reflection-to-next-goal as the first real 2-link addition to the existing 3-link Coach Development chain (§20) — explicitly not a Coach Score, not full longitudinal history yet. WHY_NOW: this was named "the biggest real gap" as far back as DEC-0069 and remains entirely unbuilt; a minimal version is achievable without cloud infrastructure (can live in `CoachState` locally first). DEPENDENCIES: Reflection V2 should be wired into the personal reflection tool first (currently only display-only on session pages). UNLOCKS: a genuine product differentiator ready before any commercial push. DONE_CRITERIA: a coach can see "you focused on COACH-C01 last time; here's a suggested next focus," entirely from local data.

**WAVE_5 — Accounts/Cloud + Privacy Foundation.** GOAL: real (not just "ready") authentication and cloud persistence via the existing `CoachStatePort` abstraction, plus a real privacy/consent page wiring in the already-mature safeguarding data. WHY_NOW: this is the actual gate for both cross-device continuity (a top user-visible gap) and any future video-consent flow (a precondition for Wave M4/M5 real footage) or commercial launch. DEPENDENCIES: should follow Wave 1-4 so there's a validated, retained product worth persisting in the cloud. UNLOCKS: private beta → paid beta transition, real footage collection with proper consent. DONE_CRITERIA: a coach can log in on a second device and see the same saved sessions/reflections; a real privacy policy page exists and is linked from the footer.

---

## PARALLEL LANES

- **LANE A — Field/Human Validation**: Wave 1 → ongoing pilots feeding Wave 2/3/4 priorities.
- **LANE B — Multimedia/Demonstration**: Wave 3 (synthetic) → depends on Lane A findings for which exercises matter most → real footage only after Wave 5's consent infrastructure exists.
- **LANE C — Content Scale**: Wave 2 → continues in parallel with Lane B, feeding it new exercises to illustrate.
- **LANE D — Product/Cloud/Coach Development**: Wave 4 (local-first) can start immediately and in parallel with Lanes A-C; Wave 5 (cloud) should wait until Lane A validates the product is worth persisting.
- **LANE E — Commercial/Academy/Scale**: explicitly held until Lanes A-D produce a validated, retained product — starting Lane E earlier would mean selling something unvalidated, contradicting the product's own `COMMERCIALIZATION_ROADMAP.md`.

Dependency summary: **A blocks nothing but informs everything; C and D can run in parallel with each other and with the tail of A; B depends partly on C (new content to illustrate) and fully on E's eventual consent work for its real-footage half; E is deliberately last.**

---

## MULTIMEDIA ROADMAP (derived, not accepted blindly from the suggested §45 order)

The suggested order in the master prompt (M1 tactical/exercise animations → M2 Pedagogul/Antrenorul explainers → M3 simulated coaching-moment demos → M4 real field recording → M5 match-transfer library) is **broadly confirmed as correct** by this audit's evidence, with one adjustment: M1 (tactical/exercise animations) is already ~50-75% complete for the existing 5-exercise corpus and should be treated as "extend to new content as it's authored" (folded into Content Wave 2) rather than a standalone wave. The real sequencing gap is between M3 (simulated, buildable now) and M4 (real, requires consent infrastructure that doesn't exist) — this is exactly why Wave 5 (Accounts/Cloud + Privacy) is sequenced before any real-footage wave in the roadmap above, even though the master prompt's suggested order doesn't explicitly call this out.

---

## CONTENT SCALE ROADMAP

**Recommendation: do NOT jump immediately to 60 exercises / 36 sessions.** Evidence for this: (1) the field pilot (Wave 1) has never run even once, so there is no validated signal about which exercise types actually work with real children; scaling content 12x before that signal exists risks producing 55 more exercises with the same unvalidated assumptions as the first 5. (2) The task-batch system already has 15 exercise batches and 18 session batches fully planned and ready to execute — the risk is not planning, it's sequencing. **Recommended intermediate milestone: 15-20 exercises, 8-12 sessions** (roughly one batch wave of exercises, half the planned session batches), timed to follow Wave 1's field pilot so early lessons can shape which of the remaining planned batches are prioritized or revised before full-scale authoring.

---

## PILOT ROADMAP (plan only — not executed by this audit)

Minimum controlled pilot package, derived from what already exists and is ready:
- **Content**: SES-0001 (already built, V2-complete) + EX-0001, EX-0002, EX-0003 (all V2-complete, in-scope of SES-0001).
- **Prerequisites**: one Pedagogul chapter most relevant to the session's core skill (e.g. CH-0101, already mature) + the corresponding Antrenorul chapter(s) (CH-0407/0408, already mature and cross-linked).
- **Tools**: Field Mode (already built, V2-aware) + Reflection V2 (data model exists; recommend wiring it into the reflection form — Wave 4 — before the pilot, or accept V1-only reflection for this first pilot).
- **Protocol**: a pre-session coach scenario (what does the coach expect to see), the session itself, immediate post-session reflection, and a **delayed recall check** (e.g. one week later, ask the coach what they remember and whether they used it again) — this delayed-recall step does not currently exist anywhere in the product and should be added as a lightweight follow-up form, not fabricated as already present.
- **Field observation**: use the existing (currently blank) `docs/field-pilot/PHASE23_FIELD_RETURN_TEMPLATE_R1.md` as the actual data-collection instrument — it was built for exactly this purpose and has never been used.

This plan is offered for future authorization; **no pilot was run by this audit**, consistent with its read-only mandate.

---

## COMMERCIAL LAUNCH GATE DEFINITIONS

See the LAUNCH GATES table above for the five-gate definition (Controlled Pilot / Private Beta / Paid Coach Beta / Public Paid Launch / Academy Pilot), each with explicit, checkable conditions rather than vague readiness language.

---

## PREMIUM V1 DEFINITION

The minimum coherent product that genuinely deserves payment, distinct from the full multi-year vision:

**User-visible requirements**: 15-20 well-demonstrated exercises and 8-12 sessions (not 60/36 — see Content Scale Roadmap), at least static+loop multimedia for all of them, a working Coach Development minimum-viable loop (Wave 4), cross-device account/cloud persistence (Wave 5), and evidence from at least one real controlled pilot that the product changes what a coach actually does on the pitch (Wave 1).

**Invisible requirements**: a real privacy/consent page, basic error monitoring, a CI/CD gate on the existing validators, and an honest public statement of what remains field-unvalidated (continuing the project's own strong tradition of not overclaiming).

**Explicitly NOT required for Premium V1**: multi-age content, multilingual support, Academy/Club features, real match-transfer video, or a full 60/36 content library — all of these are legitimately Full Vision items, not Premium V1 blockers.

---

## FULL VISION DEFINITION

The final multi-year destination described across `PRODUCT_VISION.md`, `MULTI_AGE_EXPANSION_ARCHITECTURE.md`, and `COMMERCIALIZATION_ROADMAP.md`: a complete U4-U18 coach-education platform with 60+ exercises and 36+ sessions per age band, real consented field/match footage demonstrating every major competency, a full Coach Development longitudinal system with mentor feedback, Academy/Club organizational features for federated coaching bodies, multilingual delivery, and a validated commercial model (subscription and/or club licensing) — reached only after each of the Premium V1 gates above has been validated with real users and real revenue signal, not designed speculatively in advance of that evidence.

---

## NEW_OPTIONAL_IDEAS (do not affect any completion percentage above)

- A lightweight "delayed recall" follow-up form (1 week post-pilot) — needed for the Pilot Roadmap above but does not exist yet; flagged as a small, well-scoped addition, not a scope expansion.
- A public "what we haven't validated yet" page, turning the project's existing internal honesty (DEC entries, `NOT_YET_RUN` markers) into a user-facing trust signal — differentiator, not a requirement.
- A minimal competency glossary/tooltip so raw `COACH-C01`-style IDs shown on exercise pages are not opaque to a first-time visitor.

---

## GOVERNANCE / VALIDATION RUN FOR THIS AUDIT

```
python scripts/validate_project.py         → 0 erori, 0 avertismente (300 taskuri; 158 DONE / 142 PENDING)
python scripts/generate_task_registry.py --check → reproductibil (300 taskuri)
git diff --check                            → clean
```

No runtime code, schema, content, or data file was modified in the production of this audit. Only two new documentation files were created: this report and `docs/product/MANUALFC_FINAL_PRODUCT_FEATURE_LEDGER_V2.md`.
