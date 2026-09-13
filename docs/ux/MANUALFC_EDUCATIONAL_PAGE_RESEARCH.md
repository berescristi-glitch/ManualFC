# MANUALFC — Educational Page Architecture & Learning UX Research (Gate 1)

**Statut:** cercetare finalizată, alimentează decizia de arhitectură (Gate 2-4). Acest document NU autorizează nicio implementare — implementarea e tratată separat, cu propriile audituri, în rapoartele de acceptanță ale acestei faze.

**Metodă:** 6 clustere de cercetare independente, fiecare executat de un agent cu buget propriu de căutare web reală (WebSearch/WebFetch), reguli explicite anti-fabricare, obligație de verificare a fiecărei surse înainte de citare, și obligație de a semnala explicit dovezile contestate/contradictorii. Sursele acoperă meta-analize, review-uri sistematice, studii experimentale peer-reviewed, standarde normative (WCAG/W3C) și cercetare de uzabilitate practician (Nielsen Norman Group) — aceasta din urmă etichetată explicit ca "practician", nu peer-reviewed, dar cu metodologie disclosed și istoric de 25+ ani.

Matricea completă de dovezi, rând cu rând, e în [`LEARNING_UX_EVIDENCE_MATRIX.md`](./LEARNING_UX_EVIDENCE_MATRIX.md). Acest document sintetizează constatările în proză și trage concluziile pentru fiecare temă majoră cerută de specificație.

---

## 1. Cognitive Load Theory & Multimedia Learning (Mayer)

**Notă metodologică:** acest cluster a necesitat un al doilea val de cercetare — primul agent dispatch-at pentru acest subiect nu a finalizat (eșec de sesiune, fără raport recuperabil), iar prima variantă a acestei secțiuni fusese scrisă din sinteză proprie, nu din cercetare externă verificată, încălcând exact regula anti-fabricare aplicată riguros celorlalte 5 clustere. Defectul a fost descoperit prin verificare directă (agentul lipsea din lista de task-uri active) și corectat printr-un al doilea val de cercetare genuină, documentat explicit în DECISIONS.md.

Modelul cu trei factori al Cognitive Load Theory (intrinsec/extraneu/germane) e aproape unanim acceptat pentru distincția intrinsec/extraneu, dar "germane load" ca al treilea factor măsurabil separat e contestat (Jiang & Kalyuga 2020 argumentează pentru un model cu 2 factori). **Implicație:** tratează "reducerea aglomerării" (extraneu) și "gestionarea dificultății inerente a subiectului" (intrinsec) ca cele două pârghii reale de proiectare — nu proiecta în jurul unui "germane load" ca buton reglabil direct.

**Contiguitatea spațială/split-attention** (Schroeder & Cenkci 2018, meta-analiză, k=58, N=2426, g=0,63) e unul dintre cele mai solid replicate efecte din toată literatura de multimedia learning, confirmat din nou ca efect de top-nivel în meta-meta-analiza Noetel et al. (2022). Susține direct: textul necesar interpretării unei diagrame trebuie unit spațial cu ea, nu separat prin scroll lung sau printr-o filă/tab distinctă. Aceasta converge cu constatarea din Cluster 5 (benchmarking) că platformele tehnice puternice (Kubernetes, Stripe, MDN) plasează exemplul/diagrama imediat lângă explicația relevantă.

**Semnalizarea/cueing** (Richter, Scheiter & Eitel 2016, meta-analiză) are suport solid, moderat semnificativ de cunoștințele anterioare — efect mai mare pentru novici, aproape dispărut pentru experți (exact tiparul de inversare a expertizei). **Coerența** (Sundararajan & Adesope 2020, meta-analiză) — eliminarea detaliilor "seducătoare" (anecdote tangențiale, imagini decorative) — are suport solid, dar NU se aplică scenariilor concrete de teren ale ManualFC, care sunt direct relevante conceptului predat, nu detalii tangențiale.

**Efectul de modalitate** (audio > text pe ecran, lângă o imagine) e contestat pentru aplicare generală și se referă în principal la conținut animat/audio — **NU se transferă** la formatul ManualFC (fără canal audio, conținut necinematic, citire auto-ritmată), o extrapolare care ar depăși ce a testat efectiv literatura.

