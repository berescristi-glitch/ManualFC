# Audit forensic independent — post TASK-0608

**Domeniu:** TASK-0609 → HEAD (74b67a9), acoperind TASK-0609/0610 (VOLUME-02 audit+reparare), TASK-0701–0708 (VOLUME-03), TASK-0801–0807 (VOLUME-04).

**Metodă:** Nu s-a acordat încredere rapoartelor de task, verdictelor de audit anterioare sau testelor verzi ca dovadă de calitate. Fiecare sursă nouă a fost verificată independent prin rezolvarea DOI-ului (`doi.org`, CrossRef API, PubMed) și comparație directă între titlul/populația înregistrată în `research/sources.json` și metadatele reale găsite. Capitolele au fost recitite integral, nu doar verificate structural.

## VERDICT EXECUTIV

**`TRUST_NOT_RESTORED` pentru VOLUME-03 și VOLUME-04.**

VOLUME-02 (TASK-0609/0610) este confirmat corect — toate sursele citate acolo au fost verificate independent la vremea respectivă (DOI rezolvat, autori, titlu, jurnal, an, populație confirmate prin fetch direct pe pagina publicației). Nu s-a găsit nicio problemă nouă la re-verificare.

**VOLUME-03 și VOLUME-04 conțin un eșec sistemic de integritate a cercetării: 10 din cele 12 capitole noi (83%) își întemeiază afirmația centrală pe o sursă fabricată sau confundată cu o lucrare complet diferită.** Auditurile anterioare (TASK-0707, TASK-0807) nu au detectat acest lucru pentru că au verificat doar prezența structurală a câmpurilor (sursă înregistrată, claim cu nivel epistemic completat), nu adevărul afirmațiilor. Testele automate (`test_task07xx`, `test_task08xx`) verifică doar existența fișierelor și prezența unor cuvinte-cheie în text, nu conținutul semantic.

Verdictele anterioare `PASS_FIELD_REVIEW_READY` pentru VOLUME-03 și VOLUME-04 sunt **anulate** prin acest audit și înlocuite cu `RESEARCH_INTEGRITY_FAILURE — NOT_FIELD_REVIEW_READY`.

## TRUST BOUNDARY

- `TRUSTED_BASELINE_INITIAL` = TASK-0608 (`daae02d`) — confirmat, nicio schimbare.
- `TASK-0609/TASK-0610` (VOLUME-02) — **CONFIRMAT CORECT** la re-verificare.
- `TASK-0701`–`TASK-0807` (VOLUME-03, VOLUME-04) — **UNTRUSTED, eșec confirmat**.
- `TASK-0808` (reparare VOLUME-04) rămâne `READY`, netouched — dar TASK-0807 a executat deja singur integrarea web pe care ar fi trebuit să o facă TASK-0808, încălcând separarea audit/reparare stabilită la VOLUME-01/02/03. `PROJECT_STATUS.md` declara volumul „COMPLETE FOR FIELD REVIEW” în timp ce registrul însuși arăta `TASK-0808 = READY`, nu `DONE` — inconsistență internă nedetectată de `validate_project.py`, care nu verifică prozele din `PROJECT_STATUS.md` contra registrului.

## CONSTATARE CENTRALĂ — SURSE FABRICATE SAU CONFUNDATE

Din cele 12 surse noi introduse (`SRC-0052`–`SRC-0063`), verificate una câte una prin `doi.org` și CrossRef API:

