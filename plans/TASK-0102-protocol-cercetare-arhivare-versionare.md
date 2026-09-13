# TASK-0102 — Protocol operațional de căutare, arhivare și versiuni

## 1. Titlu și scop

Rezultatul este un sistem reproductibil pentru întrebări, căutări, surse, afirmații, citări, drepturi, arhivare, versiuni și reverificare, utilizabil pe întreaga durată a Manualului U11.

## 2. Context pentru un cititor nou

TASK-0101 a introdus validatorul canonic Python și JSON Schema Draft 2020-12. Registrele reale de surse, afirmații și citări sunt goale. TASK-0102 construiește infrastructura, nu cercetarea tematică. Categoria rămâne unică: 10–11 ani, copii născuți în 2015 și 2016 tratați împreună.

## 3. Rezultatul verificabil

Există taxonomie validată, scheme v2, registre reale goale, structură documentată, politici complete, CLI fail-closed, migrare, fixture-uri separate și teste pentru cele 20 de cazuri obligatorii.

## 4. Domeniu și non-obiective

Intră: proceduri, date canonice, înregistrarea sigură, duplicate certe, actualitate, manifest de arhivă, versionare, drepturi și integrarea validatorului.

Nu intră: cercetarea pe volume, redactarea capitolelor, exerciții, aplicația web sau PDF-ul.

## 5. Fișiere și module afectate

`research/`, `schemas/`, `config/research-taxonomy.json`, `scripts/research_tool.py`, `scripts/migrate_research_v1_to_v2.py`, `tests/fixtures/research/`, `tests/test_research_protocol.py`, `docs/research/`, starea persistentă și raportul.

## 6. Cercetare necesară

Nu se formulează concluzii despre fotbal. Fixture-urile sunt sintetice și marcate. Protocolul prioritizează sursele primare, păstrează limitele și interzice confundarea prestigiului cu forța dovezii.

## 7. Model pedagogic

Selecția surselor trebuie să descrie populația reală și relevanța pentru categoria comună 10–11 ani. Lipsa dovezilor directe produce marcaj de extrapolare și audit suplimentar, nu curriculum separat 2015/2016.

## 8. Design vizual și interactiv

Sursele vizuale externe cer autor, proprietar, licență, permisiuni și canale de distribuție. Diagramele proprii sunt marcate ca originale. Niciun activ cu drepturi neclare nu intră în build.

## 9. Pași de implementare

1. Definește taxonomiile și contractele v2.
2. Creează migrarea no-op/compatibilă pentru registrele goale.
3. Implementează CLI-ul fără suprascriere și cu hash SHA-256.
4. Integrează duplicate, versiuni, actualitate, drepturi și arhive în validator.
5. Documentează workflow-ul, rolurile, contradicțiile și citarea exactă.
6. Creează fixture-uri sintetice separate și testele negative.
7. Actualizează starea, validează strict și comite focalizat.

## 10. Validare și acceptare

- `python scripts/research_tool.py --help`
- `python scripts/validate_content.py`
- `python scripts/validate_content.py --strict`
- `python -m unittest discover -s tests -p "test_*.py"`
- `python scripts/validate_project.py`
- `git diff --check`

## 11. Progres

- [x] 2026-07-30T04:00:00+03:00 — lectura și preflight-ul au trecut pe HEAD-ul cerut.
- [x] 2026-07-30T04:35:00+03:00 — Taxonomiile, schemele și migrarea sunt complete.
- [x] 2026-07-30T04:55:00+03:00 — Uneltele și validările sunt complete.
- [x] 2026-07-30T05:05:00+03:00 — Documentația și structura persistentă sunt complete.
- [x] 2026-07-30T05:20:00+03:00 — Fixture-urile și cele 20 de teste obligatorii trec.
- [x] 2026-07-30T05:30:00+03:00 — Starea persistentă este actualizată; auditul și commitul sunt etapa finală.

## 12. Descoperiri și surprize

- Registrele reale sunt goale, deci migrarea v1→v2 poate fi verificată fără risc de pierdere a datelor.
- Snapshoturile trebuie ignorate implicit de Git chiar când sunt permise local; includerea lor cere audit explicit de drepturi și manifest.
- Raportarea duplicatelor după titlu rămâne deliberat neblocantă, pentru a păstra edițiile distincte.

## 13. Jurnal de decizii

- 2026-07-30 — Registrele JSON rămân sursa canonică; jurnalele de căutare sunt JSONL append-only pentru trasabilitate.
- 2026-07-30 — ID-urile sunt alocate numai după validarea candidatului și verificarea duplicatelor certe.
- 2026-07-30 — Fixture-urile folosesc domeniul `.invalid` și nu intră în registrele reale.

## 14. Rezultat și retrospectivă

Protocolul operațional este implementat fără cercetare tematică sau conținut de
manual. Contractele v2 separă sursa, afirmația și citarea exactă; taxonomia este
validabilă, căutările sunt reproductibile, iar arhivele și versiunile sunt
controlate fail-closed. Registrele reale au rămas goale. Suita finală are 31 de
teste, dintre care 20 acoperă explicit cazurile protocolului, inclusiv respingeri.
