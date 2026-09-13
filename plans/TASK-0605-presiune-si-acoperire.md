# TASK-0605 — Presiune și acoperire

## Scop

Producerea CH-0205 despre coordonarea primului și celui de-al doilea apărător: presiunea reduce timpul, acoperirea protejează depășirea, iar rolurile se schimbă odată cu mingea.

## Rezultat

Capitol, principiu, fișă de teren, dosar research, audituri distincte, teste și raport verificabil.

## Cercetare

- Cum schimbă tipul țintei locul și modalitatea recuperării în jocuri juvenile 4v4?
- Ce limite apar din populația U13/U15 și din eșantionul mic?
- Cum proiectăm presiunea–acoperirea fără dublaj rigid sau comandă permanentă?

## Model de teren

2v2+portari cu două echipe în rotație activă, 24 × 18 m. Primul apărător întârzie; al doilea protejează depășirea și preia rolul când mingea se mută.

## Design

`VISUAL_DEBT_DEFERRED`; design freeze și fișierele vizuale protejate rămân intacte.

## Pași

- [x] 2026-08-10 — TASK-0604 închis și TASK-0605 selectat READY;
- [x] 2026-08-10 — studiul U13/U15 despre tipul țintei și recuperare verificat;
- [x] 2026-08-10 — registre și dosar;
- [x] 2026-08-10 — capitol, principiu și fișă;
- [x] 2026-08-10 — audituri și 8/8 teste task;
- [x] 2026-08-10 — 226/226 full Python, validatoare și Astro check/build PASS; registry/history închise.

## Rezultat și retrospectivă

Capitolul este publicabil și refuză folosirea tacklingului ca proxy pentru calitatea presiunii. Rotația explicită și varianta cu două terenuri păstrează fezabilitatea pentru efective diferite. Sursa indirectă rămâne limitată la efectul țintei asupra comportamentului observat.

## Acceptare

Capitol publicabil, chain-uri complete, mesaj fundamentat integral, categoria 2015–2016 unitară și toate validările verzi.

## Decizii

- Presiunea este influență controlată asupra purtătorului, nu sprint necondiționat la minge.
- Acoperirea pregătește răspunsul la depășire și poate deveni imediat noua presiune.
