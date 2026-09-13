# Sistemul canonic de date, cercetare și citare

## Surse de adevăr

- `content/`: proza capitolelor în Markdown/MDX;
- `data/`: entități pedagogice structurate;
- `research/sources.json`: metadatele surselor;
- `research/claims.json`: afirmațiile verificabile;
- `research/citations.json`: relația exactă dintre afirmație, sursă și locul utilizării;
- `assets/manifests/`: metadatele activelor vizuale;
- `schemas/`: contractele aplicate înainte de integrare;
- `config/project.json`: invariabilele proiectului.

Fișierele generate din aceste surse se scriu doar în `dist/` și nu devin surse editoriale.

## Identificatori

Prefixele canonice sunt `SRC-`, `CLM-`, `CIT-`, `PRI-`, `EX-`, `SES-`, `MSG-`, `VIS-`, `CH-` și `TASK-`. Identificatorii nu se reutilizează după publicare. Redenumirea necesită migrare explicită a tuturor referințelor.

## Separarea tipurilor de afirmații

Fiecare afirmație declară una dintre categoriile:

- fapt verificabil;
- recomandare oficială;
- rezultat de studiu;
- practică de academie;
- opinie profesională;
- sinteză metodologică a manualului.

Ultimele două nu sunt prezentate drept dovezi externe. O sinteză trebuie să indice materialul pe care îl combină și limitele transferului.

## Citarea exactă

O citare leagă un `claim_id` de un `source_id`, precizează locatorul concret — pagină, secțiune, tabel sau paragraf — și locația din manual. URL-ul unei pagini generale nu este suficient pentru o afirmație precisă. Datele actualizabile includ versiunea verificată și data accesării.

## Fundamentarea mesajului către copil

Orice mesaj, regulă, întrebare, constrângere, feedback sau corecție primește un obiect conform `schemas/message-foundation.schema.json`. Modelul separă:

`problemă → informație observată → interpretare → decizie → execuție → rezultat → reacție`

Fundamentarea include formularea exactă, sensul pentru antrenor, motivul formulării, comportamente observabile, cele șase perspective profesionale, adecvarea la vârstă, formulări de evitat, interpretări greșite, verificarea înțelegerii, intervenția alternativă și transferul în meci.

## Flux de acceptare

1. Sursa este înregistrată și evaluată.
2. Afirmația este formulată la granularitatea pe care sursa o susține.
3. Citarea fixează locatorul și utilizarea.
4. Autorul integrează afirmația fără a depăși limitele.
5. Auditorul factual verifică eșantionat relația.
6. Build-ul respinge referințele lipsă și ID-urile orfane.
