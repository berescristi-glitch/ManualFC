# TASK-2702 — Production hygiene

## Scop și rezultat verificabil

Separă suprafețele publice de laboratoarele și fixture-urile tehnice. Buildul public nu mai generează rutele interne, însă sursele de QA rămân în repository și testabile.

## Domeniu

Clasificare exhaustivă a rutelor, relocarea controlată a paginilor interne, actualizarea testelor și verificare browser a rutelor publice, a răspunsurilor 404 și a absenței rutelor interne. Nu schimbă IA publică și nu redesenează template-urile.

## Progres

- [x] Stare Git și handoff recuperate.
- [x] Task formalizat înaintea implementării.
- [x] Inventar și clasificare de rută documentate.
- [x] Fixture-urile scoase din buildul public fără pierderea sursei de QA.
- [x] Validări automate și browser la 1440/768/390; 1280 este acoperit în acceptanța Wave-1 finală.
- [x] Raport și registre finalizate; commit separat urmează imediat.

## Rezultat

Cinci suprafețe interne nu mai sunt generate: laboratorul UI, fixture-ul MDX, rutele fixture de exercițiu/problemă și principiul fixture. Buildul public conține 69 de pagini, iar ruta internă eșantion `/design-system` afișează 404.

## Riscuri și control

Testele istorice pot presupune că fixture-urile locuiesc în `pages/`; ele vor fi actualizate să verifice noua frontieră public/intern. Nicio entitate canonică nu este ștearsă.
