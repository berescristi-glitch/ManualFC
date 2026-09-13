# Strategie de build și testare

## Trepte de build

1. validarea registrelor și a JSON Schema;
2. validarea referințelor și a manifestelor;
3. compilarea conținutului și a datelor într-un model de citire;
4. build static web fără dependență de rețea;
5. verificarea rutelor, linkurilor și activelor;
6. randarea print și generarea PDF cu Chromium;
7. verificarea vizuală eșantionată și automată;
8. împachetarea surselor, resurselor editabile și produselor;
9. dezarhivarea într-un director curat și rerularea testelor de acceptare;
10. calcularea hashurilor și raportul final.

## Piramida de testare

- bootstrap: `scripts/validate_project.py`;
- contracte: toate instanțele JSON contra schemelor;
- unitare: parsare, identificatori, graf, transformări și calculul progresului;
- integrare: referințe între capitole, date, surse și active;
- browser: navigație, căutare, controale de animație, tastatură și offline;
- vizual: viewport desktop/mobil, print color/alb-negru, zoom;
- livrare: build și PDF din mediu curat, apoi testul arhivei.

## Politica de blocare

Erorile de schemă, referințele orfane, afirmațiile critice fără surse, activele lipsă, problemele de accesibilitate critice și eșecul buildului blochează `DONE`. Un validator indisponibil este raportat și produce task de remediere; nu este tratat drept PASS.
