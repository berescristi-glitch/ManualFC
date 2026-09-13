# TASK-0602 — Spațiu și unghiuri

## Scop

Producerea CH-0202, astfel încât antrenorul să predea spațiul ca relație schimbătoare între minge, adversar, coleg și țintă, nu ca poziție fixă pe teren.

## Rezultat verificabil

- capitol canonic publicabil și principiu structurat;
- două chain-uri research despre dimensiunea terenului și comportamentul juvenil;
- fișă de observație utilizabilă pe teren;
- audit factual/pedagogic și audit editorial distincte;
- validări complete și raport TASK-0602.

## Domeniu și non-obiective

Intră: lățime, adâncime, linie de pasă, umbra adversarului, orientarea primirii, reglarea spațiului și transferul în joc. Nu intră: formații rigide, dimensiuni declarate „optime”, active vizuale ori modificări de design.

## Cercetare

- Cum schimbă dimensiunea suprafeței dispersia colectivă în jocurile reduse?
- Ce diferențe de amplitudine apar la jucători tineri între jocuri complete și reduse?
- Ce nu poate fi transferat direct la grupa combinată 10–11 ani?

## Model de teren

3v3 la două porți mici, aproximativ 28 × 22 m, cu minimum 2 m spațiu de siguranță. Golul contează normal; antrenorul observă dacă jucătorul fără minge schimbă relația cu același apărător și creează o linie nouă.

## Design

`VISUAL_DEBT_DEFERRED`: design freeze rămâne activ; nu se ating fișierele vizuale protejate.

## Pași

- [x] 2026-08-10 — task, dependențe, standarde și worktree inspectate;
- [x] 2026-08-10 — sursele primare și limitele de aplicabilitate verificate;
- [x] 2026-08-10 — registre, dosar și claim decisions;
- [x] 2026-08-10 — capitol, principiu și instrument de teren;
- [x] 2026-08-10 — audit factual/pedagogic și editorial;
- [x] 2026-08-10 — 8/8 teste task, 202/202 full Python, validatoare și Astro check/build PASS; registry/history închise.

## Rezultat și retrospectivă

CH-0202 este publicabil și lasă o fișă care separă oportunitatea, percepția, decizia, execuția și rezultatul. Un test persistent pentru următorul task READY a detectat tranziția neactualizată și a fost mutat la TASK-0603. Design freeze a rămas intact.

## Acceptare

Testele taskului, toate testele Python, validarea strictă a conținutului, registry check, validatorul proiectului, testele npm, Astro check/build și `git diff --check` trebuie să treacă. Afirmațiile despre dimensiuni trebuie să rămână contextuale, nu prescriptive.

## Decizii

- Spațiul util este definit operațional prin efectul asupra posibilităților de joc, nu prin ocuparea unui reper geometric.
- „Mută-te până când adversarul nu vă mai poate acoperi pe amândoi” este o sinteză practică ManualFC, nu formulare validată experimental.
