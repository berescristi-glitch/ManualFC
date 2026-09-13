# ManualFC — Product Integrity Register

| Domeniu | Stare finală | Dovadă / limită |
|---|---|---|
| Fișiere versionate | PASS | 0 fișiere tracked de 0 bytes; 895 fișiere text UTF-8 valide |
| JSON tracked | PASS | 98/98 parse Python în Stage 1 |
| Dovezi publicate | PASS | validator fail-closed + test de regresie; PRB-0008 remapat la claim-uri active |
| Safeguarding | PASS | validator 0 erori; 4 contacte reverificate, contactul local neverificabil eliminat |
| Pytest | PASS | 506 passed, 25 subtests; colectare limitată explicit la `tests/` |
| Node tests | PASS | 1 test real; 101 pagini, `main=1`, `h1=1` |
| Astro check/build | PASS | 96 fișiere fără diagnostic; 101 pagini construite |
| Linkuri interne | PASS | 101 HTML, 0 referințe interne rupte |
| Chromium/Axe | PASS | 52 combinații, 0 findings; Axe 0 |
| Offline pregătit | PASS | cold reload 200, SW/cache/badge și controale verificate |
| Firefox/WebKit | NOT_RUN | executabile indisponibile; datorie înainte de comercializare |
| npm advisory audit | NOT_RUN_POLICY_BLOCKED | escaladarea a fost respinsă din cauza exportului de metadate |
| Human learning validation | NOT_YET_RUN | nu este substituită de teste automate |
| PHASE-23 | FIELD_INPUT_REQUIRED | neschimbat |
