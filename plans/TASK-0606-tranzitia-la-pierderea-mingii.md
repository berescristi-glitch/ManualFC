# TASK-0606 — Tranziția la pierderea mingii

## Scop

Producerea CH-0206 despre reacția coordonată a echipei imediat după pierderea mingii: cel mai bine plasat jucător decide influența sau întârzierea, restul echipei protejează centrul, fără presing în bloc și fără prag temporal netestat.

## Rezultat

Capitol, principiu, fișă de teren, dosar research, audituri distincte, teste și raport verificabil.

## Cercetare

- Ce se știe despre comportamentul jucătorilor tineri imediat după pierderea posesiei?
- Cât de des se află jucătorii tineri sub presiune defensivă imediată, la vârste apropiate de U11?
- Există un prag temporal validat științific pentru recuperarea mingii (tip „regula de 5 secunde”)?

## Model de teren

5v5 + portari pe aproximativ 30 × 20 m (variantă 3v3 pe 20 × 15 m), atingeri limitate pentru linia ofensivă, observație fără intervenție verbală în primele momente după pierdere.

## Design

`VISUAL_DEBT_DEFERRED`; design freeze și fișierele vizuale protejate rămân intacte.

## Pași

- [x] 2026-08-10 — TASK-0605 închis; TASK-0606 recuperat din registry ca `READY`, fără muncă anterioară reală (verificat în `TASK_HISTORY.jsonl`, `research/`, `content/volume-02/`);
- [x] 2026-08-10 — cercetare verificată: Pires et al. 2025 (U14, pilot), González-Rodenas et al. 2022 (U10/U12), Merckx et al. 2021 (context tehnic pentru respingerea pragului de secunde);
- [x] 2026-08-10 — registre (`RQ-0527..0529`, `SRC-0044..0046`, `CLM-0045..0047`, `CIT-0050..0052`) și dosar `research/dossiers/ch-0206-tranzitia-la-pierdere.md`;
- [x] 2026-08-10 — capitol, principiu și fișă de teren;
- [x] 2026-08-10 — audituri factual/pedagogic și editorial distincte, teste task;
- [x] 2026-08-10 — full Python, validatoare și Astro check/build; registry/history închise.

## Rezultat și retrospectivă

Capitolul separă explicit influența imediată de protecția centrului și refuză două tentații: introducerea presingului în bloc ca metodă U11 și impunerea unui prag temporal de recuperare fără bază testată. Cercetarea directă la U11 pentru acest moment exact lipsește; capitolul este transparent despre acest gol.

## Acceptare

Capitol publicabil, chain-uri complete, mesaj fundamentat integral, categoria 2015–2016 unitară, toate validările verzi.

## Decizii

- Tranziția la pierdere este o secvență de decizii individuale coordonate, nu un cronometru sau o comandă unică.
- Presingul în bloc, cu roluri fixe și declanșator comun, rămâne `PRACTICE_ONLY` și amânat.
- Nu există prag temporal validat științific pentru recuperarea mingii, la nicio vârstă; „regulile de secunde” rămân folclor de coaching.
