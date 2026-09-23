# TASK-3721 — Integrarea fluxului de lucru al antrenorului în toate sistemele de conținut

## 1. Titlu și scop

Rezultatul observabil: cele patru sisteme de conținut ManualFC (teme/metodologie, exerciții/ședințe, scripturi de comunicare, planificare de sezon) formează un flux coerent — un antrenor poate porni de la o problemă observată și ajunge natural la înțelegere, acțiune, script, plan de sezon, reflecție și revenire — fără fundături, fără sisteme izolate, fără etichete neclare.

## 2. Context pentru un cititor nou

- Repository canonic: `E:\ManualFC-clean`. Repository legacy `E:\ManualFC` — NU se atinge.
- Cele patru sisteme există deja, complete și validate: teme (`TASK-3712`/`TASK-3718`), scripturi (`TASK-3719`), planuri de sezon (`TASK-3720`). Produsul e stabil tehnic și public. Pilotarea reală (`TASK-3714`) rămâne `BLOCKED`.
- Acest task NU adaugă un al cincilea pilon de conținut — integrează ce există deja.

## 3. Harta fluxului actual al antrenorului (constatări verificate direct, nu presupuse)

**Navigare globală (`AppHeader.astro`):** `getPrimaryNavigation()` returnează 7 intrări (inclusiv `/cauta`), dar `preferredLabels` din `AppHeader.astro` filtrează la doar 5 (`/incepe-aici`, `/volum`, `/principii`, `/rezolva-pe-teren`, `/gold-standard`) + `/spatiul-meu` adăugat manual. **`/cauta` (Caută) e eliminat silențios din antet, deși există deja în `getPrimaryNavigation()`.** `/aparare` (tema 2), `/scripturi`, `/planuri-de-sezon` nu sunt deloc în `getPrimaryNavigation()`. `AppFooter.astro` are propria listă hardcodată, complet duplicată și cu aceleași lipsuri, plus fără `/spatiul-meu`.

**Pagina principală (`index.astro`) și onboarding (`/incepe-aici`):** oferă doar două „moduri" (Vreau să învăț → `/principii`/`/incepe-aici`; Rezolvă pe teren → `/rezolva-pe-teren`), gândite înainte de a exista scripturile sau planificarea de sezon. Niciuna nu menționează cele două pillere mai noi, nici tema a doua, nici Spațiul meu.

**Pagina de problemă (`rezolva-pe-teren/[slug].astro`):** fiecare problemă are `related_principles` în date, dar pagina NU randează niciodată acest câmp — zero legătură vizibilă problemă→principiu. De asemenea, zero legătură problemă→scripturi (nu există niciun `getScriptsForProblem`).

**Pagina de exercițiu și de ședință:** câmpul `problem_being_solved` există în schema exercițiului dar nu e randat niciunde pe pagină; nu există nicio legătură înapoi către problema reală din motorul de decizie (`PRB-XXXX`) de la niciuna dintre cele două pagini.

**Reflecția de închidere a ședinței:** secțiunea „Reflecție de închidere" din pagina de ședință afișează întrebările canonice ca text static, dar NU leagă deloc la instrumentul interactiv `/spatiul-meu/reflectie?sesiune=SES-XXXX` — deși acel instrument acceptă deja parametrul `sesiune` din URL. Tranziția „reflectă după ședință" e efectiv ruptă.

**Căutarea unificată (`/cauta`):** `types` se calculează deja dinamic din `getDiscoveryIndex()`, deci SCRIPT și PLAN DE SEZON apar deja ca opțiuni de filtru — dar logica `playerOk`/`timeOk` din scriptul de filtrare exclude silențios orice element fără `playersMin`/`minutes` (adică toate scripturile și toate planurile de sezon) de îndată ce antrenorul alege un filtru de Efectiv sau Timp diferit de „Toate" — o fundătură reală de căutare. Descrierea paginii și placeholder-ul mai menționează doar „probleme, principii, exerciții, ședințe, evaluări și capitole", nu cele patru sisteme reale.

