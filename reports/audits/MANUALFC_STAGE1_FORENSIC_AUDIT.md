# ManualFC — Stage 1 Forensic Audit

## Stare

`COMPLETE_WITH_FINDINGS` — toate căile read-only disponibile au fost executate. Route crawl dintr-un build proaspăt și deployment parity sunt limitări explicite, mutate la retest după repair.

## Guvernanță

- INITIAL_HEAD: `0466ea9b684eff787cd2caea7ee5c76bf01cfbf2`
- LATEST_RUNTIME_BASELINE: `1404fb980505c9f3d2751dc44827dbe13c5fa1a9`
- LATEST_AUDIT_COMMIT: `0466ea9b684eff787cd2caea7ee5c76bf01cfbf2`
- WORKTREE_STATUS: dirty, numai artefacte neversionate preexistente la preflight

## Dovezi

- 98 JSON versionate parsează cu Python; zero invalid.
- 895 fișiere text versionate sunt UTF-8 valide.
- zero fișiere versionate de 0 bytes.
- registrele critice coincid cu Git index.
- `validate_project.py`, `validate_content.py --strict`, `validate_gold_standard_v2.py`, registry reproducibility: PASS.
- pytest: 505 passed + 25 subtests, un warning de cache.
- Node test: exit 0, dar 0 teste — INT-0002.
- Astro check și build: FAIL — INT-0001.
- safeguarding validator: FAIL, cinci contacte overdue — INT-0004.
- landmark validator: reporter crash pe Windows și zero HTML după build-ul eșuat — INT-0005/INT-0006.
- regression forensics: remedierea istorică a surselor fabricate este parțial invalidată de utilizarea live din PRB-0008 — INT-0007.

## Limită curentă

Nu se acordă PASS și nu se reconfirmă claim-uri istorice browser/deployment înainte de rebuild și retest. `CROSS_BROWSER_NOT_FULLY_RUN` și deployment parity rămân explicite.
