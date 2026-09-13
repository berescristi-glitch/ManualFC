# Audit independent post-remediere — VOLUME-04 (TASK-0810)

**Domeniu:** TASK-0809 (`HEAD` la momentul auditului) — remedierea completă a VOLUME-04 (CH-0401–CH-0406), realizată ca urmare a `reports/audits/POST_TASK0608_FORENSIC_AUDIT.md` și `DEC-0040`.

**Executant:** Sesiune separată de TASK-0809, fără nicio implicare în scrierea remedierii. Nu s-a pornit de la premisa că TASK-0809 e corect — fiecare afirmație de mai jos a fost re-derivată independent, nu copiată din `reports/task-reports/TASK-0809.md` sau din `plans/TASK-0809-remediere-volume-04.md`. Respectă aceeași separare audit/reparație stabilită după eșecul documentat în `DEC-0040` (TASK-0807 a combinat reparația VOLUME-04 cu propriul verdict de aprobare, ceea ce a permis fabricărilor din VOLUME-03/04 să treacă nedetectate) și aplicată deja cu succes la VOLUME-03 (`TASK-0710`).

**Metodă:** Nu s-a acordat încredere rapoartelor de task, registrului JSON sau testelor verzi ca dovadă suficientă. Toate cele 21 de surse noi introduse de TASK-0809 (`SRC-0087`–`SRC-0107`) au fost verificate direct prin `https://api.crossref.org/works/<DOI>` (unealta MCP `fetch_crossref_by_doi`), comparând titlu, autori, an și revistă cu ce e înregistrat în `research/sources.json` și cu ce e citat în capitole. Pentru cifra cea mai încărcată epistemic din tot volumul (`SRC-0101`, Rössler et al. 2018, reducere 48% a riscului de accidentare, HR 0,52), s-a făcut o verificare terță independentă prin OpenAlex (abstract complet, separat de CrossRef, care nu expune abstractul acestei surse) — nu doar re-citirea `researcher_notes` din registru. Cele 6 capitole au fost recitite integral, nu doar verificate structural. Registrele `research/*.json` au fost interogate programatic pentru consistență internă (status, `replacement_claim_id`, `withdrawn`, acoperire de citare). Cele 6 fișe de teren și cele 6 fișiere `data/principles/*.json` corespunzătoare au fost citite integral. S-au rulat cele 4 gate-uri de validare cerute, independent, plus `generate_task_registry.py --check`.

---

## VERDICT EXECUTIV

# `PASS_FIELD_REVIEW_READY`

VOLUME-04 (CH-0401–CH-0406) este considerat pregătit pentru field review. Remedierea TASK-0809 rezistă unei re-verificări independente și sceptice: nu s-a găsit nicio sursă fabricată, nicio sursă cu DOI nepotrivit, nicio suprasolicitare epistemică nedeclarată, nicio cifră exactă prezentată drept cercetare fără sursă reală, și nicio dogmă înlocuită cu dogma opusă. Cifra cea mai încărcată epistemic a volumului (reducerea de 48% a riscului de accidentare prin FIFA 11+ Kids) a fost confirmată independent, cu exactitate. Au fost găsite 2 defecte minore, strict cosmetice, care nu afectează adevărul, siguranța sau calibrarea epistemică a conținutului — enumerate mai jos, cu remediere propusă opțională, nu blocantă.

---

## Verificare bibliografică independentă (CrossRef)

Toate cele 21 de surse noi introduse de TASK-0809 (`SRC-0087`–`SRC-0107`) au un DOI care rezolvă real la CrossRef și au fost verificate independent — nu un eșantion, ci setul complet cerut.

