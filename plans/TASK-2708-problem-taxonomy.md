# ExecPlan TASK-2708 — Problem taxonomy

## Purpose

Livrarea unei biblioteci canonice de probleme U11, observație-first, cu dovezi și graf validat.

## Progress

- [x] Recuperare Git și sanity Production.
- [x] Citirea arhitecturii și cercetare externă.
- [x] Schema și opt probleme, trei flagship.
- [x] Teste fail-closed pentru graf și limbaj diagnostic.
- [x] Validare completă, raport și registru.

## Decisions

Se reutilizează principii/exerciții/sesiuni/evaluări; lipsa unei relații legitime rămâne listă goală. Testele reduc incertitudinea și nu confirmă o cauză. Media disponibilă este limitată la flagship-uri.

## Evidence

`python -m unittest tests.test_task2708_problem_graph -v` — 4/4 PASS. Validatorul de conținut — 0 erori.
