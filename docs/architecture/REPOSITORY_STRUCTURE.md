# Structura repository-ului

| Cale | Responsabilitate | Sursă sau output |
|---|---|---|
| `content/` | Capitole MDX și manifestul editorial | sursă |
| `data/` | Principii, exerciții, ședințe, planuri, evaluări, scripturi, cazuri și glosar | sursă |
| `research/` | Surse, afirmații, citări, dosare și jurnal de căutare | sursă |
| `schemas/` | Contracte JSON Schema | sursă |
| `assets/diagrams/` | SVG-uri finale | sursă |
| `assets/diagram-sequences/` | Cadre statice pentru PDF | sursă |
| `assets/animations/` | Datele animațiilor | sursă |
| `assets/editable/` | Surse vizuale editabile | sursă |
| `assets/manifests/` | Legătura dintre entitate și active | sursă |
| `app/` | Shell-ul Astro și componentele interactive | sursă |
| `print/` | CSS și pipeline PDF | sursă |
| `templates/` | Șabloane structurale, fără conținut fictiv | sursă |
| `tests/` | Teste de contract, integrare, browser și livrare | sursă |
| `plans/` | ExecPlans vii | stare persistentă |
| `reports/` | Dovezi de task, audit și build | stare persistentă |
| `dist/` | Web, PDF, editabile și arhivă generate | output regenerabil |

Directoarele de conținut se materializează când taskul aferent este executat. Nu se adaugă fișiere goale sau exemple doar pentru a simula progresul.
