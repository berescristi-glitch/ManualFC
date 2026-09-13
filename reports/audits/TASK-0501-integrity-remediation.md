# Raport corectiv forward-only — TASK-0501 integrity remediation

**Data:** 2026-08-09  
**Commit inițial păstrat:** `69b62d055d873e6ef1abb5850caf92765d977a7a`  
**Statut evidence integrity:** PASS

## Natura corecției

Raportul inițial TASK-0501 a declarat greșit chain-ul și fidelitatea produsului drept validate. Acest raport nu rescrie acel eveniment. Documentează corecția ulterioară: citări lipsă, metadata incompletă, o sursă cu metadata eronată, claims supra-formulate și evidence hard-coded în pagină.

## Decizii claim-by-claim

- `CLM-0022`: `NARROW + DOWNGRADE` la `MODERATE / PARTIAL`; a fost eliminată valoarea nesusținută „±2–3 ani la U11”.
- `CLM-0023`: `NARROW + DOWNGRADE` la `MODERATE / INDIRECT`; sursele susțin limitele clasificării cronologice și prudența față de ferestre fixe, nu superioritatea demonstrată a training age.
- `CLM-0024`: `NARROW + DOWNGRADE` la `LOW / INDIRECT`; ajustarea sarcinii este recomandare metodologică testată prin reobservare, nu efect experimental U11.
- `CLM-0025`: `NARROW + DOWNGRADE` la `MODERATE / PARTIAL`; sursa susține limitele evaluării maturizării și potențialului, iar interdicția etichetării psihologice rămâne protecție pedagogică explicită.

## Citări și surse

Au fost create `CIT-0024`–`CIT-0029`. `SRC-0024` a fost corectat de la o publicație și un DOI inexistente la capitolul real „A personal assets approach to youth sport”, Côté, Turnnidge și Vierimaa (2016). `SRC-0021` și `SRC-0022` sunt clasificate drept narrative reviews, nu systematic reviews.

## Produs și validare

`resolveEvidenceClaims()` leagă `principle.evidence_claim_ids` de claims, citations și sources și oprește build-ul dacă chain-ul sau metadata lipsesc. Ruta afișează separat „Ce știm”, „Ce înseamnă pentru antrenor” și „Ce NU putem concluziona”. HTML-ul static verificat conține `CLM-0022`, `CIT-0024`, `SRC-0021` și aplicabilitatea reală; nu conține `CLM-001`.

Validatorul canonic deține noile gate-uri: `CANONICAL_EVIDENCE_CHAIN_BROKEN`, `CANONICAL_EVIDENCE_METADATA_MISSING` și `CITATION_SOURCE_MISMATCH`. Testele negative demonstrează fiecare eșec.

`astro check`: PASS, 0 erori / 0 warnings / 0 hints.  
`astro build`: PASS, 9 pagini statice.  
`validate_content.py` normal și strict: PASS.  
`validate_project.py`, safeguarding, regulations, registry și `git diff --check`: PASS.  
Audit vizual în browser: NEEXECUTAT — runtime-ul sesiunii nu a expus niciun browser; HTML-ul a fost inspectat automat, dar această verificare nu este prezentată drept audit vizual.

## Protecția worktree-ului

Remedierea a fost construită într-un worktree curat. Draftul TASK-0502 existent în worktree-ul principal rămâne în afara commitului corectiv și nu a fost șters, stashed sau resetat.
