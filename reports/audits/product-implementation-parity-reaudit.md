# Re-audit independent — paritate implementare produs (TASK-2402)

**Domeniu:** re-verificare independentă a `TASK-2401` (audit + prima rundă de remediere, comisă în `8d213d4`/`0c7ec97`), conform DEC-0040 (audit și remediere nu se combină; auditorul nu a scris materialul auditat).
**Executat de:** subagent independent, fără nicio scriere în cod/date. Toate constatările verificate direct pe repository, nu preluate din raportul TASK-2401.
**HEAD la momentul re-auditului:** `0c7ec97`. Working tree: aceeași stare „murdară" (design-freeze) documentată de TASK-2401, neschimbată.

---

## Verdict executiv

**`REPAIR_REQUIRED`** — dintr-un singur defect blocant, precis delimitat mai jos. Toate celelalte constatări ale TASK-2401 s-au confirmat exacte prin verificare independentă (inventar, remediere comisă, design freeze, teste, validatoare). Defectul găsit nu a fost inventat de acest re-audit — el există deja în working tree-ul curent și a fost pur și simplu **raportat greșit ca reparat** de TASK-2401.

**Ce s-a găsit:** butonul hero de pe homepage (`app/src/components/HomepageHero.astro`, linia 16), cel mai proeminent CTA de pe întreaga pagină ("Am nevoie acum"), duce încă la ruta fixture stricată `/probleme/lipsa-unghi-de-pasa` — exact ruta pe care TASK-2401 a documentat-o inițial ca fiind critică. Raportul TASK-2401 (§4 și §5) și `DEC-0048` afirmă explicit că `index.astro` a primit „remedieri echivalente...funcționale acum în build-ul local" — afirmație **falsă**, verificată prin build propriu (`npm run build` din rădăcină, 72 pagini, 0 erori) și inspecția HTML-ului generat (`dist/web/index.html`).

---

## 1. Tabel de verificare independentă

