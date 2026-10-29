"""Fail-closed acceptance gate for synthetic equation-discovery candidates.

This gate combines held-out numerical accuracy with a separately measured
finite-perturbation diagnostic and explicit constraint/failure counts. It is
not a physical-law verifier and does not implement the published EIC method.
"""
from __future__ import annotations

import math
from collections.abc import Iterable


def _finite_vector(name: str, values: Iterable[object]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{name} must be a non-string iterable")
    try:
        raw = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be iterable") from exc
    if not raw:
        raise ValueError(f"{name} must not be empty")
    result: list[float] = []
    for value in raw:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} values must be numeric and not boolean")
        number = float(value)
        if not math.isfinite(number):
            raise ValueError(f"{name} values must be finite")
        result.append(number)
    return tuple(result)


def _finite_nonnegative(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric and not boolean")
    number = float(value)
    if not math.isfinite(number) or number < 0.0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return number


def _nonnegative_count(name: str, value: object) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def evaluate_candidate_acceptance(
    reference_outputs: Iterable[object],
    candidate_outputs: Iterable[object],
    output_scales: Iterable[object],
    measured_perturbation_amplification: object,
    max_normalized_rms_error: object,
    max_perturbation_amplification: object,
    constraint_violations: object = 0,
    numerical_failures: object = 0,
) -> dict[str, object]:
    """Evaluate a candidate under thresholds frozen before the comparison.

    Acceptance requires every gate to pass. A low perturbation score cannot
    compensate for poor held-out accuracy, and a low error cannot compensate
    for instability, constraint violations, or numerical failures.
    """
    reference = _finite_vector("reference_outputs", reference_outputs)
    candidate = _finite_vector("candidate_outputs", candidate_outputs)
    scales = _finite_vector("output_scales", output_scales)
    if len(reference) != len(candidate) or len(reference) != len(scales):
        raise ValueError("reference, candidate, and scales must have equal lengths")
    if any(scale <= 0.0 for scale in scales):
        raise ValueError("output scales must be strictly positive")

    max_error = _finite_nonnegative("max_normalized_rms_error", max_normalized_rms_error)
    amplification = _finite_nonnegative(
        "measured_perturbation_amplification",
        measured_perturbation_amplification,
    )
    max_amplification = _finite_nonnegative(
        "max_perturbation_amplification", max_perturbation_amplification
    )
    violations = _nonnegative_count("constraint_violations", constraint_violations)
    failures = _nonnegative_count("numerical_failures", numerical_failures)

    normalized_squared_errors = [
        ((actual - target) / scale) ** 2
        for actual, target, scale in zip(candidate, reference, scales)
    ]
    normalized_rms_error = math.sqrt(math.fsum(normalized_squared_errors) / len(reference))
    if not math.isfinite(normalized_rms_error):
        raise ValueError("normalized RMS error must be finite")

    reasons: list[str] = []
    if normalized_rms_error > max_error:
        reasons.append("HELDOUT_ACCURACY_THRESHOLD_FAILED")
    if amplification > max_amplification:
        reasons.append("PERTURBATION_STABILITY_THRESHOLD_FAILED")
    if violations:
        reasons.append("PHYSICS_OR_DOMAIN_CONSTRAINT_VIOLATION")
    if failures:
        reasons.append("NUMERICAL_FAILURE_PRESENT")

    return {
        "gate_id": "EQN-CANDIDATE-ACCEPTANCE-001",
        "evidence_class": "MODEL_ONLY_SYNTHETIC_EQUATION_EVALUATION",
        "accepted_for_synthetic_benchmark": not reasons,
        "metrics": {
            "normalized_rms_error": normalized_rms_error,
            "measured_perturbation_amplification": amplification,
            "constraint_violations": violations,
            "numerical_failures": failures,
        },
        "thresholds": {
            "max_normalized_rms_error": max_error,
            "max_perturbation_amplification": max_amplification,
        },
        "rejection_reasons": reasons,
        "claim_boundary": (
            "Acceptance is only a synthetic benchmark gate. It does not prove "
            "equation equivalence, physical truth, a new law, device/material/"
            "fuel/fusion/finance advantage, or real-QPU benefit."
        ),
    }
