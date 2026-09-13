# PHASE-32 — Blueprint de autorizare pentru Antrenorul V1

**Versiune:** 1.0.0 · **Fază:** PHASE-30 Wave-3 · **Task de referință:** TASK-3031 · **Statut:** Architecture (blueprint, nu redactare)

Nu conține proză finală de lecție. 34 de domenii grupate într-o progresie coerentă de învățare, nu 34 de capitole de top nivel.

## Ordinea canonică a capitolelor

| Cap. | Titlu de lucru | Domenii | Întrebare centrală | Dosare/claim-uri sursă | Competențe legate |
|---|---|---|---|---|---|
| A1 | Identitatea antrenorului | COACH-D01 | Ce fel de adult sunt pentru acești copii? | `COACH_IDENTITY_AND_ROLE_R1.md` | (identitate, nu competență numerotată) |
| A2 | Observă | COACH-D02/D03 | Ce se întâmplă efectiv, înainte de interpretare? | Decision Engine (pre-existent) | COACH-C01 |
| A3 | Formulează problema | COACH-D04 | Cum transform o observație într-o problemă lucrabilă? | `problem-library.json` (pre-existent) | COACH-C02 |
| A4 | Decide dacă intervine | COACH-D05/D06 | Când vorbesc, când tac? | `COACH_INTERVENTION_R1.md` | COACH-C03 |
| A5 | Comunică | COACH-D07-D11 | Cum predau prin limbaj, nu doar prin conținut? | `QUESTIONING_GUIDED_DISCOVERY_R1.md`, `FEEDBACK_R1.md`, `ATTENTION_COGNITIVE_LOAD_R1.md`, `GENERAL_PEDAGOGICAL_COMMUNICATION_R1.md` | COACH-C04/C05/C06/C07 |
| A6 | Proiectează practica | COACH-D12-D16 | Cum construiesc un exercițiu care păstrează problema reală? | `SKILL_ACQUISITION_FRAMEWORKS_R1.md`, `YOUTH_SESSION_DESIGN_R1.md` | COACH-C08/C09/C12 |
| A7 | Organizează | COACH-D17-D21 | Cum organizez grupul/spațiul/timpul? | `COACHING_ORGANIZATION_AND_ACTIVE_TIME_R1.md` (D19/D20); D17/D18/D27 deja funcționale la produs | COACH-C10 |
| A8 | Predă jocul | COACH-D22-D24 | Cum predau percepția, decizia și tehnica legate de context? | `PERCEPTION_DECISION_ACTION_R1.md` | COACH-C11 |
| A9 | Verifică transferul | COACH-D25 | Comportamentul apare cu adevărat în joc liber? | `TRANSFER_RETENTION_R1.md` | COACH-C14 |
| A10 | Evaluează | COACH-D26 | Ce înseamnă „dovadă de învățare"? | `TRANSFER_RETENTION_R1.md` (reutilizat) | COACH-C15 |
| A11 | Planifică | COACH-D27/D28 | Cum leg o ședință de următoarele? | `YOUTH_SESSION_DESIGN_R1.md`, `YOUTH_MEDIUM_TERM_PLANNING_R1.md` | COACH-C16 |
| A12 | Diferențiază | COACH-D29 | Cum adaptez fără să separ permanent copiii? | `DIFFERENTIATION_AND_CHALLENGE_R1.md` | COACH-C13 |
| A13 | Climatul de grup | COACH-D30/D31 | Cum vorbesc către întregul grup, ce climat creez? | `ch-0301` (pre-existent), `MOTIVATION_AUTONOMY_R1.md` | — |
| A14 | Reflectă | COACH-D32/D33 | Ce am observat despre propria intervenție? | `COACH_REFLECTIVE_PRACTICE_R1.md`, `COACH_SELF_EVALUATION_R1.md` | COACH-C17 |
| A15 | Se dezvoltă | COACH-D34 | Cum îmi construiesc practica pe termen lung? | `COACH_PROFESSIONAL_DEVELOPMENT_R1.md` | COACH-C18 |

## Sub-lecții estimate

**15 capitole × ~3-4 sub-lecții = ~50-55 unități.** Capitolele A5-A8 (comunicare, proiectare, organizare, predarea jocului) sunt cele mai dense — probabil 5-6 sub-lecții fiecare, dat fiind volumul de dovadă acumulat (peste 60 de claim-uri combinate).

## Arhitectura de caz

Aceeași structură ca Pedagogul: `CONTEXT → OBSERVAȚIE → INTERPRETĂRI POSIBILE → LEGĂTURĂ CU DOVADA → DECIZIA ANTRENORULUI → LIMBAJ → RĂSPUNS ALTERNATIV → CE SĂ OBSERVE MAI DEPARTE → REFLECȚIE`.

## Banca de exemple reutilizabile (tipuri, nu conținut)

Conversație antrenor-copil · Incident de antrenament · Incident de meci · Conversație cu părinte · Conflict de grup · Răspuns la eroare · Moment de chestionare · Moment de feedback · Moment de „over-coaching" · Moment de diferențiere · Verificare de transfer.

## Harta de legături încrucișate (către Pedagogul V1)

Vezi `PHASE31_PEDAGOGUL_AUTHORING_BLUEPRINT.md` §Harta de legături — relația e simetrică.

## Straturi de profunzime

Identic cu Pedagogul: TEREN/ACUM · ÎNȚELEGE · APROFUNDEAZĂ · DOVEZI.

## Avertismente de dovadă

A1 (identitate) și A11 (planificare pe termen mediu) sunt cele mai noi domenii, cu evidență football-specifică cea mai subțire. A7 (organizare — poziționarea antrenorului) rămâne explicit `PRACTICE_HEURISTIC`, nu știință — de marcat clar în redactare, nu de prezentat ca regulă validată.

## Poartă de autorizare

Acest blueprint NU autorizează redactarea. Vezi `reports/audits/MANUALFC_PHASE30_WAVE3_RESEARCH_FOUNDATION_ACCEPTANCE.md` pentru verdictul final `ANTRENORUL_V1`.
