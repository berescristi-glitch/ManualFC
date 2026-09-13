# PHASE-31 — Blueprint de autorizare pentru Pedagogul V1

**Versiune:** 1.0.0 · **Fază:** PHASE-30 Wave-3 · **Task de referință:** TASK-3031 · **Statut:** Architecture (blueprint, nu redactare)

Nu conține proză finală de lecție. Definește structura, nu conținutul. Autorizarea redactării efective (PHASE-31) rămâne separată de acest blueprint.

## Ordinea canonică a capitolelor (derivată pentru înțelegerea cursantului, nu oglindă 1:1 a celor 12 domenii)

| Cap. | Titlu de lucru | Domeniu(i) | Întrebare centrală | Dosare/claim-uri sursă | Competențe legate |
|---|---|---|---|---|---|
| P1 | Copilul de 10-11 ani | PED-D01 | Cine e copilul pe care îl antrenez? | `CHILD_DEVELOPMENT_10_11_R1.md` | PED-C02, PED-C10 |
| P2 | Cum învață copilul | PED-D02 | Ce înseamnă „a învăța" la această vârstă? | `SKILL_ACQUISITION_FRAMEWORKS_R1.md`, `ATTENTION_COGNITIVE_LOAD_R1.md`, `TRANSFER_RETENTION_R1.md` | PED-C01, COACH-C14 |
| P3 | Ce îl motivează | PED-D03 | De ce joacă/rămâne/renunță un copil? | `MOTIVATION_AUTONOMY_R1.md` | PED-C07 |
| P4 | Emoțiile în joc | PED-D04 | Cum reacționează emoțional un copil de 10-11 ani? | `EMOTIONAL_DEVELOPMENT_AND_REGULATION_R1.md` | PED-C06 |
| P5 | Eroarea ca informație | PED-D05 | Ce înseamnă o greșeală? | `ch-0103-decision-error.md` (pre-existent) | PED-C06 |
| P6 | Relația pedagogică | PED-D07 | Cum mă apropii fără să pierd autoritatea, sau invers? | `PEDAGOGICAL_RELATIONSHIP_R1.md` | PED-C09 |
| P7 | Comunicarea | PED-D06 | Cum vorbesc astfel încât să fiu înțeles? | `GENERAL_PEDAGOGICAL_COMMUNICATION_R1.md` | PED-C03, PED-C04 |
| P8 | Grupul și apartenența | PED-D08 | Ce se întâmplă între copii, nu doar între mine și ei? | `GROUP_DYNAMICS_YOUTH_SPORT_R1.md` | PED-C11 |
| P9 | Diferențele individuale | PED-D11 | Cum adaptez fără să etichetez? | `INDIVIDUAL_DIFFERENCES_IN_YOUTH_COACHING_R1.md` | PED-C10 |
| P10 | Familia | PED-D10 | Ce rol au părinții, real, nu presupus? | `PARENTS_YOUTH_SPORT_R1.md` | PED-C12 |
| P11 | Reflecția copilului | PED-D12 | Cât de mult poate copilul reflecta singur? | `CHILD_METACOGNITION_AND_REFLECTION_R1.md` | PED-C13 |
| P12 | Siguranța copilului (graniță permanentă) | PED-D09 | Ce nu negociez niciodată? | `data/safeguarding/canonical.json` (pre-existent) | PED-C08 |

## Sub-lecții estimate (structural, nu conținut)

Fiecare capitol: 3-5 sub-lecții tematice (ex. P1 → dezvoltare cognitivă / emoțională / motrică / variabilitate). Estimat: **12 capitole × ~4 sub-lecții = ~48 unități**, nu 12 capitole monolitice.

## Arhitectura de caz (per capitol major)

`CONTEXT → OBSERVAȚIE → INTERPRETĂRI POSIBILE → LEGĂTURĂ CU DOVADA → DECIZIA ANTRENORULUI → LIMBAJ → RĂSPUNS ALTERNATIV → CE SĂ OBSERVE MAI DEPARTE → REFLECȚIE`. Niciun caz fictiv nu se prezintă ca dovadă de teren reală — marcat explicit ca ilustrativ.

## Straturi de profunzime (per capitol, per `CONTENT_DEPTH_STANDARD.md`)

TEREN/ACUM · ÎNȚELEGE · APROFUNDEAZĂ · DOVEZI — un singur obiect canonic, patru adâncimi de prezentare, nu patru articole separate.

## Harta de legături încrucișate (către Antrenorul V1)

| Capitol Pedagogul | Capitole Antrenorul conectate | Competențe partajate |
|---|---|---|
| P1 Copilul | A2 Observă, A8 Predă jocul | PED-C02↔COACH-C01 |
| P6 Relația | A1 Identitate | PED-C09↔COACH identitate |
| P7 Comunicarea | A5 Comunică | PED-C03/C04↔COACH-C04/C05 |
| P9 Diferențe individuale | A12 Diferențiază | PED-C10↔COACH-C13 |
| P11 Reflecția copilului | A14 Reflectă (antrenor) | PED-C13↔COACH-C17 (paralele, nu identice) |

## Avertismente de dovadă (de purtat în redactare)

Nicio sursă directă U11-fotbal simultan nu există pentru majoritatea capitolelor — excepții: P11 (2 surse), P3/P10 parțial (studii de fotbal 11-14 ani). Toate extrapolările rămân marcate `PARTIAL`/`INDIRECT` în claim-uri, nu ascunse în proza finală.

## Poartă de autorizare

Acest blueprint NU autorizează redactarea. Vezi `reports/audits/MANUALFC_PHASE30_WAVE3_RESEARCH_FOUNDATION_ACCEPTANCE.md` pentru verdictul final `PEDAGOGUL_V1`.
