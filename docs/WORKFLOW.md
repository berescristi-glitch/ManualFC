# Flux de lucru recomandat în Codex

## 1. Prima sesiune

Trimite `START_CODEX_PROMPT.md`. Scopul este inițializarea, nu redactarea.

## 2. Mărimea taskurilor

Pentru calitate, folosește taskuri delimitate:

- un capitol coerent;
- 3–5 exerciții;
- 1–2 ședințe;
- un sistem tehnic;
- un audit;
- un lot de reparații strâns legate.

Un volum întreg într-un singur task este permis doar dacă este scurt și poate fi revizuit riguros. În mod normal, volumele se împart pe capitole.

## 3. Ciclul recomandat

Pentru fiecare livrabil:

1. task de cercetare/planificare, dacă este necesar;
2. task de producție;
3. task de audit independent într-un chat nou;
4. task de reparare;
5. task de aprobare și integrare.

Nu folosi același context pentru autor și auditor când poți deschide un chat nou.

## 4. Ordinea proiectului

1. bootstrap și arhitectură;
2. cercetare transversală;
3. sistem de conținut, vizual și validare;
4. Volumele I–IV;
5. curriculumul din Volumul V;
6. exercițiile și ședințele derivate din fundamente;
7. Volumele VIII–X;
8. integrare, editare și build;
9. audit final.

Biblioteca de exerciții nu trebuie să fie inventată înaintea principiilor și a criteriilor pedagogice.

## 5. Ce mesaj se trimite

Folosește șabloanele din `TASK_PROMPTS.md`. Pentru majoritatea sesiunilor este suficient promptul de continuare normală sau promptul cu un `TASK-ID` precis.

## 6. Când Codex se oprește din cauza limitei sau contextului

Nu cere să își „amintească” conversația. Deschide repository-ul, pornește un chat nou și trimite:

```text
Citește AGENTS.md și starea persistentă. Reia proiectul de la taskul IN_PROGRESS sau următorul READY. Verifică întâi integritatea outputurilor și istoricul. Continuă conform ExecPlan-ului și nu presupune că pașii anteriori au reușit fără dovezi.
```

## 7. Commituri

Recomandat:

- un commit după fiecare task validat sau grup foarte strâns de reparații;
- mesaj: `<TASK-ID>: descriere concisă`;
- nu amesteca un capitol, o schimbare de framework și un audit în același commit.

## 8. Verificarea utilizatorului

Utilizatorul nu trebuie să aprobe fiecare propoziție. Sunt utile puncte de control după:

- arhitectură și prototipul vizual;
- finalizarea fiecărui volum;
- primele 5 exerciții și primele 2 ședințe;
- primul PDF reprezentativ;
- release candidate.

Dacă utilizatorul nu oferă feedback, proiectul continuă pe baza standardelor canonice.
