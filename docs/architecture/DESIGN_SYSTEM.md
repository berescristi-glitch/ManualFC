# Specificație de Arhitectură: Sistemul de Design Web, Editorial, Print și Accesibilitate (ManualFC)

**Versiune:** 1.0.0  
**Data:** 2026-08-09  
**Statut:** Canonical / Approved  
**Task de referință:** TASK-0302  

---

## 1. Viziune & Principii de Design

Sistemul de design al platformei ManualFC transpune viziunea pedagogică în interfață web statică, accesibilă și printabilă. Sistemul deserveste două moduri principale ale produsului:

1. **Mode A („Vreau să învăț”)** — Parcursul editorial aprofundat (citire confortabilă, ierarhie clară, lățime container `prose`: 68ch, note de subsol, etichete de dovadă).
2. **Mode B („Am nevoie acum”)** — Rezolvarea rapidă pe teren/mobil (scanare facilă, culori de acțiune/avertisment, componente compacte, fără elemente ascunse în hover).

### Principii de Design:
- **Mobile-first & Field Use:** Lizibilitate maximă pe ecran de telefon pe terenul de antrenament.
- **Static-first & Token-driven:** 100% Vanilla CSS conectat la `config/visual-tokens.json`, fără dependențe UI externe.
- **AccesibilitateWCAG:** Semantice HTML5, landmark-uri, `skip-to-content`, contrast înalt, `lang="ro"`, respect pentru `prefers-reduced-motion`.
- **Print-Safe:** Modul `@media print` dezactivează navigația și chrome-ul web, asigurând lizibilitate alb-negru și export secundar PDF.

---

## 2. Jetoane Vizuale & Culori Semantice

Toate variabilele CSS sunt definite în `app/src/styles/tokens.css` și derivă din `config/visual-tokens.json`:

- **Roluri Tactice:**
  - Posesie (Atacant - A): `--color-role-possession` (`#1769AA`)
  - Oponent (Fundaș - D): `--color-role-opponent` (`#C62828`)
  - Neutral (N): `--color-role-neutral` (`#F9A825`)
  - Portar (P): `--color-role-goalkeeper` (`#2E7D32`)
  - Antrenor-Pedagog (C): `--color-role-coach` (`#FFFFFF`, outline `#111111`)

- **Culori Semantice:**
  - Suport Pedagogic: `--color-pedagogical` (`#0EA5E9`)
  - Evidență & Metodologie: `--color-evidence` (`#8B5CF6`)
  - Psihologie: `--color-psychology` (`#EC4899`)
  - Tactică: `--color-tactical` (`#10B981`)
  - Avertisment: `--color-warning` (`#F9A825`)
  - Pericol / Evitat: `--color-danger` (`#C62828`)

- **Lățimi de Container:**
  - `prose`: `68ch` (text editorial citire)
  - `standard`: `900px` (structură pagină)
  - `wide`: `1200px` (shell/navigare)

---

## 3. Taxonomie Epistemică (Research Layer)

Etichetele epistemice din `EvidenceBadge.astro` sunt cartografiate direct din valorile canonice ale registrului de cercetare:

| Valoare Canonică | Etichetă UI (Română) | Simbol Accesibil | Culoare Badge |
| :--- | :--- | :--- | :--- |
| **`HIGH`** | Evidență Puternică | `[EVIDENȚĂ RĂSPÂNDITĂ]` | `#166534` |
| **`MODERATE`** | Evidență Moderată | `[STUDIU EXPERIMENTAL]` | `#075985` |
| **`LOW`** | Evidență Limitată | `[DATE RESTRÂNSE]` | `#854D0E` |
| **`PRACTICE_ONLY`** | Practică de Academie | `[CONSENS EXPERȚI]` | `#6B21A8` |
| **`UNRESOLVED`** | Neconfirmat | `[ÎN VERIFICARE]` | `#991B1B` |

---

## 4. Contractul Semantic Nivel 1 & Nivel 2

Modelul canonic în 18 puncte separă riguros cele două niveluri de comunicare:
- **`ChildMessage.astro` (Nivelul 1):** Formularea exactă adresată copilului pe teren (ex: *"Verifică spațiul din spatele tău înainte să atinge minge!"*).
- **`CoachMessage.astro` (Nivelul 2):** Explicația profesională și sensul pentru antrenorul-pedagog (fundamentare, comportament urmărit, formulări de evitat, verificarea înțelegerii, transfer în meci).

---

## 5. Arhitectura Componentelor & Primitive-ul Comun

Pentru a preveni explozia de componente, toate blocurile pedagogice reutilizează primitive-ul unic `PedagogicalBlock.astro`:
- `WhyThisMatters` (`type="why"`)
- `ObserveThis` (`type="observe"`)
- `DecisionToLearn` (`type="decision"`)
- `CommonMistake` (`type="mistake"`)
- `PhraseToAvoid` (`type="avoid"`)
- `UnderstandingCheck` (`type="check"`)
- `Adaptation` (`type="adaptation"`)
- `MatchTransfer` (`type="transfer"`)
- `EvidenceNote` (`type="evidence"`)

---

## 6. Pattern-uri Structurale

- **`QuickModePattern.astro` (Mode B):** Structură compozițională prin sloturi (`causes`, `observe`, `say`, `why`, `action`, `adaptation`).
- **`DeepLearningPattern.astro` (Mode A):** Șablon compozițional editorial (`why-it-matters`, `perception`, `decision`, `coach-wording`, `evidence`, `transfer`).

---

## 7. Laboratorul Vizual Tehnic (Dev Only)

Ruta `app/src/pages/design-system.astro` servește ca laborator vizual izolat:
- Marcată cu `noindex,nofollow` și banner `INTERNAL / DEVELOPMENT ONLY`.
- Exclusă din navigarea publică.
