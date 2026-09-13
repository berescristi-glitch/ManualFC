# Mesaje de lucru pentru Codex

Nu retrimite master promptul la fiecare task. Instrucțiunile stabile sunt deja în repository.

## A. Continuarea normală — un task

```text
Citește AGENTS.md, starea persistentă și ExecPlan-ul relevant. Selectează următorul task READY din TASK_REGISTRY.json, cu prioritatea și dependențele corecte. Execută exact un task principal până la validare completă. Actualizează toate fișierele de stare și raportul taskului. Nu începe un al doilea task principal în aceeași execuție. La final indică dovezile, validările, problemele rămase și următorul task READY.
```

## B. Task de capitol

```text
Execută taskul <TASK-ID>. Construiește capitolul ca livrabil publicabil, nu ca schiță. Respectă fundamentarea „ce îi spun copilului și de ce”, cercetarea, stilul editorial, imaginile planificate și schemele de date. Rulează auditul factual, pedagogic și editorial. Nu marca DONE până când fișierele, citările și validările există.
```

## C. Task de exerciții

```text
Execută taskul <TASK-ID> și livrează numai lotul declarat de 3–5 exerciții. Fiecare exercițiu trebuie să treacă schema, să conțină dimensiuni justificate, diagramă SVG, animație sau storyboard, fundamentarea completă a mesajelor și transferul în joc. Verifică montarea practică, siguranța, timpul activ și coerența dintre date, imagine și text.
```

## D. Task de ședințe

```text
Execută taskul <TASK-ID> pentru 1–2 ședințe complete. Justifică ordinea fiecărei părți, durata, tranzițiile logistice și mesajele. Verifică faptul că ședința formează o progresie și că jocul final testează transferul fără dependență de constrângeri artificiale.
```

## E. Revizie independentă într-un chat Codex nou

```text
Acționează ca auditor independent. Nu rescrie imediat. Citește AGENTS.md, CODEX.md, standardele și outputurile taskului <TASK-ID>. Verifică separat: factualitatea și sursele, adecvarea la 10–11 ani, coerența metodologică, justificarea fiecărei sarcini, fezabilitatea exercițiilor, consistența vizuală și calitatea limbii române. Creează un raport cu severitate, dovezi și recomandări. Deschide taskuri de reparare pentru problemele reale. Nu aproba materialul doar pentru că este complet ca volum.
```

## F. Reparare

```text
Execută taskul de reparare <TASK-ID>. Pornește de la raportul de audit și remediază doar problemele confirmate. Nu ascunde limitările și nu introduce schimbări fără legătură. Rulează din nou toate validările afectate și înregistrează diferențele.
```

## G. Revizie editorială anti-șablon

```text
Revizuiește outputurile taskului <TASK-ID> conform docs/EDITORIAL_STYLE_GUIDE.md. Nu încerca să păcălești detectoare de AI. Elimină repetițiile, frazele ceremoniale, simetria artificială, abstracțiile fără exemple și explicațiile circulare. Păstrează faptele, citările și sensul pedagogic. Textul final trebuie să fie concret, natural în română și recognoscibil ca voce editorială unitară.
```

## H. Audit de volum

```text
Auditează integral Volumul <N>. Verifică acoperirea cuprinsului, lipsa repetițiilor între capitole, coerența termenilor, citările, legăturile, exemplele, imaginile, accesibilitatea și instrumentele practice. Creează taskuri de reparare pentru toate problemele de severitate critică sau mare. Volumul nu este aprobat până la închiderea lor.
```

## I. Build și audit final

```text
Execută faza finală conform MASTER_EXECUTION_PROMPT.md. Generează build-ul web, PDF-ul, resursele editabile și arhiva. Testează arhiva într-un director curat. Rulează toate validările, verifică vizual pagini reprezentative și diagramele, calculează hashurile și generează FINAL_REPORT.md. Nu emite PASS dacă există placeholder-e, resurse lipsă, erori de navigare, pagini PDF defecte sau taskuri obligatorii neînchise.
```
