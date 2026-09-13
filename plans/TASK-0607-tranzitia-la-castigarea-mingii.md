# TASK-0607 — Tranziția la câștigarea mingii

## Scop

Producerea CH-0207 despre secvența control-privire-decizie imediat după câștigarea mingii, fără regulă fixă de tipul „atacă imediat” sau „păstrează mereu în siguranță”.

## Rezultat

Capitol, principiu, fișă de teren, dosar research, audituri distincte, teste și raport verificabil.

## Cercetare

- Ce diferențiază comportamentul vizual (scanarea) copiilor cu nivel mai ridicat, în jurul primirii mingii, la vârste apropiate de U11?
- Corelează un test formal de decizie cu succesul real în jocuri reduse, la U10?
- Există dovadă că antrenamentul cu jocuri reduse schimbă decizia de tranziție? (reluat din registrul existent, `CLM-0036`)

## Model de teren

4v4 + portari pe aproximativ 25 × 18 m (variantă 3v3 pe două terenuri), pasă inițială de la antrenor/jucător neutru, fără presiune excesivă în primele 2 secunde.

## Design

`VISUAL_DEBT_DEFERRED`; design freeze și fișierele vizuale protejate rămân intacte.

## Pași

- [x] 2026-08-10 — TASK-0606 închis; TASK-0607 devine `READY`, verificat în registry/history;
- [x] 2026-08-10 — cercetare verificată: Savelsbergh et al. 2010 (10-12 ani, scanare), Fenner et al. 2022 (U10, test decizie), Clemente et al. 2021 reluat (`CLM-0036`);
- [x] 2026-08-10 — registre (`RQ-0530..0531`, `SRC-0047..0048`, `CLM-0048..0049`, `CIT-0053..0054`) și dosar `research/dossiers/ch-0207-tranzitia-la-castigare.md`;
- [x] 2026-08-10 — capitol, principiu și fișă de teren;
- [x] 2026-08-10 — audituri factual/pedagogic și editorial distincte, teste task;
- [x] 2026-08-10 — full Python, validatoare și Astro check/build; registry/history închise.

## Rezultat și retrospectivă

Capitolul respinge atât „atacă imediat” cât și „păstrează mereu în siguranță” ca reguli fixe, propunând o secvență observabilă (control, privire, decizie) fundamentată pe context, nu pe timp sau viteză. Cercetarea directă la U11 despre chiar momentul câștigării mingii lipsește; capitolul este transparent despre acest gol și respinge explicit importul statisticilor despre eficiența contraatacului din fotbalul profesionist adult.

## Acceptare

Capitol publicabil, chain-uri complete, mesaj fundamentat integral, categoria 2015–2016 unitară, toate validările verzi.

## Decizii

- Câștigarea mingii este o tranziție cu propria secvență: control, apoi privire, apoi decizie.
- Nu se importă „contraatacul e mai eficient” din fotbalul profesionist adult ca regulă pentru U11.
- Un test izolat de decizie nu înlocuiește observarea comportamentului real în joc.
