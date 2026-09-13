#!/usr/bin/env python3
"""Validează fundația persistentă a proiectului fără dependențe externe."""
from __future__ import annotations

from collections import Counter, deque
from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
ERRORS: list[str] = []
WARNINGS: list[str] = []

REQUIRED = [
    "AGENTS.md", "CODEX.md", "PLANS.md", "MASTER_EXECUTION_PROMPT.md",
    "TASK_REGISTRY.json", "TASK_HISTORY.jsonl", "PROJECT_STATUS.md", "DECISIONS.md",
    "plans/TASK-0001-initializare-arhitectura.md",
    "docs/EDITORIAL_STYLE_GUIDE.md", "docs/RESEARCH_PROTOCOL.md",
    "docs/VISUAL_INTERACTIVE_STANDARD.md", "docs/QUALITY_GATES.md",
    "docs/architecture/ADR-0001-STACK-SI-FLUX-DATE.md",
    "docs/architecture/DATA_AND_CITATION_SYSTEM.md",
    "docs/architecture/VISUAL_SYSTEM.md",
    "docs/architecture/BUILD_AND_TEST_STRATEGY.md",
    "schemas/task.schema.json", "schemas/principle.schema.json",
    "schemas/exercise.schema.json", "schemas/session.schema.json",
    "schemas/source-registry.schema.json", "schemas/claim-registry.schema.json",
    "schemas/citation-registry.schema.json", "schemas/message-foundation.schema.json",
    "schemas/visual-asset.schema.json", "schemas/project.schema.json",
    "config/project.json", "config/visual-tokens.json",
    "research/sources.json", "research/claims.json", "research/citations.json",
    "scripts/validate_content.py", "scripts/validation/codes.py",
    "docs/architecture/VALIDATION_SYSTEM.md", "requirements-dev.txt",
]

ALLOWED_STATUS = {
    "PENDING", "READY", "IN_PROGRESS", "BLOCKED", "VALIDATING",
    "REPAIR_REQUIRED", "DONE", "FAILED_CRITICAL",
}
REQUIRED_TASK_FIELDS = {
    "task_id", "title", "phase", "status", "priority", "dependencies", "outputs",
    "acceptance_criteria", "validation_commands", "weight_percent", "attempts", "max_attempts",
}


def load_json(relative: str) -> dict:
    try:
        return json.loads((ROOT / relative).read_text(encoding="utf-8"))
    except Exception as exc:
        ERRORS.append(f"{relative} nu poate fi citit ca JSON UTF-8: {exc}")
        return {}


for relative in REQUIRED:
    if not (ROOT / relative).exists():
        ERRORS.append(f"Lipsește fișierul obligatoriu: {relative}")

for path in (ROOT / "schemas").glob("*.json"):
    load_json(str(path.relative_to(ROOT)))

project = load_json("config/project.json")
age = project.get("age_category", {})
if age.get("birth_years") != [2015, 2016] or age.get("single_curriculum") is not True:
    ERRORS.append("Configurația proiectului trebuie să păstreze 2015 și 2016 într-o singură categorie.")
minimums = project.get("minimum_deliverables", {})
for key, minimum in {"volumes": 10, "exercises": 60, "sessions": 36, "communication_scripts": 50, "case_studies": 15}.items():
    if minimums.get(key, 0) < minimum:
        ERRORS.append(f"Pragul {key} este sub minimul canonic {minimum}.")

sources = load_json("research/sources.json").get("sources", [])
claims = load_json("research/claims.json").get("claims", [])
citations = load_json("research/citations.json").get("citations", [])
source_ids = [item.get("source_id") for item in sources]
claim_ids = [item.get("claim_id") for item in claims]
if len(source_ids) != len(set(source_ids)):
    ERRORS.append("Registrul surselor conține ID-uri duplicate.")
if len(claim_ids) != len(set(claim_ids)):
    ERRORS.append("Registrul afirmațiilor conține ID-uri duplicate.")
for citation in citations:
    if citation.get("source_id") not in source_ids:
        ERRORS.append(f"Citare cu sursă orfană: {citation.get('citation_id')}.")
    if citation.get("claim_id") not in claim_ids:
        ERRORS.append(f"Citare cu afirmație orfană: {citation.get('citation_id')}.")

registry = load_json("TASK_REGISTRY.json")
tasks = registry.get("tasks", [])
ids = [task.get("task_id") for task in tasks]
known = set(ids)
if len(ids) != len(known):
    ERRORS.append("TASK_REGISTRY.json conține ID-uri duplicate.")
if len(tasks) < 100:
    ERRORS.append("Registrul nu este suficient de granular pentru întregul proiect.")
if abs(sum(float(task.get("weight_percent", 0)) for task in tasks) - 100) > 0.0001:
    ERRORS.append("Suma weight_percent trebuie să fie 100.")