| Sursă | DOI | Titlu confirmat CrossRef | Autori/An/Revistă confirmate | Rezultat |
|---|---|---|---|---|
| `SRC-0087` | 10.1371/journal.pone.0104744 | "Nonlinear Pedagogy: An Effective Approach to Cater for Individual Differences in Learning a Sports Skill" | Lee, Chow, Komar, Tan, Button (2014), *PLoS ONE* | Potrivire exactă — RCT, fete de 10 ani, tenis. |
| `SRC-0088` | 10.1177/17479541241240853 | "The adaptable coach – a critical review of the practical implications for traditional and constraints-led approaches in sport coaching" | Lindsay, Spittle (2024), *Int. J. of Sports Science & Coaching* | Potrivire exactă; abstract confirmă exact teza citată — nicio abordare nu e „superioară" universal. |
| `SRC-0089` | 10.3389/fpsyg.2021.772201 | "Perceptual-Motor and Perceptual-Cognitive Skill Acquisition in Soccer: A Systematic Review..." | Bergmann, Gray, Wachsmuth, Höner (2021), *Frontiers in Psychology* | Potrivire exactă; abstract confirmă 34 studii fotbal, calitate metodologică moderată, impactul asupra jocului real „insuficient testat" — exact ce citează CH-0402. |
| `SRC-0090` | 10.1007/s40279-015-0452-2 | "Scaling the Equipment and Play Area in Children's Sport to improve Motor Skill Acquisition: A Systematic Review" | Buszard, Reid, Masters, Farrow (2016), *Sports Medicine* | Potrivire exactă. |
| `SRC-0091` | 10.1080/24748668.2018.1517288 | "Small sided games in soccer – a systematic review" | Sarmento, Clemente, Harper, Teoldo da Costa, Owen, Figueiredo (2018), *Int. J. of Performance Analysis in Sport* | Potrivire exactă. |
| `SRC-0092` | 10.1371/journal.pone.0247067 | "Small-sided games: An umbrella review of systematic reviews and meta-analyses" | Clemente, Afonso, Sarmento (2021), *PLOS ONE* | Potrivire exactă; abstract confirmă cuvânt cu cuvânt „7 din 12 review-uri au calitate scăzută, 5 critic-scăzută" — capitolul citează onest acest semnal de calitate slabă. |
| `SRC-0093` | 10.1515/hukin-2015-0053 | "Game-Based Approaches' Pedagogical Principles: Exploring Task Constraints in Youth Soccer" | Serra-Olivares, González-Víllora, García-López, Araújo (2015), *Journal of Human Kinetics* | Potrivire exactă; abstract confirmă N=21, jucători U10, 3v3. |
| `SRC-0094` | 10.1186/s40064-016-1813-5 | "Sports teams as complex adaptive systems: manipulating player numbers shapes behaviours during football small-sided games" | Silva, Vilar, Davids, Araújo, Garganta (2016), *SpringerPlus* | Potrivire exactă. |
| `SRC-0095` | 10.3389/fpsyg.2020.01444 | "When and How to Provide Feedback and Instructions to Athletes?..." | Otte, Davids, Millar, Klatt (2020), *Frontiers in Psychology* | Potrivire exactă. |
| `SRC-0096` | 10.3389/fpsyg.2021.724848 | "Teaching Children's Motor Skills for Team Games Through Guided Discovery: How Constraints Enhance Learning" | Newell, Rovegno (2021), *Frontiers in Psychology* | Potrivire exactă; abstract confirmă context „elementary school-aged children", exact populația citată. |
| `SRC-0097` | 10.1177/1747954115624824 | "Exploring coach behaviours, session contexts and key stakeholder perceptions of non-linear coaching approaches in youth sport" | Vinson, Brady, Moreland, Judge (2016), *Int. J. of Sports Science & Coaching* | Potrivire exactă; abstract confirmă „lower rate of coach behaviour... fewer technical interventions and more questioning" — exact ce citează CH-0404. |
| `SRC-0098` | 10.1186/s12966-017-0479-x | "Framework for the design and delivery of organized physical activity sessions for children and adolescents: ... 'SAAFE' teaching principles" | Lubans, Lonsdale, Cohen, Eather, Beauchamp, Morgan, Sylvester, Smith (2017), *IJBNPA* | Potrivire exactă. |
| `SRC-0099` | 10.1186/s12966-020-01054-y | "Physical activity and sedentary time of youth in structured settings: a systematic review and meta-analysis" | Tassitano, Weaver, Tenório, Brazendale, Beets (2020), *IJBNPA* | Potrivire exactă; abstract confirmă 187 studii, 74.870 tineri, vârstă medie 8,6 ani — cifrele exacte citate în CH-0405. |
| `SRC-0100` | 10.1080/19406940.2014.919338 | "Evidence-based policies for youth sport programmes" | Côté, Hancock (2014), *Int. J. of Sport Policy and Politics* | Potrivire exactă. |
| `SRC-0101` | 10.1007/s40279-017-0834-8 | "A Multinational Cluster Randomised Controlled Trial to Assess the Efficacy of '11+ Kids'..." | Rössler, Junge, Bizzini, Verhagen, Chomiak, aus der Fünten, Meyer, Dvorak, Lichtenstein, Beaudouin, Faude (2017/2018), *Sports Medicine* | Potrivire exactă. **Cifra centrală verificată separat — vezi secțiunea dedicată mai jos.** |
| `SRC-0102` | 10.1136/bjsports-2015-094765 | "FIFA 11+: an effective programme to prevent football injuries in various player groups worldwide—a narrative review" | Bizzini, Dvorak (2015), *British Journal of Sports Medicine* | Potrivire exactă — sursă oficială F-MARC/FIFA, folosită corect ca sprijin de context pentru siguranță. |
| `SRC-0103` | 10.1016/j.jshs.2021.10.002 | "Epidemiology of injuries in male and female youth football players: A systematic review and meta-analysis" | Robles-Palazón, López-Valenciano, De Ste Croix, Oliver, García-Gómez, Sainz de Baranda, Ayala (2022), *Journal of Sport and Health Science* | Potrivire exactă. |
| `SRC-0104` | 10.33043/sswj.1.1.78-95 | "Social Skill Transfer from a Sport-Based Positive Youth Development Program to the School Setting" | Pierce, Scheadler, Anderson-Butcher, Amorose, Wade-Mdivanian (2022), *Sport Social Work Journal* | Potrivire exactă; abstract confirmă N=176, transfer de autocontrol către școală — exact cifrele citate în CH-0406. |
| `SRC-0105` | 10.1080/1750984x.2016.1180704 | "A grounded theory of positive youth development through sport based on results from a qualitative meta-study" | Holt, Neely, Slater, Camiré, Côté, Fraser-Thomas, MacDonald, Strachan, Tamminen (2016/2017), *Int. Review of Sport and Exercise Psychology* | Potrivire exactă (63 studii, confirmat). |
| `SRC-0106` | 10.2522/ptj.20070196 | "Motor Learning in Children: Feedback Effects on Skill Acquisition" | Sullivan, Kantak, Burtner (2008), *Physical Therapy* | Potrivire exactă; abstract confirmă N=20 copii/20 adulți, comparație transfer feedback — context indirect, corect declarat ca atare în capitol. |
| `SRC-0107` | 10.3389/fpsyg.2017.01931 | "Quantifying Contextual Interference and Its Effect on Skill Transfer in Skilled Youth Tennis Players" | Buszard, Reid, Krause, Kovalchik, Farrow (2017), *Frontiers in Psychology* | Potrivire exactă. |

