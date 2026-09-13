# TASK-2706 — SES-0001/SES-0002 operational contingencies

## Scop și rezultat verificabil

Face SES-0001 și SES-0002 robuste la condiții reale de teren: efective de 8–18, întârziați, spațiu redus, material insuficient, un exercițiu care eșuează sau durează prea mult la tranziție — fără să inventeze logistică nefundamentată.

## Progres

- [x] `players_range` extins de la 9–16 la 8–18 în ambele ședințe, cu notă actualizată care trimite la configuratorul de grup (`TASK-2705`) pentru numărul exact de grupe la fiecare efectiv.
- [x] `schemas/session.schema.json` extins aditiv cu `operational_contingencies` (obligatoriu, minim 1 element).
- [x] 5 scenarii reale per ședință (întârziați, spațiu redus, material insuficient, exercițiu eșuat, tranziție lungă), fiecare cu ghidare etichetată explicit `PRACTICE_HEURISTIC`, reutilizând câmpuri canonice deja existente (`too_small_signs`, `transition_logistics`, `regression`) în loc să dubleze conținut.
- [x] `content-bridge.ts` extins (`GoldStandardOperationalContingency`, fail-closed pe `operational_contingencies`).
- [x] Pagina de ședință (`[id].astro`) afișează secțiunea „Contingențe operaționale” și un link către configuratorul de grup din „Pregătire”.
- [x] Verificat browser la 1440/390: 0 erori consolă, 0 overflow orizontal.
- [x] Validare locală completă PASS.

## Limită

Nu produce vizualuri noi pentru EX-0004/EX-0005 (`TASK-2707`) și nu construiește Field Mode (`TASK-2710`) — contingențele sunt text, nu un instrument interactiv de teren.
