# Unelte operaționale

```powershell
python scripts/research_tool.py add-source --input candidate.json
python scripts/research_tool.py add-source --input candidate.json --file research/source-snapshots/file.pdf
python scripts/research_tool.py add-search --input search.json
python scripts/research_tool.py duplicates
python scripts/research_tool.py freshness --as-of 2026-07-30
python scripts/research_tool.py archive-file --source-id SRC-0001 --file path/to/permitted.pdf
python scripts/migrate_research_v1_to_v2.py
```

`add-source` normalizează autorii, DOI, ISBN și URL-ul, calculează hashul când primește fișier, detectează duplicate certe și nu suprascrie. Potrivirile numai după titlu sunt raportate pentru revizie, nu fuzionate.

`add-search` validează întrebarea și scrie append-only. `freshness` este read-only. `archive-file` copiază numai dacă drepturile permit și refuză suprascrierea.

Toate comenzile emit JSON și cod nenul la eroare. După orice mutație se rulează `python scripts/validate_content.py`.