| # | Constatare din TASK-2401 | Verificare independentă | Rezultat |
|---|---|---|---|
| 1 | Inventar canonic: 25 capitole (5+8+6+6), 25 principii, 5 exerciții GS, 2 ședințe GS, 1 evaluare GS | Numărat direct: `content/volume-0{1-4}/*.mdx` → 5,8,6,6 = 25; `data/principles/principle-*.json` → 25 (26 fișiere minus README); `data/exercises` → 5; `data/sessions` → 2; `data/assessments` → 1 | **CONFIRMAT identic** |
| 2 | `getPrimaryNavigation()` reparată, consumată direct/nefiltrat de `AppHeader.astro` din `git HEAD` | Citit `git show HEAD:...AppHeader.astro` — confirmă `{navItems.map(...)}` fără niciun filtru; citit `content-bridge.ts` curent — hrefs sunt `/principii`, `/gold-standard/rapid`, `/gold-standard`, toate rute reale, confirmate în build (72 pagini, 0 erori) | **CONFIRMAT** — remedierea pentru `git clone` curat e reală și corectă |
| 3 | Working tree `AppHeader.astro` filtrează prin `preferredLabels`, divergență preexistentă, nu cauzată de TASK-2401 | Citit fișierul working tree — filtrare pe `preferredLabels` (`/incepe-aici`, `/principii`, `/gold-standard/rapid`, `/gold-standard`), design complet diferit de HEAD (logo, meniu mobil) | **CONFIRMAT** — divergența e reală și structural diferită de HEAD, consistent cu narațiunea unui redesign necomis |
| 4 | `/principii` index nou, 25 principii reale, fixture exclus | Citit `principii/index.astro` — folosește `getCanonicalProductionContent(getAllPrinciples())`; build → `dist/web/principii/index.html` conține exact 25 linkuri reale (`/principii/adaptarea-sarcinii-u11` ... `/principii/variabilitatea-dezvoltarii-u11`), zero referință la fixture-ul `orientare-corporala-scanare` | **CONFIRMAT identic** |
| 5 | Cross-linkuri volum→volum consistente (V01→V02, V02→V01+V03, V03→V02+V04, V04→V03) + fiecare → `/principii` + `/gold-standard` | Citit diff-urile `8d213d4` pentru toate cele 4 `volum/0N/index.astro` | **CONFIRMAT identic**, lanț fără verigi lipsă |
| 6 | Design freeze: commit-ul remedierii nu atinge niciun `<style>` din fișiere frozen existente | `git show 8d213d4 --stat` → doar `content-bridge.ts`, `principii/index.astro` (fișier nou), 4× `volum/0N/index.astro` (adăugări mici de `<nav>`/`<p>` + reguli CSS minime folosind tokene existente), `test_task2208_web_integration.py`. Niciun fișier din lista frozen (`AppHeader`, `AppFooter`, `index.astro`, `incepe-aici.astro`, etc.) apare în commit | **CONFIRMAT** — zero atingere a fișierelor frozen în commit |
| 7 | `git status` curent confirmă fișierele frozen încă necomise/murdare, neschimbate de TASK-2401 | `git status --short` la începutul acestei sesiuni — toate cele 16 fișiere din lista frozen apar `M` sau, pt. cele noi (`HomepageHero.astro` etc.), `??`, exact ca înainte | **CONFIRMAT** |
| 8 | Teste + validatoare: toate PASS | Rulate direct: `python -m unittest discover` → 417/417 PASS; `validate_content.py --strict` → 0 erori; `validate_project.py` → 0 erori; `generate_task_registry.py --check` → reproductibil | **CONFIRMAT identic** |
| 9 | `/exercitii/[slug]`, `/probleme/[slug]` rămân doar pe fixture-uri | Citit `content-bridge.ts`: `getAllExercises()`/`getAllProblems()` citesc exclusiv `data/fixtures/*.json` | **CONFIRMAT** |
| 10 | `/design-system` etichetat public ca resursă, e de fapt un lab intern | Citit `design-system.astro`: `title="Brand / UI Lab"`, descriere „Laborator intern pentru identitatea și componentele ManualFC"; `AppFooter.astro` îl etichetează „Metodologie și resurse"; `AppHeader.astro` (working tree) îl etichetează „Resurse" | **CONFIRMAT** |
| 11 | „10 din 15 categorii taxonomie fără conținut" | Numărat direct `data/taxonomy/registry.json` → **16** categorii declarate, nu 15. Din ele, 3 au rută de producție reală (`principii-joc`→`/principii`, `exercitii`→fixture, `probleme-teren`→fixture) și **13** nu au nicio rută/conținut — lista de 13 nume enumerată explicit în raportul original e corectă, dar numărul sumar „10 din 15" e greșit pe ambele cifre | **PARȚIAL EXACT** — vezi §3, defect minor de acuratețe, nu de substanță |
| 12 | Homepage/„Începe aici" working tree ar avea „remedieri echivalente...funcționale acum în build-ul local" (raport §4/§5, `DEC-0048`) | Build propriu + inspecție `dist/web/index.html`: CTA-ul principal din hero (`HomepageHero.astro:16`) duce încă la `/probleme/lipsa-unghi-de-pasa` (bannerul „⚠️ DEVELOPMENT FIXTURE" confirmat pe pagina țintă). `incepe-aici.astro` e într-adevăr complet reparat; restul homepage-ului (secțiunea „Am nevoie acum" din `index.astro` propriu-zis) e reparat. Doar componenta hero a rămas nereparată | **CONTRAZIS — vezi §2, defectul blocant al acestui re-audit** |

---

## 2. Defectul blocant: CTA-ul hero al homepage-ului rămâne pe ruta fixture stricată

**Fișier:** `app/src/components/HomepageHero.astro`, linia 16 (componentă nouă, necomisă, parte a redesign-ului vizual în lucru).

```html
<a class="button hero-secondary" href="/probleme/lipsa-unghi-de-pasa">Am nevoie acum <span aria-hidden="true">◷</span></a>
```

Verificat prin build propriu (`npm run build` din `E:\ManualFC`, 72 pagini, 0 erori) și inspecția `dist/web/index.html`: linkul apare exact așa în HTML-ul livrat, iar `/probleme/lipsa-unghi-de-pasa` afișează bannerul `⚠️ DEVELOPMENT FIXTURE: Această pagină este generată din date neutre de dezvoltare...`.

