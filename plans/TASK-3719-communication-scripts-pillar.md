# TASK-3719 — Biblioteca de scripturi de comunicare antrenor-copil

## 1. Titlu și scop

Rezultatul observabil: un al treilea sistem canonic de conținut ManualFC (după cele două teme de antrenament) — o bibliotecă de ~24-26 scripturi de comunicare reutilizabile, fiecare ancorat într-o situație reală de teren, cu fundamentare pedagogică completă, căutabil, navigabil din exerciții/ședințe/principii ale AMBELOR teme, și integrat în rute/sitemap/căutare fără a corupe conținutul existent.

## 2. Context pentru un cititor nou

- Repository canonic: `E:\ManualFC-clean`. Repository legacy `E:\ManualFC` — NU se atinge.
- Există deja **două teme complete de antrenament**: „Sprijinul și unghiul de pasă" (`theme: sprijin-si-unghi-de-pasa`, EX-0001–EX-0015, SES-0001–SES-0006, ASM-0001) și „Apărarea: presiune și acoperire" (`theme: apararea-presiune-si-acoperire`, EX-0016–EX-0025, SES-0007–SES-0010, ASM-0002) — construite în TASK-3712/TASK-3718.
- Motorul de decizie (`data/problems/problem-library.json`) are 8 probleme (`PRB-0001`–`PRB-0008`), fiecare cu `related_exercises`/`related_sessions`/`assessment_links`/`related_principles`.
- `data/principles/` conține 21 de principii canonice (`principle.<slug>`), atât tactice specifice temelor (`spatiu-si-unghiuri`, `progresie-si-sprijin`, `presiune-si-acoperire`, `protejarea-centrului`, `tranzitia-la-pierderea-mingii`, `tranzitia-la-castigarea-mingii`, `transfer-autonom-cooperare`, `jocul-ca-sistem-de-probleme`, `superioritate-egalitate-inferioritate-numerica`) cât și pedagogice universale (`eroarea-ca-informatie`, `greseala-ca-informatie-si-siguranta`, `disciplina-fara-umilire`, `conversatii-individuale-si-echitate`, `reflectia-ghidata-si-transferul-in-joc`, `manipularea-si-dozarea-constrangerilor`, `focalizarea-observatiei-si-criterii-de-interventie`, `tacet-si-observa-fara-joystick`, `intrebari-si-verificarea-intelegerii`, `limbaj-scurt-si-relevanta`).
- **Există deja un schelet neutilizat pentru acest pilon:** `schemas/communication-script.schema.json` (5 proprietăți: `id` SCR-XXXX, `slug`, `title`, `principle_ids`, `message_foundations`) și directorul gol `data/communication-scripts/` (doar README). `scripts/validate_content.py` are deja mapat directorul (`"data/communication-scripts/": "communication-script"`) și prefixul (`"SCR": "communication-script"`), și deja include `communication-script` în lista de tipuri verificate de `_validate_pedagogy`/`_walk_text`. Zero fișiere `SCR-*.json` există azi.
- `schemas/message-foundation.schema.json` (tip `MSG-XXXX`) definește deja, complet neutilizat ca document de sine stătător, aproape toate câmpurile de fundamentare cerute de acest task pentru un mesaj individual (`child_wording`, `coach_meaning`, `why_this_wording`, `problem_being_solved`, `information_to_notice`, `interpretation`, `decision_to_learn`, `observable_behaviours`, `rationales` cu exact 7 chei, `age_appropriateness`, `phrases_to_avoid`, `misinterpretation_risks`, `task_risks`, `understanding_check`, `response_if_not_working`, `match_transfer`, `source_claim_ids`).
- `config/project.json.minimum_deliverables.communication_scripts = 50` — o țintă declarată pe termen lung, verificată doar static de `scripts/validate_project.py` (compară configul cu el însuși, nu numără fișiere reale) — acest task NU trebuie să atingă 50; scopul explicit al taskului este 20-30.
- Roadmap-ul canonic (`docs/roadmap/MANUALFC_CANONICAL_ROADMAP.md`, Phase 5) plasează populația unui pilon de conținut gol DUPĂ dovezi de pilotare reală ("selected by pilot-evidenced need, not schema convenience"). Pilotarea rămâne `BLOCKED` (`TASK-3714`). **Utilizatorul autorizează explicit această abatere de la secvențierea roadmap-ului** — exact ca la TASK-3718 pentru a doua temă — și acest task nu pretinde nicio validare de teren.
- Ambele teme urmează convenția FAIL_CLOSED: `app/src/lib/content-bridge.ts` are liste hardcodate de importuri (nu glob) + funcții `parseGoldStandard*` care aruncă eroare la orice referință inexistentă; `getGoldStandardAssessments()`/`getGoldStandardAssessment(id?)` sunt deja generalizate multi-temă din TASK-3718.
- `scripts/validate_gold_standard_v2.py` verifică DOAR exerciții/ședințe cu `gold_standard_v2.status === "V2"` — nu se extinde la scripturi (scop diferit); acest task adaugă un validator nou, dedicat, `scripts/validate_communication_scripts.py`, urmând exact același tipar (citește fișierele reale din `data/`, verifică fiecare ID referențiat există cu adevărat, 0 rezultate = 0 erori).
- `research/claims.json` conține deja evidență reală (verificată direct, nu presupusă) despre: susținerea autonomiei (`CLM-0080`, `CLM-0119`, `CLM-0130`, `CLM-0131`), focalizare atențională externă la copii (`CLM-0066`, `CLM-0102`, `CLM-0135`), feedback auto-controlat (`CLM-0150`, `CLM-0183`), structură + autonomie coexistente (`CLM-0078`, `CLM-0081`), timp de așteptare după întrebare (`CLM-0170`), supraîncrederea copiilor în auto-evaluare (`CLM-0071`, `CLM-0072`), lauda de proces vs. lauda de persoană (`CLM-0263`), efectul frustrării asupra erorilor (`CLM-0267`), percepția tratamentului diferențiat (`CLM-0235`), agresivitatea verbală a antrenorului (`CLM-0308`), ierarhia calității reflecției (`CLM-0274`). **Atenție verificată direct:** `CLM-0054`, `CLM-0056`, `CLM-0057` sunt intrări auto-corective — declară explicit că afirmația inițială nu era susținută de sursa citată (fabricată/nepotrivită) și redirecționează spre alte CLM reale (`CLM-0069`–`CLM-0072`, `CLM-0078`–`CLM-0083`, `CLM-0088`); acest task NU le citează ca dovadă directă, doar `CLM-0088` pentru a declara onest statutul incert al termenului „joystick coaching".

