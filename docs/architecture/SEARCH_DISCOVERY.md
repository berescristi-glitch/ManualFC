# Search & Discovery — Wave 3

Indexul este construit static din aceleași loadere canonice ca paginile. Căutarea normalizează diacriticele și folosește scor fix: titlu 5, rezumat/observație 3, restul câmpurilor indexate 1. Interfața explică sursa potrivirii.

Tipurile sunt problemă, principiu, exercițiu, ședință, evaluare și capitol. Filtrele expuse sunt tip, efectiv, timp și stare a dovezii; efectivul/timpul elimină tipurile fără metadata în loc să inventeze compatibilitate. Starea fără rezultate oferă reset și întoarcere la observații.

Arhitectura rămâne static-first, fără backend, profilare, vector DB sau colectare de identități. IDs și URLs stabile permit favorite/saved plans ulterior, fără controale moarte acum.
