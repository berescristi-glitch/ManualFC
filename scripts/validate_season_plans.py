#!/usr/bin/env python3
"""Validator dedicat pentru pilonul de planificare de sezon (TASK-3720).

Verifica, pentru fiecare `data/curriculum/curriculum-*.json` si fiecare
`data/season-plans/season-plan-*.json`, ca fiecare ID referentiat
(principle_ids, related_problem_ids, related_exercise_ids,
related_session_ids, related_script_ids, curriculum_ids) exista cu adevarat
in sursele canonice ale proiectului -- niciun ID inventat -- si ca nu exista
ID-uri BLK-/MIC- duplicate intre documente (acestea sunt imbricate in
blocks/microcycles, deci nu sunt indexate generic de validate_content.py).

Strict aditiv fata de `validate_content.py` (care verifica deja schema JSON
si, generic, referintele in format PREFIX-XXXX gasite la orice adancime).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def real_principle_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/principles").glob("*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def real_problem_ids() -> set[str]:
    data = load_json(ROOT / "data/problems/problem-library.json")
    return {p["problem_id"] for p in data.get("problems", []) if "problem_id" in p}


def real_exercise_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/exercises").glob("exercise-*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def real_session_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/sessions").glob("session-*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def real_script_ids() -> set[str]:
    ids: set[str] = set()
    for f in (ROOT / "data/communication-scripts").glob("script-*.json"):
        data = load_json(f)
        if "id" in data:
            ids.add(data["id"])
    return ids


def main() -> int:
    errors: list[str] = []

    principle_ids = real_principle_ids()
    problem_ids = real_problem_ids()
    exercise_ids = real_exercise_ids()
    session_ids = real_session_ids()
    script_ids = real_script_ids()

    curriculum_files = sorted((ROOT / "data/curriculum").glob("curriculum-*.json"))
    plan_files = sorted((ROOT / "data/season-plans").glob("season-plan-*.json"))

    seen_cur_ids: set[str] = set()
    seen_blk_ids: set[str] = set()
    real_cur_ids: set[str] = set()

    for f in curriculum_files:
        data = load_json(f)
        cid = data.get("id", f.name)
        if cid in seen_cur_ids:
            errors.append(f"{cid}: id de curriculum duplicat intre fisiere.")
        seen_cur_ids.add(cid)
        real_cur_ids.add(cid)

        for block in data.get("blocks", []):
            bid = block.get("id", "?")
            if bid in seen_blk_ids:
                errors.append(f"{cid}/{bid}: id de bloc (BLK-) duplicat intre curricula.")
            seen_blk_ids.add(bid)

            for pid in block.get("principle_ids", []):
                if pid not in principle_ids:
                    errors.append(f"{cid}/{bid}: principle_ids contine \"{pid}\", care nu exista in data/principles/.")
            for sid in block.get("session_ids", []):
                if sid not in session_ids:
                    errors.append(f"{cid}/{bid}: session_ids contine \"{sid}\", care nu exista in data/sessions/.")
            for prb in block.get("related_problem_ids", []):
                if prb not in problem_ids:
                    errors.append(f"{cid}/{bid}: related_problem_ids contine \"{prb}\", care nu exista in problem-library.json.")

    seen_plan_ids: set[str] = set()
    seen_plan_slugs: set[str] = set()
    seen_mic_ids: set[str] = set()

    for f in plan_files:
        data = load_json(f)
        pid_doc = data.get("id", f.name)

        if pid_doc in seen_plan_ids:
            errors.append(f"{pid_doc}: id de plan duplicat intre fisiere.")
        seen_plan_ids.add(pid_doc)

        slug = data.get("slug")
        if slug in seen_plan_slugs:
            errors.append(f"{pid_doc}: slug duplicat (\"{slug}\").")
        if slug:
            seen_plan_slugs.add(slug)

        for cur in data.get("curriculum_ids", []):
            if cur not in real_cur_ids:
                errors.append(f"{pid_doc}: curriculum_ids contine \"{cur}\", care nu exista in data/curriculum/.")

        for pid in data.get("principle_ids", []):
            if pid not in principle_ids:
                errors.append(f"{pid_doc}: principle_ids contine \"{pid}\", care nu exista in data/principles/.")
        for prb in data.get("related_problem_ids", []):
            if prb not in problem_ids:
                errors.append(f"{pid_doc}: related_problem_ids contine \"{prb}\", care nu exista in problem-library.json.")
        for ex in data.get("related_exercise_ids", []):
            if ex not in exercise_ids:
                errors.append(f"{pid_doc}: related_exercise_ids contine \"{ex}\", care nu exista in data/exercises/.")
        for ses in data.get("related_session_ids", []):
            if ses not in session_ids:
                errors.append(f"{pid_doc}: related_session_ids contine \"{ses}\", care nu exista in data/sessions/.")
        for scr in data.get("related_script_ids", []):
            if scr not in script_ids:
                errors.append(f"{pid_doc}: related_script_ids contine \"{scr}\", care nu exista in data/communication-scripts/.")

        plan_session_ids: set[str] = set()
        for mic in data.get("microcycles", []):
            mid = mic.get("id", "?")
            if mid in seen_mic_ids:
                errors.append(f"{pid_doc}/{mid}: id de microciclu (MIC-) duplicat intre planuri.")
            seen_mic_ids.add(mid)

            for sid in mic.get("session_ids", []):
                plan_session_ids.add(sid)
                if sid not in session_ids:
                    errors.append(f"{pid_doc}/{mid}: session_ids contine \"{sid}\", care nu exista in data/sessions/.")
            for scr in mic.get("related_script_ids", []):
                if scr not in script_ids:
                    errors.append(f"{pid_doc}/{mid}: related_script_ids contine \"{scr}\", care nu exista in data/communication-scripts/.")

        declared_sessions = set(data.get("related_session_ids", []))
        missing_from_declared = plan_session_ids - declared_sessions
        if missing_from_declared:
            errors.append(f"{pid_doc}: microciclurile folosesc sedinte ({sorted(missing_from_declared)}) absente din related_session_ids de la nivel de plan.")

    for err in errors:
        print(f"ERROR {err}", file=sys.stderr)

    print(f"Planificare de sezon: {len(curriculum_files)} curricula, {len(plan_files)} planuri verificate.")
    if errors:
        print(f"Rezultat: {len(errors)} erori")
        return 1
    print("Rezultat: 0 erori")
    return 0


if __name__ == "__main__":
    sys.exit(main())