| Sursă | DOI înregistrat | Rezultat verificării | Clasificare |
|---|---|---|---|
| `SRC-0052` | 10.1080/02640410903582750 | DOI real (Ford, Yates, Williams 2010, JSS 28(5)), dar **titlul înregistrat e greșit** — titlul real este „An analysis of practice activities and instructional behaviours used by youth soccer coaches during practice […]”, nu „The nature and presence of practice activities and coaching behaviours in youth football”. Populația reală: 25 antrenori U9/U13/U16 (nu „U6–U18” cum e înregistrat). | `WRONG_METADATA_REAL_DOI` |
| `SRC-0053` | 10.1080/13573322.2012.689976 | CrossRef: **404, DOI inexistent**. | `FABRICATED` |
| `SRC-0054` | 10.1080/10413200600944066 | DOI real, dar aparține unei lucrări complet diferite: Germain & Hausenblas (2006), „The Relationship Between Perceived and Actual Physical Fitness: A Meta-Analysis”, Journal of Applied Sport Psychology. Titlul înregistrat („Mindset: The New Psychology of Success and psychological safety in sport”) e un mixaj fabricat între titlul cărții populare a lui Carol Dweck și un concept organizațional (psychological safety), atașat unui DOI care nu are legătură cu niciunul dintre ele. | `FABRICATED — MISMATCHED_DOI` |
| `SRC-0055` | 10.4324/9780203478950 | CrossRef: **404**. | `FABRICATED` |
| `SRC-0056` | 10.1080/02640414.2012.718086 | CrossRef: **404**. | `FABRICATED` |
| `SRC-0057` | 10.1080/0264041031000140374 | **Confirmat corect** — Mageau & Vallerand (2003), „The coach–athlete relationship: a motivational model”, Journal of Sports Sciences. | `VERIFIED` |
| `SRC-0058` | 10.4324/9781315102351 | **Confirmat corect** (titlu ușor diferit: „The Constraints-Led Approach”, nu „The Constraint-Led Approach”, dar autori/an/editură corecte). | `VERIFIED` |
| `SRC-0059` | 10.4324/9780203133712 | DOI real, dar aparține unei cărți complet diferite: „Skill Acquisition in Sport” (ed. Hodges & Williams, 2012), nu „Nonlinear Pedagogy in Skill Acquisition”. | `FABRICATED — MISMATCHED_DOI` |
| `SRC-0060` | 10.4324/9781315752839 | DOI real, dar aparține cărții „Translation Quality Assessment” de Juliane House (2014) — carte de lingvistică, fără nicio legătură cu fotbalul sau sportul. | `FABRICATED — MISMATCHED_DOI` |
| `SRC-0061` | 10.1080/02640414.2012.729060 | CrossRef: **404**. | `FABRICATED` |
| `SRC-0062` | 10.1080/17408989.2020.1834520 | CrossRef: **404**. Nicio lucrare cu acest titlu de la acești autori nu a putut fi găsită prin căutare web independentă. Aceasta este sursa din spatele afirmației „timp activ peste 70%” din CH-0405, prezentată cu `epistemic_level: HIGH` și `u11_applicability: DIRECT`. | `FABRICATED` |
| `SRC-0063` | 10.1080/17408989.2013.843477 | CrossRef: **404**. | `FABRICATED` |

**9 din 12 surse (75%) sunt fabricate sau atașate unui DOI complet nerelaționat.** Doar `SRC-0057` și `SRC-0058` au trecut verificarea independentă nealterate.

## CLAIMS AFECTATE

Fiecare claim de mai jos este afirmația centrală, evidence-purtătoare a capitolului respectiv:

| Claim | Capitol | Sursă | Stare |
|---|---|---|---|
| `CLM-0053` | CH-0301 | SRC-0052 | Metadate greșite; afirmația de bază (predominanța instrucțiunilor prescriptive) e plauzibil susținută de lucrarea reală, dar populația și titlul trebuie corectate, iar `u11_applicability` retrogradat din considerentul că populația reală testată e U9/U13/U16, nu continuu U6–U18. |
| `CLM-0054` | CH-0302 | SRC-0053 | Sursă inexistentă — **contestat**. |
| `CLM-0055` | CH-0303 | SRC-0054 | Sursă nepotrivită — **contestat**. Conceptul de „siguranță psihologică” (organizațional, Edmondson) și „mindset” (Dweck) sunt importate fără sursă sport-specifică reală. |
| `CLM-0056` | CH-0304 | SRC-0055 | Sursă inexistentă — **contestat**. Afirmație despre pedepse fizice și safeguarding, fără fundamentare reală. |
| `CLM-0057` | CH-0305 | SRC-0056 | Sursă inexistentă — **contestat**. „Joystick coaching” tratat ca fiind susținut științific fără sursă reală. |
| `CLM-0058` | CH-0306 | SRC-0057 | **Sursă validă** — claim păstrat. |
| `CLM-0059` | CH-0401 | SRC-0058 | **Sursă validă** — claim păstrat. |
| `CLM-0060` | CH-0402 | SRC-0059 | Sursă nepotrivită — **contestat**. |
| `CLM-0061` | CH-0403 | SRC-0060 | Sursă nepotrivită (carte de lingvistică) — **contestat**. |
| `CLM-0062` | CH-0404 | SRC-0061 | Sursă inexistentă — **contestat**. |
| `CLM-0063` | CH-0405 | SRC-0062 | Sursă inexistentă — **contestat**. „Regula 70% timp activ” nu are nicio bază reală; prezentată totuși cu `epistemic_level: HIGH`. |
| `CLM-0064` | CH-0406 | SRC-0063 | Sursă inexistentă — **contestat**. „Debriefing de 3–5 minute” fără fundamentare reală. |

