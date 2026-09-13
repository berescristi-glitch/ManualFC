# Pedagogul — harta completă de domeniu

**Versiune:** 1.0.0 · **Task de referință:** TASK-2902 · **Statut:** Architecture (PHASE-29)

Taxonomie completă pentru pilonul PEDAGOGUL („Înțelege copilul." — PE CINE ANTRENEZ?). Extinde categoriile deja canonice `cat.copilul-10-11`, `cat.psihologie`, `cat.comunicare`, `cat.parinti`, `cat.safeguarding` din `data/taxonomy/registry.json`. ID-urile domeniilor nu conțin vârstă (regulă §15 din arhitectura master) — vor rămâne valabile la extinderea multi-vârstă.

Prefix ID: `PED-D` (domeniu), `PED-D{n}-S` (subdomeniu). Legături spre conținut existent: capitolele Volumelor 01-04 unde există deja acoperire reală (nu presupusă).

## Legendă coloane

`EVIDENCE PRIORITY` / `RESEARCH PRIORITY` / `CONTENT PRIORITY`: `CRITICAL` / `HIGH` / `MEDIUM` / `LOW` — cât de urgent trebuie cercetat/scris, nu cât de important e conceptual (un subiect `LOW` pe cercetare poate fi deja bine acoperit).

---

## PED-D01 — Dezvoltarea copilului

**Întrebare:** Cum se dezvoltă real un copil de 10-11 ani, dincolo de vârsta cronologică?
**De ce contează în fotbalul U11:** Fără acest domeniu, antrenorul confundă maturizarea cu talentul sau lipsa de efort — cea mai frecventă sursă de decizii greșite de selecție/presiune la această vârstă.
**Acoperire existentă:** `content/volume-01/ch-0101` (variabilitate dezvoltare, competență motrică) — parțial construit.

| Subdomeniu | Întrebare | Cluster de concepte | Prioritate dovadă | Sensibilitate vârstă | Sensibilitate safeguarding |
|---|---|---|---|---|---|
| PED-D01-S01 Dezvoltare cognitivă | Ce poate procesa/reține copilul la această vârstă? | atenție, memorie de lucru, gândire operațională concretă | HIGH | AGE_SPECIFIC | LOW |
| PED-D01-S02 Dezvoltare emoțională | Cum reglează copilul emoția la 10-11 ani? | reglare emoțională, autocontrol, frustrare | HIGH | AGE_SPECIFIC | LOW |
| PED-D01-S03 Dezvoltare socială | Cum se raportează copilul la grup la această vârstă? | apartenență, status, prietenie | MEDIUM | AGE_SPECIFIC | LOW |
| PED-D01-S04 Dezvoltare motrică | Ce e realist motric la 10-11 ani? | coordonare, control motric fin, viteză de procesare motrică | HIGH | AGE_SPECIFIC | LOW |
| PED-D01-S05 Maturizare | Cum variază maturizarea biologică independent de vârsta cronologică? | maturizare timpurie/târzie, variabilitate | CRITICAL | AGE_SPECIFIC | MEDIUM (risc de etichetare nedreaptă) |
| PED-D01-S06 Diferențe individuale de dezvoltare | De ce doi copii de 10 ani pot fi la niveluri diferite? | variabilitate normală, vârstă cronologică vs. dezvoltare | CRITICAL | AGE_SPECIFIC | MEDIUM |
| PED-D01-S07 Vârstă cronologică vs. dezvoltare | Cum evită antrenorul confuzia sistematică între cele două? | eroare de atribuire, comparație nedreaptă | CRITICAL | AGE_SPECIFIC | HIGH |

**Competențe pedagogice legate:** `PED-C02` (înțelege comportamentul în context de dezvoltare), `PED-C10` (adaptează la diferențe individuale).
**Competențe de coaching legate:** `COACH-C13` (diferențiere), `COACH-C16` (progresie/regresie).
**Conexiuni de practică:** regresie/progresie per exercițiu (câmp deja existent în schema `exercise.schema.json`).

---

## PED-D02 — Învățarea

**Întrebare:** Cum învață real un copil o deprindere sau o decizie, nu doar cum o exersează?
**De ce contează:** Fundamentează de ce exercițiile ManualFC amplifică o problemă în loc să dicteze o coregrafie (deja principiu de produs, `PRODUCT_VISION.md`).

| Subdomeniu | Întrebare | Cluster de concepte | Prioritate dovadă | Sensibilitate vârstă | Safeguarding |
|---|---|---|---|---|---|
| PED-D02-S01 Atenție | Cât și ce poate urmări copilul simultan? | atenție selectivă, capacitate de procesare | HIGH | AGE_SPECIFIC | LOW |
| PED-D02-S02 Memorie | Cum reține copilul o instrucțiune sau un reper? | memorie de lucru, memorie procedurală | MEDIUM | AGE_SPECIFIC | LOW |
| PED-D02-S03 Încărcare cognitivă | Câtă informație simultană e utilă vs. copleșitoare? | încărcare cognitivă intrinsecă/extrinsecă | HIGH | AGE_SPECIFIC | LOW |
| PED-D02-S04 Explorare | Ce rol are explorarea liberă în învățare? | descoperire ghidată, explorare | HIGH | UNIVERSAL | LOW |
| PED-D02-S05 Repetiție | Repetiția identică ajută sau blochează transferul? | repetiție fără repetiție, variabilitate practică | HIGH | UNIVERSAL | LOW |
| PED-D02-S06 Variabilitate | De ce variația contextului ajută retenția? | variabilitate practică, interferență contextuală | HIGH | UNIVERSAL | LOW |
| PED-D02-S07 Învățare implicită/explicită | Când instrucția verbală ajută și când o blochează? | învățare implicită, instrucție explicită | CRITICAL | AGE_SPECIFIC | LOW |
| PED-D02-S08 Transfer | Ce condiții permit transferul spre joc liber? | transfer aproape/departe | CRITICAL | UNIVERSAL | LOW |
| PED-D02-S09 Retenție | Ce diferă între performanța imediată și retenția reală? | retenție, uitare, curba învățării | MEDIUM | UNIVERSAL | LOW |

**Competențe pedagogice:** `PED-C01` (observă înainte de a judeca), `PED-C07` (susține autonomia).
**Competențe de coaching:** `COACH-C01` (observație), `COACH-C09` (predare percepție/decizie), `COACH-C25` (verificare transfer).
**Conexiuni de practică:** deja implementat parțial — `related_exercises`, câmpul `regression`/`progression` din schema exercițiu.

---

## PED-D03 — Motivația

**Întrebare:** Ce face un copil să vrea să continue, nu doar să participe?
**De ce contează:** Retenția reală în fotbalul de bază depinde de motivație intrinsecă, nu de recompense externe repetate.

| Subdomeniu | Întrebare | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|---|
| PED-D03-S01 Motivație intrinsecă/extrinsecă | Ce diferență practică au cele două tipuri? | teoria autodeterminării | HIGH | UNIVERSAL | LOW |
| PED-D03-S02 Autonomie | Cum oferă antrenorul alegere reală fără haos? | susținerea autonomiei | HIGH | AGE_SENSITIVE | LOW |
| PED-D03-S03 Competență | Cum simte copilul progres real? | percepție de competență | HIGH | UNIVERSAL | LOW |
| PED-D03-S04 Relaționare | Cum contribuie apartenența la grup la motivație? | relatedness | MEDIUM | UNIVERSAL | LOW |
| PED-D03-S05 Auto-eficacitate | Cum se construiește încrederea că poate reuși? | self-efficacy | HIGH | UNIVERSAL | LOW |
| PED-D03-S06 Implicare | Ce ține copilul prezent mental, nu doar fizic? | engagement | MEDIUM | UNIVERSAL | LOW |
| PED-D03-S07 Recompense | Când o recompensă ajută și când subminează motivația? | efectul de subminare | HIGH | UNIVERSAL | LOW |
| PED-D03-S08 Presiune | Cum afectează presiunea (părinte/antrenor/competiție) motivația? | presiune evaluativă | CRITICAL | UNIVERSAL | HIGH |

**Competențe pedagogice:** `PED-C07` (susține autonomia), `PED-C13` (reflectează asupra propriului impact).
**Competențe de coaching:** `COACH-C31` (climat motivațional).
**Conexiuni de practică:** feedback informativ vs. laudă generică (deja parțial în `child_message` din exerciții).

---

## PED-D04 — Emoțiile

**Întrebare:** Ce trăiește real copilul în timpul antrenamentului?
**De ce contează:** Frica de greșeală și rușinea publică sunt cele mai frecvente cauze de abandon la această vârstă.

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D04-S01 Frustrare | reglare emoțională, toleranță la frustrare | HIGH | AGE_SPECIFIC | LOW |
| PED-D04-S02 Anxietate | anxietate de performanță | HIGH | AGE_SENSITIVE | MEDIUM |
| PED-D04-S03 Frica de eroare | climat de eroare, evaluare percepută | CRITICAL | UNIVERSAL | MEDIUM |
| PED-D04-S04 Jenă/rușine | expunere publică, comparație socială | HIGH | AGE_SENSITIVE | HIGH |
| PED-D04-S05 Încredere | încredere în sine, atribuire | HIGH | UNIVERSAL | LOW |
| PED-D04-S06 Siguranță psihologică | climat de siguranță | CRITICAL | UNIVERSAL | HIGH |
| PED-D04-S07 Succes/eșec | atribuire cauzală, mentalitate de creștere | HIGH | UNIVERSAL | MEDIUM |

**Acoperire existentă:** `content/volume-03/ch-0303` (siguranță emoțională) — construit.
**Competențe pedagogice:** `PED-C05` (creează siguranță psihologică), `PED-C08` (protejează demnitatea).
**Competențe de coaching:** `COACH-C08` (feedback), `COACH-C31` (climat motivațional).

---

## PED-D05 — Eroarea și eșecul

**Întrebare:** Ce face antrenorul cu o greșeală — informație sau verdict?
**De ce contează:** Principiu fondator deja adoptat de produs (`docs/architecture/*`, testat prin `test_task0806_reflection_transfer.py`).

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D05-S01 Învățare prin eroare | eroare ca informație, nu verdict | HIGH | UNIVERSAL | LOW |
| PED-D05-S02 Climat de eroare | climat orientat spre efort vs. rezultat | HIGH | UNIVERSAL | MEDIUM |
| PED-D05-S03 Răspuns la eșec | reacția adultului la eșecul copilului | CRITICAL | UNIVERSAL | HIGH |
| PED-D05-S04 Evitarea fricii | evitare comportamentală indusă de frică | HIGH | UNIVERSAL | MEDIUM |
| PED-D05-S05 Experimentare | permisiunea de a încerca fără penalizare | HIGH | UNIVERSAL | LOW |

**Acoperire existentă:** `content/volume-01/ch-0103` (eroare de decizie), deja cu dosar de cercetare complet (`research/dossiers/ch-0103-decision-error.md`) — cel mai matur domeniu din tot Pedagogul.
**Competențe pedagogice:** `PED-C06` (răspunde constructiv la eroare).
**Competențe de coaching:** `COACH-C08` (feedback), `COACH-C26` (evaluare).

---

## PED-D06 — Comunicarea

**Întrebare:** Cum ajunge un mesaj la un copil de 10-11 ani fără să se piardă sau să copleșească?
**De ce contează:** Fiecare exercițiu canonic are deja un `child_message` — acest domeniu explică de ce mesajul e formulat așa.

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D06-S01 Limbaj adecvat vârstei | complexitate lexicală, lungime propoziție | HIGH | AGE_SPECIFIC | LOW |
| PED-D06-S02 Ascultare | ascultare activă a copilului | MEDIUM | UNIVERSAL | LOW |
| PED-D06-S03 Explicație | claritate, concizie | HIGH | AGE_SENSITIVE | LOW |
| PED-D06-S04 Chestionare | întrebări ghidate vs. instrucție directă | CRITICAL | AGE_SENSITIVE | LOW |
| PED-D06-S05 Feedback | feedback specific vs. laudă generică | HIGH | UNIVERSAL | LOW |
| PED-D06-S06 Cueing | reper extern vs. instrucție tehnică internă | HIGH | UNIVERSAL | LOW |
| PED-D06-S07 Comunicare non-verbală | ton, poziție, expresie | MEDIUM | UNIVERSAL | LOW |

**Acoperire existentă:** `content/volume-01/ch-0104` (mesaj pedagogic), `content/volume-03/ch-0301/0302` (limbaj concis, întrebări ghidate) — bine construit.
**Competențe pedagogice:** `PED-C03` (comunică adecvat vârstei), `PED-C04` (ascultă activ).
**Competențe de coaching:** `COACH-C07` (întrebare), `COACH-C08` (feedback), `COACH-C09` (cueing).

---

## PED-D07 — Relația pedagogică

**Întrebare:** Ce fel de relație de autoritate construiește antrenorul cu copilul?

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D07-S01 Autoritate | autoritate vs. autoritarism | HIGH | UNIVERSAL | HIGH |
| PED-D07-S02 Respect | respect reciproc | MEDIUM | UNIVERSAL | HIGH |
| PED-D07-S03 Încredere | construirea încrederii | HIGH | UNIVERSAL | HIGH |
| PED-D07-S04 Limite | limite sănătoase, disciplină respectuoasă | CRITICAL | UNIVERSAL | HIGH |
| PED-D07-S05 Corectitudine | tratament echitabil | HIGH | UNIVERSAL | HIGH |
| PED-D07-S06 Autonomie în relație | spațiu de decizie al copilului | MEDIUM | AGE_SENSITIVE | MEDIUM |
| PED-D07-S07 Relația adult-copil | putere asimetrică, responsabilitate adultului | CRITICAL | UNIVERSAL | HIGH |

**Acoperire existentă:** `content/volume-03/ch-0304` (disciplină respectuoasă) — construit.
**Competențe pedagogice:** `PED-C09` (stabilește limite sănătoase), `PED-C08` (protejează demnitatea).
**Competențe de coaching:** `COACH-C31` (climat motivațional).

---

## PED-D08 — Dinamica de grup

**Întrebare:** Cum funcționează 12-18 copii ca grup, nu ca sumă de indivizi?

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D08-S01 Apartenență | sentiment de apartenență la echipă | MEDIUM | UNIVERSAL | LOW |
| PED-D08-S02 Cooperare | cooperare vs. competiție internă | HIGH | UNIVERSAL | LOW |
| PED-D08-S03 Competiție | competiție sănătoasă vs. nesănătoasă | HIGH | AGE_SENSITIVE | MEDIUM |
| PED-D08-S04 Conflict | rezolvarea conflictului între copii | HIGH | UNIVERSAL | MEDIUM |
| PED-D08-S05 Status | ierarhie informală în grup | MEDIUM | UNIVERSAL | MEDIUM |
| PED-D08-S06 Includere | includerea copiilor marginali | CRITICAL | UNIVERSAL | HIGH |
| PED-D08-S07 Relații între egali | dinamica prieteniilor și excluderii | MEDIUM | UNIVERSAL | HIGH |

**Competențe pedagogice:** `PED-C11` (creează apartenență).
**Competențe de coaching:** `COACH-C17` (organizare de grup).
**Conexiuni de practică:** Group Configurator (deja implementat, `docs/architecture/GROUP_CONFIGURATOR.md`) — locul natural unde dinamica de grup devine decizie practică (mărime de grupă, rotație).

---

## PED-D09 — Safeguarding

**Întrebare:** Ce garantează că niciun copil nu e expus unui risc evitabil?
**De ce contează:** Domeniu deja parțial implementat (`schemas/safeguarding.schema.json`, `data/safeguarding/canonical.json`, `test_safeguarding.py`) — cel mai reglementat domeniu din tot produsul.

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D09-S01 Protecția copilului | principii de bază | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S02 Limite | limite fizice și verbale ale adultului | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S03 Bullying | recunoaștere și intervenție | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S04 Discriminare | tratament echitabil indiferent de nivel/gen/origine | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S05 Recunoașterea riscului | semne de risc care depășesc rolul antrenorului | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S06 Raportare | ce face antrenorul când observă un risc | CRITICAL | UNIVERSAL | HIGH |
| PED-D09-S07 Comportament sigur de coaching | limite de contact, comunicare, poziționare | CRITICAL | UNIVERSAL | HIGH |

**Acoperire existentă:** `data/safeguarding/canonical.json`, validat fail-closed prin schemă — deja producție, nu doar arhitectură.
**Competențe pedagogice:** toate competențele PED au o componentă de safeguarding implicită (regulă transversală, nu o competență separată).
**Regulă permanentă (reconfirmată din TASK-2806):** safeguarding nu poate fi niciodată plătit/blocat comercial.

---

## PED-D10 — Părinții

**Întrebare:** Cum lucrează antrenorul constructiv cu adulții din jurul copilului?

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D10-S01 Rolul părintelui | rol de sprijin vs. rol de presiune | HIGH | UNIVERSAL | MEDIUM |
| PED-D10-S02 Comunicare cu părinții | mesaje clare, așteptări comune | HIGH | UNIVERSAL | LOW |
| PED-D10-S03 Așteptări | gestionarea așteptărilor nerealiste | HIGH | UNIVERSAL | MEDIUM |
| PED-D10-S04 Conflict cu părinți | dezacord, presiune la marginea terenului | HIGH | UNIVERSAL | MEDIUM |
| PED-D10-S05 Competiție (presiune parentală) | comparație între copii, presiune de rezultat | HIGH | UNIVERSAL | HIGH |
| PED-D10-S06 Perspectivă centrată pe dezvoltare | cum explică antrenorul prioritatea dezvoltării | HIGH | UNIVERSAL | LOW |

**Competențe pedagogice:** `PED-C12` (lucrează constructiv cu părinții).
**Conexiuni de practică:** momentan absent din exercițiu/ședință — legătură viitoare prin comunicare pre/post-ședință (nu implementat).

---

## PED-D11 — Diferențe individuale

**Întrebare:** Cum adaptează antrenorul fără să eticheteze sau să diagnosticheze?

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D11-S01 Variabilitate dezvoltare | vezi PED-D01-S06, aplicată la adaptare | CRITICAL | AGE_SPECIFIC | MEDIUM |
| PED-D11-S02 Încredere individuală | diferențe de încredere între copii | HIGH | UNIVERSAL | LOW |
| PED-D11-S03 Temperament | temperament, unde dovada susține (fără etichetare clinică) | MEDIUM | UNIVERSAL | HIGH |
| PED-D11-S04 Experiență anterioară | istoricul copilului cu sportul/eșecul | MEDIUM | UNIVERSAL | MEDIUM |
| PED-D11-S05 Diferențe de învățare | adaptare fără diagnostic | CRITICAL | UNIVERSAL | HIGH |

**Regulă permanentă (reconfirmată):** niciun conținut din acest domeniu nu produce diagnostic medical/psihologic — regulă deja aplicată produsului (`FINAL_PRODUCT_FEATURE_LEDGER.md`, safeguarding).

---

## PED-D12 — Reflecție și metacogniție (a copilului)

**Întrebare:** Cum ajută antrenorul copilul să înțeleagă propria decizie, nu doar să o repete?
**Distincție importantă:** acest domeniu e despre metacogniția **copilului**; reflecția **antrenorului** e domeniu de Coaching (`COACH-D32`/`COACH-D33`), nu se confundă.

| Subdomeniu | Cluster | Dovadă | Vârstă | Safeguarding |
|---|---|---|---|---|
| PED-D12-S01 Ajutor pentru înțelegere | verbalizare ghidată a deciziei | HIGH | AGE_SENSITIVE | LOW |
| PED-D12-S02 Auto-reflecție adecvată vârstei | cât de complexă poate fi introspecția la 10-11 ani | HIGH | AGE_SPECIFIC | LOW |
| PED-D12-S03 Autonomie în reflecție | copilul numește, nu doar confirmă | MEDIUM | AGE_SENSITIVE | LOW |
| PED-D12-S04 Conștientizarea deciziei | „de ce am ales asta" | HIGH | AGE_SENSITIVE | LOW |

**Acoperire existentă:** `content/volume-04/ch-0806` (reflecție și transfer) — construit; produsul are deja o buclă de reflecție post-ședință (TASK-2803) care operaționalizează parțial acest domeniu la nivelul antrenorului, nu încă la nivelul copilului.

---

## Rezumat de prioritate (pentru `PHASE30_RESEARCH_ROADMAP.md`)

| Domeniu | Prioritate cercetare | Motiv |
|---|---|---|
| PED-D05 (eroare) | LOW — deja acoperit matur | dosar complet existent |
| PED-D09 (safeguarding) | LOW — deja producție | schema + date canonice existente |
| PED-D06 (comunicare) | LOW-MEDIUM — parțial acoperit | 3 capitole existente |
| PED-D01 (dezvoltare), PED-D02 (învățare) | HIGH | fundamentează tot restul |
| PED-D03 (motivație), PED-D04 (emoții) | HIGH | direct legate de retenție, cerute des în auditurile de produs |
| PED-D07 (relație pedagogică) | HIGH | parțial acoperit, lipsă componentă de autoritate/limite |
| PED-D08 (grup), PED-D11 (diferențe individuale) | MEDIUM | conectate la Group Configurator existent |
| PED-D10 (părinți) | MEDIUM | zero acoperire de cercetare azi |
| PED-D12 (metacogniție copil) | MEDIUM | parțial acoperit prin Volume 04 |
