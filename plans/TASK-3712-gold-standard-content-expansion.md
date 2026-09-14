# TASK-3712 — Gold Standard Content Expansion

## 1. Titlu și scop

Extinde tema Gold Standard existentă ("Sprijinul și unghiul de pasă") dintr-o demonstrație validată (5 exerciții, 2 ședințe) într-un sistem de coaching complet, reutilizabil de-a lungul unui sezon: 10 exerciții noi (EX-0006–EX-0015) și 4 ședințe noi (SES-0003–SES-0006), la aceeași profunzime pedagogică și tehnică ca EX-0001–EX-0005/SES-0001–SES-0002.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD de pornire `3d9c6da349ccd3054f4713b811c2d4aa68944392` (rezultatul TASK-3711).
- Conținutul Gold Standard actual: `data/exercises/*.json` (5 fișiere, EX-0001–EX-0005), `data/sessions/*.json` (2 fișiere, SES-0001/SES-0002), `data/assessments/assessment-sprijin-si-unghi-de-pasa.json` (ASM-0001, 5 criterii, unul per exercițiu), validate de `schemas/exercise.schema.json`/`session.schema.json`/`assessment.schema.json` și, pentru câmpurile V2, de `scripts/validate_gold_standard_v2.py`.
- `app/src/lib/content-bridge.ts` încarcă exercițiile/ședințele/evaluarea prin **liste statice hardcodate** de importuri (nu glob) — `getGoldStandardExercises()`/`getGoldStandardSessions()` trebuie extinse manual cu noile fișiere.
- Rutele `/gold-standard/exercitii/[id]`, `/gold-standard/sedinte/[id]`, `/gold-standard/sedinte/[id]/mod-teren` sunt generate dinamic din `getStaticPaths()` — orice exercițiu/ședință nou apare automat, fără cod nou de rutare. Diagramele SVG sunt limitate explicit la EX-0001–EX-0005 (`diagramVariants` hardcodat în ambele pagini `[id].astro`); exercițiile noi vor afișa onest nota „Organizare fără diagramă în această versiune" deja existentă — consecvent cu convenția `visual_assets: PENDING` deja folosită de EX-0001–EX-0005 (design freeze activ, nicio diagramă produsă încă pentru niciun exercițiu).
- `data/problems/problem-library.json` conține 8 probleme reale ale Deciziei Engine; 5 dintre ele (PRB-0001, 0002, 0003, 0005, 0007, 0008) sunt deja tematic legate de „sprijin și unghi de pasă"; PRB-0004 (îngheață după pierderea mingii) și PRB-0006 (primul apărător presează fără acoperire) sunt organizare defensivă — o temă diferită, deliberat neatinsă (vezi §4).
- `scripts/validate_content.py` (schema JSON, glob pe `data/exercises`/`data/sessions`) și `scripts/validate_gold_standard_v2.py` (completitudine semantică V2: `pedagog_competency_ids`/`coach_competency_ids` reale din `docs/knowledge/PEDAGOG_COMPETENCY_FRAMEWORK.md`/`COACH_COMPETENCY_FRAMEWORK.md`, `related_*_lesson_ids` reale din `content/volume-0{1,3,4}/chapter-*.mdx`, `pedagogical_principle_ids` reale din `data/principles/`, `assessment_ref` real) rulează glob-based — preiau automat fișierele noi.
- Testele Python existente (`test_task2204_exercises.py`, `test_task2205_sessions.py`, `test_task2206_assessment.py`) verifică EXCLUSIV lista hardcodată a celor 5/2 fișiere vechi — rămân verzi neschimbate. `test_task2708_problem_graph.py` e glob-based și va revalida automat legăturile noi din `problem-library.json`.

## 3. Rezultatul verificabil

- 10 fișiere noi în `data/exercises/`, 4 fișiere noi în `data/sessions/`, toate valide contra schemelor și `validate_gold_standard_v2.py`.
- `data/assessments/assessment-sprijin-si-unghi-de-pasa.json` extins cu 3 criterii noi (C6–C8) acoperind conceptele noi.
- `data/problems/problem-library.json`: `related_exercises`/`related_sessions` întărite pentru PRB-0001, 0002, 0003, 0005, 0007, 0008.
- `app/src/lib/content-bridge.ts` încarcă toate cele 15 exerciții/6 ședințe.
- Un test nou (`tests/test_task3712_gold_standard_expansion.py`) verifică rigoarea conținutului nou, analog cu testele TASK-2204/2205/2206.
- `npm run build` produce toate rutele noi; `tests/web/built-routes.test.js` reflectă noul număr total de pagini.
- Toate validările obligatorii trec, atât în repo-ul canonic cât și într-un fresh clone.

## 4. Domeniu și non-obiective

