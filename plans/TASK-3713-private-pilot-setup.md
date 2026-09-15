# TASK-3713 — ManualFC Private Pilot Setup

## 1. Titlu și scop

Pregătește un pilot privat, disciplinat, cu 2-3 antrenori U11 reali, care testează comportamentul efectiv al antrenorului în folosire realistă a produsului actual (15 exerciții, 6 ședințe, Decision Engine, offline), nu doar opinii sau complimente. Rezultatul verificabil este un protocol executabil + materiale pentru antrenori + un format de captură a observațiilor — nu date de teren, care nu există încă.

## 2. Context pentru un cititor nou

- Repo canonic: `E:/ManualFC-clean`, HEAD de pornire `23568cb4366c4611d20643be0f49af387e8e5f01` (rezultatul TASK-3712).
- **Precedent important:** `PHASE-23` (`REAL_FIELD_PILOT_RESUMABLE_LOOP`, `TASK-2301`) a pregătit deja o pilotare de teren restrânsă — o singură ședință (`SES-0001`, doar `EX-0001`–`EX-0003`), un singur antrenor implicit — livrabile: `docs/field-pilot/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_SHEET_R1.md` + `docs/field-pilot/PHASE23_FIELD_RETURN_TEMPLATE_R1.md`. **Acel pilot nu a primit niciodată date reale** — `PHASE-23 = FIELD_INPUT_REQUIRED` rămâne neschimbat în `PROJECT_STATUS.md` de la `TASK-2301` până azi. Regula absolută a acelei faze rămâne validă și aici: **niciun rezultat, comportament de copil, feedback de antrenor sau dată de sesiune nu poate fi inventat sau simulat.**
- TASK-3713 e o pilotare mult mai amplă: 2-3 antrenori reali, întregul produs actual (nu doar 3 exerciții), acoperind homepage→onboarding→Decision Engine→exercițiu→ședință→reflecție→Spațiul meu→offline→navigare de revenire.
- **Constatare din inspecția jurnalului antrenorului (acest task, înainte de orice modificare):** produsul e deja neobișnuit de matur pentru scop de pilot. `app/src/lib/coach-state.ts` + `CoachActions.astro` înregistrează automat `recents` la vizitarea oricărei probleme/principiu/exercițiu/ședință (`recordRecent()` apelat din `connectedCallback`) — „revino la un articol folosit anterior" funcționează deja, verificat prin citirea codului, nu presupus. `spatiul-meu/reflectie.astro` are deja avertismentul explicit „Nu introduce nume, date medicale sau alte date personale despre copii" pe formular. `spatiul-meu/sedinta.astro` are avertisment identic. Tot ce ține de „Spațiul meu" (sesiuni, reflecții, pachete offline) e 100% local (`localStorage`, cheia `manualfc.coach-state.v1`) — nimic nu pleacă de pe dispozitiv, confirmat prin citirea directă a codului. `public/manifest.webmanifest` are deja `display: standalone` și pictograme — instalabil pe telefon ca aplicație. Un parcurs real de browser (Playwright, 1440px și 390px) prin toate cele 11 suprafețe cerute de task (homepage, Decision Engine, exercițiu, ședință completă + Mod Teren, configurator, Spațiul meu, constructor de ședință, reflecție, principii→gold-standard, căutare, fișe de teren) nu a găsit 0 overflow orizontal, `h1`=1 peste tot, toate rutele răspund 200.
- **Decizie de scop rezultată direct din constatarea de mai sus:** nu sunt necesare reparații de produs pentru pregătirea pilotului — surprinzător, dar onest. Munca principală a acestui task e protocolul de cercetare și materialele pentru antrenori, exact cum specifică taskul („This task is primarily about pilot readiness, instrumentation-light research design, documentation, and product usability preparation").

## 3. Rezultatul verificabil

- `docs/field-pilot/MANUALFC_PRIVATE_PILOT_PROTOCOL.md` — protocolul complet (profil participant, recrutare, confidențialitate, durată, sesiuni, sarcini, condiții mobil/desktop/online/offline, metodă de observare, întrebări de debrief, dovezi comportamentale, distincția spune-vs-face, criterii de succes/oprire, clasificare severitate, metodă de prioritizare, decizie MUST/SHOULD/NOT_NOW/IGNORE).
- `docs/field-pilot/PRIVATE_PILOT_COACH_PACK.md` — instrucțiuni pentru antrenor, printabile/partajabile, cu scenariile de sarcini exacte cerute de task.
- `docs/field-pilot/PRIVATE_PILOT_OBSERVATION_TEMPLATE.md` — format de captură a observațiilor/feedback-ului, RAW OBSERVATION separat de INTERPRETATION, fără niciun rezultat presupus.
- Guvernanță actualizată (`TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, raport de task) care declară explicit: pregătirea e completă, **execuția pilotului și datele reale rămân `FIELD_INPUT_REQUIRED`**, la fel ca PHASE-23.
- Toate validările obligatorii trec, în repo canonic și într-un fresh clone.

## 4. Domeniu și non-obiective

**Intră:** protocolul de pilot, materialele pentru antrenori, inspecția jurnalului antrenorului, orice reparație minimă de produs strict necesară descoperită în timpul inspecției.

**Nu intră:** autentificare, conturi cu bază de date, analytics, colectare de date personale, funcții sociale, gamification, a doua temă de antrenament, arhitectură multi-age, personalizare speculativă, redesign amplu, orice rezultat de pilot inventat (participanți, citate, comportamente de copil).

## 5. Fișiere și module afectate

Noi: `docs/field-pilot/MANUALFC_PRIVATE_PILOT_PROTOCOL.md`, `docs/field-pilot/PRIVATE_PILOT_COACH_PACK.md`, `docs/field-pilot/PRIVATE_PILOT_OBSERVATION_TEMPLATE.md`, `plans/TASK-3713-private-pilot-setup.md`.

Posibil modificate (numai dacă inspecția găsește un defect real): fișiere de pagină/componentă implicate în parcursul antrenorului. **Rezultat efectiv:** inspecția nu a găsit defecte care necesită reparație (vezi §2) — niciun fișier de produs nu a fost modificat.

Guvernanță: `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md`, `scripts/generate_task_registry.py`, `reports/task-reports/TASK-3713.md`.

## 9. Pași de implementare

1. Verificare stare Git + citire documente obligatorii (finalizat).
2. Inspecția jurnalului antrenorului: citire cod (`coach-state.ts`, `CoachActions.astro`, paginile relevante) + parcurs real de browser la 1440px/390px pe toate cele 11 suprafețe cerute (finalizat, 0 defecte găsite).
3. Acest ExecPlan.
4. Redactarea protocolului complet de pilot.
5. Redactarea pachetului pentru antrenor (instrucțiuni + scenarii de sarcini).
6. Redactarea formatului de captură a observațiilor.
7. Validare completă (schema, teste, build, browser+axe, offline, linkuri, sitemap) — fără modificări de produs așteptate, dar rulată integral conform cerinței taskului.
8. Fresh clone + guvernanță + raport final, cu verdict explicit că pregătirea e completă și datele rămân `FIELD_INPUT_REQUIRED`.

## 11. Progres

- [x] Context, inventar documentație existentă (RESEARCH_PROTOCOL, field-pilot R1, safeguarding), decizie de scop.
- [x] Inspecția jurnalului antrenorului (cod + browser real 1440/390px) — 0 defecte găsite.
- [ ] Protocol complet de pilot
- [ ] Pachet pentru antrenor
- [ ] Format de captură a observațiilor
- [ ] Validare completă
- [ ] Fresh clone + guvernanță + raport

## 13. Jurnal de decizii

- **Decizie:** niciun cod de produs nu a fost modificat. **Motiv:** inspecția directă (cod + browser real la 1440px/390px pe toate cele 11 suprafețe ale parcursului antrenorului cerute de task) nu a găsit overflow orizontal, `h1` multiplu, rute căzute sau lipsa funcționalității cerute (revenire la conținut, confidențialitate, offline) — toate erau deja implementate corect înainte de acest task. **Alternativă respinsă:** inventarea unei „îmbunătățiri" minore doar pentru a avea un diff de produs — respinsă explicit ca ne-onestă și contrară regulii „Do not invent... product problem". **Efect:** munca acestui task e, corect, aproape integral documentație de cercetare/pilot, exact cum indică propriul task („primarily about pilot readiness... documentation").
- **Decizie:** pilotul nou nu redenumește sau nu suprascrie Runda 1 (`TASK-2301`, `SES-0001` izolat). **Motiv:** Runda 1 rămâne o decizie validă, nefinalizată (`FIELD_INPUT_REQUIRED`), din motive de izolare a constatărilor înainte de expunerea întregului sistem (`DEC-0047`). **Efect:** noul protocol e documentat ca extensie/succesor conștient, nu ca o corecție a Rundei 1; ambele rămân în așteptare de date reale, sub aceeași regulă absolută de a nu inventa rezultate.
- **Decizie:** formatul de feedback rămâne document static (markdown, de completat și trimis manual), nu un formular live pe site. **Motiv:** un formular live ar necesita fie stocare server-side (interzisă explicit — nicio bază de date), fie colectare prin serviciu terț (analytics/infrastructură speculativă, interzisă explicit). **Efect:** consecvent cu precedentul `PHASE23_FIELD_RETURN_TEMPLATE_R1.md` și cu principiul local-first deja aplicat în „Spațiul meu".
