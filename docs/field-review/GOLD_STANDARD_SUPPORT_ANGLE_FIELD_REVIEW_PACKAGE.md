# Pachet de Recenzie de Teren — Gold Standard: Sprijinul și unghiul de pasă

**Status Macro:** `GOLD_STANDARD_SUPPORT_ANGLE = READY_FOR_FIELD_PILOT`
**Verdict de audit independent:** `PASS_FIELD_REVIEW_READY` (vezi `reports/audits/gold-standard-support-angle-audit.md`, `TASK-2209`, executat separat de producție)
**Data livrării:** 2026-08-13
**Target:** Antrenori-pedagogi U11, coordonatori metodologici, echipa care va rula primul pilot de teren real

---

## 1. Întrebarea reală de la care pornește acest sistem

Un antrenor U11 real vine cu propoziția: **„Copiii mei nu oferă unghiuri bune de sprijin."**

Acest pachet e testul dacă acel antrenor poate primi, dintr-un singur sistem conectat, tot ce-i trebuie ca să antreneze asta mai bine mâine — nu un articol lung, ci un lanț funcțional: PROBLEMĂ → CONCEPT → DOVADĂ → PERCEPȚIE → DECIZIE → LIMBAJ PENTRU COPIL → SENS PENTRU ANTRENOR → EXERCIȚIU → PROGRESIE → ȘEDINȚĂ → OBSERVAȚIE → INTERVENȚIE → EVALUARE → TRANSFER ÎN MECI → INSTRUMENTE DE TEREN → INTEGRARE WEB.

Acesta e primul subiect ManualFC dus complet prin acest lanț, capăt la capăt. Scopul acestui pachet nu e să demonstreze că sistemul funcționează — asta nu se poate ști fără un pilot real — ci să declare, onest și verificabil, că sistemul e **gata să fie testat** pe teren.

---

## 2. Ce este acest pachet și ce NU este

**ESTE**: o declarație de pregătire pentru pilotare, susținută de un audit independent al integrității conținutului (surse reale, cifre etichetate corect, nicio dogmă, niciun rezultat de pilotare fabricat).

**NU ESTE**:
- O dovadă că exercițiile funcționează cu copii reali. Niciun copil nu a fost observat folosind acest material.
- Un rezultat de eficacitate pedagogică. `FIELD_VALIDATION_PENDING` apare consecvent în `EX-0005`, `ASM-0001` (criteriul C5) și pe pagina `/gold-standard` — nu a fost și nu va fi înlocuit cu date simulate.
- O confirmare că progresia de exerciții (EX-0001→EX-0005, 2v1→3v2→4v4) e optimă — e justificată pedagogic (fiecare pas introduce o informație/decizie nouă, vezi `reports/task-reports/TASK-2204.md`), dar nu e testată empiric.
- O confirmare că numărul de ședințe (2) sau durata lor (75 min) sunt corecte pentru toate contextele — sunt justificate pentru acest conținut specific, nu presupuse dintr-un tipar vechi de „2 ședințe standard".

---

## 3. Harta completă a sistemului

### 3.1 Fundație conceptuală (reutilizată, nu re-derivată)
- `principle-spatiu-si-unghiuri` (VOLUME-02, CH-0202) — `FIELD_REVIEW_READY`
- `principle-progresie-si-sprijin` (VOLUME-02, CH-0203) — `FIELD_REVIEW_READY`
- `docs/gold-standard/CONCEPT_MODEL.md` (TASK-2203) — definiție profesională, model perceptiv/decizional, dimensiune tehnică nouă, taxonomie de erori, model de intervenție

### 3.2 Cercetare
- `docs/gold-standard/GOLD_STANDARD_READINESS_AUDIT.md` (TASK-2201) — matricea de pregătire, clasificare a materialului vechi
- `research/dossiers/gold-standard-support-angle.md` (TASK-2202) — 6 surse noi (`SRC-0108`–`SRC-0113`) + 1 reutilizată (`SRC-0089`), 4 claim-uri noi (`CLM-0101`–`CLM-0104`), toate verificate extern prin CrossRef, re-verificate independent la audit

