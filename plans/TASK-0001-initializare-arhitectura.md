# TASK-0001 — Inițializare, arhitectură și registru executabil

## 1. Titlu și scop

Rezultatul acestui plan este o fundație verificabilă pentru manual: arhitectură decisă, contracte canonice de date, structură persistentă, registru granular de taskuri și validare locală reproductibilă. Taskul nu produce conținut editorial pentru volume.

## 2. Context pentru un cititor nou

Documentele canonice sunt `AGENTS.md`, `CODEX.md`, `MASTER_EXECUTION_PROMPT.md`, `PLANS.md` și standardele din `docs/`. Registrul inițial conținea 22 de faze reprezentate ca taskuri mari. Schemele existente acopereau taskurile, principiile, exercițiile și ședințele, dar nu registrele de cercetare, mesajele către copil sau activele vizuale.

Categoria este unică: copii de aproximativ 10–11 ani, grupele 2015 și 2016 tratate împreună. Diferențierea viitoare va fi individuală.

## 3. Rezultatul verificabil

La încheiere trebuie să existe:

- un ADR pentru stack și fluxul data-driven;
- contracte JSON Schema pentru surse, afirmații, citări, fundamentarea mesajelor și active vizuale;
- registre canonice valide și inițial goale pentru cercetare;
- documentație pentru arhitectura datelor, build, testare și structură;
- un registru granular cu dependențe, ponderi, outputuri și comenzi de validare;
- directoare persistente fără conținut demonstrativ;
- un validator care verifică schemele, graful de dependențe, stările și dovezile taskurilor;
- fișierele de stare și raportul taskului actualizate.

## 4. Domeniu și non-obiective

Intră în task: inspectarea mediului, deciziile arhitecturale inițiale, contractele de date, structura, registrul și validarea bootstrapului.

Nu intră: redactarea volumelor, exemple fictive, exerciții demonstrative, instalarea frameworkului web, cercetare factuală de fond, build web/PDF sau inițializarea Git fără autorizare explicită.

## 5. Fișiere și module afectate

Se creează sau se modifică în `plans/`, `docs/architecture/`, `schemas/`, `research/`, `config/`, `scripts/`, `reports/task-reports/`, directoarele de produs și fișierele persistente din rădăcină.

## 6. Cercetare necesară

TASK-0001 nu formulează afirmații despre dezvoltarea copiilor sau metodologia fotbalistică. Nu necesită cercetare web. Definește doar mecanismul prin care taskurile ulterioare vor înregistra surse, afirmații, niveluri de încredere, limite și utilizări.

## 7. Model pedagogic

Contractul `message-foundation` va separa problema jocului, informația observată, interpretarea, decizia, execuția și rezultatul. Va cere justificări tactice, perceptive, cognitive, psihologice, tehnice și sociale, adecvare la vârstă, formulări de evitat, riscuri, verificarea înțelegerii, intervenția alternativă și transferul în meci.

## 8. Design vizual și interactiv

Se definește un manifest pentru SVG, storyboard/animație și cadre PDF. Identitatea vizuală și motorul de randare vor fi implementate în taskuri separate. Niciun activ demonstrativ nu este produs aici.

## 9. Pași de implementare

1. Citește integral corpusul obligatoriu și inventariază fișierele, Git și toolchain-ul.
2. Înregistrează arhitectura aleasă și alternativele într-un ADR.
3. Definește contractele de date și registrele canonice inițiale.
4. Descompune fazele în unități de cercetare, producție, audit, reparare și integrare, cu loturi normale de un capitol, 3–5 exerciții sau 1–2 ședințe.
5. Extinde validatorul pentru integritate structurală, JSON Schema locală, graf, ponderi, outputuri și coerența stărilor.
6. Rulează validările, repară erorile și consemnează comenzile și rezultatele.
7. Actualizează planul, registrul, istoricul, statusul, deciziile și raportul.

## 10. Validare și acceptare

Comenzi:

- `python scripts/validate_project.py`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/generate_task_registry.py --check`

Criterii:

- toate comenzile ies cu cod 0;
- toate taskurile respectă schema, au ID unic, dependențe existente și graf aciclic;
- suma ponderilor este 100;
- TASK-0001 are toate outputurile existente înainte de `DONE`;
- următorul task eligibil este `READY`;
- nu există fișiere de conținut demonstrativ.

## 11. Progres

- [x] 2026-07-30T00:00:00+03:00 — corpusul obligatoriu și skillul proiectului au fost citite integral.
- [x] 2026-07-30T00:10:00+03:00 — mediul și inventarul au fost inspectate; Python 3.14, Node 24, npm 11, Git 2.54 și ripgrep 15 sunt disponibile.
- [x] 2026-07-30T00:25:00+03:00 — contractele și documentația arhitecturală au fost create.
- [x] 2026-07-30T00:35:00+03:00 — registrul granular și structura persistentă au fost create.
- [x] 2026-07-30T00:43:00+03:00 — validările au trecut.
- [x] 2026-07-30T00:45:00+03:00 — starea persistentă și raportul au fost finalizate.

## 12. Descoperiri și surprize

- Directorul de lucru nu conține `.git`; comenzile `git status`, `git branch` și `git log` nu pot rula. Bootstrapul existent ar inițializa Git, dar această acțiune nu este presupusă automat.
- Afișarea PowerShell folosește o codare care redă diacriticele UTF-8 ca mojibake în terminal; Python citește fișierele explicit ca UTF-8. Validatorul trebuie să opereze pe UTF-8, nu pe redarea consolei.
- Validatorul inițial verifică doar câteva invariabile și nu aplică JSON Schema.
- Prima rulare a validatorului extins a ajuns la raportare, dar `stdout` CP1252 a produs `UnicodeEncodeError` pentru diacritice. Ieșirea a fost configurată explicit UTF-8, iar suita a fost rerulată integral.

## 13. Jurnal de decizii

- 2026-07-30 — Se păstrează o sursă de adevăr data-driven, cu Markdown/MDX pentru capitole și JSON validat pentru entități. Motiv: separă conținutul de UI și permite web, PDF și audit din aceleași date.
- 2026-07-30 — Stackul țintă este Astro + TypeScript, cu componente interactive izolate și Playwright pentru verificare. Alternative analizate: Next.js și generator propriu. Astro favorizează exportul static offline și reduce JavaScript-ul implicit.
- 2026-07-30 — Registrul va include ponderi explicite cu sumă 100, astfel încât progresul să nu fie distorsionat de numărul mare de taskuri mici.
- 2026-07-30 — Git nu este inițializat în acest task fără autorizare explicită; limita este raportată și devine task separat.

## 14. Rezultat și retrospectivă

Fundația observabilă a fost creată fără conținut demonstrativ. Registrul are 176 de taskuri și acoperă explicit pragurile cantitative. Cele trei validări declarate au trecut. Stackul nu este încă instalat, iar validarea JSON Schema completă rămâne deliberat în TASK-0101. Git lipsește și este delimitat în TASK-0002. TASK-0001 îndeplinește criteriile și poate fi marcat `DONE`.