**Efectul exemplelor rezolvate** (meta-analiză 2023, domeniul matematicii, g=0,48) are suport solid pentru novici specific, dar mai ales în domenii procedurale (matematică/STEM) — transferul la proza pedagogică abstractă a ManualFC e o extrapolare rezonabilă, nu identic testată.

**Efectul de inversare a expertizei** (Tetzlaff, Simonsmeier, Peters & Brod 2025, meta-analiză, k=176 mărimi de efect/60 studii/N=5924) e descris de autorii înșiși ca "un efect puternic și puternic generalizabil" — dar **asimetric**: beneficiul pentru novici la scaffolding (d=0,505) e mai mare decât costul pentru experți la același scaffolding (d=−0,428). Aceasta e cea mai puternică dovadă disponibilă pentru întrebarea "mod simplificat vs. profund".

**Constatare-cheie de context, adesea omisă:** meta-meta-analiza Noetel et al. (2022, 29 review-uri/1189 studii/78177 participanți) arată explicit că aceste principii, deși solide per ansamblu, sunt **măsurabil mai slabe în contexte auto-ritmate, controlate de cititor (ca o pagină web) decât în contexte cu ritm impus de sistem** (prelegere/video). Cea mai mare parte a canonului clasic CLT/CTML a fost construit pe studii de prelegere/slide-show/video narat, unde cititorul NU controlează ritmul — formatul ManualFC (pagină web derulabilă, auto-ritmată) elimină deja o parte din problema de încărcare extraneică pe care aceste principii au fost inventate să o rezolve. Aplică principiile, dar așteaptă câștiguri mai mici decât sugerează mărimile de efect din laborator.

**Verdict de poziționare text+imagine:** diagramele tactice și imaginile trebuie plasate imediat adiacent (nu într-o galerie de media, nu "vezi figura mai jos" la câteva ecrane distanță, nu în spatele unui click, decât dacă diagrama e genuin suplimentară) paragrafului pe care îl explică. Etichetele esențiale pentru citirea diagramei aparțin diagramei înseși, nu doar unei legende îndepărtate. Aceasta e recomandarea cu cel mai puțin contestat suport meta-analitic din tot acest cluster.

**Verdict expertise reversal — mod simplificat vs. profund:** dovada susține straturi adaptive DUPĂ cunoștințele anterioare, în principiu, dar NU prescrie CUM trebuie livrată acea stratificare — un toggle binar "simplu/profund" e o alegere de implementare, nu o cerință a cercetării. Dat fiind asimetria (sub-scaffolding-ul rănește novicii mai mult decât over-scaffolding-ul rănește experții) și costul de mentenanță al unui sistem cu două trasee paralele de conținut, recomandarea proporțională cu dovada este: **nu construi două trasee paralele de conținut**, ci folosește **disclosure în pagină, controlat de cititor** (secțiuni comprimabile "aprofundează", exemple extinse opționale) — exact mecanismul ales pentru Model C Hybrid (§8, `ExplanationToggle`), nu un mod separat.

---

## 2. Progressive Disclosure, Information Scent, Scanabilitate, Tipografie, Navigare

Constatarea centrală, confirmată din trei unghiuri independente (uzabilitate practician NN/g, psihologie cognitivă a hipertextului, benchmarking structural), este că **progressive disclosure clasic (acordeoane, tab-uri) nu are dovadă de îmbunătățire a învățării** — are dovadă doar de reducere a lungimii *percepute*, cu risc documentat de omisiune completă a conținutului ascuns. Aceasta este exact distincția pe care specificația cere să nu fie confundată: engagement/percepție ≠ învățare.

Scent-ul informațional (Pirolli & Card) rămâne cadrul explicativ pentru *de ce* eșuează multe implementări de disclosure: nu widget-ul e problema, ci calitatea titlului. Un titlu generic ("Detalii", "Mai mult") ucide orice beneficiu de organizare, indiferent dacă informația e într-un acordeon, un tab sau o secțiune vizibilă.

Cercetarea de scanabilitate confirmă modelul "layer-cake" (structură puternică de titluri → scanare eficientă) ca intervenție mai bine susținută decât modelul F-shape (contestat de studii independente). Pentru ManualFC, aceasta înseamnă investiție prioritară în titluri de secțiune descriptive și front-loaded, nu în ascunderea conținutului.

