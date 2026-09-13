# Protocol Operațional de Autorizare și QA (`CANONICAL_AUTHORING_AND_QA_PROTOCOL`)

**Versiune:** 1.0.0 (Minimal Operational)  
**Data:** 2026-08-09  
**Task de referință:** TASK-0202  

---

## 1. Misiune

Acest protocol stabilește ghidul operațional în 10 pași pentru redactarea, revizuirea și integrarea capitolelor din platforma **ManualFC**, legând direct procesul de cercetare factuală de publicarea pe web.

---

## 2. Protocolul Operațional în 10 Pași

### 1. Definește problema / întrebarea pedagogică
- Identifică situația reală de pe teren și ce trebuie să poată face sau înțeleagă antrenorul (vezi [VOLUME_01_ARCHITECTURE.md](file:///e:/ManualFC/docs/content/VOLUME_01_ARCHITECTURE.md)).

### 2. Definește research questions (RQ-XXXX)
- Clarifică întrebările exacte de cercetare înainte de a redacta afirmațiile.

### 3. Colectează și verifică dovezile
- Identifică sursele cu prioritate pe review-uri sistematice, meta-analize, studii peer-reviewed și standarde oficiale (vezi [RESEARCH_PROTOCOL.md](file:///e:/ManualFC/docs/research/RESEARCH_PROTOCOL.md)).

### 4. Creează claims canonice
- Înregistrează afirmațiile în `research/claims.json` cu ID-uri unice (`CLM-XXXX`), nivel de dovadă și aplicabilitate U11.

### 5. Separă nivelurile epistemice
- Separă strict în text: `EVIDENCE` (ce susține literatura), `INTERPRETATION` (ce deducem), `PRACTICAL_RECOMMENDATION` (ce recomandăm antrenorului) și `FIELD_HYPOTHESIS` (ce testăm).

### 6. Redactează conținutul canonic
- Completează secțiunile din [CHAPTER_PRODUCTION_TEMPLATE.md](file:///e:/ManualFC/docs/content/CHAPTER_PRODUCTION_TEMPLATE.md) respectând ghidul editorial [EDITORIAL_STYLE_GUIDE.md](file:///e:/ManualFC/docs/EDITORIAL_STYLE_GUIDE.md).

### 7. Transformă în intervenție pedagogică
- Definește formularea pentru copil (`child_wording`), sensul pentru antrenor (`coach_meaning`), motivele, comportamentele urmărite și formulările de evitat.

### 8. Verifică aplicabilitatea și limitele
- Completează secțiunea obligatorie `LIMITATIONS / WHAT WE CANNOT CONCLUDE` și ajustează recomandările pentru diferențele individuale ale copiilor de 10–11 ani (2015-2016).

### 9. QA Pedagogic și Științific
- Parcurge porțile de calitate stabilite în [QUALITY_GATES.md](file:///e:/ManualFC/docs/QUALITY_GATES.md) (pedagogic, normativ, safeguarding, lingvistic, tehnic).

### 10. Publish Gate
- Rulează validatoarele automate, verifică referințele, execută `npm run check` și `npm run build`. Capitolul este aprobat doar cu cod de ieșire 0.
