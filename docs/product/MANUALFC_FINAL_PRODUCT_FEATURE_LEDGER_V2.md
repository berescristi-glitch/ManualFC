# ManualFC — Final Product Feature Ledger V2

**Task de referință:** control-plane audit (a se vedea `reports/audits/MANUALFC_MASTER_FINAL_PRODUCT_GAP_AUDIT_V2.md` pentru metodologie completă) · **Statut document:** as-built, evidence-based, read-only · **Data:** 2026-08-31

Acest document NU înlocuiește `docs/product/FINAL_PRODUCT_FEATURE_LEDGER.md` (păstrat neschimbat ca jurnal istoric per-fază). Este o **re-evaluare independentă**, măsurată explicit față de viziunea finală a produsului (nu față de task-uri DONE), cu procent de completare și dovadă de repository pentru fiecare capacitate.

Coloane: ID | Feature | Category | Final Target | Current Implementation | Status | Completion % | Evidence | User-visible? | Field validation required? | Human validation required? | Dependencies | Launch priority.

Vocabular de status: `BUILT` · `MATURE` · `FUNCTIONAL_BUT_PARTIAL` · `FOUNDATION_ONLY` · `NOT_STARTED` · `FIELD_VALIDATION_REQUIRED` · `HUMAN_VALIDATION_REQUIRED` · `REQUIRES_REFACTOR` · `BLOCKED`.

---

## A. Knowledge / Methodology

| ID | Feature | Final Target | Current | Status | % | Evidence | User-visible | Field val. | Human val. | Priority |
|---|---|---|---|---|---:|---|---|---|---|---|
| A1 | Evidence architecture (sources/claims/citations) | Cross-referenced, verified, self-correcting registry covering all content | 361 sources, 380 claims, 408 citations, fully cross-ID'd; one real fabrication caught and fully remediated (DEC-0040) | MATURE | 90% | `research/sources.json` (20,919 lines), `claims.json` (12,803), `citations.json` (7,758); DECISIONS.md DEC-0040/0041/0042 | NO | NO | NO | POST_LAUNCH_OK |
| A2 | Research dossiers | Full topical coverage for all pedagogical/coaching domains | 67 dossier files across child development, safeguarding, per-chapter, and 24 topic-level "R1" dossiers | MATURE | 85% | `research/dossiers/*.md` (67 files) | NO | NO | NO | POST_LAUNCH_OK |
| A3 | Pedagogul content (Volume 01) | Complete lesson set for the pedagogue pillar | 10/10 chapter-*.mdx, substantive (76–130 lines), all real prose | BUILT | 88% | `content/volume-01/chapter-01..10.mdx`; DEC-0071 acceptance | YES | NO | YES (unmeasured) | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH |
| A4 | Antrenorul content (Volumes 03/04) | Complete lesson set for the coach pillar | 21 chapters (10+11), substantive (85–205 lines) | BUILT | 85% | `content/volume-03/chapter-01..10.mdx`, `volume-04/chapter-01..11.mdx`; DEC-0077 | YES | NO | YES (unmeasured) | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH |
| A5 | Pedagog competency framework (PED-C01–13) | 13 competencies, each linked to real product behavior | 13 defined; framework's own coverage matrix: 3 fully linked (DA), 2 partial, 8 unlinked ("conceptual only") | FUNCTIONAL_BUT_PARTIAL | 31% | `docs/knowledge/PEDAGOG_COMPETENCY_FRAMEWORK.md` line 215 self-audit table | NO (IDs shown raw, unlabeled, to coaches on exercise/session pages) | NO | NO | SHOULD_HAVE_FOR_PREMIUM_V1 |
| A6 | Coach competency framework (COACH-C01–18) | 18 competencies, each linked to a lesson + real product data | 18 defined; ~11/18 appear in real exercise/session `coach_competency_ids` data (PHASE-33); COACH-C06 explicitly has no dedicated chapter (declared gap, not hidden) | FUNCTIONAL_BUT_PARTIAL | 45% | `docs/knowledge/COACH_COMPETENCY_FRAMEWORK.md`; `data/exercises/*.json`; DEC-0077/0078 | Partially (raw IDs on pages) | NO | NO | SHOULD_HAVE_FOR_PREMIUM_V1 |
| A7 | Theory → Practice Contract | Applied to the full practice library | 18-question lesson contract + 11-step chain defined; **fully implemented on 100% of the existing 5 exercises + 2 sessions**, 0% of the other 55 exercises/34 sessions that don't yet exist | FUNCTIONAL_BUT_PARTIAL | 40% (contract quality high; breadth of application is the limiter) | `docs/knowledge/THEORY_TO_PRACTICE_CONTRACT.md`; PHASE-33 acceptance report | Partially (visible on the 5 exercise pages) | NO | NO | SHOULD_HAVE_FOR_PREMIUM_V1 |
| A8 | Knowledge Graph | Real relational structure connecting problem↔concept↔competency↔exercise↔session↔assessment↔reflection | Its own spec explicitly states: *"Fără implementare de motor de graf... Fără UI nou de explorare a grafului."* Implemented as ID-array cross-references resolved at build time in `content-bridge.ts`, not a graph engine or explorable structure | FOUNDATION_ONLY | 35% | `docs/knowledge/KNOWLEDGE_GRAPH_SPECIFICATION.md` §7 (self-declared non-scope); `app/src/lib/content-bridge.ts` | NO | NO | NO | CAN_FOLLOW_AFTER_LAUNCH |
| A9 | Evidence boundaries (`evidence_boundary`/`PRACTICE_HEURISTIC`/`FIELD_INPUT_REQUIRED`) | Applied consistently across all content | 20 `evidence_boundary`, 15 `PRACTICE_HEURISTIC`, 2 `FIELD_INPUT_REQUIRED` occurrences — concentrated entirely in the 5-exercise/2-session Gold Standard corpus, not the wider 31-chapter narrative content (which uses its own "Ce nu putem concluziona" pattern instead, present in 30/31 chapters) | MATURE (for its scope) | 75% | grep counts across `data/` + `content/` | Partially | NO | NO | POST_LAUNCH_OK |
| A10 | Age/developmental architecture | Flexible age-band data model supporting U4–U18 | `age_category` is a hardcoded JSON Schema `const` in every schema; a `future_age_architecture` field exists with a provisional (explicitly changeable) rollout order, but zero flexible implementation | FOUNDATION_ONLY | 12% | `schemas/exercise.schema.json` lines 56-58; `schemas/project.schema.json` `future_age_architecture`; `MULTI_AGE_EXPANSION_ARCHITECTURE.md` | NO | NO | NO | CAN_FOLLOW_AFTER_LAUNCH |