Tipografia converge din trei surse independente (experiment controlat Dyson & Haselgrove, experiment controlat Ling & van Schaik, canonul Bringhurst) pe o fereastră de **60-75 caractere pe linie**, font **16-18px**, line-height **≥1.5** (acesta din urmă e prag de conformitate WCAG 1.4.12, nu doar preferință stilistică).

TOC/navigare internă are dovadă reală de utilitate la lungimea paginilor ManualFC (2000-6000+ cuvinte), dar cu o condiție empirică precisă: un TOC sticky care nu marchează secțiunea curentă este frecvent netrecut cu vederea de utilizatori (constatare directă NN/g) — deci nu orice TOC sticky e automat un beneficiu.

Bara de progres la citire nu are nicio dovadă directă — analogia cu toleranța la așteptare (Nah 2004) este un mecanism psihologic diferit (anxietate în timpul blocării) de citirea activă. Verdict: decorativă, prioritate scăzută.

---

## 3. Retrieval Practice, Spacing, Self-Explanation, Generation Effect, Metacogniție

Aceasta este cea mai importantă secțiune de disciplină anti-fabricare a întregii cercetări. Efectele puternice, bine documentate (testarea practicată g≈0.5-0.9, Adesope et al. 2017; Roediger & Karpicke 2006) **cer producerea efectivă a unui răspuns**, nu doar o invitație de a reflecta. ManualFC nu are (și nu construiește în această fază) un sistem de quiz cu răspuns forțat și feedback — deci aceste efecte puternice NU se transferă automat la un simplu prompt de pagină.

Excepția structural relevantă este **efectul de pre-testare** (Kornell, Hays & Bjork 2009): o întrebare plasată ÎNAINTE de conținutul relevant, chiar dacă cititorul nu poate răspunde corect, produce beneficiu pentru că citirea ulterioară funcționează ca feedback implicit. Acesta este singurul mecanism din literatura de retrieval practice care se potrivește structural cu formatul static al ManualFC (fără JavaScript de colectare a răspunsurilor).

O replicare recentă de înaltă calitate (Harders et al. 2026, preînregistrată) și un eșec direct de replicare a efectului de generare pentru proză conectată (Schindler & Richter 2025, 7 experimente) sunt constatări importante de prudență: NU presupune că "efectul de generare" sau "auto-explicația" se transferă automat la citirea pasivă a unui text expozitiv/factual — o mare parte din conținutul ManualFC este exact de acest tip (fapte despre dezvoltarea copilului, proceduri de antrenor).

Cea mai solidă idee nouă, cu fundamentare teoretică convergentă (pretesting + spacing), este o **suprafață de "recall rapid"** distinctă — nu un rezumat de recitit, ci un set de repere/întrebări la care antrenorul încearcă să răspundă înainte de a vedea răspunsul complet, folosită la o revenire ulterioară (zile/săptămâni). Aceasta obține gratuit componenta de "spațiere în timp" pe care o singură pagină citită o dată nu o poate oferi — pur și simplu pentru că revenirea ulterioară e un comportament natural al utilizatorilor de referință, nu ceva ce trebuie construit ca sistem de repetiție spațiată.

Advance organizers (rezumat/hartă la începutul paginii) au efect mic dar pozitiv și replicat de două ori independent (Luiten et al. 1980, Stone 1983) — o adăugare cu risc scăzut, cost mic, dar care nu trebuie vândută ca lever puternic de retenție.

---

## 4. Accesibilitate (WCAG), Mobil, Expertise Reversal, Adult Learning

Standardele WCAG 2.1/2.2 relevante pentru orice pattern de disclosure (acordeon/tab) sunt verificate direct contra textului normativ W3C, nu din surse secundare: SC 1.4.10 (Reflow), SC 2.5.8 (Target Size Minimum, 24×24px, **AA**) vs. SC 2.5.5 (Target Size Enhanced, 44×44px, **AAA** — frecvent confundat în literatura de blog ca fiind cerință AA, ceea ce NU este), SC 2.4.6 (Headings and Labels), SC 2.4.7/2.4.11 (Focus Visible/Not Obscured), SC 1.4.1 (Use of Color), SC 2.3.3 (AAA, reduced motion). Pattern-ul de referință APG Accordion (buton real, `aria-expanded`, `hidden` pe panourile închise) este contractul minim obligatoriu dacă ManualFC construiește vreun disclosure — checklist-ul complet e reprodus în `EDUCATIONAL_COMPONENT_CONTRACT.md`.

