# Gold Standard — Pachetul de concept: Sprijinul și unghiul de pasă

**Task:** TASK-2203
**Status:** COMPLETE
**Data:** 2026-08-12

Acest document nu re-derivă conceptul de bază — îl reutilizează explicit din `principle-spatiu-si-unghiuri` (CH-0202) și `principle-progresie-si-sprijin` (CH-0203), ambele `FIELD_REVIEW_READY`, și adaugă doar ce lipsea: definiția profesională extinsă, distincția principiu-vs-regulă-geometrică, dimensiunea tehnică (din `TASK-2202`), și o taxonomie de erori observabile + model de intervenție specifice acestui subiect (reutilizând cadrul general din CH-0404).

## 1. Definiția profesională

**Sprijin** = poziționarea și disponibilitatea unui jucător fără minge astfel încât să ofere purtătorului mingii o continuare reală a jocului — nu prezența într-un loc, ci o relație funcțională între minge, adversar(i) relevanți, coleg(i) și țintă.

**Unghi de pasă** = linia geometrică dintre purtătorul mingii și un coechipier, evaluată prin capacitatea unui adversar de a o închide simultan cu o altă opțiune. Un unghi „bun” nu e un unghi cu o valoare fixă în grade — e un unghi pe care adversarul relevant nu-l poate acoperi fără să deschidă o altă opțiune (`principle-spatiu-si-unghiuri`: „Mută-te până când adversarul nu vă mai poate acoperi pe amândoi”).

### Relațiile implicate
- **Purtătorul mingii** — presiunea asupra lui determină timpul disponibil pentru decizie.
- **Jucătorul de sprijin** — reglează direcția, distanța și orientarea corporală.
- **Adversarul relevant** — cel care poate acoperi simultan două opțiuni; nu orice adversar de pe teren.
- **Linia/unghiul de pasă** — funcție a poziției relative, nu geometrie fixă.
- **Distanța** — suficientă pentru a nu fi acoperită de același adversar, dar utilă pentru continuare.
- **Orientarea corporală** — determină ce poate face jucătorul de sprijin *după* ce primește (dimensiunea tehnică, secțiunea 4).
- **Spațiul disponibil** — ce rămâne accesibil după deplasarea adversarului.
- **Acțiunea următoare** — sprijinul nu e un scop în sine; există pentru ce urmează după recepție.

## 2. Principiu, nu regulă geometrică

`principle-spatiu-si-unghiuri` respinge explicit formulările de tip regulă fixă: „Stai larg” (transformă lățimea într-o poziție permanentă), „Fă triunghi” (cere o formă geometrică fără funcția liniei/distanței/orientării). Gold Standard-ul păstrează această poziție: **niciun unghi exact (ex. 45°) nu e prezentat ca regulă tactică validată**. Cercetarea nu susține un unghi universal — principiul rămâne funcțional („creează o opțiune de pasă utilă”), nu geometric. Orice unghi/distanță folosit(ă) în exercițiile viitoare (`TASK-2204`) va fi etichetat(ă) explicit `EXERCISE_SPECIFIC_PARAMETER` sau `MANUALFC_HEURISTIC`, niciodată `SOURCE_DIRECT`.

## 3. Modelul perceptiv (ce trebuie să observe copilul)

Reutilizat direct din `principle-spatiu-si-unghiuri` și `principle-progresie-si-sprijin`:
- poziția și orientarea mingii;
- adversarul care acoperă linia de pasă;
- poziția celuilalt coleg (dacă există opțiune alternativă);
- ținta și acțiunea următoare;
- timpul în care adversarul relevant poate ajunge să acopere;
- presiunea asupra purtătorului mingii;
- spațiul care apare după deplasarea adversarului.

Nu se adaugă informații suplimentare doar pentru că par tactic sofisticate — lista de mai sus e suficientă și sursa (CLM-0036, CLM-0038, CLM-0040–CLM-0042) o susține.

## 4. Dimensiunea tehnică (nou, din TASK-2202)

Sprijinul bun creează o *opțiune*; execuția tehnică determină dacă acea opțiune poate fi *folosită* după recepție.

- **Orientare la recepție**: dovada disponibilă (`CLM-0101`) leagă scanarea dinainte de a primi mingea de o orientare corporală mai bună la recepție — dar la populații elite U17+/adulte. Extrapolarea la U11 e plauzibilă, declarată explicit ca extrapolare.
- **Focus atențional extern**: cea mai apropiată dovadă de vârsta U11 (`CLM-0102`, RCT la 7 ani + studiu la 12,94 ani) arată că indicii externi (nu instrucțiuni interne despre poziția piciorului) și sarcinile cu decizie activă îmbunătățesc execuția tehnică măsurabil.
- **Nu există o „tehnică de recepție corectă” unică validată** (`CLM-0103`) — execuția depinde de designul sarcinii, consecvent cu cadrul de dinamică ecologică deja folosit în proiect.
- **Direcția primului contact relativ la presiune** — nicio cercetare găsită nu o testează direct (`CLM-0104`). Rămâne euristică practică, niciodată prezentată drept cercetare.

