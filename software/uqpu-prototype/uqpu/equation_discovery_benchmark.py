"""Matched held-out error metrics for equation-discovery robustness trials.

This module checks experimental bookkeeping and score thresholds only. It does
not prove semantic equivalence, establish a physical law, or validate a device.
Equivalence certificate hashes are provenance identifiers; an independent
checker must establish that each transformation preserves the intended meaning.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
import math
import re

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_EQUIVALENCE_STATUSES = {"CHECKED_EQUIVALENCE", "UNVERIFIED", "FAILED"}


def _normalize_group_ids(name: str, values: Iterable[str]) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError(f"{name} must be a collection of group IDs, not a string")
    try:
        group_ids = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be iterable") from exc
    if not group_ids:
        raise ValueError(f"{name} must not be empty")
    if any(not isinstance(item, str) or not item.strip() for item in group_ids):
        raise ValueError(f"{name} entries must be nonempty strings")
    if len(set(group_ids)) != len(group_ids):
        raise ValueError(f"{name} contains duplicate group IDs")
    return tuple(sorted(group_ids))


def validate_grouped_splits(
    train_group_ids: Iterable[str],
    validation_group_ids: Iterable[str],
    test_group_ids: Iterable[str],
) -> dict[str, tuple[str, ...]]:
    """Validate nonempty, pairwise-disjoint group splits and return stable order.

    Group IDs should identify the highest-level unit that could leak related
    observations (equation family, physical system, experiment or specimen),
    not merely individual rows.
    """
    splits = {
        "train": _normalize_group_ids("train_group_ids", train_group_ids),
        "validation": _normalize_group_ids("validation_group_ids", validation_group_ids),
        "test": _normalize_group_ids("test_group_ids", test_group_ids),
    }
    sets = {name: set(ids) for name, ids in splits.items()}
    names = tuple(splits)
    for i, left in enumerate(names):
        for right in names[i + 1:]:
            overlap = sets[left] & sets[right]
            if overlap:
                raise ValueError(
                    f"group IDs overlap between {left} and {right}: {sorted(overlap)}"
                )
    return splits


def compare_matched_heldout_errors(
    baseline_errors: Mapping[str, float],
    candidate_errors: Mapping[str, float],
    equivalence_statuses: Mapping[str, str],
    equivalence_certificate_sha256: Mapping[str, str],
    *,
    max_relative_regression: float = 0.05,
    minimum_cases: int = 3,
) -> dict[str, object]:
    """Summarize paired errors under matched held-out transformations/cases.

    The metric gate passes only when mean candidate/baseline error is below one,
    no case regresses beyond the configured fraction, and every transformation
    is marked CHECKED_EQUIVALENCE. That status is caller-supplied and is not
    independently verified here. Baseline errors must be strictly positive.
    """
    if not isinstance(baseline_errors, Mapping) or not isinstance(candidate_errors, Mapping):
        raise ValueError("baseline_errors and candidate_errors must be mappings")
    if not isinstance(equivalence_statuses, Mapping):
        raise ValueError("equivalence_statuses must be a mapping")
    if not isinstance(equivalence_certificate_sha256, Mapping):
        raise ValueError("equivalence_certificate_sha256 must be a mapping")
    if not isinstance(minimum_cases, int) or isinstance(minimum_cases, bool) or minimum_cases < 3:
        raise ValueError("minimum_cases must be an integer >= 3")
    try:
        regression_limit = float(max_relative_regression)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError("max_relative_regression must be finite and >= 0") from exc
    if not math.isfinite(regression_limit) or regression_limit < 0:
        raise ValueError("max_relative_regression must be finite and >= 0")

    keys = set(baseline_errors)
    if not keys or len(keys) < minimum_cases:
        raise ValueError(f"at least {minimum_cases} matched cases are required")
    if any(not isinstance(key, str) or not key.strip() for key in keys):
        raise ValueError("case IDs must be nonempty strings")
    if set(candidate_errors) != keys:
        raise ValueError("baseline and candidate must use identical case IDs")
    if set(equivalence_statuses) != keys:
        raise ValueError("equivalence statuses must cover exactly the matched case IDs")
    if set(equivalence_certificate_sha256) != keys:
        raise ValueError("equivalence certificate hashes must cover exactly the matched case IDs")

    rows: list[dict[str, object]] = []
    ratios: list[float] = []
    for case_id in sorted(keys):
        status = equivalence_statuses[case_id]
        if status not in _EQUIVALENCE_STATUSES:
            raise ValueError(f"unknown equivalence status for {case_id}: {status}")
        certificate_hash = equivalence_certificate_sha256[case_id]
        if not isinstance(certificate_hash, str) or not _SHA256.fullmatch(certificate_hash):
            raise ValueError(f"equivalence certificate for {case_id} must be a lowercase SHA-256 hex digest")
        values: list[float] = []
        for label, source in (("baseline", baseline_errors), ("candidate", candidate_errors)):
            value = source[case_id]
            if isinstance(value, bool):
                raise ValueError(f"{label} error for {case_id} must be numeric, not bool")
            try:
                number = float(value)
            except (TypeError, ValueError, OverflowError) as exc:
                raise ValueError(f"{label} error for {case_id} must be finite") from exc
            if not math.isfinite(number) or number < 0:
                raise ValueError(f"{label} error for {case_id} must be finite and >= 0")
            if label == "baseline" and number <= 0:
                raise ValueError(f"baseline error for {case_id} must be > 0 for ratio comparison")
            values.append(number)
        baseline, candidate = values
        ratio = candidate / baseline
        ratios.append(ratio)
        rows.append({
            "case_id": case_id,
            "baseline_error": baseline,
            "candidate_error": candidate,
            "candidate_to_baseline_ratio": ratio,
            "relative_improvement": 1.0 - ratio,
            "equivalence_status": status,
            "equivalence_certificate_sha256": certificate_hash,
        })

    mean_ratio = math.fsum(ratios) / len(ratios)
    worst_relative_regression = max(0.0, max(ratios) - 1.0)
    metric_conditions_passed = (
        mean_ratio < 1.0 and worst_relative_regression <= regression_limit
    )
    equivalence_conditions_passed = all(
        equivalence_statuses[key] == "CHECKED_EQUIVALENCE" for key in keys
    )
    return {
        "case_results": rows,
        "case_count": len(rows),
        "mean_candidate_to_baseline_ratio": mean_ratio,
        "mean_relative_improvement": 1.0 - mean_ratio,
        "worst_relative_regression": worst_relative_regression,
        "max_relative_regression_limit": regression_limit,
        "metric_conditions_passed": metric_conditions_passed,
        "equivalence_conditions_passed": equivalence_conditions_passed,
        "metric_gate_passed": metric_conditions_passed and equivalence_conditions_passed,
        "evidence_class": "MODEL_ONLY_METRIC_SUMMARY",
        "claim_boundary": "not proof of semantic equivalence, physical truth, application acceptance or technology advantage",
    }
