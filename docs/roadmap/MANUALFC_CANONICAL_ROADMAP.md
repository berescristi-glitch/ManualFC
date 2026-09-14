# ManualFC — Canonical Roadmap (TASK-3711)

**Status: ACTIVE — this is the single canonical planning document.**
Superseded/historical: `COMMERCIALIZATION_ROADMAP.md`, `ROADMAP_MIGRATION_REPORT.md`, `MULTI_AGE_EXPANSION_ARCHITECTURE.md` (kept as historical input/aspiration records — do not treat as current plan). Future tasks derive from this document; do not create a competing master roadmap. Routine implementation fixes do not require a new DECISION document (see §24).

Built directly from the TASK-3710 Master Audit (no new repository research — this is synthesis). Evidence tags: **FACT** / **INFERENCE** / **DECISION** / **DEPENDENCY** / **ASSUMPTION**.

---

## 1. EXECUTIVE ROADMAP (one page)

ManualFC is a pedagogically rigorous but content-thin product (maturity ~43/100, **FACT**-based from TASK-3710) built on a lean, sound technical foundation. It is not ready for Public Beta. The path is: **fix three cheap P0 defects → deepen the one proven content theme → run a real pilot with 2–5 coaches → let their behavior (not internal assumption) decide the next theme, the next content pillar, and whether multi-age expansion is even worth starting.** Multi-age (4–18) is a schema-level redesign, not a content task, and must not begin until U11 usage evidence justifies it. Governance/documentation growth is itself a diagnosed risk and this roadmap replaces, not adds to, that volume.

**Current phase:** Phase 0 (Stabilize the Baseline) — not yet exited.
**Current gate:** Gate A, not yet passed.
**Top 3 priorities:** (1) fix the `/gold-standard/rapid` nav mis-route, (2) unblock the Git remote (TASK-3709), (3) declare the undeclared Playwright/axe dependencies.
**Current blockers:** TASK-3709 (remote authentication) is externally blocked pending user action.
**Next decision point:** once Gate A passes, decide Phase 1 content target (which exercises to add) with no new research needed — the theme is already chosen (see §6).

---

## 2. PRODUCT NORTH STAR

*ManualFC is a local-first coaching-methodology and field-decision tool for the individual U11 volunteer coach who needs to build real pedagogical judgment over time AND get an honest, evidence-bounded answer to a specific in-game problem right now — without an account, an app store, or a connection.* (**DECISION**, carried forward from TASK-3710 §3)

---

## 3. PRIMARY USER

