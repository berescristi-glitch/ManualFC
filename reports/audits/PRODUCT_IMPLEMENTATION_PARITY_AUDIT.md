# Audit de paritate implementare — produs canonic vs. produs web real

**Domeniu:** Întreaga platformă web ManualFC (VOLUME-01–04, cele 25 de principii, Gold Standard „Sprijinul și unghiul de pasă", integrarea web).
**HEAD la începutul auditului:** `a039f94` (PHASE-23/TASK-2301). **HEAD după prima rundă de remediere:** `8d213d4`.
**Motivație:** suspiciunea explicită a utilizatorului că repository-ul conține substanțial mai multă informație cercetată/documentată/validată decât e efectiv disponibilă în produsul web real. **Constatare: suspiciunea era corectă și severă.**

---

## VERDICT EXECUTIV

Conținutul canonic (25 de capitole în 4 volume, 25 de principii de producție, sistemul Gold Standard complet — concept, 5 exerciții, 2 ședințe, 1 evaluare, instrumente de teren) **există și e corect**, dar **navigarea primară a site-ului nu ducea la niciunul dintre ele**. Homepage-ul, „Începe aici" și antetul global al site-ului (prezent pe fiecare pagină) rutau exclusiv către trei rute fixture de dezvoltare (marcate explicit „⚠️ DEVELOPMENT FIXTURE") plus un singur principiu real. Niciunul dintre cele 4 volume, niciunul dintre celelalte 24 de principii, și întregul sistem Gold Standard erau **rute orfane** — accesibile doar cunoscând URL-ul exact.

O a doua constatare, descoperită abia în timpul remedierii: **fișierele „design freeze" (antet, subsol, homepage, „Începe aici") au o versiune complet diferită și mult mai veche în `git HEAD`** față de ce rulează efectiv în working tree-ul curent — o remediere/redesign vizual în lucru, necomis niciodată, care nu poate fi atinsă fără a încălca politica de design freeze. Asta înseamnă că un `git clone` curat produce un produs și mai deconectat de conținutul real decât ce am testat inițial în working tree.

**Prima rundă de remediere (acest task) a rezolvat gap-ul CRITIC de navigare la nivelul datelor** (funcția `getPrimaryNavigation()`, care alimentează direct antetul din `git HEAD` fără filtrare) și a adăugat un index real de principii + cross-linkuri între volume — toate sigure de comis. Gap-urile rămase, inclusiv divergența HEAD/working-tree, sunt documentate mai jos ca lucru rezidual.

---

## 1. Inventarul canonic (ce deține ManualFC)

| Tip entitate | Număr | Locație |
|---|---|---|
| Volume | 4 (VOLUME-01–04) | `content/volume-0{1-4}/*.mdx` |
| Capitole | 25 (5+8+6+6) | idem, `<Content />` randat integral pe rută |
| Principii de producție | 25 | `data/principles/principle-*.json` |
| Exerciții Gold Standard | 5 (EX-0001–EX-0005) | `data/exercises/*.json` |
| Ședințe Gold Standard | 2 (SES-0001–SES-0002) | `data/sessions/*.json` |
| Evaluare Gold Standard | 1 (ASM-0001) | `data/assessments/*.json` |
| Instrumente de teren Gold Standard | 4 | `docs/gold-standard/FIELD_TOOLS.md` |
| Specificații vizuale tactice | 5 (VIS-EX-0001–0005) | `docs/gold-standard/TACTICAL_VISUAL_SPECS.md` |
| Probleme (entitate `Problem`) | 0 reale, 1 fixture | `data/fixtures/problems.json` |
| Exerciții „vechi" (schema legacy) | 0 reale, 1 fixture | `data/fixtures/exercises.json` |
| Categorii taxonomie | 15 declarate | `data/taxonomy/registry.json` |

---

## 2. Clasificare produs-facing vs. intern

