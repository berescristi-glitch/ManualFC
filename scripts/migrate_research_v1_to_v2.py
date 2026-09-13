#!/usr/bin/env python3
"""Migrare explicită și idempotentă a registrelor de cercetare v1 la v2."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from research_tool import write_json_atomic

ROOT = Path(__file__).resolve().parents[1]


def migrate_empty_registry(path: Path, collection: str) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") == "2.0.0":
        return False
    if data.get(collection):
        raise RuntimeError(f"{path}: migrarea automată refuză un registru v1 ne-gol; este necesară revizie manuală.")
    data["schema_version"] = "2.0.0"
    write_json_atomic(path, data)
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    changed = []
    for name, collection in (("sources.json", "sources"), ("claims.json", "claims"), ("citations.json", "citations")):
        path = args.root / "research" / name
        if migrate_empty_registry(path, collection):
            changed.append(path.relative_to(args.root).as_posix())
    print(json.dumps({"changed": changed}, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
