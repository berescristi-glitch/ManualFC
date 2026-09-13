# TASK-2208 — Integrare web Gold Standard (Quick Mode + Deep Mode)

## Scop

Integra continuu entitățile Gold Standard (exerciții, ședințe, evaluare) în platforma web existentă, folosind arhitectura curentă (`content-bridge.ts`, Astro), fără infrastructură paralelă și fără a atinge design freeze-ul.

## Constatare și decizie de arhitectură

Adaptorul TypeScript existent pentru exerciții (`ExerciseEntity`/`validateAndParseExercise`, din `TASK-0402`) așteaptă o formă mult mai simplă decât schema reală de producție (`schemas/exercise.schema.json`). Clasificat `SYSTEMIC_PRODUCT_PROBLEM` (afectează orice exercițiu viitor, nu doar Gold Standard), dar rezolvat **minimal și aditiv**: tipuri și loadere noi (`GoldStandardExercise`/`Session`/`Assessment`) adăugate în `content-bridge.ts`, fără să se modifice sau să se rupă loaderele existente pentru principii/exerciții/probleme.

## Metodă

1. Import direct al celor 5 exerciții, 2 ședințe, 1 evaluare din `data/`.
2. Funcții fail-closed (aruncă eroare la câmp lipsă sau referință ruptă), consecvent cu stilul existent din `content-bridge.ts`.
3. Patru pagini noi: index (Deep Mode), rapid (Quick Mode, reutilizează `QuickModePattern`), detaliu exercițiu, detaliu ședință.
4. Verificare: `npx astro check`, `npm run build`, apoi test dedicat care confirmă static că niciun fișier de design freeze nu conține marcaje Gold Standard.

## Rezultat

Vezi `reports/task-reports/TASK-2208.md`. `TASK-2209` (audit independent) devine `READY`.