## B. Decision Support

| ID | Feature | Final Target | Current | Status | % | Evidence | User-visible | Field val. | Human val. | Priority |
|---|---|---|---|---|---:|---|---|---|---|---|
| B1 | Problem Library | Comprehensive observable-problem coverage | 8 problems (3 flagship), meets the schema's own stated minimum (8) exactly; schema allows up to 12 | BUILT (at stated floor) | 100% of stated minimum / thin in absolute terms | `data/problems/problem-library.json`; `schemas/problem.schema.json` (`minItems:8`) | YES | Partial (`transfer_checks` all `NEEDS_FIELD_VALIDATION`) | NO | SHOULD_HAVE_FOR_PREMIUM_V1 (grow beyond floor) |
| B2 | Decision Engine UI (quick test → possible explanations → intervention → transfer) | Full observation-first workflow for every problem | Real, working, honestly-degrading UI (`rezolva-pe-teren/[slug].astro`); when `related_exercises` is empty (2/8 problems), shows an honest "no exercise yet" message instead of fabricating one | MATURE | 85% | `app/src/pages/rezolva-pe-teren/[slug].astro` (41 lines); `index.astro` | YES | NO | NO | POST_LAUNCH_OK |
| B3 | Pedagogul/Antrenorul/practice links from Problems | Every problem links to real lessons + exercises + sessions + assessment | `related_principles` never empty (8/8); `related_exercises`/`related_sessions` empty in 2/8; `assessment_links` empty in 4/8 (only 1 assessment exists) | FUNCTIONAL_BUT_PARTIAL | 60% | `data/problems/problem-library.json` field-by-field audit | YES | NO | NO | SHOULD_HAVE_FOR_PREMIUM_V1 |

## C. Practice System (Gold Standard V2)

