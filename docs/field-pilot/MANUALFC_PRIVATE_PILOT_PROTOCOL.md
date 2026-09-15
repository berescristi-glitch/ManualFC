# Protocolul pilotului privat ManualFC

**Task de referință:** TASK-3713. **Stare:** protocol pregătit, `FIELD_INPUT_REQUIRED = YES` — niciun antrenor nu a fost încă recrutat, nicio ședință nu a avut loc, niciun rezultat nu există. **Relație cu PHASE-23 / TASK-2301:** acel pilot izola o singură ședință (`SES-0001`) pentru un singur antrenor și rămâne, la rândul lui, neexecutat (`FIELD_INPUT_REQUIRED` neschimbat). Acest protocol nu îl anulează — îl extinde la 2-3 antrenori și la produsul complet actual (15 exerciții, 6 ședințe, Decision Engine cu 8 probleme, Spațiul meu, offline). Ambele rămân guvernate de aceeași regulă absolută: **niciun rezultat, comportament de copil, citat de antrenor sau dată de sesiune nu se inventează sau se simulează.** Un protocol pregătit nu este o dovadă de teren.

## 1. Scopul pilotului

Testează dacă antrenori reali pot folosi ManualFC ca să pregătească și să conducă un antrenament real, fără ajutorul echipei de produs, și dacă produsul rezistă la condițiile reale de teren (telefon, conexiune instabilă, timp limitat). Pilotul nu măsoară dacă antrenorii sunt mulțumiți — măsoară dacă reușesc sarcinile, unde ezită, unde greșesc și unde renunță.

Nu este un test al copiilor. Nu este o evaluare a antrenorului. Este un test al produsului, folosind comportament real ca dovadă.

## 2. Profilul participantului și criterii de includere

**Cine se califică:**
- antrenor activ sau recent activ cu copii de aproximativ 10–11 ani (2015–2016), în club, academie sau context organizat independent;
- acces la un grup real de copii cu care poate conduce cel puțin o ședință în perioada pilotului;
- acces la un telefon și, ideal, la un laptop/desktop (nu obligatoriu — vezi §7);
- dispus să încerce produsul fără ghidare live din partea echipei ManualFC în timpul sesiunilor observate.

