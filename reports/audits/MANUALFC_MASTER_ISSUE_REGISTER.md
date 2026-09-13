# ManualFC — Master Issue Register

Registru viu început la 2026-08-31. Snapshot-ul pre-repair va rămâne separat și imuabil.

## INT-0001 — Instalarea locală Node este coruptă și blochează build-ul

- STAGE_FOUND: STAGE 1
- SEVERITY: MAJOR
- CATEGORY: BUILD / DEPENDENCY INTEGRITY
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: întregul runtime
- AFFECTED_FILES: `node_modules/**`
- AFFECTED_ROUTES: toate
- USER_IMPACT: candidatul nu poate fi construit sau servit local din sursă
- COACHING_IMPACT: journeys și Field Mode nu pot fi retestate
- DATA_RISK: LOW
- EVIDENCE_RISK: MEDIUM — claim-urile istorice PASS nu pot fi reconfirmate în starea curentă
- PRIVACY_RISK: NONE OBSERVED
- SAFEGUARDING_RISK: NONE OBSERVED
- ROOT_CAUSE: directoare din `node_modules` raportate de Windows ca ilizibile; importul Astro eșuează înainte de compilarea sursei
- REPRODUCTION_STEPS: `npm.cmd run check`; `npm.cmd run build`
- EXPECTED: Astro check/build cu exit 0
- ACTUAL: `SyntaxError: Unexpected token '|'`
- EVIDENCE: output terminal 2026-08-31; enumerarea a raportat `node_modules/.../syntax/node` și `node_modules/zod/v4/locales` corupte/ilizibile
- FIX_COMPLEXITY: S
- FIX_DEPENDENCIES: snapshot pre-repair înghețat
- REGRESSION_RISK: LOW dacă se folosește `npm ci` cu lockfile verificat
- STATUS: ROOT_CAUSE_CONFIRMED

## Resolution ledger — 2026-08-31

| ID | Severitate | Stare finală | Dovadă |
|---|---|---|---|
| INT-0001 | MAJOR | FIXED / RETEST_PASS | instalare refăcută; Astro check/build PASS |
| INT-0002 | MODERATE | FIXED / RETEST_PASS | test Node real pe 101 pagini |
| INT-0003 | MINOR | DEFERRED_OWNERSHIP | artefacte preexistente păstrate |
| INT-0004 | MAJOR | FIXED / RETEST_PASS | safeguarding validator PASS; contact neverificabil eliminat |
| INT-0005 | MODERATE | FIXED / RETEST_PASS | stdout UTF-8; 101 landmarks PASS |
| INT-0006 | MODERATE | DEFERRED_WITH_JUSTIFICATION | candidat valid; staging/swap înainte de scalare |
| INT-0007 | CRITICAL | FIXED / RETEST_PASS | claim-uri active + validator fail-closed + test |
| INT-0008 | MAJOR | FIXED / RETEST_PASS | Field Mode: un H1 în 4 viewport-uri |
| INT-0009 | MAJOR | FIXED / RETEST_PASS | homepage Axe zero după contrast fix |

Problemele `INT-0008` și `INT-0009` au fost descoperite după snapshot, la reluarea Stage 2; snapshot-ul nu a fost rescris.

## INT-0002 — Scriptul Node de testare trece fără să ruleze teste

- STAGE_FOUND: STAGE 1
- SEVERITY: MODERATE
- CATEGORY: TEST INTEGRITY
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: suita web Node
- AFFECTED_FILES: `package.json`, `tests/web/`
- AFFECTED_ROUTES: toate fluxurile web
- USER_IMPACT: falsă încredere în regresia web
- COACHING_IMPACT: fluxurile practice pot regresa fără detecție
- DATA_RISK: LOW
- EVIDENCE_RISK: HIGH pentru claim-ul „testele Node trec”
- PRIVACY_RISK: NONE OBSERVED
- SAFEGUARDING_RISK: NONE OBSERVED
- ROOT_CAUSE: globul `tests/web/*.test.js` nu selectează teste existente
- REPRODUCTION_STEPS: `npm.cmd test`
- EXPECTED: cel puțin o suită/test executat
- ACTUAL: `tests 0`, `suites 0`, exit 0
- FIX_COMPLEXITY: M
- FIX_DEPENDENCIES: inventar testelor și definirea acoperirii minime
- REGRESSION_RISK: LOW
- STATUS: REPRODUCED

