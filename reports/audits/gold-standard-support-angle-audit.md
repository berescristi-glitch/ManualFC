# Audit independent — Gold Standard: Sprijinul și unghiul de pasă (TASK-2209)

**Domeniu:** TASK-2201–TASK-2208 (`HEAD` la momentul auditului: `2b135f2`) — primul sistem pedagogic vertical complet al ManualFC (readiness audit → cercetare → concept → exerciții → ședințe → evaluare → instrumente de teren → specificații vizuale → integrare web), pentru tema „Sprijinul și unghiul de pasă".

**Executant:** Sesiune separată de TASK-2201–2208, fără nicio implicare în scrierea materialului auditat. Nu s-a pornit de la premisa că munca de producție e corectă — fiecare sursă, cifră și claim de mai jos a fost re-derivată/re-verificată independent, nu copiată din rapoartele de task sau din `researcher_notes`. Respectă separarea audit/reparație impusă după eșecul documentat în `DEC-0040` (combinarea reparației cu verdictul propriu a permis fabricărilor din VOLUME-03/04 să treacă nedetectate).

**Metodă:** Toate cele 7 surse cerute explicit (`SRC-0089`, `SRC-0108`–`SRC-0113`) verificate direct prin CrossRef (`fetch_crossref_by_doi`), comparând titlu/autori/an/revistă cu `research/sources.json`. Trei dintre cifrele eșantion cele mai încărcate epistemic (De Giorgio 2018: 34 copii de 7 ani, 17v17; Coutinho 2023: 16 copii, 12,94 ani; McGuckian 2018: 32 semi-elită adulți) au fost verificate terț prin acces la abstractul integral (PLOS ONE fulltext, CrossRef abstract, Frontiers fulltext), nu doar prin titlu. Toate cele 14 documente/entități listate în specificația task-ului au fost citite integral. `research/claims.json`, `citations.json`, `questions.json` interogate programatic pentru ID-urile cerute. S-au rulat cele 5 gate-uri de validare cerute, independent. Design freeze verificat prin `git diff a5251c6 HEAD --stat` pe lista exactă de fișiere înghețate.

---

## VERDICT EXECUTIV

# `PASS_FIELD_REVIEW_READY`

Vertical slice-ul Gold Standard rezistă unei re-verificări independente și sceptice. Nu s-a găsit nicio sursă fabricată, niciun DOI nepotrivit, nicio suprasolicitare epistemică nedeclarată, nicio cifră exactă prezentată drept cercetare fără etichetă onestă, nicio dogmă înlocuită cu dogma opusă, nicio dovadă de pilotare fabricată, și nicio încălcare a design freeze-ului. S-au găsit 3 defecte minore/cosmetice, niciunul blocant — enumerate mai jos.

---

## 1. Verificare bibliografică independentă (CrossRef)

