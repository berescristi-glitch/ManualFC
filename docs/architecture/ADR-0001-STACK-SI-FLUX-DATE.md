# ADR-0001 — Stack static, data-driven, cu o singură sursă de adevăr

- Statut: acceptat
- Data: 2026-07-30
- Decidenți: proiectul Manual U11, prin TASK-0001

## Context

Același material trebuie publicat ca manual web offline, PDF și pachet editabil. Principiile, exercițiile, ședințele, citările și activele vizuale trebuie auditate fără a inspecta componente UI. Animațiile sunt necesare doar pentru situațiile dinamice, iar PDF-ul trebuie să primească o reprezentare statică echivalentă.

## Decizie

Arhitectura țintă folosește:

- Astro în mod static pentru shell, navigație, pagini și generarea site-ului;
- TypeScript strict pentru încărcarea, validarea și conectarea datelor;
- Markdown/MDX pentru proza capitolelor;
- JSON conform JSON Schema 2020-12 pentru entitățile structurate;
- SVG original, semantic și accesibil pentru diagrame;
- componente interactive izolate, încărcate numai unde sunt necesare;
- CSS cu profil distinct pentru ecran, print color și print alb-negru;
- Playwright/Chromium pentru fluxuri, capturi și PDF;
- validare Python fără dependențe pentru integritatea repository-ului, completată ulterior de validatorul JSON Schema din toolchain-ul Node;
- toate resursele împachetate local; niciun CDN obligatoriu.

Fluxul este:

`surse → afirmații → citări → capitole/date → SVG/animații → site static → PDF → audit → arhivă`

## Contracte de separare

- UI nu conține definiții canonice de principii, exerciții sau ședințe.
- O afirmație factuală importantă indică cel puțin o sursă prin registrul de citări.
- Orice mesaj transmis copilului referă o fundamentare conform schemei dedicate.
- Un activ vizual are manifest, sursă editabilă, descriere accesibilă și echivalent PDF.
- ID-urile sunt stabile și sunt validate înainte de build.

## Alternative

### Next.js

Are ecosistem extins, dar adaugă concepte de runtime și server care nu sunt necesare produsului static. Poate fi reconsiderat numai dacă apare o cerință justificată de server.

### Generator propriu

Ar reduce dependențele inițiale, dar ar transfera proiectului costul navigației, MDX, optimizării și al accesibilității fără avantaj editorial.

### Document-first, cu web derivat din PDF

Ar simplifica tiparul, dar ar slăbi interactivitatea, validarea entităților și reutilizarea datelor.

## Consecințe

Pozitive: o singură sursă de adevăr, export static offline, audit automat, JavaScript limitat, paritate controlată web/PDF.

Costuri: toolchain mixt Python/Node, reguli stricte de ID și legături, necesitatea testării separate a randării print.

## Condiții de revizuire

ADR-ul se revizuiește numai dacă un prototip validat demonstrează că exportul static, PDF-ul sau accesibilitatea nu pot îndeplini cerințele. Comoditatea implementării nu este motiv suficient.
