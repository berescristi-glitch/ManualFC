# ManualFC — Wave-4 Browser Acceptance Audit (TASK-2806)

## Scope

Full-product integration audit for PHASE-28/WAVE-4: does ManualFC work as one coherent product across TASK-2801–2805, not six disconnected feature demos? This is the local half of the required acceptance — the deployed-Preview half is blocked (see "Preview deployment" below) and this document says so honestly rather than substituting local results for it.

## Repository state

- `INITIAL_HEAD` / `SOURCE_RUNTIME`: `d7474ded9cf785e9fb866f771991c31d13568493` (TASK-2805 runtime commit)
- Branch: `main`, working tree clean at start, all Wave-4 task commits confirmed ancestors of HEAD.
- Baselines recovered from `PROJECT_STATUS.md`/`DECISIONS.md`: WAVE1=`15694b0`, WAVE2=`eccec0b`, WAVE2_FINAL=`ba78399`, WAVE3=`ae04ed5`, WAVE3_FINAL=`bc2f676` (current Production, `dpl_GwmVnMkeBy7aMnAAQzBNgEFHYRv6`, `manualfc.vercel.app`). None altered.

## Pre-flight product integrity

Single coherent domain model confirmed: `CoachState` (`app/src/lib/coach-state.ts`) — one `version: 1`, one `localStorage` key (`manualfc.coach-state.v1`), one `sanitizeState()` covering `saved`/`favorites`/`recents`/`sessions`/`reflections`/`offlinePacks` together. No parallel adapter, no direct `localStorage`/`Cache Storage` access found outside the two designated ports (`CoachStatePort` for user state, `sw.js`/Cache Storage for static bytes). Canonical content boundary holds: Workspace/Reflection/OfflinePack store only stable IDs, short titles/hrefs, and coach-entered configuration — never canonical pedagogical prose.

## Real defects found through end-to-end integration testing (not visible from isolated feature tests)

Two genuine issues were found by walking the full signature journey in a real browser — neither was catchable by TASK-2802–2805's own isolated acceptance, since each only exercised its own surface.

1. **Decision Engine → Workspace context loss.** A coach following `?problema=PRB-0003&sursa=decision-engine` from the Decision Engine into an exercise page, then using the quick "+ Ședință" action, got a session with **no** `problemId` — the exercise/problem pages are fully static-prerendered (`getStaticPaths`), so `Astro.url.searchParams` is never available server-side, and `CoachActions.astro` never read the query string client-side either. Fixed: `CoachActionsElement` now reads `problema` from `location.search` and sets it on session creation (or fills a still-empty `problemId` on the active session), without ever overwriting a problem the coach already chose explicitly in the builder. Verified live: builder's "Problema urmărită" dropdown now correctly pre-selects the originating problem.
2. **New touch-target violation in TASK-2805's own addition.** Live `getBoundingClientRect()` measurement (not CSS reading) on the session builder at 390px found the "Adaugă ședință" button (added in TASK-2805 for canonical-session linking) rendering at **19px** height — the shared `min-height:44px` rule was never extended to cover it. Fixed and re-measured: 44px.

Both are covered by new regression tests in `tests/test_task2806_integration.py`.

## Signature journey — verified live, local `astro preview` server

Fresh browser state throughout (localStorage + Cache Storage + Service Worker cleared before each major leg).

