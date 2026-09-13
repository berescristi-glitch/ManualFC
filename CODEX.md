# Constituția proiectului — Platformă web pedagogică pentru 10–11 ani

## 1. Scopul proiectului

Livrabilul principal este platforma web statică pentru formarea antrenorului-pedagog. Principiul canonic este că antrenorul trebuie format mai întâi ca pedagog și apoi ca antrenor; PDF-ul și resursele editabile sunt exporturi secundare.

Repository-ul trebuie să producă un manual complet de formare pentru antrenorii care lucrează cu copii de aproximativ 10–11 ani. Cele două grupe, formate din copii născuți în 2015 și 2016, sunt tratate împreună. Manualul nu construiește două curricule paralele și nu presupune că anul nașterii descrie nivelul copilului.

Diferențierea este individuală și se bazează pe:

- nivelul de experiență;
- dezvoltarea tehnică;
- înțelegerea jocului;
- maturizarea fizică;
- încrederea și disponibilitatea de a participa;
- nevoile cognitive, emoționale și sociale;
- ritmul de învățare.

Manualul nu urmărește să transforme copiii în executanți ai unei table tactice. Scopul este dezvoltarea unor jucători care observă, aleg, cooperează, se adaptează și înțeleg motivele propriilor acțiuni.

## 2. Ce trebuie să primească antrenorul

Antrenorul trebuie să afle, pentru fiecare temă:

1. ce reprezintă principiul;
2. de ce contează;
3. ce poate înțelege copilul la această vârstă;
4. cum este tradus principiul în limbaj simplu;
5. ce vede copilul;
6. ce alegere învață;
7. ce execuție susține alegerea;
8. cum este construit exercițiul;
9. de ce sunt folosite acele reguli și dimensiuni;
10. ce observă și când intervine antrenorul;
11. cum verifică transferul în joc;
12. cum adaptează sarcina fără a pierde intenția.

Manualul trebuie să permită antrenorului să argumenteze și să adapteze independent fiecare sarcină, nu doar să o reproducă.

## 3. Principii pedagogice canonice

### 3.1 Percepție–decizie–acțiune

Comportamentul tactic este prezentat ca un ciclu:

`observare → interpretare → alegere → execuție → evaluare → reacție`

Nu separa artificial tehnica de informația care îi dă sens. O pasă corectă tehnic nu este automat o decizie bună; o decizie bună poate avea o execuție imperfectă.

### 3.2 Probleme de joc, nu răspunsuri memorate

Exercițiile trebuie să facă vizibilă o problemă reală: lipsa unui unghi, apărarea centrului, folosirea superiorității, momentul presiunii. Regula sau constrângerea trebuie să amplifice problema, nu să impună o coregrafie.

### 3.3 Autonomie ghidată

Antrenorul creează contextul, observă și intervine precis. Nu dictează fiecare pasă. Întrebările sunt folosite când îl ajută pe copil să caute informația relevantă, nu ca procedeu teatral.

### 3.4 Greșeala are valoare informațională

Corectarea separă:

- ce a observat copilul;
- ce a decis;
- cum a executat;
- ce rezultat a obținut.

Nu pedepsi o decizie curajoasă și justificată doar fiindcă execuția a eșuat.

### 3.5 Dezvoltare înaintea scorului imediat

Meciul este mediu de evaluare și învățare. Victoria nu validează automat metodologia; înfrângerea nu o invalidează. Se urmărește apariția comportamentelor fără comandă de pe margine.

### 3.6 Poziții variate, nu etichete permanente

Copiii trebuie să întâlnească roluri diferite, într-o rotație planificată și inteligibilă. Nu schimba haotic posturile și nu fixa prematur copiii după statură, viteză sau rezultate pe termen scurt.

## 4. Regula de fundamentare a fiecărei sarcini

Orice recomandare adresată copilului trebuie să conțină o casetă sau o secțiune echivalentă cu titlul:

### Ce se află în spatele acestei sarcini?

Aceasta răspunde la:

