# Matricea de acoperire prin cercetare — Antrenorul

**Versiune:** 1.0.0 · **Fază:** PHASE-30 · **Task de referință:** TASK-3010 · **Statut:** Research

Aceleași stări ca în matricea Pedagogul. Clusterele urmează gruparea deja existentă din `COACH_DOMAIN_MAP.md`.

| Domeniu | Stare | Sursă acoperire | Notă |
|---|---|---|---|
| **Cluster 1 — Identitate** | | | |
| COACH-D01 — Identitatea antrenorului | NOT_RESEARCHED | — | Nu a fost un cluster prioritar în Valul 1. |
| **Cluster 2 — Observație și formulare a problemei** | | | |
| COACH-D02 — Observație | EXISTING_EVIDENCE_REUSED | Decision Engine, deja implementat | Model semantic OBSERVATION deja funcțional. |
| COACH-D03 — Observație vs. interpretare | EXISTING_EVIDENCE_REUSED | Decision Engine | Deja separă OBSERVATION/POSSIBLE_CAUSE. |
| COACH-D04 — Formularea problemei | EXISTING_EVIDENCE_REUSED | `problem-library.json`, `observable_behavior` | Deja implementat. |
| COACH-D05 — Decizii de intervenție | EXISTING_EVIDENCE_REUSED | `possible_explanations` (schema problem) | Deja implementat. |
| COACH-D06 — Când NU intervine | **FOUNDATION_READY** | `COACH_INTERVENTION_R1.md` (14 claim-uri) | Domeniul marcat `CRITICAL — cel mai slab acoperit azi` în `COACH_DOMAIN_MAP.md` §Cluster 2 — acum are dosar dedicat. |
| **Cluster 3 — Comunicare de predare** | | | |
| COACH-D07 — Chestionare | **FOUNDATION_READY** | `QUESTIONING_GUIDED_DISCOVERY_R1.md` (13 claim-uri) | |
| COACH-D08 — Feedback | **FOUNDATION_READY** | `FEEDBACK_R1.md` (19 claim-uri) | |
| COACH-D09 — Cueing | **PARTIAL** | Secțiune dedicată în `ATTENTION_COGNITIVE_LOAD_R1.md` | Nu dosar de sine stătător — `RESEARCH_REQUIRED` pentru extindere Val 2 dacă „exact cue" evoluează spre schemă formală. |
| COACH-D10 — Demonstrație | **PARTIAL** | Atins în AC (demonstrație + explicație verbală) | `RESEARCH_REQUIRED`. |
| COACH-D11 — Ghidarea atenției | **FOUNDATION_READY** | `ATTENTION_COGNITIVE_LOAD_R1.md` (nucleul dosarului) | |
| **Cluster 4 — Proiectarea exercițiului** | | | |
| COACH-D12 — Proiectare de exercițiu | EXISTING_EVIDENCE_REUSED | `ch-0801`, Gold Standard | Matur. |
| COACH-D13 — Constrângeri | EXISTING_EVIDENCE_REUSED | `ch-0802` | Matur. |
| COACH-D14 — Design reprezentativ | EXISTING_EVIDENCE_REUSED | Principiu Gold Standard existent | Matur; extins teoretic de `SKILL_ACQUISITION_FRAMEWORKS_R1.md` și `PERCEPTION_DECISION_ACTION_R1.md`. |
| COACH-D15 — Variabilitate | **PARTIAL → FOUNDATION_READY parțial** | Interferență contextuală, variabilitatea practicii → `SKILL_ACQUISITION_FRAMEWORKS_R1.md` | Evidență directă la copii slabă/nulă (SMD=0,12 sub 18 ani) — se aplică prudență explicită. |
| COACH-D16 — Progresie/regresie | EXISTING_EVIDENCE_REUSED | Câmpuri `progression`/`regression`, deja în schemă | Matur. |
| **Cluster 5 — Organizare și predare tactică** | | | |
| COACH-D17 — Organizare de grup | NOT_RESEARCHED (produs) | Deja implementat (Group Configurator) | Nu necesită cercetare nouă acum. |
| COACH-D18 — Spațiu/numere/reguli | NOT_RESEARCHED (produs) | Deja implementat | — |
| COACH-D19 — Poziționarea antrenorului | NOT_RESEARCHED | — | `RESEARCH_REQUIRED`, marcat `HIGH` în domain map. |
| COACH-D20 — Timp activ de învățare | NOT_RESEARCHED (produs) | `ch-0805` | — |
| COACH-D21 — Predare tactică (freeze/în flux) | **PARTIAL** | Atins tangențial în `COACH_INTERVENTION_R1.md` (freeze coaching, fără literatură proprie sub acest nume) și pedagogia non-liniară din SA | `RESEARCH_REQUIRED` pentru un dosar dedicat. |
| COACH-D22 — Percepție | **FOUNDATION_READY** | `PERCEPTION_DECISION_ACTION_R1.md` (10 claim-uri) | Domeniu flagship (Decision Engine → PRB-0003), acum și fundamentat teoretic. |
| COACH-D23 — Luarea deciziei | **FOUNDATION_READY** | `PERCEPTION_DECISION_ACTION_R1.md` + antrenamentul deciziei din SA | |
| **Cluster 6 — Tehnică, transfer și evaluare** | | | |
| COACH-D24 — Tehnică în context | **PARTIAL** | Discuție „technique-in-context" în SA/PD | Nu dosar dedicat separat; concluzie nuanțată deja produsă (nici izolarea tehnicii e inutilă, nici suficientă singură). |
| COACH-D25 — Transfer | **FOUNDATION_READY (teoretic)** | `TRANSFER_RETENTION_R1.md` (13 claim-uri) | Fundamentul teoretic e gata; verificarea reală rămâne `FIELD_INPUT_REQUIRED` la nivel de produs (PHASE-23), neschimbat. |
| COACH-D26 — Evaluare | NOT_RESEARCHED | Assessment deja implementat la nivel de produs | — |
| **Cluster 7 — Planificare și diferențiere** | | | |
| COACH-D27 — Design de ședință | NOT_RESEARCHED (produs) | SES-0001/0002 deja implementat | — |
| COACH-D28 — Planificare pe termen mediu | NOT_RESEARCHED | `season-plans`, schemă fără conținut | `RESEARCH_REQUIRED`, marcat `HIGH` (zero conținut azi) — Val 3. |
| COACH-D29 — Diferențiere | NOT_RESEARCHED | — | Val 3. |
| COACH-D30 — Comunicare către grup | NOT_RESEARCHED | `ch-0301` (pre-PHASE-30) | — |
| COACH-D31 — Climat motivațional | **PARTIAL** | Climat motivațional acoperit indirect prin `MOTIVATION_AUTONOMY_R1.md` (PED-D03) | Legătura explicită COACH-D31 ↔ PED-D03 confirmată în domain map. |
| **Cluster 8 — Reflecție și dezvoltare profesională** | | | |
| COACH-D32 — Reflecție (a antrenorului) | NOT_RESEARCHED | — | Cluster complet nou, zero conținut azi — `RESEARCH_REQUIRED`, Val 2 (fundamentează Coach Development). |
| COACH-D33 — Auto-evaluare | NOT_RESEARCHED | — | Val 2. |
| COACH-D34 — Dezvoltare profesională | NOT_RESEARCHED | — | Val 2. |

## Rezumat

- `FOUNDATION_READY` (complet sau teoretic): 6 domenii — COACH-D06, D07, D08, D11, D22, D23, plus D25 parțial (teoretic, nu field-validat).
- `EXISTING_EVIDENCE_REUSED`: 6 domenii — deja mature din Decision Engine/Gold Standard, corect nere-cercetate.
- `PARTIAL`: 6 domenii — D09, D10, D15, D21, D24, D31.
- `NOT_RESEARCHED`: 16 domenii — majoritatea în clusterele 5 (organizare, unde produsul e deja implementat și cercetarea nu e urgentă), 7 (planificare, D28 marcat prioritate reală) și 8 (reflecție/dezvoltare, întregul cluster e teritoriu complet nou pentru Coach Development).

Consistent cu `PHASE30_RESEARCH_ROADMAP.md`: clusterul 8 (reflecția antrenorului) rămâne cel mai mare gol real — nu pentru că a fost ignorat, ci pentru că fundamentează direct funcționalitatea viitoare de Coach Development, care nu a fost autorizată pentru cercetare de fond în acest val.