- **New coach**: homepage (no Workspace clutter, clear two-path framing) → `/rezolva-pe-teren` (Decision Engine, 8 observations, filters) → flagship problem PRB-0003 (before/after diagram + animated loop + coach-explainer script disclosure, all reached via real navigation) → EX-0003 exercise page → "+ Ședință" → Workspace session created with `problemId` correctly set (post-fix). 0 console errors at every step.
- **Group configuration**: tested both required configurations — 12 players/1 coach (EX-0003-only session) and 16 players/2 coaches (session rebuilt with the canonical `SES-0001` linked via the "Adaugă ședință canonică" selector); also verified `/gold-standard/configurator?exercitiu=EX-0003&copii=16&antrenori=2` directly, 0 errors.
- **60 vs 75 minutes**: both Field Mode variants run end-to-end from the *same* single cached HTML document (`ignoreSearch` cache match) — confirmed the two variants render genuinely distinct segment timing (`0′–12′` vs `0′–9′`, `55′–65′` vs `53′–60′`), not a cosmetic difference, both fully offline.
- **Prepare for field → online→offline → cold-adjacent flow**: "Disponibil pe teren" → `READY` status confirmed in `CoachState` and all required routes + hashed assets confirmed in `Cache Storage` → network disabled → Surface Map (`/gold-standard/sedinte/SES-0001`) re-renders deterministically offline (player-count radio change offline recomputes groups live) → Field Mode (both durations) with working timer and 6-segment navigation → "Termină ședința → Reflecție".
- **Reflection scenario 1** (from TASK-2805, same runtime, re-confirmed still valid): `CONSISTENT_IN_TASK` + `TRANSFER_UNCONFIRMED`, saved offline. **Reflection scenario 2** (fresh in this task): `CONSISTENT_IN_TASK` + `TRANSFER_SEEN` — next-action text read "Crește dificultatea sau verifică transferul într-un context diferit," honest and non-overclaiming (no percentages, no "validated improvement" language).
- **Offline reflection persistence**: reloaded the specific reflection by ID while still offline — both radio states correctly pre-populated, 0 loss.
- **Returning coach**: reload of `/spatiul-meu/` still offline — Continue correctly prioritized the active unfinished session over the just-completed reflection and over "Vizitate recent," exactly matching the documented priority order (active session → unreflected session → latest reflection → recent).
- **Mixed Wave-4 corrupted state** (new for this task — TASK-2802/2803 tested corruption before `offlinePacks` existed): injected a single state object with a valid session + a session with garbage types (`duration:999`, `players:-5`, `items:"not-an-array"`, `title:12345`), a valid reflection + a reflection with invalid enum values (dropped entirely by the sanitizer, not rendered with a garbage label), an orphan reflection (pointing at a session ID that doesn't exist — rendered fine, since a reflection is a valid historical record independent of whether its originating session still exists), an offline pack pointing at a removed session (silently inert — never surfaces in any UI list, since packs are looked up *by* session, not enumerated independently), a malformed offline pack (`contentVersion:42`, `status:"SOME_MADE_UP_STATUS"`, `canonicalRefs` with a bogus kind), an unresolvable `activeSessionId`, and `favorites: null`. Result: **0 console errors, 0 crashes**, every malformed field either coerced to a safe default or the whole entry dropped, Continue correctly cascaded past the unresolvable `activeSessionId` to the next valid priority. One minor, non-blocking gap found: `saved` entries are rendered without verifying the referenced canonical ID still exists in the current content graph, so a stale saved reference (only reachable if canonical content were later removed, which has not happened across this project's history) would render a dead link rather than being filtered — documented as a Minor limitation, not repaired, since building live-catalog validation for saved/favorite/recent lists is disproportionate scope for a single latent, low-probability edge case.

## Cross-cutting checks

- **Search regression**: `/cauta` with query "pasa" → 14 results spanning Problem/Principle/Exercise/Session/Assessment, 0 errors. No Wave-4 regression.
- **Homepage / IA**: unchanged from Wave-3, still clearly frames the two entry paths ("Vreau să învăț" / "Rezolvă pe teren") for a new visitor with no Workspace widget clutter; returning-coach continuity lives entirely inside `/spatiul-meu`, not on the public homepage — no IA correction needed.
- **Responsive**: 390/768/1280 checked for horizontal overflow on `/spatiul-meu` and the session builder (the two pages most changed this wave) — 0 overflow at any width.
- **Touch targets**: live-measured (not CSS-read) on every interactive Wave-4 control; one real violation found and fixed (see above), all others already at 44px.
- **Landmarks**: repository-wide, 87/87 documents, `main=1`/`nested_main=0`.

## Automated validation

- `python -m unittest discover -s tests`: **505/505 PASS** (501 from TASK-2805 + 4 new integration tests in `test_task2806_integration.py`).
- `python scripts/validate_content.py --strict`: PASS, 0/0/0.
- `python scripts/validate_project.py`: PASS, 0/0.
- `python scripts/generate_task_registry.py --check`: PASS, 228 tasks reproducible.
- `npm run check`: PASS, 89 files, 0/0/0.
- `npm run build`: PASS, 87 pages.
- `python scripts/validate_html_landmarks.py --dist dist/web`: PASS, 87/87, `main=1`/`nested=0`.
- `git diff --check`: PASS.

## Preview deployment — initially BLOCKED, resolved by the user

Section 60 requires deploying the accepted local candidate to an isolated Vercel Preview and independently re-auditing the *deployed* runtime before Wave-4 can be declared PASS. This was initially blocked: no Vercel CLI installed, and the Vercel MCP connector available in-session, while authenticated, had no access to the `manualfc` project (`get_project` → `404`) — the same blocker recorded historically for `TASK-2717`. The user resolved it by authenticating the Vercel CLI locally (`npx vercel`, account `berescristi-8889`), confirmed to have real access to the correct project (`vercel project ls` lists `manualfc` under team `berescristi-8889s-projects`).

## Isolated deployment

A clean git worktree was created pinned exactly to the candidate commit (`git worktree add ... 560e27c7f6c81e841affe0ff7b072ba91d872c91`), verified `git status --short` empty and `git rev-parse HEAD` exactly matching before deploying. `.vercel/project.json` was copied in unchanged (same `projectId`/`orgId` already linked locally — no identity mismatch, no relink needed). Deployed with `vercel deploy` (no `--prod` flag):