### 3.3 Exerciții (prima producție reală a acestui tip de entitate)
| ID | Titlu funcțional | Format | Rol în progresie |
|---|---|---|---|
| `EX-0001` | Recunoașterea umbrei defensive | 2v1, opoziție semi-pasivă | Introducere — prima expunere la problemă |
| `EX-0002` | Creează opțiunea sub presiune | 2v1, opoziție activă continuă | Consolidare sub presiune reală |
| `EX-0003` | Primește gata să continui | 2v1, orientare la recepție | Dimensiune tehnică (recepție) |
| `EX-0004` | Sprijin cu doi coechipieri | 3v2, coordonare | Complexitate perceptivă crescută |
| `EX-0005` | Transferul în joc mic | 4v4, reprezentativ | Testul de transfer |

Fișiere: `data/exercises/exercise-*.json`. Fiecare validează contra `schemas/exercise.schema.json` (46 câmpuri obligatorii), fiecare parametru exact etichetat `EXERCISE_SPECIFIC_PARAMETER`.

### 3.4 Ședințe
- `SES-0001` — „Introducere" (75 min: încălzire → EX-0001 → EX-0002 → EX-0003 → reflecție → joc liber)
- `SES-0002` — „Coordonare și transfer" (75 min: recapitulare → EX-0004 → EX-0005 → reflecție și încheiere)

Fișiere: `data/sessions/session-*.json`.

### 3.5 Evaluare
- `ASM-0001` — 5 criterii (câte unul per exercițiu), niveluri calitative pe 3 trepte (nu scoruri numerice), criteriul C5 marchează explicit `FIELD_VALIDATION_PENDING` pentru transferul în meci.

Fișier: `data/assessments/assessment-sprijin-si-unghi-de-pasa.json`.

### 3.6 Instrumente de teren și specificații vizuale
- `docs/gold-standard/FIELD_TOOLS.md` — cardul „Am nevoie acum", grila de observare, matricea de selecție a exercițiului, fișa de progresie/regresie
- `docs/gold-standard/TACTICAL_VISUAL_SPECS.md` — specificații semantice `VIS-EX-0001`–`VIS-EX-0005` (fără niciun fișier grafic real produs — design freeze activ)

### 3.7 Integrare web
- Deep Mode: `/gold-standard`
- Quick Mode: `/gold-standard/rapid`
- Detaliu exercițiu: `/gold-standard/exercitii/[id]` (5 rute statice)
- Detaliu ședință: `/gold-standard/sedinte/[id]` (2 rute statice)

### 3.8 Audit independent
- `reports/audits/gold-standard-support-angle-audit.md` (TASK-2209) — verdict `PASS_FIELD_REVIEW_READY`, 0 constatări critice/majore.

---

## 4. Ce înseamnă „problemă" într-un pilot de teren — trei categorii distincte

Un pilot viitor va genera observații amestecate. Acest pachet fixează dinainte cum se clasifică, ca să nu se confunde o problemă de produs cu una pedagogică sau cu una specifică unui exercițiu — confuzia asta ar duce fie la remedieri greșite, fie la abandonarea unui conținut bun din cauza unei probleme de altă natură.

### 4.1 Problemă de produs
Sistemul nu ajunge la antrenor sau nu poate fi folosit în timp real pe teren.
*Exemple concrete pentru acest subiect:* cardul „Am nevoie acum" cere prea mult timp de citit lângă teren; ruta web `/gold-standard/rapid` nu se încarcă offline/pe conexiune slabă; antrenorul nu găsește exercițiul potrivit din matricea de selecție.
*Nu implică:* nimic despre corectitudinea conceptului tactic sau a exercițiilor în sine.

### 4.2 Problemă pedagogică
Modelul conceptual, perceptiv sau decizional nu corespunde comportamentului real al copiilor de această vârstă.
*Exemple concrete:* taxonomia de erori din `CONCEPT_MODEL.md` §6 nu acoperă un tipar de eroare frecvent observat; copiii nu pot procesa lanțul informație→decizie→mișcare la complexitatea propusă în `EX-0004` (3v2); intervențiile din modelul reutilizat (CH-0404) nu produc schimbarea de comportament așteptată.
*Nu implică:* automat că un exercițiu specific trebuie eliminat — poate fi o problemă de progresie (secvența greșită) sau de complexitate (nivelul greșit), nu de concept.

