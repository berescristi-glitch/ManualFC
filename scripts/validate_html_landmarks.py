#!/usr/bin/env python3
"""Fail closed when a built product document has anything but one main landmark."""
from __future__ import annotations

import argparse
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


class LandmarkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.main_count = 0
        self.main_depth = 0
        self.nested_main = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "main":
            if self.main_depth:
                self.nested_main += 1
            self.main_count += 1
            self.main_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag == "main" and self.main_depth:
            self.main_depth -= 1


def validate(dist: Path) -> list[str]:
    errors: list[str] = []
    html_files = sorted(dist.rglob("*.html"))
    if not html_files:
        return [f"Nu există documente HTML în {dist}."]
    for path in html_files:
        parser = LandmarkParser()
        parser.feed(path.read_text(encoding="utf-8"))
        relative = path.relative_to(dist)
        if parser.main_count != 1:
            errors.append(f"{relative}: main_count={parser.main_count}, expected=1")
        if parser.nested_main:
            errors.append(f"{relative}: nested_main={parser.nested_main}, expected=0")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", type=Path, default=ROOT / "dist" / "web")
    args = parser.parse_args()
    errors = validate(args.dist)
    if errors:
        print("INVALID landmarks")
        for error in errors:
            print(f"ERROR {error}")
        return 1
    count = len(list(args.dist.rglob("*.html")))
    print(f"VALID landmarks: {count} documente, main=1, nested_main=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