| ID | Feature | Final Target | Current | Status | % | Evidence | User-visible | Field val. | Human val. | Priority |
|---|---|---|---|---|---:|---|---|---|---|---|
| C1 | Exercise data model V2 | Applied to 60 exercises | Schema built additively (16 optional fields), applied to 5/5 existing exercises (100% of what exists) | MATURE (mechanism) / early (breadth) | 85% mechanism, 8.3% breadth | `schemas/exercise.schema.json`; `data/exercises/*.json` | YES | NO | NO | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH (breadth) |
| C2 | Session data model V2 (dual objectives, Reflection V2) | Applied to 36 sessions | Schema built additively, applied to 2/2 existing sessions | MATURE (mechanism) / early (breadth) | 85% mechanism, 5.6% breadth | `schemas/session.schema.json`; `data/sessions/*.json` | YES | NO | NO | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH (breadth) |
| C3 | Group Configurator | Handle any realistic squad size/coach count | 6 player counts (8–18), 1-2 coaches, fails closed with an honest note rather than fabricating an infeasible config | MATURE | 85% | `app/src/lib/group-configurator.ts` (130 lines) | YES | Partial (positioning heuristics unvalidated) | NO | POST_LAUNCH_OK |
| C4 | Surface Maps | Visual field layout for any configuration | Real inline SVG, deterministically generated (not ~60 hand-drawn variants), with accessibility title/desc | MATURE | 85% | `app/src/lib/surface-map.ts`; `app/src/components/SurfaceMap.astro` | YES | NO | NO | POST_LAUNCH_OK |
| C5 | Field Cards | Printable one-page reference per exercise | Built for all 5 existing exercises; no V2 fields shown (by design — kept minimal for pitch-side use) | MATURE (for existing exercises) | 80% | `app/src/components/FieldCard.astro`; `fise-de-teren.astro` | YES | NO | NO | POST_LAUNCH_OK |
| C6 | Field Mode | Segment-by-segment live coaching UI with coach focus/intervention guidance | Fully built, renders `coach_focus`/`non_intervention_criteria`/`verification_method` per segment; one-segment-one-screen preserved | MATURE | 85% | `app/src/pages/gold-standard/sedinte/[id]/mod-teren.astro` (220 lines) | YES | YES (usability in real training unverified) | NO | POST_LAUNCH_OK |
| C7 | Assessment | Criteria-based, non-numeric evaluation | 1 assessment (ASM-0001), 5 criteria, each with 3 observable levels, tied to specific exercises | BUILT (for its scope) | 70% (only 1 assessment exists) | `data/assessments/assessment-sprijin-si-unghi-de-pasa.json` | YES | Partial | NO | SHOULD_HAVE_FOR_PREMIUM_V1 |
| C8 | Reflection V2 (dual-dimension) | Full child/game + coach dimension reflection, wired into the personal reflection tool | Data model complete on both sessions; **displayed read-only on the session page**, but the actual personal reflection FORM (`spatiul-meu/reflectie.astro`) still only captures V1 fields (`observedState`/`transferState`/free text) — the two dimensions are not yet a guided input flow | FUNCTIONAL_BUT_PARTIAL | 45% | `data/sessions/*.json` `reflection_v2`; `app/src/pages/spatiul-meu/reflectie.astro` (191 lines, unchanged fields) | YES | NO | YES | SHOULD_HAVE_FOR_PREMIUM_V1 |

## D. Content Breadth

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| D1 | Exercises | 60 (project.schema.json `minimum_deliverables`) | 5 | FOUNDATION_ONLY (breadth) | **8.3%** | `data/exercises/*.json` (5 files); 15 planned batch tasks, all `PENDING` | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH |
| D2 | Sessions | 36 | 2 | FOUNDATION_ONLY (breadth) | **5.6%** | `data/sessions/*.json` (2 files); 18 planned batch tasks, all `PENDING` | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH |
| D3 | Communication scripts | 50 | 0 | NOT_STARTED | **0%** | `data/communication-scripts/` = README only; 10 planned batches, all `PENDING` | SHOULD_HAVE_FOR_PREMIUM_V1 |
| D4 | Case studies | 15 | 0 | NOT_STARTED | **0%** | `data/case-studies/` = README only; 5 planned batches, all `PENDING` | SHOULD_HAVE_FOR_PREMIUM_V1 |
| D5 | Problems | ≥8 (schema floor) | 8 | BUILT (at floor) | 100% of stated minimum | `data/problems/problem-library.json` | CAN_FOLLOW_AFTER_LAUNCH (grow beyond floor) |
| D6 | Principles | no canonical numeric target found | 25 | BUILT (for its own scope) | n/a (treated as complete) | `data/principles/*.json` | POST_LAUNCH_OK |
| D7 | Season plans | referenced by schema, no populated target stated | 0 | NOT_STARTED | 0% | `data/season-plans/` = README only | CAN_FOLLOW_AFTER_LAUNCH |
| D8 | Coach/parent scenarios | mentioned in vision docs, no schema/data exists | 0 | NOT_STARTED | 0% | zero repo-wide matches | LONG_TERM |