**Spațiul meu:** listele Salvate/Favorite/Vizitate recent randează doar titlu+link, fără nicio etichetă de tip — un antrenor nu poate distinge dintr-o privire dacă un element salvat e un exercițiu, un script sau un plan de sezon. Textele de stare goală („Nimic încă.") sunt corecte dar minimale, nu ghidează spre acțiune.

**Confirmat funcțional și NEATINS:** `getDiscoveryIndex()` acoperă deja toate cele 4 sisteme (adăugat în `TASK-3719`/`TASK-3720`); `CanonicalKind`/local-first save-favorite-recent acoperă deja toate cele 4 sisteme; blocurile „Scripturi relevante"/„Planuri de sezon relevante" există deja pe exerciții, ședințe, principii (parțial); paginile de script și de plan au deja legături complete înapoi spre principii/probleme/exerciții/ședințe.

## 4. Rezultatul verificabil

- Antrenorul poate parcurge complet: problemă → principiu → exercițiu/ședință → script → plan de sezon → reflecție → salvare/continuare → revenire, din orice punct de intrare.
- Niciun sistem de conținut izolat din navigarea globală.
- Căutarea unificată nu exclude silențios niciun sistem.
- Spațiul meu arată clar la ce sistem aparține fiecare element salvat.

## 5. Domeniu și non-obiective

**În scop:** legături contextuale lipsă, navigare globală, căutare, Spațiul meu, stări goale, ghidare „ce fac acum".

**Non-obiective explicite:** niciun cont, bază de date, analitice, funcții sociale, plăți, conturi de jucători, personalizare speculativă, arhitectură multi-vârstă, redesign nelegat de flux. Niciun conținut existent al celor 4 sisteme nu se modifică — doar cablarea dintre ele.

## 6. Fișiere și module afectate

**Modificate:** `app/src/lib/content-bridge.ts` (getteri noi de legătură inversă), `app/src/components/AppHeader.astro`, `app/src/components/AppFooter.astro`, `app/src/pages/index.astro`, `app/src/pages/incepe-aici.astro`, `app/src/pages/rezolva-pe-teren/[slug].astro`, `app/src/pages/gold-standard/exercitii/[id].astro`, `app/src/pages/gold-standard/sedinte/[id].astro`, `app/src/pages/principii/[slug].astro`, `app/src/pages/planuri-de-sezon/[id].astro`, `app/src/pages/cauta.astro`, `app/src/pages/spatiul-meu/index.astro`, `app/src/lib/coach-state.ts` (etichete de tip).

**Noi:** `tests/test_task3721_workflow_integration.py`, teste web noi în `tests/web/`.

## 7. Model pedagogic

Fiecare legătură nouă e derivată din date reale deja existente (relații explicite `related_*_ids`), nu dintr-un algoritm de recomandare sau popularitate — consecvent cu `computeNextAction` (deterministă, nu generată liber). Etichetele de tip și titlurile rămân în română naturală, consecventă cu vocea editorială existentă. Nicio pretenție de validare de teren nu se introduce.

## 8. Pași de implementare

1. `content-bridge.ts`: `getScriptsForProblem`, `getProblemsForExercise`, `getProblemsForSession`, `getProblemsForPrinciple`, etichete de tip canonice.
2. Pagina de problemă: secțiuni „Principii legate" și „Scripturi relevante".
3. Paginile de exercițiu/ședință: secțiune „Problema pe care o rezolvă" cu legătură reală.
4. Pagina de ședință: CTA „Reflectează după ședință →" spre `/spatiul-meu/reflectie?sesiune=`.
5. Pagina de plan de sezon: CTA de reflecție per microciclu.
6. Pagina de principiu: legătură înapoi spre probleme.
7. Navigare: repară `/cauta` în antet, adaugă `/aparare`/`/scripturi`/`/planuri-de-sezon` în `getPrimaryNavigation()`, antet și subsol; unifică subsolul să consume aceeași sursă.
8. Homepage + onboarding: a treia intrare/mențiune pentru planificare de sezon și scripturi.
9. `/cauta`: repară filtrele Efectiv/Timp să nu excludă scripturi/planuri; actualizează copy.
10. Spațiul meu: etichete de tip pe elementele salvate/favorite/recente; stări goale mai acționabile.
11. Teste noi + validare completă + fresh clone + guvernanță + raport.

## 9. Validare și acceptare

Toate comenzile din task: validatoare de conținut, `npm run check`, `npm test`, `pytest`, build, browser+axe la 1440/390px, sitemap, offline, `git fsck --full`, fresh clone.

## 10. Progres

- [x] Harta fluxului actual, constatări verificate
- [ ] Getteri noi de legătură inversă
- [ ] Legături contextuale noi pe problemă/exercițiu/ședință/principiu/plan
- [ ] Navigare globală reparată și unificată
- [ ] Homepage/onboarding actualizate
- [ ] Căutare reparată
- [ ] Spațiul meu — etichete de tip + stări goale
- [ ] Teste noi + validare completă + fresh clone + guvernanță

## 11. Jurnal de decizii

1. **Decizie:** unific sursa navigării (antet + subsol consumă `getPrimaryNavigation()`), nu mențin liste hardcodate duplicate. **Motiv:** task-ul avertizează explicit despre „trasee de descoperire duplicate"; o singură sursă elimină riscul de divergență viitoare. **Data:** 2026-09-23.
2. **Decizie:** legăturile problemă↔principiu↔script folosesc exclusiv date deja declarate (`related_principles`, `related_problem_ids`), nu un motor de recomandare nou. **Motiv:** cerință explicită de a distinge relevanța de popularitate și de a evita „recomandat pentru tine" nefundamentat. **Data:** 2026-09-23.
3. **Decizie:** CTA-ul de reflecție per microciclu de plan de sezon leagă la sesiunea principală a microciclului, nu la toate sesiunile — păstrează un singur pas următor clar, nu o listă ambiguă. **Data:** 2026-09-23.

## 12. Rezultat și retrospectivă

_(completat la finalul taskului)_
