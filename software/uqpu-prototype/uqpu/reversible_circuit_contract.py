"""Fail-closed contract for evaluator-checked reversible quantum subroutines.

This module validates candidate metadata; it does not simulate a circuit, prove a
claim, estimate wall-plug energy, or establish useful-task/economic advantage.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import re

_SHA256 = re.compile(r"\A[0-9a-f]{64}\Z")
_VERIFICATION_STATUSES = {
    "UNVERIFIED",
    "EXHAUSTIVE_PASS",
    "FORMAL_PROOF_CHECKED",
    "INDEPENDENT_REPLICA_PASS",
    "FAILED",
    "INCOMPARABLE",
}
_VERIFIED_STATUSES = {
    "EXHAUSTIVE_PASS",
    "FORMAL_PROOF_CHECKED",
    "INDEPENDENT_REPLICA_PASS",
}
_PHASE_STATUSES = {
    "UNVERIFIED",
    "EXACT_RELATIVE_PHASE_PASS",
    "FORMAL_PHASE_PROOF_CHECKED",
    "FAILED",
}
_PHASE_PASS_STATUSES = {"EXACT_RELATIVE_PHASE_PASS", "FORMAL_PHASE_PROOF_CHECKED"}
_ANCILLA_STATUSES = {
    "UNVERIFIED",
    "EXHAUSTIVE_ZERO_PASS",
    "FORMAL_ZERO_PROOF_CHECKED",
    "FAILED",
}
_ANCILLA_PASS_STATUSES = {"EXHAUSTIVE_ZERO_PASS", "FORMAL_ZERO_PROOF_CHECKED"}


def _is_sha256(value: object) -> bool:
    return isinstance(value, str) and _SHA256.fullmatch(value) is not None


def _require_text(name: str, value: object) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")


def _require_nonnegative_int(name: str, value: object) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive_int(name: str, value: object) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class ReversibleCircuitCandidate:
    """Evidence record for comparing two implementations of the same function.

    peak_qubits includes input, output, and all live ancillas. Verification
    status is metadata about a recorded procedure, not an automatic proof of
    the procedure's correctness or independence.
    """

    candidate_id: str
    function_id: str
    function_spec_sha256: str
    candidate_sha256: str
    generator_id: str
    evaluator_id: str
    evaluator_sha256: str
    input_width_bits: int
    output_width_bits: int
    peak_qubits: int
    toffoli_count: int
    t_depth: int
    logical_depth: int
    failure_probability_upper_bound: float
    allowed_failure_probability: float
    verification_status: str = "UNVERIFIED"
    exhaustive_basis_states_checked: int = 0
    verification_artifact_sha256: str | None = None
    proof_artifact_sha256: str | None = None
    independent_replica_sha256: str | None = None
    phase_check_status: str = "UNVERIFIED"
    ancilla_cleanup_status: str = "UNVERIFIED"
    target_id: str | None = None

    def validate(self) -> None:
        for name in ("candidate_id", "function_id", "generator_id", "evaluator_id"):
            _require_text(name, getattr(self, name))
        if self.generator_id.strip() == self.evaluator_id.strip():
            raise ValueError("generator_id and evaluator_id must be distinct roles")

        for name in ("function_spec_sha256", "candidate_sha256", "evaluator_sha256"):
            if not _is_sha256(getattr(self, name)):
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")

        _require_positive_int("input_width_bits", self.input_width_bits)
        _require_positive_int("output_width_bits", self.output_width_bits)
        _require_positive_int("peak_qubits", self.peak_qubits)
        if self.peak_qubits < self.input_width_bits + self.output_width_bits:
            raise ValueError("peak_qubits must include at least input and output registers")
        for name in ("toffoli_count", "t_depth", "logical_depth", "exhaustive_basis_states_checked"):
            _require_nonnegative_int(name, getattr(self, name))

        expected_basis_states = 1 << (self.input_width_bits + self.output_width_bits)
        if self.exhaustive_basis_states_checked > expected_basis_states:
            raise ValueError("exhaustive_basis_states_checked exceeds the declared basis domain")
        if self.verification_status not in _VERIFICATION_STATUSES:
            raise ValueError("unknown verification_status")
        if self.phase_check_status not in _PHASE_STATUSES:
            raise ValueError("unknown phase_check_status")
        if self.ancilla_cleanup_status not in _ANCILLA_STATUSES:
            raise ValueError("unknown ancilla_cleanup_status")

        for name in ("failure_probability_upper_bound", "allowed_failure_probability"):
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                raise ValueError(f"{name} must be finite")
        if not 0.0 <= self.failure_probability_upper_bound <= 1.0:
            raise ValueError("failure_probability_upper_bound must be in [0, 1]")
        if not 0.0 <= self.allowed_failure_probability < 1.0:
            raise ValueError("allowed_failure_probability must be in [0, 1)")

        for name in ("verification_artifact_sha256", "proof_artifact_sha256", "independent_replica_sha256"):
            value = getattr(self, name)
            if value is not None and not _is_sha256(value):
                raise ValueError(f"{name} must be None or a lowercase SHA-256 hex digest")
        if self.target_id is not None:
            _require_text("target_id", self.target_id)

        if self.verification_status == "EXHAUSTIVE_PASS":
            if self.exhaustive_basis_states_checked != expected_basis_states:
                raise ValueError("EXHAUSTIVE_PASS requires every declared input/output basis state")
        if self.verification_status in _VERIFIED_STATUSES and self.verification_artifact_sha256 is None:
            raise ValueError("verified candidates require verification_artifact_sha256")
        if self.verification_status == "FORMAL_PROOF_CHECKED" and self.proof_artifact_sha256 is None:
            raise ValueError("FORMAL_PROOF_CHECKED requires proof_artifact_sha256")
        if self.verification_status == "INDEPENDENT_REPLICA_PASS" and self.independent_replica_sha256 is None:
            raise ValueError("INDEPENDENT_REPLICA_PASS requires independent_replica_sha256")
        if (
            self.phase_check_status == "FORMAL_PHASE_PROOF_CHECKED"
            or self.ancilla_cleanup_status == "FORMAL_ZERO_PROOF_CHECKED"
        ) and self.proof_artifact_sha256 is None:
            raise ValueError("formal phase/ancilla checks require proof_artifact_sha256")

    @property
    def eligible_for_resource_comparison(self) -> bool:
        """Eligibility for logical-resource comparison only, never cost promotion."""
        try:
            self.validate()
        except ValueError:
            return False
        return (
            self.verification_status in _VERIFIED_STATUSES
            and self.phase_check_status in _PHASE_PASS_STATUSES
            and self.ancilla_cleanup_status in _ANCILLA_PASS_STATUSES
            and self.failure_probability_upper_bound <= self.allowed_failure_probability
        )

    @property
    def toffoli_qubit_proxy(self) -> int:
        """A descriptive T*Q proxy only; it is not a cost or advantage metric."""
        return self.toffoli_count * self.peak_qubits


def compare_resource_frontier(
    candidate_a: ReversibleCircuitCandidate,
    candidate_b: ReversibleCircuitCandidate,
) -> str:
    """Compare verified candidates only when their semantic/error contracts match.

    Returns A_DOMINATES_B, B_DOMINATES_A, EQUIVALENT, TRADEOFF,
    INCOMPARABLE, or BLOCKED_UNVERIFIED. Metrics are logical resource proxies;
    target-native cost and accepted useful-task economics remain separate gates.
    """
    candidate_a.validate()
    candidate_b.validate()
    if not candidate_a.eligible_for_resource_comparison or not candidate_b.eligible_for_resource_comparison:
        return "BLOCKED_UNVERIFIED"

    same_contract = (
        candidate_a.function_id == candidate_b.function_id
        and candidate_a.function_spec_sha256 == candidate_b.function_spec_sha256
        and candidate_a.input_width_bits == candidate_b.input_width_bits
        and candidate_a.output_width_bits == candidate_b.output_width_bits
        and candidate_a.allowed_failure_probability == candidate_b.allowed_failure_probability
        and candidate_a.target_id == candidate_b.target_id
    )
    if not same_contract:
        return "INCOMPARABLE"

    metrics_a = (
        candidate_a.toffoli_count,
        candidate_a.peak_qubits,
        candidate_a.t_depth,
        candidate_a.logical_depth,
        candidate_a.failure_probability_upper_bound,
    )
    metrics_b = (
        candidate_b.toffoli_count,
        candidate_b.peak_qubits,
        candidate_b.t_depth,
        candidate_b.logical_depth,
        candidate_b.failure_probability_upper_bound,
    )
    a_no_worse = all(a <= b for a, b in zip(metrics_a, metrics_b))
    b_no_worse = all(b <= a for a, b in zip(metrics_a, metrics_b))
    if metrics_a == metrics_b:
        return "EQUIVALENT"
    if a_no_worse and any(a < b for a, b in zip(metrics_a, metrics_b)):
        return "A_DOMINATES_B"
    if b_no_worse and any(b < a for a, b in zip(metrics_a, metrics_b)):
        return "B_DOMINATES_A"
    return "TRADEOFF"
