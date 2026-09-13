# TASK-2705 — Group Configurator

## Scop și rezultat verificabil

Răspunde determinist la „Am X copii, cum organizez exercițiul?” pentru fiecare exercițiu Gold Standard, la efective de 8–18 copii și 1 sau 2 antrenori, derivat exclusiv din datele canonice ale exercițiilor — fără logistică inventată sau duplicată față de sursa de adevăr existentă.

## Progres

- [x] `schemas/exercise.schema.json` extins aditiv cu `equipment_items` (cantități structurate, extrase din proza `equipment` existentă, nu inventate).
- [x] Cele 5 fișiere de exercițiu (`data/exercises/*.json`) actualizate cu `equipment_items`.
- [x] `content-bridge.ts` extins (`GoldStandardEquipmentItem`, fail-closed pe `equipment_items`).
- [x] `app/src/lib/group-configurator.ts` — motor determinist (grupe, activi/așteptare, suprafață, echipament, poziționare antrenor), cu heuristicile etichetate explicit `PRACTICE_HEURISTIC`.
- [x] `app/src/pages/gold-standard/configurator.astro` — pagină publică, legată din `/gold-standard`.
- [x] Verificat browser la 1440/768/390 (dev preview): 0 erori consolă, 0 overflow orizontal, tabelul cu scroll propriu.
- [x] Validare locală completă: `validate_content.py --strict`, `validate_project.py`, `astro check`, `npm run build`.

## Limită

Nu acoperă contingențele operaționale ale ședințelor SES-0001/SES-0002 (întârziați, spațiu redus, material insuficient) — acela este scopul explicit al `TASK-2706`. Configuratorul răspunde la nivel de exercițiu individual, nu la nivel de ședință completă.
