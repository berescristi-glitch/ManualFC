# Specificație de Arhitectură: Taxonomie și Arhitectură de Conținut (ManualFC)

**Versiune:** 1.0.0  
**Data:** 2026-08-09  
**Statut:** Canonical / Approved  
**Task de referință:** TASK-0201  

---

## 1. Misiune & Principii de Arhitectură

Taxonomia de conținut a platformei **ManualFC** stabilește structura canonică mașină-citibilă prin care conceptele pedagogice, exercițiile, problemele de joc, recomandările și dovezile sunt identificate, legate și publicate pe web.

Taxonomia deserveste două moduri principale ale produsului:
- **Mode A („Vreau să învăț”)** — Navigare după categorie, concept, principiu, domeniu, progresie și relații pedagogice.
- **Mode B („Am nevoie acum”)** — Navigare rapidă după problema observată, simptom, cauză probabilă, mesaj exact pentru copil, exercițiu de corecție și verificare.

### Principii Fondatoare:
1. **Separare ID / Slug / Titlu:** ID-ul canonic (`principle.scanning-before-receive`) este stabil și decuplat de titlu sau slug. Slug-ul (`orientare-corporala-scanare`) este strictly `lowercase ASCII kebab-case, fără diacritice`.
2. **Clasificarea Entităților (Entity Classes):** `PRIMARY_CONTENT_ENTITY`, `SUPPORTING_ENTITY`, `RESEARCH_ENTITY`, `VISUAL_ENTITY`, `SYSTEM_ENTITY`.
3. **Model Relațional Static-First (Knowledge Graph Light):** Legăturile se rezolvă la build-time prin ID-uri și array-uri de referințe în `app/src/lib/content-bridge.ts`, cu verificare fail-closed.
4. **Discuție Semantică Riguroasă pentru Probleme (Mode B):** Separare obligatorie între `OBSERVATION` (simptom observat), `POSSIBLE_CAUSE` (ipoteză) și `INTERVENTION` (acțiune recomandată).

---

## 2. Categorii Canonice (16 Domenii)

| ID Categorie | Denumire Română | Slug ASCII | Ruta Bază |
| :--- | :--- | :--- | :--- |
| `cat.copilul-10-11` | Copilul de 10–11 ani | `copilul-10-11` | `/copilul-10-11` |
| `cat.antrenorul-pedagog` | Antrenorul-pedagog | `antrenorul-pedagog` | `/antrenorul-pedagog` |
| `cat.principii-joc` | Principii de joc | `principii` | `/principii` |
| `cat.perceptie-decizie` | Percepție și decizie | `perceptie-decizie` | `/perceptie-decizie` |
| `cat.tehnica-context` | Tehnică în context | `tehnica-context` | `/tehnica-context` |
| `cat.motricitate` | Motricitate & Dezvoltare Fizică | `motricitate` | `/motricitate` |
| `cat.psihologie` | Psihologie & Emoție | `psihologie` | `/psihologie` |
| `cat.comunicare` | Comunicare & Relaționare | `comunicare` | `/comunicare` |
| `cat.exercitii` | Biblioteca de exerciții | `exercitii` | `/exercitii` |
| `cat.sedinte` | Ședințe complete de antrenament | `sedinte` | `/sedinte` |
| `cat.probleme-teren` | Probleme de rezolvat pe teren | `probleme` | `/probleme` |
| `cat.evaluare` | Evaluare & Progresie | `evaluare` | `/evaluare` |
| `cat.safeguarding` | Protecția copilului & Safeguarding | `safeguarding` | `/safeguarding` |
| `cat.parinti` | Relația cu părinții | `parinti` | `/parinti` |
| `cat.resurse` | Resurse & Fișe descurcabile | `resurse` | `/resurse` |
| `cat.metodologie-surse` | Metodologie & Surse de cercetare | `surse` | `/surse` |

---

## 3. Relații Canonice & Cardinalitate

```text
[Principle] (many-to-many) ──> [Exercise]
[Principle] (many-to-many) ──> [Claim] ──> [Source]
[Problem]   (many-to-many) ──> [Exercise]
[Problem]   (many-to-many) ──> [Principle]
[Exercise]  (one-to-many)  ──> [TacticalVisual] (Hooks)
```

---

## 4. Contractul Semantic al Entității Problem (Mode B)

Pentru orice problemă de teren, modelul impune distincția semantică strictă:
- **`OBSERVATION`:** Ceea ce antrenorul observă direct cu ochii pe teren (ex: *"Doi jucători se apropie la 1 metru de purtătorul de minge"*).
- **`POSSIBLE_CAUSE`:** Ipoteza metodologică (ex: *"Nivel afectiv de siguranță sau neînțelegere a orientării spațiale"*).
- **`INTERVENTION`:** Acțiunea practică și exercițiul recomandat pentru rezolvare.

---

## 5. Tactical Visual Hooks

Modelul pregătește câmpurile pentru motorul vizual ulterior:
- `diagram_ref`: referință diagramă statică SVG
- `animation_ref`: referință animație dinamică
- `video_export_ref`: export media/video
- `print_fallback_ref`: variantă simplificată pentru print alb-negru
