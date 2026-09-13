#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .git ]; then
  git init
fi

mkdir -p \
  plans research/source-notes content \
  data/{principles,exercises,sessions,season-plans,assessments,communication-scripts,case-studies} \
  assets/{diagrams,diagram-sequences,illustrations,icons,animations} \
  app print tests reports/{task-reports,final-audit} dist

python3 scripts/validate_project.py
echo "Repository pregătit. Deschide rădăcina în Codex și trimite START_CODEX_PROMPT.md."