**Rezultat:** 21 din 21 surse verificate — 0 titluri greșite, 0 autori greșiți, 0 DOI aparținând altei lucrări. Niciun eșec de tipul găsit de auditul forensic inițial (`FABRICATED`, `WRONG_METADATA_REAL_DOI`, `MISMATCHED_DOI`) nu se repetă.

### Verificare terță a cifrei centrale — `SRC-0101` / `CLM-0097` (FIFA 11+ Kids)

Capitolul CH-0405 citează: RCT multinațional, vârstă medie 10,8 ani, reducere de **48%** a riscului global de accidentare (HR 0,52), reducere de **74%** a accidentărilor severe. Verificat independent prin OpenAlex (`fetch_openalex_by_doi`, sursă distinctă de CrossRef, care nu expune abstractul acestei lucrări), pe baza abstractului complet indexat:

> "The overall injury rate in the intervention group was reduced by 48% compared with the control group (hazard ratio 0.52; 95% confidence interval 0.32-0.86). Severe (74% reduction, hazard ratio 0.26; 95% confidence interval 0.10-0.64)... The mean age of players was 10.8 (standard deviation 1.4) years."

Cifrele din capitol, din fișa de teren (`CH_0405_ACTIVE_TIME_ORGANIZATION_CARD.md`) și din `research/sources.json`/`claims.json` se potrivesc exact, cuvânt cu cuvânt/cifră cu cifră, cu abstractul real al studiului. Aceasta este singura cifră exactă din tot volumul prezentată ca rezultat de cercetare solid — și rezistă verificării terțe.