- Ce îi spun copilului?
- De ce aleg exact această formulare?
- Ce problemă a jocului rezolvă?
- Ce trebuie să observe copilul?
- Ce decizie trebuie să învețe?
- Ce comportament concret aștept?
- Ce principiu tactic dezvoltă?
- Ce proces perceptiv și cognitiv solicită?
- Ce componentă tehnică este necesară?
- Ce efect psihologic și social urmăresc?
- De ce este adecvată vârstei?
- Cum poate fi interpretată greșit?
- Ce formulare ar transforma copilul într-un executant?
- Cum verific înțelegerea?
- Cum simplific dacă nu funcționează?
- Unde reapare în meci?

Această regulă se aplică și dimensiunilor terenului, duratei, ordinii exercițiilor, progresiilor, regresiilor, feedbackului și deciziei de a nu interveni.

## 5. Arhitectura editorială

Parcursul aprofundat păstrează zece volume editoriale, dar platforma web și cele două moduri de utilizare sunt produsul principal:

1. Copilul și procesul de învățare.
2. Fundamentele tactice.
3. Comunicarea și psihologia aplicată.
4. Metodologia practică de predare.
5. Curriculumul și planificarea.
6. Biblioteca de exerciții.
7. Biblioteca de ședințe complete.
8. Meciul și evaluarea.
9. Părinții, disciplina și protecția copilului.
10. Instrumentele digitale și interactive.

Conținutul transversal include:

- glosar;
- bibliografie;
- index tematic;
- fișe editabile;
- studii de caz;
- scripturi de comunicare;
- plan anual și microcicluri;
- reguli de safeguarding;
- instrucțiuni de utilizare a produsului digital.

## 6. Arhitectura tehnică

Produsul trebuie să fie data-driven. Conținutul nu se îngroapă în componente UI dacă poate fi reprezentat prin fișiere structurate.

Preferințe:

- Markdown sau MDX pentru capitole;
- JSON/YAML validate pentru principii, exerciții, ședințe și evaluări;
- SVG pentru terenuri și diagrame;
- TypeScript pentru logica interactivă;
- export static care funcționează fără server;
- print CSS și generare PDF automatizată;
- teste de browser pentru fluxurile principale;
- fără dependență obligatorie de CDN.

Alegerea finală a stackului trebuie justificată într-un Architecture Decision Record și nu se schimbă din comoditate.

## 7. Cercetarea

### 7.1 Ierarhia surselor

1. documente oficiale și regulamente;
2. ghiduri FIFA, UEFA, FRF și federații relevante;
3. articole academice și revizuiri sistematice;
4. cărți și capitole academice;
5. metodologii publice ale academiilor;
6. interviuri sau opinii ale practicienilor, marcate corespunzător.

### 7.2 Registrul afirmațiilor

Pentru fiecare afirmație importantă, păstrează:

- formularea afirmației;
- sursa;
- tipul dovezii;
- anul și data accesării;
- limitele;
- capitolele în care este folosită.

### 7.3 Reguli de citare

- Citările trebuie să susțină afirmația exactă.
- Nu cita o pagină generală pentru o afirmație precisă pe care pagina nu o conține.
- Evită citarea în exces a fiecărei propoziții când un paragraf sintetizează coerent aceeași sursă.
- Bibliografia trebuie să poată fi verificată și exportată.
- Nu transforma manualul într-o colecție de citate; sintetizează și indică limitele.

## 8. Scrierea profesionistă și naturală

Manualul trebuie să sune ca munca unei echipe editoriale competente, nu ca un șablon completat mecanic.

### 8.1 Ce se evită

- introduceri de tipul „În lumea dinamică a fotbalului modern”;
- afirmații grandioase fără conținut;
- repetarea expresiilor „este esențial”, „este important de menționat”, „în concluzie”;
- paragrafe construite permanent în aceeași lungime și sintaxă;
- enumerări perfect simetrice fără motiv;
- rezumarea repetată a aceluiași lucru sub alte titluri;
- tranziții artificiale între secțiuni;
- formulări impersonale care ascund cine recomandă și pe ce bază;
- metafore generice, marketing și superlative;
- fraze care pretind certitudine acolo unde cercetarea este mixtă;
- repetiția mecanică a cuvintelor-cheie;
- exemple fără detalii concrete de teren;
- anecdote inventate pentru „umanizare”.

### 8.2 Ce se urmărește