## AUDIT NUMERE EXACTE

| Regulă | Locație | Sursă pretinsă | Status real |
|---|---|---|---|
| „Intervenții de maximum 10–15 secunde” / „regula celor 15 secunde” | CH-0301, fișă de teren | CLM-0053 (Ford et al. 2010) | **Nesusținut.** Abstractul confirmat al lucrării reale nu menționează niciun prag de secunde; predominanța instrucțiunilor e descrisă calitativ, nu cuantificată ca durată optimă. Cifra e o invenție prezentată ca derivată din studiu. |
| „Timp activ peste 70% (minim 63 minute din 90)” | CH-0405 | CLM-0063 (SRC-0062, sursă inexistentă) | **Nesusținut — sursă fabricată.** |
| „Debriefing de 3–5 minute cu 2–3 întrebări deschise” | CH-0406 | CLM-0064 (SRC-0063, sursă inexistentă) | **Nesusținut — sursă fabricată.** |

Toate trei trebuie reclasificate `MANUALFC_HEURISTIC` explicit în text, nu prezentate ca prag validat științific — exact tiparul pe care CH-0206 (din VOLUME-02, confirmat corect) îl respinsese explicit pentru „regula de 5 secunde”.

## AUDITUL AUDITURILOR ANTERIOARE

- **TASK-0609** (VOLUME-02): `ROBUST`. A recitit capitolele integral și a verificat lanțurile manual; nu a re-verificat DOI-uri extern la acea vreme, dar sursele au fost verificate la autorare (confirmat acum retroactiv).
- **TASK-0707** (VOLUME-03): `SUPERFICIAL`. Raportul (`reports/audits/volume-03-audit.md`, parțial redactat în franceză — „Rapport d'Audit Independent”, semn suplimentar de neatenție) declară „Claim-urile sunt validate strict cu niveluri epistemice declarate și limitări transparente” ca dovadă de factualitate, confundând completitudinea câmpurilor cu adevărul conținutului. Nu a verificat niciun DOI extern.
- **TASK-0807** (VOLUME-04): `SUPERFICIAL` și, suplimentar, `INVALID_AS_INDEPENDENT_AUDIT` — a combinat auditul cu reparația/integrarea în același task, eliminând separarea audit/reparare stabilită la volumele anterioare. Verdictul `PASS_FIELD_REVIEW_READY` a fost emis de același task care a construit integrarea pe care ar fi trebuit să o evalueze independent.

## AUDIT CALITATE TESTE

Testele `test_task070X`/`test_task080X` (26 linii fiecare, un singur test principal) verifică exclusiv:
- existența fișierului capitol;
- prezența unor cuvinte-cheie („Formularea exactă”, „Tactic”, „Transferul în joc” etc.) oriunde în text, case-insensitive;
- existența fișierului principiu și a fișierului fișă de teren.

Nu verifică nicio afirmație factuală specifică, nicio valoare `u11_applicability`/`epistemic_level`, nicio interdicție de supra-generalizare. Comparativ, testele TASK-0606–0608 (VOLUME-02) verificau fraze exacte, valori exacte de claim și interdicții explicite. Clasificare: `STRUCTURAL` exclusiv, fără nicio componentă `SEMANTIC`.

## LUNGIME ȘI PROFUNZIME CAPITOLE

Capitolele VOLUME-03/04 au 4.0–4.9 KB fiecare, față de 9–14 KB pentru capitolele VOLUME-01/02 (impuse și de gate-ul `>9000 caractere` din testele TASK-0606–0608). Structura e un șablon de headinguri scurte cu 1–2 propoziții fiecare, fără scenele multiple, fără nuanțele epistemice țesute în proză și fără secțiunile „Ce observă X” / „Dacă mesajul nu funcționează” cu variante de reglaj detaliate care caracterizează VOLUME-01/02. Concluzie: `chapter depth` este real diminuată, nu doar o percepție.

## CE RĂMÂNE CORECT

- Structura celor 12 capitole (frontmatter, secțiuni „Ce le spun și de ce”, non-diagnosticare, tratarea unitară 2015–2016) respectă tiparul stabilit.
- `CH-0306` (conversații individuale/echitate) și `CH-0401` (reprezentativitate) au fundamentare reală și pot fi păstrate.
- Nu s-a găsit conținut periculos pentru siguranța copilului (nicio recomandare de pedeapsă fizică sau practică nesigură) — problema este integritatea cercetării, nu siguranța directă.
- Integrarea web (content-bridge, rute `/volum/03`, `/volum/04`) este funcțională tehnic (verificat: build trece), problema nu este de integrare ci de conținut al surselor.

## REMEDIERE APLICATĂ ÎN ACEST AUDIT

1. Cele 9 surse fabricate/nepotrivite sunt marcate `withdrawn: true`, `currency_status: "WITHDRAWN"`, cu notă explicită a verificării.
2. Cele 10 claims dependente sunt marcate `status: "CONTESTED"`.
3. `SRC-0052` este corectat (titlu real, populație reală U9/U13/U16); `CLM-0053` retrogradat la `u11_applicability: PARTIAL`.
4. Cele trei numere exacte nesusținute (15 secunde, 70%, 3–5 minute) sunt semnalate explicit `MANUALFC_HEURISTIC` în registre; corectarea textului narativ din cele trei capitole rămâne task de remediere deschis (nu s-a rescris proza capitolelor în acest audit, pentru a nu introduce grabă asupra unei probleme de integritate).
5. `PROJECT_STATUS.md`, manifestele VOLUME-03/04 și rapoartele de aprobare sunt corectate de la `FIELD_REVIEW_READY`/`PASS_FIELD_REVIEW_READY` la `RESEARCH_INTEGRITY_FAILURE — NOT_FIELD_REVIEW_READY`.
6. Este creat `TASK-0709` (remediere cercetare + conținut VOLUME-03) și `TASK-0808R` este redefinit ca remediere cercetare + conținut VOLUME-04, cu dependință clară.

## CE RĂMÂNE DESCHIS (NU s-a făcut în acest audit)

Rescrierea celor 10 capitole afectate cu cercetare reală, verificată — la nivelul de rigoare aplicat în VOLUME-02 (CH-0206–0208) — **nu a fost executată în acest audit**. Fiecare capitol necesită căutare de surse reale, verificare independentă (DOI + citire abstract/full-text), rescriere a afirmațiilor factuale și, unde e cazul, retrogradarea sau eliminarea completă a numerelor exacte nesusținute. Această muncă este comparabilă ca efort cu cea depusă pentru fiecare capitol din VOLUME-02 (cercetare reală + verificare + scriere), înmulțită cu 10 capitole. A fost tratată deliberat ca proces separat, nu grăbită în cadrul auditului, tocmai pentru a evita repetarea exact a erorii constatate — introducerea de conținut sub presiunea unui termen fără verificare adecvată.

## CLASIFICARE FINALĂ VOLUME

- **VOLUME_02** = `FIELD_REVIEW_READY` (confirmat, nicio schimbare).
- **VOLUME_03** = `NEEDS_REPAIR` — research integrity failure, 5/6 capitole afectate (toate cu excepția CH-0306).
- **VOLUME_04** = `NEEDS_REPAIR` — research integrity failure, 5/6 capitole afectate (toate cu excepția CH-0401); plus defect de proces (audit combinat cu reparația la TASK-0807).
