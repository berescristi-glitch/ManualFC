# Ghidul registrelor

## Întrebări și căutări

Întrebările sunt în `research/questions.json`. Jurnalul `search-logs.jsonl` este append-only și păstrează interogarea exactă, filtrele, data/ora, limba, intervalul, rezultate, includeri, excluderi și rolul.

## Surse, afirmații și citări

`sources.json` păstrează proveniența, versiunea, drepturile, populația și actualitatea. `claims.json` separă afirmația, încrederea, limitele și formularea permisă. `citations.json` fixează locatorul precis și utilizarea.

Lanțul obligatoriu este:

`RQ → SEARCH → SRC → CLM → CIT → locație în manual`.

Notele separă: ce spune sursa; locatorul; interpretarea; relevanța; limita; utilizarea posibilă; întrebările rămase.

## Încredere

`HIGH`, `MODERATE`, `LOW`, `PRACTICE_ONLY`, `UNRESOLVED` iau în calcul metoda, populația, fotbalul, consistența, actualitatea, conflictele și cauzalitatea. Prestigiul singur nu modifică nivelul.

Afirmațiile `CONTESTED`, `OUTDATED`, `WITHDRAWN` sau `REPLACED` nu intră în build fără explicație și aprobare.
