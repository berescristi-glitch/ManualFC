#!/usr/bin/env python3
"""Validare fail-closed pentru matricea regulamentelor U11."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def validate(root: Path = ROOT) -> list[str]:
    schema = json.loads((root / "schemas/regulation-rule.schema.json").read_text(encoding="utf-8"))
    data = json.loads((root / "data/regulations/u11-rules.json").read_text(encoding="utf-8"))
    errors = [
        f"schema:{'.'.join(map(str, error.absolute_path))}:{error.message}"
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data)
    ]
    ids = set()
    for index, rule in enumerate(data.get("rules", [])):
        rid = rule.get("rule_id")
        if rid in ids:
            errors.append(f"duplicate:{rid}")
        ids.add(rid)
        for field in ("field_length_m", "field_width_m"):
            value = rule.get(field)
            if value and value["min"] > value["max"]:
                errors.append(f"range:{rid}:{field}:min>max")
        if rule.get("category_kind") != "MATCH_REGULATION" and rule.get("status") in {
            "CURRENT_CONFIRMED", "CURRENT_LOCAL_CONFIRMED"
        }:
            errors.append(f"category:{rid}:non-match marked confirmed regulation")
        if rule.get("status") in {"CURRENT_CONFIRMED", "CURRENT_LOCAL_CONFIRMED"}:
            if not rule.get("source_id") or not rule.get("exact_locations"):
                errors.append(f"evidence:{rid}:confirmed without source/location")
        if rule.get("jurisdiction") == "OTHER_AJF_COMPARATIVE" and rule.get("status") == "CURRENT_LOCAL_CONFIRMED":
            errors.append(f"jurisdiction:{rid}:comparative source marked Satu Mare local")
    space = json.loads((root / "data/regulations/u11-space-per-player.json").read_text(encoding="utf-8"))
    by_id = {item["rule_id"]: item for item in data["rules"]}
    for row in space["rows"]:
        rule = by_id.get(row["rule_id"])
        if not rule:
            errors.append(f"space:{row['rule_id']}:unknown rule")
            continue
        expected_area = rule["field_length_m"]["min"] * rule["field_width_m"]["min"]
        expected_players = 2 * rule["players_on_field"]
        if row["area_m2"] != expected_area:
            errors.append(f"space:{row['rule_id']}:area")
        if row["total_players_including_goalkeepers"] != expected_players:
            errors.append(f"space:{row['rule_id']}:players")
        if abs(row["area_per_player_m2"] - round(expected_area / expected_players, 2)) > 0.001:
            errors.append(f"space:{row['rule_id']}:area-per-player")
    return sorted(errors)


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors))
        return 1
    print("VALID: matrice regulamente și calcule descriptive")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
