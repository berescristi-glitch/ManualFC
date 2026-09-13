# MANUALFC PREMIUM PRODUCT MASTER AUDIT

**Data auditului:** 14 august 2026  
**Produs auditat:** `https://manualfc.vercel.app/`  
**Baseline pedagogic:** `4bf2064`  
**Sursă deployment:** `e59f10d`  
**Verdict:** `STRONG_PEDAGOGICAL_PRODUCT / PRE_COMMERCIAL_TRANSFORMATION_REQUIRED`

## 1. Executive verdict

ManualFC are deja partea cel mai greu de fabricat: o poziție pedagogică distinctă, un model canonic riguros, limbaj pentru copil legat de mecanismul profesional și un Gold Standard care conectează principiu, exercițiu, ședință și evaluare. Nu este un catalog generic. Este începutul credibil al unui sistem de decizie pentru antrenorul-pedagog.

Produsul nu este încă pregătit pentru o promisiune premium plătită. În prezent, valoarea există mai ales în text și în schema internă; utilizatorul trebuie să o extragă prin lectură lungă. Field Mode nu există, problema-first are o singură pagină fixture, EX-0004 și EX-0005 anunță public că diagrama este încă în lucru, ședințele nu rezolvă determinist efectivele 8–18, iar evaluarea nu poate fi completată sau urmărită. Multimedia, search, salvare, offline și continuitatea de utilizare lipsesc.

Direcția recomandată nu este un redesign cosmetic și nici construirea unui SaaS generic. ManualFC trebuie să devină un **sistem evidence-aware care reduce timpul dintre „observ ceva la copii” și „știu ce testez, ce spun, ce organizez și cum verific transferul”**. Primele investiții sunt: Problem Engine, Presentation Layer V2, Field Mode + Group Configurator, completarea vizuală/multimedia și bucla Session Workspace → Assessment.

## 2. Current product maturity

| Dimensiune | Scor /10 | Judecată |
|---|---:|---|
| Conținut | 8.2 | Bogat, riguros, dar neuniform și incomplet ca produs total |
| Pedagogie | 9.0 | Diferențiatorul cel mai puternic |
| Practicitate | 6.0 | Gold Standard utilizabil, dar realitatea efectivelor rămâne subrezolvată |
| Arhitectură informațională | 5.5 | Reflectă structura creatorilor mai mult decât joburile antrenorului |
| UX | 6.0 | Clară la nivel de pagină; slabă la nivel de flux recurent |
| UI | 7.5 | Coerentă și distinctă, cu câteva template-uri mature |
| Premium vizual | 6.5 | Homepage puternic; paginile lungi și lipsa multimedia rup promisiunea |
| Mobile | 7.0 | Responsiv și lizibil; nu este încă operabil cu o mână pe teren |
| Field use | 4.5 | Conținut relevant, dar fără mod de teren, timer, pack sau configurator |
| Multimedia | 2.5 | SVG static parțial; video/animație practic absente |
| Discoverability | 3.5 | Navigație de bază; fără search, filtre sau taxonomie expusă |
| Diferențiere | 7.5 | Model pedagogic rar; experiența încă nu îl face imediat tangibil |
| Monetizare | 3.5 | Valoare latentă, fără package, loop sau paywall logic |
| Scalabilitate | 6.5 | Date/schema bune; presentation layer și tooling insuficiente |

**Nivel de maturitate:** beta editorială solidă, acceptată pentru pilot de teren; pre-comercială ca produs premium recurent. Scorurile sunt judecăți profesionale pe baza rubricii cerute, nu rezultate de piață (`PRACTICE_HEURISTIC`).

## 3. What is genuinely exceptional already

1. **Copilul precede exercițiul.** Mesajele nu sunt comenzi izolate; sunt legate de ce vede, decide și poate înțelege copilul.
2. **Separarea observației de diagnostic.** „Nu presupune” este o disciplină de coaching, nu copy decorativ.
3. **Trasabilitatea epistemică.** Claims, limitări și aplicabilitate U11 sunt păstrate fără a simula certitudine.
4. **Gold Standard ca lanț complet.** Problemă/concept → cinci exerciții → două ședințe → ASM-0001 → transfer.
5. **Voce editorială proprie.** „Înțelege copilul. Antrenează jocul.” este demonstrată prin structură, nu doar slogan.
6. **Model data-driven.** 25 principii, 25 capitole, cinci exerciții, două ședințe și evaluarea au baze reutilizabile.

## 4. What currently prevents premium perception

