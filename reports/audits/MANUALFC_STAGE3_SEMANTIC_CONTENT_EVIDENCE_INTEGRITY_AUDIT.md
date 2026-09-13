# ManualFC — Stage 3 Semantic, Content and Evidence Integrity Audit

## Stare

`COMPLETE_WITH_CRITICAL_FINDING`.

Validatoarele structurale și Gold Standard V2 trec pentru 5 exerciții și 2 ședințe, dar auditul adversarial a demonstrat că PASS-ul este incomplet: validatorul acceptă claim-uri `REPLACED` și surse `withdrawn` în obiecte `PUBLISHED`.

## Claim–source audit

- Registre: 380 claim-uri, 361 surse, 408 citări.
- `CLM-0055` și `CLM-0056` declară explicit că nu mai sunt folosite public și că sursele inițiale sunt fabricate/nepotrivite.
- `PRB-0008` le folosește încă în `evidence_claim_ids`; contradicție directă, INT-0007.
- Claim-urile active eșantionate pentru scanare/SSG declară populațiile și limitele U11; nu s-a transformat corelația în cauzalitate în obiectele eșantionate.

## Zece trasee semantice

Au fost inspectate ca relații SOURCE/CLAIM → KNOWLEDGE → COMPETENCY → PRACTICE → FIELD ACTION → OBSERVATION → TRANSFER → REFLECTION:

1. EX-0001: complet structural, boundary FIELD_INPUT_REQUIRED prezent.
2. EX-0002: complet structural, transferul sub opoziție activă nu este presupus.
3. EX-0003: limitele populațiilor U17–adult pentru scanare sunt declarate.
4. EX-0004: complet structural, alegerea dimensiunilor rămâne euristică.
5. EX-0005: complet până la testul de transfer; meciul oficial rămâne neconfirmat.
6. SES-0001: obiective copil/antrenor și reflection_v2 prezente; limita de trei concepte este practică ManualFC, nu prag științific.
7. SES-0002: separarea ședințelor este declarată alegere practică, nu interval optim dovedit.
8. PRB-0001: claim-uri de scanare cu limite U11 și transfer neconfirmat.
9. PRB-0003: quick test-ul nu este prezentat ca diagnostic.
10. PRB-0008: BROKEN — claim-uri retrase/fabricate în fundamentarea unui obiect publicat.

## Integritate pedagogică și safeguarding

Eșantionul păstrează percepție → decizie → execuție → rezultat, evită diagnosticul copilului și etichetele. Integritatea safeguarding este însă `FAIL` până la reverificarea contactelor și repararea INT-0007.

## Verdict Stage 3

`FAIL_PRE_REPAIR`: CRITICAL=1, MAJOR=cel puțin 2. HUMAN_LEARNING_VALIDATION=`NOT_YET_RUN`; PHASE-23=`FIELD_INPUT_REQUIRED`.
