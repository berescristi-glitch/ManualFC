#!/usr/bin/env python3
"""Unelte fail-closed pentru registrele de cercetare Manual U11."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


class ResearchError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


def read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ResearchError("JSON_PARSE_ERROR", f"{path}: {exc}") from None


def write_json_atomic(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(data, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temp_name, path)
    finally:
        if os.path.exists(temp_name):
            os.unlink(temp_name)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_url(value: str | None) -> str | None:
    if not value:
        return None
    parts = urlsplit(value.strip())
    scheme = parts.scheme.lower()
    host = (parts.hostname or "").lower()
    port = parts.port
    netloc = host
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        netloc += f":{port}"
    path = re.sub(r"/+", "/", parts.path or "/")
    if path != "/":
        path = path.rstrip("/")
    query = urlencode(sorted((k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
                             if not k.lower().startswith("utm_")))
    return urlunsplit((scheme, netloc, path, query, ""))


def normalize_doi(value: str | None) -> str | None:
    if not value:
        return None
    result = value.strip().lower()
    result = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", result)
    return result.removeprefix("doi:").strip()


def normalize_isbn(value: str | None) -> str | None:
    return re.sub(r"[^0-9Xx]", "", value).upper() if value else None


def normalize_title(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", value.casefold())).strip()


def next_id(items: list[dict], key: str, prefix: str) -> str:
    numbers = []
    for item in items:
        match = re.fullmatch(fr"{re.escape(prefix)}-(\d+)", str(item.get(key, "")))
        if match:
            numbers.append(int(match.group(1)))
    return f"{prefix}-{max(numbers, default=0) + 1:04d}"


def schema_item(root: Path, schema_name: str) -> dict:
    schema = read_json(root / "schemas" / schema_name)
    if "sources" in schema.get("properties", {}):
        return schema["properties"]["sources"]["items"]
    if "archives" in schema.get("properties", {}):
        return schema["properties"]["archives"]["items"]
    return schema


def validate_item(item: dict, schema: dict, label: str) -> None:
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(item),
                    key=lambda error: list(error.absolute_path))
    if errors:
        first = errors[0]
        path = "$" + "".join(f"[{part}]" if isinstance(part, int) else f".{part}" for part in first.absolute_path)
        raise ResearchError("SCHEMA_VALIDATION_ERROR", f"{label} {path}: {first.message}")


def duplicate_matches(candidate: dict, sources: list[dict]) -> list[dict]:
    checks = {
        "DOI": (normalize_doi(candidate.get("doi")), lambda item: normalize_doi(item.get("doi"))),
        "URL": (normalize_url(candidate.get("url")), lambda item: normalize_url(item.get("url"))),
        "SHA256": (candidate.get("sha256"), lambda item: item.get("sha256")),
        "ISBN": (normalize_isbn(candidate.get("isbn")), lambda item: normalize_isbn(item.get("isbn"))),
    }
    matches = []
    for source in sources:
        reasons = [name for name, (value, getter) in checks.items() if value and value == getter(source)]
        if reasons:
            matches.append({"source_id": source["source_id"], "exact_identifiers": sorted(reasons)})
    return sorted(matches, key=lambda item: item["source_id"])


def prepare_source(candidate: dict, sources: list[dict], file_path: Path | None = None,
                   root: Path | None = None) -> dict:
    item = dict(candidate)
    item["source_id"] = next_id(sources, "source_id", "SRC")
    item["authors"] = [re.sub(r"\s+", " ", str(author)).strip() for author in item.get("authors", [])]
    item["title"] = re.sub(r"\s+", " ", str(item.get("title", "")).strip())
    item["url"] = normalize_url(item.get("url"))
    item["doi"] = normalize_doi(item.get("doi"))
    item["isbn"] = normalize_isbn(item.get("isbn"))
    if file_path:
        item["sha256"] = sha256_file(file_path)
        item["local_file"] = (file_path.relative_to(root).as_posix()
                              if root is not None else file_path.as_posix())
    return item


def add_source(args) -> dict:
    registry_path = args.root / "research" / "sources.json"
    registry = read_json(registry_path)
    candidate = read_json(args.input)
    file_path = args.file.resolve() if args.file else None
    if file_path:
        try:
            file_path.relative_to(args.root.resolve())
        except ValueError:
            raise ResearchError("PATH_OUTSIDE_REPOSITORY", "Fișierul sursei trebuie să fie în repository.")
    item = prepare_source(candidate, registry["sources"], file_path, args.root.resolve())
    matches = duplicate_matches(item, registry["sources"])
    if matches:
        raise ResearchError("DUPLICATE_SOURCE", json.dumps(matches, ensure_ascii=False))
    validate_item(item, schema_item(args.root, "source-registry.schema.json"), "source")
    registry["sources"].append(item)
    registry["sources"].sort(key=lambda source: source["source_id"])
    write_json_atomic(registry_path, registry)
    return {"added": item["source_id"]}


def add_search(args) -> dict:
    entry = read_json(args.input)
    questions = read_json(args.root / "research" / "questions.json").get("questions", [])
    question_ids = {item["research_question_id"] for item in questions}
    if entry.get("research_question_id") not in question_ids:
        raise ResearchError("BROKEN_REFERENCE", "Întrebarea de cercetare nu există.")
    source_ids = {
        item["source_id"]
        for item in read_json(args.root / "research" / "sources.json").get("sources", [])
    }
    missing_sources = sorted(set(entry.get("included_source_ids", [])) - source_ids)
    if missing_sources:
        raise ResearchError("BROKEN_REFERENCE",
                            f"Sursele incluse nu există: {', '.join(missing_sources)}")
    log_path = args.root / "research" / "search-logs.jsonl"
    existing = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    entry["search_id"] = next_id(existing, "search_id", "SEARCH")
    validate_item(entry, schema_item(args.root, "search-log.schema.json"), "search")
    with log_path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")
    return {"added": entry["search_id"]}


def duplicate_report(args) -> dict:
    sources = read_json(args.root / "research" / "sources.json")["sources"]
    exact = []
    for index, source in enumerate(sources):
        for match in duplicate_matches(source, sources[index + 1:]):
            exact.append({
                "left_source_id": source["source_id"],
                "right_source_id": match["source_id"],
                "exact_identifiers": match["exact_identifiers"],
            })
    probable = []
    groups: dict[tuple, list[str]] = {}
    for source in sources:
        key = (normalize_title(source["title"]), tuple(author.casefold() for author in source["authors"]), source["year"])
        groups.setdefault(key, []).append(source["source_id"])
    for ids in groups.values():
        if len(ids) > 1:
            probable.append({"source_ids": sorted(ids), "action": "REVIEW_ONLY_DO_NOT_MERGE"})
    return {"exact": sorted(exact, key=lambda item: (item["left_source_id"], item["right_source_id"])),
            "probable": sorted(probable, key=lambda item: item["source_ids"])}


def freshness_report(args) -> dict:
    as_of = date.fromisoformat(args.as_of) if args.as_of else date.today()
    sources = read_json(args.root / "research" / "sources.json")["sources"]
    result = {"as_of": as_of.isoformat(), "missing_verification": [], "expired": [], "superseded": [], "withdrawn": [], "inaccessible": []}
    for source in sources:
        sid = source["source_id"]
        if not source.get("verified_at"):
            result["missing_verification"].append(sid)
        if source.get("next_review_at") and date.fromisoformat(source["next_review_at"]) < as_of:
            result["expired"].append(sid)
        if source.get("currency_status") == "SUPERSEDED":
            result["superseded"].append(sid)
        if source.get("withdrawn") or source.get("currency_status") == "WITHDRAWN":
            result["withdrawn"].append(sid)
        if source.get("access_status") == "INACCESSIBLE":
            result["inaccessible"].append(sid)
    for key in result:
        if isinstance(result[key], list):
            result[key].sort()
    return result


def archive_file(args) -> dict:
    root = args.root.resolve()
    registry = read_json(root / "research" / "sources.json")
    source = next((item for item in registry["sources"] if item["source_id"] == args.source_id), None)
    if not source:
        raise ResearchError("BROKEN_REFERENCE", "Sursa nu există.")
    if not source["usage_rights"]["store_snapshot"]:
        raise ResearchError("RIGHTS_RESTRICTION", "Drepturile nu permit păstrarea snapshotului.")
    source_file = args.file.resolve()
    if not source_file.is_file():
        raise ResearchError("FILE_NOT_FOUND", "Fișierul de arhivat nu există.")
    destination_dir = root / "research" / "source-snapshots"
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / f"{args.source_id}-{source_file.name}"
    if destination.exists():
        raise ResearchError("FILE_EXISTS", "Snapshotul există deja; nu este suprascris.")
    shutil.copy2(source_file, destination)
    manifests_path = root / "research" / "archive-manifests.json"
    manifests = read_json(manifests_path)
    item = {
        "archive_id": next_id(manifests["archives"], "archive_id", "ARCH"),
        "source_id": args.source_id,
        "path": destination.relative_to(root).as_posix(),
        "sha256": sha256_file(destination),
        "size_bytes": destination.stat().st_size,
        "archived_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "licence": source["licence"],
        "storage_level": "B_PERMITTED_SNAPSHOT",
        "distribution_status": "PUBLIC" if source["usage_rights"]["public_distribution"] else "LOCAL_ONLY"
    }
    validate_item(item, schema_item(root, "archive-manifest.schema.json"), "archive")
    manifests["archives"].append(item)
    write_json_atomic(manifests_path, manifests)
    return {"added": item["archive_id"], "path": item["path"], "sha256": item["sha256"]}


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    sub = result.add_subparsers(dest="command", required=True)
    add = sub.add_parser("add-source"); add.add_argument("--input", type=Path, required=True); add.add_argument("--file", type=Path); add.set_defaults(func=add_source)
    search = sub.add_parser("add-search"); search.add_argument("--input", type=Path, required=True); search.set_defaults(func=add_search)
    duplicates = sub.add_parser("duplicates"); duplicates.set_defaults(func=duplicate_report)
    freshness = sub.add_parser("freshness"); freshness.add_argument("--as-of"); freshness.set_defaults(func=freshness_report)
    archive = sub.add_parser("archive-file"); archive.add_argument("--source-id", required=True); archive.add_argument("--file", type=Path, required=True); archive.set_defaults(func=archive_file)
    return result


def main(argv=None) -> int:
    args = parser().parse_args(argv)
    args.root = args.root.resolve()
    try:
        output = args.func(args)
        print(json.dumps({"ok": True, "result": output}, ensure_ascii=False, sort_keys=True))
        return 0
    except ResearchError as exc:
        print(json.dumps({"ok": False, "code": exc.code, "message": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