- Pagina promite un produs multimedia, dar EX-0004/EX-0005 afișează „diagramă tactică… încă în lucru”; în date, asseturile statice, animațiile și cadrele PDF sunt `PENDING`.
- Pagini de 1.700–2.480 de cuvinte sunt livrate aproape liniar, fără rezumat operațional, reading map sau progresive disclosure.
- „Am nevoie acum” este o singură temă; problem-first nu este încă o funcție de produs.
- Navigația `Începe aici / Volume / Principii / Am nevoie acum / Gold Standard` cere utilizatorului să înțeleagă modelul intern înainte să-și rezolve problema.
- `/design-system`, `/fixture-mdx`, `/exercitii/2v1-unghi-de-suport` și pagina fixture de problemă sunt publicabile direct. Lipsa linkurilor publice nu înlocuiește eliminarea lor din buildul Production.
- Nu există search, filtre, favorite, istoric, offline, session pack, progres sau instrument interactiv.
- Autoritatea metodologică este reală, dar „cine, cum, ce a fost validat și ce nu” nu are încă un trust layer compact pentru utilizator.

## 5. Content quality audit

### Capitole și principii

Capitolele sunt puternice prin cauzalitate și prudență. Volumul 02 este însă foarte dens: opt capitole au aproximativ 1.700–2.480 cuvinte fiecare. Principiile repetă deliberat concept, observație, mesaj, „de ce” și dovezi. Repetarea este adesea `NECESSARY_REINFORCEMENT` în modelul canonic, dar devine `UX_REDUNDANCY` când toate straturile apar simultan.

### Exerciții

Cele cinci exerciții oferă obiectiv, relație numerică, dimensiuni, mesaj, reguli cu motiv, șapte rationale, erori, regresie/progresie și transfer. Calitatea pedagogică este peste media unei biblioteci de drills. Lipsesc însă rezumatul „gata de montat”, echipamentul total cuantificat, poziția antrenorului vizual, rotația pentru fiecare efectiv și vizualurile complete EX-0004/EX-0005.

### Ședințe

SES-0001/0002 au progresie și minutaj coerent, dar nu sunt încă robuste pentru lumea reală. Intervalele declarate 9–16 exclud cerințele explicite 8 și 18; nu există configurații exacte pentru 8/10/12/14/16/18, un versus doi antrenori, trei întârziați, spațiu redus sau material insuficient. `players_range.note` descrie principiul, nu răspunsul operațional.

### Evaluare

ASM-0001 distinge corect performanța de învățare și evită etichetarea copilului. Ca produs este însă o pagină de lectură: antrenorul nu poate marca rapid, data observația, păstra un identificator anonim, compara două momente sau primi următorul pas.

## 6. Content structure audit

Modelul recomandat este cu trei stări, dar nu trei silozuri:

1. **Acum, pe teren:** decizia imediată — observă, spune, montează, ajustează, verifică.
2. **Înțelege mecanismul:** percepție, decizie, tactică, pedagogie și risc.
3. **Verifică dovezile:** claims, surse, aplicabilitate și limite.

Ordinea implicită trebuie să fie „acțiune sigură → mecanism → dovezi”, cu acces permanent la toate. Canonical data model rămâne bogat; presentation layer compune subseturi în funcție de context. Nimic critic pentru siguranță, mesaj sau interpretare nu intră într-un accordion închis implicit.

## 7. Information architecture audit

Arhitectura actuală este coerentă editorial, dar nu acoperă joburile recurente. Recomandarea V2:

- **Rezolvă pe teren** — intrare problem-first: „Ce observi?”
- **Planifică** — ședințe, configurator de grup, session builder determinist, pack.
- **Învață** — traseul pedagogic în volume și competențe.
- **Bibliotecă** — principii, exerciții, ședințe, evaluări, filtre și search.
- **Spațiul meu** — salvări, planul de joi, istoric și reflecții; numai după conturi.

„Gold Standard” rămâne marcă editorială, dar primește explicația „modul complet demonstrativ”. „ASM” este ascuns din titlul utilizatorului și păstrat ca ID tehnic secundar. „Principiu canonic” devine „principiu verificat ManualFC”, cu sensul explicat.

## 8. UX audit

Homepage-ul răspunde bine la „pentru cine” și diferențiază pedagogia, dar nu demonstrează în primele 10 secunde rezultatul concret: cât de repede ajunge antrenorul de la o observație la o intervenție. CTA-urile „Începe să înveți” și „Am nevoie acum” sunt bune; al doilea trebuie să arate imediat o selecție de comportamente observabile, nu o singură temă.

Fluxurile au linkuri corecte, însă nu păstrează starea utilizatorului: nu există „continuă”, „salvat pentru joi”, „folosit pe teren” sau „reflectează după sesiune”. Premium înseamnă reducerea muncii antrenorului între vizite, nu doar calitatea fiecărei pagini.

