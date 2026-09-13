# TASK-0101 — Validator JSON Schema și referințe încrucișate

## 1. Titlu și scop

Construirea unui validator central, determinist și fail-closed pentru datele structurate, referințele, activele și starea persistentă a Manualului U11.

## 2. Context pentru un cititor nou

TASK-0001 a creat schemele inițiale și registrele goale. TASK-0002 a fixat baseline-ul Git. Schemele din `schemas/` sunt sursa canonică. `scripts/validate_project.py` verifică bootstrapul, dar nu aplică integral JSON Schema și nu oferă diagnostice stabile pe fișier și cale JSON.

## 3. Rezultatul verificabil

La final există un CLI care validează întregul repository, un fișier sau un tip, produce output uman/JSON, aplică mod strict/debug, încarcă toate schemele, construiește indexul ID-urilor și verifică relațiile disponibile. Fixture-urile invalide sunt respinse cu codurile așteptate.

## 4. Domeniu și non-obiective

Intră: scheme necesare validatorului, motorul Python unic, diagnostice, referințe, euristici pedagogice prudente, teste, documentație și integrarea în validatorul general.

Nu intră: scrierea conținutului manualului, instalarea Astro, adevărul pedagogic automat, detector AI, repararea automată a datelor sau TASK-0102.

## 5. Fișiere și module afectate

`scripts/validate_content.py`, `scripts/validation/`, `schemas/`, `tests/fixtures/validation/`, `tests/test_content_validator.py`, `requirements-dev.txt`, `docs/architecture/VALIDATION_SYSTEM.md`, starea persistentă și raportul TASK-0101.

## 6. Cercetare necesară

Nu este necesară cercetare factuală despre fotbal. Implementarea folosește JSON Schema Draft 2020-12 prin pachetul `jsonschema`, fixat în dependențele de dezvoltare. Validarea locală nu necesită internet după instalare.

## 7. Model pedagogic

Validatorul cere fundamentarea mesajului și verifică structura, valori ne-goale, placeholder-e, densitate explicativă minimă și duplicare evidentă. Aceste euristici semnalează lipsa mecanismului; nu pretind să decidă automat calitatea pedagogică finală.

## 8. Design vizual și interactiv

Manifestele vizuale sunt verificate contra schemei, fișierele trebuie să rămână în repository, iar animațiile dinamice trebuie să indice cadre PDF. Validatorul nu randă SVG-ul sau animația.

## 9. Pași de implementare

1. Definește catalogul central de coduri și diagnosticul serializabil.
2. Încarcă și verifică toate schemele Draft 2020-12.
3. Descoperă documentele după `$schema`, registru sau director canonic.
4. Validează JSON, formate, texte goale și placeholder-e.
5. Construiește indexul tipizat de ID-uri și aplică relațiile.
6. Aplică integritatea taskurilor, istoricului, rapoartelor și outputurilor.
7. Adaugă modurile CLI și sortarea stabilă.
8. Testează cele 25 de clase minime și integrarea repository-ului.
9. Actualizează documentația și starea, apoi validează și comite.

## 10. Validare și acceptare

- `python scripts/validate_content.py`
- `python scripts/validate_content.py --format json`
- `python scripts/validate_content.py --file config/project.json`
- `python scripts/validate_content.py --type source`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/validate_project.py`
- `git diff --check`

Toate comenzile trebuie să aibă rezultat determinist și cod de ieșire corect. Repository-ul curent trebuie să treacă fără avertismente neexplicate.

## 11. Progres

- [x] 2026-07-30T02:00:00+03:00 — preflight, corpus, scheme și rapoarte citite; HEAD curat confirmat.
- [x] 2026-07-30T02:10:00+03:00 — decizia pentru validatorul Python unic și JSON Schema canonic a fost fixată.
- [x] 2026-07-30T02:25:00+03:00 — motorul și schemele sunt implementate.
- [x] 2026-07-30T02:40:00+03:00 — fixture-urile și testele trec.
- [x] 2026-07-30T02:55:00+03:00 — integrarea, documentația și starea persistentă sunt complete.
- [x] 2026-07-30T03:00:00+03:00 — commitul focalizat este pregătit; verificarea hashului și a worktree-ului se face imediat după creare.

## 12. Descoperiri și surprize

- Mediul nu avea pachetul `jsonschema`; a fost instalată versiunea 4.26.0, compatibilă cu Python 3.14.
- Stackul Node/Astro este planificat pentru TASK-0401, deci un validator TypeScript acum ar introduce prematur două bootstrapuri.

## 13. Jurnal de decizii

- 2026-07-30 — Python este runtime-ul canonic al validatorului de conținut în această fază; JSON Schema rămâne sursa regulilor structurale. Motiv: bootstrapul existent, rulare locală rapidă și evitarea instalării premature a aplicației.
- 2026-07-30 — Erorile de conținut nu produc stack trace decât cu `--debug`.
- 2026-07-30 — Schemele viitoare sunt introduse acum pentru tipurile cerute, fără migrare de date deoarece nu există încă instanțe.

## 14. Rezultat și retrospectivă

Validatorul central este funcțional, determinist și integrat. Repository-ul real trece în mod normal și strict fără diagnostice. Cele 25 de clase de fixture demonstrează acceptarea controlată și respingerea fail-closed. Limitările rămân explicit la validările ce necesită audit uman sau randare vizuală.
