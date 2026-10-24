"""Small analytic audit for the GHZ example in arXiv:2610.29146.

This is a MODEL_ONLY consistency check of the paper's worked example and its
stated score-class/ancilla-dimension precondition. It does not reproduce the
paper's general no-go proof or establish a physical result.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import math
from typing import Any


@dataclass(frozen=True)
class QFITransferAudit:
    system_qubits: int
    ancilla_dimension: int
    phase_radians: float
    theoretical_system_qfi: float
    direct_measurement_cfi: float
    distinct_nonzero_score_classes: int
    theorem_2_precondition_m_gt_n: bool
    ghz_formula_check_passed: bool
    evidence_class: str = "MODEL_ONLY"
    provider_jobs: int = 0
    shots: int = 0
    measured_energy_j: float | None = None
    measured_cost: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self) | {
            "nonclaims": [
                "not an independent proof of Theorem 2",
                "not a real-QPU experiment",
                "not a memory/storage equivalence result",
                "not evidence of quantum advantage or a new physical law",
            ]
        }


def _positive_integer(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def ghz_outcome_probabilities(system_qubits: int, phase_radians: float) -> tuple[float, ...]:
    """Return probabilities for each computational-basis outcome.

    The state is (|0...0> + exp(i*N*x)|1...1>)/sqrt(2), measured after
    H**N. Outcome probability depends on the Hamming-weight parity.
    """
    n = _positive_integer("system_qubits", system_qubits)
    x = float(phase_radians)
    if not math.isfinite(x):
        raise ValueError("phase_radians must be finite")
    c = math.cos(n * x)
    return tuple((1.0 + (-1 if index.bit_count() % 2 else 1) * c) / (2**n)
                 for index in range(2**n))


def ghz_direct_measurement_cfi(system_qubits: int, phase_radians: float) -> float:
    """Compute classical Fisher information of the paper's H**N measurement.

    Singular phase points where an outcome has zero probability are rejected;
    use a generic interior phase for this regular-score calculation.
    """
    n = _positive_integer("system_qubits", system_qubits)
    x = float(phase_radians)
    if not math.isfinite(x):
        raise ValueError("phase_radians must be finite")
    s = math.sin(n * x)
    c = math.cos(n * x)
    if abs(s) < 1e-12 or abs(1.0 - abs(c)) < 1e-12:
        raise ValueError("phase is singular for the regular CFI calculation")
    total = 0.0
    for index in range(2**n):
        parity_sign = -1.0 if index.bit_count() % 2 else 1.0
        probability = (1.0 + parity_sign * c) / (2**n)
        derivative = -parity_sign * n * s / (2**n)
        total += derivative * derivative / probability
    return total


def distinct_nonzero_score_classes(system_qubits: int, phase_radians: float,
                                   tolerance: float = 1e-9) -> int:
    """Count distinct nonzero d(log p_i)/dx values for the GHZ measurement."""
    n = _positive_integer("system_qubits", system_qubits)
    x = float(phase_radians)
    tol = float(tolerance)
    if not math.isfinite(x) or not math.isfinite(tol) or tol <= 0:
        raise ValueError("phase must be finite and tolerance must be finite and > 0")
    c = math.cos(n * x)
    s = math.sin(n * x)
    if abs(s) < 1e-12 or abs(1.0 - abs(c)) < 1e-12:
        raise ValueError("phase is singular for score-class counting")
    scores = set()
    for index in range(2**n):
        parity_sign = -1.0 if index.bit_count() % 2 else 1.0
        probability = (1.0 + parity_sign * c) / (2**n)
        derivative = -parity_sign * n * s / (2**n)
        score = derivative / probability
        if abs(score) > tol:
            scores.add(round(score / tol) * tol)
    return len(scores)


def audit_ghz_qfi_transfer(system_qubits: int, phase_radians: float,
                           ancilla_dimension: int, tolerance: float = 1e-8) -> QFITransferAudit:
    """Audit the GHZ worked example and report only the theorem's precondition.

    theorem_2_precondition_m_gt_n flags when the paper's stated necessary
    condition for a perfect protocol is violated. A false flag does not prove
    attainability; a true flag is not an independent proof of the theorem.
    """
    n = _positive_integer("system_qubits", system_qubits)
    d = _positive_integer("ancilla_dimension", ancilla_dimension)
    cfi = ghz_direct_measurement_cfi(n, phase_radians)
    score_classes = distinct_nonzero_score_classes(n, phase_radians)
    target = float(n * n)
    passed = math.isclose(cfi, target, rel_tol=tolerance, abs_tol=tolerance)
    return QFITransferAudit(
        system_qubits=n,
        ancilla_dimension=d,
        phase_radians=float(phase_radians),
        theoretical_system_qfi=target,
        direct_measurement_cfi=cfi,
        distinct_nonzero_score_classes=score_classes,
        theorem_2_precondition_m_gt_n=score_classes > d,
        ghz_formula_check_passed=passed,
    )
