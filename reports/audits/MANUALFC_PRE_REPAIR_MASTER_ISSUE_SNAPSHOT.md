# ManualFC — Pre-Repair Master Issue Snapshot

**FROZEN:** 2026-08-31, după Stage 1–3. Acest document nu se rescrie în repair; dispozițiile evoluează numai în registrul viu.

## Număr inițial

| Severitate | Număr | IDs |
|---|---:|---|
| CRITICAL | 1 | INT-0007 |
| MAJOR | 2 | INT-0001, INT-0004 |
| MODERATE | 3 | INT-0002, INT-0005, INT-0006 |
| MINOR | 1 | INT-0003 |

## Categorii

| Categorie | Număr |
|---|---:|
| SEMANTIC/EVIDENCE | 1 |
| DATA/SAFEGUARDING | 1 |
| BUILD/TEST/VALIDATION | 4 |
| WORKTREE HYGIENE | 1 |
| UX/ACCESSIBILITY/OFFLINE/STATE | NOT_FULLY_AUDITED_PRE_REPAIR |

## Freeze statement

Snapshot-ul consemnează adevărul pre-repair chiar dacă reparațiile ulterioare închid toate problemele. Niciun PASS istoric nu este rescris: remedierea fabricației din 2026-08-11 este clasificată `PARTIALLY_INVALID` în starea curentă, deoarece PRB-0008 păstrează două claim-uri retrase.
