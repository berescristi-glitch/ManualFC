# Specificație de Arhitectură: Modelul de Conținut și Relații (ManualFC)

**Versiune:** 1.0.0  
**Data:** 2026-08-09  
**Statut:** Canonical / Approved  
**Task de referință:** TASK-0201  

---

## 1. Misiune & Structura Modelului

Modelul de conținut al platformei **ManualFC** definește clasele de entități, contractul unic de ID-uri și slug-uri, modelul relațional static-first (Knowledge Graph Light) și modul în care datele sunt consumate de aplicația web.

### Documentație de referință:
- [CONTENT_TAXONOMY.md](file:///e:/ManualFC/docs/architecture/CONTENT_TAXONOMY.md) — Registrul de taxonomie și contractele de date.
- [DESIGN_SYSTEM.md](file:///e:/ManualFC/docs/architecture/DESIGN_SYSTEM.md) — Sistemul de design și componentele vizuale/pedagogice.

---

## 2. Clasificarea Entităților (Entity Classes)

1. **`PRIMARY_CONTENT_ENTITY`:** `Principle`, `Exercise`, `Session`, `Problem`, `Assessment`, `CaseStudy`
2. **`SUPPORTING_ENTITY`:** `Concept`, `PerceptualCue`, `Decision`, `CoachMessage`, `ChildMessage`, `Adaptation`, `SafeguardingRule`
3. **`RESEARCH_ENTITY`:** `Source`, `Claim`, `Citation`
4. **`VISUAL_ENTITY`:** `TacticalVisual`, `Animation`
5. **`SYSTEM_ENTITY`:** `Category`, `AgeProfile`

---

## 3. Rute Web Dinamice & Bridge de Conținut

Toate entitățile canonice stocate în `data/` sunt procesate prin `app/src/lib/content-bridge.ts` pentru generarea rutelor statice:
- `/principii/[slug]`
- `/probleme/[slug]`
- `/exercitii/[slug]`
