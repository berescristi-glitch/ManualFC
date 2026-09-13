# Group Configurator — logistică de teren determinată din date canonice

## Ce calculează, de unde

Configuratorul (`app/src/lib/group-configurator.ts`) nu autorizează conținut nou — derivă, pentru un efectiv țintă (8/10/12/14/16/18) și 1 sau 2 antrenori, câte grupe, câți copii activi/în așteptare, câtă suprafață și câte materiale sunt necesare la fiecare exercițiu Gold Standard, exclusiv din câmpurile deja canonice ale exercițiului: `players.total` (mărimea grupului), `field` (dimensiuni + marjă de siguranță), `equipment_items` (cantități structurate) și `duration.format`.

Mărimea grupului rămâne fixă la `players.total` al exercițiului — niciodată umflată sau micșorată pentru a se potrivi unui efectiv, pentru că asta ar schimba relația numerică (`numerical_relation`, ex. „2v1”) și, cu ea, ce anume exersează exercițiul. La un efectiv neuniform, restul de copii rămân explicit „în așteptare”, cu rotație în grupele active la fiecare set.

## Ce este etichetat `PRACTICE_HEURISTIC`

Trei decizii nu sunt validate de cercetare și sunt etichetate explicit ca atare, vizibil pe pagină:

1. **regula de rotație** pentru copiii rămași în afara unei grupe complete;
2. **aranjamentul spațial** — grupele așezate una lângă alta pe un singur rând, cu marja de siguranță proprie fiecărei grupe;
3. **poziționarea antrenorului/antrenorilor** — câte grupe poate acoperi direct un antrenor.

Nimic din acestea nu este prezentat ca prag validat științific.

## `equipment_items` — extensie aditivă a schemei

`schemas/exercise.schema.json` primește un câmp nou, obligatoriu, `equipment_items: [{item, quantity, quantity_max?}]`, alături de `equipment` (proza existentă, neschimbată, folosită pentru afișare). Cantitățile din `equipment_items` sunt aceleași numere deja prezente în proza `equipment` a fiecărui exercițiu — o structurare, nu o invenție. `content-bridge.ts` extinde tipul `GoldStandardExercise` și parserul fail-closed cu acest câmp.

## Unde apare

`/gold-standard/configurator` — o pagină dedicată, legată din `/gold-standard` (secțiunea „Configurator de grup”), cu un tabel per exercițiu × per efectiv, pentru 1 și 2 antrenori. Sursa de adevăr rămâne aceeași folosită de paginile de exercițiu/ședință (`getGoldStandardExercises()`), fără date paralele.