- `WAVE4_PREVIEW_COMMIT`: `560e27c7f6c81e841affe0ff7b072ba91d872c91`
- `WAVE4_PREVIEW_DEPLOYMENT`: `dpl_He9tPBT7SG77WqwBhoR6W3yAbeVX`
- `WAVE4_PREVIEW_URL`: `https://manualfc-ea7ifgvc8-berescristi-8889s-projects.vercel.app`
- `target: null` (Preview, confirmed via `vercel inspect` → `target preview`) — Production untouched.
- `X-Robots-Tag: noindex` confirmed present on the response.

## Runtime identity verification

Not assumed — proven by content hash. The deployed `astro-assets-manifest.json` lists `CoachActions.astro_astro_type_script_index_0_lang.CfvghWJB.js`, a **different** content hash from the pre-fix bundle (`...1vAmKmJ9.js`) seen in the TASK-2805 runtime. Since Astro hashes are content-addressed, this is direct proof the deployed bundle contains the TASK-2806 `problemIdFromContext()` fix, not an older runtime. `sedinta.astro`'s script bundle hash (`BkRg7Yrg`) is correctly unchanged, matching that its TASK-2806 fix was CSS-only.

## Preview access for automated testing

The Preview was protected by Vercel Authentication (SSO), confirmed via a `302` redirect to `vercel.com/sso-api` on an unauthenticated request. Per spec section 7, global protection was **not** disabled. Instead, "Protection Bypass for Automation" was enabled additively (`vercel project protection enable manualfc --protection-bypass`), generating a bypass secret used only as a `?x-vercel-protection-bypass=...&x-vercel-set-bypass-cookie=true` parameter on the first Playwright navigation (the resulting cookie then covers all subsequent same-context navigations). The secret itself is not reproduced in this report.

## Independent live browser audit (deployed Preview, not localhost)

Fresh browser state (localStorage cleared, real Playwright interaction against the live HTTPS URL):

- **Service worker on real infrastructure**: `navigator.serviceWorker.controller` present, registration `activated`, scope correctly the deployed origin. `manualfc-shell-v1` cache verified to contain all 13 hashed assets plus the app shell — identical precache behavior to localhost, confirmed live rather than assumed.
- **Problem-context regression (the TASK-2806 fix)**: navigated to `EX-0003?problema=PRB-0003&sursa=decision-engine` on the live Preview, clicked "+ Ședință" — `sessions[0].problemId === "PRB-0003"` confirmed in live `localStorage`. The exact defect this task fixed is proven fixed on the actual deployed runtime, not just locally.
- **16 players / 2 coaches**, session linked to canonical `SES-0001`, saved live.
- **Offline preparation**: "Disponibil pe teren" → pack `status: "READY"` confirmed in live state.
- **Genuine cold offline start on deployed infrastructure**: closed the tab, opened a brand-new tab (no prior in-memory state), set the browser context offline, navigated directly to `.../mod-teren?durata=75` on the live HTTPS Preview — loaded cleanly, **0 console errors**. This is the strongest possible cold-start proof available: a real service worker, on real HTTPS infrastructure, serving a route from disk-persisted Cache Storage with zero warm in-memory illusion.
- **Field Mode**: timer started and progressed, all 6 segments navigated, "Termină ședința → Reflecție" reached, still fully offline.
- **Offline Reflection**: `CONSISTENT_IN_TASK` + `TRANSFER_UNCONFIRMED` recorded and saved while offline on the live deployment; reloaded `/spatiul-meu/` still offline — reflection, session, and offline badge all persisted with **zero data loss**, confirmed by reading live `localStorage` after reload.
- **Back online**: Search (`/cauta`) returned results with 0 console errors; landmark check (`document.querySelectorAll('main').length === 1`) confirmed on the live deployment; touch targets re-measured live at 390px (`[data-add-session]` and `[data-add]` both exactly 44px) and no horizontal overflow at 390px or 1440px; reduced-motion emulation on `EX-0001` loaded cleanly with 0 errors.

No Critical or Major finding surfaced on the live deployment. No repair was required beyond what was already committed in the candidate.

## Verdict

`TASK-2806 = DONE`. `PHASE-28 / WAVE-4 = PASS`. `MANUALFC_PREMIUM_WAVE4_BASELINE = 560e27c7f6c81e841affe0ff7b072ba91d872c91` — the exact commit deployed and independently audited live, proven via content-hash runtime identity, not merely declared. Production remains fully unchanged (`bc2f676`, `dpl_GwmVnMkeBy7aMnAAQzBNgEFHYRv6`); Wave-4 was never promoted there and no such promotion was authorized.