**Consecință pentru exerciții (`TASK-2204`)**: exercițiile vor folosi indicii externe (unde e spațiul, nu ce unghi să facă piciorul) și sarcini cu decizie activă, nu instrucție tehnică izolată despre forma „corectă” de recepție.

## 5. Modelul decizional

Reutilizat din `principle-spatiu-si-unghiuri` (direcție + distanță a deplasării) și `principle-progresie-si-sprijin` (prioritizare: progresie directă înainte de a căuta sprijin lateral/înapoi). Deciziile pe care copilul le învață:
1. Există o cale directă de progresie? (verifică întâi)
2. Dacă nu — ce direcție/distanță de deplasare creează o opțiune pe care adversarul relevant nu o poate acoperi simultan cu alta?
3. Odată ce primește — ce orientare corporală păstrează o continuare posibilă?

Aceasta e explicit un lanț `INFORMAȚIE → DECIZIE → MIȘCARE → INFORMAȚIE NOUĂ`, nu o poziție finală statică (instrucțiunea #25 din specificația Gold Standard).

## 6. Taxonomia erorilor observabile

Erorile sunt **observații**, nu diagnostice. Fiecare rând separă explicit ce s-a văzut de cauzele posibile (care necesită verificare, nu presupunere).

| Observație | Cauze posibile (de verificat, nu presupuse) |
|---|---|
| Copilul rămâne pe aceeași linie cu purtătorul mingii (acoperit de același adversar) | nu a perceput unghiul adversarului · nu știe unde e spațiul util · a fost instruit greșit anterior („stai larg”) · sarcina e prea grea perceptiv |
| Copilul se deplasează, dar prea aproape de purtător | nu a evaluat distanța · presiune de timp prea mare · lipsă de încredere să se îndepărteze |
| Copilul se deplasează, dar prea departe (opțiune inutilă) | a supra-corectat · nu a evaluat timpul de reacție al adversarului |
| Copilul se mișcă abia după ce linia de pasă e deja blocată | timing întârziat, posibil lipsă de scanare anterioară · procesare lentă, nu lipsă de „inteligență” |
| Copilul primește cu corp închis, nu poate continua | nu a scanat înainte de recepție · instrucție tehnică anterioară supra-încărcată · execuție motrică încă instabilă la această vârstă |
| Toți jucătorii de sprijin se mută în aceeași zonă | lipsă de comunicare între ei · lipsă de conștientizare a colegilor · sarcina nu impune diferențiere |

**Regulă:** nu se afirmă niciodată „nu înțelege sprijinul” pe baza unei singure erori de poziționare (`principle-eroarea-ca-informatie`, CH-0103, reutilizat direct).

## 7. Modelul de intervenție

Reutilizat integral din `principle-focalizarea-observatiei-si-criterii-de-interventie` (CH-0404) — nu se re-inventează:
1. Un singur focalizator de observare per rundă (ex: doar orientarea la recepție, sau doar direcția deplasării).
2. Observă înainte de a interveni — nu la prima eroare izolată, fără număr fix de repetări.
3. Evaluează: eroare de execuție izolată → lasă jocul să curgă; tipar repetat de percepție/decizie → întrebare ghidată la pauză; pericol fizic → intervenție imediată.
4. Intervenție scurtă, fără durată cronometrată fixă.

Aplicat la acest subiect: întrebarea ghidată tipică nu e „De ce nu ai văzut unghiul?” (diagnostic), ci „Ce ai văzut acolo?” / „Unde altundeva puteai fi ca să nu fii acoperit?” (`principle-eroarea-ca-informatie`).

## 8. Ce NU afirmăm (rezumat)

- Niciun unghi/distanță exactă ca regulă tactică validată.
- Niciun prag de timp/repetiții pentru intervenție.
- Nicio „tehnică de recepție corectă” unică.
- Nicio dovadă directă a lanțului scanare→orientare→atingere la exact 10–11 ani — doar extrapolare declarată de la populații mai mari.
- Nicio dovadă pentru direcția primului contact relativ la presiune.

## 9. Concluzie

`CONCEPT_MODEL = COMPLETE`. Fundația conceptuală, perceptivă și decizională e cea deja aprobată din VOLUME-02; dimensiunea tehnică e nouă și calibrată sceptic; taxonomia de erori și modelul de intervenție sunt specifice acestui subiect, dar reutilizează integral cadrul general validat din VOLUME-01/VOLUME-04. `TASK-2204` (sistemul de exerciții) devine `READY`.