| Sursă | DOI | Titlu confirmat CrossRef | Autori/An/Revistă confirmate | Verdict |
|---|---|---|---|---|
| `SRC-0089` (reutilizat din CH-0402) | `10.3389/fpsyg.2021.772201` | „Perceptual-Motor and Perceptual-Cognitive Skill Acquisition in Soccer: A Systematic Review on the Influence of Practice Design and Coaching Behavior" | Bergmann, Gray, Wachsmuth, Höner (2021), *Frontiers in Psychology* | Potrivire exactă |
| `SRC-0108` | `10.3389/fpsyg.2018.02520` | „Don't Turn Blind! The Relationship Between Exploration Before Ball Possession and On-Ball Performance in Association Football" | McGuckian, Cole, Jordet, Chalkley, Pepping (2018), *Frontiers in Psychology* | Potrivire exactă. Verificat terț (fulltext Frontiers): N=32, 16–30 ani (medie 19,03), nivel semi-elită Australia — identic cu `population`/`age_range` din `sources.json`. |
| `SRC-0109` | `10.1080/02640414.2023.2235160` | „Head movement direction in football – a field study on visual scanning activity during the UEFA-U17 and -U21 European Championship 2019" | Pokolm, Kirchhain, Müller, Jordet, Memmert (2023), *Journal of Sports Sciences* | Potrivire exactă |
| `SRC-0110` | `10.1080/02640414.2021.1935115` | „Scanning activity in elite youth football players" | Aksum, Pokolm, Bjørndal, Rein, Memmert, Jordet (2021), *Journal of Sports Sciences* | Potrivire exactă |
| `SRC-0111` | `10.1371/journal.pone.0200689` | „Enhancing motor learning of young soccer players through preventing an internal focus of attention: The effect of shoes colour" | De Giorgio, Sellami, Kuvačić, Lawrence, Padulo, Mingardi, Mainolfi (2018), *PLOS ONE* | Potrivire exactă. Verificat terț (fulltext PLOS): „Thirty-four 7-years-old soccer players... randomized to two groups (Coloured n = 17 and Black, n = 17)" — cuvânt cu cuvânt identic cu `population` din `sources.json` și cu `CLM-0102`. |
| `SRC-0112` | `10.3390/children10020220` | „Exploring the Effects of Tasks with Different Decision-Making Levels on Ball Control, Passing Performance, and External Load in Youth Football" | Coutinho, Kelly, Santos, Figueiredo, Pizarro, Travassos (2023), *Children* | Potrivire exactă. Abstract CrossRef confirmă „16 male youth football players (age: 12.94 ± 0.25 years)" — identic cu `population`. |
| `SRC-0113` | `10.1177/17479541231168930` | „Challenging traditions: Systematic review of practice, instruction, and motor skill acquisition in soccer" | Pacheco, de Oliveira, dos Santos, Godoi Filho, Drews (2023), *International Journal of Sports Science & Coaching* | Potrivire exactă |

**Rezultat: 7 din 7 surse verificate — 0 titluri greșite, 0 autori greșiți, 0 DOI aparținând altei lucrări.** Niciun eșec de tipul `FABRICATED`/`WRONG_METADATA_REAL_DOI`/`MISMATCHED_DOI` documentat în precedentul `DEC-0040`.

---

## 2. Verificare eșantion / populație / aplicabilitate U11

Verificat pentru toate cele 4 claim-uri cerute (`CLM-0101`–`CLM-0104`), plus sursele reutilizate în exerciții/ședințe (`SRC-0035`, `SRC-0037`, `SRC-0039`–`SRC-0042`, `SRC-0101`–`SRC-0105`):

- **`CLM-0101`** (scanare → orientare → atingere): sursele sunt corect etichetate „Adulti semi-elita + tineret elit U17-U21", `u11_applicability` implicit `INDIRECT` (dosarul o declară explicit). `allowed_wording` interzice explicit „Rezultatul e dovedit la copii de 10-11 ani" — și nicăieri în `EX-0003`, `CONCEPT_MODEL.md` sau paginile web nu apare o formulare care ridică acest claim la un fapt dovedit la U11. Formularea folosită peste tot e „extrapolare plauzibilă, declarată ca atare".
- **`CLM-0102`** (De Giorgio 34×7 ani + Coutinho 16×12,94 ani): populația exactă din claim se potrivește cu `sources.json` și cu abstractele reale (verificat mai sus). Nicăieri nu e prezentat ca testat exact la 10-11 ani — `forbidden_overstatements` interzice explicit asta, și textul din `EX-0003`/`CONCEPT_MODEL.md` spune „cea mai apropiată dovadă de vârsta U11", nu „dovadă la U11".
- **`CLM-0103`** (nicio tehnică unică validată): sinteze sistematice, populație declarată corect ca „sinteze, fotbal", fără supra-extrapolare.
- **`CLM-0104`** (absența cercetării pentru direcția primului contact): etichetat corect `UNRESOLVED`/`confidence: LOW`, prezentat explicit ca „constatare de absență", nu rezultat pozitiv. `EX-0003`, `FIELD_TOOLS.md` și dosarul repetă consecvent: „rămâne recomandare practică ManualFC, nu cercetare".

