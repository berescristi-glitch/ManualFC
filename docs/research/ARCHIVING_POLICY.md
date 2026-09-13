# Politica de arhivare și distribuție

## Niveluri

- A — metadate: obligatoriu pentru orice sursă; intră în Git și pachetul sursă.
- B — snapshot permis: copie publică sau licențiată, hash SHA-256, manifest și drepturi; intră în Git numai dacă licența și dimensiunea permit.
- C — referință fără redistribuire: metadate, note, locator și eventual hash; fișierul rămâne local și este exclus din Git/distribuție.

`research/source-snapshots/` conține numai nivel B. `restricted-source-metadata/` nu conține operele protejate. Fișierele locale restrictive nu intră în site, PDF, pachet editabil sau arhiva publică.

## Reguli

Nu se copiază integral cărți, articole restricționate, cursuri comerciale sau active cu drepturi neclare. Snapshotul este creat numai dacă `usage_rights.store_snapshot` este adevărat. Manifestul păstrează sursa, calea, hashul, dimensiunea, data, licența și statutul distribuției.

Fișierele descărcate nu sunt executate. Secretele, cookie-urile, conturile și datele despre copii identificabili sunt interzise.