for task in tasks:
    tid = task.get("task_id")
    missing = REQUIRED_TASK_FIELDS - set(task)
    if missing:
        ERRORS.append(f"{tid} nu are câmpurile: {sorted(missing)}")
    if not re.fullmatch(r"TASK-\d{4}", tid or ""):
        ERRORS.append(f"ID de task invalid: {tid}")
    if task.get("status") not in ALLOWED_STATUS:
        ERRORS.append(f"Status invalid pentru {tid}: {task.get('status')}")
    unknown = [dep for dep in task.get("dependencies", []) if dep not in known]
    if unknown:
        ERRORS.append(f"{tid} are dependențe necunoscute: {unknown}")
    if tid in task.get("dependencies", []):
        ERRORS.append(f"{tid} depinde de el însuși.")
    if not task.get("outputs") or not task.get("acceptance_criteria"):
        ERRORS.append(f"{tid} nu are outputuri sau criterii de acceptare.")
    if task.get("weight_percent", 0) <= 0:
        ERRORS.append(f"{tid} trebuie să aibă pondere pozitivă.")
    if task.get("status") == "DONE":
        missing_outputs = [item for item in task["outputs"] if not (ROOT / item).exists()]
        if missing_outputs:
            ERRORS.append(f"{tid} este DONE, dar lipsesc outputuri: {missing_outputs}")
        if not task.get("completed_at"):
            ERRORS.append(f"{tid} este DONE fără completed_at.")
    if task.get("status") == "READY":
        unfinished = [dep for dep in task["dependencies"] if next(t for t in tasks if t["task_id"] == dep)["status"] != "DONE"]
        if unfinished:
            ERRORS.append(f"{tid} este READY cu dependențe neînchise: {unfinished}")

# Kahn: graful taskurilor trebuie să fie aciclic.
indegree = {tid: 0 for tid in ids}
children = {tid: [] for tid in ids}
for task in tasks:
    for dep in task.get("dependencies", []):
        indegree[task["task_id"]] += 1
        children[dep].append(task["task_id"])
queue = deque(tid for tid, degree in indegree.items() if degree == 0)
visited = 0
while queue:
    current = queue.popleft()
    visited += 1
    for child in children[current]:
        indegree[child] -= 1
        if indegree[child] == 0:
            queue.append(child)
if visited != len(tasks):
    ERRORS.append("Graful dependențelor conține cel puțin un ciclu.")

# Pragurile cantitative trebuie să fie acoperite explicit de taskuri.
titles = " ".join(task.get("title", "") for task in tasks)
exercise_count = sum(4 for task in tasks if re.match(r"Lot exerciții \d+ — 4 exerciții", task.get("title", "")))
session_count = sum(2 for task in tasks if re.match(r"Lot ședințe \d+ — 2 ședințe", task.get("title", "")))
script_count = sum(5 for task in tasks if "5 scripturi" in task.get("title", ""))
case_count = sum(3 for task in tasks if "3 scenarii" in task.get("title", ""))
for label, actual, expected in [
    ("exerciții", exercise_count, 60), ("ședințe", session_count, 36),
    ("scripturi", script_count, 50), ("studii de caz", case_count, 15),
]:
    if actual < expected:
        ERRORS.append(f"Registrul planifică doar {actual} {label}; minimul este {expected}.")

placeholder_patterns = [r"\bTODO\b", r"\bTBD\b", r"lorem ipsum"]
scan_dirs = [ROOT / "content", ROOT / "data", ROOT / "app"]
for base in scan_dirs:
    if not base.exists():
        continue
    for path in base.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".mdx", ".json", ".yaml", ".yml", ".ts", ".tsx", ".js", ".html"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                ERRORS.append(f"Fișierul nu este UTF-8: {path.relative_to(ROOT)}")
                continue
            for pattern in placeholder_patterns:
                if re.search(pattern, text, flags=re.IGNORECASE):
                    WARNINGS.append(f"Posibil placeholder în {path.relative_to(ROOT)}: {pattern}")

content_validation = subprocess.run(
    [sys.executable, str(ROOT / "scripts" / "validate_content.py"), "--format", "human"],
    cwd=ROOT, capture_output=True, text=True, encoding="utf-8"
)
if content_validation.returncode:
    ERRORS.append("Validatorul canonic de conținut a eșuat:\n" + content_validation.stdout.strip())

status_counts = Counter(task.get("status") for task in tasks)
print("=== Validare proiect ===")
print(f"Taskuri: {len(tasks)}; stări: {dict(status_counts)}")
print(f"Planificat: {exercise_count} exerciții, {session_count} ședințe, {script_count} scripturi, {case_count} studii de caz")
for warning in WARNINGS:
    print(f"WARNING: {warning}")
for error in ERRORS:
    print(f"ERROR: {error}")
print(f"Rezultat: {len(ERRORS)} erori, {len(WARNINGS)} avertismente")
sys.exit(1 if ERRORS else 0)
