# TASK-2707 — EX-0004/EX-0005 visuals + Field Cards

## Scop și rezultat verificabil

Închide paritatea vizuală pentru EX-0004/EX-0005 (diagramă tactică reală, nu declarația de lipsă) și produce câte o Fișă de teren pentru toate cele 5 exerciții — un ecran de referință lângă teren, fără raționale sau dovezi.

## Progres

- [x] `TacticalDiagram.astro` extins cu variantele `ex-0004`/`ex-0005`, hand-authored SVG, fără poziții inventate ca „ideale”.
- [x] EX-0004: diagramă „grupare instinctivă (fantomă) → diferențiere pe două linii”, direct din `child_message`/`problem_being_solved` canonice.
- [x] EX-0005: diagramă etichetată explicit „un moment reprezentativ posibil, nu o formă obligatorie” — jucătorii neimplicați în decizia arătată sunt puncte estompate, fără poziție prescrisă.
- [x] Pagina de exercițiu (`[id].astro`) randează diagrama pentru toate cele 5 exerciții; nota „fără diagramă” dispare pentru EX-0004/EX-0005.
- [x] Actualizate `docs/architecture/PRESENTATION_LAYER_V2.md` și starea de pe `/gold-standard` — nu mai afirmă că EX-0004/EX-0005 sunt „doar text”.
- [x] `FieldCard.astro` — componentă nouă: titlu, obiectiv, format, spațiu, timp, materiale, diagramă, mesaj exact, ce urmărești, regresie, progresie, link spre pagina completă. Fără raționale, fără cele 7 dimensiuni, fără surse.
- [x] `/gold-standard/fise-de-teren` — toate cele 5 fișe, cu `page-break-after` la print.
- [x] Verificat browser la 1440/390: 0 erori consolă, 0 overflow orizontal.
- [x] Validare locală completă PASS.

## Limită

O fișă de teren ocupă ~1.6 ecrane la 390px (diagramă + toate câmpurile cerute), nu exact un singur ecran — păstrat onest, nu comprimat artificial în detrimentul lizibilității. Fișele rămân static text/SVG; interactivitatea (timer, navigare sticky) e scopul `TASK-2710`.