## INT-0003 — Artefacte temporare anormale și cache pytest nefuncțional în worktree

- STAGE_FOUND: STAGE 1
- SEVERITY: MINOR
- CATEGORY: WORKTREE HYGIENE / ENVIRONMENT
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: audit și dezvoltare locală
- AFFECTED_FILES: `.pytest_cache/`, `!x.complete`, `!x.hidden).length`, `x.naturalWidth).join()` și capturi neversionate
- AFFECTED_ROUTES: none direct
- USER_IMPACT: zgomot forensically relevant și risc de confundare a dovezilor
- COACHING_IMPACT: none direct
- DATA_RISK: LOW
- EVIDENCE_RISK: MODERATE
- PRIVACY_RISK: UNKNOWN până la inspectarea artefactelor
- SAFEGUARDING_RISK: UNKNOWN până la inspectarea artefactelor
- ROOT_CAUSE: artefacte preexistente ale automatizărilor; ownership necunoscut
- REPRODUCTION_STEPS: `git status --short`; `pytest -q`
- EXPECTED: worktree controlat și cache funcțional
- ACTUAL: numeroase artefacte; PytestCacheWarning
- FIX_COMPLEXITY: S
- FIX_DEPENDENCIES: decizie explicită de ownership; nu se șterg automat
- REGRESSION_RISK: LOW
- STATUS: OPEN

## INT-0004 — Contactele canonice de safeguarding au reverificarea expirată

- STAGE_FOUND: STAGE 1
- SEVERITY: MAJOR
- CATEGORY: SAFEGUARDING / FRESHNESS
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: toate paginile și resursele care expun contactele de escaladare
- AFFECTED_FILES: `data/safeguarding/canonical.json`
- AFFECTED_ROUTES: safeguarding și resurse derivate
- USER_IMPACT: antrenorul poate primi date operaționale care nu mai au freshness validat
- COACHING_IMPACT: risc de întârziere sau canal greșit la o îngrijorare despre copil
- DATA_RISK: HIGH
- EVIDENCE_RISK: HIGH
- PRIVACY_RISK: MODERATE
- SAFEGUARDING_RISK: HIGH
- ROOT_CAUSE: toate cele cinci intrări au `recheck_at: 2026-08-15`, anterior datei auditului 2026-08-31
- REPRODUCTION_STEPS: `python scripts/validate_safeguarding.py`
- EXPECTED: exit 0, contacte în fereastra de reverificare
- ACTUAL: cinci erori `CONTACT_RECHECK_OVERDUE`
- FIX_COMPLEXITY: M
- FIX_DEPENDENCIES: reverificare din surse instituționale; internetul de audit nu a returnat conținut, deci valorile nu se actualizează prin presupunere
- REGRESSION_RISK: LOW
- STATUS: ROOT_CAUSE_CONFIRMED

## INT-0005 — Validatorul landmark nu își poate raporta eroarea pe consola Windows

- STAGE_FOUND: STAGE 1
- SEVERITY: MODERATE
- CATEGORY: VALIDATION RELIABILITY
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: gate-ul `main=1`
- AFFECTED_FILES: `scripts/validate_html_landmarks.py`
- AFFECTED_ROUTES: toate rutele construite
- USER_IMPACT: defectele de landmark pot fi mascate de crash-ul reporterului
- COACHING_IMPACT: none direct
- DATA_RISK: LOW
- EVIDENCE_RISK: HIGH
- ROOT_CAUSE: scriptul nu configurează stdout UTF-8; mesajul românesc produce `UnicodeEncodeError` în CP1252
- REPRODUCTION_STEPS: `python scripts/validate_html_landmarks.py --dist dist`
- EXPECTED: listă de erori și exit 1
- ACTUAL: traceback înaintea listei complete
- FIX_COMPLEXITY: S
- FIX_DEPENDENCIES: none după freeze
- REGRESSION_RISK: LOW
- STATUS: ROOT_CAUSE_CONFIRMED