## E. Multimedia (see dedicated deep-dive in the Gap Audit report §14-15)

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| E1 | Static tactical diagrams | Cover full exercise library | 5/5 existing exercises (hand-authored SVG); 3/8 problems (before/after) | BUILT (for existing scope) | 75% of current corpus | `TacticalDiagram.astro`, `ProblemVisual.astro` | POST_LAUNCH_OK |
| E2 | Tactical loop animations | Cover exercises where useful | 4 loops (EX-0001/0002/0003, PRB-0003); EX-0004/0005 deliberately excluded (would imply false fixed choreography) | FUNCTIONAL_BUT_PARTIAL | 50% of current corpus | `TacticalLoop.astro`, `ConceptLoop.astro` | POST_LAUNCH_OK |
| E3 | Exercise full-cycle animation | One per exercise where useful | 1/5 (EX-0001 only) | FOUNDATION_ONLY | 20% of current corpus | `ExerciseSequenceAnimation.astro` | CAN_FOLLOW_AFTER_LAUNCH |
| E4 | Coach explainer scripts | Text ready for future recording, 3 flagship problems | 3/3 flagship problems, explicitly labeled "not a real recording" | BUILT (as scripts) | 100% of its own narrow scope | `data/media/media-registry.json`; `CoachExplainerScript.astro` | N/A (not a video) |
| E5 | Coach explainer videos | Recorded video matching the 3 scripts | 0 | NOT_STARTED | **0%** | Exhaustive repo-wide video-file search: zero results | SHOULD_HAVE_FOR_PREMIUM_V1 |
| E6 | Real field training footage | Consented real footage of real training | 0; 9-stage pipeline documented, zero stages executed | NOT_STARTED | **0%** | `docs/architecture/MULTIMEDIA_PRODUCTION_PIPELINE.md` | FIELD_VALIDATION_REQUIRED first |
| E7 | Real intervention / child response footage | Real footage of coach interventions and child responses | 0; not even a distinct registry type populated | NOT_STARTED | **0%** | repo-wide search, zero hits | FIELD_VALIDATION_REQUIRED first |
| E8 | Match transfer footage / annotated clips | Real match footage showing transfer | 0 | NOT_STARTED | **0%** | `FINAL_PRODUCT_FEATURE_LEDGER.md` rows explicitly `FIELD_INPUT_REQUIRED` | FIELD_VALIDATION_REQUIRED first |
| E9 | Reduced-motion support | Every animated asset has a static fallback | Genuinely implemented per-component, fail-closed validated | MATURE | 90% | 6 files with `prefers-reduced-motion`; registry validator enforces `reduced_motion_fallback` | POST_LAUNCH_OK |
| E10 | Media offline support | Media bytes cached for offline use | Only route-level caching; media tracked as metadata but not independently cached (works today only because media is inline SVG/CSS, not separate files) | FOUNDATION_ONLY | 40% | `app/src/lib/offline-pack.ts` | CAN_FOLLOW_AFTER_LAUNCH |

## F. Educational Experience

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| F1 | Educational Page System (Learn/Recall/Apply components) | Applied to all lesson content | 6 components built and mature; applied to 19/31 chapters (all of volume-01, only the newest 9 of 21 in volumes 03/04) | FUNCTIONAL_BUT_PARTIAL | 61% (19/31 chapters) | `app/src/components/{ChapterOrganizer,ExplanationToggle,...}.astro`; grep across `content/` | SHOULD_HAVE_FOR_PREMIUM_V1 |
| F2 | "Ce nu putem concluziona" evidence-boundary pattern | Universal across all lessons | 30/31 chapters (97%) | MATURE | 97% | grep count | POST_LAUNCH_OK |
| F3 | Deep linking / section navigation | Real anchor-based navigation | Implemented via a custom `<section-navigator>` Web Component with `IntersectionObserver` scroll-spy, not literal markdown anchors — works only where the component is used (19/31 chapters) | FUNCTIONAL_BUT_PARTIAL | 55% | `app/src/lib/educational-page.ts` | POST_LAUNCH_OK |
| F4 | Human learning validation | Real coaches tested for comprehension/retention/application | Explicit protocol exists (`docs/ux/MANUALFC_EDUCATIONAL_PAGE_USER_TEST_PROTOCOL.md`) but **never executed** — no results file exists anywhere | HUMAN_VALIDATION_REQUIRED | 0% | Every PHASE-27→33 acceptance report states `HUMAN_LEARNING_VALIDATION: NOT_YET_RUN` verbatim | MUST_HAVE_BEFORE_PAID_PUBLIC_LAUNCH |