- **PRODUCT_FACING_REQUIRED, deja implementat corect:** cele 25 de capitole (randare MDX integrală, confirmat pentru toate cele 4 volume), toate cele 5 componente Gold Standard (concept, exerciții, ședințe, evaluare, instrumente de teren — evaluarea apare confirmat pe `/gold-standard`).
- **PRODUCT_FACING_REQUIRED, NEIMPLEMENTAT înainte de remediere:** index de principii (0 → acum 1, vezi §4), cross-linkuri volum→volum și volum→Gold Standard (0 → acum prezente).
- **INTERNAL_ONLY_BUT_LABELED_AS_RESOURCE:** `/design-system` — un „Brand/UI Lab" intern (showcase de componente/tokens), etichetat global „Resurse" în antet și subsol, ceea ce induce în eroare un antrenor care se așteaptă la resurse de coaching.
- **DEVELOPMENT_FIXTURE, corect etichetat static dar incorect legat din navigarea primară:** `/probleme/lipsa-unghi-de-pasa`, `/exercitii/2v1-unghi-de-suport`, `/principii/orientare-corporala-scanare` — toate afișează bannerul de avertizare „DEVELOPMENT FIXTURE", dar erau exact rutele către care duceau CTA-urile principale ale site-ului.
- **NOT_YET_CANONICAL (categorii taxonomie fără conținut):** 10 din cele 15 categorii din `data/taxonomy/registry.json` (`copilul-10-11`, `antrenorul-pedagog`, `perceptie-decizie`, `tehnica-context`, `motricitate`, `psihologie`, `comunicare`, `sedinte`, `evaluare`, `safeguarding`, `parinti`, `resurse`, `metodologie-surse`) nu au nicio rută corespunzătoare și nicio entitate de producție dedicată — taxonomia descrie o arhitectură țintă aspirațională, nu conținut existent nerandat. Construirea a 10+ pagini-hub goale ar fi infrastructură nejustificată, nu expunerea unui conținut existent — clasificat explicit în afara scopului acestei remedieri.

---

## 3. Constatarea centrală: navigarea globală nu ducea la niciun conținut real

Verificat static și live (server dev pe `localhost:4321`/`4322`):