## INT-0006 — Build-ul șterge candidatul anterior înainte de a dovedi că noul build reușește

- STAGE_FOUND: STAGE 1
- SEVERITY: MODERATE
- CATEGORY: BUILD ATOMICITY
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: `dist/`
- AFFECTED_FILES: `package.json`, `scripts/clean_web_build.mjs`
- AFFECTED_ROUTES: toate
- USER_IMPACT: un eșec de compilare lasă zero runtime local disponibil
- COACHING_IMPACT: Field Mode/offline nu mai pot fi folosite din artefactul local anterior
- DATA_RISK: LOW
- EVIDENCE_RISK: MODERATE
- ROOT_CAUSE: curățarea `dist` precedă compilarea și nu există build temporar + swap atomic
- REPRODUCTION_STEPS: pornește cu un `dist` valid și provoacă un eșec Astro; rulează `npm run build`
- EXPECTED: candidatul anterior rămâne până când noul build este complet
- ACTUAL: `dist` rămâne doar cu README
- FIX_COMPLEXITY: M
- FIX_DEPENDENCIES: repair build environment
- REGRESSION_RISK: MODERATE
- STATUS: ROOT_CAUSE_CONFIRMED

## INT-0007 — O problemă publicată citează claim-uri retrase bazate pe surse fabricate

- STAGE_FOUND: STAGE 3
- SEVERITY: CRITICAL
- CATEGORY: EVIDENCE INTEGRITY / HISTORICAL PASS REGRESSION
- CONFIDENCE: HIGH
- REPRODUCIBLE: YES
- AFFECTED_SURFACES: Problem Library, Decision Engine, PRB-0008 și orice traseu downstream
- AFFECTED_FILES: `data/problems/problem-library.json`, `research/claims.json`, `research/sources.json`, validatorul de conținut
- AFFECTED_ROUTES: problema `evita-repetat-sa-primeasca-sub-presiune` și traseele asociate
- USER_IMPACT: produsul prezintă ca fundamentare ID-uri pe care propriul registru le interzice în conținut public
- COACHING_IMPACT: o intervenție pedagogică sensibilă este ancorată într-un lanț de dovadă retras
- DATA_RISK: HIGH
- EVIDENCE_RISK: CRITICAL
- PRIVACY_RISK: MODERATE
- SAFEGUARDING_RISK: HIGH
- ROOT_CAUSE: `PRB-0008.evidence_claim_ids` păstrează `CLM-0055` și `CLM-0056`; ambele au `status: REPLACED`, `confidence: UNRESOLVED`, surse `withdrawn: true` și note explicite de fabricație. Validatorul verifică numai existența ID-ului, nu eligibilitatea statusului.
- REPRODUCTION_STEPS: inspectează `PRB-0008.evidence_claim_ids`, apoi claim-urile și `SRC-0054`/`SRC-0055`; rulează validatorul strict și observă falsul PASS
- EXPECTED: numai claim-uri active/verificate pot susține obiecte `PUBLISHED`
- ACTUAL: claim-uri retrase sunt acceptate; `practical_implication` spune explicit „Nu mai este folosit în conținutul publicat”, contrazis de PRB-0008
- FIX_COMPLEXITY: M
- FIX_DEPENDENCIES: maparea canonică spre `CLM-0073`, `CLM-0079` și claim-urile active relevante; validator fail-closed pentru status/source withdrawal
- REGRESSION_RISK: MODERATE
- STATUS: ROOT_CAUSE_CONFIRMED
