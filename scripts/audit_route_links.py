#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "web"


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.refs.append((attr, value))


def resolves(path: str) -> bool:
    clean = unquote(urlsplit(path).path)
    if not clean.startswith("/"):
        return True
    target = DIST / clean.lstrip("/")
    candidates = [target]
    if clean.endswith("/"):
        candidates.append(target / "index.html")
    elif not target.suffix:
        candidates.extend([target / "index.html", target.with_suffix(".html")])
    return any(candidate.is_file() for candidate in candidates)


errors: list[str] = []
files = sorted(DIST.rglob("*.html"))
for html in files:
    parser = LinkParser()
    parser.feed(html.read_text(encoding="utf-8"))
    for attr, ref in parser.refs:
        scheme = urlsplit(ref).scheme
        if scheme in {"http", "https", "mailto", "tel", "data"} or ref.startswith("#"):
            continue
        if not resolves(ref):
            errors.append(f"{html.relative_to(DIST)} {attr}={ref}")

if errors:
    print(f"BROKEN_INTERNAL_REFS={len(errors)}")
    print("\n".join(errors))
    raise SystemExit(1)
print(f"ROUTE_CRAWL_PASS HTML={len(files)} BROKEN_INTERNAL_REFS=0")