**Politica numerelor exacte:** verificată în toate cele 5 exerciții. Fiecare dimensiune de teren, durată de set, prag de repetiție are `dimension_rationale`/`why` explicit etichetat `EXERCISE_SPECIFIC_PARAMETER`, niciodată `SOURCE_DIRECT`. Nu există niciun unghi exact (`45°` apare o singură dată, în `EX-0003.phrases_to_avoid`, explicit ca frază de evitat, nu ca regulă). Nu există niciun procent (`grep` pentru „%" nu a găsit nicio potrivire în `docs/gold-standard/`, `data/exercises/`, `data/sessions/`, `data/assessments/`, dosarul de cercetare). Niciun scor pseudo-precis (`X.X/10`) — evaluarea (`ASM-0001`) folosește exclusiv niveluri calitative pe 3 trepte per criteriu.

---

## 3. Verificare evitare dogmă

`CONCEPT_MODEL.md` secțiunea 2 respinge explicit atât un unghi universal fix, cât și implicit poziția „unghiul nu contează" — principiul rămâne funcțional („creează o opțiune de pasă utilă"), nu geometric fix, dar nici arbitrar. `CLM-0103`/`SRC-0113` sunt folosite pentru a respinge o „tehnică de recepție corectă" unică, fără a aluneca în „orice execuție e la fel de bună" — textul spune explicit „calitatea execuției tehnice depinde substanțial de designul practicii și de context", păstrând un standard funcțional (poate copilul continua acțiunea?), nu unul relativist. Nu s-a găsit nicio afirmație care ar declara constrângerile/CLA superioare universal instrucției directe sau invers — de fapt exercițiile combină ambele (indicii externe + reguli explicite de joc), consecvent cu poziția de mijloc deja stabilită în VOLUME-04/CH-0402 (verificată la auditul anterior).

---

## 4. Consistență internă

- **ID-uri referite există și spun ce li se atribuie:** `principle.spatiu-si-unghiuri`, `principle.progresie-si-sprijin`, `principle.transfer-autonom-cooperare` (referite de `ASM-0001.principle_ids`) — toate există în `data/principles/` cu ID-urile exacte. Toate sursele citate în exerciții/ședințe (`SRC-0035`, `SRC-0037`, `SRC-0039`–`SRC-0042`, `SRC-0101`–`SRC-0105`, `SRC-0108`, `SRC-0109`, `SRC-0111`, `SRC-0113`) există în `research/sources.json`, niciuna `withdrawn`.
- **Sumele segmentelor de ședință:** `SES-0001` (0–12–24–38–55–65–75, total 75 min = `duration_min`) și `SES-0002` (0–10–30–55–75, total 75 min = `duration_min`) — ambele contigue, fără goluri sau suprapuneri, ambele corespund exact cu `duration_min` declarat.
- **Evaluarea (`ASM-0001`):** exclusiv niveluri calitative pe 3 trepte (fără comportament observat → cu reper extern → autonom), nicio pseudo-precizie numerică.
- **Referințe exercițiu→ședință:** toate `exercise_ids` din segmentele `SES-0001`/`SES-0002` (`EX-0001`–`EX-0005`) rezolvă corect prin `content-bridge.ts` (`getGoldStandardSessionExercises`, verificat prin build-ul Astro reușit — toate cele 5 rute `/gold-standard/exercitii/EX-000N` și 2 rute `/gold-standard/sedinte/SES-000N` s-au generat static fără erori).

**Defect minor găsit (neblocant):** `CLM-0103.source_ids` include `SRC-0089`, dar `research/citations.json` nu conține nicio intrare `citation_id` care leagă explicit `CLM-0103` de `SRC-0089` (singura citare a `SRC-0089` din registru e `CIT-0096`, legată de `CLM-0090`, din VOLUME-04). Legătura conceptuală există și e corectă (dosarul explică reutilizarea), dar lipsește o intrare formală de citare pentru acest link specific. Nu afectează adevărul conținutului — sursa e reală și relevantă — doar completitudinea registrului de citări.

**Defect cosmetic găsit:** `SRC-0112` (Coutinho et al. 2023, unul din cei doi piloni ai `CLM-0102`) nu apare în câmpul `sources` al niciunui exercițiu (`EX-0001`–`EX-0005`) — doar în dosarul de cercetare și, indirect, în `CONCEPT_MODEL.md`. `EX-0003` citează explicit doar `SRC-0111` (De Giorgio) când invocă `CLM-0102`, deși claim-ul se sprijină pe ambele surse. Nu e o eroare de conținut (nimic fals afirmat), dar lista `sources` a exercițiului e incompletă față de claim-ul pe care îl folosește.

