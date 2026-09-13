# ManualFC — Final Product Feature Ledger

Legendă: `DONE`, `PARTIAL`, `FOUNDATION`, `NOT_STARTED`, `BLOCKED`, `FIELD_INPUT_REQUIRED`, `RESEARCH_REQUIRED`.

| Capability group | Feature | Status | Blocker / limit | Next wave |
|---|---|---:|---|---|
| Core methodology | Development, pedagogy, football methodology, motor learning, perception/decision, communication, safeguarding, parents | PARTIAL | 4/10 volume web complete; corpusul final rămâne sub pragurile cantitative | Content completion cluster |
| Core methodology | Principles, exercises, sessions, assessment, evidence | PARTIAL | 25 principles, 5 exercises, 2 sessions, 1 assessment; final contract asks 60/36 | Content completion cluster |
| Decision support | Problem Library, observation-first Decision Engine, tests, cues, intervention, verification, transfer | DONE | 8 problems; real transfer stays field input | Field evidence |
| Field system | Configurator, Surface Maps, 60/75, Field Cards, Field Mode, contingencies | DONE | Coverage is Gold Standard family, not full future library | Content expansion |
| Field system | One-hand mobile and outdoor readability | PARTIAL | Browser-validated; real outdoor field feedback missing | FIELD_INPUT_REQUIRED |
| Discovery | Search, filters, problem/principle/exercise/session discovery | DONE | Chapter results aggregate by volume | Discovery refinement |
| Multimedia | Static tactical diagrams | DONE | 5/5 Gold Standard exercises + 2/3 flagship problems (before/after); scope stays Gold Standard + flagship | Expand with content |
| Multimedia | Tactical loops | PARTIAL | Gold Standard: 3/3 applicable (raw 3/5 exercises — EX-0004/EX-0005 documented `NOT_APPLICABLE`, would fabricate a false fixed formation). Flagship problems: 1/3 raw, but 3/3 accounted for — PRB-0001 reuses EX-0001's existing loop one click away (documented, avoids duplicating the same movement); PRB-0002 is a spatial contrast, not a temporal sequence (documented); only PRB-0003 needed and has its own loop | Extend if new exercises/problems justify a genuinely new loop |
| Multimedia | Exercise animations | PARTIAL | 1 real Level-3 prototype (EX-0001 full role-swap cycle, 24s); not yet extended to EX-0002–EX-0005 | Extend per exercise if justified |
| Multimedia | Coach explainers | FOUNDATION / scripts ready | 3/3 flagship problems have production-ready 6-part scripts (`SCRIPT_READY`); no recorded audio/video exists or is claimed | Recording production |
| Multimedia | Captions / transcripts | FOUNDATION | Animations without speech carry an always-available text transcript (`<details>`); spoken-video caption/transcript contract documented but unused until real recordings exist | Recording production |
| Multimedia | Reduced motion | DONE | Every animated asset has a verified static fallback; enforced fail-closed by the media registry validator | Continuous |
| Multimedia | Static fallback | DONE | Every Level-2/3 asset degrades to a settled static frame, not a blank or broken state | Continuous |
| Multimedia | Real field video | FIELD_INPUT_REQUIRED | Genuine consented footage absent; 9-stage pipeline documented, unexecuted | FIELD_INPUT_REQUIRED |
| Multimedia | Match transfer video | FIELD_INPUT_REQUIRED | Must show target behaviour in freer play, not drill choreography; requirements documented, no footage exists | FIELD_INPUT_REQUIRED |
| Personal workflow | Anonymous/local mode, profile/onboarding, saved/favorite/recent/continue | DONE | Local-first only; cloud account absent. TASK-2806 found and fixed one real gap: problem context from a Decision Engine deep link did not survive into a session created via the quick "+ Ședință" action (static-prerendered pages never read the query string server-side) | Accounts/cloud sync |
| Personal workflow | Session Workspace, planning, history, reflection, assessment references | DONE | End-to-end integration verified (Decision Engine → exercise → Workspace → Group Configurator 12/1 and 16/2 → save → offline prepare → Field Mode 60/75 → Reflection both scenarios → returning-coach Continue), including a mixed-corruption test across all four state slices (sessions/reflections/offlinePacks/saved) with 0 crashes | Accounts/cloud sync |
| Personal workflow | Accounts and secure cloud persistence | NOT_STARTED | Provider/product decision required | Full accounts/cloud sync |
| Offline | Installable PWA (manifest, service worker, icons) | DONE | Vanilla service worker, no library; conservative update policy (no forced reload mid-session) | Continuous |
| Offline | Offline session preparation ("Disponibil pe teren") | DONE | Fail-closed: never claims ready unless every required route cached; deterministic resource graph, not a manually maintained list | Extend per canonical content growth |
| Offline | Offline Field Mode (timer, segment navigation, cue/observe, tactical visuals) | DONE | Browser-verified end-to-end for a prepared session, including cold start (fresh tab, no prior in-memory state) and mid-session online→offline transition | Continuous |
| Offline | Offline Surface Map / Field Cards / Group Configurator | PARTIAL | Deterministically re-rendered offline (verified: changing player count offline recomputes groups live, not a screenshot); only reachable through a prepared workspace session that links the canonical session itself, not yet through a standalone Field Card/Configurator visit | Extend prepare flow to cover standalone visits |
| Offline | Offline post-session reflection (save, no data loss) | DONE | Verified: full offline run — finish Field Mode → record observed/transfer state → save → reload — with zero loss | Continuous |
| Offline | Non-prepared content honest unavailable state | DONE | Dedicated fallback page, no crash, no blank page, explicit path back to Spațiul meu | Continuous |
| Offline | Cloud sync / cross-device reconciliation | FOUNDATION / NOT_STARTED | Only a documented future contract (stable IDs + `updatedAt`, no silent overwrite of newer local data); no sync code exists | Cloud sync wave |
| Offline | Full product offline (search, evidence pages, unvisited content) | NOT_STARTED | Explicitly out of scope — only sessions prepared from Spațiul meu are offline-guaranteed; everything else is "may work if visited before," never promised | Not planned this wave |
| Coach development | Learning path, competency/progress, gap recommendations | NOT_STARTED | Model and evidence rules required | Coach development wave |
| Academy/Club | Roles, organization workspace, shared curriculum/templates, collaboration, standards, permissions, auditability | NOT_STARTED | Organization UI explicitly out of Wave-4 | Academy/Club wave |
| Commercial | Open/Coach/Pro/Academy plans and entitlement boundary | FOUNDATION | Central policy in Wave-4; packaging unvalidated | Commercial discovery |
| Commercial | Billing, subscriptions, trials, upgrade, analytics | NOT_STARTED | Research/WTP and privacy decisions | RESEARCH_REQUIRED |
| Platform | Authentication, secure persistence, authorization | FOUNDATION | Replaceable ports; real auth absent | Accounts/cloud sync |
| Platform | Privacy/GDPR architecture, export/delete compatibility | FOUNDATION | No child PII; full DPIA/provider process pending | Privacy/account wave |
| Platform | Observability/error monitoring | NOT_STARTED | Provider decision | Platform hardening |
| Platform | Performance and accessibility | PARTIAL | Continuous gates; full audit remains per wave | Continuous |
| Expansion | U4–U18 architecture and age adaptation | FOUNDATION | User model age-band ready; content remains U11 | Multi-age wave |
| Expansion | Multilingual/regional variants | NOT_STARTED | Editorial and translation governance absent | Expansion wave |
| Expansion | Certification/CPD | RESEARCH_REQUIRED | Requires external validation/accreditation | Later decision |
| Knowledge foundation | Pedagog knowledge base (domain map) | FOUNDATION | 12 domains, 66 subdomains architected (`docs/knowledge/PEDAGOG_DOMAIN_MAP.md`); no lesson content authored yet | PHASE-30 research |
| Knowledge foundation | Coach knowledge base (domain map) | FOUNDATION | 34 domains architected (`docs/knowledge/COACH_DOMAIN_MAP.md`); no lesson content authored yet | PHASE-30 research |
| Knowledge foundation | Pedagog competency framework | DONE | 13 competencies complete at architecture level (`docs/knowledge/PEDAGOG_COMPETENCY_FRAMEWORK.md`); as of PHASE-33, `pedagog_competency_ids` are real, validated JSON properties on all 5 Gold Standard exercises, linked to real chapter IDs and displayed on the exercise page | PHASE-33 (DONE) |
| Knowledge foundation | Coach competency framework | DONE | 18 competencies complete at architecture level (`docs/knowledge/COACH_COMPETENCY_FRAMEWORK.md`); as of PHASE-33, `coach_competency_ids` are real, validated JSON properties on all 5 exercises + both sessions (`coach_objectives`), linked to real chapter IDs. COACH-C06 (Cueing) honestly declared `COMPETENCY_SUPPORTED`/`DEDICATED_CHAPTER_GAP` | PHASE-33 (DONE) |
| Knowledge foundation | Knowledge graph (extended) | DONE | No parallel graph built — the existing flagship-problem graph (`related_exercises`/`related_sessions`/`related_principles`/`assessment_links`, already implemented) now transitively surfaces the new PHASE-33 competency/lesson links via its existing exercise references (e.g. PRB-0003 → EX-0003 → its new competency/lesson fields), verified end-to-end from the problem page's existing "Deschide exercițiul" link | PHASE-33 (DONE) |
| Knowledge foundation | Theory-practice traceability | DONE | Contract defined and stress-tested against 3 example chains + 1 reverse chain (`docs/knowledge/THEORY_TO_PRACTICE_CONTRACT.md`); PHASE-33 implemented the missing explicit competency link as real, validated data (not just a documented gap) and verified 2 complete traces cap-to-cap with no broken link | PHASE-33 (DONE) |
| Knowledge foundation | Coach objectives in sessions | NOT_STARTED | Session Contract V2 specified, not implemented; today's sessions carry only child objectives | Session/Field/Reflection V2 wave |
| Knowledge foundation | Coach reflection | NOT_STARTED | Reflection V2 specified as an additive extension of the existing `SessionReflection` (same pattern used 3 times already); not implemented | Session/Field/Reflection V2 wave |
| Knowledge foundation | Coach development | NOT_STARTED | Depends on coach reflection + competency linkage; no Coach Score, no leaderboard by design | Coach development wave |
| Knowledge foundation | Research dossiers | FOUNDATION | 24 new domain-level dossiers added across PHASE-30 Wave-1+2+3 (`research/dossiers/*_R1.md`, total now 68 dossier files); still research inputs, no final lesson prose | PHASE-31/32 authoring |
| Knowledge foundation | Claim registry | FOUNDATION | Grew from 103 to 380 claims, 112 to 361 sources across all of PHASE-30, all schema-validated against the existing `claim-registry.schema.json`/`source-registry.schema.json`; no competing vocabulary introduced; independent claim-to-source audit sample (14 claims across 3 waves) found 0 mismatches | PHASE-31/32 authoring |
| Knowledge foundation | Content depth layers (4-layer model) | FOUNDATION | Formalizes the existing 2-level model (`CONTENT_STRATEGY.md`) into 4 explicit presentation depths over one canonical object; no UI change | Continuous |
| Knowledge foundation | Competency evidence matrix | FOUNDATION | 23 of 31 competency families now have direct PHASE-30 research linkage (`docs/knowledge/research/COMPETENCY_EVIDENCE_MATRIX_R3.md`, final), up from 13 after Wave-1; remaining 8 are mostly already-functional product areas (organization, evaluation) or pre-existing mature domains (safety, dignity) | PHASE-31/32 authoring |
| Knowledge foundation | Overclaim watchlist | FOUNDATION | 35+ verified coaching myths/oversimplifications catalogued (`docs/knowledge/research/MANUALFC_RESEARCH_OVERCLAIM_WATCHLIST.md`, v2.0), spanning cueing, feedback frequency, questioning, coach-child relationship, group competition, parent involvement, and coach reflection | Continuous |
| Knowledge foundation | Pedagog domain coverage | FOUNDATION | All 12 of 12 Pedagog domains are now `FOUNDATION_READY` or `EXISTING_EVIDENCE_REUSED` (`docs/knowledge/research/PEDAGOG_RESEARCH_COVERAGE_MATRIX_R3.md`, final) — 0 `PARTIAL`, 0 `NOT_RESEARCHED`; this closes the research-foundation gate for Pedagogul V1 authoring | PHASE-31 authoring |
| Knowledge foundation | Coach domain coverage | FOUNDATION | All 34 of 34 Antrenorul domains now have an explicit, justified state (`docs/knowledge/research/COACH_RESEARCH_COVERAGE_MATRIX_R3.md`, final) — 0 `NOT_RESEARCHED`; coach identity, session design, medium-term planning, and differentiation (all previously zero-coverage) are now `FOUNDATION_READY`; coach positioning is honestly formalized as `PRACTICE_HEURISTIC` rather than backed with manufactured science | PHASE-32 authoring |
| Content | Pedagogul V1 — Volume 01 (10 chapters) | DONE | PHASE-31 authored 5 genuinely new chapters (CH-0106 emotions, CH-0107 relationship, CH-0108 communication, CH-0109 parents, CH-0110 child metacognition) extending the 5 that already existed (CH-0101-0105), after discovering the blueprint's planned "12 new chapters" would have duplicated 5 already-published ones. All 13 Pedagog competency families now have a home chapter (PED-C12, parents, was previously the sole UNRESOLVED one). Live at `/volum/01/ch-0101` through `/volum/01/ch-0110`; `npm run check` and `npm run build` both pass clean | PHASE-32 (Antrenorul V1) |
| Content | Antrenorul V1 — 9 new chapters (VOLUME-03/04) | DONE | PHASE-32 authorized and completed: existing-content reconciliation found ~40-50% of the originally-scoped 15 modules already existed (CH-0301-0306, CH-0401-0406), reducing new authoring to 9 chapters (CH-0307/0308/0309/0310; CH-0407/0408/0409/0410/0411), each sourced from a dedicated research dossier under the Antrenorul lesson contract plus four new required sections (pedagogy linkage, coaching competencies, practice linkage, coach reflection). No Coach Score/ranking anywhere; the "85% rule" and LTAD explicitly identified and rejected as unvalidated. `GOLD_STANDARD_V2_MAPPING.md` adds the required EX-0001-0005/SES-0001-0002 mapping with no schema migration. Full Pedagogul↔Antrenorul competency audit (13 PED-C × 18 COACH-C) and 6 theory-to-practice trace chains documented, with one gap honestly declared (COACH-C06 Cueing has no dedicated narrative chapter). Live at `/volum/03/ch-0307`-`ch-0310` and `/volum/04/ch-0407`-`ch-0411`; Educational Page System V1 components applied to all 9. A real pre-existing H1-overflow defect (DEC-0075's fix never propagated to volume-02/03/04) was found during QA and fixed identically across all affected files. 60/60 real-browser route×viewport combinations PASS; baseline `MANUALFC_ANTRENORUL_V1_BASELINE = 00cd0f5` | DEC-0077 |
| Content / Knowledge foundation | Gold Standard V2 — EX-0001-0005 + SES-0001/0002 migration | DONE | PHASE-33 turned the PHASE-32 documentation-only mapping into real, additive, validated schema/data: `exercise.schema.json`/`session.schema.json` gained 16+7 optional fields (zero `required` changes, V1 content stays valid), plus a dedicated `scripts/validate_gold_standard_v2.py` that checks every V2 object's fields are non-empty and every referenced ID (PED-C/COACH-C/chapter/principle/assessment) resolves against its real canonical source. All 5 exercises and both sessions migrated sequentially (EX-0001 as reference implementation, full gates before continuing), with the loop surfaced in the product itself — a new "Pedagogul → Antrenorul → Practica" section on the exercise page, a "Copiii și antrenorul" dual-objective section plus two-dimension reflection on the session page, and coach-focus/non-intervention/verification lines in Field Mode. Two real defects found and fixed: an unsupported "45 de grade" repetition caught by an existing test, and a pre-existing color-contrast defect on the session pages (fixed because it blocked this phase's own declared QA gate). `ASM-0001` and `CoachState` deliberately left unmodified per the phase's own scope rules. 76 real-browser route×viewport combinations PASS; baseline `MANUALFC_GOLD_STANDARD_V2_BASELINE = 1404fb9` | DEC-0078 |
| Content / UX | Educational Page System V1 (Pedagogul lesson architecture) | DONE | Evidence-based page architecture (`docs/ux/MANUALFC_EDUCATIONAL_PAGE_STANDARD_V1.md`) — Model C Hybrid (nucleus always visible, comprimable elaboration, quick-recall surface) applied to all 10 VOLUME-01 chapters; 6-component budget (`docs/ux/EDUCATIONAL_COMPONENT_CONTRACT.md`); live-audited with a real browser (Chrome via CDP, user-authenticated session) — 28 page×viewport combinations, real Axe scan (0 violations across 5 pages), interactive tests (compression toggle, Quick Recall, keyboard, deep links) all PASS; one real MAJOR defect (mobile H1 overflow, pre-existing but found on a test page) and one real content-fidelity defect were found and repaired during earlier gates (DEC-0072), plus a pre-existing zero-byte working-tree corruption (4 unrelated files, predating this task) found and repaired (DEC-0075); baseline `aff2017` | Reused as-is by Antrenorul V1 (PHASE-32, DONE) |