**The individual U11 volunteer/grassroots coach, alone, without club infrastructure.** (**FACT**, implicit in the product's own A/B "învăț"/"rezolv" framing at `app/src/pages/index.astro`)

Explicitly NOT the near-term target: club administrator, technical director, player, parent, scout, analyst, CRM user. (**DECISION**) These become candidates only if pilot evidence (Phase 2/3) surfaces real demand — **needs validation**, none exists today.

---

## 4. CURRENT BASELINE

Carried verbatim from TASK-3710 (**FACT** unless noted): Astro static, 2 runtime deps, 101 pages, 518 pytest (74% one-off task tests — **not** equivalent to behavioral regression coverage), 5 exercises, 2 sessions, 8 problems, 39 chapters, 3 empty content pillars (case studies/scripts/season plans), U11 hardcoded as JSON-Schema `const` in 6+ schemas, no auth/DB, no PII, strong offline architecture, coherent post-migration brand, zero SEO infrastructure, no remote git backup (blocked mid-TASK-3709), 12 dead components, split search, weak `/spatiul-meu` empty states, disproportionate governance volume (123 KB DECISIONS.md, 268 report files).

**Maturity: ~43/100. Readiness: Private Pilot, not Public Beta.** (**FACT**, from TASK-3710 §23)

---

## 5. STRATEGIC PRINCIPLES

The 12 principles from the task brief are adopted as-is and are binding on all future prioritization: fix blockers before expansion; validate one user before many; deepen before multiplying; real usage beats assumption; product value beats governance volume; reusable coverage beats task-count growth; U11 must work before 4–18 starts; offline is a differentiator to preserve; evidence-bounded pedagogy is non-negotiable; no infrastructure for hypothetical users; no auth/DB/cloud until justified; keep the architecture simple as long as possible. (**DECISION**)

---

## 6. ROADMAP PHASES (0 → 10)

### Phase 0 — Stabilize the Baseline
**Objective:** remove every P0/high-confidence/low-effort defect.
**Work:** fix `/gold-standard/rapid`→`/rezolva-pe-teren` nav mis-route (**FACT**, TASK-3710 §11); complete TASK-3709 remote backup (**DEPENDENCY** — blocked on user-side GitHub auth, not code); declare `playwright`/`@axe-core/playwright` in `package.json` devDependencies (**FACT**, TASK-3710 §13); verify clean `npm install`→`npm run build` on a fresh clone; add `site:` to `astro.config.mjs` + minimal sitemap/robots (**FACT**, TASK-3710 §18); wire one automated browser+axe smoke check into a CI-equivalent script; confirm build stability (101 pages) and offline behavior unchanged.
**Exit condition:** fresh clone → install → build → test → open, with zero special local knowledge required.
**Effort:** low (days, not weeks) — none of this is new architecture.

### Phase 1 — Deepen the Proven U11 Core
**Objective:** enough depth that a coach uses ManualFC repeatedly, not just inspects it.
**Explicit non-goal:** no new training themes yet (**DECISION**).
**Target:** 15–20 exercises (from 5), 6–8 sessions (from 2), stronger problem→exercise→session→chapter links, richer `/spatiul-meu` empty/continuation states, one unified search (retiring the duplicate `/rezolva-pe-teren` local filter — **FACT** of duplication, TASK-3710 §11).
**Exit condition:** a coach can plan several real training weeks without hitting a dead end.

### Phase 2 — Private Pilot
**Objective:** test with real coaches, not internal review.
**Recruit:** 2–5 real volunteer U11 coaches (**ASSUMPTION** that this population is reachable — needs validation of recruitment channel).
**Test surfaces:** onboarding, finding exercises, Decision Engine, mobile use, offline use, session readability, navigation, pedagogical clarity, `/spatiul-meu` usefulness, return usage.
**Measure behavior, not compliments** (explicit rule, §9 detail below).
**Exit condition:** ≥2 external coaches independently use ManualFC across multiple real sessions without continuous owner explanation.

### Phase 3 — Product Reality Check
**Objective:** turn pilot evidence into a validated backlog.
**Output:** friction ranking; classify every finding MUST FIX / SHOULD FIX / IGNORE / NOT NOW.
**Rule:** do not implement every request (§18 Stop/Go governs this explicitly).
**Exit condition:** a backlog exists that is evidence-derived, not assumption-derived.

### Phase 4 — Second Complete Training Theme
**Objective:** prove the content model repeats.
**Scope:** one new theme, full stack — methodology, exercises, sessions, Decision Engine problems, reflections, cross-links, offline availability.
**Theme selection:** decided in Phase 3, from pilot evidence — **needs validation**, not pre-selected here.
**Exit condition:** two themes work end-to-end on the same architecture.

### Phase 5 — Content System Maturity
**Objective:** populate exactly one currently-empty pillar (case studies / communication scripts / season plans), selected by pilot-evidenced need, not schema convenience (**DECISION**: do not fill all three "because schemas exist" — TASK-3710 explicitly flagged this anti-pattern).
**Exit condition:** that one pillar demonstrably helps in real pilot usage.

### Phase 6 — Public Beta Readiness (gate, not work)
Entry requires ALL of: P0 defects gone; remote exists; CI browser/a11y smoke exists; nav stable; two themes complete; content breadth no longer demo-like; repeat real coach usage observed; major pilot friction addressed; offline proven in real use; mobile performance acceptable; SEO fundamentals present; no major accessibility blocker. **Not** page count or task count (explicit rule).

### Phase 7 — Public Beta
**Objective:** controlled wider exposure. Focus: reliability, search, discovery, retention, field usability, bug/support intake, content demand signal. **No large architecture changes** unless real usage forces it (**DECISION**).

### Phase 8 — Multi-Age Architecture Design
**Only if** U11 usage justifies it (**DEPENDENCY** on Phase 2/3/7 evidence, not calendar time). Real product-model work: age-category model, schema refactor (`const`→parameter, **not** a find-replace — explicit warning in the brief), shared-vs-age-specific principles, progression model, route implications, migration plan.

### Phase 9 — First Multi-Age Expansion
One adjacent band only (U9 or U13 — **ASSUMPTION**, actual choice needs pilot-demand validation), chosen on content transferability + demand + pedagogical adjacency + effort. Exit: two age groups coherent, no methodology-model corruption.

### Phase 10 — Scale Toward 4–18
Only after Phase 9 succeeds. Bands (4–6, 7–8, 9–10, 11–12, 13–14, 15–16, 17–18) are a **starting hypothesis to re-evaluate pedagogically**, not a committed structure (**ASSUMPTION**, needs validation against real developmental-stage evidence before locking in).

---

## 7. DEPENDENCY MAP

```
REMOTE + BASELINE STABILITY (Phase 0)
        ↓
CONTENT DEPTH (Phase 1)
        ↓
PRIVATE PILOT (Phase 2)  ← cannot start before Phase 0 nav/baseline fixes
        ↓
PRODUCT REALITY CHECK (Phase 3)
        ↓
SECOND THEME (Phase 4)  ← theme choice depends on Phase 3 evidence
        ↓
CONTENT PILLAR MATURITY (Phase 5)  ← pillar choice depends on Phase 3 evidence
        ↓
PUBLIC BETA READINESS GATE (Phase 6)
        ↓
PUBLIC BETA (Phase 7)
        ↓
MULTI-AGE DESIGN (Phase 8)  ← gated on Phase 7 usage evidence, not time
        ↓
FIRST SECOND AGE (Phase 9)
        ↓
SCALE 4–18 (Phase 10)
```
Dependencies override priority scores (§12 rule) — e.g., Phase 2 cannot start before Phase 0's nav fix regardless of how "exciting" a pilot feels.

---

## 8. MILESTONE GATES

| Gate | PASS | FAIL | BLOCKED |
|---|---|---|---|
| **A** — Stable baseline | Fresh clone builds/tests/opens clean; nav fixed; remote exists | Any of these fail on a truly fresh clone | Remote auth unresolved (current state) |
| **B** — Content depth for pilot | 15–20 exercises, 6–8 sessions, no dead-end paths in the core loop | Coach would hit a dead end in normal use | Content authoring not yet started |
| **C** — Private pilot validated | ≥2 coaches use it repeatedly, unprompted | Coaches need continuous explanation or abandon after one use | Pilot not yet recruited |
| **D** — Two themes proven | Both themes complete end-to-end, no model corruption | Second theme requires special-casing the architecture | Theme 2 not started |
| **E** — Public beta ready | All Phase 6 entry conditions met | Any one missing | — |
| **F** — Multi-age architecture ready | Schema redesigned, migration plan validated | `const`→enum treated as "done" without model work | Design not started |
| **G** — First second-age pilot | Two age groups coherent, no regressions to U11 | Regression in U11 quality, or model duplication instead of proper abstraction | Age-band choice unvalidated |

No phase starts merely because time has passed (explicit rule).

---

## 9. NEXT 7 DAYS
**Objective:** clear every Phase-0 P0 item.
**Must:** fix nav mis-route; resolve TASK-3709 remote auth and complete the push+fresh-clone verification; declare Playwright/axe as real devDependencies.
**Should:** add `astro.config.mjs` `site:` + sitemap/robots.
**Non-goals:** no new content, no design changes.
**Exit criteria:** fresh clone builds/tests/deploys clean; `origin/main` exists and independently reconstructs the repo (per TASK-3709's own acceptance criteria).
**Dependency:** remote fix depends on user supplying working GitHub authentication (external blocker, not engineering effort).
**Risk:** if auth remains blocked, Phase 0 cannot fully close — flag explicitly, do not silently skip.

## 10. NEXT 30 DAYS
**Objective:** Phase 1 content depth + UX cleanup.
**Must:** unify search; improve `/spatiul-meu` empty states; wire CI browser/a11y smoke check; author exercises toward the 15–20 target within the existing theme.
**Should:** begin informal outreach for 1–2 pilot coaches.
**Non-goals:** no second theme, no schema/age work.
**Exit criteria:** Gate B trending toward pass; at least 10 total exercises.

## 11. NEXT 60 DAYS
**Objective:** finish Phase 1, start Phase 2.
**Must:** reach 15–20 exercises / 6–8 sessions; recruit and onboard 2–5 pilot coaches.
**Should:** first informal reflection on pilot behavior (not yet the formal Phase 3 reality check).
**Exit criteria:** Gate B passed; pilot actively running.

## 12. NEXT 90 DAYS
**Objective:** complete Private Pilot and Product Reality Check.
**Must:** run Phase 2 to its exit condition; produce the Phase 3 MUST/SHOULD/IGNORE/NOT-NOW backlog.
**Should:** decide (from evidence) the second theme and the one content pillar to mature.
**Exit criteria:** Gate C passed; validated backlog exists.
**The single most important outcome for these 90 days: real, repeated, independent use of ManualFC by at least two coaches who were not walked through it — everything else is secondary to obtaining this evidence.**

## 13. NEXT 180 DAYS
**Objective:** Phase 4 + Phase 5, approach Gate E.
**Must:** ship second complete theme; mature one content pillar.
**Should:** re-evaluate whether Public Beta conditions (Phase 6) are realistically close.
**Non-goal:** do not start multi-age design yet unless Phase 3 evidence explicitly demands it (**needs validation**, not assumed).

## 14. NEXT 12 MONTHS
**Objective:** reach Gate E (Public Beta Readiness) and, only if justified, open Phase 7. Multi-age design (Phase 8) begins within this window **only if** beta usage data shows real demand — this is a conditional milestone, not a calendar commitment (**ASSUMPTION** flagged: do not schedule Phase 8 into month 10 "because it's next" without evidence).

---

## 15. CONTENT ROADMAP

| Phase | Chapters | Exercises | Sessions | Problems | Case studies | Scripts | Season plans |
|---|---|---|---|---|---|---|---|
| Current | 39 | 5 | 2 | 8 | 0 | 0 | 0 |
| Phase 1 exit | 39 (no new) | 15–20 | 6–8 | 8–10 | 0 | 0 | 0 |
| Phase 4 exit | +theme-2 chapters as needed | +theme-2 set | +theme-2 set | +theme-2 problems | 0 | 0 | 0 |
| Phase 5 exit | — | — | — | — | *one of these three, evidence-selected* | | |

Every new exercise must answer the 8 questions in the brief (problem solved, constraint rationale, intervene/don't-intervene criteria, do-not-assume, game-transfer, session membership, evidence boundary) — this is already the Gold Standard schema's intent (TASK-3710 §9) and is reaffirmed as mandatory, not optional, going forward (**DECISION**: promote the currently-optional pedagogy fields to effectively-required practice even where the schema doesn't enforce it).

---

## 16. PEDAGOGICAL ROADMAP

| Stage | What exists | What coach can do | Learning outcome | Validate before advancing |
|---|---|---|---|---|
| **Drill library** (superseded — already past this) | — | — | — | — |
| **Coach decision system** (current) | Decision Engine (8 problems), 5 exercises | Diagnose one observed behavior, get one evidence-bounded response | Coach makes a better in-moment adjustment | Pilot coaches actually use Decision Engine unprompted (Phase 2) |
| **Coach learning system** (target of Phase 1/4/5) | 15–20+ exercises, 2 themes, richer reflection | Build judgment across sessions, not just react once | Coach's own reflections show pattern-recognition over time | `/spatiul-meu` reflection data shows repeat, evolving use |
| **Age-progressive methodology platform** (Phase 8–10) | Multi-age schema, 2+ age bands | Follow a player/team's development across years | Longitudinal coherence, not just per-age content | Phase 9 shows no model corruption between ages |

---

## 17. TECHNICAL ROADMAP

**NOW:** stability, reproducibility (Phase 0), browser/a11y CI, SEO basics, image optimization (astro:assets or sharp — trigger: content volume growing means unoptimized-PNG pattern compounds, TASK-3710 §15), remote backup.

**LATER, ONLY IF TRIGGERED:**
- **Authentication** — trigger: pilot coaches request saving across devices, not just one browser's localStorage.
- **Database** — trigger: authentication is approved AND content volume makes static JSON authoring genuinely unwieldy (not before).
- **Cloud sync** — trigger: same as authentication; do not build ahead of accounts.
- **Multi-user roles / club management** — trigger: a real club (not an individual coach) explicitly requests it during/after beta, per the "not the near-term persona" decision in §3.
- **Analytics backend** — trigger: Public Beta begins and product decisions genuinely need usage data beyond direct pilot observation.
- **Payments / marketplace** — trigger: Public Launch is approaching AND a real monetizable unit of value exists (not before).
- **Personalization engine** — trigger: enough content variety exists that "which content for this coach" is a real problem (not at 5–20 exercises).

No speculative platform engineering before its trigger (explicit rule).

---

## 18. UX ROADMAP

Critical journey: **HOME → identify intent → learn OR solve → find relevant content → use session/exercise → save/continue → return.**

| Priority | Fix | Phase |
|---|---|---|
| 1 | Correct core CTA routing (`/gold-standard/rapid` → `/rezolva-pe-teren`) | 0 |
| 2 | Unify search | 1 |
| 3 | Strong `/spatiul-meu` empty states | 1 |
| 4 | Mobile-first CSS pass (currently desktop-first-then-squeezed, TASK-3710 §11) | 1–2 |
| 5 | Faster re-entry into recent content (continue-logic already exists in `coach-state.ts` — surface it more prominently) | 1 |
| 6 | Reduce navigation complexity (footer duplicates header with zero added value) | 1 |
| 7 | 404 with real recovery options (search/suggested links) | 2 |

---

## 19. USER VALIDATION ROADMAP

| Stage | Who | What they test | Duration | Measure | Success | Stop |
|---|---|---|---|---|---|---|
| **Stage 1** | 2–3 volunteer U11 coaches | Onboarding, Decision Engine, mobile/offline use, session prep | 2–4 weeks each | **Behavior**: return visits, exercises reopened, Decision Engine hits, dead-end rate | ≥2 coaches use independently across multiple real sessions | Coaches abandon after one session despite fixes |
| **Stage 2** | 5–10 coaches | Broader content (post Phase 4), search, reflection habits | 4–8 weeks | Repeat usage, content discovery success rate | Consistent multi-week return usage across most participants | Repeated, unresolved confusion despite iteration |
| **Stage 3** | Controlled public beta | Reliability, retention, support load, content demand | Ongoing | Weekly active coaches, retention, search success | Stable/growing usage, manageable support burden | Reliability or retention regress vs. Stage 2 |

**What users say vs. what they do:** compliments/complaints are recorded but **behavior (reopened content, return visits, actual field usage) governs every MUST FIX / SHOULD FIX classification** (explicit rule, §9 of brief).

---

## 20. SEO / DISCOVERABILITY ROADMAP

Phase 0: `site:` config + sitemap + robots (near-free, do regardless of content readiness — TASK-3710 §18 explicitly separates "infrastructure hygiene" from "premature SEO optimization"). Do **not** invest further in SEO (content marketing, backlinks, keyword targeting) before Phase 4/6 — product value must exist before it's worth ranking for. **Needs validation:** whether organic search is even the right acquisition channel for grassroots volunteer coaches (no evidence either way currently).

---

## 21. QUALITY / TESTING ROADMAP

Phase 0: declare real devDependencies, add one automated browser+axe smoke check. Phase 1–2: convert the highest-value one-off task tests into reusable regression suites as time allows (not a dedicated project — opportunistic, per TASK-3710 §14's finding that 74% of tests are one-off). Phase 6 entry requires this CI gate to be real and running, not aspirational.

---

## 22. OFFLINE ROADMAP

Offline is a confirmed strategic differentiator (TASK-3710 §17, the single most technically mature subsystem) — **preserve, don't touch**, through Phase 0–5. Only revisit if Phase 2/3 pilot evidence shows offline usage is actually low-value to real coaches (§18 Stop/Go example explicitly names this scenario) — **needs validation**, currently assumed valuable based on product design intent, not measured real usage.

---

## 23. MULTI-AGE ROADMAP

See Phases 8–10 above. Restated constraint: **do not** treat `const: "U11"` → enum as the deliverable — this is a product-model decision (age-appropriate progression, shared vs. unique principles, developmental-stage differences) requiring the same rigor as the original U11 schema design. Entry trigger is Phase 7 usage evidence, not elapsed time.

---

## 24. GOVERNANCE SIMPLIFICATION

**Rule: Roadmap > Task Registry > Implementation.** This document is the one active roadmap. No new competing master roadmap/audit documents.

| Type | When required |
|---|---|
| **DECISION RECORD** | Only for choices that materially change architecture or product direction (e.g., "start multi-age design," "adopt a database") — NOT for routine content additions or bug fixes |
| **NORMAL TASK** | Any planned unit of work traceable to this roadmap's phases |
| **BUG FIX** | Defect correction with no architectural implication — no decision record, no lengthy report required |

This directly addresses TASK-3710 §20's finding (84 decision entries, one 815 words for a logo-PNG swap, 268 report files, 7+ overlapping master audits). Going forward: **routine implementation fixes get a one-line changelog entry, not a DEC-XXXX essay.**

---

## 25. KPI FRAMEWORK

**Early-stage (Phase 2–5), all currently at zero/unmeasured — needs baseline:**
real coaches using ManualFC; sessions prepared with it; exercises reopened >1×; Decision Engine invocations; offline-route usage; return-usage rate; time-to-find-useful-content; dead-end rate; pilot completion rate; number of fully-realized themes (currently 1).

**Later-stage (Phase 6+):** weekly active coaches; retention; content-discovery rate; search success rate; session-plan reuse.

No numerical targets are set here — none are evidence-backed yet (**explicit "needs validation"** per brief's rule against invented targets). First action is instrumenting measurement itself, not hitting a number.

---

## 26. RISK REGISTER

| Risk | Probability | Impact | Early warning | Mitigation |
|---|---|---|---|---|
| Insufficient content breadth | High (current fact) | High | Pilot coaches run out of relevant content quickly | Phase 1 depth work before pilot |
| Overbuilding governance | High (already observed) | Medium | New audit/decision docs outpacing shipped content | §24 rule enforcement |
| Age expansion too early | Medium | High | Schema work starts before Phase 7 evidence | Gate F/dependency enforcement |
| No real coach adoption | Medium | Critical | Pilot recruits don't return after session 1 | Behavior-based Stop/Go (§18) |
| Content consistency degradation at scale | Medium | Medium | New exercises skip the 8 mandatory pedagogy questions | Make pedagogy fields practice-mandatory now (§15) |
| Pedagogical rigor lost while scaling | Medium | High | Same as above | Same |
| Offline regressions | Low (currently solid) | High if it happens | SW cache-version bump forgotten | Add version-bump check to CI (Phase 0/21) |
| Test-suite false confidence | High (already documented) | High | Real bugs shipped despite 518 green tests | Automated browser/a11y CI (Phase 0) |
| Image/performance growth | Medium | Medium | Build output size creeping up | Image pipeline (Phase 0/17) |
| Schema lock-in (U11 const) | High (current fact) | High for Phase 8+ | Attempting non-U11 content against current schema | Gate F enforcement |
| Single-maintainer dependence | High (current reality) | Critical | No backup, no remote (current state) | Phase 0 remote fix |
| Backup/repository risk | **Realized once already** (this session's git corruption incident) | Critical | — | Remote + secondary backup (Phase 0, TASK-3709) |

---

## 27. TOP 20 PRIORITIES (ranked; dependencies override raw score)

| # | Initiative | Impact | Urgency | Confidence | Effort(inv.) | Risk↓ | User evid. | Phase |
|---|---|---|---|---|---|---|---|---|
| 1 | Fix nav mis-route | 5 | 5 | 5 | 5 | 5 | 0 | 0 |
| 2 | Complete remote backup (TASK-3709) | 5 | 5 | 4 | 4 | 5 | 0 | 0 |
| 3 | Declare Playwright/axe deps | 3 | 4 | 5 | 5 | 4 | 0 | 0 |
| 4 | `site:` + sitemap/robots | 4 | 3 | 5 | 5 | 3 | 0 | 0 |
| 5 | Automated browser/a11y CI smoke check | 5 | 4 | 3 | 2 | 5 | 0 | 0 |
| 6 | Unify search | 3 | 3 | 4 | 4 | 2 | 0 | 1 |
| 7 | Improve `/spatiul-meu` empty states | 4 | 3 | 4 | 4 | 2 | 0 | 1 |
| 8 | Author 10–15 more exercises (existing theme) | 5 | 4 | 3 | 2 | 3 | 0 | 1 |
| 9 | Author 4–6 more sessions | 4 | 4 | 3 | 2 | 3 | 0 | 1 |
| 10 | Image optimization pass | 3 | 2 | 5 | 4 | 2 | 0 | 0–1 |
| 11 | Recruit 2–5 pilot coaches | 5 | 4 | 2 | 3 | 4 | 0 | 2 |
| 12 | Run Private Pilot | 5 | 4 | 2 | 2 | 5 | 0 | 2 |
| 13 | Produce validated backlog (Phase 3) | 4 | 3 | 3 | 3 | 3 | 5* | 3 |
| 14 | Second training theme | 5 | 2 | 3 | 1 | 3 | 0 | 4 |
| 15 | Mature one content pillar | 3 | 2 | 3 | 2 | 2 | 0 | 5 |
| 16 | Mobile-first CSS pass | 2 | 2 | 4 | 3 | 1 | 0 | 1–2 |
| 17 | Consolidate overlapping audit reports | 2 | 2 | 4 | 3 | 2 | 0 | 0 |
| 18 | Delete/document 12 dead components | 1 | 2 | 5 | 5 | 1 | 0 | 0–1 |
| 19 | Convert top one-off tests to reusable suites | 2 | 1 | 3 | 2 | 2 | 0 | 1–2 |
| 20 | Multi-age schema design | 4 | 1 | 2 | 2 | 3 | 0 | 8 |

*Item 13's "user evidence" score is 5 by definition — it IS the pilot evidence.

---

## 28. WHAT NOT TO BUILD (with reconsideration thresholds)

| Feature | Evidence threshold to reconsider |
|---|---|
| Social network / messaging | Multiple pilot coaches independently request coach-to-coach contact, unprompted |
| CRM / club management | A real club (not individual coach) requests it post-beta |
| Player accounts / tracking | Never, unless a specific legal/privacy design is separately resourced and a clear product need is validated |
| Rankings / gamification | Not compatible with stated pedagogy (no Coach Score, historically rejected) — would need a full philosophy reversal, not just evidence |
| Complex analytics | Public Beta begins and direct pilot observation is no longer sufficient |
| Payments / marketplace | Approaching Public Launch with a validated monetizable unit of value |
| Video-analysis platform | Content pillars (case studies/scripts/plans) are already populated and coaches specifically request video over static diagrams |
| AI-generated coaching advice | Only if it can be held to the same evidence-boundary discipline as current exercises — very high bar, likely not soon |
| Broad 4–18 content authoring | Phase 9 (single adjacent age band) succeeds first |

---

## 29. STOP / GO CONDITIONS

- **If real coaches repeatedly fail to understand ManualFC despite UX fixes:** do NOT add more content — fix comprehension/UX first (explicit rule from brief).
- **If coaches use Decision Engine heavily but rarely read methodology chapters:** treat this as real signal to invest more in Decision Engine content and less in narrative volume expansion — do not assume the reverse.
- **If offline usage proves irrelevant to actual pilot coaches:** reassess its strategic priority — do not keep investing by default (though current evidence suggests it's valuable by design, this is unmeasured — **needs validation**).
- **If Phase 2 pilot shows <2 coaches return independently:** STOP — do not advance to Phase 4/5; return to Phase 1/UX fixes instead.

---

## 30. DEFINITIONS OF READY

**Private Pilot ready:** Gate A passed (Phase 0 exit conditions). *(Condition-based — realistically achievable once TASK-3709 auth is resolved and the nav/dependency fixes land; no calendar estimate given.)*

**Public Beta ready:** Gate E — all Phase 6 entry conditions met (P0 gone, remote exists, CI a11y/browser gate real, nav stable, two themes complete, real repeat coach usage observed, offline proven in use, mobile performance acceptable, SEO fundamentals present, no major a11y blocker). **Not** defined by page/task count.

**Public Launch ready:** Public Beta has run long enough to show stable/growing retention and manageable support load (Stage 3 in §19), with no unresolved CRITICAL/HIGH items in the risk register (§26).

**Multi-age ready:** Phase 7 (Public Beta) usage data shows real coach demand for a specific adjacent age band, AND Phase 8 schema redesign is complete and validated (Gate F) — not before either condition.

---

## 31. NEXT 5 TASKS (exact order)

1. **TASK-3712** — Fix `/gold-standard/rapid`→`/rezolva-pe-teren` navigation mis-route (header + footer + any internal links); verify via the same real-browser check pattern used throughout this project.
2. **TASK-3713** — Declare `playwright` and `@axe-core/playwright` as real devDependencies; verify a clean `npm install` matches what the audit scripts actually require.
3. **TASK-3714** — Resume/complete TASK-3709 (remote backup + fresh-clone recovery proof) once GitHub authentication is available.
4. **TASK-3715** — Add `site:` to `astro.config.mjs`, generate `sitemap.xml`/`robots.txt`, verify build.
5. **TASK-3716** — Wire one automated browser+axe smoke script into a repeatable local/CI command (does not require solving full CI infrastructure — a single reliable script satisfies Phase 0's exit condition).

---

## 32. FINAL EXECUTIVE RECOMMENDATION

Close Phase 0 this week — all five items above are cheap and mechanical. Then spend the next 60–90 days doing exactly one thing well: **add exercises and sessions to the one theme that already works, and get it in front of real coaches.** Do not start a second theme, a new content pillar, or any multi-age work until pilot behavior — not internal judgment — says so. The product's core risk right now is not technical; it's that almost nobody outside this project has used it yet.

---

# MANUALFC CANONICAL ROADMAP

**Current phase:**
Phase 0 — Stabilize the Baseline

**Current gate:**
Gate A (not yet passed)

**Next milestone:**
Gate A pass → begin Phase 1 content depth work

**Top 3 priorities:**
1. Fix the `/gold-standard/rapid` navigation mis-route
2. Complete the blocked Git remote backup (TASK-3709)
3. Declare Playwright/axe as real dependencies

**Top current blocker:**
TASK-3709 remote authentication — externally blocked, pending user-supplied working GitHub credentials

**What we explicitly will NOT build now:**
Social network, messaging, CRM, player accounts/tracking, rankings/gamification, complex analytics, payments/marketplace, video-analysis platform, AI-generated coaching advice, club management, broad 4–18 content authoring

**Next 5 execution tasks:**
1. TASK-3712 — Fix navigation mis-route
2. TASK-3713 — Declare Playwright/axe dependencies
3. TASK-3714 — Complete remote backup + fresh-clone recovery proof
4. TASK-3715 — Add site config + sitemap/robots
5. TASK-3716 — Wire automated browser+axe smoke check

**Earliest justified Private Pilot:**
Once Gate A passes — condition-based (Phase 0 exit), not calendar-based.

**Earliest justified Public Beta:**
Once Gate E passes — requires two complete themes, real repeat coach usage, and all Phase 6 entry conditions. Not before real pilot evidence exists.

**Multi-age expansion starts only when:**
Phase 7 (Public Beta) usage data shows real, specific coach demand for an adjacent age band, AND the Phase 8 schema redesign (not a find-replace) is complete and validated.

**The single most important outcome for the next 90 days:**
Real, repeated, independent use of ManualFC by at least two coaches who were not walked through it by the product owner.
