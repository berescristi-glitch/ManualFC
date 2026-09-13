# Politica de versionare a surselor

O versiune nouă primește ID nou. Istoricul nu se suprascrie.

`supersedes_source_id` indică versiunea anterioară, iar aceasta indică noua versiune prin `superseded_by_source_id`. Lanțul trebuie să fie aciclic și bidirecțional. Se înregistrează schimbarea URL-ului, conținutului, versiunii, recomandării, licenței sau statutului.

Pentru fiecare schimbare se notează diferența relevantă, afirmațiile și capitolele afectate și taskurile de actualizare. Două ediții legitime rămân surse separate. Titlul similar nu autorizează fuziunea automată.

O sursă retrasă păstrează metadatele și trece la `WITHDRAWN`. O sursă înlocuită trece la `SUPERSEDED`; afirmațiile afectate sunt reverificate înainte de publicare.
