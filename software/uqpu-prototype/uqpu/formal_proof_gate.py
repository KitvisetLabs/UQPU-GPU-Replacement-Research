"""Metadata gate for formally checked theorem candidates.

This module validates provenance and consistency fields reported by external
proof checkers. It does not parse or check proof objects and never establishes
physical truth. A checker must actually validate the proof in its own trusted
kernel; an independent replay record must come from a distinct checker build.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import re

_RESULTS = frozenset({"NOT_RUN", "PASS", "REJECTED", "ERROR"})
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def sha256_hex(data: bytes | str) -> str:
    """Return a canonical lowercase SHA-256 digest for bytes or UTF-8 text."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    if not isinstance(data, bytes):
        raise TypeError("data must be bytes or str")
    return sha256(data).hexdigest()


def _valid_digest(value: object) -> bool:
    """Accept only canonical lowercase SHA-256 strings."""
    return isinstance(value, str) and bool(_SHA256_RE.fullmatch(value))


@dataclass(frozen=True)
class FormalProofRecord:
    """Provenance record for a candidate theorem and external proof-check runs.

    A complete record is evidence that the required metadata was captured, not
    a replacement for independently inspecting the proof checker or its logs.
    """

    theorem_id: str
    statement: str
    axiom_set_sha256: str = ""
    proof_object_sha256: str = ""
    checker_id: str = ""
    checker_version: str = ""
    checker_image_sha256: str = ""
    checker_result: str = "NOT_RUN"
    checker_exit_code: int | None = None
    checker_log_sha256: str = ""
    independent_checker_id: str = ""
    independent_checker_version: str = ""
    independent_checker_image_sha256: str = ""
    independent_result: str = "NOT_RUN"
    independent_exit_code: int | None = None
    independent_log_sha256: str = ""
    independent_axiom_set_sha256: str = ""
    independent_proof_object_sha256: str = ""
    independent_statement_sha256: str = ""

    def validate(self) -> None:
        for name in (
            "theorem_id",
            "statement",
            "checker_id",
            "checker_version",
            "independent_checker_id",
            "independent_checker_version",
        ):
            if not isinstance(getattr(self, name), str):
                raise ValueError(f"{name} must be a string")
        if not self.theorem_id.strip():
            raise ValueError("theorem_id is required")
        if not self.statement.strip():
            raise ValueError("statement is required")

        for name in ("checker_result", "independent_result"):
            value = getattr(self, name)
            if not isinstance(value, str) or value not in _RESULTS:
                raise ValueError(f"unknown or non-string {name}")

        for name in ("checker_exit_code", "independent_exit_code"):
            value = getattr(self, name)
            if value is not None and (
                isinstance(value, bool) or not isinstance(value, int)
            ):
                raise ValueError(f"{name} must be an integer or None")

        for name in (
            "axiom_set_sha256",
            "proof_object_sha256",
            "checker_image_sha256",
            "checker_log_sha256",
            "independent_checker_image_sha256",
            "independent_log_sha256",
            "independent_axiom_set_sha256",
            "independent_proof_object_sha256",
            "independent_statement_sha256",
        ):
            value = getattr(self, name)
            if not isinstance(value, str):
                raise ValueError(f"{name} must be a string")
            if value and not _valid_digest(value):
                raise ValueError(
                    f"{name} must be a 64-character lowercase SHA-256 hex digest"
                )

        if self.checker_result == "PASS" and self.checker_exit_code != 0:
            raise ValueError("primary PASS requires checker_exit_code == 0")
        if (
            self.independent_result == "PASS"
            and self.independent_exit_code != 0
        ):
            raise ValueError(
                "independent PASS requires independent_exit_code == 0"
            )

    @property
    def statement_sha256(self) -> str:
        if not isinstance(self.statement, str):
            raise ValueError("statement must be a string")
        return sha256_hex(self.statement)

    @property
    def has_complete_primary_check_record(self) -> bool:
        """True only when a successful primary checker record is complete."""
        try:
            self.validate()
        except ValueError:
            return False
        return all((
            bool(self.checker_id.strip()),
            bool(self.checker_version.strip()),
            self.checker_result == "PASS",
            self.checker_exit_code == 0,
            _valid_digest(self.axiom_set_sha256),
            _valid_digest(self.proof_object_sha256),
            _valid_digest(self.checker_image_sha256),
            _valid_digest(self.checker_log_sha256),
        ))

    @property
    def has_complete_independent_replay_record(self) -> bool:
        """Require a distinct checker build to replay the same statement/axioms/proof."""
        try:
            self.validate()
        except ValueError:
            return False
        return all((
            self.has_complete_primary_check_record,
            bool(self.independent_checker_id.strip()),
            bool(self.independent_checker_version.strip()),
            self.independent_result == "PASS",
            self.independent_exit_code == 0,
            _valid_digest(self.independent_checker_image_sha256),
            _valid_digest(self.independent_log_sha256),
            self.independent_checker_id != self.checker_id,
            self.independent_checker_image_sha256
            != self.checker_image_sha256,
            self.independent_axiom_set_sha256 == self.axiom_set_sha256,
            self.independent_proof_object_sha256 == self.proof_object_sha256,
            self.independent_statement_sha256 == self.statement_sha256,
        ))

    @property
    def audit_status(self) -> str:
        """Report metadata state only; no status means a physical law is proven."""
        try:
            self.validate()
        except ValueError:
            return "INVALID_METADATA"
        if self.checker_result in {"REJECTED", "ERROR"} or (
            self.independent_result in {"REJECTED", "ERROR"}
        ):
            return "FAILED_OR_COUNTEREXAMPLE"
        if self.has_complete_independent_replay_record:
            return "INDEPENDENT_REPLAY_METADATA_COMPLETE"
        if self.has_complete_primary_check_record:
            return "PRIMARY_CHECK_METADATA_COMPLETE"
        return "UNVERIFIED"
