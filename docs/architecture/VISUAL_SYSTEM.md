# Sistemul vizual canonic

Standardul normativ rămâne `docs/VISUAL_INTERACTIVE_STANDARD.md`. Acest document stabilește implementarea.

## Artefacte și directoare

- `assets/diagrams/`: SVG-urile statice finale;
- `assets/diagram-sequences/`: cadrele statice pentru situații dinamice și PDF;
- `assets/animations/`: datele de stare și traseele, nu video opac;
- `assets/editable/`: sursele editabile;
- `assets/manifests/`: câte un manifest conform schemei pentru fiecare set vizual;
- `config/visual-tokens.json`: culori, forme, linii și marcaje canonice.

## Regula de paritate

O situație dinamică nu este acceptată dacă animația transmite informație absentă din cadrele PDF. Manifestul enumeră stările, declanșatorul, traseele, explicația și cadrele echivalente.

## Accesibilitate

Culoarea dublează, nu înlocuiește, rolul. Jucătorii au formă, cod și etichetă; traseele au tipuri de linie; SVG-ul are `title`, `desc` și ordine semantică. Interactivitatea oferă tastatură, focus vizibil, oprirea mișcării și respectă `prefers-reduced-motion`.

## Validare

Validarea automată verifică manifestul, identificatorii, fișierele referite și elementele accesibile. Auditul vizual verifică desktop, telefon, zoom 200%, print color și alb-negru. Dimensiunile tactice sunt date, nu desenate aproximativ în UI.
