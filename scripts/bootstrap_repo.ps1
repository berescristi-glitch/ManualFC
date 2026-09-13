$ErrorActionPreference = "Stop"

if (-not (Test-Path .git)) {
    git init
}

$folders = @(
    "plans",
    "research/source-notes",
    "content",
    "data/principles",
    "data/exercises",
    "data/sessions",
    "data/season-plans",
    "data/assessments",
    "data/communication-scripts",
    "data/case-studies",
    "assets/diagrams",
    "assets/diagram-sequences",
    "assets/illustrations",
    "assets/icons",
    "assets/animations",
    "app",
    "print",
    "tests",
    "reports/task-reports",
    "reports/final-audit",
    "dist"
)

foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder | Out-Null
}

python scripts/validate_project.py
Write-Host "Repository pregătit. Deschide rădăcina în Codex și trimite START_CODEX_PROMPT.md."
