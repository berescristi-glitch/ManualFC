from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .codes import ERROR_CODES, SEVERITY_ORDER


@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: str
    message: str
    file: str
    json_path: str = "$"
    found_value: Any = None
    expected: str | None = None
    related_file: str | None = None
    suggestion: str | None = None

    def __post_init__(self) -> None:
        if self.code not in ERROR_CODES:
            raise ValueError(f"Cod de diagnostic necunoscut: {self.code}")
        if self.severity not in SEVERITY_ORDER:
            raise ValueError(f"Severitate necunoscută: {self.severity}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def sort_key(self) -> tuple:
        return (SEVERITY_ORDER[self.severity], self.file, self.json_path, self.code, self.message)