## 9. UI / visual audit

Identitatea bleumarin–auriu, tipografia editorială, fotografia hero și layouturile de principiu sunt memorabile. Premium-ul scade pe paginile operaționale: mult text pe fundal alb, puține repere vizuale, aceeași greutate pentru instrucțiune și rationale, lipsă de media și lipsă de sticky action bar. Aurul este folosit rezonabil; problema nu este ornamentul, ci ierarhia.

Limbaj vizual V2:

| Rol | Semnal vizual | Regula |
|---|---|---|
| Acțiune pe teren | bleumarin compact + accent auriu | maxim 6 informații, scanare sub 30 secunde |
| Mesaj copil | ghilimele + icon voce | text exact, fără parafrază ascunsă |
| Observație | cerc/ochi + numerotare | fapt observabil, nu diagnostic |
| Ipoteză | contur punctat | exprimă incertitudine |
| Exercițiu | mini-teren + parametri | cifrele înaintea rationale-ului |
| Ședință | timeline | timp, tranziție, material și status |
| Evaluare | scală neutră | fără roșu-verde sau etichete de copil |
| Dovezi | strat discret | nivel, aplicabilitate, limită, surse la cerere |

## 10. Mobile / field audit

Auditul browser-first a parcurs nouă template-uri la 1440 și 390 px, completat de acceptanța live existentă la 1280/768. Paginile sunt responsive și lizibile. La 390 px, însă, SES-0001 și ASM-0001 devin scrolluri foarte lungi; utilizatorul nu poate ajunge rapid la „ce spun acum”. Nu există control cu degetul mare, ecran persistent, timer, next exercise, luminozitate/contrast de teren sau offline.

### Field Mode propus

- activat explicit, nu detectat automat;
- sticky bar jos: `Înapoi / Timer / Următorul`;
- card 1: setup + diagramă + material;
- card 2: mesaj exact + un singur comportament observat;
- swipe vertical: regresie → progresie → stop condition;
- ecranul rămâne treaz doar cu acord; font minim 18 px; control ≥48 px;
- video mut, loop 8–15 secunde, caption și poster static;
- conținutul salvat disponibil offline;
- fără date nominale despre copii în MVP.

**Test o singură mână / 30 secunde:** astăzi `NO`; cu Field Mode și configurator `YES` este o țintă verificabilă.

## 11. Multimedia audit

### Multimedia Content Matrix

| Familie | Tactical loop | Animation | Coach explainer | Field example | Before/after | Match example | Prioritate |
|---|---|---|---|---|---|---|---|
| Probleme | necesar | opțional | opțional | necesar | necesar | opțional | P0 |
| Principii tactice | necesar | necesar când dinamice | 45–90s | util | util | necesar | P1 |
| Principii pedagogice | rar | rar | necesar | necesar | necesar | util | P1 |
| EX-0001–0005 | necesar | 20–40s | util | necesar | util | transfer la EX-0005 | P0 |
| SES-0001/0002 | overview | timeline animat opțional | 60–90s | necesar | nu | final game | P1 |
| ASM-0001 | micro-demo per criteriu | nu | 60s | necesar | necesar | necesar | P1 |

Standard video: fără autoplay cu sunet; loops tactice autoplay numai mute și cu `prefers-reduced-motion`; captions și transcript; 0.5×/1×/1.5×; poster static; fullscreen; download controlat; overlay cu roluri și timp; rezumat textual echivalent. Offline numai pentru materialele salvate.

## 12. Principles audit

Template-ul actual este cel mai matur vizual, dar doar principiul de referință folosește integral detalierea specială; restul compun fallbackuri. Template ideal:

`Problemă observabilă → idee într-o propoziție → ce spui → loop tactic → aplică pe teren → ce poate însemna → mecanism → erori/adaptări → dovezi și limite → următorul pas`.

CTA-ul principal este „Aplică pe teren”, nu „citește mai mult”. Indexul de 25 principii are nevoie de grupare pe job/comportament și search, nu doar categorii editoriale.

## 13. Exercises audit

Un exercițiu trebuie înțeles în 15–30 secunde. Above-the-fold V2:

`Titlu + obiectiv / 2v1 / 12×10m / 3 jucători / 8 min / diagramă-loop / mesaj exact / observă acest lucru / Pornește Field Mode`.

Sub fold: montare, rotație, reguli, stop condition, regresie, progresie, erori, rationale, dovezi. EX-0004 și EX-0005 nu pot rămâne premium până nu au vizualuri. Echipamentul trebuie cuantificat, nu doar enumerat.

## 14. Sessions audit

