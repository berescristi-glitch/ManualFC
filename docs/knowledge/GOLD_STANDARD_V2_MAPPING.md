# Gold Standard V2 — maparea exactă (EX-0001–EX-0005, SES-0001–SES-0002)

**Versiune:** 1.0.0 · **Task de referință:** TASK-3407 (PHASE-32) · **Statut:** Documentație de mapare, NU migrare de schemă

Conform regulii §51 din specificația PHASE-32: acest document produce maparea exactă cerută, dar **nu migrează runtime-ul**. Niciun câmp nou nu a fost adăugat la `exercise.schema.json`/`session.schema.json`; toate valorile de mai jos sunt derivate direct din câmpurile deja existente (`primary_objective`, `rationales`, `coach_questions`, `common_errors`, `match_transfer`, etc.), verificate prin citirea directă a fișierelor JSON reale, nu presupuse. Migrarea efectivă a schemei rămâne o decizie viitoare (PHASE-33/Gold Standard V2 runtime).

## EX-0001 — Cine ne poate acoperi pe amândoi?

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C01 (Observă înainte de a judeca), PED-C07 (Susține autonomia) |
| COACH_COMPETENCY_IDS | COACH-C01 (Observație), COACH-C06 (Cueing), COACH-C11 (Predarea percepției și deciziei) |
| CHILD_OBJECTIVE | Recunoaște momentul în care un singur adversar poate acoperi simultan două opțiuni de pasă și se deplasează pentru a ieși din acea umbră defensivă |
| COACH_OBJECTIVE | Verifică dacă deplasarea laterală apare fără comandă verbală, folosind un singur focalizator (deplasarea, nu tehnica) |
| COACH_FOCUS | Cueing extern ("spațiul liber", nu "piciorul") + observație a apariției autonome a comportamentului |
| EXACT_CUE | „Mută-te până când adversarul nu ne mai poate acoperi pe amândoi deodată!" |
| WHAT_TO_OBSERVE | Deplasare laterală fără comandă; cere mingea doar când linia de pasă e vizibil deschisă |
| WHEN_TO_INTERVENE | Tipar repetat de rămânere pe aceeași linie cu purtătorul, la pauza dintre seturi — nu la prima repetiție nereușită |
| WHEN_NOT_TO_INTERVENE | O singură încercare nereușită; deplasare prezentă dar insuficientă ca distanță — se lasă încă o repetiție înainte de a corecta |
| TRANSFER_CHECK | În meci, recunoaște autonom acoperirea unui adversar și se repoziționează fără comanda antrenorului (`match_transfer`) |
| COACH_REFLECTION | Am oferit copilului timp să repete decizia înainte să intervin, sau am corectat la prima încercare nereușită? |

## EX-0002 — Creează opțiunea sub presiune reală

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C01, PED-C07 |
| COACH_COMPETENCY_IDS | COACH-C01, COACH-C06, COACH-C11, COACH-C12 (Progresie/regresie — succesor direct al EX-0001) |
| CHILD_OBJECTIVE | Aplică decizia direcție+distanță pentru a crea un unghi de pasă util sub opoziție activă și continuă |
| COACH_OBJECTIVE | Observă un singur focalizator per set (ex. doar distanța de sprijin), fără evaluare verbală imediată |
| COACH_FOCUS | Actualizarea continuă a deciziei (nu o alegere unică per repetiție) |
| EXACT_CUE | „Mută-te până când adversarul nu ne mai poate acoperi — și fii gata să mai schimbi dacă se mișcă!" |
| WHAT_TO_OBSERVE | Reglarea poziției de sprijin când mingea/adversarul se mută; alegerea unghiului fără comandă |
| WHEN_TO_INTERVENE | La pauza dintre seturi, cu întrebarea „Ce ai văzut chiar înainte să te muți a doua oară?" — niciodată în timpul jocului continuu |
| WHEN_NOT_TO_INTERVENE | Opoziție prea intensă de la început nu justifică revenirea imediată la comenzi verbale — se folosește regresia documentată (adversar semi-pasiv), nu corecția verbală |
| TRANSFER_CHECK | În meci, ajustează continuu poziția de sprijin pe măsură ce faza de joc evoluează, nu doar la începutul posesiei |
| COACH_REFLECTION | Am numit o cauză (ex. "nu e atent") sau am descris comportamentul exact înainte de a decide dacă intervin? |

