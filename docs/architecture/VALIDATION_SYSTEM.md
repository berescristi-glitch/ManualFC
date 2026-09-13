# Sistemul canonic de validare

## Rol și sursă de adevăr

`scripts/validate_content.py` este singurul motor canonic pentru date structurate și referințe. Schemele din `schemas/` sunt sursa structurală; motorul adaugă regulile globale care nu se exprimă suficient prin JSON Schema: indexuri, grafuri, existența fișierelor, starea taskurilor și euristici editoriale sau pedagogice.

Runtime-ul este Python 3.14, cu `jsonschema==4.26.0` fixat în `requirements-dev.txt`. După instalarea dependențelor, validarea este locală și nu accesează internetul. Când aplicația Astro va exista, aceasta va apela aceeași comandă; nu va introduce un al doilea set de reguli.

## Comenzi

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate_content.py
python scripts/validate_content.py --file config/project.json
python scripts/validate_content.py --type exercise
python scripts/validate_content.py --format json
python scripts/validate_content.py --strict
python scripts/validate_content.py --debug
```

`--file` și `--type` sunt mutual exclusive. Căile sunt relative la repository. `--strict` promovează avertismentele la erori. `--debug` adaugă traceback numai pentru defecte interne, nu pentru erori normale de conținut.

## Severități și ordine

- `ERROR`: materialul nu poate fi validat sau publicat; cod de ieșire 1.
- `WARNING`: necesită revizie, dar nu blochează rularea normală; în `--strict` devine `ERROR`.
- `INFO`: context diagnostic fără acțiune obligatorie.

Ordinea este stabilă: severitate, fișier, cale JSON, cod și mesaj. Outputul JSON nu conține timestampuri.

## Diagnostic

```json
{
  "code": "BROKEN_REFERENCE",
  "severity": "ERROR",
  "message": "Referința nu există în indexul canonic.",
  "file": "data/exercises/EX-001.json",
  "json_path": "$.principle_ids[0]",
  "found_value": "PRI-9999",
  "expected": "ID existent de tip principle",
  "related_file": null,
  "suggestion": null
}
```

Valorile lungi sunt trunchiate. Validatorul nu citește variabile de mediu și nu afișează fișiere de secrete.

## Tipuri și descoperire

Documentele sunt asociate schemei prin calea canonică, `$schema` sau prefixul ID-ului. Sunt acoperite proiectul, taskurile, sursele, afirmațiile, citările, principiile, exercițiile, ședințele, mesajele, curriculumul, planurile sezoniere, scripturile, cazurile, evaluările, activele, diagramele, animațiile și manifestele de build/distribuție.

Un JSON fără tip determinabil produce `SCHEMA_NOT_FOUND`. YAML nu este folosit în repository; apariția sa necesită schemă, parser sigur și teste înainte de acceptare.

## Index și relații

Indexul global reține tipul, fișierul și calea fiecărui ID. Sunt verificate relațiile pentru capitole, principii, exerciții, ședințe, curriculum, scripturi, surse, afirmații, active, diagrame și animații. Validările speciale acoperă sursă–afirmație–citare–locație, task–dependență–output–raport–istoric, ciclurile taskurilor, manifest–fișier vizual și animație–storyboard–cadre PDF.

O relație nouă se adaugă în `REFERENCE_FIELDS`, cu fixture valid și invalid. Relațiile complexe primesc o funcție separată.

## Fundamentare pedagogică și text

Pentru principii, exerciții, mesaje și scripturi sunt cerute mesajul copilului, sensul antrenorului, formularea, problema, informația, decizia, comportamentele, justificările tactică/perceptivă/cognitivă/psihologică/tehnică/socială, adecvarea, riscurile, verificarea, răspunsul alternativ și transferul.

Euristicile resping text gol, placeholder, răspunsuri pur generice, justificări foarte scurte și duplicare identică. Verificările editoriale semnalează spații multiple, markup executabil, URL-uri brute, linii goale excesive și indicii prudente de text accidental în engleză. Ele nu certifică adevărul sau calitatea pedagogică; auditul uman rămâne obligatoriu.

## Coduri și extindere

Catalogul stabil este în `scripts/validation/codes.py`. Un cod nou se adaugă acolo, este emis prin `Diagnostic`, documentat și acoperit de un test.

Pentru un tip nou:

1. creează schema Draft 2020-12 în `schemas/`;
2. adaugă tipul în `SCHEMA_TYPES`;
3. definește descoperirea, wrapperul, prefixul și relațiile;
4. creează fixture valid și cel puțin unul invalid;
5. rulează suita completă și validatorul general.

## Securitate, integrare și depanare

Validatorul nu execută datele, refuză symlinkuri, nu urmează căi în afara rădăcinii, limitează fiecare JSON la 5 MiB și nu modifică fișierele. Repararea rămâne task separat.

`scripts/validate_project.py` rulează validatorul canonic și transformă orice eșec în eroare de proiect. Fiecare task cu date structurate rulează comanda completă sau filtrul tipului, apoi validatorul general. Auditul final folosește `--strict`.

Pentru `SCHEMA_INVALID`, rulează cu `--debug`. Pentru `BROKEN_REFERENCE`, verifică tipul și prezența țintei. Pentru `SCHEMA_NOT_FOUND`, definește tipul și schema; nu adăuga excepții locale.