- o idee clară per paragraf;
- exemple tactice concrete;
- explicații cauzale: „aceasta produce… deoarece…”;
- diferențe între cazuri și excepții;
- verbe directe și subiecte clare;
- fraze scurte lângă fraze mai ample, când logica o cere;
- vocabular profesional tradus imediat în limbaj accesibil;
- observații practice care pot fi verificate la antrenament;
- concluzii locale, nu formule de încheiere automate;
- voce editorială calmă, competentă și lipsită de teatralitate.

### 8.3 Revizia obligatorie

Fiecare capitol trece prin cel puțin patru lecturi distincte:

1. audit factual și al surselor;
2. audit pedagogic;
3. editare structurală și de claritate;
4. editare finală de limbă română.

Generatorul inițial nu își validează singur textul. O revizie într-un task sau context separat trebuie să caute repetiții, formule șablon și lipsă de specificitate.

### 8.4 Detectoarele de AI

Nu există o listă sigură de trăsături care dovedește autorul unui text. Detectoarele produc erori și sunt sensibile la domeniu, lungime și formatare. Proiectul nu urmărește ocolirea lor. Standardul este unul editorial: documentare verificabilă, voce coerentă, explicații concrete, variație naturală și revizie umană.

## 9. Standardul principiilor tactice

Fiecare principiu conține minimum:

- definiția profesională;
- formularea pentru copil;
- fundamentarea completă;
- imagine conceptuală;
- diagramă statică;
- animație, când principiul este dinamic;
- situație simplificată;
- întrebări și feedback;
- greșeli și cauze posibile;
- progresie și regresie;
- evaluare pe niveluri;
- transfer în joc;
- surse.

## 10. Standardul exercițiilor

Fiecare exercițiu trebuie să fie complet conform schemei din `schemas/exercise.schema.json`.

Reguli suplimentare:

- maximum trei comportamente principale;
- nu folosi limitarea atingerilor fără o justificare clară;
- nu adăuga o regulă doar pentru a face exercițiul „mai interesant”;
- precizează când constrângerea trebuie eliminată;
- explică de ce terenul are acele dimensiuni;
- include semnele că terenul este prea mic sau prea mare;
- include spațiu de siguranță;
- arată poziția antrenorului;
- include o variantă de montare rapidă;
- evită cozile și perioadele lungi fără participare;
- descrie rotația și repornirea clar.

## 11. Standardul ședințelor

Fiecare ședință trebuie să includă:

- tema și comportamentele observabile;
- rațiunea ordinii segmentelor;
- plan minut cu minut;
- harta întregii suprafețe;
- timp activ estimat;
- tranziții logistice;
- mesaje și justificări;
- criterii de intervenție;
- adaptări pentru efective diferite;
- joc final cu constrângeri eliminate;
- reflecție scurtă;
- transferul în meci.

Ședința nu este doar suma exercițiilor. Fiecare parte trebuie să pregătească următoarea.

## 12. Standardul vizual

Diagramele sunt originale, unitare și accesibile. Fiecare diagramă include:

- lungime și lățime;
- dimensiunile zonelor;
- distanțe relevante;
- porți și jaloane;
- direcția atacului;
- poziția mingii;
- rolurile jucătorilor;
- trasee diferențiate;
- legendă;
- casetă de utilizare independentă.

Animațiile includ control pas cu pas, iar PDF-ul primește cadre succesive echivalente.

## 13. Taskuri, validări și dovezi

Un task `DONE` trebuie să aibă:

- outputurile declarate;
- fișiere existente;
- validări executate;
- raport în `reports/task-reports/`;
- modificări în registru și istoric;
- probleme rămase declarate;
- commit focalizat, când utilizatorul a autorizat commiturile.

Nu ascunde eșecurile. Dacă un validator nu poate fi rulat, raportul trebuie să spună de ce și să creeze un task de remediere.

## 14. Condiția finală

Manualul este terminat numai când:

- toate cele zece volume sunt complete;
- pragurile cantitative sunt atinse;
- fiecare exercițiu și ședință trece schema și auditul pedagogic;
- manualul web funcționează offline;
- PDF-ul este verificat vizual;
- resursele editabile sunt incluse;
- arhiva finală este testată într-un director curat;
- raportul final are verdict `PASS` și declară onest limitările rămase.
