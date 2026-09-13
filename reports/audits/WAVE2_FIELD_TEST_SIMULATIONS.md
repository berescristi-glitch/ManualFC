# Wave-2 — Simulări de teren (§38 din specificația Wave-2)

Toate cifrele de mai jos sunt extrase direct din `/gold-standard/configurator` (motorul determinist `group-configurator.ts`, `TASK-2705`), verificat prin `browser_evaluate` pe pagina reală randată, nu recalculate manual.

## Scenariul A — 8 copii, 1 antrenor

| Exercițiu | Grupe | Activi | Așteptare | Poziționare antrenor |
|---|---:|---:|---:|---|
| EX-0001/2/3 (2v1, grup 3) | 2 | 6 | 2 | circulă între cele două grupe, alternând la fiecare set |
| EX-0004 (3v2, grup 5) | 1 | 5 | 3 | observă direct, fără rotație de atenție |
| EX-0005 (4v4, grup 8) | 1 | 8 | 0 | observă direct, fără rotație de atenție |

## Scenariul B — 12 copii, 1 antrenor

| Exercițiu | Grupe | Activi | Așteptare | Poziționare antrenor |
|---|---:|---:|---:|---|
| EX-0001/2/3 | 4 | 12 | 0 | prioritizează 1-2 grupe pe rând, restul auto-verificare |
| EX-0004 | 2 | 10 | 2 | circulă între cele două grupe |
| EX-0005 | 1 | 8 | 4 | observă direct |

## Scenariul C — 16 copii, 2 antrenori

| Exercițiu | Grupe | Activi | Așteptare | Împărțire antrenori |
|---|---:|---:|---:|---|
| EX-0001/2/3 | 5 | 15 | 1 | primul 3 grupe, al doilea 2 grupe |
| EX-0004 | 3 | 15 | 1 | primul 2 grupe, al doilea 1 grup |
| EX-0005 | 2 | 16 | 0 | primul 1 grup, al doilea 1 grup |

## Scenariul D — 18 copii, 1 antrenor

| Exercițiu | Grupe | Activi | Așteptare | Poziționare antrenor |
|---|---:|---:|---:|---|
| EX-0001/2/3 | 6 | 18 | 0 | prioritizează 1-2 grupe pe rând, restul auto-verificare |
| EX-0004 | 3 | 15 | 3 | prioritizează 1-2 grupe pe rând |
| EX-0005 | 2 | 16 | 2 | circulă între cele două grupe |

## Scenariul E — 14 copii, 3 ajung după începerea ședinței

Nu e un caz de configurator (grupele nu se recalculează la mijlocul ședinței) — e exact scenariul acoperit de `operational_contingencies` din `TASK-2706` (`SES-0001`, scenariul „3 copii ajung după ce ședința a început”): copiii întârziați așteaptă vizibil lângă cea mai apropiată stație și intră la următoarea rotație naturală (90 secunde la EX-0001, la fiecare set la EX-0002/EX-0003) — nu se creează o a patra stație improvizată doar pentru ei. Configuratorul răspunde separat la întrebarea „cum organizez pentru 14, dacă toți sunt deja prezenți”: 4 grupe de 3, 12 activi, 2 în așteptare de la început (independent de întârziere).

## Verdict

Toate cele 4 scenarii de efectiv (A–D) produc configurații complete și consistente (grupe × mărime grup = activi; activi + așteptare = total; echipamentul scalează liniar cu numărul de grupe) pentru toate cele 5 exerciții. Scenariul E este acoperit de contingențele de ședință, nu de configurator — corect, pentru că e o problemă de secvențiere în timp real, nu de împărțire inițială pe grupe.

`GROUP_CONFIG_8 = PASS`, `GROUP_CONFIG_10 = PASS`, `GROUP_CONFIG_12 = PASS`, `GROUP_CONFIG_14 = PASS`, `GROUP_CONFIG_16 = PASS`, `GROUP_CONFIG_18 = PASS`, `ONE_COACH = SUPPORTED`, `TWO_COACHES = SUPPORTED`, `SESSION_CONTINGENCIES = IMPLEMENTED`.