## 3. Rezultatul verificabil

- Schema `schemas/communication-script.schema.json` extinsă (aditiv, document nou — 0 fișiere existente afectate) cu toate câmpurile cerute de task.
- 26 fișiere `data/communication-scripts/script-<slug>.json`, validate 0 erori de `validate_content.py --strict` și de noul `validate_communication_scripts.py`.
- `app/src/lib/content-bridge.ts` extins cu `getCommunicationScripts()`/`getCommunicationScript(id)`, FAIL_CLOSED.
- Pagini noi: `/scripturi/` (index, filtrabil pe categorie — traseu de descoperire 1), `/scripturi/[id].astro` (detaliu). Bloc „Scripturi relevante" adăugat pe paginile de exercițiu, ședință și principiu, generat din legăturile reale (`related_exercise_ids`/`related_session_ids`/`principle_ids`) — traseu de descoperire 2.
- `discovery-index.ts` extins să indexeze scripturile (căutare unificată).
- Teste noi (`tests/test_task3719_communication_scripts.py`), teste web actualizate (contor de rute).
- Guvernanță actualizată (`TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, raport final).

## 4. Domeniu și non-obiective

**În scop:** biblioteca de scripturi, cele două trasee de descoperire, integrarea în căutare/sitemap/rute, cross-linkuri reale către ambele teme.

**Non-obiective explicite:**
- NU se ating pilonii „case studies" sau „season plans" (rămân goi, deliberat, ca și înainte).
- NU se atinge conținutul existent al celor două teme (exerciții/ședințe/evaluări/probleme) — doar se citește pentru a construi legături reale.
- NU se construiește autentificare, cont, bază de date, analitice sau personalizare.
- NU se creează diagrame SVG/animații pentru scripturi — acestea sunt text de rostit, nu situații tactice spațiale; nu există un echivalent al `visual_assets` necesar aici (spre deosebire de exerciții).
- NU se urmărește atingerea pragului de 50 din `config/project.json` — scopul explicit e 20-30, calitate peste cantitate.
- NU se modifică `schemas/message-foundation.schema.json` sau `schemas/case-study.schema.json` — rămân neatinse, doar inspirație de design.

## 5. Fișiere și module afectate

**Noi:**
- `schemas/communication-script.schema.json` (rescris, aditiv — 0 documente existente)
- `data/communication-scripts/script-*.json` (26 fișiere)
- `scripts/validate_communication_scripts.py`
- `app/src/pages/scripturi/index.astro`
- `app/src/pages/scripturi/[id].astro`
- `tests/test_task3719_communication_scripts.py`

**Modificate:**
- `app/src/lib/content-bridge.ts` (26 importuri + 2 funcții noi)
- `app/src/lib/discovery-index.ts` (indexare scripturi)
- `app/src/pages/gold-standard/exercitii/[id].astro`, `app/src/pages/gold-standard/sedinte/[id].astro`, `app/src/pages/principii/[slug].astro` (bloc „Scripturi relevante")
- `tests/web/built-routes.test.js` (contor de rute)

## 6. Cercetare necesară

Niciun claim nou de cercetat — se reutilizează exclusiv `research/claims.json`/`sources.json` existente, verificate deja non-retrase. Pentru fiecare script cu `source_claim_ids`, se verifică manual textul complet al claim-ului înainte de citare (nu doar căutare de cuvinte cheie) — vezi §2 pentru claim-urile auto-corective descoperite.

## 7. Model pedagogic

Fiecare script răspunde la „ce spun acum?" păstrând raționamentul professional din spate — exact structura deja aplicată la exerciții (`child_message`/`why_this_message`/`rationales` cu 7 dimensiuni), dar centrată pe un MOMENT DE COMUNICARE, nu pe o sarcină motrică. Un script NU e o frază motivațională generică — fiecare reprezintă o situație distinctă de teren (declanșator, informație de observat, decizie de învățat), cu o variantă scurtă (joc activ) și una extinsă (pauză/reflecție), o întrebare de verificare a înțelegerii care NU e „ai înțeles?" (motivat de `CLM-0071`/`CLM-0072`: copiii nu-și detectează fiabil propria neînțelegere când sunt întrebați direct), și o listă explicită de formulări de evitat.

## 8. Design vizual și interactiv

Fără diagrame/animații (non-obiectiv, §4). Paginile de scripturi reutilizează componentele text existente (`ChildMessage.astro`, `CoachMessage.astro` dacă se potrivesc structural) și stilul `FieldCard`-like pentru lizibilitate pe teren (variantă scurtă vizibilă imediat, restul extensibil). Accesibilitate: aceleași standarde ca restul site-ului (axe 0 violări, `main`=1/`h1`=1).

## 9. Pași de implementare

1. Inspectare completă (acest document, §2) — FĂCUT.
2. Rescriere `schemas/communication-script.schema.json`.
3. Redactare 26 scripturi, în ordinea categoriilor din inventar (§ mai jos, în corpul planului actualizat pe parcurs).
4. `scripts/validate_communication_scripts.py` + rulare.
5. `validate_content.py --strict` pe toate scripturile.
6. Extindere `content-bridge.ts`, `discovery-index.ts`.
7. Pagini noi `/scripturi/index.astro`, `/scripturi/[id].astro`; blocuri „Scripturi relevante" pe exercitii/sedinte/principii.
8. Teste Python + actualizare `built-routes.test.js`.
9. `npm run check`, `npm run build`, Playwright+axe la 1440/390px, sitemap.
10. `pytest` complet, `git fsck`, fresh clone, commit, push, guvernanță, raport.

## 10. Validare și acceptare

- `python scripts/validate_content.py --strict` — 0 erori.
- `python scripts/validate_communication_scripts.py` — 0 erori.
- `npm run check` — 0 erori.
- `npm test` — 9/9 (contor de rute actualizat).
- `python -m pytest tests/ -q` — 0 eșecuri.
- `npm run build` — pagini noi prezente (`/scripturi/`, 26× `/scripturi/SCR-XXXX/`).
- Playwright+axe la 1440px/390px pe cel puțin: `/scripturi/`, 2 pagini de detaliu script, o pagină de exercițiu/ședință/principiu cu bloc „Scripturi relevante" din fiecare temă.
- `git fsck --full` curat, fresh clone reproduce identic.

## 11. Progres

- [x] Inspecție completă + decizie arhitecturală (schema, reutilizare `message-foundation` ca model de câmpuri)
- [ ] Schema rescrisă
- [ ] 26 scripturi redactate și validate
- [ ] Validator nou scris
- [ ] `content-bridge.ts`/`discovery-index.ts` extinse
- [ ] Pagini noi + blocuri „Scripturi relevante"
- [ ] Teste noi
- [ ] Validare completă + fresh clone
- [ ] Guvernanță + raport + push

## 12. Descoperiri și surprize

- Schema `communication-script.schema.json` și directorul `data/communication-scripts/` existau deja ca schelet neutilizat — nu s-a pornit de la zero, dar schema stub era mult prea subțire (5 proprietăți) față de cerințele explicite ale taskului (~20 câmpuri).
- `schemas/message-foundation.schema.json` (tip MSG, de asemenea complet neutilizat ca document de sine stătător) s-a dovedit aproape identic ca formă cu ce cerea taskul pentru un singur mesaj — decizie: **un script E un obiect în formă de message-foundation, extins cu câmpuri specifice scriptului** (situație/declanșator, variantă scurtă/extinsă, observație înainte de a vorbi, când intervii/nu intervii), NU un container care înfășoară un array de `message_foundations` ca la exerciții/ședințe. Motivul: un script reprezintă UN singur mesaj pentru O singură situație, nu un grup de mesaje ca într-un exercițiu complet.
- Reutilizarea numelor de câmpuri din `message-foundation.schema.json`/`exercise.schema.json` (`child_wording`, `rationales` cu exact 7 chei) declanșează automat validatorul FAIL_CLOSED de pedagogie deja existent în `validate_content.py` (`_walk_pedagogy_objects`/`_validate_pedagogy`), fără cod nou — validare gratuită, consistentă cu restul proiectului.
- Trei claim-uri (`CLM-0054`, `CLM-0056`, `CLM-0057`) găsite inițial prin căutare de cuvinte cheie s-au dovedit, la citirea textului complet, a fi intrări auto-corective (nu suportă afirmația inițială) — verificarea manuală a textului complet, nu doar căutarea de cuvinte cheie, a prevenit o citare incorectă.

## 13. Jurnal de decizii

1. **Decizie:** un script = un obiect message-foundation-shaped extins, nu un container de `message_foundations`. **Motiv:** un script descrie o singură situație/mesaj, nu un exercițiu complet cu mai multe mesaje. **Alternativă respinsă:** păstrarea câmpului `message_foundations` din schema stub ca array — ar fi adăugat un nivel de nesting fără beneficiu real. **Efect:** schema nouă elimină `message_foundations` din required, adaugă direct câmpurile message-foundation. **Data:** 2026-09-21.
2. **Decizie:** rutele de detaliu exercițiu/ședință/principiu rămân la căile existente; se adaugă doar un bloc nou de conținut („Scripturi relevante"), nu rute noi pentru ele. **Motiv:** nu rupe URL-uri live, consecvent cu decizia de rutare din TASK-3718. **Data:** 2026-09-21.
3. **Decizie:** niciun `applicable_themes` denormalizat pe script; legătura cu „ambele teme" se demonstrează la nivel de bibliotecă prin `related_exercise_ids`/`related_session_ids`/`principle_ids` reale din ambele teme, nu printr-un câmp redundant care ar putea deveni inconsecvent. **Data:** 2026-09-21.
4. **Decizie:** validator nou dedicat (`validate_communication_scripts.py`), nu extinderea `validate_gold_standard_v2.py` (scop diferit, nume specific „Gold Standard V2"). **Data:** 2026-09-21.

## 14. Rezultat și retrospectivă

_(completat la finalul taskului)_
