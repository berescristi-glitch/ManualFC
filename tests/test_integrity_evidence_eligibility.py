from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def test_published_problems_do_not_use_replaced_claims_or_withdrawn_sources():
    claims = {item["claim_id"]: item for item in load("research/claims.json")["claims"]}
    sources = {item["source_id"]: item for item in load("research/sources.json")["sources"]}
    for problem in load("data/problems/problem-library.json")["problems"]:
        if problem.get("status") != "PUBLISHED":
            continue
        for claim_id in problem.get("evidence_claim_ids", []):
            claim = claims[claim_id]
            assert claim.get("status") not in {"OUTDATED", "WITHDRAWN", "REPLACED"}, (
                f"{problem['problem_id']} uses ineligible {claim_id}"
            )
            assert not [sid for sid in claim.get("source_ids", []) if sources[sid].get("withdrawn")], (
                f"{problem['problem_id']} uses withdrawn evidence through {claim_id}"
            )