## Permanent constraints

Safety, safeguarding and evidence limitations can never be paywalled. No child identity is required by the current domain. Every wave must update this file without deleting rows silently.

## Architecture readiness (TASK-2806)

Statuses: `READY`, `READY_WITH_MINOR_EXTENSION`, `REQUIRES_REFACTOR`, `BLOCKED`.

| Future cluster | Status | Why |
|---|---|---|
| Accounts + cloud persistence | READY_WITH_MINOR_EXTENSION | `CoachStatePort` is already the single point of contact for all state (`saved`/`favorites`/`recents`/`sessions`/`reflections`/`offlinePacks`); every entity already carries a stable `id` and `createdAt`/`updatedAt`. Swapping the `localStorage` adapter for a cloud-backed one requires no product UI rewrite — only a new `CoachStatePort` implementation and an auth boundary. |
| Cross-device sync | READY_WITH_MINOR_EXTENSION | The `updatedAt`-based no-silent-overwrite contract is documented (`docs/architecture/OFFLINE_ACCOUNT_ENTITLEMENT.md`) but unimplemented — no merge/conflict resolution code exists yet. Missing piece: an actual sync engine, not a data-model rework. |
| Commercial / entitlement | READY_WITH_MINOR_EXTENSION | No scattered hardcoded `pro`/`premium`/`free` checks found anywhere in the codebase during this audit. A future entitlement layer can wrap existing features (offline pack count, saved-session limits, etc.) without touching their internals. |
| Academy / Club | READY_WITH_MINOR_EXTENSION | `WorkspaceSession`/`SessionReflection` already carry only stable IDs and coach-entered configuration, never copied canonical prose — adding an `organizationId`/shared-template origin later is additive, not a redesign. |
| Multi-age (U4–U18) | REQUIRES_REFACTOR | The user-facing domain model itself (`CoachProfile`, `WorkspaceSession`) carries no U11 hardcoding, but every piece of canonical content (`data/exercises`, `data/sessions`, `data/problems`) and every generated static route is U11-only by construction — a real content and generation-pipeline expansion, not a config flag. |
| Multilingual | REQUIRES_REFACTOR | No i18n routing, no string externalization; all Romanian copy is inline in `.astro` templates. A real refactor, not a minor extension. |

## Capability maturity summary (TASK-2806)

Buckets: `MATURE`, `FUNCTIONAL_BUT_PARTIAL`, `FOUNDATION_ONLY`, `NOT_STARTED`, `FIELD_INPUT_REQUIRED`. No invented percentage.

| Group | Bucket |
|---|---|
| Core methodology | FUNCTIONAL_BUT_PARTIAL |
| Decision Engine | MATURE |
| Field system | MATURE |
| Discovery | MATURE |
| Workspace / persistence | MATURE |
| Assessment / transfer loop | FUNCTIONAL_BUT_PARTIAL (real transfer confirmation stays field input by design) |
| Multimedia | FUNCTIONAL_BUT_PARTIAL |
| Offline (prepared session) | MATURE |
| Offline (full product) | NOT_STARTED (by design, documented) |
| Accounts / cloud | FOUNDATION_ONLY |
| Coach development | NOT_STARTED |
| Academy / Club | NOT_STARTED |
| Commercialization | FOUNDATION_ONLY |
| Multi-age | FOUNDATION_ONLY |
| Multilingual | NOT_STARTED |
| Real field/match video | FIELD_INPUT_REQUIRED |