Lipsuri P0:

- matrice exactă 8/10/12/14/16/18 copii;
- suprafețe și material total;
- rolul unui versus doi antrenori;
- ce fac jucătorii rămași și cum se evită cozile;
- scenarii „3 întârzie”, „teren mai mic”, „lipsește o poartă”, „exercițiul nu funcționează”;
- hartă completă a suprafeței și tranzițiilor;
- variante de 60 și 75 minute;
- session pack print/offline.

SES-0001 declară reflecție înaintea jocului liber, deși evaluarea recomandă observația în jocul final; ordinea merită testată în pilot (`NEEDS_RESEARCH`), nu schimbată din birou.

## 15. Assessment audit

ASM-0001 trebuie să devină unealtă, dar cu privacy by design:

- dată, sesiune, criteriu, nivel, notă scurtă;
- identificator local/pseudonim opțional, fără nume implicit;
- trend numai după observații repetate, fără scor global al copilului;
- recomandare deterministă spre exercițiul asociat;
- export/ștergere și retenție configurabilă;
- cont de club numai cu roluri, temei legal, DPA, audit și politici pentru minori.

Orice longitudinal child data este `NEEDS_RESEARCH` juridic și operațional. Nu se lansează înaintea DPIA/consimțământului/rolurilor clare.

## 16. Gold Standard audit

Gold Standard este dovada cea mai bună a produsului și trebuie transformat într-un demo complet, nu într-o denumire internă. Puncte forte: coerență, progresie, transfer, legături 9/9. Puncte slabe: o singură temă, două vizualuri lipsă, lipsă Field Mode, fără instrumente persistente. Următorul Gold Standard nu trebuie produs înainte ca primul să fie complet multimedia și validat pe teren.

## 17. Search / discovery opportunities

Taxonomia recomandată:

- observație/comportament;
- problemă de joc;
- moment: posesie, pierdere, câștigare, apărare;
- percepție și decizie;
- format numeric;
- jucători, timp, spațiu, echipament;
- nivel de complexitate;
- scop pedagogic;
- tip de material;
- dovadă/aplicabilitate.

MVP: căutare lexicală + filtre deterministe. Semantic search este `EXPERIMENT`, cu rezultate limitate la ID-uri canonice și explicația „de ce acest rezultat”; fără generare metodologică liberă.

## 18. New product capabilities

1. Problem Engine.
2. Field Mode.
3. Group Configurator.
4. Session Workspace determinist.
5. Interactive Assessment local-first.
6. Saved packs/offline.
7. Search și filtre.
8. Coach progress orientat pe competențe, nu streak.
9. Club curriculum/share layer.

## 19. Missing content

| Titlu propus | Problema utilizatorului | Plasare | Dovezi necesare | Prioritate |
|---|---|---|---|---|
| Organizare pentru 8–18 copii | „Cum împart grupa?” | fiecare exercițiu/ședință | pilot logistic | P0 |
| Demonstrația antrenorului | demonstrația poate dicta sau confuza | Vol. 04 + Field | research motor learning | P1 |
| Plan de urgență al ședinței | întârzieri/material/teren | session template | practică + pilot | P0 |
| Managementul timpului de joc | echitate și dezvoltare | viitor Vol. 08 | federații + safeguarding | P1 |
| Conversația cu părintele | conflict/așteptări | viitor Vol. 09 | safeguarding/club policy | P1 |
| Încredere și anxietate | copilul evită sau se blochează | problem library | research psihologie | P1 |
| Feedback post-meci | separă scorul de învățare | Vol. 08 | coach education | P1 |
| Prevenție și răspuns la accidentare | siguranță reală | tools/safeguarding | ghiduri medicale oficiale | P0 |

## 20. Competitive benchmark

| Produs | Ce face bine (`VERIFIED`) | Limită observabilă | Ce învață ManualFC | Ce nu copiază |
|---|---|---|---|---|
| FIFA Training Centre | video + rezumat + diagrame; planuri downloadabile; filtre după intenție/tip | orientare vastă, nu specific U11 român | media echivalentă și field packs | autoritate generică fără diferențiere locală |
| The Coaching Manual | sute de sesiuni, planner, season plans, folders, print, search, iOS/Android | avantajul este volum/tooling, nu neapărat explicația copilului | workflow, salvare, share | cursa pentru cea mai mare bibliotecă |
| Touchtight | 1.500+ video, filtre jucători/spațiu, offline, planner și club tools | risc de all-in-one și complexitate | offline, filtre și vizualuri pitchside | management de club înaintea nucleului pedagogic |
| Player Development Project | probleme reale, research, mentoring, cursuri și parteneriate | experiență fragmentată între content/courses/services | coach development și real-world problems | dependența de comunitate ca valoare principală |
| Barça Education | autoritate, programe structurate, feedback, certificare | orientare formală/elite, cost și durată mari | trasee și proof of completion | imitarea prestigiului sau certificare prematură |

