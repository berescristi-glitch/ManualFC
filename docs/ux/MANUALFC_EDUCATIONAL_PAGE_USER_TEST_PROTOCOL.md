# ManualFC — Educational Page User Test Protocol (viitor, neexecutat în acest task)

**Statut:** protocol propus pentru validare umană viitoare. Browser automation (folosit în această fază pentru QA structurală) NU poate dovedi învățare umană reală — vezi distincția explicită de mai jos.

## Distincție obligatorie

- **STRUCTURAL_READINESS** (ce se testează în acest task): pagina se încarcă, ierarhia semantică e corectă, nucleul procedural e găsibil fără JS, toggle-ul funcționează, nu există overflow, tastatura funcționează.
- **HUMAN_VALIDATION_REQUIRED** (ce NU se testează în acest task, cere utilizatori reali): comprehensiune, retenție la 24h, aplicare corectă în teren, calitate percepută.

Niciun rezultat de mai jos nu va fi fabricat sau presupus. Dacă nu a fost rulat cu utilizatori reali, raportul va spune explicit `NOT_YET_RUN`.

## Teste propuse (viitor)

### F1 — Findability
Sarcină: „Găsește ce NU trebuie să presupui despre acest copil." Măsoară: timp, număr de click-uri greșite, succes/eșec.

### F2 — Comprehensiune
Sarcină: „Explică cu cuvintele tale de ce antrenorul spune exact această propoziție, nu alta." Evaluare calitativă a răspunsului.

### F3 — Retenție la 24h
Revenire după 24-48h: „Ce ai reținut din acest capitol fără să-l recitești?" Comparație cu un grup care a văzut doar varianta fără secțiunea Recall rapid.

### F4 — Aplicare
Scenariu nou, neîntâlnit în capitol: „Ce ai face în această situație similară?" Evaluare a transferului.

### F5 — Reference use
Sarcină cronometrată: „Ai citit acest capitol săptămâna trecută. Găsește din nou formularea exactă recomandată." Măsoară eficiența suprafeței de recall rapid.

### F6 — Calitate percepută
Scală Likert scurtă: claritate, încredere, utilitate percepută, dorința de a reveni.

## Limitări onest declarate
- Fără utilizatori reali testați, toate cele șase teste rămân `NOT_YET_RUN`.
- Rezultatele de automatizare browser din auditul de acceptanță (acest task) verifică DOAR structura, nu învățarea.
