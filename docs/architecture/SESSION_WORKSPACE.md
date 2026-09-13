# Session Workspace — contract de domeniu

## Scop

Workspace-ul Wave-4 leagă descoperirea unei probleme de pregătirea unei ședințe, fără cont obligatoriu și fără un model de date despre copii. Este un instrument al antrenorului, nu un registru al lotului.

## Sursa adevărului

Conținutul pedagogic rămâne în fișierele canonice din `data/`. Starea personală păstrează exclusiv `id`, `kind`, `href`, eticheta de afișare, ordinea și configurația de lucru. Titlul din referință este un label de interfață; nu este o copie a metodologiei. La deschiderea constructorului, referințele sunt reconciliate cu catalogul construit, iar ID-urile dispărute sunt eliminate.

## Port și adapter

`CoachStatePort` expune `read` și `write`. Adapterul anonim folosește cheia versionată `manualfc.coach-state.v1` din `localStorage`. Comenzile UI depind de port, astfel încât sincronizarea viitoare cu un cont să poată înlocui adapterul, nu domeniul și paginile.

`read()` normalizează starea persistată la limita adapterului: JSON invalid, `version` diferit de 1, sau câmpuri corupte (`null`, tip greșit, sesiuni malformate, efectiv/durată/antrenori în afara intervalului) revin fail-closed la valori implicite sigure, fără să propage verificări defensive în componentele UI. Verificat prin injecție directă de stare coruptă în browser (10 scenarii), fără erori de consolă și fără stare fabricată.

Starea conține:

- preferințe de pornire: experiență auto-declarată, efectiv uzual și 60/75 minute;
- referințe salvate, favorite și ultimele 12 repere vizitate;
- ședințe proprii cu problemă-țintă opțională, efectiv 8–18, 1/2 antrenori, ordine, minute și notițe;
- ID-ul ședinței active pentru continuitate.

## Invariante

- Nu există câmpuri pentru nume, contact, sănătate, dată de naștere sau evaluarea nominală a copiilor.
- O ședință se salvează numai cu cel puțin un reper canonic valid.
- Suma blocurilor nu poate depăși durata aleasă.
- Reordonarea este accesibilă prin butoane, fără dependență de drag-and-drop.
- `Salvate`, `Favorite`, `Recente` și `Continuă` se reconstruiesc după reload din aceeași stare versionată.
- Ștergerea datelor browserului elimină starea anonimă; nu există încă backup sau sincronizare cloud.

## Limite Wave-4

Notițele sunt text liber și includ un avertisment explicit împotriva PII. Entitlement, conturile și sincronizarea sunt doar limite arhitecturale pentru un task ulterior. Conflict resolution multi-device nu este pretins.
