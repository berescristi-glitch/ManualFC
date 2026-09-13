#!/usr/bin/env python3
"""Validatorul canonic fail-closed pentru datele Manualului U11."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import traceback
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any, Iterable

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import SchemaError, ValidationError
except ImportError:
    print("ERROR SCHEMA_INVALID: lipsește dependența jsonschema; rulează pip install -r requirements-dev.txt", file=sys.stderr)
    raise SystemExit(2)

try:
    from validation.diagnostic import Diagnostic
except ModuleNotFoundError:  # Importat ca modul `scripts.validate_content` în teste.
    from scripts.validation.diagnostic import Diagnostic

ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 5 * 1024 * 1024
SUPPORTED_DIALECT = "https://json-schema.org/draft/2020-12/schema"
PLACEHOLDER_RE = re.compile(r"(?i)\b(?:TODO|TBD|placeholder|de completat|lorem ipsum)\b")
MULTISPACE_RE = re.compile(r" {2,}")
RAW_URL_RE = re.compile(r"(?<!\]\()https?://\S+")
ID_RE = re.compile(r"^(?P<prefix>[A-Z][A-Z0-9]*?)-[A-Z0-9][A-Z0-9_-]*$")
SCHEMA_TYPES = {
    "project": "project.schema.json",
    "visual-token": "visual-tokens.schema.json",
    "source": "source-registry.schema.json",
    "claim": "claim-registry.schema.json",
    "citation": "citation-registry.schema.json",
    "task": "task.schema.json",
    "principle": "principle.schema.json",
    "problem": "problem.schema.json",
    "media": "media-registry.schema.json",
    "exercise": "exercise.schema.json",
    "session": "session.schema.json",
    "message": "message-foundation.schema.json",
    "visual-asset": "visual-asset.schema.json",
    "chapter": "chapter.schema.json",
    "curriculum": "curriculum.schema.json",
    "season-plan": "season-plan.schema.json",
    "communication-script": "communication-script.schema.json",
    "case-study": "case-study.schema.json",
    "assessment": "assessment.schema.json",
    "animation": "animation.schema.json",
    "diagram": "diagram.schema.json",
    "task-report": "task-report.schema.json",
    "build-manifest": "build-manifest.schema.json",
    "distribution-manifest": "distribution-manifest.schema.json",
    "research-taxonomy": "research-taxonomy.schema.json",
    "research-question": "research-question.schema.json",
    "search-log": "search-log.schema.json",
    "archive-manifest": "archive-manifest.schema.json",
    "regulation-rule": "regulation-rule.schema.json",
    "regulation-conflict": "regulation-conflict.schema.json",
    "regulation-space": "regulation-space.schema.json",
    "safeguarding": "safeguarding.schema.json",
}
PREFIX_TYPES = {
    "TASK": "task", "SRC": "source", "CLM": "claim", "CIT": "citation",
    "PRI": "principle", "PR": "principle", "EX": "exercise", "SES": "session",
    "MSG": "message", "VIS": "visual-asset", "CH": "chapter", "CUR": "curriculum",
    "MIC": "microcycle", "SCR": "communication-script", "CASE": "case-study",
    "ASM": "assessment", "ANI": "animation", "DIA": "diagram", "RQ": "research-question",
    "SEARCH": "search-log", "ARCH": "archive-manifest",
}
REFERENCE_FIELDS = {
    "chapter_ids": "chapter", "principle_ids": "principle", "principles": "principle",
    "exercise_ids": "exercise", "exercises": "exercise", "session_ids": "session",
    "sessions": "session", "script_ids": "communication-script", "source_ids": "source",
    "sources": "source", "claim_ids": "claim", "source_claim_ids": "claim",
    "curriculum_ids": "curriculum", "curriculum_id": "curriculum",
    "visual_asset_ids": "visual-asset", "visual_assets": "visual-asset",
    "animation_id": "animation", "animation_ids": "animation",
    "storyboard_id": "diagram", "pdf_frame_ids": "diagram", "paired_variant_id": "diagram",
    "licence_source_id": "source",
    "research_question_ids": "research-question", "research_question_id": "research-question",
    "claim_ids": "claim", "supersedes_source_id": "source",
    "superseded_by_source_id": "source", "replacement_claim_id": "claim",
}
PEDAGOGICAL_FIELDS = {
    "child_wording", "child_message", "coach_meaning", "why_this_wording",
    "why_this_message", "problem_being_solved", "decision_to_learn",
    "decision_children_must_learn", "age_appropriateness", "match_transfer",
}
RATIONALE_FIELDS = {"tactical", "perceptual", "decisional", "cognitive", "psychological", "technical", "social"}


def json_path(parts: Iterable[Any]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def safe_relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return str(path)


def diagnostic(code: str, message: str, file: str, path: str = "$", *,
               severity: str = "ERROR", found: Any = None, expected: str | None = None,
               related: str | None = None, suggestion: str | None = None) -> Diagnostic:
    if isinstance(found, str) and len(found) > 160:
        found = found[:157] + "..."
    return Diagnostic(code, severity, message, file, path, found, expected, related, suggestion)


class ContentValidator:
    def __init__(self, root: Path = ROOT, *, strict: bool = False, debug: bool = False) -> None:
        self.root = root.resolve()
        self.strict = strict
        self.debug = debug
        self.diagnostics: list[Diagnostic] = []
        self.schemas: dict[str, dict[str, Any]] = {}
        self.documents: list[tuple[str, str, Any]] = []
        self.index: dict[str, tuple[str, str, str]] = {}
        self.ids_by_type: dict[str, set[str]] = defaultdict(set)
        self.slug_index: dict[str, tuple[str, str]] = {}

    def add(self, item: Diagnostic) -> None:
        if self.strict and item.severity == "WARNING":
            item = Diagnostic(item.code, "ERROR", item.message, item.file, item.json_path,
                              item.found_value, item.expected, item.related_file, item.suggestion)
        self.diagnostics.append(item)

    def load_schemas(self) -> None:
        schema_dir = self.root / "schemas"
        if not schema_dir.is_dir():
            self.add(diagnostic("SCHEMA_NOT_FOUND", "Directorul canonic schemas lipsește.", "schemas"))
            return
        for path in sorted(schema_dir.glob("*.json")):
            rel = safe_relative(path, self.root)
            try:
                schema = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                self.add(diagnostic("SCHEMA_INVALID", "Schema nu este JSON valid.", rel, found=str(exc)))
                continue
            dialect = schema.get("$schema")
            if dialect != SUPPORTED_DIALECT:
                self.add(diagnostic("SCHEMA_VERSION_UNSUPPORTED", "Dialect JSON Schema nesuportat.", rel, "$.$schema",
                                    found=dialect, expected=SUPPORTED_DIALECT))
                continue
            try:
                Draft202012Validator.check_schema(schema)
            except SchemaError as exc:
                self.add(diagnostic("SCHEMA_INVALID", "Schema nu respectă metaschema Draft 2020-12.", rel,
                                    json_path(exc.absolute_schema_path), found=exc.message))
                continue
            self.schemas[path.name] = schema
        for type_name, filename in SCHEMA_TYPES.items():
            if filename not in self.schemas:
                self.add(diagnostic("SCHEMA_NOT_FOUND", f"Schema pentru tipul {type_name} lipsește.", f"schemas/{filename}"))

    def _safe_file(self, path: Path) -> bool:
        rel = safe_relative(path, self.root)
        if path.is_symlink():
            self.add(diagnostic("SYMLINK_NOT_ALLOWED", "Fișierele validate nu pot fi symlinkuri.", rel))
            return False
        try:
            path.resolve().relative_to(self.root)
        except ValueError:
            self.add(diagnostic("PATH_OUTSIDE_REPOSITORY", "Calea iese din repository.", rel))
            return False
        try:
            size = path.stat().st_size
        except OSError as exc:
            self.add(diagnostic("INVALID_VALUE", "Fișierul nu poate fi inspectat.", rel, found=str(exc)))
            return False
        if size > MAX_FILE_BYTES:
            self.add(diagnostic("FILE_TOO_LARGE", "Fișierul depășește limita validatorului.", rel,
                                found=size, expected=f"maximum {MAX_FILE_BYTES} bytes"))
            return False
        return True

    def _infer_type(self, rel: str, data: Any) -> str | None:
        direct = {
            "config/project.json": "project",
            "config/visual-tokens.json": "visual-token",
            "research/sources.json": "source",
            "research/claims.json": "claim",
            "research/citations.json": "citation",
            "research/questions.json": "research-question",
            "research/archive-manifests.json": "archive-manifest",
            "config/research-taxonomy.json": "research-taxonomy",
            "TASK_REGISTRY.json": "task",
            "data/regulations/u11-rules.json": "regulation-rule",
            "data/regulations/u11-conflicts.json": "regulation-conflict",
            "data/regulations/u11-space-per-player.json": "regulation-space",
            "data/safeguarding/canonical.json": "safeguarding",
        }
        if rel in direct:
            return direct[rel]
        directory_map = {
            "data/principles/": "principle", "data/exercises/": "exercise",
            "data/sessions/": "session", "data/season-plans/": "season-plan",
            "data/assessments/": "assessment", "data/communication-scripts/": "communication-script",
            "data/case-studies/": "case-study", "assets/manifests/": "visual-asset",
            "data/curriculum/": "curriculum", "data/animations/": "animation",
            "data/diagrams/": "diagram",
        }
        for prefix, kind in directory_map.items():
            if rel.startswith(prefix):
                return kind
        if isinstance(data, dict):
            schema_ref = data.get("$schema")
            if isinstance(schema_ref, str):
                name = Path(schema_ref).name
                return next((kind for kind, schema in SCHEMA_TYPES.items() if schema == name), None)
            entity_id = data.get("id") or data.get("task_id") or data.get("source_id") or data.get("claim_id")
            if isinstance(entity_id, str) and "-" in entity_id:
                return PREFIX_TYPES.get(entity_id.split("-", 1)[0])
        return None

    def discover(self, selected_file: str | None = None, selected_type: str | None = None) -> None:
        if selected_file:
            candidate = (self.root / selected_file).resolve()
            try:
                candidate.relative_to(self.root)
            except ValueError:
                self.add(diagnostic("PATH_OUTSIDE_REPOSITORY", "Fișierul selectat iese din repository.", selected_file))
                return
            paths = [candidate]
        else:
            paths = []
            for base in ("config", "research", "data", "assets/manifests"):
                folder = self.root / base
                if folder.exists():
                    paths.extend(folder.rglob("*.json"))
            paths.append(self.root / "TASK_REGISTRY.json")
        seen: set[Path] = set()
        for path in sorted(paths):
            if path in seen or not path.is_file():
                continue
            seen.add(path)
            if not self._safe_file(path):
                continue
            rel = safe_relative(path, self.root)
            if rel.startswith("data/fixtures/") or rel.startswith("data/taxonomy/") or rel.startswith("data/content/") or rel.startswith("data/platform/"):
                continue
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                self.add(diagnostic("JSON_PARSE_ERROR", "Fișierul JSON nu poate fi analizat.", rel,
                                    f"$[line:{exc.lineno},column:{exc.colno}]", found=exc.msg,
                                    suggestion="Corectează sintaxa JSON."))
                continue
            except UnicodeDecodeError:
                self.add(diagnostic("JSON_PARSE_ERROR", "Fișierul JSON nu este UTF-8.", rel))
                continue
            kind = self._infer_type(rel, data)
            if not kind:
                self.add(diagnostic("SCHEMA_NOT_FOUND", "Nu poate fi determinată schema documentului.", rel,
                                    suggestion="Adaugă $schema sau plasează fișierul într-un director canonic."))
                continue
            if selected_type and kind != selected_type:
                continue
            self.documents.append((rel, kind, data))

    def _instances(self, kind: str, data: Any) -> list[tuple[Any, str]]:
        if kind == "task":
            return [(item, f"$.tasks[{i}]") for i, item in enumerate(data.get("tasks", []))]
        wrappers = {
            "source": "sources", "claim": "claims", "citation": "citations",
            "principle": "principles", "exercise": "exercises", "session": "sessions",
            "season-plan": "season_plans", "assessment": "assessments",
            "communication-script": "scripts", "case-study": "case_studies",
            "visual-asset": "assets", "curriculum": "curricula", "animation": "animations",
            "diagram": "diagrams",
            "research-question": "questions", "archive-manifest": "archives",
            "regulation-rule": "rules", "regulation-conflict": "conflicts",
            "regulation-space": "rows",
        }
        key = wrappers.get(kind)
        if key and isinstance(data, dict) and key in data:
            return [(item, f"$.{key}[{i}]") for i, item in enumerate(data[key])]
        if isinstance(data, list):
            return [(item, f"$[{i}]") for i, item in enumerate(data)]
        return [(data, "$")]

    def validate_schemas(self) -> None:
        format_checker = FormatChecker()
        for rel, kind, data in self.documents:
            schema_name = SCHEMA_TYPES.get(kind)
            schema = self.schemas.get(schema_name or "")
            if not schema:
                self.add(diagnostic("SCHEMA_NOT_FOUND", f"Schema pentru {kind} nu poate fi încărcată.", rel))
                continue
            wrapper_key = {
                "task": "tasks", "source": "sources", "claim": "claims",
                "citation": "citations", "research-question": "questions",
                "archive-manifest": "archives", "regulation-rule": "rules",
                "regulation-conflict": "conflicts", "regulation-space": "rows",
            }.get(kind)
            schema_requires = schema.get("required", [])
            validates_wrapper = wrapper_key in schema_requires if wrapper_key else False
            instances = [(data, "$")] if validates_wrapper else self._instances(kind, data)
            for instance, base_path in instances:
                validator = Draft202012Validator(schema, format_checker=format_checker)
                for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.absolute_path)):
                    self.add(self._schema_diagnostic(error, rel, base_path))
            self._validate_document_metadata(rel, data)

    def _schema_diagnostic(self, error: ValidationError, rel: str, base: str) -> Diagnostic:
        suffix = json_path(error.absolute_path)
        path = base + (suffix[1:] if suffix != "$" else "")
        code_map = {
            "required": "REQUIRED_FIELD_MISSING", "minLength": "EMPTY_REQUIRED_VALUE",
            "minItems": "EMPTY_REQUIRED_VALUE", "type": "TYPE_MISMATCH",
            "enum": "INVALID_VALUE", "const": "INVALID_VALUE", "pattern": "INVALID_IDENTIFIER",
            "format": "INVALID_FORMAT", "additionalProperties": "ADDITIONAL_PROPERTY_FORBIDDEN",
        }
        code = code_map.get(error.validator, "INVALID_VALUE")
        if error.validator == "required":
            missing = re.search(r"'([^']+)' is a required property", error.message)
            if missing:
                path += f".{missing.group(1)}"
        return diagnostic(code, error.message, rel, path, found=error.instance,
                          expected=f"JSON Schema: {error.validator}={error.validator_value}")

    def _validate_document_metadata(self, rel: str, data: Any) -> None:
        if not isinstance(data, dict):
            return
        version = data.get("schema_version")
        if version is not None and not re.fullmatch(r"\d+\.\d+\.\d+", str(version)):
            self.add(diagnostic("SCHEMA_VERSION_UNSUPPORTED", "Versiunea schemei nu este semantică.", rel,
                                "$.schema_version", found=version, expected="MAJOR.MINOR.PATCH"))

    def build_index(self) -> None:
        preferred_id_keys = {
            "task": "task_id", "source": "source_id", "claim": "claim_id",
            "citation": "citation_id", "research-question": "research_question_id",
            "search-log": "search_id", "archive-manifest": "archive_id",
            "regulation-rule": "rule_id", "regulation-conflict": "conflict_id",
        }
        id_keys = ("id", "task_id", "citation_id", "claim_id", "source_id", "research_question_id",
                   "search_id", "archive_id", "chapter_id",
                   "curriculum_id", "script_id", "case_study_id", "assessment_id", "asset_id",
                   "rule_id", "conflict_id")
        for rel, kind, data in self.documents:
            if kind == "regulation-space":
                continue
            for instance, base in self._instances(kind, data):
                if not isinstance(instance, dict):
                    continue
                preferred = preferred_id_keys.get(kind)
                key = preferred if preferred and isinstance(instance.get(preferred), str) else next(
                    (item for item in id_keys if isinstance(instance.get(item), str)), None
                )
                if key:
                    value = instance[key]
                    path = f"{base}.{key}"
                    previous = self.index.get(value)
                    if previous:
                        self.add(diagnostic("DUPLICATE_ID", "Identificatorul este duplicat.", rel, path,
                                            found=value, related=previous[1]))
                    else:
                        self.index[value] = (kind, rel, path)
                        self.ids_by_type[kind].add(value)
                slug = instance.get("slug")
                if isinstance(slug, str):
                    previous_slug = self.slug_index.get(slug)
                    if previous_slug:
                        self.add(diagnostic("DUPLICATE_SLUG", "Slugul este duplicat.", rel, f"{base}.slug",
                                            found=slug, related=previous_slug[0]))
                    else:
                        self.slug_index[slug] = (rel, f"{base}.slug")

    def validate_references(self) -> None:
        for rel, kind, data in self.documents:
            for instance, base in self._instances(kind, data):
                self._walk_references(instance, rel, base)
        self._validate_research()
        self._validate_tasks()
        self._validate_assets()

    def _walk_references(self, value: Any, rel: str, path: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                expected_type = REFERENCE_FIELDS.get(key)
                if expected_type:
                    values = child if isinstance(child, list) else [child]
                    for index, reference in enumerate(values):
                        ref_path = f"{path}.{key}" + (f"[{index}]" if isinstance(child, list) else "")
                        if not isinstance(reference, str):
                            continue
                        if not ID_RE.fullmatch(reference):
                            # Unele câmpuri istorice precum `sources` pot conține căi de registru.
                            continue
                        target = self.index.get(reference)
                        if not target:
                            self.add(diagnostic("BROKEN_REFERENCE", "Referința nu există în indexul canonic.",
                                                rel, ref_path, found=reference,
                                                expected=f"ID existent de tip {expected_type}"))
                        elif target[0] != expected_type:
                            self.add(diagnostic("REFERENCE_TYPE_MISMATCH", "Referința indică un tip greșit.",
                                                rel, ref_path, found=reference,
                                                expected=expected_type, related=target[1]))
                self._walk_references(child, rel, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                self._walk_references(child, rel, f"{path}[{index}]")

    def _validate_research(self) -> None:
        source_ids = self.ids_by_type["source"]
        claim_ids = self.ids_by_type["claim"]
        citations = [item for rel, kind, data in self.documents if kind == "citation"
                     for item, _ in self._instances(kind, data) if isinstance(item, dict)]
        claims = {item.get("claim_id"): (item, rel, base)
                  for rel, kind, data in self.documents if kind == "claim"
                  for item, base in self._instances(kind, data)
                  if isinstance(item, dict) and isinstance(item.get("claim_id"), str)}
        sources = {item.get("source_id"): item
                   for rel, kind, data in self.documents if kind == "source"
                   for item, _ in self._instances(kind, data)
                   if isinstance(item, dict) and isinstance(item.get("source_id"), str)}
        citations_by_claim: dict[str, list[dict]] = {}
        for citation in citations:
            citations_by_claim.setdefault(citation.get("claim_id"), []).append(citation)
        for rel, kind, data in self.documents:
            if kind == "claim":
                for item, base in self._instances(kind, data):
                    if not isinstance(item, dict):
                        continue
                    refs = item.get("source_ids", [])
                    if item.get("claim_type") not in {"OPINION", "METHODOLOGICAL_SYNTHESIS"} and not refs:
                        self.add(diagnostic("CLAIM_WITHOUT_SOURCE", "Afirmația necesită cel puțin o sursă.", rel,
                                            f"{base}.source_ids"))
                    for i, ref in enumerate(refs):
                        if ref not in source_ids:
                            self.add(diagnostic("BROKEN_REFERENCE", "Afirmația indică o sursă inexistentă.", rel,
                                                f"{base}.source_ids[{i}]", found=ref))
                    if item.get("status") in {"OUTDATED", "WITHDRAWN", "REPLACED"} and item.get("usage_locations"):
                        self.add(diagnostic("TASK_STATE_INCONSISTENT",
                                            "Afirmația neactuală nu poate avea utilizări publice active.",
                                            rel, f"{base}.usage_locations", found=item.get("status")))
            if kind == "source":
                for item, base in self._instances(kind, data):
                    if isinstance(item, dict) and item.get("source_type") in {"OFFICIAL_REGULATION", "LOCAL_COMPETITION_RULE", "LEGAL_SOURCE"} and not item.get("version"):
                        self.add(diagnostic("SOURCE_WITHOUT_REQUIRED_METADATA", "Sursa actualizabilă necesită versiune.",
                                            rel, f"{base}.version", severity="WARNING",
                                            suggestion="Înregistrează versiunea verificată."))
                    if isinstance(item, dict) and item.get("source_type") == "VISUAL_ASSET_SOURCE" and (
                        not item.get("licence") or not item.get("visual_rights")
                    ):
                        self.add(diagnostic("RIGHTS_METADATA_MISSING",
                                            "Sursa vizuală nu are drepturi complete.", rel, base))
        self._validate_source_duplicates_and_versions()
        self._validate_search_logs()
        for index, item in enumerate(citations):
            if item.get("claim_id") not in claim_ids or item.get("source_id") not in source_ids:
                self.add(diagnostic("CITATION_TARGET_MISSING", "Citarea are o țintă inexistentă.",
                                    "research/citations.json", f"$.citations[{index}]",
                                    found={"claim_id": item.get("claim_id"), "source_id": item.get("source_id")}))
            location = item.get("usage_location")
            if isinstance(location, str) and location and not (self.root / location.split("#", 1)[0]).exists():
                self.add(diagnostic("CITATION_TARGET_MISSING", "Locația utilizării citării nu există.",
                                    "research/citations.json", f"$.citations[{index}].usage_location",
                                    found=location))
        self._validate_production_evidence(claims, citations_by_claim, source_ids, sources)

    def _validate_production_evidence(self, claims: dict, citations_by_claim: dict,
                                      source_ids: set[str], sources: dict[str, dict]) -> None:
        required_metadata = (
            "epistemic_level", "population", "participant_age", "context",
            "u11_applicability", "limitations", "practical_implication",
        )
        for rel, kind, data in self.documents:
            if "/fixtures/" in rel.replace("\\", "/"):
                continue
            for entity, base in self._instances(kind, data):
                if not isinstance(entity, dict) or entity.get("development_fixture") is True:
                    continue
                for index, claim_id in enumerate(entity.get("evidence_claim_ids", [])):
                    claim_record = claims.get(claim_id)
                    if not claim_record:
                        continue
                    claim, claim_rel, claim_base = claim_record
                    if claim.get("status") in {"OUTDATED", "WITHDRAWN", "REPLACED"}:
                        self.add(diagnostic(
                            "CANONICAL_EVIDENCE_CHAIN_BROKEN",
                            "Conținutul publicat nu poate folosi un claim retras sau înlocuit.",
                            rel, f"{base}.evidence_claim_ids[{index}]", found=claim_id,
                            expected="claim activ", related=claim_rel,
                        ))
                    withdrawn_sources = [source_id for source_id in claim.get("source_ids", [])
                                         if sources.get(source_id, {}).get("withdrawn") is True]
                    if withdrawn_sources:
                        self.add(diagnostic(
                            "CANONICAL_EVIDENCE_CHAIN_BROKEN",
                            "Conținutul publicat nu poate folosi un claim bazat pe surse retrase.",
                            rel, f"{base}.evidence_claim_ids[{index}]", found=withdrawn_sources,
                            expected="surse active", related=claim_rel,
                        ))
                    missing = [field for field in required_metadata
                               if field not in claim or claim.get(field) in (None, "", [])]
                    if missing:
                        self.add(diagnostic(
                            "CANONICAL_EVIDENCE_METADATA_MISSING",
                            "Claim-ul folosit de conținutul canonic nu are metadata epistemică completă.",
                            claim_rel, claim_base, found=missing,
                            expected=list(required_metadata), related=rel,
                        ))
                    linked = citations_by_claim.get(claim_id, [])
                    valid = [citation for citation in linked
                             if citation.get("source_id") in source_ids
                             and citation.get("source_id") in claim.get("source_ids", [])]
                    if not valid:
                        self.add(diagnostic(
                            "CANONICAL_EVIDENCE_CHAIN_BROKEN",
                            "Claim-ul folosit de conținutul canonic nu rezolvă prin citare către o sursă declarată.",
                            rel, f"{base}.evidence_claim_ids[{index}]", found=claim_id,
                            expected="cel puțin o citare validă către source_ids",
                        ))
        for claim_id, linked in citations_by_claim.items():
            claim_record = claims.get(claim_id)
            if not claim_record:
                continue
            claim = claim_record[0]
            for citation in linked:
                if citation.get("source_id") not in claim.get("source_ids", []):
                    self.add(diagnostic(
                        "CITATION_SOURCE_MISMATCH",
                        "Citarea indică o sursă care nu este declarată de claim.",
                        "research/citations.json", f"$.citations[{citation.get('citation_id')}]",
                        found=citation.get("source_id"), expected=claim.get("source_ids", []),
                    ))

    def _validate_source_duplicates_and_versions(self) -> None:
        sources = [(item, rel, base) for rel, kind, data in self.documents if kind == "source"
                   for item, base in self._instances(kind, data) if isinstance(item, dict)]
        exact_fields = ("doi", "url", "sha256", "isbn")
        for field in exact_fields:
            seen: dict[str, tuple[str, str]] = {}
            for item, rel, base in sources:
                value = item.get(field)
                if not value:
                    continue
                normalized = str(value).strip().casefold().rstrip("/")
                if field == "url":
                    normalized = re.sub(r"[?#].*$", "", normalized)
                if normalized in seen:
                    self.add(diagnostic("DUPLICATE_SOURCE", f"Identificator de sursă duplicat: {field}.",
                                        rel, f"{base}.{field}", found=value, related=seen[normalized][0]))
                else:
                    seen[normalized] = (rel, base)
        graph = {item["source_id"]: [item["supersedes_source_id"]] if item.get("supersedes_source_id") else []
                 for item, _, _ in sources}
        cycle = self._find_cycle(graph)
        if cycle:
            self.add(diagnostic("VERSION_CYCLE", "Lanțul versiunilor de surse conține un ciclu.",
                                "research/sources.json", "$.sources", found=" -> ".join(cycle)))
        by_id = {item["source_id"]: item for item, _, _ in sources}
        for item, rel, base in sources:
            previous = item.get("supersedes_source_id")
            if previous and by_id.get(previous, {}).get("superseded_by_source_id") != item["source_id"]:
                self.add(diagnostic("TASK_STATE_INCONSISTENT",
                                    "Relația de versiune nu este bidirecțională.", rel,
                                    f"{base}.supersedes_source_id", found=previous))

    def _validate_search_logs(self) -> None:
        path = self.root / "research" / "search-logs.jsonl"
        if not path.exists():
            return
        schema = self.schemas.get("search-log.schema.json")
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                self.add(diagnostic("JSON_PARSE_ERROR", "Jurnalul de căutare conține JSON invalid.",
                                    "research/search-logs.jsonl", f"$[line:{line_no}]", found=exc.msg))
                continue
            for error in Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(entry):
                self.add(self._schema_diagnostic(error, "research/search-logs.jsonl", f"$[line:{line_no}]"))
            rq = entry.get("research_question_id")
            if rq not in self.ids_by_type["research-question"]:
                self.add(diagnostic("BROKEN_REFERENCE", "Căutarea indică o întrebare inexistentă.",
                                    "research/search-logs.jsonl", f"$[line:{line_no}].research_question_id",
                                    found=rq))
            for index, source_id in enumerate(entry.get("included_source_ids", [])):
                if source_id not in self.ids_by_type["source"]:
                    self.add(diagnostic("BROKEN_REFERENCE", "Căutarea include o sursă inexistentă.",
                                        "research/search-logs.jsonl",
                                        f"$[line:{line_no}].included_source_ids[{index}]",
                                        found=source_id))

    def _validate_tasks(self) -> None:
        task_doc = next(((rel, data) for rel, kind, data in self.documents if kind == "task"), None)
        if not task_doc:
            return
        rel, data = task_doc
        tasks = data.get("tasks", [])
        by_id = {item.get("task_id"): item for item in tasks if isinstance(item, dict)}
        graph: dict[str, list[str]] = {}
        history_ids: set[str] = set()
        history_path = self.root / "TASK_HISTORY.jsonl"
        if history_path.exists():
            for line_no, line in enumerate(history_path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                try:
                    event = json.loads(line)
                    if event.get("event") == "COMPLETED":
                        history_ids.add(event.get("task_id"))
                except json.JSONDecodeError as exc:
                    self.add(diagnostic("JSON_PARSE_ERROR", "Linie JSONL invalidă.", "TASK_HISTORY.jsonl",
                                        f"$[line:{line_no}]", found=exc.msg))
        for i, task in enumerate(tasks):
            tid = task.get("task_id")
            graph[tid] = task.get("dependencies", [])
            base = f"$.tasks[{i}]"
            for j, dep in enumerate(task.get("dependencies", [])):
                if dep not in by_id:
                    self.add(diagnostic("BROKEN_REFERENCE", "Dependența taskului nu există.", rel,
                                        f"{base}.dependencies[{j}]", found=dep))
            if task.get("status") == "DONE":
                for j, output in enumerate(task.get("outputs", [])):
                    if not isinstance(output, str) or not self._repo_path_exists(output):
                        self.add(diagnostic("OUTPUT_MISSING", "Outputul unui task DONE lipsește.", rel,
                                            f"{base}.outputs[{j}]", found=output))
                report = self.root / "reports/task-reports" / f"{tid}.md"
                if not report.exists():
                    self.add(diagnostic("REPORT_MISSING", "Raportul taskului DONE lipsește.", rel, base,
                                        found=tid, expected=report.relative_to(self.root).as_posix()))
                elif "valid" not in report.read_text(encoding="utf-8").casefold():
                    self.add(diagnostic("TASK_STATE_INCONSISTENT", "Raportul taskului DONE nu documentează validările.",
                                        safe_relative(report, self.root), "$", found=tid))
                if tid not in history_ids:
                    self.add(diagnostic("TASK_STATE_INCONSISTENT", "Taskul DONE nu are eveniment COMPLETED în istoric.",
                                        rel, f"{base}.status", found=tid))
                if not task.get("validation_commands"):
                    self.add(diagnostic("TASK_STATE_INCONSISTENT", "Taskul DONE nu declară validări.", rel,
                                        f"{base}.validation_commands"))
            if task.get("status") == "BLOCKED" and not task.get("last_error"):
                self.add(diagnostic("TASK_STATE_INCONSISTENT", "Taskul BLOCKED nu are motiv.", rel,
                                    f"{base}.last_error"))
        cycle = self._find_cycle(graph)
        if cycle:
            self.add(diagnostic("FORBIDDEN_REFERENCE_CYCLE", "Graful taskurilor conține un ciclu.",
                                rel, "$.tasks", found=" -> ".join(cycle)))
        for report in sorted((self.root / "reports/task-reports").glob("TASK-*.md")):
            task_id = report.stem
            if task_id not in by_id:
                self.add(diagnostic("BROKEN_REFERENCE", "Raportul indică un task inexistent.",
                                    safe_relative(report, self.root), "$", found=task_id))

    def _repo_path_exists(self, relative: str) -> bool:
        try:
            candidate = (self.root / relative).resolve()
            candidate.relative_to(self.root)
            return candidate.exists()
        except (ValueError, OSError):
            return False

    @staticmethod
    def _find_cycle(graph: dict[str, list[str]]) -> list[str] | None:
        visiting: set[str] = set()
        visited: set[str] = set()
        stack: list[str] = []
        def visit(node: str) -> list[str] | None:
            if node in visiting:
                start = stack.index(node)
                return stack[start:] + [node]
            if node in visited:
                return None
            visiting.add(node)
            stack.append(node)
            for child in graph.get(node, []):
                cycle = visit(child)
                if cycle:
                    return cycle
            stack.pop()
            visiting.remove(node)
            visited.add(node)
            return None
        for node in sorted(graph):
            cycle = visit(node)
            if cycle:
                return cycle
        return None

    def _validate_assets(self) -> None:
        registered_files: set[str] = set()
        diagram_items: dict[str, tuple[dict[str, Any], str, str]] = {}
        for rel, kind, data in self.documents:
            if kind == "diagram":
                for item, base in self._instances(kind, data):
                    if isinstance(item, dict) and isinstance(item.get("id"), str):
                        diagram_items[item["id"]] = (item, rel, base)
        for rel, kind, data in self.documents:
            if kind != "visual-asset":
                continue
            for item, base in self._instances(kind, data):
                if not isinstance(item, dict):
                    continue
                asset_id = item.get("id")
                subject_id = item.get("subject_id")
                subject = self.index.get(subject_id)
                if not subject:
                    self.add(diagnostic("BROKEN_REFERENCE", "Activul indică un subiect inexistent.", rel,
                                        f"{base}.subject_id", found=subject_id,
                                        expected="principiu sau exercițiu existent"))
                elif subject[0] not in {"principle", "exercise"}:
                    self.add(diagnostic("REFERENCE_TYPE_MISMATCH", "Activul indică un tip de subiect neacceptat.",
                                        rel, f"{base}.subject_id", found=subject_id,
                                        expected="principle sau exercise", related=subject[1]))
                else:
                    subject_doc = next((doc for file, _, doc in self.documents if file == subject[1]), None)
                    subject_item = next((candidate for candidate, _ in self._instances(subject[0], subject_doc)
                                         if isinstance(candidate, dict) and candidate.get("id") == subject_id), None)
                    declared = (subject_item or {}).get("visual_asset_ids")
                    if isinstance(declared, list) and asset_id not in declared:
                        self.add(diagnostic("UNUSED_REQUIRED_ASSET",
                                            "Legătura bidirecțională activ–subiect este incompletă.", rel, base,
                                            found=asset_id, related=subject[1],
                                            suggestion="Adaugă activul în visual_asset_ids al subiectului."))
                fields = ["editable_source", "static_svg", "animation_data"]
                frames = item.get("pdf_equivalent", {}).get("frames", [])
                values = [(field, item.get(field)) for field in fields] + [
                    (f"pdf_equivalent.frames[{i}]", value) for i, value in enumerate(frames)
                ]
                for field, value in values:
                    if not value:
                        continue
                    registered_files.add(str(value))
                    if not self._repo_path_exists(str(value)):
                        self.add(diagnostic("ASSET_FILE_MISSING", "Fișierul activului înregistrat lipsește.",
                                            rel, f"{base}.{field}", found=value))
        visual_ext = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif"}
        for folder in ("assets/diagrams", "assets/diagram-sequences", "assets/animations", "assets/editable"):
            base = self.root / folder
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if path.is_file() and path.suffix.lower() in visual_ext:
                    rel = safe_relative(path, self.root)
                    if rel not in registered_files:
                        self.add(diagnostic("UNREGISTERED_ASSET", "Fișierul vizual nu are manifest.", rel))
        for diagram_id, (item, rel, base) in diagram_items.items():
            if item.get("variant") == "color":
                paired_id = item.get("paired_variant_id")
                paired = diagram_items.get(paired_id)
                if not paired or paired[0].get("variant") != "black-and-white":
                    self.add(diagnostic("UNUSED_REQUIRED_ASSET",
                                        "Diagrama color nu are varianta alb-negru obligatorie.", rel,
                                        f"{base}.paired_variant_id", found=paired_id,
                                        expected="ID-ul unei diagrame black-and-white"))
        manifests = [item for rel, kind, data in self.documents if kind == "archive-manifest"
                     for item, _ in self._instances(kind, data) if isinstance(item, dict)]
        manifest_paths = {item.get("path") for item in manifests}
        source_ids = self.ids_by_type["source"]
        snapshots = self.root / "research" / "source-snapshots"
        if snapshots.exists():
            for path in snapshots.rglob("*"):
                if path.is_file() and path.name != "README.md":
                    rel = safe_relative(path, self.root)
                    if rel not in manifest_paths:
                        self.add(diagnostic("ARCHIVE_MANIFEST_MISSING",
                                            "Snapshotul arhivat nu are manifest.", rel))
        for index, item in enumerate(manifests):
            base = f"$.archives[{index}]"
            if item.get("source_id") not in source_ids:
                self.add(diagnostic("BROKEN_REFERENCE", "Manifestul indică o sursă inexistentă.",
                                    "research/archive-manifests.json", f"{base}.source_id",
                                    found=item.get("source_id")))
            manifest_path = item.get("path")
            if isinstance(manifest_path, str):
                candidate = self.root / manifest_path
                if not self._repo_path_exists(manifest_path):
                    self.add(diagnostic("OUTPUT_MISSING", "Fișierul declarat de manifest lipsește.",
                                        "research/archive-manifests.json", f"{base}.path",
                                        found=manifest_path))
                elif candidate.is_file():
                    digest = hashlib.sha256(candidate.read_bytes()).hexdigest()
                    if digest != item.get("sha256"):
                        self.add(diagnostic("HASH_MISMATCH", "Hashul snapshotului diferă de manifest.",
                                            "research/archive-manifests.json", f"{base}.sha256",
                                            found=item.get("sha256"), expected=digest))
                    if candidate.stat().st_size != item.get("size_bytes"):
                        self.add(diagnostic("VALUE_OUT_OF_RANGE", "Dimensiunea snapshotului diferă de manifest.",
                                            "research/archive-manifests.json", f"{base}.size_bytes",
                                            found=item.get("size_bytes"), expected=candidate.stat().st_size))
            if item.get("storage_level") == "C_REFERENCE_ONLY" and item.get("distribution_status") == "PUBLIC":
                self.add(diagnostic("RESTRICTED_ASSET_IN_PUBLIC_DISTRIBUTION",
                                    "O sursă restrictivă este marcată pentru distribuție publică.",
                                    "research/archive-manifests.json", f"$.archives[{index}].distribution_status"))

    def validate_pedagogy_and_text(self) -> None:
        for rel, kind, data in self.documents:
            for instance, base in self._instances(kind, data):
                self._walk_text(instance, rel, base, kind)
                if kind in {"principle", "exercise"} and isinstance(instance, dict):
                    self._validate_pedagogy(instance, rel, base, kind)
                self._walk_pedagogy_objects(instance, rel, base)

    def _walk_pedagogy_objects(self, value: Any, rel: str, path: str) -> None:
        if isinstance(value, dict):
            if "child_wording" in value and "rationales" in value:
                self._validate_pedagogy(value, rel, path)
            for key, child in value.items():
                self._walk_pedagogy_objects(child, rel, f"{path}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                self._walk_pedagogy_objects(child, rel, f"{path}[{index}]")

    def _walk_text(self, value: Any, rel: str, path: str, kind: str) -> None:
        if isinstance(value, dict):
            for key, child in value.items():
                self._walk_text(child, rel, f"{path}.{key}", kind)
        elif isinstance(value, list):
            for i, child in enumerate(value):
                self._walk_text(child, rel, f"{path}[{i}]", kind)
        elif isinstance(value, str):
            if not value.strip():
                self.add(diagnostic("EMPTY_REQUIRED_VALUE", "Textul este gol sau conține doar spații.", rel, path))
            if PLACEHOLDER_RE.search(value):
                self.add(diagnostic("PLACEHOLDER_DETECTED", "A fost detectat text placeholder.", rel, path,
                                    found=value))
            if MULTISPACE_RE.search(value):
                self.add(diagnostic("TEXT_QUALITY_ISSUE", "Textul conține spații multiple.", rel, path,
                                    severity="WARNING", found=value))
            if kind in {"principle", "exercise", "session", "message", "communication-script",
                        "case-study", "chapter"} and RAW_URL_RE.search(value):
                self.add(diagnostic("TEXT_QUALITY_ISSUE", "Textul publicabil conține un URL brut.", rel, path,
                                    severity="WARNING"))
            if kind in {"principle", "exercise", "session", "message", "communication-script",
                        "case-study", "chapter"}:
                if re.search(r"<\s*(?:script|iframe|style)\b", value, flags=re.IGNORECASE):
                    self.add(diagnostic("TEXT_QUALITY_ISSUE", "Textul publicabil conține markup executabil.", rel, path))
                if "\n\n\n\n" in value:
                    self.add(diagnostic("TEXT_QUALITY_ISSUE", "Textul conține linii goale excesive.", rel, path,
                                        severity="WARNING"))
                english_hits = len(re.findall(r"(?i)\b(?:the|this|that|with|should|player|coach|because)\b", value))
                if english_hits >= 3:
                    self.add(diagnostic("TEXT_QUALITY_ISSUE", "Câmpul publicabil pare să conțină text accidental în engleză.",
                                        rel, path, severity="WARNING", found=value))

    def _validate_pedagogy(self, item: dict[str, Any], rel: str, base: str, kind: str = "principle") -> None:
        keys = set(item)
        # exercise.schema.json nu definește coach_meaning (additionalProperties: false) —
        # sensul pentru antrenor e acoperit acolo de why_this_message + problem_being_solved.
        applicable_fields = PEDAGOGICAL_FIELDS - {"coach_meaning"} if kind == "exercise" else PEDAGOGICAL_FIELDS
        missing = [field for field in applicable_fields if field not in keys]
        # Acceptă aliasurile istorice între scheme.
        alias_groups = [
            {"child_wording", "child_message"}, {"why_this_wording", "why_this_message"},
            {"decision_to_learn", "decision_children_must_learn"},
        ]
        for group in alias_groups:
            if keys & group:
                missing = [field for field in missing if field not in group]
        if missing:
            self.add(diagnostic("PEDAGOGICAL_RATIONALE_MISSING", "Fundamentarea pedagogică nu are toate componentele.",
                                rel, base, found=sorted(missing)))
        rationales = item.get("rationales")
        if not isinstance(rationales, dict):
            self.add(diagnostic("PEDAGOGICAL_RATIONALE_MISSING", "Obiectul rationales lipsește.", rel,
                                f"{base}.rationales"))
            return
        required = RATIONALE_FIELDS
        absent = sorted(field for field in required if not isinstance(rationales.get(field), str) or not rationales[field].strip())
        if absent:
            self.add(diagnostic("PEDAGOGICAL_RATIONALE_INCOMPLETE", "Justificările profesionale sunt incomplete.",
                                rel, f"{base}.rationales", found=absent))
        generic = re.compile(r"(?i)^\s*(?:pentru a învăța|este important|ajută copilul)\.?\s*$")
        explanatory_values = []
        for key in PEDAGOGICAL_FIELDS:
            value = item.get(key)
            if isinstance(value, str):
                explanatory_values.append((key, value.strip()))
        explanatory_values.extend((f"rationales.{key}", str(value).strip()) for key, value in rationales.items())
        for key, value in explanatory_values:
            if generic.fullmatch(value) or (key.startswith("rationales.") and len(value) < 24):
                self.add(diagnostic("PEDAGOGICAL_RATIONALE_INCOMPLETE",
                                    "Textul nu explică suficient mecanismul urmărit.", rel, f"{base}.{key}",
                                    found=value, expected="o explicație cauzală și contextuală"))
        normalized = [re.sub(r"\s+", " ", value.casefold()) for _, value in explanatory_values if len(value) >= 24]
        duplicates = [text for text, count in Counter(normalized).items() if count > 1]
        if duplicates:
            self.add(diagnostic("DUPLICATE_CONTENT_DETECTED",
                                "Aceeași justificare este copiată în câmpuri distincte.", rel, base,
                                found=duplicates[0]))

    def run(self, selected_file: str | None = None, selected_type: str | None = None) -> list[Diagnostic]:
        try:
            self.load_schemas()
            self.discover(selected_file, selected_type)
            self.validate_schemas()
            self.build_index()
            self.validate_references()
            self.validate_pedagogy_and_text()
        except Exception as exc:  # Numai defectele validatorului ajung aici.
            detail = traceback.format_exc() if self.debug else type(exc).__name__
            self.add(diagnostic("SCHEMA_INVALID", "Validatorul a întâlnit o eroare internă.",
                                "<validator>", found=detail,
                                suggestion="Rulează cu --debug și deschide un task de remediere."))
        self.diagnostics.sort(key=Diagnostic.sort_key)
        return self.diagnostics


def render_human(items: list[Diagnostic]) -> str:
    if not items:
        return "VALID: 0 erori, 0 avertismente, 0 informații"
    lines = []
    for item in items:
        lines.append(f"{item.severity} {item.code} {item.file} {item.json_path}: {item.message}")
        if item.suggestion:
            lines.append(f"  Sugestie: {item.suggestion}")
    counts = Counter(item.severity for item in items)
    lines.append(f"Rezultat: {counts['ERROR']} erori, {counts['WARNING']} avertismente, {counts['INFO']} informații")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--file", help="Cale relativă la repository pentru un singur fișier.")
    selection.add_argument("--type", choices=sorted(SCHEMA_TYPES), help="Validează numai tipul indicat.")
    parser.add_argument("--format", choices=("human", "json"), default="human")
    parser.add_argument("--strict", action="store_true", help="Transformă WARNING în ERROR.")
    parser.add_argument("--debug", action="store_true", help="Include detalii tehnice pentru erori interne.")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    validator = ContentValidator(args.root, strict=args.strict, debug=args.debug)
    items = validator.run(args.file, args.type)
    if args.format == "json":
        print(json.dumps({
            "valid": not any(item.severity == "ERROR" for item in items),
            "diagnostics": [item.to_dict() for item in items],
        }, ensure_ascii=False, indent=2))
    else:
        print(render_human(items))
    return 1 if any(item.severity == "ERROR" for item in items) else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