## EX-0003 — Primește gata să continui

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C03 (Comunică adecvat vârstei — indiciu extern, nu instrucție tehnică internă) |
| COACH_COMPETENCY_IDS | COACH-C06 (Cueing), COACH-C11 (Predarea percepției și deciziei) |
| CHILD_OBJECTIVE | Folosește orientarea corporală la recepție pentru a păstra o acțiune posibilă imediat după ce primește mingea |
| COACH_OBJECTIVE | Verifică scanarea vizibilă înainte de recepție, prin observare directă, nu prin „ai înțeles?" |
| COACH_FOCUS | Indiciu extern (conul colorat) — niciodată instrucție tehnică internă despre poziția piciorului |
| EXACT_CUE | „Uită-te la conul colorat înainte să primești, și primește-o spre acolo." |
| WHAT_TO_OBSERVE | Scanarea vizibilă a conului înainte de recepție; prima atingere păstrează mingea într-o zonă utilă |
| WHEN_TO_INTERVENE | Corp închis la recepție repetat — demonstrație scurtă din perspectiva jucătorului, fără explicație tehnică lungă |
| WHEN_NOT_TO_INTERVENE | Nu se prescrie un unghi exact al piciorului („45 de grade") — nicio tehnică unică de recepție nu e validată de cercetare ca superioară |
| TRANSFER_CHECK | În meci, scanează înainte de a primi și orientează recepția pentru a continua imediat, fără pauză de reorientare |
| COACH_REFLECTION | Am oferit un indiciu extern (con, spațiu) sau am prescris o poziție tehnică exactă a corpului? |

## EX-0004 — Sprijin cu doi coechipieri

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C01, PED-C10 (Adaptează la diferențe individuale — complexitate crescută per copil) |
| COACH_COMPETENCY_IDS | COACH-C01, COACH-C03 (Selecția intervenției — întrebare, nu corecție directă), COACH-C11 |
| CHILD_OBJECTIVE | Coordonează două poziții de sprijin diferite astfel încât un adversar să nu poată acoperi ambele simultan |
| COACH_OBJECTIVE | La tipar repetat de grupare în aceeași zonă, oprește scurt și pune întrebarea ghidată — nu corectează direct poziția |
| COACH_FOCUS | Coordonarea IMPLICITĂ între doi coechipieri, nu doar decizia individuală |
| EXACT_CUE | „Dacă coechipierul tău e deja într-o zonă bună, găsește-ți propria zonă — nu vă adunați amândoi în același loc!" |
| WHAT_TO_OBSERVE | Cei doi jucători de sprijin se diferențiază spațial; purtătorul alege pe baza presiunii reale, nu dintr-un tipar fix |
| WHEN_TO_INTERVENE | Tipar repetat (nu prima apariție) de grupare în aceeași zonă — oprire scurtă + întrebare ghidată |
| WHEN_NOT_TO_INTERVENE | Prima apariție a grupării — se lasă comportamentul să reapară sau nu înainte de a opri jocul |
| TRANSFER_CHECK | În meciul 7v7, mai mulți jucători fără minge se coordonează implicit pentru opțiuni distincte |
| COACH_REFLECTION | Am corectat direct poziția sau am pus o întrebare care lasă copiii să găsească singuri soluția? |

## EX-0005 — Transferul în joc mic

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C07 (autonomie completă, fără comandă de pe margine), PED-C06 (răspuns la eroare — „eroarea rămâne informație, nu verdict") |
| COACH_COMPETENCY_IDS | COACH-C01, COACH-C03 (non-intervenție deliberată), COACH-C14 (Verificarea transferului), COACH-C15 (Evaluare) |
| CHILD_OBJECTIVE | Aplică lanțul decizional exersat izolat (EX-0001-EX-0004) într-un joc reprezentativ complet, fără constrângeri artificiale |
| COACH_OBJECTIVE | Observă tăcut, cu un singur focalizator per repriză, dacă principiul exersat apare autonom |
| COACH_FOCUS | Non-intervenție verbală în timpul fazei active — testul de transfer, nu de performanță în sarcină izolată |
| EXACT_CUE | „Jucați ca de obicei — folosiți ce ați exersat dacă vă ajută!" |
| WHAT_TO_OBSERVE | Apariția autonomă a unui unghi de sprijin util sau a recepției orientate, fără comandă de pe margine |
| WHEN_TO_INTERVENE | Doar pentru siguranță fizică sau comportament nesportiv — niciodată pentru a corecta tactic în timpul fazei active |
| WHEN_NOT_TO_INTERVENE | Comportamentul țintă nu apare deloc — se notează ca informație validă (nu eșec), nu se întrerupe jocul pentru a preda din nou |
| TRANSFER_CHECK | Acest exercițiu ESTE testul de transfer; transferul complet în meci real rămâne neconfirmat până la pilotare reală pe teren (`FIELD_INPUT_REQUIRED`) |
| COACH_REFLECTION | Am rezistat impulsului de a interveni tactic în timpul jocului liber? Ce am notat ca informație, nu ca verdict, dacă transferul nu a apărut? |

## SES-0001 — Sprijinul și unghiul de pasă — introducere

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C01, PED-C03, PED-C07 |
| COACH_COMPETENCY_IDS | COACH-C01, COACH-C06, COACH-C10 (Organizare de grup — stații paralele), COACH-C11, COACH-C16 (Planificarea ședinței) |
| CHILD_OBJECTIVE | Introduce lanțul decizional de bază (umbră defensivă → decizie sub opoziție → orientare la recepție) pe EX-0001→EX-0002→EX-0003 |
| COACH_OBJECTIVE | Limitează deliberat la 3 concepte noi per ședință, pentru a nu supra-încărca vârsta U11 (`session_rationale`) |
| COACH_FOCUS | Un singur focalizator de observație per segment, progresiv: deplasare → repoziționare dinamică → scanare la recepție |
| EXACT_CUE | Variază pe segment — vezi tabelul EX-0001/0002/0003 de mai sus |
| WHAT_TO_OBSERVE | Vezi coloanele WHAT_TO_OBSERVE ale EX-0001/0002/0003; la nivel de ședință: numărul de concepte noi introduse rămâne 3, deliberat limitat |
| WHEN_TO_INTERVENE | Rutina de siguranță — intervenție imediată doar la risc fizic real; segmentele tehnice — la tipar repetat, nu la prima încercare |
| WHEN_NOT_TO_INTERVENE | Dacă un exercițiu eșuează complet, se tratează ca informație despre exercițiu, nu despre copii — se scurtează segmentul, nu se forțează repetiții suplimentare |
| TRANSFER_CHECK | Reflecția de închidere leagă explicit exercițiile de situația din meci; jocul liber final nu introduce constrângeri noi |
| COACH_REFLECTION | Am respectat limita de 3 concepte noi, sau am adăugat corecții suplimentare neplanificate pe parcurs? |

## SES-0002 — Sprijinul și unghiul de pasă — coordonare și transfer

| Câmp | Valoare |
|---|---|
| PEDAGOG_COMPETENCY_IDS | PED-C01, PED-C07, PED-C10 |
| COACH_COMPETENCY_IDS | COACH-C01, COACH-C03, COACH-C10, COACH-C14, COACH-C15, COACH-C16 |
| CHILD_OBJECTIVE | Consolidează decizia de bază printr-o reamintire scurtă, apoi coordonează doi jucători de sprijin (EX-0004) și transferă în joc reprezentativ (EX-0005) |
| COACH_OBJECTIVE | Verifică dacă cel puțin un comportament exersat izolat apare autonom în jocul liber final — testul central al ședinței |
| COACH_FOCUS | Non-intervenție verbală completă în timpul EX-0005 — observare tăcută, un singur focalizator per repriză |
| EXACT_CUE | Variază pe segment — vezi tabelul EX-0004/0005 de mai sus |
| WHAT_TO_OBSERVE | Diferențierea spațială a celor doi jucători de sprijin (EX-0004); apariția autonomă a comportamentului țintă (EX-0005) |
| WHEN_TO_INTERVENE | Tipar repetat de grupare (EX-0004); doar siguranță fizică sau comportament nesportiv (EX-0005) |
| WHEN_NOT_TO_INTERVENE | Transferul nu apare deloc în EX-0005 — se notează ca informație pentru evaluare (`ASM-0001`), sesiunea nu se anulează, nu se reia predarea în mijlocul jocului liber |
| TRANSFER_CHECK | Reflecția finală leagă explicit jocul liber de EX-0004/EX-0001-0003; separarea în două ședințe (nu una de ~120 min) e alegere practică ManualFC, nu rezultat de cercetare despre intervalul optim |
| COACH_REFLECTION | Am rezistat să intervin tactic în timpul EX-0005? Am notat corect dacă transferul a apărut sau nu, ca informație, nu ca verdict despre copii? |

## Notă de guvernanță

Niciun exercițiu/ședință V1 (EX-0001–EX-0005, SES-0001–SES-0002) nu devine invalid prin acest document — este strict aditiv, o mapare de documentare peste date deja existente. Migrarea efectivă a schemei (adăugarea câmpurilor `PEDAGOG_COMPETENCY_IDS`/`COACH_COMPETENCY_IDS`/etc. ca proprietăți JSON reale) rămâne explicit amânată pentru o fază viitoare de migrare Gold Standard V2, conform regulii §51 ("Do NOT migrate runtime yet").
