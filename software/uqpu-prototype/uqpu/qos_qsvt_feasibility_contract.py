"""Preregistration and provenance contract for QSP/QSVT feasibility work.

This module does not implement a QSP/M-QSP theorem or decide polynomial
feasibility. It freezes the metadata and fail-closed boundaries required before
a theorem-backed feasibility result can be independently audited. A recorded
classification is not yet permission to skip synthesis, a hardware claim, or
a physical/economic result.
"""
from __future__ import annotations

import math
import re
from dataclasses import dataclass

MODEL_CLASSES = {"UNIVARIATE_QSP", "MULTIVARIATE_QSP", "UNKNOWN_CHANNEL_QSVT"}
DECISIONS = {"FEASIBLE", "INFEASIBLE", "UNKNOWN"}
RUN_STATUSES = {"PREREGISTERED_ONLY", "THEOREM_CHECKED", "TOOL_ERROR", "UNRESOLVED"}
_SHA256 = re.compile(r"[0-9a-f]{64}")


@dataclass(frozen=True)
class QSVTFeasibilityFixture:
    fixture_id: str
    model_class: str
    source_reference: str
    statement_sha256: str
    specification: str
    expected_decision: str
    scope_note: str
    signal_variables: tuple[str, ...] = ()
    signal_operator_count: int | None = None
    channel_dimension: int | None = None
    delta: float | None = None
    error_metric: str | None = None
    oracle_access_model: str | None = None
    query_count_bound_reference: str | None = None

    def validate(self) -> None:
        for name in ("fixture_id", "source_reference", "specification", "scope_note"):
            if not str(getattr(self, name)).strip():
                raise ValueError(f"{name} is required")
        if self.model_class not in MODEL_CLASSES:
            raise ValueError(f"unsupported model_class: {self.model_class}")
        if not _SHA256.fullmatch(self.statement_sha256):
            raise ValueError("statement_sha256 must be a lowercase SHA-256 hex digest")
        if self.expected_decision not in DECISIONS:
            raise ValueError("expected_decision must be FEASIBLE, INFEASIBLE, or UNKNOWN")

        if self.model_class in {"UNIVARIATE_QSP", "MULTIVARIATE_QSP"}:
            if not self.signal_variables or any(not v.strip() for v in self.signal_variables):
                raise ValueError("QSP fixtures require named signal variables")
            expected_minimum = 1 if self.model_class == "UNIVARIATE_QSP" else 2
            if len(self.signal_variables) < expected_minimum:
                raise ValueError(f"{self.model_class} requires at least {expected_minimum} signal variable(s)")
            if self.model_class == "UNIVARIATE_QSP" and len(self.signal_variables) != 1:
                raise ValueError("UNIVARIATE_QSP requires exactly one signal variable")
            if not isinstance(self.signal_operator_count, int) or isinstance(self.signal_operator_count, bool):
                raise ValueError("signal_operator_count must be an integer")
            if self.signal_operator_count < 1:
                raise ValueError("signal_operator_count must be >= 1")
        else:
            if not isinstance(self.channel_dimension, int) or isinstance(self.channel_dimension, bool):
                raise ValueError("UNKNOWN_CHANNEL_QSVT requires an integer channel_dimension")
            if self.channel_dimension < 2:
                raise ValueError("channel_dimension must be >= 2")
            if self.delta is None or not math.isfinite(float(self.delta)) or not 0.0 < float(self.delta) < 1.0:
                raise ValueError("delta must be finite and strictly between 0 and 1")
            if self.error_metric != "diamond_norm":
                raise ValueError("unknown-channel QSVT must name diamond_norm as its error metric")
            if not str(self.oracle_access_model or "").strip():
                raise ValueError("oracle_access_model is required")
            if not str(self.query_count_bound_reference or "").strip():
                raise ValueError("query_count_bound_reference is required")


@dataclass(frozen=True)
class QSVTFeasibilityRunRecord:
    fixture_id: str
    statement_sha256: str
    status: str
    decision: str | None = None
    theorem_scope: str = ""
    certificate_reference: str = ""


@dataclass(frozen=True)
class QSVTFeasibilityGateDecision:
    status: str
    recorded_decision: str | None
    independent_audit_required: bool
    may_skip_synthesis: bool
    may_claim_mathematical_infeasibility: bool
    may_claim_hardware_advantage: bool
    next_gate: str


def classify_feasibility_record(
    fixture: QSVTFeasibilityFixture,
    record: QSVTFeasibilityRunRecord,
) -> QSVTFeasibilityGateDecision:
    """Classify record completeness without certifying the theorem or physics."""
    safe_flags = {
        "independent_audit_required": False,
        "may_skip_synthesis": False,
        "may_claim_mathematical_infeasibility": False,
        "may_claim_hardware_advantage": False,
    }
    try:
        fixture.validate()
    except (TypeError, ValueError):
        return QSVTFeasibilityGateDecision(
            "PROVENANCE_INVALID", None, **safe_flags,
            next_gate="repair fixture metadata and freeze the exact input hash",
        )

    if record.fixture_id != fixture.fixture_id or record.statement_sha256 != fixture.statement_sha256:
        return QSVTFeasibilityGateDecision(
            "PROVENANCE_INVALID", None, **safe_flags,
            next_gate="re-run against the exact preregistered fixture and hash",
        )
    if record.status not in RUN_STATUSES:
        return QSVTFeasibilityGateDecision(
            "UNRESOLVED", None, **safe_flags,
            next_gate="use a governed run status and preserve the raw output",
        )
    if record.status == "TOOL_ERROR":
        return QSVTFeasibilityGateDecision(
            "TOOL_BLOCKED", None, **safe_flags,
            next_gate="repair or independently replace the tool; do not infer mathematical infeasibility",
        )
    if record.status != "THEOREM_CHECKED":
        return QSVTFeasibilityGateDecision(
            "PREREGISTRATION_ONLY" if record.status == "PREREGISTERED_ONLY" else "UNRESOLVED",
            None, **safe_flags,
            next_gate="implement the cited theorem and independently check the result",
        )
    if (
        record.decision not in DECISIONS
        or not record.theorem_scope.strip()
        or not record.certificate_reference.strip()
    ):
        return QSVTFeasibilityGateDecision(
            "RESULT_INCOMPLETE", None, **safe_flags,
            next_gate="attach the exact theorem scope and auditable proof/certificate artifact",
        )
    if record.decision == "UNKNOWN":
        return QSVTFeasibilityGateDecision(
            "UNRESOLVED", "UNKNOWN", **safe_flags,
            next_gate="retain the fixture as unresolved and add a counterexample or stronger certificate",
        )
    if record.decision != fixture.expected_decision:
        return QSVTFeasibilityGateDecision(
            "EXPECTED_DECISION_MISMATCH", record.decision, **safe_flags,
            next_gate="preserve the counterexample and independently audit theorem scope, input hash, and classification",
        )

    return QSVTFeasibilityGateDecision(
        "READY_FOR_INDEPENDENT_AUDIT",
        record.decision,
        independent_audit_required=True,
        may_skip_synthesis=False,
        may_claim_mathematical_infeasibility=False,
        may_claim_hardware_advantage=False,
        next_gate="independent theorem/certificate review, deterministic replay, then target-aware resource accounting",
    )
