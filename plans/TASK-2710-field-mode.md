# TASK-2710 — Field Mode

## Scop și rezultat verificabil

Un mod de teren, activat explicit, care arată un segment de ședință o dată, cu cronometru și navigare cu degetul mare, consumând exclusiv date canonice deja existente (niciun conținut paralel).

## Progres

- [x] Rută nouă `/gold-standard/sedinte/[id]/mod-teren`, activată explicit dintr-un CTA vizibil pe pagina normală de ședință (`Pornește modul teren →`) — nu auto-detectat.
- [x] Un segment pe ecran: timp, titlu, mesaj exact (cue), ce urmărești, tranziție; pentru segmentele cu exercițiu: format/spațiu/materiale + diagrama tactică (reutilizate din datele canonice ale exercițiului), plus regresie/progresie ascunse implicit sub „Ajustează dacă e nevoie” (fără raționale lungi implicit).
- [x] Bară inferioară fixă: Înapoi / Cronometru (Start/Pauză/Reset) / Următorul; toate controalele ≥48px înălțime.
- [x] Cronometru: start/pauză/reset funcțional, persistă la navigarea între segmente (verificat: 00:46 → avansare segment → cronometrul continuă).
- [x] Navigarea principală și subsolul site-ului ascunse doar pe această rută (verificat: nu afectează alte pagini).
- [x] Toate datele provin din `getGoldStandardSession`/`getGoldStandardExercise` — aceeași sursă ca pagina normală de ședință și paginile de exercițiu.

## Defecte reale găsite și reparate în timpul verificării browser

1. **`<main>` dublu imbricat** — pagina folosea propriul `<main>` în interiorul `<main>`-ului deja furnizat de `BaseLayout`, o încălcare de semantică HTML/accesibilitate. Corectat la `<div>`.
2. **Comentariu CSS scăpat în afara `<style>`** — un comentariu plasat greșit deasupra tagului `<style>` apărea ca text vizibil literal pe pagină. Mutat în interiorul blocului `<style>`.
3. **Bara fixă suprapunea conținutul la ≤560px** — la lățimi mobile bara se stivuiește pe 3 rânduri (mult mai înaltă decât presupusese padding-ul inițial de 80px), blocând click-uri pe conținutul din josul unui segment (verificat direct: click pe „Ajustează dacă e nevoie” eșua cu „elementul e interceptat”). Corectat cu padding inferior dedicat la mobil.
4. **Butonul final rămânea activabil** — la ultimul segment textul devenea „Ședință încheiată”, dar butonul nu era dezactivat (inconsecvent cu „Înapoi”, care e corect dezactivat la primul segment). Corectat.

Toate cele 4 au fost găsite prin interacțiune reală în browser (click, scroll, evaluare JS), nu doar prin citirea codului.

## Limită

Nu implementează timp offline/PWA (§34 din specificație — necesită decizie separată, neautorizat aici) și nu persistă starea cronometrului la reîncărcarea paginii (acceptabil explicit — „don't overengineer”). Nu există Field Mode separat per exercițiu individual (în afara unei ședințe) — fluxul acoperă exercițiile prin segmentele ședinței, care e cazul real de utilizare descris în specificație.