**Cine nu se califică pentru acest pilot:**
- antrenori care au contribuit deja la conținutul ManualFC sau au acces privilegiat la echipa de produs (introduce distorsiune — nu pot evalua „primul contact" cu produsul);
- context fără niciun grup real de copii disponibil în fereastra pilotului (pilotul cere ședințe reale, nu simulări).

**Număr țintă:** 2–3 antrenori. Motivul plafonului: la acest număr, fiecare constatare de utilizabilitate poate fi urmărită individual, pe persoană și context, fără a avea nevoie de agregare statistică — potrivit pentru un pilot calitativ, nu pentru validare cantitativă.

## 3. Ipoteze de recrutare

Recrutarea rămâne responsabilitatea persoanei care conduce pilotul (nu a acestui document). Ipoteze care trebuie confirmate înainte de start, nu presupuse:

- antrenorii sunt contactați direct (rețea personală, club, asociație), nu prin reclamă publică;
- niciun antrenor nu este plătit pentru participare, dar timpul lui e respectat (fereastră scurtă, sarcini clare, fără sesiuni lungi de interviu);
- fiecare antrenor confirmă explicit disponibilitatea pentru numărul minim de ședințe (§5) înainte de a începe;
- dacă mai puțin de 2 antrenori confirmă, pilotul nu pornește ca „pilot" — devine un singur studiu de caz, raportat ca atare, nu extrapolat.

## 4. Participare informată și limite de confidențialitate

**Ce i se spune fiecărui antrenor înainte de a începe** (vezi formularea exactă în `PRIVATE_PILOT_COACH_PACK.md`):
- ce se testează (produsul, nu el);
- ce se cere de la el (sarcini concrete, timp aproximativ);
- ce se notează despre el (fără nume, fără date de contact în orice document păstrat după pilot — vezi mai jos);
- că poate renunța oricând, fără explicație;
- că nu se colectează absolut nicio informație despre copii.

**Limite stricte, fără excepție:**
- **fără date despre copii** — nici nume, nici inițiale care ar putea fi legate de un copil real, nici fotografii, nici informații de sănătate sau comportament individual atribuibil unui copil identificabil;
- **fără nume de club sau locație precisă** — „un club din județul X" sau „grupă de club" e suficient de context; nu se cere adresa, numele clubului sau numele competiției;
- **fără identitatea antrenorului în documentele păstrate** — antrenorii sunt codificați `A1`, `A2`, `A3` în orice document de analiză; numele real (dacă a fost necesar pentru coordonare logistică) nu apare în niciun fișier din acest repository;
- **fără audio, video sau fotografie de teren identificabilă** — dacă echipa de produs dorește vreodată să înregistreze o sesiune, aceasta necesită autorizare separată, explicită, în afara acestui task, cu acord scris al antrenorului și al clubului/părinților pentru orice copil care ar putea apărea în cadru. Acest protocol NU autorizează nicio înregistrare.
- coordonarea logistică (nume, telefon, WhatsApp) există doar în afara acestui repository (mesagerie personală a coordonatorului pilotului) — niciodată în fișiere commise aici.

## 5. Durata pilotului și numărul de ședințe

- **Fereastră totală:** 2–4 săptămâni calendaristice de la primul contact cu primul antrenor, suficient pentru ca fiecare să găsească o fereastră reală de antrenament fără presiune de timp artificială.
- **Ședințe reale minime per antrenor:** 2 ședințe complete de antrenament folosind conținut ManualFC, la interval de minimum 3-4 zile una de alta (nu în aceeași zi — nu testează retenția reală dacă sunt consecutive).
- **Tip de ședință:** cel puțin o ședință canonică completă (`SES-0001` sau `SES-0002`, care folosesc doar exercițiile deja pilotate parțial în teorie, sau oricare din cele 6 ședințe canonice, la alegerea antrenorului pe baza grupei lui) și cel puțin o utilizare a Decision Engine-ului („Rezolvă pe teren") pentru o problemă reală observată la propriul grup, independent de ședința canonică.
- Antrenorul alege ședința și problema — nu i se dictează care, pentru ca alegerea însăși să fie o dovadă (ce a găsit relevant, nu ce i s-a recomandat).

## 6. Sarcini obligatorii per antrenor

Fiecare antrenor parcurge, cel puțin o dată în fereastra pilotului, toate cele 9 scenarii de mai jos (detaliate cu pași exacți în `PRIVATE_PILOT_COACH_PACK.md`):

1. Găsește o problemă de joc relevantă pentru propriul grup, pornind doar de la homepage, fără link direct primit de la coordonator.
2. Folosește Decision Engine-ul („Rezolvă pe teren") pentru acea problemă, până la o recomandare concretă.
3. Deschide și citește un exercițiu complet pe telefon, ca și cum s-ar pregăti chiar înainte de antrenament.
4. Pregătește și citește o ședință completă (toate segmentele), inclusiv Mod Teren, cel puțin o dată direct înainte de a antrena.
5. Identifică, dintr-un exercițiu la alegere, ce anume trebuie să observe și când trebuie să intervină — fără să i se explice acest lucru de coordonator.
6. Revine, într-o sesiune de folosire ulterioară, la un exercițiu/ședință/problemă folosit(ă) anterior, fără să-l caute din nou de la zero.
7. Folosește produsul cu conexiune limitată sau deloc — cel puțin o dată, verifică ce rămâne disponibil (ideal: chiar la teren, unde semnalul e real, nu simulat în oraș).
8. Pornește de la un principiu sau de la un volum de metodologie și ajunge la un exercițiu conectat, apoi citește explicit ce spune exercițiul despre transferul în meci.
9. Completează o reflecție după cel puțin o ședință reală, în „Spațiul meu".

## 7. Condiții mobil și desktop

- Fiecare antrenor folosește **telefonul propriu** pentru sarcinile 3, 6 și 7 (mobil e contextul real de teren) — nu un dispozitiv oferit de coordonator, pentru ca friecțiunile reale de ecran/browser/versiune de sistem să fie vizibile.
- Sarcinile 1, 2, 4, 5, 8, 9 pot fi făcute pe orice dispozitiv are antrenorul disponibil (telefon, tabletă, laptop) — se notează explicit ce dispozitiv a folosit, pentru fiecare sarcină, în formularul de observație.
- Dacă un antrenor nu are acces la desktop/laptop deloc, pilotul continuă doar pe mobil — se notează ca limitare a eșantionului, nu se exclude antrenorul.

## 8. Condiții online și offline

- Cel puțin o interacțiune (sarcina 7) trebuie să aibă loc cu conexiune absentă sau vizibil instabilă — ideal chiar pe terenul de antrenament, nu simulat prin mod avion acasă (deși modul avion acasă e acceptabil dacă terenul chiar nu permite testarea).
- Se cere explicit ca antrenorul să încerce **cel puțin o dată să pregătească o ședință pentru offline** înainte de a pleca spre teren (butonul „Disponibil pe teren" din Spațiul meu) și **cel puțin o dată să deschidă produsul deja offline, fără pregătire prealabilă**, pentru a vedea diferența reală dintre cele două experiențe.
- Restul sarcinilor se fac în condiții normale de conectivitate.

## 9. Metoda de observare

Nu există instrumentare tehnică de urmărire (fără analytics, fără telemetrie) — observarea e manuală, prin unul din cele două canale, în funcție de ce e realist pentru fiecare antrenor:

- **A. Auto-observare ghidată:** antrenorul completează singur `PRIVATE_PILOT_OBSERVATION_TEMPLATE.md` imediat după fiecare sarcină/ședință, cât mai aproape în timp de momentul faptei (nu la o săptămână distanță, din memorie).
- **B. Observare însoțită (dacă logistic posibil):** coordonatorul pilotului stă lângă antrenor (fizic sau pe apel video) în timp ce acesta parcurge sarcinile 1-6 și 8-9 prima dată, notează ce vede fără să intervină sau să sugereze soluții, apoi antrenorul completează aceleași secțiuni ale formularului cu propriile cuvinte.

Metoda B produce dovezi mai puternice (comportament observat direct, nu doar auto-raportat) și e preferată acolo unde logistica o permite. Metoda A e acceptabilă și trebuie tratată cu granița epistemică explicită din §11.

## 10. Întrebări de debrief / interviu

După fiecare ședință folosită pentru pilot, coordonatorul (sau antrenorul, dacă completează singur) pune aceste întrebări, în ordine, fără a sugera răspunsul:

1. Ce ai încercat să faci chiar înainte de exercițiul/ședința asta?
2. Unde ai ezitat sau te-ai oprit ca să te gândești ce urmează?
3. A existat un moment în care ai crezut că produsul face altceva decât a făcut de fapt?
4. Ce ai fi vrut să știi mai devreme decât ai aflat?
5. Ce ai făcut când nu ai avut semnal / conexiune?
6. Ai revenit la ceva folosit anterior? A fost ușor de găsit?
7. Ce ai ignorat complet, deși era pe ecran?
8. Dacă ai avea 30 de secunde să schimbi un singur lucru din ce ai folosit azi, ce ai schimba?

Nu se pun întrebări de satisfacție generală („ți-a plăcut?") ca măsură principală — răspunsurile la ele sunt notate dacă apar spontan, dar nu numără ca dovadă de utilizabilitate (vezi §12).

## 11. Dovezi comportamentale de capturat

Pentru fiecare sarcină din §6, formularul de observație cere, separat:

- **RAW OBSERVATION** — ce s-a întâmplat efectiv, fapt verificabil: pagina la care a ajuns, click-ul pe care l-a dat, timpul aproximativ până a găsit ceva, dacă a reușit sau nu sarcina fără ajutor;
- **INTERPRETATION** — de ce crede observatorul (antrenor sau coordonator) că s-a întâmplat asta — marcată explicit ca interpretare, niciodată amestecată cu observația brută;
- **CONFIDENCE** — cât de sigură e observația: `OBSERVAT_DIRECT` (cineva a văzut exact ce s-a întâmplat), `RAPORTAT_DE_ANTRENOR` (antrenorul a povestit ulterior, nu a fost observat live), `NECLAR` (nu se poate stabili cu certitudine ce s-a întâmplat).

Această separare urmează exact convenția deja stabilită de `PHASE23_FIELD_RETURN_TEMPLATE_R1.md` — nu e o invenție nouă a acestui task, e o extindere a unei discipline deja acceptate în proiect.

## 12. Distincția între ce spun antrenorii și ce fac efectiv

Regulă explicită de analiză, aplicată de oricine procesează datele întoarse (inclusiv o sesiune Claude viitoare):

- O afirmație de tipul „a fost ușor de folosit" NU e dovadă de utilizabilitate dacă `RAW OBSERVATION` arată ezitare, revenire la pagina anterioară de mai multe ori, sau abandonarea sarcinii.
- O afirmație de tipul „nu mi-a plăcut X" NU e automat un defect de reparat — devine constatare doar dacă se leagă de un comportament observat (nu a reușit sarcina, a folosit greșit o funcție, a ignorat o informație necesară).
- Complimentele generale („e un produs frumos") nu se înregistrează ca succes de utilizabilitate — se notează, dar nu influențează clasificarea de severitate (§13).
- Când ce spune antrenorul contrazice ce arată observația directă, **observația directă are prioritate** în clasificare; contradicția însăși se notează ca fapt interesant (poate arăta că problema e reală, dar antrenorul nu o percepe conștient — sau invers, o frustrare exprimată care nu a împiedicat de fapt sarcina).

## 13. Criterii de succes

Pilotul e considerat un succes pentru produs (nu pentru antrenor) dacă, agregat pe cei 2-3 antrenori:

- cel puțin 2 din 3 (sau 2 din 2) reușesc, fără ajutor din partea coordonatorului, toate cele 9 sarcini din §6;
- cel puțin o ședință completă e condusă efectiv cu copii reali, folosind conținut ManualFC ca sursă principală (nu doar consultat, ci efectiv folosit pe teren);
- comportamentul-țintă al cel puțin unui exercițiu apare, conform relatării antrenorului, fie în exercițiul structurat, fie în joc liber (indiferent care — ambele sunt informație validă, „nu a apărut" e la fel de valid ca „a apărut");
- funcția offline e testată real și antrenorul poate descrie diferența dintre „pregătit dinainte" și „neprepărat" (arată că a înțeles mecanismul, nu doar că a apăsat un buton).

## 14. Criterii de oprire

Pilotul se oprește (nu se continuă „ca să vedem ce iese") dacă:

- niciun antrenor nu reușește să găsească o problemă relevantă de la homepage în sarcina 1, în mai multe încercări — indică un defect de navigare mai profund decât poate repara un pilot, cere revenire la produs înainte de a continua cu alți antrenori;
- funcția offline eșuează complet (produsul devine inutilizabil, nu doar incomplet) pentru toți antrenorii testați — oprire imediată, raportare ca defect `MUST_FIX` (§13 din protocol, criteriile de mai jos), fără a mai cere altor antrenori să repete același eșec;
- un antrenor semnalează disconfort privind confidențialitatea (a simțit că i s-a cerut sau că a introdus accidental date despre un copil) — oprire imediată a acelui traseu de pilot, investigare separată, în afara scopului acestui protocol;
- mai puțin de 2 antrenori rămân disponibili la jumătatea ferestrei — pilotul continuă ca studiu de caz unic, nu ca „pilot", și raportul final trebuie să declare asta explicit.

## 15. Clasificarea severității constatărilor

| Severitate | Definiție | Exemplu |
|---|---|---|
| **CRITICĂ** | Antrenorul nu poate finaliza o sarcină obligatorie din §6, în nicio încercare, fără ajutor extern. | Nu poate deschide o ședință pregătită offline de deloc. |
| **MAJORĂ** | Antrenorul finalizează sarcina, dar cu confuzie vizibilă, timp mult peste așteptări, sau printr-o cale ocolitoare, nu prin calea intenționată. | Găsește exercițiul căutând pe Google în loc de căutarea din site. |
| **MODERATĂ** | Antrenorul finalizează sarcina normal, dar semnalează o ezitare sau o întrebare care ar putea afecta alți antrenori. | Nu a fost sigur dacă „Salvează" înseamnă că se sincronizează undeva. |
| **MINORĂ** | Observație de rafinament, fără impact asupra reușitei sarcinii. | Ar prefera un text de buton diferit. |

Severitatea se stabilește pe baza `RAW OBSERVATION`, niciodată doar pe baza unei păreri exprimate (`INTERPRETATION`) fără comportament corespunzător.

## 16. Metoda de prioritizare a frecvenței/frecției

Pentru fiecare constatare, se înregistrează:

- **Câți din antrenori** au întâmpinat-o (1, 2 sau 3 din cei disponibili);
- **La ce sarcină** din §6 a apărut;
- **Severitatea** (§15);
- **Dacă a fost observată direct sau doar raportată** (§11).

Prioritatea de reparare = severitate întâi, apoi frecvența (câți antrenori), apoi tipul de dovadă (observat direct > raportat). O constatare CRITICĂ văzută la un singur antrenor, dar observată direct, precede o constatare MODERATĂ raportată de toți trei.

## 17. Decizia MUST FIX / SHOULD FIX / NOT NOW / IGNORE

| Decizie | Regulă |
|---|---|
| **MUST FIX** | Orice constatare CRITICĂ, indiferent de câți antrenori a afectat; sau orice constatare MAJORĂ observată direct la 2 sau mai mulți antrenori. |
| **SHOULD FIX** | Constatare MAJORĂ la un singur antrenor; sau constatare MODERATĂ la 2 sau mai mulți antrenori, observată direct. |
| **NOT NOW** | Constatare MODERATĂ la un singur antrenor, sau orice constatare (indiferent de severitate) care ar cere o schimbare arhitecturală majoră, în afara „celei mai mici modificări necesare" — se documentează ca temă pentru un task viitor dedicat, nu se rezolvă ad-hoc. |
| **IGNORE** | Constatare MINORĂ fără legătură cu o sarcină obligatorie; preferință de stil fără dovadă comportamentală. |

Această decizie se aplică DUPĂ ce datele reale există — acest protocol nu clasifică nimic acum, pentru că nu există încă nicio constatare de clasificat.

## 18. Ce se întâmplă cu datele după pilot

Formularele completate (`PRIVATE_PILOT_OBSERVATION_TEMPLATE.md`, câte o copie per antrenor per sesiune) se colectează de coordonator și se procesează într-un task viitor separat (analog `PHASE23_FIELD_RETURN_TEMPLATE_R1.md`→procesare), respectând aceeași regulă: conținutul brut nu se rescrie, nu se „curăță", nu se completează cu presupuneri pentru câmpuri goale. Fișierele completate, dacă sunt păstrate în acest repository, se de-identifică complet (coduri `A1`/`A2`/`A3`, fără nume, fără club, fără locație precisă) înainte de commit.

## 19. Ce NU face acest protocol

- Nu recrutează antrenori — recrutarea rămâne o acțiune umană, în afara acestui repository.
- Nu programează ședințe reale — programarea rămâne responsabilitatea coordonatorului.
- Nu produce niciun rezultat, constatare sau citat — acestea nu există până la date reale de teren.
- Nu modifică `ASM-0001` sau conținutul canonic pe baza unor presupuneri despre ce ar putea spune antrenorii — la fel ca regula deja aplicată în Runda 1 (`docs/field-pilot/GOLD_STANDARD_SUPPORT_ANGLE_FIELD_SHEET_R1.md`, secțiunea 8: „Nu modifica ASM-0001 acum — doar observă").