Surse oficiale consultate: [FIFA downloads](https://www.fifatrainingcentre.com/en/downloadable-session-plans-now-available.php), [FIFA grassroots](https://www.fifatrainingcentre.com/en/practice/grassroots.php), [TCM features](https://www.thecoachingmanual.com/features), [Touchtight app](https://www.touchtight.com/app), [PDP Academy](https://academy.playerdevelopmentproject.com/), [PDP school partnerships](https://playerdevelopmentproject.com/school-partnerships/), [Barça Education](https://barcainnovationhub.fcbarcelona.com/education/).

## 21. Premium benchmark

- Duolingo arată valoarea unui traseu unic și a unităților mici; ManualFC preia claritatea progresului, nu streakuri sau mascote.
- Khan Academy arată progres legat de mastery și controlul educatorului; ManualFC păstrează antrenorul ca decident.
- Coursera arată valoarea downloadului și gestionării conținutului offline; pentru teren, aceasta este funcție de bază, nu bonus.

Surse: [Duolingo learning path](https://blog.duolingo.com/how-well-does-duolingo-teach-english/), [Duolingo mini-units](https://blog.duolingo.com/intermediate-mini-units/), [Khan mastery progress](https://support.khanacademy.org/hc/en-us/articles/360031123551-How-can-I-monitor-mastery-progress-), [Coursera offline](https://blog.coursera.org/mobile-offline-features/).

## 22. Monetization architecture

| Nivel | Valoare livrată | Nu doar „acces” |
|---|---|---|
| Open | filosofie, onboarding, exemple selectate, un diagnostic problem-first | dovedește metoda și încrederea |
| Coach | biblioteca completă, Field Mode, packs, offline, salvări | economisește timp și îmbunătățește intervenția |
| Coach Pro | configurator, builder determinist, evaluări și reflecții | transformă conținutul în workflow recurent |
| Academy/Club | curriculum, colecții comune, roluri, QA metodologic, progresul antrenorilor | consistență între echipe, fără ranking de copii |

Disponibilitatea de plată, limitele planurilor și prețul sunt `HYPOTHESIS`; necesită interviuri și teste. Core paid value trebuie să fie field workflow + adaptation, nu blocarea cunoașterii de bază despre siguranța copilului.

## 23. Retention model

Antrenorul revine pentru: pregătirea antrenamentului, pachetul salvat, utilizarea pe teren, observația post-sesiune și următoarea adaptare. Loop:

`observă problema → salvează planul → rulează Field Mode → notează rezultatul → primește următorul pas canonic → revine la următoarea ședință`.

Newsletterul și conținutul nou susțin retenția, dar nu sunt motorul principal.

## 24. Product moats

1. Knowledge graph problemă–cauză testabilă–mesaj–exercițiu–evaluare–transfer.
2. Developmental adaptation engine pentru 10–11 ani, fără separare rigidă 2015/2016.
3. Evidence layer cu limite și aplicabilitate.
4. Group configuration rules validate pe teren.
5. Field validation data agregate, fără a expune copii.
6. Curriculum și multimedia coerente, nu clipuri izolate.

## 25. What NOT to build

- generator AI liber de ședințe;
- feed social generalist;
- leaderboards pentru copii sau antrenori;
- CRM, plăți și management complet de club;
- motor 3D complex înaintea completării vizualurilor de bază;
- certificare proprie înainte de validarea curriculară și parteneri credibili;
- tracking nominal al copiilor înainte de privacy/legal design;
- zece planuri comerciale sau paywall pe safeguarding.

## 26. Page-by-page audit

| Pagină/tip | Scop | Forță | Slăbiciune | Recomandare | Prioritate |
|---|---|---|---|---|---|
| Homepage | orientare/conversie | brand și filosofie memorabile | demonstrează insuficient workflow-ul | demo problem-first în primul scroll | P0 |
| Începe aici | onboarding | principiu clar | nu personalizează următorul pas | onboarding după job și timp disponibil | P1 |
| Volume index | traseu | ordine pedagogică bună | doar 4/10 publice | progres și „de ce acum” | P1 |
| Volume landing | capitole | simplu | puțin context operațional | outcomes + timp + continuă | P2 |
| Capitol | învățare profundă | calitate și surse | densitate 500–2.480 cuvinte | summary, anchors, reading mode | P0 |
| Principii index | discovery | 25 intrări reale | scanare grea | filtre după observație/job | P0 |
| Principiu | mecanism | cel mai bun template | fallback neuniform | template V2 și CTA teren | P0 |
| Gold Standard | demo complet | legături și coerență | jargon de marcă, o temă | explicare + progress map | P1 |
| Quick Mode | intervenție rapidă | model foarte bun | o singură problemă | Problem Engine | P0 |
| Exercițiu | rulare | rationale excepțional | first viewport lent, media incompletă | field summary + vizual + configurator | P0 |
| Ședință | plan | minutaj și progresie | realitatea efectivelor incompletă | Session Workspace + contingencies | P0 |
| Assessment | verificare | criterii prudente | doar text | tool local-first | P1 |
| Problem fixture | demo Mode B | structură promițătoare | fixture public, fără h1 principal | scoate din prod; înlocuiește cu date canonice | P0 |
| Design/MDX fixtures | QA intern | utile dezvoltării | accesibile public | exclude din build Production | P0 |

## 27. Template V2 proposals

| Tip | Current canonical fields → strat „Teren” | „Înțelege” | „Dovezi” |
|---|---|---|---|
| Principle | child wording, observable, exercise links | concept, rationale, errors | claims, sources, limits |
| Exercise | players/field/time/equipment, message, steps, regression | problem, decision, 7 rationales | sources, uncertainty, transfer status |
| Session | timeline, stations, totals, contingencies | sequence rationale, observation | source links, pilot status |
| Assessment | criteria, levels, next action | performance vs learning | limits, privacy, transfer status |
| Problem | observation, test, say, modify, verify | possible causes, mechanism | evidence confidence, unknowns |

Schema actuală se extinde numai cu presentation metadata și reguli logistice; nu se duplică conținutul.

## 28. Wireframes

### Homepage

`HEADER → HERO/value → „Ce observi?” selector → rezultat demonstrativ → cum funcționează în 6 pași → Gold Standard proof → trust/evidence → pentru coach/club → CTA`.

### Principiu

`PROBLEMĂ → IDEE → CHILD CUE → TACTICAL LOOP → APLICĂ PE TEREN → OBSERVĂ/IPOTEZE → MECANISM → ADAPTĂRI → DOVEZI → NEXT`.

### Exercițiu

`FIELD SUMMARY sticky → DIAGRAM/LOOP → START TIMER → SETUP → CUE + OBSERVE → RULES → REGRESS/PROGRESS → ERRORS → WHY → EVIDENCE → NEXT`.

### Ședință

`READINESS CHECK → GROUP CONFIG → SURFACE MAP → TIMELINE → START FIELD MODE → SEGMENT CARDS → CONTINGENCIES → ASSESS → REFLECT/EXPORT`.

### Assessment

`CONTEXT/DATE → CRITERION QUICK SELECT → LEVEL + NOTE → SAVE LOCALLY → NEXT EXERCISE → LIMITS/PRIVACY → HISTORY`.

### Problem page

`OBSERVAȚIE → NU PRESUPUNE → TEST RAPID → CE SPUI → CE MODIFICI → EXERCIȚIU → ȘEDINȚĂ → CE VERIFICI → DE CE/DOVEZI`.

## 29. Quick wins

1. Exclude cele trei fixture/lab routes din Production.
2. Înlocuiește termenii ASM și canonic în UI.
3. Adaugă summary operațional la începutul capitolelor lungi.
4. Adaugă anchors/sticky contents pe pagini lungi.
5. Mută parametrii exercițiului înaintea descrierii.
6. Cuantifică echipamentul.
7. Adaugă „ce observi acum” în primul viewport.
8. Marchează durata estimată de lectură/pregătire.
9. Explică Gold Standard într-o propoziție.
10. Adaugă CTA „Aplică pe teren”.
11. Completează SVG-urile EX-0004/EX-0005.
12. Publică Field Card print pentru EX-0001–0005.
13. Adaugă o hartă de progres Gold Standard.
14. Separă „fapt observat” de „ipoteză” consecvent.
15. Adaugă trust strip: metodă, surse, limitări, safeguarding.

## 30. Strategic projects

| Proiect | Valoare | Complexitate | Prioritate |
|---|---|---:|---|
| Problem Engine | cel mai scurt drum spre acțiune | medie | P0 |
| Presentation Layer V2 | face valoarea canonică utilizabilă | medie | P0 |
| Field Mode + Group Configurator | diferențiator pitchside | mare | P0 |
| Multimedia Standard + Pipeline | înțelegere rapidă și premium | mare | P1 |
| Session Workspace | retenție și monetizare | mare | P1 |
| Assessment Engine | buclă de învățare | mare/privacy | P1 |
| Search/Taxonomy | discovery la scară | medie | P1 |
| Offline/PWA | robustețe pe teren | medie | P1 |
| Club Curriculum Layer | valoare B2B | foarte mare | P2 |

## 31. Prioritized roadmap

### Phase A — Product hygiene și UX foundation

Fixture cleanup, IA V2, terminology, summaries, anchors, analytics de cercetare doar după consent design. **Needed before commercial launch.**

### Phase B — Premium content templates

Principle/Exercise/Session/Problem V2, EX-0004/5 visuals, field cards, group matrices pentru Gold Standard. **Needed before launch.**

### Phase C — Field experience

Field Mode, Group Configurator, offline packs, timer și contingencies. **Needed before paid promise.**

### Phase D — Multimedia

Pipeline, tactical loops, exercise animation, captions, field examples. **Launch cohort minim; extindere post-launch.**

### Phase E — Workflow și personalization

Saved plans, Session Workspace, local-first assessment, progress. **Post-launch/experiment.**

### Phase F — Commercial and club

Packaging, billing, roles, shared curriculum, reporting. **După validarea valorii cu antrenori.**

## 32. Pre-commercial requirements

- zero fixture sau placeholder public;
- Gold Standard complet vizual și testat pe teren;
- group configs pentru efective reale;
- Field Mode funcțional offline pe telefon;
- problem-first cu minimum 8–12 probleme validate;
- search și filtrare de bază;
- trust/authorship/methodology page;
- privacy, terms, cookie/analytics decision și safeguarding review;
- onboarding și sample-to-paid journey;
- minimum două runde de usability/field testing și interviuri willingness-to-pay;
- suport, export și recuperare date definite.

## 33. Future expansion

Volumele 05–10, mai multe Gold Standards, curriculum anual, club layer, coach competencies, assessment longitudinal și certificare cu partener. Acestea sunt dependente de validarea nucleului, nu justificări pentru amânarea Field Mode.

## 34. Top 20 highest-value recommendations

| # | Recomandare | Clasă | Impact/Efort/Risc | Efect comercial |
|---:|---|---|---|---|
| 1 | Problem Engine | PRODUCT_IDEA | foarte mare/mediu/mediu | diferențiere + activation |
| 2 | Field Mode | PRODUCT_IDEA | foarte mare/mare/mediu | core paid value |
| 3 | Group Configurator 8–18 | PRODUCT_IDEA | foarte mare/mediu/mediu | moat practic |
| 4 | Presentation Layer V2 | PRACTICE_HEURISTIC | foarte mare/mediu/mic | premium perception |
| 5 | Completează EX-0004/5 media | VERIFIED gap | mare/mediu/mic | launch credibility |
| 6 | Session contingencies | VERIFIED gap | mare/mediu/mic | field trust |
| 7 | Field/session packs offline | PRODUCT_IDEA | mare/mediu/mic | retention/paid |
| 8 | Search + filters | PRODUCT_IDEA | mare/mediu/mic | discoverability |
| 9 | Assessment local-first | PRODUCT_IDEA | mare/mare/mare | retention/moat |
| 10 | Exclude fixtures din prod | VERIFIED gap | mare/mic/mic | trust |
| 11 | Tactical loop pipeline | PRODUCT_IDEA | mare/mare/mediu | premium/differentiation |
| 12 | Quantified equipment/setup | VERIFIED gap | mare/mic/mic | practicality |
| 13 | Problem library 8–12 teme | NEEDS_RESEARCH | mare/mare/mediu | activation |
| 14 | Saved „antrenamentul de joi” | PRODUCT_IDEA | mediu/mediu/mic | retention |
| 15 | Coach progress by competency | HYPOTHESIS | mediu/mare/mediu | retention |
| 16 | Trust/evidence layer compact | PRACTICE_HEURISTIC | mediu/mic/mic | conversion |
| 17 | Session builder determinist | PRODUCT_IDEA | mare/mare/mediu | Pro value |
| 18 | Field usability research | NEEDS_RESEARCH | foarte mare/mediu/mic | reduce product risk |
| 19 | Packaging interviews/tests | NEEDS_RESEARCH | mare/mediu/mic | pricing confidence |
| 20 | Club curriculum layer | HYPOTHESIS | mare/foarte mare/mare | B2B expansion |

### Top 5 transformational bets

1. **Problem Engine.** De ce: transformă filosofia în acțiune. Valoare: răspuns sigur în minute. Diferențiere: lanț cauzal evidence-aware. Monetizare: activation pentru Coach. Efort/risc: mediu/mediu.
2. **Field Mode + Group Configurator.** De ce: rezolvă realitatea de lângă teren. Valoare: operare cu o mână și efectiv real. Diferențiere: reguli logistice validate. Monetizare: core paid. Efort/risc: mare/mediu.
3. **Presentation Layer V2.** De ce: eliberează valoarea datelor existente. Valoare: 30 secunde sau aprofundare la alegere. Diferențiere: aceeași sursă, trei contexte. Monetizare: premium perception. Efort/risc: mediu/mic.
4. **Multimedia completă, nu decorativă.** De ce: fotbalul este dinamic. Valoare: vede timingul, nu îl ghicește. Diferențiere: loop + explicație + transfer. Monetizare: perceived value. Efort/risc: mare/mediu.
5. **Session Workspace → Assessment loop.** De ce: creează revenirea. Valoare: planifică, rulează, observă, adaptează. Diferențiere: coaching development, nu content consumption. Monetizare: Pro/Club. Efort/risc: foarte mare/mare, mai ales privacy.

## 35. Final recommended product architecture

**Diferențiator într-o propoziție:** ManualFC este sistemul pentru antrenorii U11 care transformă un comportament observat pe teren într-o ipoteză prudentă, o intervenție explicată, o sarcină adaptabilă și o verificare a transferului — cu copilul înaintea exercițiului.

Arhitectura finală are trei motoare conectate:

1. **Decision Engine:** observație → cauze testabile → mesaj → acțiune.
2. **Learning Engine:** principii → traseu → competențe ale antrenorului → dovezi.
3. **Field Engine:** configurare → ședință → Field Mode → evaluare → adaptare.

Biblioteca și multimedia alimentează motoarele; contul și club layer le păstrează și le distribuie. Monetizarea se așază peste economie de timp, adaptare și continuitate, nu peste un zid arbitrar de articole.

> Dacă implementăm recomandările, ManualFC devine un copilot metodologic pentru antrenorul de copii: începe cu ceea ce observă pe teren, îl ajută să nu confunde comportamentul cu diagnosticul, îi oferă un mesaj exact și o sarcină justificată, adaptează organizarea la grupa reală și îl conduce până la verificarea transferului. Acasă funcționează ca traseu de formare; înainte de antrenament ca workspace; lângă teren ca instrument rapid, offline; după antrenament ca memorie profesională și punct de reflecție. Produsul nu concurează prin numărul de exerciții, ci prin coerența dintre copil, joc, pedagogie, dovezi și acțiune. Pentru academii, aceeași arhitectură poate deveni un curriculum comun și un sistem de dezvoltare a antrenorilor, fără ranking infantil sau colectare inutilă de date despre copii. Premium-ul rezultă din claritate, economie de timp, media relevantă și încredere — nu din ornament.

## PREMIUM TRANSFORMATION BACKLOG

| ID propus | Task | Prioritate | Dependență | Gate |
|---|---|---|---|---|
| TASK-2702 | Production hygiene: eliminare fixtures/placeholders | P0 | TASK-2701 | zero rute interne publice |
| TASK-2703 | IA și terminology V2 prototype | P0 | TASK-2701 | usability test |
| TASK-2704 | Presentation Layer V2 — principle/exercise | P0 | TASK-2703 | 30-second comprehension |
| TASK-2705 | Group Configurator spec + field research | P0 | TASK-2701 | 8–18 configs validate |
| TASK-2706 | SES-0001/2 operational contingencies | P0 | TASK-2705 | field rehearsal |
| TASK-2707 | EX-0004/5 diagrams and Field Cards | P0 | TASK-2704 | visual/PDF PASS |
| TASK-2708 | Problem taxonomy and canonical library research | P0 | TASK-2703 | 8–12 verified problems |
| TASK-2709 | Problem Engine MVP | P0 | TASK-2708 | end-to-end user test |
| TASK-2710 | Field Mode prototype | P0 | TASK-2704/2705 | one-hand field test |
| TASK-2711 | Multimedia production standard/pipeline | P1 | TASK-2704 | accessibility + fallback |
| TASK-2712 | Search/filter MVP | P1 | TASK-2708 | relevance audit |
| TASK-2713 | Offline packs/PWA feasibility | P1 | TASK-2710 | offline field test |
| TASK-2714 | Assessment privacy/DPIA discovery | P1 | real pilot | legal/product gate |
| TASK-2715 | Session Workspace prototype | P1 | TASK-2710/2714 | workflow usability |
| TASK-2716 | Commercial discovery and packaging tests | P1 | TASK-2709/2710 | interview/WTP evidence |

**STOP GATE:** acest backlog este propus, nu autorizat pentru implementare. Direcția trebuie selectată înaintea schimbărilor majore.