Constatarea NN/g repetată — acordeoanele scad descoperirea conținutului și cresc costul de interacțiune — este confirmată independent de cercetarea de sarcină cognitivă a hipertextului (DeStefano & LeFevre 2007): fiecare decizie de navigare (ce secțiune să deschid) consumă resurse de memorie de lucru, mai mult pentru cititorii cu cunoștințe reduse. Aceasta e o dublă confirmare împotriva ascunderii conținutului esențial pentru antrenorii novici, exact populația cu cel mai mare risc.

Efectul de inversare a expertizei (Kalyuga et al. 2003) este solid în domeniul lui original (sarcini procedurale scurte de laborator) dar NU a fost testat direct pe citire web lungă auto-dirijată. Răspunsul rezonabil, susținut indirect: comprimare reversibilă a elaborării, nu conținut complet diferit pentru cele două audiențe.

Andragogia (Knowles) — teoria "învățării adulților" des invocată în produse educaționale pentru profesioniști — are, conform literaturii proprii (Merriam 2001, Rachal 2002), **suport empiric slab și contestat**, fără o definiție operațională agreată. ManualFC nu va cita andragogia ca justificare științifică pentru decizii de design; unde e folosit un raționament "respectă experiența antrenorului", acesta e etichetat explicit ca euristică de proiectare, nu ca dovadă.

Comprehensiunea pe mobil este aproximativ egală cu desktop pentru text simplu, dar costul (mai ales de timp, nu neapărat de acuratețe) crește la text dificil (NN/g 2016) — relevant direct pentru pasajele tehnice dense ale ManualFC, care ar trebui scrise mai strâns și susținute vizual (diagramă) mai ales pe mobil.

---

## 5. Case-Based Learning, Contrastare, Comunicarea incertitudinii

Structura deja existentă a capitolelor ManualFC (scenariu concret de teren → "Ce știm" → explicație structurată pe 8 subsecțiuni fixe → instrument practic → limite → transfer) se potrivește precis cu pattern-ul validat de literatura de instrucție ghidată-cu-ancoră (Kirschner, Sweller & Clark 2006 combinat cu tradiția de ancorare CTGV/Vanderbilt): un scenariu concret motivează și oferă un reper comun, urmat imediat de explicație structurată explicită — nu descoperire minim-ghidată. **Concluzia directă: NU inversa la "concept întâi"** pentru structura de bază a capitolului. Meta-analizele de învățare bazată pe caz în educație medicală (BMC Med Educ 2025, PLOS ONE 2022) confirmă același tipar: beneficiul e cel mai slab exact quando cazul e lăsat "să vorbească singur", fără debrief structurat — ceea ce ManualFC deja nu face.

O adăugare bine fundamentată, absentă din structura actuală: **exemple contrastante explicite** — o variantă de eroare/eșec ("ce ar face un antrenor greșit aici") plasată lângă scenariul corect, cu corectare explicită (Durkin & Rittle-Johnson 2012; Schwartz & Bransford 1998). Structura actuală are deja o secțiune "Riscuri și formulări de evitat" care acoperă parțial acest rol, dar nu ca o comparație explicită "greșit vs. corect" alăturată.

Comunicarea incertitudinii ("Ce nu putem concluziona") este cea mai riguros fundamentată decizie din întreaga cercetare: literatura de comunicare a riscului (van der Bles et al. 2019) și cea clinică (Simpkin & Armstrong 2019, modelul GRADE) converg pe aceeași concluzie — vizibilitatea structurată a limitelor NU erodează încrederea, dar hedging-ul vag sau ascunderea limitelor într-o secțiune opțională de profunzime **subminează** încrederea pe termen lung, când limitele devin evidente altfel. **Verdict ferm: "Ce nu putem concluziona" rămâne o secțiune obligatorie, vizibilă, în fluxul principal — nu se retrogradează într-o zonă de profunzime opțională.**

Prompt-urile de predicție de tip "ce ai face tu?" cu reveal `<details>/<summary>` sunt susținute ca adăugare ieftină și fără risc, cu condiția să ceară explicit un angajament ("gândește-te la răspunsul tău înainte să extinzi") — fără această formulare, mecanismul de auto-explicație comparativă nu se declanșează, pentru că cititorul poate pur și simplu deschide imediat.

---

## 6. Benchmarking — platforme de coach-education și cross-domain

