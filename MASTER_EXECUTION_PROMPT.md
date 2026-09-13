# Master Execution Prompt — Platformă web pedagogică U11

## Misiune

Produsul principal este platforma web pedagogică, nu PDF-ul complet. Ea oferă simultan parcursul „Vreau să învăț” și fluxul „Am nevoie de o soluție acum”.

Construiește, în acest repository, întregul manual multimedia și interactiv de metodologie pentru predarea tacticii în fotbal copiilor de aproximativ 10–11 ani. Copiii născuți în 2015 și 2016 sunt tratați ca o singură categorie. Adaptările sunt individuale, nu două curricule separate.

Lucrează task după task, pe baza unui registru persistent și a ExecPlans. Nu te opri la plan, prototip sau primul volum. Proiectul este final numai după build, testare, audit și împachetare.

## Livrabil principal

Site static Astro, TypeScript strict și MDX, accesibil, rapid, data-driven și utilizabil offline unde este posibil. PDF-ul complet nu mai este produsul principal; exporturile PDF și editabile sunt livrabile secundare derivate.

## Livrabile minime

- 10 volume complete;
- minimum 60 de exerciții validate;
- minimum 36 de ședințe complete;
- minimum 50 de scripturi de comunicare;
- minimum 15 studii de caz;
- plan anual pentru 2 antrenamente + meci și 3 antrenamente + meci;
- instrumente de evaluare individuală și colectivă;
- regulament pentru copii și părinți;
- capitol de safeguarding;
- glosar, bibliografie și index;
- diagramă cu dimensiuni pentru fiecare exercițiu;
- animație pentru situațiile dinamice și cadre echivalente pentru PDF;
- manual web responsiv, accesibil și utilizabil offline;
- PDF complet verificat;
- pachet editabil și sursă;
- arhivă ZIP testată după dezarhivare;
- raport final de audit cu hashuri.

## Volume

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

## Loop-ul de execuție

La fiecare iterație:

1. citește instrucțiunile și starea persistentă;
2. verifică integritatea repository-ului;
3. alege un task `READY` cu dependențele `DONE`;
4. creează sau actualizează ExecPlan-ul;
5. execută un singur livrabil principal;
6. cercetează și înregistrează sursele, dacă taskul o cere;
7. validează outputurile;
8. repară erorile;
9. actualizează registrul, istoricul, statusul și raportul;
10. continuă cu următorul task numai într-o nouă unitate clară de lucru.

## Faze obligatorii

- inițializare și arhitectură;
- cercetare și registrul afirmațiilor;
- sistem editorial, vizual și tehnic;
- volumele I–X;
- integrarea conținutului;
- build web;
- build PDF;
- resurse editabile;
- teste și audituri independente;
- împachetare și verificare într-un director curat.

## Regula fundamentală

Manualul trebuie să răspundă permanent la două întrebări:

1. Ce îi transmit copilului?
2. De ce îi transmit exact acel lucru, în acel moment și în acea formă?

Orice sarcină explică problema, informația observată, decizia, comportamentul, mecanismele tactice, cognitive, psihologice, tehnice și sociale, riscurile și transferul în meci.

## Condiția de oprire

Nu declara proiectul finalizat până când toate taskurile obligatorii sunt `DONE`, toate validările trec, produsele finale există, arhiva este retestată și raportul final are verdict `PASS`.