| Element de navigare | Ținta înainte de remediere | Verdict |
|---|---|---|
| Antet global, „Principii"/„Învață" (pe fiecare pagină) | `/principii/orientare-corporala-scanare` | **Fixture** (`data/fixtures/principles.json`), nu unul din cele 25 de principii reale |
| Antet global, „Am nevoie acum" | `/probleme/lipsa-unghi-de-pasa` | **Fixture**, banner explicit de avertizare |
| Antet global, „Exerciții" | `/exercitii/2v1-unghi-de-suport` | **Fixture**, banner explicit de avertizare |
| Homepage, CTA „Am nevoie acum" | `/probleme/lipsa-unghi-de-pasa` (working tree) / `/design-system` (git HEAD) | **Fixture** sau **link fără sens** |
| „Începe aici", traseul „Învață în profunzime" | un singur principiu (`variabilitatea-dezvoltarii-u11`) | Real, dar fără cale înapoi spre restul conținutului |
| „Începe aici", traseul „Intervino pe teren" | `/probleme/lipsa-unghi-de-pasa` | **Fixture** |
| `/volum/01`–`/volum/04` (paginile index) | — | **0 linkuri de intrare** din restul site-ului (doar link-ul „înapoi" din propriile capitole) |
| `/gold-standard`, `/gold-standard/rapid` | — | **0 linkuri de intrare** din homepage, „Începe aici" sau volume |
| `/principii/[slug]` (oricare din cele 25 reale) | — | Accesibile doar cunoscând URL-ul exact; niciun index |

**Consecință directă:** un antrenor care ajunge pe homepage și dă click pe orice element principal de navigare ajunge fie la o pagină de dezvoltare marcată explicit ca atare, fie într-o fundătură. Sistemul Gold Standard complet — singurul verificat independent `PASS_FIELD_REVIEW_READY` — era complet inaccesibil din fluxul normal de utilizare.

---

## 4. Remediere aplicată (comis în `8d213d4`)

1. **`app/src/lib/content-bridge.ts` → `getPrimaryNavigation()`** — cele 3 rute fixture înlocuite cu rute reale: `/principii` (index nou), `/gold-standard/rapid` (singura instanță reală de Quick Mode), `/gold-standard` (Deep Mode). Această funcție e consumată direct, fără filtrare, de `AppHeader.astro` din `git HEAD` — remedierea rezolvă deci navigarea globală **pentru orice checkout curat al repository-ului**, nu doar pentru working tree-ul curent.
2. **`app/src/pages/principii/index.astro` (fișier nou)** — primul index real al celor 25 de principii de producție, grupate tematic după `category_id`, excluzând explicit fixture-urile (`getCanonicalProductionContent`). Anterior, niciun principiu nu era descoperibil fără a cunoaște URL-ul exact.
3. **Cross-linkuri între cele 4 pagini index de volum** (`volum/01`–`04/index.astro`) — navigare volum-anterior/volum-următor plus linkuri către `/principii` și `/gold-standard` de pe fiecare. Anterior, fiecare volum era o insulă.
4. **`tests/test_task2208_web_integration.py`** — invariantul de design freeze a fost precizat (interzice marcaje Gold Standard doar în blocurile `<style>`, nu în text simplu de navigare), reflectând autorizarea explicită din această buclă pentru edit-uri funcționale minime.

Working tree-ul curent conține și remedieri echivalente în `AppHeader.astro`, `AppFooter.astro`, `incepe-aici.astro`, `index.astro` (etichete/hreffuri corectate) — funcționale acum în build-ul local, dar **necomise**, din motivul de la §5.

---

## 5. Constatare nouă, majoră: divergența git HEAD vs. working tree pentru fișierele design-freeze

În timpul remedierii am descoperit că fișierele din lista de design freeze (`AppHeader.astro`, `AppFooter.astro`, `index.astro`, `incepe-aici.astro`, `principii/[slug].astro`, CSS-urile globale) au în `git HEAD` un conținut **complet diferit și semnificativ mai vechi** decât ce rulează în working tree-ul curent:

- `git show HEAD:app/src/pages/index.astro` → homepage vechi, folosește componente `PageHeader`/`ModeCard`/`SectionHeader` (nu `HeroBallFlight`/`HomepageHero` din working tree), iar CTA-ul „Am nevoie de o soluție acum" duce direct la **`/design-system`** (chiar mai puțin coerent decât fixture-ul găsit în working tree).
- `git show HEAD:app/src/pages/incepe-aici.astro` → conține **zero** linkuri (`href=`) — o pagină complet diferită de cea din working tree.
- `git show HEAD:app/src/components/AppHeader.astro` → antet simplu, text „ManualFC" + badge, fără logo, fără meniu mobil.

Acest lucru înseamnă că **produsul livrabil dintr-un checkout git curat e diferit de (și mai deconectat decât) produsul auditat în working tree-ul acestei sesiuni**. Politica de design freeze — nicio remediere din acest proiect nu a comis vreodată aceste fișiere — a păstrat intenționat necomisă o lucrare de redesign vizual în curs (documentată parțial în `plans/MANUALFC-visual-identity-v1.md`, tot necomis). Remedierea `getPrimaryNavigation()` de la §4 rezolvă corect navigarea pentru ambele stări (HEAD o consumă direct fără filtrare; working tree o consumă prin `preferredLabels`), dar CTA-ul hardcodat din `index.astro` (HEAD) rămâne stricat (`/design-system`) până la o decizie explicită despre fișierele de design freeze.

**Această divergență nu e un defect al acestei sesiuni — e o stare preexistentă, documentată de fiecare raport de task de-a lungul întregului proiect** (`git status` a arătat aceste fișiere ca „murdare" în fiecare sesiune anterioară). Auditul o semnalează acum explicit ca fiind relevantă pentru paritatea produsului, nu doar ca zgomot de fond.

---

## 6. Alte constatări

- **`/exercitii/[slug]` și `/probleme/[slug]`** rămân rute funcționale dar exclusiv pe fixture-uri (`getAllExercises()`/`getAllProblems()` din `content-bridge.ts` citesc doar `data/fixtures/*.json`, niciodată `data/exercises/*.json` reale). Bannerul de avertizare e onest și corect — problema era doar că navigarea primară ducea acolo. Remediat prin eliminarea lor din navigare; rutele rămân, corect etichetate, ca schele tehnice de dezvoltare.
- **`/design-system`** e un dev/brand lab intern, etichetat public „Resurse" — inducere în eroare minoră/moderată, nefixată în acest task (ar necesita fie relabeling fie separarea unei pagini reale de resurse, ambele în afara scopului minim al acestei runde).
- **Nicio scurgere de dovezi retrase** — căutare explicită (`SRC-005[3-9]`, `SRC-006[0-3]`) în `app/src/` și `content/` → 0 rezultate.
- **Nicio copie stale de conținut fabricat** — căutare explicită (`peste 70%`, `regula celor`, `15 secunde`) → singura potrivire e în `content/volume-03/chapter-05.mdx`, folosire legitimă și corect remediată (definește termenul „joystick coaching" doar pentru a-l respinge explicit ca dogmă, nu ca regulă validată).
- **Gold Standard, integrare internă:** confirmată completă — `/gold-standard` (Deep Mode) leagă corect exercițiile, ședințele ȘI evaluarea (`ASM-0001`); `/gold-standard/rapid` (Quick Mode) leagă cele 3 exerciții relevante și înapoi la Deep Mode; Deep Mode leagă ședințele, iar ședințele conțin exercițiile — `SES-0001`/`EX-0001`–`EX-0003` (felia Rundei 1 de pilotare) e accesibilă din produs în maximum 2 click-uri de la `/gold-standard`.

---

## 7. Coverage matrix (după remedierea acestei runde)

| Dimensiune | Înainte | După |
|---|---|---|
| Capitole complet expuse / total | 25/25 (conținutul era deja complet randat) | 25/25, acum și descoperibile prin volume cross-linked |
| Principii complet expuse / total | 25/25 randate, 0/25 descoperibile fără URL exact | 25/25 randate + descoperibile prin `/principii` |
| Componente Gold Standard implementate / necesare | 8/8 (concept, cercetare, 5 exerciții, 2 ședințe, evaluare, instrumente, specificații vizuale, integrare web) — toate existau, 0/8 descoperibile din navigarea primară | 8/8 existente + descoperibile din antet/homepage/volume |
| Navigabilitate (suprafețe reale atinse din navigarea primară) | ~2 din ~30 rute reale (homepage, un principiu) | volume, principii, Gold Standard toate atinse din antet și „Începe aici" |
| `FIELD_PILOT_CAN_RUN_WITHOUT_REPO_ACCESS` | **NU** | **DA** pentru checkout git curat (via `getPrimaryNavigation()`); **DA** și pentru working tree curent (fix suplimentar în fișierele frozen, necomis) |

---

## 8. Constatări pe severitate

### Critice
1. **Navigarea globală (antet, homepage, „Începe aici") nu ducea la niciun conținut real de producție** — REMEDIAT în `8d213d4` la nivelul care contează pentru checkout curat (`getPrimaryNavigation()`).

### Majore
2. **Divergență HEAD vs. working tree pentru toate fișierele design-freeze** — produsul dintr-un checkout curat diferă semnificativ (și e mai stricat) decât ce a fost testat manual în această sesiune. Nefixat — necesită o decizie explicită a utilizatorului despre statutul redesign-ului vizual în lucru.
3. **CTA principal homepage („Am nevoie de o soluție acum") în `git HEAD` duce la `/design-system`**, o pagină internă fără relevanță pentru problema utilizatorului. Nefixat (fișier frozen).
4. **10 din 15 categorii de taxonomie declarate nu au nicio rută sau conținut** — arhitectură aspirațională nerealizată. Nu s-a acționat (ar fi infrastructură nejustificată pentru conținut inexistent).

### Moderate
5. **`/design-system` etichetat public „Resurse"** induce în eroare — e un instrument intern de brand, nu o resursă de coaching.
6. **`/exercitii/[slug]` și `/probleme/[slug]` rămân găzduite exclusiv pe fixture-uri**, fără o cale de migrare spre schema reală de producție (problemă sistemică deja documentată în DEC-0044, nerezolvată aici, în afara scopului minim).

### Minore
7. Fixture-ul de la `/principii/orientare-corporala-scanare` afișează corect bannerul de avertizare, dar folosește un titlu ("Orientare corporală și scanare") suficient de plauzibil încât ar putea fi confundat cu un principiu real dacă e accesat direct.

---

## 9. Remediation order (aplicat parțial în această rundă)

1. ~~Navigare globală stricată → conținut real~~ **FĂCUT**
2. ~~Index de principii lipsă~~ **FĂCUT**
3. ~~Volume izolate, fără cross-link~~ **FĂCUT**
4. Divergență HEAD/working-tree pentru fișierele frozen → **necesită decizie explicită a utilizatorului**, nu remediat autonom
5. CTA homepage stricat în HEAD → blocat de #4
6. Relabeling `/design-system` → **neîncepe**, moderat, opțional
7. Migrarea `/exercitii`/`/probleme` de pe fixture pe schema reală → **neîncepe**, sistemic, în afara scopului minim

---

## 10bis. Addendum după audit independent (TASK-2402/TASK-2403)

Auditul independent `TASK-2402` a confirmat exacte toate constatările de mai sus, cu două corecții:

1. **Eroare aritmetică (§2):** taxonomia are **16** categorii declarate (nu 15), din care **13** fără conținut (nu 10) — lista de nume enumerată era deja corectă, doar cifrele-sumar erau greșite.
2. **Afirmație de „funcțional" invalidată (§4/§5):** `app/src/components/HomepageHero.astro` — componenta hero importată de `index.astro`, necomisă, parte a aceluiași redesign vizual în lucru — NU primise remedierea CTA-ului „Am nevoie acum" (rămăsese pe `/probleme/lipsa-unghi-de-pasa`), contrar afirmației din acest raport și din `DEC-0048`. Corectat în `TASK-2403` (modificare de o linie, verificată prin build propriu și inspecția HTML-ului generat — vezi `reports/task-reports/TASK-2403.md`). Fișierul rămâne necomis, din același motiv ca celelalte fișiere din redesign-ul în lucru.

Verdict independent final: `REPAIR_REQUIRED` → remediat → toate constatările blocante închise.

## 10. Ce NU s-a făcut și de ce

- Nu s-au creat cele 10+ pagini-hub de taxonomie aspirațională (safeguarding, părinți, resurse, motricitate, psihologie etc.) — zero conținut canonic real le-ar susține; ar fi infrastructură nouă, nu expunerea unui conținut existent.
- Nu s-a atins niciun fișier CSS/`<style>` — toate remedierile sunt text/hreffuri simple, verificat programatic (`tests/test_task2208_web_integration.py`).
- Nu s-a comis nicio modificare la `AppHeader.astro`, `AppFooter.astro`, `index.astro`, `incepe-aici.astro` — deși editate funcțional în working tree, sunt inseparabile de un redesign vizual necomis mai amplu; comiterea lor ar fi încălcat politica de design freeze prin includerea accidentală a acelui redesign.
- Nu s-a re-cercetat sau modificat niciun claim, sursă sau capitol — acest audit privește exclusiv implementarea, nu adevărul conținutului (deja stabilit `PASS_FIELD_REVIEW_READY` pentru toate componentele).
