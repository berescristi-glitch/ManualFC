#!/usr/bin/env python3
"""Validator Gold Standard V2 (PHASE-33, TASK-3502).

Verifica, DOAR pentru exercitiile/sedintele marcate explicit
`gold_standard_v2.status == "V2"`, ca toate legaturile semantice cerute de
specificatia PHASE-33 sectiunea 8/20 sunt prezente, nevide, si ca fiecare
ID referentiat (PED-Cxx, COACH-Cxx, CH-xxxx, principle.*, ASM-xxxx) exista
cu adevarat in sursele canonice ale proiectului -- niciun ID inventat.

Obiecte V1 (fara `gold_standard_v2` sau cu status "V1") nu sunt afectate.
Acest script este strict aditiv fata de `validate_content.py` (care verifica
deja conformitatea cu schema JSON) -- verifica completitudine semantica,
nu forma JSON.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_EXERCISE_V2_FIELDS = [
    "pedagogical_principle_ids",
    "pedagog_competency_ids",
    "coach_competency_ids",
    "child_action",
    "coach_focus",
    "do_not_assume",
    "when_to_intervene",
    "when_not_to_intervene",
    "coach_common_errors",
    "coach_reflection",
    "evidence_boundary",
    "assessment_ref",
]

REQUIRED_SESSION_V2_FIELDS = [
    "child_objectives",
    "coach_objectives",
    "reflection_v2",
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def real_ped_competency_ids() -> set[str]:
    text = (ROOT / "docs/knowledge/PEDAGOG_COMPETENCY_FRAMEWORK.md").read_text(encoding="utf-8")
    return set(re.findall(r"PED-C\d{2}", text))


def real_coach_competency_ids() -> set[str]:
    text = (ROOT / "docs/knowledge/COACH_COMPETENCY_FRAMEWORK.md").read_text(encoding="utf-8")
    return set(re.findall(r"COACH-C\d{2}", text))


def real_chapter_ids() -> set[str]:
    ids: set[str] = set()
    for mdx in (ROOT / "content").glob("volume-*/chapter-*.mdx"):
        text = mdx.read_text(encoding="utf-8")
        m = re.search(r'chapter_id:\s*"([^"]+)"', text)
        if m:
            ids.add(m.group(1))
    return ids


def real_principle_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/principles").glob("*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def real_assessment_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/assessments").glob("*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    ped_ids = real_ped_competency_ids()
    coach_ids = real_coach_competency_ids()
    chapter_ids = real_chapter_ids()
    principle_ids = real_principle_ids()
    assessment_ids = real_assessment_ids()

    exercise_files = sorted((ROOT / "data/exercises").glob("exercise-*.json"))
    session_files = sorted((ROOT / "data/sessions").glob("session-*.json"))

    v2_exercise_count = 0
    for f in exercise_files:
        data = load_json(f)
        v2 = data.get("gold_standard_v2")
        if not v2 or v2.get("status") != "V2":
            continue
        v2_exercise_count += 1
        eid = data.get("id", f.name)

        for field in REQUIRED_EXERCISE_V2_FIELDS:
            value = data.get(field)
            if value is None or value == "" or value == []:
                errors.append(f"{eid}: campul V2 obligatoriu \"{field}\" lipseste sau e gol.")

        for pid in data.get("pedagog_competency_ids", []):
            if pid not in ped_ids:
                errors.append(f"{eid}: pedagog_competency_ids contine \"{pid}\", care nu exista in PEDAGOG_COMPETENCY_FRAMEWORK.md.")
        for cid in data.get("coach_competency_ids", []):
            if cid not in coach_ids:
                errors.append(f"{eid}: coach_competency_ids contine \"{cid}\", care nu exista in COACH_COMPETENCY_FRAMEWORK.md.")
        for lid in data.get("related_pedagog_lesson_ids", []) + data.get("related_coach_lesson_ids", []):
            if lid not in chapter_ids:
                errors.append(f"{eid}: o referinta de capitol (\"{lid}\") nu corespunde niciunui chapter_id real din content/.")
        for prid in data.get("pedagogical_principle_ids", []):
            if prid not in principle_ids:
                errors.append(f"{eid}: pedagogical_principle_ids contine \"{prid}\", care nu exista in data/principles/.")
        aref = data.get("assessment_ref")
        if aref and aref not in assessment_ids:
            errors.append(f"{eid}: assessment_ref \"{aref}\" nu corespunde niciunui fisier real din data/assessments/.")

        if not data.get("related_pedagog_lesson_ids") and not data.get("related_coach_lesson_ids"):
            warnings.append(f"{eid}: nicio legatura de capitol (nici pedagog, nici coach) -- verifica daca e intentionat.")

    v2_session_count = 0
    for f in session_files:
        data = load_json(f)
        v2 = data.get("gold_standard_v2")
        if not v2 or v2.get("status") != "V2":
            continue
        v2_session_count += 1
        sid = data.get("id", f.name)

        for field in REQUIRED_SESSION_V2_FIELDS:
            value = data.get(field)
            if value is None or value == "" or value == []:
                errors.append(f"{sid}: campul V2 obligatoriu \"{field}\" lipseste sau e gol.")

        for co in data.get("coach_objectives", []):
            cid = co.get("coach_competency_id")
            if cid and cid not in coach_ids:
                errors.append(f"{sid}: coach_objectives contine coach_competency_id \"{cid}\", care nu exista in COACH_COMPETENCY_FRAMEWORK.md.")

        rv2 = data.get("reflection_v2") or {}
        if not rv2.get("child_game_dimension"):
            errors.append(f"{sid}: reflection_v2.child_game_dimension lipseste sau e gol.")
        if not rv2.get("coach_dimension"):
            errors.append(f"{sid}: reflection_v2.coach_dimension lipseste sau e gol.")

    for err in errors:
        print(f"ERROR {err}", file=sys.stderr)
    for warn in warnings:
        print(f"WARN {warn}", file=sys.stderr)

    print(f"Gold Standard V2: {v2_exercise_count} exercitii V2, {v2_session_count} sedinte V2 verificate.")
    if errors:
        print(f"Rezultat: {len(errors)} erori, {len(warnings)} avertismente")
        return 1
    print(f"Rezultat: 0 erori, {len(warnings)} avertismente")
    return 0


if __name__ == "__main__":
    sys.exit(main())
