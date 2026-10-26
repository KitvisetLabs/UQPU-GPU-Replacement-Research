"""Record-level evidence contract for formal proof artifacts.

This module binds a declared proof-check result to exact statement, proof-artifact,
and log bytes. It does not execute a prover, authenticate a toolchain, establish
novelty, or turn a mathematical result into an empirical physical law.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import re


PROOF_STATUSES = frozenset(
    {
        "NOT_RUN",
        "PROOF_TEXT_ONLY",
        "FORMAL_STATEMENT",
        "KERNEL_CHECKED",
        "INDEPENDENTLY_REPRODUCED",
        "FAILED",
        "INCONCLUSIVE",
    }
)
CLAIM_KINDS = frozenset(
    {"MATHEMATICAL_THEOREM", "PHYSICAL_EQUATION_HYPOTHESIS", "ENGINEERING_CLAIM"}
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_IMMUTABLE_REVISION = re.compile(r"^(?:[0-9a-f]{40}|[0-9a-f]{64})$")
_CHECKED_STATUSES = frozenset({"KERNEL_CHECKED", "INDEPENDENTLY_REPRODUCED"})


def sha256_hex(payload: bytes) -> str:
    """Return the SHA-256 digest of exact bytes, without text normalization."""
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class FormalProofEvidence:
    claim_id: str
    claim_kind: str
    statement: str
    statement_sha256: str
    assumptions: tuple[str, ...]
    status: str
    source_revision: str = ""
    proof_artifact_sha256: str = ""
    checker_name: str = ""
    checker_version: str = ""
    checker_command: str = ""
    environment_sha256: str = ""
    run_log_sha256: str = ""
    checker_exit_code: int | None = None
    independent_reproduction_count: int = 0
    notes: tuple[str, ...] = ()

    def validate_metadata(self) -> None:
        """Validate declared metadata; this is not a proof-checking operation."""
        if not self.claim_id.strip():
            raise ValueError("claim_id is required")
        if self.claim_kind not in CLAIM_KINDS:
            raise ValueError("unknown claim_kind")
        if not self.statement.strip():
            raise ValueError("statement is required")
        if self.statement_sha256 != sha256_hex(self.statement.encode("utf-8")):
            raise ValueError("statement_sha256 does not match the exact UTF-8 statement")
        if not self.assumptions or any(not item.strip() for item in self.assumptions):
            raise ValueError("explicit nonempty assumptions are required")
        if self.status not in PROOF_STATUSES:
            raise ValueError("unknown proof status")
        if self.independent_reproduction_count < 0:
            raise ValueError("independent_reproduction_count cannot be negative")
        if any(not item.strip() for item in self.notes):
            raise ValueError("notes must contain nonempty strings")

        if self.status in _CHECKED_STATUSES:
            if not _IMMUTABLE_REVISION.fullmatch(self.source_revision):
                raise ValueError("checked proof requires an immutable 40- or 64-character source revision")
            for field_name in ("proof_artifact_sha256", "environment_sha256", "run_log_sha256"):
                if not _SHA256.fullmatch(getattr(self, field_name)):
                    raise ValueError(f"{field_name} must be a lowercase SHA-256 digest")
            for field_name in ("checker_name", "checker_version", "checker_command"):
                if not getattr(self, field_name).strip():
                    raise ValueError(f"{field_name} is required for a checked proof")
            if self.checker_exit_code != 0:
                raise ValueError("a checked proof must record checker_exit_code=0")
        elif self.status == "FAILED":
            if self.checker_exit_code in (None, 0):
                raise ValueError("FAILED requires a recorded nonzero checker exit code")
            if not self.notes:
                raise ValueError("FAILED requires a note describing the failed attempt")
            if not _IMMUTABLE_REVISION.fullmatch(self.source_revision):
                raise ValueError("FAILED attempt requires an immutable source revision")
            for field_name in ("proof_artifact_sha256", "environment_sha256", "run_log_sha256"):
                if not _SHA256.fullmatch(getattr(self, field_name)):
                    raise ValueError(f"{field_name} must be a lowercase SHA-256 digest")
            for field_name in ("checker_name", "checker_version", "checker_command"):
                if not getattr(self, field_name).strip():
                    raise ValueError(f"{field_name} is required for a failed proof attempt")
        elif self.status == "INCONCLUSIVE" and not self.notes:
            raise ValueError("INCONCLUSIVE requires a note explaining the unresolved result")

        if self.status == "INDEPENDENTLY_REPRODUCED" and self.independent_reproduction_count < 1:
            raise ValueError("INDEPENDENTLY_REPRODUCED requires at least one independent reproduction")

    def verify_artifact_bytes(self, proof_artifact: bytes, run_log: bytes) -> "ArtifactIntegrityResult":
        """Check that supplied proof/log bytes match this record's declared hashes.

        A successful result verifies byte binding only. It does not rerun the checker,
        authenticate who ran it, validate proof semantics, or establish physical truth.
        """
        self.validate_metadata()
        if self.status not in _CHECKED_STATUSES | {"FAILED"}:
            raise ValueError("artifact-byte verification requires a checked or failed attempt")
        if sha256_hex(proof_artifact) != self.proof_artifact_sha256:
            raise ValueError("proof artifact bytes do not match proof_artifact_sha256")
        if sha256_hex(run_log) != self.run_log_sha256:
            raise ValueError("run log bytes do not match run_log_sha256")
        return ArtifactIntegrityResult(
            claim_id=self.claim_id,
            status=self.status,
            statement_sha256=self.statement_sha256,
            proof_artifact_sha256=self.proof_artifact_sha256,
            run_log_sha256=self.run_log_sha256,
            record_integrity_verified=True,
            independent_reproduction_recorded=(self.status == "INDEPENDENTLY_REPRODUCED"),
            empirical_physics_established=False,
            note=(
                "Exact bytes match the declared hashes. This does not execute or authenticate the prover, "
                "certify novelty, or establish an empirical physical law."
            ),
        )


@dataclass(frozen=True)
class ArtifactIntegrityResult:
    claim_id: str
    status: str
    statement_sha256: str
    proof_artifact_sha256: str
    run_log_sha256: str
    record_integrity_verified: bool
    independent_reproduction_recorded: bool
    empirical_physics_established: bool
    note: str


def build_formal_proof_evidence(
    *,
    claim_id: str,
    claim_kind: str,
    statement: str,
    assumptions: tuple[str, ...],
    status: str,
    source_revision: str = "",
    proof_artifact: bytes | None = None,
    checker_name: str = "",
    checker_version: str = "",
    checker_command: str = "",
    environment_bytes: bytes | None = None,
    run_log: bytes | None = None,
    checker_exit_code: int | None = None,
    independent_reproduction_count: int = 0,
    notes: tuple[str, ...] = (),
) -> FormalProofEvidence:
    """Build a record from exact bytes, then validate its metadata."""
    record = FormalProofEvidence(
        claim_id=claim_id,
        claim_kind=claim_kind,
        statement=statement,
        statement_sha256=sha256_hex(statement.encode("utf-8")),
        assumptions=assumptions,
        status=status,
        source_revision=source_revision,
        proof_artifact_sha256=sha256_hex(proof_artifact) if proof_artifact is not None else "",
        checker_name=checker_name,
        checker_version=checker_version,
        checker_command=checker_command,
        environment_sha256=sha256_hex(environment_bytes) if environment_bytes is not None else "",
        run_log_sha256=sha256_hex(run_log) if run_log is not None else "",
        checker_exit_code=checker_exit_code,
        independent_reproduction_count=independent_reproduction_count,
        notes=notes,
    )
    record.validate_metadata()
    return record
