# Instrucțiuni Codex — Platformă web pedagogică U11

## Misiune

Construiește integral o platformă web profesională, documentată, vizuală și interactivă pentru formarea antrenorului-pedagog care lucrează cu copii de aproximativ 10–11 ani. Copiii născuți în 2015 și 2016 sunt tratați ca o singură categorie. Nu separa curriculumul după anul nașterii; adaptează individual după nivel, maturizare și experiență.

Principiul canonic este: antrenorul trebuie format mai întâi ca pedagog și apoi ca antrenor. Site-ul static este livrabilul principal; PDF-urile și resursele editabile sunt derivate secundare.

Manualul trebuie să îl formeze întâi pe antrenor, apoi să îl ajute să îi învețe pe copii. Orice indicație adresată copiilor trebuie să explice și ce se află în spatele ei: problema rezolvată, informația observată, decizia urmărită, mecanismul tactic, cognitiv, psihologic, tehnic și social, riscurile și verificarea înțelegerii.

## Documente obligatorii

Înainte de orice task relevant, citește:

1. `CODEX.md` — constituția completă;
2. `MASTER_EXECUTION_PROMPT.md` — misiunea și livrabilele;
3. `PLANS.md` — regulile ExecPlan;
4. documentele aplicabile din `docs/`;
5. `TASK_REGISTRY.json`, `PROJECT_STATUS.md` și ultimul raport de task, dacă există.

Instrucțiunile din acest fișier au prioritate. `CODEX.md` și documentele din `docs/` dezvoltă aceste reguli, nu le înlocuiesc.

## ExecPlans

Pentru orice fază, volum, capitol important, sistem interactiv, build sau refactor semnificativ, creează și menține un ExecPlan conform `PLANS.md`. Planul este un document viu: actualizează progresul, descoperirile, deciziile și rezultatele verificărilor.

## Mod de lucru

- Lucrează din registrul persistent de taskuri.
- Selectează un task `READY` cu dependențele închise.
- Execută un singur task principal bine delimitat.
- Creează livrabilele declarate, rulează validările și repară problemele.
- Marchează taskul `DONE` numai cu dovezi verificabile.
- Actualizează după fiecare task: `TASK_REGISTRY.json`, `TASK_HISTORY.jsonl`, `PROJECT_STATUS.md`, `DECISIONS.md` și raportul taskului.
- Nu cere utilizatorului să aleagă următorul volum. Ordinea rezultă din dependențe.
- Nu declara proiectul complet cât timp există conținut lipsă, placeholder-e, linkuri false, butoane nefuncționale sau validări neexecutate.

## Cercetare și factualitate

- Folosește prioritar surse primare și instituționale: FIFA, UEFA, FRF, federații, documente oficiale, articole academice și standarde de safeguarding.
- Pentru informații actualizabile, verifică versiunea și data.
- Înregistrează sursele și afirmațiile susținute în registrul de cercetare.
- Separă explicit: fapt, recomandare oficială, rezultat de studiu, practică de academie, opinie profesională și sinteză metodologică.
- Nu inventa surse, autori, citate, reguli, dimensiuni „oficiale” sau rezultate.
- Dacă accesul la internet lipsește, marchează taskul de cercetare `BLOCKED`; nu completa din presupuneri.

## Pedagogie obligatorie

- Tactica începe cu percepția, orientarea și decizia, nu cu memorarea unei formații.
- Predă probleme ale jocului și principii transferabile, nu coregrafii rigide.
- Folosește situații cu minge, adversar, direcție, obiectiv și alegere.
- Preferă progresii de la simplu la complex și de la grupuri mici la jocul complet.
- Protejează autonomia, creativitatea, încrederea și dreptul copilului de a greși.
- Evită joystick coaching, umilirea, sarcasmul, etichetarea, specializarea prematură și selecția bazată exclusiv pe avantaj fizic.
- Orice exercițiu trebuie să precizeze ce observă copilul, ce decide, ce comportament urmărește antrenorul și unde reapare situația în meci.

## Regula „ce le spun și de ce”

Pentru fiecare mesaj, sarcină, întrebare, regulă, constrângere, feedback sau corecție adresată copiilor, include minimum:

- formularea exactă pentru copil;
- sensul profesional pentru antrenor;
- motivul alegerii mesajului;
- problema pe care o rezolvă;
- informațiile pe care copilul trebuie să le observe;
- decizia pe care trebuie să o învețe;
- comportamentele observabile;
- justificarea tactică, perceptivă, cognitivă, psihologică, tehnică și socială;
- adecvarea la vârstă;
- formulările de evitat și motivul;
- riscurile de interpretare;
- modul de verificare a înțelegerii;
- intervenția dacă mesajul nu funcționează;
- transferul în joc.

Niciun principiu, exercițiu, script sau plan de ședință nu trece validarea fără această fundamentare.

## Stil editorial

Scrie în română naturală, profesionistă și precisă. Aplică `docs/EDITORIAL_STYLE_GUIDE.md`.

Obligatoriu:

- pornește de la situații reale de teren și exemple concrete;
- variază ritmul frazelor în mod firesc, fără artificii;
- formulează judecăți profesionale motivate;
- păstrează nuanțele și limitele dovezilor;
- evită generalitățile, clișeele, repetițiile și introducerile ceremoniale;
- nu repeta aceeași structură de paragraf mecanic;
- nu folosi liste doar pentru a umple spațiul;
- nu inventa anecdote, reacții sau experiențe personale;
- supune fiecare capitol unei revizii editoriale separate de generare.

Nu optimiza textul pentru a „păcăli” detectoare de AI. Acestea sunt nesigure. Optimizează pentru adevăr, specificitate, utilitate, voce editorială coerentă și revizie umană reală.

## Standard vizual și interactiv

Aplică `docs/VISUAL_INTERACTIVE_STANDARD.md`.

- Diagrame originale în SVG, cu legendă unitară.
- Fiecare exercițiu afișează dimensiunile, zonele, porțile, distanțele, spațiul de siguranță, direcția atacului, mingea și rolurile.
- Explică de ce este aleasă dimensiunea și cum se ajustează.
- Animațiile dinamice includ control pas cu pas și alternativă statică pentru PDF.
- Nu comunica informația doar prin culoare.
- Manualul trebuie să fie lizibil pe mobil, desktop și la tipar.

## Calitate și testare

Aplică `docs/QUALITY_GATES.md`.

- Rulează validatoarele după fiecare task relevant.
- Testează build-ul web, linkurile, datele, SVG-urile, animațiile, accesibilitatea și PDF-ul.
- Pentru schimbări UI, verifică vizual în browser, nu doar prin teste unitare.
- Orice regresie trebuie reparată înainte de `DONE`.
- Un task fără raport și fără output existent rămâne incomplet.

## Git și siguranța modificărilor

- Inspectează starea Git înainte de lucru.
- Nu șterge sau suprascrie modificări necunoscute.
- Nu utiliza resetări distructive fără solicitare explicită.
- Fă schimbări focalizate și ușor de revizuit.
- Commiturile trebuie să corespundă unui task validat și să includă ID-ul taskului în mesaj.
- Nu publica repository-ul și nu împinge modificări la distanță fără acord explicit.

## Condiția de finalizare

Proiectul este final numai când toate criteriile din `MASTER_EXECUTION_PROMPT.md` și `docs/QUALITY_GATES.md` sunt îndeplinite, build-ul web și PDF-ul sunt verificate, arhiva finală a fost dezarhivată și retestată, iar raportul final are verdict `PASS`.
