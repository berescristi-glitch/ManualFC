#!/usr/bin/env python3
"""Validare fail-closed pentru dosarul canonic de safeguarding U11."""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

FORBIDDEN = {
    "ABSOLUTE_CONFIDENTIALITY_PROMISED": (r"\b(?:secretul nostru|nu spun nimănui|confidențialitate absolută)\b",),
    "UNAUTHORIZED_INVESTIGATION_INSTRUCTION": (r"\b(?:anchetează copilul|cere dovezi copilului|confruntă presupusul autor)\b",),
    "CHILD_BLAMING_LANGUAGE": (r"\b(?:e vina ta|ai provocat|de ce n-ai spus mai devreme)\b",),
}
PERSONAL_DATA = (
    re.compile(r"(?<!\d)[1-8]\d{12}(?!\d)"),
    re.compile(r"\b(?:07\d{8})\b"),
)


def _walk_text(value: Any) -> str:
    if isinstance(value, dict):
        return " ".join(_walk_text(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(_walk_text(item) for item in value)
    return value if isinstance(value, str) else ""


def validate_payload(data: dict[str, Any], *, today: date | None = None) -> list[str]:
    errors: list[str] = []
    requirements = data.get("requirements", [])
    risks = data.get("risks", [])
    roles = data.get("roles", [])
    contacts = data.get("contacts", [])
    scripts = data.get("scripts", [])
    instruments = data.get("instruments", [])

    for item in requirements:
        status = item.get("status")
        rid = item.get("requirement_id")
        if status == "LEGAL_REQUIREMENT_ROMANIA" and not item.get("exact_article_or_section"):
            errors.append(f"LEGAL_BASIS_MISSING:{rid}")
        if status in {"FRF_REQUIREMENT", "FIFA_STANDARD", "UEFA_STANDARD"} and not item.get("applies_to"):
            errors.append(f"LEGAL_SCOPE_UNCLEAR:{rid}")
        if item.get("legal_review_required") and not item.get("uncertainty"):
            errors.append(f"LEGAL_REVIEW_REQUIRED:{rid}")
    if not any(role.get("role") == "responsabil safeguarding" for role in roles):
        errors.append("SAFEGUARDING_ROLE_MISSING:roles")
    for role in roles:
        if not role.get("reports_to"):
            errors.append(f"REPORTING_CHANNEL_MISSING:{role.get('role_id')}")
    for risk in risks:
        if not risk.get("preventive_control"):
            errors.append(f"RISK_CONTROL_MISSING:{risk.get('risk_id')}")
    check_date = today or date.today()
    for contact in contacts:
        cid = contact.get("contact_id")
        if not contact.get("verified_at") or not contact.get("source_url"):
            errors.append(f"CONTACT_NOT_VERIFIED:{cid}")
        recheck = contact.get("recheck_at")
        if recheck and date.fromisoformat(recheck) < check_date:
            errors.append(f"CONTACT_RECHECK_OVERDUE:{cid}")
    if not any("recrut" in item.lower() for item in instruments):
        errors.append("SAFE_RECRUITMENT_INCOMPLETE:instruments")
    if not any("vizual" in item.lower() or "imagine" in item.lower() or "fotograf" in item.lower()
               for item in instruments):
        errors.append("VISUAL_CONSENT_UNCLEAR:instruments")
    if not any("deplas" in item.lower() for item in instruments):
        errors.append("TRAVEL_RISK_ASSESSMENT_MISSING:instruments")
    if not any("conduit" in item.lower() or "limite" in item.lower()
               for item in instruments):
        errors.append("PROFESSIONAL_BOUNDARY_UNCLEAR:instruments")
    if len(data.get("situations", [])) != 30:
        errors.append(f"INVALID_VALUE:situations:{len(data.get('situations', []))}")
    if len(scripts) != 10:
        errors.append(f"INVALID_VALUE:scripts:{len(scripts)}")
    if len(instruments) < 20:
        errors.append(f"POLICY_APPROVAL_MISSING:instruments:{len(instruments)}")
    actionable = {
        "requirements": requirements,
        "scripts": [
            {"coach_says": item.get("coach_says"), "coach_action": item.get("coach_action")}
            for item in scripts
        ],
        "situations": [
            {"immediate_action": item.get("immediate_action"), "coach_says": item.get("coach_says")}
            for item in data.get("situations", [])
        ],
    }
    text = _walk_text(actionable).lower()
    for code, patterns in FORBIDDEN.items():
        if any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns):
            errors.append(f"{code}:canonical")
    # Numerele publice ale instituțiilor din lista de contacte sunt permise; restul
    # corpusului canonic nu trebuie să conțină date personale reale.
    scrubbed = _walk_text({k: v for k, v in data.items() if k != "contacts"})
    if any(pattern.search(scrubbed) for pattern in PERSONAL_DATA):
        errors.append("REAL_PERSONAL_DATA_DETECTED:canonical")
    return sorted(set(errors))


def validate(root: Path = ROOT, *, today: date | None = None) -> list[str]:
    schema = json.loads((root / "schemas/safeguarding.schema.json").read_text(encoding="utf-8"))
    data = json.loads((root / "data/safeguarding/canonical.json").read_text(encoding="utf-8"))
    errors = [
        f"SCHEMA_INVALID:{'.'.join(map(str, error.absolute_path))}:{error.message}"
        for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data)
    ]
    errors.extend(validate_payload(data, today=today))
    for name in ("disclosure-response.svg", "escalation.svg", "trusted-adults.svg"):
        path = root / "assets/safeguarding" / name
        if not path.is_file():
            errors.append(f"OUTPUT_MISSING:{path.relative_to(root).as_posix()}")
            continue
        svg = path.read_text(encoding="utf-8")
        if "<title" not in svg or "<desc" not in svg:
            errors.append(f"INVALID_VALUE:{name}:accessibility")
    return sorted(set(errors))


def main() -> int:
    errors = validate()
    if errors:
        print("\n".join(errors))
        return 1
    print("VALID: safeguarding U11 — schemă, controale, contacte și vizualuri")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