**De ce contează:** acest buton e primul element interactiv vizibil pe homepage (secțiunea hero, deasupra fold-ului), cu eticheta identică „Am nevoie acum" ca și elementul din antet (corect reparat, duce la `/gold-standard/rapid`) și ca secțiunea "mode-split" mai jos pe aceeași pagină (`index.astro:27`, de asemenea corect, duce la `/gold-standard/rapid`). Rezultatul: **doi butoni cu exact aceeași etichetă, pe aceeași pagină, duc la destinații diferite** — unul la conținutul real Gold Standard Quick Mode, celălalt la o pagină de dezvoltare marcată explicit ca atare. Pentru un antrenor care testează site-ul azi (working tree, nu `git HEAD`), primul click pe „Am nevoie acum" — cel mai vizibil, din hero — e exact defectul critic original pe care întregul audit TASK-2401 l-a documentat.

**De ce e o problemă de raportare, nu doar un bug rezidual:** raportul TASK-2401 (§4: „Working tree-ul curent conține și remedieri echivalente în AppHeader.astro, AppFooter.astro, incepe-aici.astro, index.astro (etichete/hreffuri corectate) — funcționale acum în build-ul local") și `DEC-0048` afirmă explicit că `index.astro` a fost reparat funcțional în working tree. Verificarea independentă arată că afirmația e parțial falsă: `index.astro` propriu-zis a fost reparat corect (secțiunea "mode-split"), dar componenta `HomepageHero.astro` pe care o importă (linia 13 din `index.astro`) — introdusă separat, tot necomisă — a rămas nereparată. TASK-2401 nu a inventat conținut și nu a mințit deliberat, dar a raportat ca „funcțional" ceva ce build-ul propriu arată clar că nu e.

**Severitate:** Majoră. Nu e critică în sensul strict al constatării originale (antetul global — cel mai des vizibil element — e corect reparat, iar a doua instanță a CTA-ului de pe aceeași pagină e corectă), dar e un defect real, reproductibil, prezent chiar acum în orice build local al working tree-ului, pe cel mai proeminent element al homepage-ului, și contrazice direct o afirmație explicită de „funcțional" din raportul remedierii anterioare.

---

## 3. Constatare secundară, minoră: eroare aritmetică în inventarul taxonomiei

Raportul TASK-2401 afirmă „15 categorii declarate" și „10 din 15 categorii...nu au conținut", dar enumeră explicit 13 nume de categorii fără conținut. Numărătoare independentă pe `data/taxonomy/registry.json`: **16** categorii declarate (nu 15), din care **13** nu au rută/conținut de producție (nu 10) — coincide exact cu lista de 13 nume deja enumerată în raportul original. Concluzia calitativă a raportului (aceste categorii sunt arhitectură aspirațională nerealizată, corect neconstruite) rămâne validă și corect argumentată; doar cifrele sumar („15", „10 din 15") sunt greșite aritmetic față de propria listă enumerată alăturat. Nu schimbă niciun verdict, dar afectează încrederea în acuratețea numerică a raportului.

---

## 4. Confirmări explicite cerute de mandat

- **Corectitudinea reparării navigării pentru `git clone` curat:** **CONFIRMATĂ.** `AppHeader.astro` din `git HEAD` consumă `getPrimaryNavigation()` direct și fără filtrare; funcția întoarce acum exclusiv rute reale (`/principii`, `/gold-standard/rapid`, `/gold-standard`), toate verificate 200/randate corect în build. Un `git clone` curat + `npm run build` produce o navigare globală funcțională spre conținut real.
- **Corectitudinea reparării pentru working tree-ul curent:** **PARȚIAL CONFIRMATĂ, CU EXCEPȚIA §2.** Antetul (`AppHeader.astro`), subsolul (`AppFooter.astro`) și „Începe aici" (`incepe-aici.astro`) din working tree sunt corect reparate — verificat direct în fiecare fișier și în HTML-ul generat. Homepage-ul (`index.astro`) e reparat parțial: secțiunea principală „mode-split" e corectă, dar componenta hero importată (`HomepageHero.astro`) nu e, contrazicând afirmația explicită de „funcțional" din raportul TASK-2401/`DEC-0048`.
- **Conformitate design freeze (zero modificări vizuale/CSS în commit):** **CONFIRMATĂ.** `8d213d4` conține doar `content-bridge.ts` (logică/date), `principii/index.astro` (fișier nou, cu propriul `<style>` minimal folosind exclusiv tokene CSS existente — necesar pentru ca pagina nouă să fie utilizabilă, nu o modificare a unui fișier frozen existent), 4 fișiere `volum/0N/index.astro` (adăugări mici de `<nav>`/`<p>` + reguli CSS folosind tokene existente, nu introduc identitate vizuală nouă), și fișierul de test. Niciunul din fișierele frozen listate (`AppHeader`, `AppFooter`, `index.astro`, `incepe-aici.astro`, `ChildMessage`, `CoachMessage`, `EvidenceBadge`, `QuickModePattern`, `BaseLayout`, `design-system.astro`, `principii/[slug].astro`, CSS-urile globale, `astro.config.mjs`, `config/visual-tokens.json`) apare în commit. `git status --short` confirmă toate rămân necomise, exact ca înainte de TASK-2401.
- **Stare verde teste/validatoare:** **CONFIRMATĂ.** 417/417 teste PASS, `validate_content.py --strict` 0 erori, `validate_project.py` 0 erori, `generate_task_registry.py --check` reproductibil.
- **Onestitatea listei de constatări reziduale:** **CONFIRMATĂ ca fond, cu o corecție aritmetică minoră** (§3) și **o afirmație de „funcțional" invalidată** (§2) — raportul nu a minimizat deliberat scopul rezidual (a documentat corect divergența HEAD/working-tree ca majoră, nerezolvată), dar a supra-raportat starea de finalizare a reparării homepage-ului în working tree.

---

## 5. Constatări pe severitate (acest re-audit)

### Majore
1. **CTA-ul hero al homepage-ului (`HomepageHero.astro:16`) duce încă la ruta fixture `/probleme/lipsa-unghi-de-pasa`**, contrazicând direct afirmația explicită de reparare „funcțională" din raportul TASK-2401 și `DEC-0048`. Reproductibil prin build propriu. **Acesta e defectul care determină verdictul `REPAIR_REQUIRED`.**

### Minore
2. Eroare aritmetică în raportul TASK-2401: „15 categorii, 10 fără conținut" ar trebui să fie „16 categorii, 13 fără conținut" — lista de nume enumerată explicit e deja corectă, doar cifrele-sumar sunt greșite.

### Reziduu acceptat (neschimbat, corect clasificat de TASK-2401, nu blochează)
- Divergența HEAD/working-tree pentru fișierele design-freeze — documentată corect ca majoră, necesită decizie explicită a utilizatorului, în afara scopului de remediere autonomă.
- `/design-system` etichetat public „Resurse"/„Metodologie și resurse" — moderat, opțional.
- `/exercitii/[slug]`, `/probleme/[slug]` rămân doar pe fixture-uri — sistemic, documentat în DEC-0044, în afara scopului minim.
- 13 categorii taxonomie aspiraționale fără conținut — corect neconstruite, nu e defect.

---

## 6. Verdict final

**`REPAIR_REQUIRED`**

**Ce blochează:** un singur defect, precis delimitat — `app/src/components/HomepageHero.astro` linia 16, `href="/probleme/lipsa-unghi-de-pasa"` trebuie schimbat la `/gold-standard/rapid` (aceeași destinație folosită corect de restul site-ului pentru eticheta „Am nevoie acum"). E o modificare de o linie, de tip hreff, în același spirit non-vizual ca restul remedierii `8d213d4` — nu implică nicio decizie despre design freeze, pentru că fișierul e deja necomis și deja în lista de „remedieri echivalente" pe care TASK-2401 pretinde (incorect) că le-a aplicat complet.

**Ce NU blochează (reziduu acceptat, consistent cu clasificarea TASK-2401):** divergența HEAD/working-tree pentru fișierele frozen (necesită decizie explicită a utilizatorului), etichetarea `/design-system`, migrarea `/exercitii`/`/probleme` de pe fixture, cele 13 categorii de taxonomie aspirațională, eroarea aritmetică minoră din §3 (corecție editorială, nu repară produsul).

**Notă asupra independenței acestui audit:** nicio linie de cod sau conținut nu a fost modificată în timpul acestui re-audit. `npm run build` a fost rulat o singură dată din rădăcină, fără `npm install`/`ci`. Niciun server de dezvoltare nu a fost lăsat pornit.