**Reamintire obligatorie, repetată din matrice:** acest cluster este descoperire de pattern-uri structurale, NU dovadă de eficiență a învățării. Popularitatea sau prestigiul unei platforme nu demonstrează că alegerea ei de design produce învățare mai bună.

Platformele de coach-education fotbalistic inspectate direct (The Coaching Manual, Player Development Project) sunt surprinzător de simple structural: flux liniar unic, fără TOC, fără secțiuni colapsabile, checklist-uri și diagrame intercalate direct în text. FIFA Training Centre și UEFA nu au putut fi inspectate la nivel de pagină (acces restricționat) — raportat onest ca limitare, nu inventat.

Platformele tehnice/de referință puternice inspectate direct (MDN Web Docs, Kubernetes Docs, Stripe Docs) converg independent pe un pattern: **orientare rapidă/exemplu concret imediat după titlu/TOC, detaliul complet urmează pe aceeași pagină** — nu într-o filă separată, nu într-o rută separată pentru "versiunea scurtă". UpToDate (referință medicală, descriere din documentația editorială proprie — nu pagină inspectată direct, sursă gated) oferă cel mai relevant model pentru separarea explicită rapid/profund: o secțiune "Summary and Recommendations" etichetată clar, repetată **atât la începutul cât și la sfârșitul** documentului lung — nu ascunsă, nu pe rută separată.

Niciuna dintre platformele puternice inspectate nu separă "răspuns rapid" de "fundal profund" prin rute complet separate ale ACELUIAȘI subiect — separarea prin rută diferită apare doar la Stripe, dar pentru variante de INTEGRARE diferite (caz de utilizare diferit), nu pentru profunzime diferită a aceluiași conținut.

---

## 7. Ce NU este susținut de cercetare (watchlist explicit)

Pentru a respecta regula explicită împotriva falsei precizii și a conflației engagement↔învățare:

- **Acordeoane/tab-uri pentru conținut esențial de lecție** — NU susținute; risc documentat de omisiune.
- **F-pattern ca lege universală de scanare** — contestat, nu trata ca literă de lege.
- **Bară de progres la citire** — nicio dovadă directă de beneficiu de învățare; decorativă/motivațională cel mult.
- **Andragogia ca fundamentare științifică** — suport empiric slab și contestat; folosește doar ca euristică etichetată explicit.
- **Reguli numerice fixe fără sursă** (ex. "paragraf sub 50 de cuvinte") — nicio sursă verificată susține praguri rigide; folosește intervale raționate, nu cifre false-precise.
- **Efectul de generare / auto-explicație pentru conținut factual pur** — replicări recente nu găsesc beneficiu; nu presupune transfer automat.
- **Un prompt de reflecție pasiv, fără angajament explicit, ca "retrieval practice"** — eticheta e falsă; efectul real cere producere activă a unui răspuns.

---

## 8. Sinteză pentru decizia de arhitectură

Cele mai puternice, convergente concluzii care alimentează Gate 2-4:

1. Nucleul procedural (ce faci, ce spui, ce verifici) rămâne **întotdeauna vizibil**, pentru toți cititorii — niciodată în spatele unui click.
2. Elaborarea/rațiunea de fundal poate fi **comprimabilă** (nu ascunsă implicit), cu un mecanism reversibil pentru cititorii experimentați — nu un produs separat.
3. Diagrama/imaginea stă **lângă** explicația ei, nu deasupra unui bloc lung de text și nu într-o filă separată.
4. "Ce nu putem concluziona" rămâne **vizibil în fluxul principal**, niciodată retrogradat într-o secțiune opțională de profunzime.
5. TOC justificat la această lungime, dar trebuie să marcheze secțiunea curentă activ.
6. O suprafață distinctă de "recall rapid" (recuperare, nu recitire) este cea mai bine fundamentată adăugare nouă absentă din arhitectura actuală.
7. Structura scenariu→explicație existentă e deja aliniată cu literatura de instrucție ghidată — nu se inversează ordinea.
8. O comparație explicită "greșit vs. corect" este o adăugare bine fundamentată, parțial absentă acum.

Aceste concluzii sunt traduse în principii testabile în `MANUALFC_EDUCATIONAL_DESIGN_PRINCIPLES.md` (Gate 2) și apoi în arhitecturi concurente în `MANUALFC_EDUCATIONAL_PAGE_STANDARD_V1.md` (Gate 3-4).
