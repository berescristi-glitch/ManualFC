# Problem Knowledge Graph — Wave 3

Graful canonic este `problem → observation → hypothesis → test → cue → principle → exercise → session → assessment → transfer → evidence → media`. Componentele UI citesc graful prin `app/src/lib/problem-library.ts`; nu codifică relațiile în pagini.

Validatorul fail-closed verifică unicitatea IDs, exact trei flagship-uri și existența țintelor canonice. Relațiile către exercițiu, ședință sau evaluare pot fi goale când produsul nu are încă un artefact legitim; interfața trebuie să spună acest lucru și nu inventează conținut.

Modelul este static-first și fără date personale. IDs stabile permit ulterior selectarea unui test într-un Session Workspace ori o reflecție post-sesiune, fără ca Wave 3 să implementeze conturi sau persistență.