**Intră:** 10 exerciții + 4 ședințe noi, întărirea legăturilor problemă→principiu→exercițiu→ședință→reflecție→transfer în interiorul temei EXISTENTE, extinderea minimă a evaluării ASM-0001, actualizarea `content-bridge.ts` și a testelor.

**Nu intră:** o a doua temă de antrenament; arhitectura multi-age; autentificare/bază de date/analytics/plăți/conturi; diagrame SVG reale (rămân `PENDING`, consecvent cu design freeze-ul deja activ pentru EX-0001–EX-0005); legarea PRB-0004/PRB-0006 (organizare defensivă — primul apărător/al doilea apărător — e conceptual distinctă de „sprijin și unghi de pasă" în posesie; construirea acestei legături ar însemna, de fapt, începutul unei a doua teme de antrenament, interzis explicit de task).

## 5. Fișiere și module afectate

Noi: `data/exercises/exercise-{unghiul-de-sprijin-din-spate,unu-doi-pentru-a-iesi-din-umbra,al-treilea-jucator-de-sprijin,receptie-sub-presiune-completa,momentul-potrivit-de-plecare,patru-sprijiniri-o-singura-minge,prima-privire-dupa-recuperare,sprijin-pe-culoar-lateral,joc-mic-3v3-doua-porti,joc-mic-5v5-zona-de-finalizare}.json` (EX-0006–EX-0015); `data/sessions/session-{sprijin-din-spate-si-combinatie,al-treilea-jucator-si-presiune,recuperare-si-sprijin-lateral,transfer-complet-jocuri-variate}.json` (SES-0003–SES-0006); `tests/test_task3712_gold_standard_expansion.py`.

Modificate: `data/assessments/assessment-sprijin-si-unghi-de-pasa.json`, `data/problems/problem-library.json`, `app/src/lib/content-bridge.ts`, `tests/web/built-routes.test.js` (numărul de pagini), guvernanță (`TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, `scripts/generate_task_registry.py`).

## 7. Model pedagogic (rezumat — detaliat per fișier în conținut)

Progresia existentă (EX-0001→EX-0005: recunoaște umbra → decizie sub presiune → orientare la recepție → coordonare 2 sprijiniri → transfer 4v4) se extinde cu patru direcții noi, toate în posesie, toate „sprijin și unghi de pasă":

1. **Adâncimea sprijinului** (EX-0006, EX-0010, EX-0013) — unghi din spate vs. lateral, momentul plecării, adaptarea la spațiu îngust de bandă.
2. **Combinația ca a doua cale de a ieși din umbră** (EX-0007) — 1-2 în loc de repoziționare pură.
3. **Coordonarea la 3 sprijiniri și presiune completă** (EX-0008, EX-0009, EX-0011) — extinde EX-0004 de la 2 la 3 jucători de sprijin; extinde EX-0003 de la presiune moderată la presiune completă.
4. **Declanșator realist: chiar după recuperarea mingii** (EX-0012) — aplică aceeași decizie sprijin/progresie exact în momentul câștigării posesiei (`principle.tranzitia-la-castigarea-mingii`, deja canonic, deja parțial folosit de EX-0005/SES-0002 prin PRB-0005).
5. **Transfer variat** (EX-0014 3v3, EX-0015 5v5) — două jocuri reprezentative noi, la relații numerice diferite de EX-0005 (4v4), pentru ca un antrenor să nu repete exact același joc de transfer sezon după sezon.

Fiecare exercițiu nou documentează integral: problema, contextul de joc, percepția și decizia cerute, comportamentul observabil, mesajul exact + sensul lui profesional, motivul constrângerii, ce/când observă și intervine/nu intervine antrenorul, progresie/regresie cu păstrarea intenției, adecvarea U11, cele 7 raționale, greșeli de interpretare și riscuri, verificarea înțelegerii, răspunsul dacă mesajul nu funcționează, transferul în meci și granița dovezii — exact structura schemei și a EX-0001–EX-0005.

## 9. Pași de implementare

1. Cercetare/inventar (finalizat — acest plan).
2. Redactare 10 exerciții (`data/exercises/`).
3. Redactare 4 ședințe (`data/sessions/`).
4. Extindere ASM-0001 (+3 criterii).
5. Întărire `problem-library.json` (legături noi, fără probleme noi).
6. Actualizare `content-bridge.ts` (importuri + array-uri).
7. Test nou `test_task3712_gold_standard_expansion.py`.
8. Build local, actualizare număr pagini în `built-routes.test.js`.
9. Validare completă (schema, V2, pytest, check, build, browser+axe real la desktop/mobil pe minimum 2 pagini noi).
10. Fresh clone + guvernanță + raport final.

## 11. Progres

- [x] Context, inventar conținut existent, decizie de scop (fără PRB-0004/0006).
- [x] 10 exerciții noi (EX-0006–EX-0015), validate 0 erori (`validate_content.py --strict`, `validate_gold_standard_v2.py`).
- [x] 4 ședințe noi (SES-0003–SES-0006), segmente contigue verificate (75 min și varianta de 60 min).
- [x] ASM-0001 extins cu 3 criterii noi (C6–C8).
- [x] problem-library.json întărit (PRB-0001,0002,0003,0005,0007,0008); PRB-0004/0006 lăsate deliberat orfane.
- [x] content-bridge.ts actualizat (15 exerciții, 6 ședințe).
- [x] Defect real găsit și reparat: `FieldCard.astro` randa necondiționat `TacticalDiagram` pentru orice exercițiu, ceea ce arunca `dist/web` gol la build imediat ce au apărut exerciții în afara EX-0001–EX-0005 (`TacticalDiagram` are un tip TypeScript și o hartă de conținut limitate explicit la acele 5 ID-uri). Reparat cu același tipar `hasDiagram`/notă onestă deja folosit în `exercitii/[id].astro` și `sedinte/[id]/mod-teren.astro`.
- [x] Test nou `tests/test_task3712_gold_standard_expansion.py` (36 teste, toate PASS).
- [x] Build + număr pagini actualizat în `tests/web/built-routes.test.js` (101 → 119).
- [x] Validare completă (schema, V2, 554 pytest, `npm run check`, `npm test` 9/9, `npm run build` 119 pagini) + verificare reală de browser (Playwright, desktop 1440/mobil 390) pe 8 pagini noi/afectate — 0 overflow orizontal, main=1/h1=1 peste tot, 0 violări axe.
- [ ] Fresh clone + guvernanță + raport

## 13. Jurnal de decizii

- **Decizie:** nu se leagă PRB-0004/PRB-0006 de exerciții noi. **Motiv:** ambele sunt despre organizarea defensivă (primul/al doilea apărător, protejarea centrului) — conceptual distincte de „sprijin și unghi de pasă" în posesie, chiar dacă principiile lor (`presiune-si-acoperire`, `protejarea-centrului`) sunt deja reale și documentate. **Alternativă respinsă:** construirea a 2-3 exerciții defensive pentru a le lega — respinsă explicit, ar constitui o a doua temă de antrenament. **Efect:** PRB-0004/0006 rămân orfane de exerciții, ca și înainte de acest task — stare neschimbată, nu o regresie.
- **Decizie:** EX-0012 (prima privire după recuperare) rămâne în aceeași temă, nu devine „tranziție" ca temă separată. **Motiv:** decizia exersată e identică cu cea din `principle.progresie-si-sprijin` (progresie vs. sprijin), doar declanșatorul (recuperarea mingii) e nou; `principle.tranzitia-la-castigarea-mingii` e deja canonic și deja parțial reutilizat (EX-0005/SES-0002, prin PRB-0005). **Efect:** întărește o legătură slabă existentă (PRB-0005 avea `assessment_links: []`) fără a extinde scopul tematic.
- **Decizie:** niciun asset vizual nou (SVG/animație). **Motiv:** design freeze activ, deja documentat pentru EX-0001–EX-0005 (`visual_assets: PENDING`); pagina `[id].astro` gestionează deja onest acest caz prin `hasDiagram`/nota „fără diagramă în această versiune". **Efect:** consecvență totală cu convenția existentă, zero risc de a viola `docs/VISUAL_INTERACTIVE_STANDARD.md` prin diagrame produse fără aprobare separată.
- **Descoperire (nu decizie):** `app/src/components/FieldCard.astro` (folosit de `/gold-standard/fise-de-teren`) randa `<TacticalDiagram variant={...} />` necondiționat pentru orice exercițiu, fără gate-ul `hasDiagram` deja prezent în `exercitii/[id].astro` și `sedinte/[id]/mod-teren.astro`. Acesta era un defect latent preexistent — invizibil cât timp au existat doar EX-0001–EX-0005 (toate cu diagramă), dar care arunca o eroare de randare și oprea complet `npm run build` imediat ce a apărut un exercițiu fără diagramă (EX-0006). Reparat minimal, cu exact același tipar deja stabilit în celelalte două fișiere — nu o soluție nouă inventată.
- **Decizie:** extinderea ASM-0001 cu 3 criterii noi (C6–C8), nu câte unul per exercițiu nou. **Motiv:** evaluarea e un instrument de teren, gândit să rămână scurt și utilizabil lângă teren, nu un tabel cu 10 rânduri noi; cele 3 criterii grupează conceptele înrudite (C6: unghi din spate + combinație; C7: coordonare la trei + presiune completă + timing; C8: decizie la recuperare + adaptare la spațiu îngust), la fel cum criteriile existente C1-C5 mapează aproximativ 1:1 pe exercițiile V1. **Efect:** evaluarea rămâne un instrument practic, nu un artefact birocratic.