---

## 5. Onestitatea transferului în meci

`FIELD_VALIDATION_PENDING` apare consecvent și corect în cele 3 locuri unde ar trebui: `EX-0005.match_transfer`, `ASM-0001-C5` (al treilea nivel), și pagina `/gold-standard` (nota de stare). Nicăieri în cele 14 documente/fișiere/pagini auditate nu apare vreo afirmație de tipul „am testat pe teren și..." sau vreun rezultat de pilotare simulat/fabricat — căutare explicită (`pilotare|piloted|field.?tested|rezultatele arată că jucătorii`) nu a găsit nicio potrivire suspectă. `EX-0005` e prezentat corect ca „testul de transfer" în cadrul familiei de exerciții, nu ca dovadă de transfer real în meci oficial.

---

## 6. Testul limbajului pentru copil

Spot-check pe `child_message`/`coach_feedback` din toate cele 5 exerciții și 2 ședințe:

- „Uită-te la conul colorat înainte să primești, și primește-o spre acolo." (`EX-0003`) — natural, spus în 2-3 secunde.
- „Bravo, ai găsit unghiul!" / „Caută spațiul liber, nu piciorul cu care primești." (`coach_feedback`) — scurte, orientate spre acțiune, fără jargon.
- „Jucați ca de obicei — folosiți ce ați exersat dacă vă ajută!" (`EX-0005`) — natural.
- „Mută-te până când adversarul nu ne mai poate acoperi pe amândoi — și fii gata să mai schimbi dacă se mișcă!" (`EX-0002`) — mai lungă (~17 cuvinte), dar contextul explicit e „la pauza dintre seturi", nu strigat în timpul jocului activ; acceptabilă pentru acel context.
- „Dacă coechipierul tău e deja într-o zonă bună, găsește-ți propria zonă — nu vă adunați amândoi în același loc!" (`EX-0004`) — similar, lungime acceptabilă pentru context de pauză, nu de joc activ.

Nu s-a găsit nicio formulare tradusă literal din jargon academic (nu apare „focalizare atențională externă" sau „orientare corporală" direct în `child_message` — aceste concepte rămân în `rationales`/`why_this_message`, destinate antrenorului, corect separate de ce se spune efectiv copilului).

---

## 7. Design freeze

