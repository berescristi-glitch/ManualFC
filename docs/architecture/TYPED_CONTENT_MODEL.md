# Specificație de Arhitectură: Sistemul Tipizat de Conținut și Relații (ManualFC)

**Versiune:** 1.0.0  
**Data:** 2026-08-09  
**Statut:** Canonical / Approved  
**Task de referință:** TASK-0402  

---

## 1. Misiune & Arhitectură TypeScript

Sistemul tipizat de conținut transpune contractele canonice de taxonomie (`data/taxonomy/registry.json`) într-un API TypeScript stabil, strict tipizat și fail-closed (`app/src/types/content-model.ts`, `app/src/lib/json-boundary.ts`, `app/src/lib/content-bridge.ts`).

### Principii Fondatoare:
1. **Branded Types cu Constructor Centralizat:** `CanonicalId`, `EntitySlug`, `CategoryId`, `EvidenceClaimId`, `SourceId` sunt create exclusiv prin funcțiile centrale de parsare/validare (`parseCanonicalId`, `parseEntitySlug`, etc.), împiedicând cast-urile arbitrare `value as CanonicalId`.
2. **Boundary de Validare Date (JSON Boundary):** Modulul `app/src/lib/json-boundary.ts` efectuează narrowing-ul și validarea la build-time la citirea fișierelor JSON.
3. **Discriminare Semantică Entitate Problem:** Separare strictă între `OBSERVATION` (simptom observat), `POSSIBLE_CAUSE` (ipoteză) și `INTERVENTION` (exercițiu/acțiune).
4. **Verificarea Tipului Țintă în Relații:** `Content Bridge 2.0` verifică nu doar existența referinței, ci și potrivirea tipului de entitate țintă (ex: refusarea unui ID `principle.*` în câmpul `exercise_ids`).
5. **Izolarea Fixture-urilor:** Separare programatică între `getDevelopmentFixtures()` și `getCanonicalProductionContent()`.

---

## 2. API Content Bridge 2.0

```typescript
// Căutare după ID canonic sau Slug
lookupByCanonicalId(id: string): PrincipleEntity | ExerciseEntity | ProblemEntity | undefined;
lookupBySlug(slug: string): PrincipleEntity | ExerciseEntity | ProblemEntity | undefined;

// Rezolvare Relații Tipizate (Fail-Closed)
getResolvedPrinciple(idOrSlug: string): ResolvedPrinciple;
getResolvedExercise(idOrSlug: string): ResolvedExercise;
getResolvedProblem(idOrSlug: string): ResolvedProblem;

// Izolare Fixtures
getDevelopmentFixtures<T>(entities: T[]): T[];
getCanonicalProductionContent<T>(entities: T[]): T[];

// Validare Duplicat ID
validateNoDuplicateIds(): void;
```

---

## 3. Model de Erori (Fail-Closed Diagnostics)

Mesajele de eroare la build indică exact contextul:
- `Source Entity`: ID-ul entității care declară referința
- `Relation Field`: numele câmpului de legătură
- `Missing/Invalid Ref`: valoarea referinței greșite
- `Expected / Actual Type`: tipul așteptat față de cel găsit