## G. Personal Workspace

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| G1 | Session builder | Build custom sessions from any content | Fully built (`spatiul-meu/sedinta.astro` + `coach-state.ts`) | MATURE | 85% | `app/src/lib/coach-state.ts` (305 lines) | POST_LAUNCH_OK |
| G2 | Saved / Favorites / Recents | Persistent personal library | All three implemented, `recents` capped at 12 | MATURE | 85% | same file | POST_LAUNCH_OK |
| G3 | Continue-where-you-left-off | Smart resumption across sessions/reflections/reading | Real 4-tier priority chain (active session → unreflected session → last reflection's next-action → last visited page) | MATURE | 80% | `app/src/pages/spatiul-meu/index.astro` lines 30, 57-66 | POST_LAUNCH_OK |
| G4 | Persistent reflections | Structured post-session reflection, saved locally | Built (V1 fields only — see C8 for the V2 gap) | FUNCTIONAL_BUT_PARTIAL | 60% | `SessionReflection` interface | SHOULD_HAVE_FOR_PREMIUM_V1 |
| G5 | Offline-prepared sessions | Explicit "take this session offline" flow | Built, fail-closed, verified | MATURE | 80% | `offline-pack.ts` | POST_LAUNCH_OK |

## H. Coach Development

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| H1 | Competency model | 18 coach competencies usable as a development framework | Defined, referenced as static labels in session/exercise data; **never aggregated, tracked, or read back into any coach-facing progress view** | FOUNDATION_ONLY | 25% | `coach-state.ts` full read: zero fields store competency progress | SHOULD_HAVE_FOR_PREMIUM_V1 |
| H2 | Coach objectives per session | Objectives explicitly tied to competencies | Built (`coach_objectives` on both sessions) | BUILT (for 2 sessions) | 70% mechanism / 5.6% breadth | `data/sessions/*.json` | SHOULD_HAVE_FOR_PREMIUM_V1 |
| H3 | Coach focus per exercise/segment | Present everywhere relevant | Built on all 5 exercises + all session segments | MATURE (for existing corpus) | 80% | verified field-by-field | POST_LAUNCH_OK |
| H4 | Coach reflection | Structured self-reflection prompts | Built (`coach_reflection` on exercises, `reflection_v2.coach_dimension` on sessions) — see gap in G4/C8 about the personal tool not yet using it | FUNCTIONAL_BUT_PARTIAL | 50% | same | SHOULD_HAVE_FOR_PREMIUM_V1 |
| H5 | Competency baseline | Starting point measurement for a coach | Does not exist | NOT_STARTED | **0%** | zero code/data found anywhere | LONG_TERM |
| H6 | Next recommended development goal | System-suggested focus for next session | Does not exist | NOT_STARTED | **0%** | zero code found (`grep "development goal"` etc. = 0 hits) | LONG_TERM |
| H7 | Longitudinal development history | Track a coach's competency over months/seasons | Does not exist | NOT_STARTED | **0%** | zero "longitudinal"/"mentor" hits anywhere in repo | LONG_TERM |
| H8 | External/mentor feedback | Capture feedback from a mentor or colleague | Does not exist | NOT_STARTED | **0%** | zero hits | LONG_TERM |
| H9 | No fake Coach Score | Never introduce a numeric ranking | Explicitly and repeatedly rejected by design (CH-0308/0310/0311; DEC-0077/0078) | BUILT (as a negative constraint, correctly upheld) | 100% (compliance) | zero "score" hits near "coach" anywhere in code | N/A |

**Coach Development overall**: `NOT_STARTED` as an end-to-end loop (§20's 9-link chain: only 3 of 9 links — coach objectives, coach focus, coach reflection — have any real data; baseline, next-goal, longitudinal, external feedback are all absent). **Reflection alone ≠ Coach Development**, per the master prompt's own explicit warning — this ledger does not conflate them.

## I. Field / Human Validation

| ID | Feature | Status | % | Evidence |
|---|---|---|---:|---|
| I1 | Real coach pilot with real children | NOT_STARTED — only preparation templates exist, both blank | 0% | `docs/field-pilot/PHASE23_FIELD_RETURN_TEMPLATE_R1.md` confirmed blank; DEC-0047 `FIELD_INPUT_REQUIRED = YES`, never closed through DEC-0078 |
| I2 | Group Configurator / positioning heuristic validation | FIELD_VALIDATION_REQUIRED | n/a | `PRACTICE_HEURISTIC` label on coach-positioning logic |
| I3 | Field Mode usability validation | FIELD_VALIDATION_REQUIRED | n/a | Browser-tested only, never used on an actual pitch by a real coach |
| I4 | Cue effectiveness validation | FIELD_VALIDATION_REQUIRED | n/a | Cues are research-informed, not field-tested |
| I5 | Transfer observation | FIELD_VALIDATION_REQUIRED | n/a | All `transfer_checks` marked `NEEDS_FIELD_VALIDATION` |
| I6 | Romanian-context / community-coach validation | FIELD_VALIDATION_REQUIRED | n/a | Research base is largely international/academy-level, honestly flagged in PHASE-30/32 |

## J. Offline / PWA

| ID | Feature | Final Target | Current | Status | % | Evidence | Priority |
|---|---|---|---|---|---:|---|---|
| J1 | Installable PWA | Manifest + icons + service worker | All present and real | BUILT | 85% | `public/manifest.webmanifest`, `public/sw.js` (172 lines) | POST_LAUNCH_OK |
| J2 | Prepared-session offline | Explicit offline mode for a chosen session | Built, fail-closed, verified in prior browser audits | MATURE | 85% | `offline-pack.ts` | POST_LAUNCH_OK |
| J3 | Full-site offline | Entire product usable offline | **Explicitly never promised** — own audit table confirms only Workspace is fully guaranteed offline; Search and evidence pages are NOT offline at all | NOT_STARTED (by design) | 30% (of a full-site definition) | `reports/audits/MANUALFC_AS_BUILT_PRODUCT_PROGRESS_AUDIT.md` table §11 | CAN_FOLLOW_AFTER_LAUNCH |
| J4 | Cloud sync / conflict resolution | Cross-device sync | Zero code; nothing to conflict since there is no cloud | NOT_STARTED | 0% | zero "conflict" hits in `app/src/lib` | CAN_FOLLOW_AFTER_LAUNCH |

## K. Accounts / Cloud

| ID | Feature | Status | % | Evidence |
|---|---|---|---:|---|
| K1 | Authentication | NOT_STARTED | 0% | zero real auth code; only Vercel's own unrelated account system |
| K2 | Profile | FOUNDATION_ONLY (local only) | 20% | `CoachProfile` interface exists but is local-only, no account tied to it |
| K3 | Cloud state persistence | NOT_STARTED | 0% | zero DB/cloud client dependency in `package.json` |
| K4 | Cross-device sync | NOT_STARTED | 0% | confirmed — `CoachState` is single-device `localStorage` only |
| K5 | Backup / restore | NOT_STARTED | 0% | no export/import mechanism found |
| K6 | Account deletion / privacy controls | NOT_STARTED | 0% | no accounts exist to delete |

**Note on "architecture readiness" claims**: `FINAL_PRODUCT_FEATURE_LEDGER.md`'s "Architecture readiness table" (TASK-2806) labels Accounts/Cloud, Commercial, and Academy as `READY_WITH_MINOR_EXTENSION`. Direct code inspection (this audit) found this reflects **absence of hardcoded blockers**, not presence of implementation — e.g., "no hardcoded pro/premium/free checks found anywhere" is being read as a positive readiness signal, when it equally means no entitlement system exists at all. This ledger scores these capabilities by what is actually built (0%), not by the absence of things that would need to be undone.

## L. Commercial Product

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| L1 | Entitlements / plans (Free/Coach/Pro/Academy) | NOT_STARTED | 0% | zero entitlement/plan code found; `COMMERCIALIZATION_ROADMAP.md` explicitly: "prima versiune nu include ... paywall, licențiere" |
| L2 | Billing / subscriptions / trials | NOT_STARTED | 0% | zero Stripe/Paddle/billing dependency anywhere |
| L3 | Pricing surfaces / conversion funnel | NOT_STARTED | 0% | no pricing page found |
| L4 | Commercial onboarding | NOT_STARTED | 0% | onboarding exists (`onboardingDone` flag) but is for the free local product, not a paid signup flow |

## M. Academy / Club

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| M1 | Organization/multi-tenant model | NOT_STARTED | 0% | zero "org"/"academy"/"club" data model in `app/src` |
| M2 | Roles / permissions | NOT_STARTED | 0% | zero matches |
| M3 | Shared curriculum / sessions | NOT_STARTED | 0% | zero matches |
| M4 | Academy-level analytics | NOT_STARTED | 0% | zero matches |

## N. Multi-Age

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| N1 | Multi-age architecture (data model) | FOUNDATION_ONLY | 12% | `future_age_architecture` field with a provisional, explicitly-changeable order |
| N2 | Multi-age content/product | NOT_STARTED | **0%** | 100% of content, schemas (`const`), and routes are U11-only; **explicitly not counted as multi-age product per the master prompt's own hard-stop rule** |

## O. Multilingual

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| O1 | i18n architecture | NOT_STARTED | 0% | zero i18n/locale-routing infrastructure; Romanian hardcoded inline throughout templates |

## P. Search / Discovery

| ID | Feature | Final Target | Current | Status | % | Evidence |
|---|---|---|---|---|---:|---|
| P1 | Cross-domain search | Problems, Principles, Pedagogul, Antrenorul, Exercises, Sessions, competencies, media | Real working client-side search over 6 categories (Problems, Principles, Exercises, Sessions, 1 Assessment, 4 hardcoded volume summaries) — no competency search, no dedicated media search | FUNCTIONAL_BUT_PARTIAL | 55% | `app/src/lib/discovery-index.ts`; `app/src/pages/cauta.astro` |

## Q. Analytics / Observability

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| Q1 | Product analytics | NOT_STARTED | 0% | zero analytics dependency anywhere |
| Q2 | Technical observability/error tracking | NOT_STARTED | 0% | zero Sentry/monitoring dependency |

## R. Trust / Privacy / Safeguarding

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| R1 | Safeguarding content (data) | BUILT (as data, unusually mature) | 75% | `data/safeguarding/canonical.json` — 12 requirement + 15 risk entries citing real Romanian/EU/FIFA/UEFA law, real content not a stub |
| R2 | Safeguarding content wired into product UI | NOT_STARTED | 0% | zero pages under `app/src/pages` consume this data — it exists but is invisible to a real user |
| R3 | Privacy policy / consent / GDPR page | NOT_STARTED | 0% | no such page exists; only one inline form-warning string in the reflection tool |
| R4 | Data retention / deletion mechanism | NOT_STARTED | 0% | no accounts exist to have data retained/deleted from |

## S. Production / Operations

| ID | Feature | Status | % | Evidence |
|---|---|---|---|---|
| S1 | Vercel build/deploy pipeline | BUILT | 65% | `vercel.json` (build config only); manual Preview→Production promotion process used successfully across 30+ phases |
| S2 | CI/CD (automated gates on PR) | NOT_STARTED | 0% | no `.github` directory exists at all |
| S3 | Monitoring / backup / incident recovery | NOT_STARTED | 0% | no such documentation or code found |

---

## Cross-cutting note on "no double counting" (master prompt §32)

This ledger deliberately avoids counting the same underlying implementation twice:
- Gold Standard V2's competency IDs (A5/A6/A7/C1/C2) are counted once as **mechanism maturity** and once, separately, as **content breadth** (D1/D2) — the two percentages are intentionally very different (mechanism ~85%, breadth ~7%) and both are reported, never blended into a single misleading number.
- Media registry infrastructure (E9/E10, validator, schema) is scored separately from actual media asset counts (E1-E8) — a mature registry holding 15 mostly-synthetic entries does not inflate the real-video score.
- Reflection data existing on exercises/sessions (H3/H4) is not counted as "Coach Development complete" (H1/H5-H8 remain separately and honestly scored near-zero).
- Pedagogul/Antrenorul content maturity (A3/A4) is not re-counted as "competency framework linkage" (A5/A6, scored much lower) — writing a good chapter is not the same as wiring its competency ID into runtime data.
