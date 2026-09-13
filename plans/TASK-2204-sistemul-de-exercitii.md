# TASK-2204 — Sistemul de exerciții Gold Standard

## Scop

Prima producție reală a entității `exercise` din proiect (schema exista în `schemas/exercise.schema.json`, 0 instanțe până acum). Familia de exerciții trebuie derivată din etapele de învățare identificate în `docs/gold-standard/CONCEPT_MODEL.md`, nu dintr-o cotă istorică ("5 exerciții" din vechiul prototip TASK-0410).

## Metodă

1. Derivarea etapelor de învățare din modelul perceptiv/decizional/tehnic deja stabilit (`TASK-2203`).
2. Auditarea explicită a progresiei istorice 2v1→3v2→4v4 — fiecare treaptă justificată prin informația/decizia nouă introdusă, nu presupusă corectă (cerință explicită `TASK-2201` secțiunea 3).
3. Fiecare exercițiu documentează job-ul lui (problemă, informație, decizie, organizare, reguli+motiv, erori comune, progresie/regresie, transfer, status evidență).
4. Politica numerelor exacte aplicată strict: toate dimensiunile etichetate `EXERCISE_SPECIFIC_PARAMETER`.
5. Ultimul exercițiu (transfer reprezentativ) marchează explicit `FIELD_VALIDATION_PENDING` — nu se simulează rezultate de pilotare.

## Rezultat

Vezi `reports/task-reports/TASK-2204.md`. `TASK-2205` (sistemul de ședințe) devine `READY`.