`git diff a5251c6 HEAD --stat` pe lista exactă a celor 15 fișiere înghețate (`AppFooter.astro`, `AppHeader.astro`, `ChildMessage.astro`, `CoachMessage.astro`, `EvidenceBadge.astro`, `QuickModePattern.astro`, `BaseLayout.astro`, `design-system.astro`, `incepe-aici.astro`, `index.astro`, `principii/[slug].astro`, `global.css`, `print.css`, `tokens.css`, `astro.config.mjs`, `config/visual-tokens.json`) → **diff gol, 0 fișiere atinse.** Paginile noi (`gold-standard/index.astro`, `gold-standard/rapid.astro`, `gold-standard/exercitii/[id].astro`, `gold-standard/sedinte/[id].astro`) importă `BaseLayout`, `Breadcrumb`, `EvidenceBadge`, `QuickModePattern` ca dependențe read-only, fără nicio modificare a acestor componente. `content-bridge.ts` extinde aditiv (secțiunea „Gold Standard Bridge", linia 385+) fără să atingă loaderele existente de principii/exerciții/probleme.

(Notă: `git status` arată fișierele de design freeze ca „murdare" — dar acesta e un state pre-existent, documentat deja în `GOLD_STANDARD_READINESS_AUDIT.md` secțiunea 0 și nelegat de commit-urile Gold Standard; `git diff a5251c6 HEAD` — commit-uri reale, nu working tree — confirmă 0 atingere.)

---

## 8. Niciun asset vizual real produs

`TACTICAL_VISUAL_SPECS.md` conține exclusiv specificații semantice (scop, jucători, relații, punct de decizie, secvență de fază, alternativă textuală) pentru toate cele 5 vizualuri (`VIS-EX-0001`–`VIS-EX-0005`). Căutare explicită de fișiere `.svg`/`.png`/`.jpg` legate de Gold Standard → 0 rezultate. Toate cele 5 câmpuri `visual_assets` din exerciții sunt marcate `PENDING` cu nota „niciun fișier grafic produs (design freeze activ)".

---

## 9. Gate-uri de validare (rulate independent)

| Comandă | Rezultat |
|---|---|
| `python scripts/validate_content.py --strict` | `VALID: 0 erori, 0 avertismente, 0 informații` |
| `python scripts/validate_project.py` | `0 erori, 0 avertismente` (203 taskuri: 59 DONE, 143 PENDING, 1 READY) |
| `python scripts/generate_task_registry.py --check` | `Registrul este reproductibil: 203 taskuri.` |
| `python -m unittest discover -s tests -p "test_*.py"` | `Ran 404 tests ... OK` |
| `cd app && npm run build` | Succes — 71 pagini generate static, inclusiv toate cele 5 rute `/gold-standard/exercitii/EX-000N`, 2 rute `/gold-standard/sedinte/SES-000N`, `/gold-standard/`, `/gold-standard/rapid/`, fără erori |

Notă: aceste gate-uri verifică integritate structurală/schema, nu adevărul conținutului — verdictul de mai sus se bazează în primul rând pe verificarea bibliografică externă și recitirea integrală descrise în secțiunile 1–8.

---

## Constatări pe severitate

### Critice
Niciuna.

### Majore
Niciuna.

### Minore (neblocante)
1. **`CLM-0103` fără citare formală pentru `SRC-0089`.** `research/claims.json`, `CLM-0103.source_ids` include `SRC-0089`, dar `research/citations.json` nu are nicio intrare `citation_id` care leagă cele două explicit (doar `CIT-0120`→`SRC-0113`). Remediere propusă opțională: adăugare `CIT-0122` (`claim_id: CLM-0103`, `source_id: SRC-0089`) pentru completitudinea registrului.

### Cosmetice
2. **`SRC-0112` (Coutinho 2023) absent din `sources` al oricărui exercițiu**, deși e unul din cei doi piloni ai `CLM-0102`, invocat explicit în `EX-0003`. Remediere propusă opțională: adăugare `SRC-0112` în `data/exercises/exercise-primeste-gata-sa-continui.json.sources`.
3. **`child_message` la `EX-0002`/`EX-0004` ușor lungi (~17-20 cuvinte)** pentru rostire instantanee — acceptabil dat fiind că sunt formulate explicit pentru pauza dintre seturi, nu pentru strigare în timpul jocului activ, dar merită scurtare opțională la o eventuală revizuire editorială.

Niciuna dintre aceste 3 constatări nu afectează adevărul, siguranța, calibrarea epistemică sau integritatea bibliografică a materialului.

---

## Concluzie

Cele 7 surse cerute (plus cele 11 surse reutilizate verificate suplimentar în secțiunea 4) sunt reale, verificabile prin CrossRef, corect atribuite și folosite strict în limitele epistemice pe care le susțin de fapt. Toate cele 4 claim-uri noi (`CLM-0101`–`CLM-0104`) declară onest populația reală a studiilor (adulți/U17+ pentru scanare, 7 ani și 12,94 ani pentru intervenții controlate) și interzic explicit, prin `forbidden_overstatements`, exact tipul de suprasolicitare care a cauzat eșecul `DEC-0040`. Politica numerelor exacte e respectată consecvent — nicio dimensiune, durată sau unghi nu apare fără etichetă `EXERCISE_SPECIFIC_PARAMETER`/`MANUALFC_HEURISTIC` explicită. Nicio dogmă nu a fost înlocuită cu dogma opusă. `FIELD_VALIDATION_PENDING` e folosit onest, fără nicio urmă de date de pilotare fabricate. Design freeze-ul e intact (verificat prin diff de commit-uri, nu doar prin declarație). Niciun fișier grafic real nu a fost produs — doar specificații semantice. Toate cele 5 gate-uri de validare trec. Cele 3 constatări minore/cosmetice de mai sus sunt oportunități de polish, nu defecte care justifică o remediere de conținut.

**Verdict: `PASS_FIELD_REVIEW_READY`.**
