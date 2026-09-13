# Antrenorul — harta completă de domeniu

**Versiune:** 1.0.0 · **Task de referință:** TASK-2903 · **Statut:** Architecture (PHASE-29)

Taxonomie completă pentru pilonul ANTRENORUL („Învață să predai jocul." — CUM ÎL AJUT SĂ ÎNVEȚE?). Extinde `cat.antrenorul-pedagog`, `cat.perceptie-decizie`, `cat.tehnica-context`, `cat.evaluare`, `cat.metodologie-surse`. Prefix ID: `COACH-D`. 34 domenii, grupate în 8 clustere ale buclei reale de antrenament (nu ordine alfabetică — ordinea reflectă fluxul: cine sunt → ce văd → ce decid → cum predau → cum organizez → cum evaluez → cum planific → cum mă dezvolt).

Pentru fiecare domeniu: **întrebare profesională**, **cunoaștere de bază**, **comportamente observabile de antrenor**, **anti-tipare comune**, **legături** (pedagogie / principii de fotbal / practică), **priorități**.

---

## Cluster 1 — Identitate și fundament (COACH-D01)

### COACH-D01 — Identitatea antrenorului
**Întrebare:** Ce fel de antrenor vreau să fiu, dincolo de tactică?
**Cunoaștere de bază:** rolul de pedagog-întâi (`PRODUCT_VISION.md`), etică profesională, model de rol.
**Comportamente observabile:** își declară explicit prioritatea dezvoltării peste rezultat; recunoaște public limitele proprii de cunoaștere.
**Anti-tipare:** confundă identitatea de antrenor cu identitatea de fost jucător; copiază stilul unui antrenor profesionist fără adaptare la vârstă.
**Legături pedagogie:** toate domeniile PED (fundamentează atitudinea). **Principii de fotbal:** —. **Practică:** onboarding-ul din Spațiul meu (`profile.experience`, deja implementat).
**Dovadă:** MEDIUM · **Cercetare:** MEDIUM · **Conținut:** MEDIUM.

---

## Cluster 2 — Observație și formulare a problemei (COACH-D02–D06)

Acest cluster e deja parțial **implementat în produs** prin Decision Engine (`docs/architecture/PROBLEM_KNOWLEDGE_GRAPH.md`, `data/problems/problem-library.json`) — domeniile de mai jos numesc explicit competența din spatele funcției deja construite.

| ID | Domeniu | Întrebare profesională | Comportamente observabile | Anti-tipar comun | Practică legată |
|---|---|---|---|---|---|
| COACH-D02 | Observație | Ce se întâmplă efectiv, înainte de orice interpretare? | descrie comportamentul văzut, nu cauza presupusă | sare direct la diagnostic („nu e atent") | `OBSERVATION` — deja model semantic (`CONTENT_TAXONOMY.md` §4) |
| COACH-D03 | Observație vs. interpretare | Separă ce vede de ce crede că înseamnă? | etichetează explicit „observ" vs. „cred că" | confundă observația cu judecata de caracter | Decision Engine, deja separă `OBSERVATION`/`POSSIBLE_CAUSE` |
| COACH-D04 | Formularea problemei | Transformă observația într-o problemă lucrabilă? | formulează comportamental, nu ca etichetă de copil | „copilul e leneș" în loc de „nu se repoziționează după pasă" | `problem-library.json`, câmpul `observable_behavior` |
| COACH-D05 | Decizii de intervenție | Alege intervenția corectă pentru problema formulată? | alege dintre mai multe ipoteze testabile | prima idee devine singura acțiune | `possible_explanations` (deja în schema `problem`) |
| COACH-D06 | Când NU intervine | Recunoaște momentul în care tăcerea ajută mai mult? | lasă o încercare în plus înainte de a vorbi | intervine la fiecare repetiție („joystick coaching", deja documentat `ch-0103`) | Field Mode — „Ajustează dacă e nevoie" (deja opțional, nu implicit) |

**Dovadă:** CRITICAL pentru toate 5 · **Cercetare:** COACH-D06 CRITICAL (cel mai slab acoperit azi), restul HIGH · **Conținut:** HIGH.

---

## Cluster 3 — Comunicare de predare (COACH-D07–D11)

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D07 | Chestionare | Întreabă în loc să spună, când e util? | pune o întrebare deschisă înainte de a corecta | întreabă retoric, răspunde singur imediat | `content/volume-03/ch-0302` (întrebări ghidate) |
| COACH-D08 | Feedback | Feedback-ul e specific și legat de acțiune? | descrie ce s-a întâmplat + o singură schimbare | laudă generică („bravo") fără informație | câmpul `child_message` din exercițiu |
| COACH-D09 | Cueing | Folosește reper extern, nu instrucție tehnică internă? | „uită-te la con", nu „pune piciorul la 45°" | prescrie un unghi/poziție exactă a corpului | deja regulă de produs (`exact_cue`, prezent în EX-0003) |
| COACH-D10 | Demonstrație | Demonstrează util, fără să impună o singură formă corectă? | arată o variantă posibilă, nu „modelul" | „așa se face", ca unică soluție validă | — |
| COACH-D11 | Ghidarea atenției | Direcționează atenția copilului spre indiciul relevant? | numește exact ce să urmărească | supraîncarcă cu 5 instrucțiuni simultan | `observable_behaviours` din exercițiu |

**Dovadă:** HIGH · **Cercetare:** COACH-D07/D09 HIGH (parțial acoperite), COACH-D10/D11 MEDIUM · **Conținut:** HIGH.

---

## Cluster 4 — Proiectarea exercițiului (COACH-D12–D16)

Cel mai matur cluster din produs — implementat integral în Gold Standard (`docs/architecture/CONTENT_MODEL.md`, schema `exercise.schema.json`).

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D12 | Proiectare de exercițiu | Exercițiul amplifică problema reală sau doar o coregrafie? | păstrează cuplajul percepție-acțiune | exercițiu analitic fără opoziție reală | `content/volume-04/chapter-01.mdx (CH-0401)` (design reprezentativ) |
| COACH-D13 | Constrângeri | Manipulează spațiu/număr/reguli pentru a produce comportamentul țintă? | schimbă o constrângere, observă efectul | schimbă totul deodată, nu poate atribui efectul | `content/volume-04/chapter-02.mdx (CH-0402)` (constrângeri de sarcină) |
| COACH-D14 | Design reprezentativ de învățare | Exercițiul păstrează informația din jocul real? | opoziție activă, decizie reală păstrată | exercițiu fără adversar unde jocul are adversar | deja principiu de exercițiu Gold Standard |
| COACH-D15 | Variabilitate | Introduce variație utilă fără haos? | variază contextul, păstrează obiectivul | schimbă exercițiul la fiecare repetiție | — |
| COACH-D16 | Progresie/regresie | Are un pas înainte și un pas înapoi pregătit? | folosește regresia la primul semn de blocaj | insistă pe aceeași formă când nu funcționează | câmpurile `progression`/`regression`, deja în schemă |

**Dovadă:** HIGH · **Cercetare:** MEDIUM (bine fundamentat deja) · **Conținut:** LOW-MEDIUM (deja acoperit prin EX-0001-0005).

---

## Cluster 5 — Organizare și predare tactică (COACH-D17–D23)

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D17 | Organizare de grup | Grupează pentru siguranță și învățare, nu doar pentru numere egale? | folosește Group Configurator pentru decizie, nu presupunere | improvizează grupe fără logică de rotație | `docs/architecture/GROUP_CONFIGURATOR.md` — deja implementat |
| COACH-D18 | Spațiu/numere/reguli | Dimensionează corect pentru vârstă și obiectiv? | respectă `too_small_signs` din exercițiu | folosește un singur spațiu standard pentru orice | schema `exercise.field` — deja implementat |
| COACH-D19 | Poziționarea antrenorului | Se poziționează pentru observație maximă? | se mută pentru unghi de vedere, nu stă fix | stă mereu în același loc, indiferent de grup | Practice Heuristic în `GROUP_CONFIGURATOR.md` |
| COACH-D20 | Timp activ de învățare | Maximizează timpul de mișcare/decizie per copil? | reduce cozile, explicații scurte | explicație de 5 minute înaintea unui exercițiu de 8 | `content/volume-04/chapter-05.mdx (CH-0405)` (organizare timp activ) |
| COACH-D21 | Predare tactică | Predă tactica prin joc, nu prin diagramă pe tablă? | folosește oprire scurtă în timpul jocului (freeze), nu lecție separată | oprește jocul 5 minute pentru explicație teoretică | Field Mode (deja implementat) |
| COACH-D22 | Percepție | Antrenează ce vede copilul înainte de a decide? | folosește reper extern pentru scanare | corectează direct decizia fără a verifica ce a văzut copilul | Decision Engine → PRB-0003 (deja implementat, flagship) |
| COACH-D23 | Luarea deciziei | Antrenează decizia, nu doar execuția tehnică? | lasă mai multe soluții valide deschise | corectează orice decizie diferită de "a lui" | Problem Library — deja separă decizie de execuție |

**Dovadă:** HIGH · **Cercetare:** COACH-D19/D22 HIGH (mai puțin acoperite), restul MEDIUM · **Conținut:** MEDIUM.

---

## Cluster 6 — Tehnică, transfer și evaluare (COACH-D24–D26)

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D24 | Tehnică în context | Predă tehnica legată de decizie, nu izolat? | tehnică servește decizia (ex. orientare la recepție → continuare) | tehnică „corectă" fără legătură cu situația de joc | EX-0003 — deja acest model |
| COACH-D25 | Transfer | Verifică apariția comportamentului în joc liber, nu doar în exercițiu? | observă în jocul final, nu doar în exercițiul structurat | declară succes după o repetiție reușită în exercițiu | `SessionReflection.transferState` — deja implementat (TASK-2803) |
| COACH-D26 | Evaluare | Evaluează comportament observabil, nu impresie generală? | folosește criterii explicite (`ASM-0001`) | evaluare globală („a fost bine azi") | Assessment — deja implementat |

**Dovadă:** CRITICAL (COACH-D25, transferul real rămâne field input) · **Cercetare:** CRITICAL · **Conținut:** LOW (deja bine modelat).

---

## Cluster 7 — Planificare și diferențiere (COACH-D27–D31)

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D27 | Design de ședință | Leagă exerciții într-o progresie coerentă, nu o listă? | tranziții logice între exerciții | exerciții aleatorii puse cap la cap | SES-0001/0002 — deja implementat |
| COACH-D28 | Planificare | Planifică pe termen mediu, nu doar ședință cu ședință? | urmărește o temă pe mai multe ședințe | fiecare ședință repornește de la zero | `season-plans` — schemă existentă, conținut 0 |
| COACH-D29 | Diferențiere | Adaptează fără să separe vizibil copiii pe „niveluri"? | oferă variante fără etichetare publică | grupează vizibil „cei buni" vs. „ceilalți" | regresie/progresie per exercițiu |
| COACH-D30 | Comunicare (a antrenorului către grup) | Comunică eficient cu 12-18 copii simultan? | instrucțiuni scurte, verificare de înțelegere | monolog lung către tot grupul | `content/volume-03/ch-0301` |
| COACH-D31 | Climat motivațional | Creează climat orientat spre efort și învățare? | recunoaște efortul, nu doar rezultatul | laudă doar golul/execuția reușită | `PED-D03`, `PED-D05` |

**Dovadă:** HIGH · **Cercetare:** COACH-D28 HIGH (zero conținut azi) · **Conținut:** COACH-D28/D29 HIGH.

---

## Cluster 8 — Reflecție și dezvoltare profesională (COACH-D32–D34)

Distincție critică: aceste domenii sunt despre reflecția **antrenorului asupra propriei practici**, nu despre reflecția copilului (`PED-D12`). Produsul are azi o buclă de reflecție (TASK-2803) axată pe copil/transfer; dimensiunea de coach lipsește — vezi `THEORY_TO_PRACTICE_CONTRACT.md` §Reflection V2.

| ID | Domeniu | Întrebare | Comportamente observabile | Anti-tipar | Practică legată |
|---|---|---|---|---|---|
| COACH-D32 | Reflecție | Ce am observat despre propria intervenție, nu doar despre copii? | reflectă asupra deciziei proprii de a interveni/nu | reflectează doar asupra rezultatului copiilor | Reflection V2 (specificat, neimplementat) |
| COACH-D33 | Auto-evaluare | Evaluează onest propriul comportament de predare? | identifică un moment de supra-corectare | evită orice autocritică | Reflection V2 |
| COACH-D34 | Dezvoltare profesională | Are un traseu de competențe pe care le dezvoltă activ? | alege conștient o competență de exersat | repetă același stil fără reflecție asupra lui | Coach Development (fundație, neimplementat) |

**Dovadă:** MEDIUM · **Cercetare:** MEDIUM · **Conținut:** HIGH (zero azi, cluster complet nou).

---

## Rezumat de prioritate (pentru `PHASE30_RESEARCH_ROADMAP.md`)

| Cluster | Prioritate cercetare | Motiv |
|---|---|---|
| 2 (Observație/formulare problemă) | CRITICAL | fundamentează Decision Engine, produsul cel mai vizibil azi |
| 4 (Proiectare exercițiu) | LOW-MEDIUM | deja matur, 5 exerciții canonice construite pe el |
| 6 (Tehnică/transfer/evaluare) | CRITICAL pe transfer, LOW pe rest | transferul real rămâne `FIELD_INPUT_REQUIRED` |
| 3 (Comunicare de predare) | HIGH | direct legat de `child_message`/`exact_cue`, folosit în fiecare exercițiu |
| 5 (Organizare/predare tactică) | MEDIUM | Group Configurator deja implementat, lipsește doar partea de cercetare a poziționării antrenorului |
| 7 (Planificare/diferențiere) | HIGH pe planificare (0 conținut azi) | `season-plans` schema există, conținut inexistent |
| 8 (Reflecție/dezvoltare) | MEDIUM cercetare, HIGH conținut | cluster nou, fundamentează Coach Development |
| 1 (Identitate) | MEDIUM | scurt, fundamentează tonul restului |
