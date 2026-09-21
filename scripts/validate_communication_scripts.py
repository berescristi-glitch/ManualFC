#!/usr/bin/env python3
"""Validator dedicat pentru biblioteca de scripturi de comunicare (TASK-3719).

Verifica, pentru fiecare fisier `data/communication-scripts/script-*.json`,
ca fiecare ID referentiat (principle_ids, related_problem_ids,
related_exercise_ids, related_session_ids, source_claim_ids) exista cu
adevarat in sursele canonice ale proiectului -- niciun ID inventat.

Strict aditiv fata de `validate_content.py` (care verifica deja schema JSON
si completitudinea campurilor pedagogice) -- verifica doar rezolvarea reala
a referintelor incrucisate, ceva ce `validate_content.py` nu poate face
pentru campul `principle_ids` (format `principle.<slug>`, care nu se
potriveste modelului generic PREFIX-XXXX verificat acolo).
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


def real_claim_ids() -> set[str]:
    data = load_json(ROOT / "research/claims.json")
    return {c["claim_id"] for c in data.get("claims", []) if "claim_id" in c and not c.get("withdrawn", False)}


def main() -> int:
    errors: list[str] = []

    principle_ids = real_principle_ids()
    problem_ids = real_problem_ids()
    exercise_ids = real_exercise_ids()
    session_ids = real_session_ids()
    claim_ids = real_claim_ids()

    script_files = sorted((ROOT / "data/communication-scripts").glob("script-*.json"))
    seen_ids: set[str] = set()
    seen_slugs: set[str] = set()

    for f in script_files:
        data = load_json(f)
        sid = data.get("id", f.name)

        if sid in seen_ids:
            errors.append(f"{sid}: id duplicat intre fisierele de scripturi.")
        seen_ids.add(sid)

        slug = data.get("slug")
        if slug in seen_slugs:
            errors.append(f"{sid}: slug duplicat (\"{slug}\").")
        if slug:
            seen_slugs.add(slug)

        for pid in data.get("principle_ids", []):
            if pid not in principle_ids:
                errors.append(f"{sid}: principle_ids contine \"{pid}\", care nu exista in data/principles/.")

        for prb in data.get("related_problem_ids", []):
            if prb not in problem_ids:
                errors.append(f"{sid}: related_problem_ids contine \"{prb}\", care nu exista in problem-library.json.")

        for ex in data.get("related_exercise_ids", []):
            if ex not in exercise_ids:
                errors.append(f"{sid}: related_exercise_ids contine \"{ex}\", care nu exista in data/exercises/.")

        for ses in data.get("related_session_ids", []):
            if ses not in session_ids:
                errors.append(f"{sid}: related_session_ids contine \"{ses}\", care nu exista in data/sessions/.")

        for clm in data.get("source_claim_ids", []):
            if clm not in claim_ids:
                errors.append(f"{sid}: source_claim_ids contine \"{clm}\", care nu exista sau e retras in research/claims.json.")

    for err in errors:
        print(f"ERROR {err}", file=sys.stderr)

    print(f"Scripturi de comunicare: {len(script_files)} fisiere verificate.")
    if errors:
        print(f"Rezultat: {len(errors)} erori")
        return 1
    print("Rezultat: 0 erori")
    return 0


if __name__ == "__main__":
    sys.exit(main())