---

## Verificare per capitol

### CH-0401 — Proiectarea unei situații reprezentative
Sursa (`SRC-0058`, Renshaw et al. 2019) nu a fost re-cercetată de TASK-0809 (era deja validă bibliografic), doar recalibrată semantic. Verificat: `CLM-0059` are `epistemic_level: MODERATE`/`u11_applicability: PARTIAL`, iar capitolul însuși spune explicit „este o sinteză metodologică de referință, larg citată, nu un studiu empiric cu populație măsurată la 10–11 ani". Pragul fabricat „2–3 stimuli simultani" e absent; secțiunea „Adecvarea la vârstă" spune explicit „Numărul exact de stimuli procesabili simultan nu este specificat de sursă — este o euristică practică ManualFC". Limbajul pentru copil e scurt și orientat spre acțiune. **Defect minor găsit** (vezi secțiunea de constatări): etichetele „Decisional"/„Technical" netraduse la secțiunea „Justificarea... pe 7 dimensiuni", exact tiparul deja documentat ca minor în auditul VOLUME-03 (acolo la CH-0306).

### CH-0402 — Constrângeri: alegere, dozare și eliminare
Sursa fabricată („Chow et al. 2016", `SRC-0059`, DOI real dar aparținând cărții de lingvistică a lui Juliane House) e eliminată; `SRC-0059` are `withdrawn: true` cu notă forensică explicită. `CLM-0060` e `REPLACED` → `CLM-0090` (VERIFIED). Testul central cerut de brief e trecut clar: capitolul are o secțiune dedicată „Despre limitele metodei" care respinge explicit superioritatea universală a abordării bazate pe constrângeri, citând direct Lindsay & Spittle 2024 (confirmat CrossRef — abstract spune literal că sarcina antrenorului nu e să aleagă o „tabără" ci să combine abordările) și Bergmann et al. 2021 (impactul asupra jocului real „widely unexplored"). Instrucția directă e păstrată explicit ca opțiune legitimă, de mai multe ori în text. Nu există niciun prag numeric exact prezentat ca validat.

### CH-0403 — Progresii și regresii fără pierderea intenției
Aceeași sursă fabricată ca CH-0402 (aceeași carte de lingvistică, atribuită „Passos et al. 2016") e eliminată; `CLM-0061` e `REPLACED` → `CLM-0093` (VERIFIED). Pragul fabricat „<50%/>80% rată de succes" e absent explicit — textul spune „nu există un prag procentual de rată de succes validat științific; decizia rămâne judecata antrenorului pe teren", repetat identic în fișa de teren. Sursa-umbrelă (`SRC-0092`) e citată cu semnalarea onestă a calității ei metodologice slabe, nu ca certitudine. Extrapolarea de vârstă (U10 la `SRC-0093`, U15 la `SRC-0094`, față de U11 țintă) e transparentă în text (vârstele exacte sunt numite direct).

### CH-0404 — Observare și criterii de intervenție
Sursa fabricată („Cushion et al. 2012", `SRC-0061`, DOI 404) e eliminată; `CLM-0062` e `REPLACED` → `CLM-0094` (VERIFIED). Pragurile fabricate „15 secunde"/„3 repetări" sunt absente; textul spune explicit „Niciuna dintre sursele găsite nu specifică însă un timing exact — în secunde sau minute — validat pentru momentul intervenției". Excepția de siguranță e păstrată clar: „Nu putem concluziona că antrenorul trebuie să tacă complet... Siguranța și respectul cer intervenție imediată". Reutilizarea `CLM-0070`/`SRC-0069` (din VOLUME-03/CH-0302, Partington/Cushion/Harvey 2013) e corect legată — vezi verificarea de duplicare de mai jos.

### CH-0405 — Organizare, rotații, timp activ și siguranță
Sursa fabricată („Scaglia et al. 2021", `SRC-0062`, DOI 404) e eliminată; `CLM-0063` e `REPLACED` → `CLM-0095` (VERIFIED). Testul central cerut de brief — trei domenii de dovadă separate — e trecut clar: capitolul are trei subsecțiuni explicite („Timp activ", „Organizare și rotații", „Siguranță"), fiecare cu propria concluzie epistemică distinctă (timp activ: „niciun prag procentual validat"; organizare: „domeniu slab acoperit de cercetare directă", `epistemic_level: LOW`; siguranță: „aici dovada e mult mai solidă", `epistemic_level: HIGH`). Pragul fabricat „>70%/63 minute" e absent. Secțiunea de siguranță folosește surse oficiale de federație (`SRC-0102`, Bizzini & Dvorak — F-MARC/FIFA) plus RCT-ul cu cifra verificată terț mai sus. Domeniile nu se amestecă niciodată — nicio afirmație de organizare nu împrumută soliditatea epistemică a secțiunii de siguranță.

### CH-0406 — Transferul și reflecția după joc
Sursa fabricată („Harvey & Light 2015", `SRC-0063`, DOI 404) e eliminată; `CLM-0064` e `REPLACED` → `CLM-0099` (VERIFIED). Pragul fabricat „3–5 minute" e absent ca prag valid — apare doar ca exemplu explicit respins: „Nu putem concluziona... că există o durată exactă (3–5 minute sau orice alt prag) validată de cercetare pentru un debriefing — nicio sursă găsită specifică asta." Aceeași formulare apare, identic, în fișa de teren și ca „posibilă interpretare greșită" în `data/principles/principle-reflectia-ghidata-si-transferul-in-joc.json`. Extrapolarea de la măsurarea transferului de autocontrol (nu tactică de fotbal) la reflecția tactică e declarată explicit: „ele măsoară transferul de abilități de viață (autocontrol), nu tactica de fotbal specific — o extrapolare rezonabilă, nu o dovadă directă".

---

## Constatări minore (nu blochează verdictul)

1. **Etichete netraduse în CH-0401.** `content/volume-04/chapter-01.mdx`, secțiunea „Justificarea tactică, perceptivă, cognitivă, psihologică și socială" (liniile 61 și 64), folosește „**Decisional**" și „**Technical**" în loc de „Decizional" și „Tehnic", folosite consecvent de celelalte 5 capitole din VOLUME-04 (toate corectate ca parte din rescrierea lor completă de TASK-0809). CH-0401 nu a fost rescris integral (doar recalibrat semantic), deci a moștenit acest defect cosmetic pre-existent. Exact același tipar de defect a fost identificat ca minor în auditul VOLUME-03 (`TASK-0710`), acolo la CH-0306, tot un capitol care nu fusese rescris integral. Defect pur cosmetic, nu de conținut sau cercetare. **Remediere propusă:** înlocuire text „Decisional"→„Decizional", „Technical"→„Tehnic" în `chapter-01.mdx`, liniile 61 și 64.
2. **Typo în `content/volume-04/manifest.json`.** Descrierea CH-0403 conține „Scalarea dificulatății sarcinilor..." — typo pentru „dificultății". Defect cosmetic, nu afectează conținutul capitolului propriu-zis (care scrie corect „dificultate" peste tot). **Remediere propusă:** corectare typo în `manifest.json`, linia 29.

Niciuna dintre aceste 2 constatări nu afectează adevărul, siguranța sau calibrarea epistemică a conținutului publicat.

---

## Consistența registrelor de cercetare

Verificat programatic (nu vizual) pe toate cele 18 claim-uri legate de VOLUME-04 (`chapter_id` începe cu `CH-04`):

- **Status:** 13 `VERIFIED`, 5 `REPLACED` (`CLM-0060`, `CLM-0061`, `CLM-0062`, `CLM-0063`, `CLM-0064`). **0 rămase `CONTESTED` sau `PROPOSED`.**
- **`replacement_claim_id` pentru cele 5 `REPLACED`:** toate cinci au un id valid, care există în registru și are status `VERIFIED`:
  - `CLM-0060` → `CLM-0090` (VERIFIED)
  - `CLM-0061` → `CLM-0093` (VERIFIED)
  - `CLM-0062` → `CLM-0094` (VERIFIED)
  - `CLM-0063` → `CLM-0095` (VERIFIED)
  - `CLM-0064` → `CLM-0099` (VERIFIED)
- **Surse `withdrawn`:** verificat programatic — 0 claim-uri `VERIFIED` din VOLUME-04 folosesc o sursă cu `withdrawn: true`. Cele 5 surse fabricate originale (`SRC-0059`–`SRC-0063`) au toate `withdrawn: true`, cu notă forensică identică, datată 2026-08-11.
- **Acoperire de citare:** toate cele 18 claim-uri au cel puțin o intrare în `research/citations.json` (27 de citări totale pe claim-urile VOLUME-04).
- **`questions.json`:** cele 9 întrebări de cercetare legate de CH-0402–CH-0406 au status `AUDITED`, niciuna `PROPOSED`/`CONTESTED`. (CH-0401 nu are întrebare de cercetare proprie — corect, nu a fost re-cercetat.)

## Duplicare între volume

S-a verificat lista completă de DOI-uri din `research/sources.json` (106 surse, toate volumele) pentru duplicate. **0 DOI-uri duplicate în întregul registru.** Reutilizarea intenționată `CLM-0070`/`SRC-0069` (Partington/Cushion/Harvey 2013, deja existent din VOLUME-03/CH-0302) în CH-0404 este gestionată corect — nu s-a creat niciun record de sursă duplicat; citarea existentă (`CIT-0075`) e reutilizată ca atare, iar capitolul o citează în context, cu prudența epistemică declarată deja de VOLUME-03.

## Relevanță pentru fotbal și aplicabilitate U11

Verificat manual, sursă cu sursă, câmpurile `sport`/`age_range`/`population` din `research/sources.json` față de cum e folosită sursa în capitol, pentru toate cele 21 de surse noi:

- Surse direct din fotbal juvenil, cu vârstă apropiată sau incluzând U11: `SRC-0089`, `SRC-0091`, `SRC-0092`, `SRC-0093` (U10), `SRC-0098`, `SRC-0101` (vârstă medie 10,8 ani), `SRC-0102`, `SRC-0103`.
- Surse din alte sporturi sau populații (tenis, multisport, context general de politici/psihologie a sportului) sunt folosite exclusiv pentru mecanisme generale (variabilitate a mișcării, timp activ, dezvoltare pozitivă prin sport, transfer al învățării) sau ca extrapolări explicit declarate — niciodată prezentate ca dovadă directă din fotbal fără avertisment. Fiecare caz de extrapolare are `u11_applicability: PARTIAL`/`INDIRECT` și o propoziție explicită de limitare în capitol sau în câmpul `limitations` al sursei (ex. „rezultatul vine dintr-un sport diferit, dar la exact vârsta de interes", „context diferit... nu din sport", „U15; peste vârsta U11, extrapolare").
- Nu s-a găsit nicio sursă folosită într-un mod nepotrivit cu domeniul ei fără avertisment.

## Verificarea separării celor trei domenii de dovadă (CH-0405)

Confirmat: timp activ, organizare/rotații și siguranță sunt tratate ca secțiuni distincte, cu titluri proprii, în capitol și în fișa de teren (`CH_0405_ACTIVE_TIME_ORGANIZATION_CARD.md`). Nivelurile epistemice diferă onest între domenii (`CLM-0095`: MODERATE, `CLM-0096`: LOW, `CLM-0097`: HIGH) — niciun domeniu nu împrumută soliditatea celuilalt. Secțiunea de siguranță folosește surse oficiale FIFA/F-MARC (`SRC-0102`, Bizzini & Dvorak, narrative review oficial) plus un RCT publicat în *Sports Medicine*, nu doar surse generice de fitness.

## Verificarea evitării dogmei opuse (CH-0402)

Capitolul are o secțiune dedicată, „Despre limitele metodei", care respinge explicit ideea că manipularea constrângerilor (CLA) e superioară în orice situație instrucției directe, citând o analiză critică (`SRC-0088`) al cărei abstract confirmă exact această poziție de mijloc. Instrucția directă e păstrată explicit ca opțiune legitimă („Păstrează instrucția directă pentru clarificări tehnice punctuale sau reguli de siguranță — nu o elimină complet"), inclusiv în secțiunea „Intervenția dacă mesajul nu funcționează". Nu s-a găsit nicio propoziție care ar reintroduce implicit dogma CLA ca superioară universal.

## Limbaj pentru copil

Toate cele 6 formulări „Formularea exactă pentru copil" sunt scurte, la persoana întâi plural (coechipier) sau imperativ prietenos, non-diagnostice, fără termeni clinici sau presiune de performanță. Niciuna nu presupune o etichetă fixă asupra copilului. Toate rămân orientate spre acțiune sau observație imediată, potrivite pentru 10–11 ani.

## Fișe de teren

Toate cele 6 fișe (`docs/content/CH_040X_*.md`) au fost citite integral. Toate corespund conținutului actual al capitolelor, fără cifre fabricate rămase și fără conținut vechi. Fiecare fișă declară explicit, în propria secțiune „Scop", când exemplele numerice (dimensiuni de teren, formate) sunt euristică practică ManualFC și nu praguri validate de cercetare — un tipar consecvent pe toate cele 6 fișe, nu doar pe cele cu problema istorică cea mai vizibilă.

## Gate-uri de validare (rulate independent)

| Comandă | Rezultat |
|---|---|
| `PYTHONIOENCODING=utf-8 python scripts/validate_content.py --strict` | `VALID: 0 erori, 0 avertismente, 0 informații` |
| `PYTHONIOENCODING=utf-8 python scripts/validate_project.py` | `0 erori, 0 avertismente` (192 taskuri: 50 DONE, 141 PENDING, 1 READY — `TASK-0810` însuși, înainte de închiderea sa) |
| `PYTHONIOENCODING=utf-8 python scripts/generate_task_registry.py --check` | `Registrul este reproductibil: 192 taskuri.` |
| `PYTHONIOENCODING=utf-8 python -m unittest discover -s tests -p "test_*.py"` | `Ran 355 tests ... OK` |

Notă: aceste gate-uri verifică integritate structurală/schema, nu adevărul conținutului — trecerea lor e necesară, dar insuficientă singură pentru verdictul de mai sus. Verdictul se bazează pe verificarea bibliografică externă (CrossRef + verificarea terță OpenAlex pentru cifra centrală de siguranță) și recitirea integrală descrise mai sus, nu doar pe aceste comenzi.

## Concluzie

TASK-0809 și-a făcut treaba corect. Cele 21 de surse noi introduse sunt reale, verificabile, corect atribuite și folosite în limitele epistemice pe care le susțin de fapt. Cele 5 claim-uri `REPLACED` au înlocuitori valizi. Cifra cea mai încărcată epistemic a volumului (reducerea de 48% a riscului de accidentare, FIFA 11+ Kids) rezistă unei verificări terțe independente, cuvânt cu cuvânt. Nicio dogmă nu a fost înlocuită cu dogma opusă la CH-0402. Cele trei domenii de dovadă din CH-0405 rămân distincte, cu niveluri epistemice onest diferențiate. Limbajul pentru copii e potrivit vârstei. Cele 2 constatări minore de mai sus sunt oportunități de polish cosmetic, nu defecte care justifică o remediere de conținut.

**Verdict: `PASS_FIELD_REVIEW_READY`.**
