# CH-0206 — Tranziția la pierderea mingii

## Întrebări

- `RQ-0527`: ce se știe despre comportamentul jucătorilor tineri imediat după pierderea posesiei, în special tendința de a urmări mingea?
- `RQ-0528`: cât de des se află jucătorii tineri sub presiune defensivă imediată în posesie, la vârste apropiate de U11?
- `RQ-0529`: există un prag temporal validat științific pentru recuperarea mingii după pierdere, de tipul unei „reguli de 5 secunde”?

## Surse verificate

### SRC-0044 — Pires, Vigário, Ferreira, Vicente (2025)

Studiu pilot exploratoriu, 20 de jucători băieți U14 dintr-un club portughez, urmăriți în cinci meciuri oficiale printr-o matrice de tranziție atac-apărare (ADT). Jucătorii au menținut semnificativ mai des intenția de recuperare a mingii după pierdere decât au abandonat-o (p=0,004). Autorii numesc explicit rezultatul „generator de ipoteze”, nu confirmator; eșantionul este mic și dintr-un singur club.

### SRC-0045 — González-Rodenas, Pedrera, Dorado, Aranda-Malavés, Tudela-Desantes, De Matías-Cid (2022)

Studiu observațional pe 1.247 posesii individuale (320 jucători, 32 echipe) din turnee elite spaniole 7 la 7, categoriile U10 și U12. Fiabilitate inter/intra-observator puternică (kappa 0,81–0,99). Jucătorii U10 s-au aflat sub presiune defensivă în 83,1% dintre posesii, față de 61,8% la U12; U10 a avut șanse mai mari de dribling față de pasă. Analizează echipa aflată în posesie, nu comportamentul echipei care tocmai a pierdut mingea.

### SRC-0046 — Merckx, Robberechts, Euvrard, Davis (2021)

Lucrare tehnică de modelare computațională (KU Leuven, atelier MLSA la ECML/PKDD 2021), aplicată pe urmărire pozițională din liga profesionistă belgiană (241 meciuri). Definește operațional „recuperarea mingii” ca etichetă de date pentru un clasificator de învățare automată. Nu conține populație de juniori și nu testează un prag pedagogic. Textul integral nu a putut fi extras automat; nu se citează un număr exact de secunde/metri fără confirmare suplimentară — se folosește doar faptul verificat că lucrarea există, este profesionistă-adultă și computațională.

## Claim decisions

### CLM-0045 — NARROW / LOW / INDIRECT

Păstrăm doar tendința observată la U14 de a menține recuperarea; nu transferăm procentul sau concluzia la U11.

### CLM-0046 — NARROW / MODERATE / PARTIAL

Păstrăm frecvența presiunii asupra jucătorului cu mingea la U10/U12, ca justificare a relevanței temei la această vârstă; nu o transformăm în descriere a reacției echipei care apără.

### CLM-0047 — KEEP / LOW / INDIRECT

Folosim lucrarea doar pentru a arăta ce înseamnă tehnic „fereastră de câteva secunde” în cercetarea profesionistă (etichetă de date, nu prag testat), ca bază pentru a respinge explicit „regula de 5 secunde” ca normă științifică pentru copii.

## Citation map

- `CLM-0045 → CIT-0050 → SRC-0044`: suport direct pentru tendința observată la U14.
- `CLM-0046 → CIT-0051 → SRC-0045`: suport direct pentru frecvența presiunii la U10/U12.
- `CLM-0047 → CIT-0052 → SRC-0046`: suport contextual pentru respingerea unui prag temporal universal.
- `CLM-0043 → CIT-0048 → SRC-0042`: context direct U11 despre acoperire și echilibru, reluat din CH-0204/CH-0205.
- `CLM-0044 → CIT-0049 → SRC-0043`: context indirect despre tipul țintei și recuperare, reluat din CH-0205.

## Ce nu susțin sursele

- că U11 urmărește automat mingea după pierdere (CLM-0045 este U14, pilot);
- cum se reorganizează defensiv echipa care tocmai a pierdut mingea (CLM-0046 măsoară echipa cu mingea);
- un prag temporal sau de distanță pentru recuperare, validat pedagogic (CLM-0047 arată doar o convenție de etichetare a datelor);
- eficiența presingului în bloc (gegenpressing) la copii de nicio vârstă;
- transferul direct al oricărui rezultat la formatul 7v7 sau la meci complet.

## Gap

Lipsește orice studiu observațional sau experimental care măsoară direct reorganizarea defensivă, timpul de reacție sau coordonarea presiune–acoperire imediat după pierderea mingii, la jucători U11.
