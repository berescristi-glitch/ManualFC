# ManualFC — Educational Design Principles (Gate 2)

Fiecare principiu de mai jos este trasabil la o constatare din `LEARNING_UX_EVIDENCE_MATRIX.md` (referință #) sau este etichetat explicit **[EURISTICĂ]** dacă e o inferență HCI rezonabilă fără dovadă directă. Niciun principiu nu e prezentat ca literă de lege dacă dovada e contestată sau slabă.

Format: EVIDENȚĂ → MECANISM → IMPLICAȚIE DE DESIGN → APLICAȚIE MANUALFC → LIMITĂ.

---

### P1 — Nucleul procedural rămâne mereu vizibil

EVIDENȚĂ: #26, #28 (risc de omisiune la acordeon + cost cognitiv al deciziilor de navigare, mai mare pt. novici) · #14-16 (retrieval slab fără conținut de bază solid) · #31-32 (instrucție ghidată).
MECANISM → orice conținut ascuns în spatele unui click poate fi pur și simplu nevăzut de exact utilizatorul cu risc mai mare (antrenorul novice).
IMPLICAȚIE → conținutul de care depinde siguranța/corectitudinea acțiunii (ce faci, ce spui exact, ce verifici, ce să nu presupui) nu se ascunde niciodată în spatele unui `<details>`, tab sau acordeon.
APLICAȚIE → secțiunile „Ce le spun și de ce" (limbaj exact, comportament urmărit, riscuri de evitat), „Instrumentul practic" și „Ce nu putem concluziona" rămân întotdeauna expandate implicit, pe toate paginile, pentru toți cititorii.
LIMITĂ → nu înseamnă că *totul* trebuie vizibil — vezi P2 pentru ce poate fi comprimat.

### P2 — Elaborarea de fundal e comprimabilă, nu ascunsă implicit

EVIDENȚĂ: #50 (Tetzlaff et al. 2025, expertise reversal, asimetric — beneficiu novici d=0,505 > cost experți d=−0,428) · #1, #26 (risc acordeon) · #51 (Noetel et al. 2022 — aceste efecte sunt mai slabe în contexte auto-ritmate ca o pagină web decât în prelegere/video, deci nu supra-estima câștigul).
MECANISM → explicația detaliată ajută novicele și încetinește/irită antrenorul experimentat; dar ascunderea implicită riscă exact opusul pentru novice. Efectul e asimetric (nu simetric) — sub-scaffolding-ul rănește novicii mai mult decât over-scaffolding-ul rănește experții.
IMPLICAȚIE → conținutul pur elaborativ (rațiunea completă pe mai multe dimensiuni, context istoric/teoretic extins) poate fi comprimat printr-un mecanism reversibil, cu stare implicită **deschisă**, nu închisă — comprimarea e o opțiune a cititorului, nu un default care ascunde conținut de novice.
APLICAȚIE → un toggle persistent de pagină ("Explicație completă" / "Doar esențialul"), nu accordion per-secțiune — vezi Gate 3/4 pentru mecanismul exact. Dovada susține disclosure controlat de cititor ÎN PRINCIPIU, dar nu prescrie un toggle binar ca mecanism obligatoriu — alegerea exactă rămâne o decizie de implementare, nu o cerință a cercetării.
LIMITĂ → efectul de inversare a expertizei e testat mai ales pe sarcini procedurale scurte de laborator, nu pe citire web auto-dirijată lungă; mecanismul exact de livrare (toggle de pagină) e o extrapolare rezonabilă, nu o intervenție validată direct pe acest format.

### P3 — Diagrama stă lângă explicația ei, niciodată într-un tab separat

EVIDENȚĂ: #45 (Schroeder & Cenkci 2018, meta-analiză, g=0,63 — unul dintre cele mai solid replicate efecte din toată literatura de multimedia learning) · #38, #42 (benchmarking: exemplul lângă explicație, nu în filă separată).
IMPLICAȚIE → orice `TacticalDiagram`/`ConceptLoop`/`SurfaceMap` se plasează imediat adiacent paragrafului pe care îl explică, în flux, niciodată într-un tab sau acordeon separat de text. Etichetele esențiale pentru citirea diagramei aparțin diagramei înseși, nu doar unei legende îndepărtate.
APLICAȚIE → componentele vizuale existente (`TacticalDiagram`, `ConceptLoop`, `ProblemVisual`) rămân inline; nu se introduce un „tab de diagrame" separat de „tab de text".

### P4 — „Ce nu putem concluziona" rămâne vizibil în fluxul principal

EVIDENȚĂ: #35, #36 (comunicarea incertitudinii, GRADE) — cea mai riguros fundamentată constatare din toată cercetarea.
IMPLICAȚIE → secțiunea de limite nu se retrogradează niciodată într-o zonă de profunzime opțională sau într-un acordeon — rămâne o secțiune cu titlu propriu, mereu vizibilă, indiferent de starea toggle-ului de comprimare (P2).
APLICAȚIE → `EvidenceNote`/secțiunea de limite e exclusă explicit din orice mecanism de comprimare.

### P5 — Titlurile de secțiune trebuie să comunice singure beneficiul (information scent)

EVIDENȚĂ: #2 (Pirolli & Card).
IMPLICAȚIE → interzice titluri generice ("Detalii", "Mai mult", "Context"); fiecare titlu de secțiune numește fenomenul/acțiunea specifică.
APLICAȚIE → structura fixă deja folosită de capitole (ex. „Riscuri și formulări de evitat", nu „Alte observații") respectă deja acest principiu — păstrează-l ca regulă explicită pentru toate componentele noi.

### P6 — Ierarhie de titluri front-loaded > ascundere de conținut, ca investiție de scanabilitate

EVIDENȚĂ: #5 (layer-cake pattern) vs. #4 (F-pattern contestat).
IMPLICAȚIE → prioritate de efort: titluri clare, specifice, la începutul propoziției-cheie — nu mecanisme de disclosure.

### P7 — Măsură tipografică 60-75 caractere, font 16-18px, line-height ≥1.5

EVIDENȚĂ: #6, #7, #8, #9 (convergență experiment + canon + accesibilitate).
APLICAȚIE → `.chapter-content p, li { max-width: 72ch }` deja existent e aproape aliniat (72ch ≈ limita superioară a intervalului) — păstrează, nu extinde.
LIMITĂ → 72ch e capătul superior al intervalului empiric, nu mijlocul; nu îngusta suplimentar fără motiv, dar nu lărgi peste el.

### P8 — TOC justificat la lungimea paginilor ManualFC, dar trebuie să marcheze secțiunea curentă

EVIDENȚĂ: #11 (TOC sticky fără highlight = "decor inert", constatare empirică directă).
IMPLICAȚIE → dacă se adaugă TOC/navigare sticky, implementarea TREBUIE să includă marcaj activ de secțiune (scroll-spy), altfel nu se adaugă deloc — un TOC static fără highlight nu justifică bugetul de complexitate.
APLICAȚIE → `SectionNavigator` existent (folosit pe `/principii/`) NU are highlight de secțiune curentă — necesită extindere înainte de a fi reutilizat pe capitole (vezi Gate 3-4).

### P9 — Bara de progres la citire: prioritate scăzută, netratată ca dovadă de învățare

EVIDENȚĂ: #13.
IMPLICAȚIE → dacă se adaugă, se etichetează intern ca decorativă/motivațională, nu ca intervenție de comprehensiune; nu consumă buget de implementare înaintea P1-P8.

### P10 — Prompt de pre-testare, plasat ÎNAINTE de secțiunea relevantă, fără a pretinde „retrieval practice" validat

EVIDENȚĂ: #16 (pretesting effect) vs. #14-15 (retrieval practice real cere răspuns produs efectiv).
IMPLICAȚIE → un prompt scurt de tip „Ce ai observa/face aici?" se plasează ÎNAINTE de reveal-ul relevant (nu după, ca reflecție post-hoc), formulat ca angajament explicit, cu `<details>/<summary>` pentru reveal — fără JS obligatoriu.
APLICAȚIE → folosire selectivă, nu pe fiecare secțiune (regula §39 din specificație: nu transforma fiecare pagină într-un quiz) — un singur prompt de acest tip per capitol, plasat la scenariul inițial sau la un punct de decizie clar.
LIMITĂ → etichetează intern acest mecanism ca „nudge anticipativ, nu retrieval practice dovedit" — vezi watchlist §7 din cercetare.

### P11 — O suprafață distinctă de „recall rapid" (recuperare, nu recitire)

EVIDENȚĂ: #16 (pretesting) + #17 (spacing, obținut gratuit prin revenire ulterioară naturală) — cea mai bine fundamentată idee nouă din cercetare.
IMPLICAȚIE → construiește ca întrebare/reper întâi, răspuns/detaliu după (reveal), nu ca rezumat de recitit pasiv.
APLICAȚIE → candidat pentru un mod/secțiune „Recall rapid" — proiectare completă în Gate 3-4, NU implementată automat ca sistem de spațiere (ManualFC nu construiește un sistem de recapitulare programată în această fază).

### P12 — Advance organizer la începutul paginii: adăugare cu risc scăzut, cost mic, efect mic

EVIDENȚĂ: #22.
APLICAȚIE → o casetă scurtă de orientare (ideea centrală + hartă a secțiunilor) la începutul capitolului — nu vândută ca lever puternic de retenție.

### P13 — Comprimare/expertise nu înseamnă conținut factual diferit, ci vizibilitate diferită a elaborării

EVIDENȚĂ: #29 (expertise reversal) + #30 (andragogia, folosită doar ca euristică, nu știință).
IMPLICAȚIE → nu construi „două produse" (Pedagogul-novice vs. Pedagogul-expert) — un singur document canonic, cu o singură axă de comprimare reversibilă (P2).

### P14 — Exemplu contrastant „greșit vs. corect", adăugare bine fundamentată, parțial absentă

EVIDENȚĂ: #33-34.
APLICAȚIE → secțiunea existentă „Riscuri și formulări de evitat" acoperă parțial acest rol; o versiune viitoare (nu neapărat în acest pilot) ar putea alătura explicit o mini-comparație — notat ca recomandare pentru autorat viitor, nu ca schimbare de conținut în acest task (regula §60: presentarea se poate schimba, sensul științific nu, fără dovadă).

### P15 — Accesibilitate: contractul minim pentru orice disclosure

EVIDENȚĂ: #23-25 (WCAG 1.4.10, 2.5.8/2.5.5, pattern APG Accordion).
APLICAȚIE → contract complet în `EDUCATIONAL_COMPONENT_CONTRACT.md`. Rezumat: buton real, `aria-expanded`, `hidden` pe panouri închise, focus vizibil, target ≥24px (minim), 44px ca practică recomandată, fără culoare ca unic semnal de stare.

### P16 — Mobil: prioritizează nucleul procedural în primul ecran, fără scroll orizontal

EVIDENȚĂ: #23 (WCAG reflow) + #27-28 (cost de timp mai mare pe mobil la text dificil + cost cognitiv de navigare).
APLICAȚIE → la 390px, nucleul procedural nu trebuie să ceară deschiderea mai multor secțiuni comprimate pentru a fi găsit.

### P17 — Nu inversa structura scenariu→explicație existentă

EVIDENȚĂ: #31-32 (instrucție ghidată + ancorare, deja aliniate cu structura curentă).
IMPLICAȚIE → arhitecturile concurente din Gate 3 NU propun „concept întâi" ca alternativă serioasă — dovada nu o susține pentru acest format.

---

## Principii respinse explicit (nu vor apărea în Gate 3-4)

- Accordion/tab ca mecanism implicit de scurtare a paginii pentru conținut esențial (P1, P4).
- F-pattern ca literă de lege pentru layout (P6).
- Bară de progres ca prioritate de implementare (P9).
- Retrieval practice „real" fără mecanism de răspuns produs efectiv (P10 — folosim doar varianta slăbită, etichetată corect).
- Andragogia ca justificare științifică (P13).
- Două arhitecturi de conținut separate pentru novice/expert (P13).
- Reguli numerice fixe fără sursă (ex. cuvinte-per-paragraf) — intervale raționate în loc.