### 4.3 Problemă de exercițiu
Un exercițiu specific nu produce comportamentul-țintă pentru care a fost proiectat, deși conceptul și pedagogia generală sunt corecte.
*Exemple concrete:* `EX-0002` nu generează presiune reală suficientă (adversarul e prea pasiv chiar „activ"); `EX-0004` (3v2) e prea complex ca al doilea pas după `EX-0001`-`EX-0003` (toate 2v1) — un salt de complexitate nejustificat; timpii segmentelor din `SES-0001`/`SES-0002` nu se potrivesc cu ritmul real al copiilor.
*Nu implică:* nimic despre celelalte exerciții din familie sau despre concept.

**Regulă de aplicare:** o singură observație izolată nu clasifică o problemă în niciuna din cele trei categorii — la fel ca regula din taxonomia de erori a copilului (`CONCEPT_MODEL.md` §6, „nu se afirmă niciodată... pe baza unei singure erori"), aceeași disciplină se aplică observațiilor despre sistem, nu doar despre copii.

---

## 5. Ce NU se poate concluziona dintr-un singur pilot de teren

Chiar și un pilot real, bine documentat, cu un singur grup/echipă, **nu poate**:

1. Demonstra eficacitate cauzală a exercițiilor asupra performanței tactice — lipsește un grup de control și orice comparație.
2. Confirma sau infirma extrapolarea de la populațiile studiate (adulți/U17+ pentru scanare, 7 ani și 12,94 ani pentru intervenție) la exact 10–11 ani — asta ar cere cercetare dedicată, nu observație de teren dintr-un pilot ManualFC.
3. Stabili retenția pe termen lung a comportamentului observat (transferul în meciul următor sau peste o lună) — un pilot de 2 ședințe observă doar transfer imediat, nu retenție.
4. Generaliza la alte grupe de vârstă, alte niveluri de joc, sau alte contexte culturale/de club — eșantionul unui pilot e prea mic și prea specific.
5. Valida sau invalida numărul exact de ședințe (2) sau exercițiile (5) ca fiind „optime" — un singur pilot poate arăta că sunt insuficiente sau prea multe pentru UN grup, nu poate stabili un număr universal corect.
6. Înlocui verificarea bibliografică — dacă o observație de teren pare să contrazică o sursă citată, asta deschide o întrebare de cercetare nouă, nu o revizuire a sursei pe baza unei observații.
7. Servi ca dovadă publicabilă sau de marketing — orice folosire a rezultatelor unui pilot în afara ciclului intern de remediere trebuie să declare explicit limitele de mai sus.

---

## 6. Protocolul minim de colectare pe teren (pentru un pilot viitor, neexecutat încă)

Acest protocol descrie CE ar trebui înregistrat într-un pilot real — nu conține date, deoarece niciun pilot nu a fost rulat.

- **Pentru fiecare ședință**: dacă cele două exerciții planificate au încăput în timpul alocat, folosind grila de observare (`FIELD_TOOLS.md` §2) cu UN singur focalizator per rundă.
- **Pentru fiecare exercițiu**: dacă comportamentul-țintă a apărut (folosind criteriul calitativ din `ASM-0001`, nu un scor numeric), și care dintre erorile din taxonomie (`CONCEPT_MODEL.md` §6) au fost observate, fără a presupune cauza dintr-o singură apariție.
- **Pentru instrumentele de teren**: dacă antrenorul a putut folosi cardul „Am nevoie acum" fără să consulte alt document, cronometrat informal.
- **Pentru transfer**: observație directă (nu chestionar retrospectiv) dacă comportamentul din exerciții a apărut în `EX-0005` (jocul reprezentativ) și, separat, într-un meci real ulterior — cele două rămân observații distincte, nu combinate într-un singur verdict.

Rezultatele acestui protocol, odată colectate, alimentează matricea de decizie de mai jos — nu sunt anticipate sau simulate aici.

---

## 7. Matricea de decizie KEEP / MODIFY / REMOVE / RESEARCH_REQUIRED

Matricea de mai jos definește **criteriile** care ar declanșa fiecare verdict, per componentă — de aplicat după un pilot real, nu completată cu rezultate fabricate acum.

| Componentă | KEEP dacă... | MODIFY dacă... | REMOVE dacă... | RESEARCH_REQUIRED dacă... |
|---|---|---|---|---|
| Concept model (`CONCEPT_MODEL.md`) | Taxonomia de erori acoperă majoritatea observațiilor reale, modelul decizional corespunde comportamentului copiilor | Taxonomia lipsește tipare frecvente observate, dar structura generală rămâne validă | — (fundația e deja `FIELD_REVIEW_READY` din VOLUME-02, nu se elimină) | O observație repetată contrazice direct un claim citat (`CLM-0101`–`CLM-0104`) |
| `EX-0001`–`EX-0005` (individual) | Produce comportamentul-țintă la majoritatea copiilor în 2-3 runde | Comportamentul apare, dar cu dificultate/timp excesiv — ajustare de constrângeri sau complexitate | Comportamentul nu apare deloc, indiferent de ajustări repetate | Copiii reacționează neașteptat la o intervenție bazată pe un claim specific (ex. focus atențional extern, `CLM-0102`) |
| Progresia (secvența EX-0001→EX-0005) | Fiecare pas e realizabil după cel anterior, fără salt de complexitate resimțit | Un pas anume (ex. `EX-0004`, 3v2) creează un salt prea mare — se inserează un pas intermediar | — (progresia servește un scop pedagogic documentat, nu se elimină în bloc) | — |
| Ședințele (`SES-0001`/`SES-0002`) | Timpii segmentelor corespund ritmului real, ambele exerciții încap | Rebalansare a minutelor între segmente | — | — |
| Evaluarea (`ASM-0001`) | Criteriile calitative disting clar între nivele de comportament | Un criteriu e ambiguu sau greu de observat live — reformulare | Un criteriu nu corespunde deloc unui comportament observabil | — |
| Instrumente de teren (`FIELD_TOOLS.md`) | Antrenorul le folosește fără pregătire suplimentară | Necesită reformulare pentru claritate sub presiune de teren | — | — |
| Specificații vizuale (`TACTICAL_VISUAL_SPECS.md`) | Antrenorii le înțeleg din descrierea text | Necesită clarificare a punctului de decizie sau a legendei | — | Producția vizuală reală rămâne o decizie separată de design, în afara acestui pilot |

**Regulă transversală:** niciun verdict `REMOVE` nu se aplică fundației conceptuale reutilizate din VOLUME-02 (deja `FIELD_REVIEW_READY` printr-un proces separat) — doar componentelor noi produse în acest ciclu Gold Standard (`TASK-2203`–`TASK-2207`).

---

## 8. Verdict de aprobare

- Readiness audit (`TASK-2201`): `DONE`.
- Cercetare (`TASK-2202`): `DONE`, 6 surse noi + 1 reutilizată, toate verificate extern.
- Concept (`TASK-2203`): `DONE`.
- Exerciții (`TASK-2204`): `DONE`, 5 instanțe, prima producție reală a acestui tip de entitate.
- Ședințe (`TASK-2205`): `DONE`, 2 instanțe.
- Evaluare (`TASK-2206`): `DONE`, 1 instanță.
- Instrumente de teren + specificații vizuale (`TASK-2207`): `DONE`.
- Integrare web (`TASK-2208`): `DONE`, 9 rute, design freeze intact.
- Audit independent (`TASK-2209`): `DONE`, verdict `PASS_FIELD_REVIEW_READY` — vezi `reports/audits/gold-standard-support-angle-audit.md`.
- Validare Proiect & Conținut: `VALID: 0 erori` (verifică integritatea structurală; adevărul conținutului e stabilit prin verificarea bibliografică externă documentată în auditul independent).

**Stare Macro: `GOLD_STANDARD_SUPPORT_ANGLE = READY_FOR_FIELD_PILOT`.**

Acest verdict înseamnă că sistemul e gata să fie testat cu copii reali — nu că a fost testat. Primul pilot real, urmat de aplicarea matricei din secțiunea 7 pe date reale (nu simulate), rămâne următorul pas, în afara scopului acestei bucle autonome.
