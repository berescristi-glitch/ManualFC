# TASK-0103 — Dosar de cercetare: regulamente, formate și dimensiuni U11

## 1. Titlu și scop

Dosar factual, datat 2026-07-30, despre regulile FRF și AJF aplicabile copiilor
din categoria pedagogică unică 2015–2016.

## 2. Context pentru un cititor nou

TASK-0102 a fixat protocolul de cercetare. TASK-0103 îl aplică fără a redacta
volume: separă jurisdicția, sezonul, competiția și statutul fiecărei valori.

## 3. Rezultatul verificabil

Întrebările, căutările, sursele, afirmațiile și citările formează un lanț
valid. Matricea regulilor păstrează necunoscutele explicit, calculează doar
valori descriptive și semnalează conflictele dintre competiții.

## 4. Domeniu și non-obiective

Intră regulamentele FRF, AJF Satu Mare și comparația Sibiu–Bihor–Suceava.
Nu intră metodologia completă, exercițiile, volumele sau alegerea unei formații.

## 5. Fișiere și module afectate

`research/`, `data/regulations/`, `schemas/regulation-rule.schema.json`,
`scripts/validate_regulations.py`, `tests/test_regulations.py` și starea proiectului.

## 6. Cercetare necesară

Prioritate: pagina FRF, regulamentele competițiilor, pagina AJF Satu Mare și
regulamentele celor trei AJF comparative. PDF-urile sunt verificate textual,
vizual și prin SHA-256, fără a fi incluse în Git.

## 7. Model pedagogic

2015 și 2016 rămân împreună pedagogic. Eligibilitatea administrativă poate
diferi pe sezon; diferența nu creează automat două metodologii.

## 8. Design vizual și interactiv

Nu se creează active vizuale. Tabelele trebuie să rămână lizibile și să declare
unitățile. Dimensiunea de meci nu devine dimensiune de antrenament.

## 9. Pași de implementare

1. Verificare 2026–2027 și căutări reproductibile.
2. Extragere cu locator și hash.
3. Matrice, conflicte și calcule.
4. Audit factual și temporal separat.
5. Teste, validare, stare și commit.

## 10. Validare și acceptare

`python scripts/validate_regulations.py`, testele complete, validator normal,
strict și general, reproductibilitatea registrului și `git diff --check`.

## 11. Progres

- [x] 2026-07-30 — baseline exact și 31/31 teste.
- [x] 2026-07-30 — paginile oficiale și PDF-urile prioritare verificate.
- [x] 2026-07-30 — registrele și matricele sunt complete.
- [x] 2026-07-30 — auditul separat și cele 20 de teste trec.
- [x] 2026-07-30 — starea persistentă este finalizată; commitul focalizat urmează după auditul Git.

## 12. Descoperiri și surprize

- FRF publică Interliga de iarnă U11 2026–2027 pentru băieți 2016–2017.
- Pagina FRF nu listează Campionatul Național U11 masculin 2026–2027.
- AJF Satu Mare publică încă pe pagina de documente regulamentul U11 2023–2024.

## 13. Jurnal de decizii

- Necunoscutele sunt `null`, nu estimări.
- PDF-urile externe sunt hash-uite în spațiu temporar, nu incluse în Git.
- Regulamentul competiției concrete prevalează numai în domeniul său.

## 14. Rezultat și retrospectivă

Dosarul canonic separă fără echivoc regulile curente, istorice, locale,
comparative și documentele negăsite. Cea mai importantă limită este lipsa
publicării unui regulament masculin FRF U11 și a unuia AJF Satu Mare pentru
2026–2027 la data de referință. Această lipsă nu a fost completată prin
presupuneri; modelul de solicitare și TASK-0111 păstrează acțiunea de
reverificare. Validatorul generic a fost întărit pentru registre-container
populate, iar matricele au scheme și 20 de teste dedicate.
