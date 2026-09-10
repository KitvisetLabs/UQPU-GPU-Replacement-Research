"""Diagnostics connecting routed control durations to ideal physical limits.

This module deliberately avoids claiming that a calibrated gate duration is an
orthogonal-state transition or that a quantum speed limit is achievable.  It
only computes the inverse Margolus-Levitin energy scale associated with each
non-zero unitary instruction duration.  A true observed-to-bound gap requires a
measured mean energy above the ground state for the *same physical evolution*.
"""
from __future__ import annotations

from collections import Counter, defaultdict
import math

from .fundamental_limits import (
    margolus_levitin_equivalent_frequency_hz,
    margolus_levitin_required_mean_energy_joule,
)


def _stats(values: list[float]) -> dict | None:
    clean = sorted(float(v) for v in values if math.isfinite(float(v)))
    if not clean:
        return None
    n = len(clean)
    return {
        "count": n,
        "min": clean[0],
        "median": clean[n // 2],
        "mean": sum(clean) / n,
        "max": clean[-1],
    }


def summarize_ml_duration_requirements(
    calibration: dict,
    *,
    unitary_operations: tuple[str, ...] = ("x", "sx", "cz", "ecr"),
) -> dict:
    """Summarize inverse ML energy scales for calibrated instruction durations.

    ``calibration`` is expected to contain ``used_instruction_instances`` as
    emitted by :func:`uqpu.target_calibration.active_instruction_calibration`.
    Measurement, virtual zero-duration instructions and operations outside the
    declared unitary set are intentionally excluded.

    The returned energy/frequency values answer only this counterfactual
    question: "what mean energy above ground would make the ML lower bound equal
    this duration?"  They are not measurements of the backend's control energy.
    """
    rows_in = calibration.get("used_instruction_instances")
    if not isinstance(rows_in, list):
        raise ValueError("calibration must contain used_instruction_instances list")

    allowed = set(unitary_operations)
    included = []
    excluded = Counter()
    durations_by_op: dict[str, list[float]] = defaultdict(list)
    energies_by_op: dict[str, list[float]] = defaultdict(list)
    freq_by_op: dict[str, list[float]] = defaultdict(list)

    for row in rows_in:
        operation = str(row.get("operation", ""))
        duration_raw = row.get("duration_seconds")

        if operation not in allowed:
            excluded[f"operation:{operation or 'unknown'}"] += 1
            continue
        if duration_raw is None:
            excluded["missing_duration"] += 1
            continue

        duration = float(duration_raw)
        if not math.isfinite(duration) or duration <= 0.0:
            excluded["nonpositive_or_invalid_duration"] += 1
            continue

        required_energy = margolus_levitin_required_mean_energy_joule(duration)
        equivalent_frequency = margolus_levitin_equivalent_frequency_hz(duration)
        record = {
            "operation": operation,
            "physical_qubits": list(row.get("physical_qubits", [])),
            "duration_seconds": duration,
            "ml_required_mean_energy_joule_for_equal_bound": required_energy,
            "ml_equivalent_energy_frequency_hz": equivalent_frequency,
        }
        included.append(record)
        durations_by_op[operation].append(duration)
        energies_by_op[operation].append(required_energy)
        freq_by_op[operation].append(equivalent_frequency)

    summary = {}
    for operation in sorted(durations_by_op):
        summary[operation] = {
            "duration_seconds": _stats(durations_by_op[operation]),
            "ml_required_mean_energy_joule_for_equal_bound": _stats(
                energies_by_op[operation]
            ),
            "ml_equivalent_energy_frequency_hz": _stats(freq_by_op[operation]),
        }

    return {
        "schema": "uqpu-ml-control-duration-diagnostic-v1",
        "interpretation": "inverse_bound_requirement_only",
        "unitary_operations_considered": sorted(allowed),
        "included_instruction_count": len(included),
        "included_instruction_instances": included,
        "excluded_instruction_counts": dict(sorted(excluded.items())),
        "summary_by_operation": summary,
        "summed_included_instruction_duration_seconds": sum(
            row["duration_seconds"] for row in included
        ),
        "summed_duration_is_wall_clock_latency": False,
        "actual_mean_energy_above_ground_measured": False,
        "true_observed_to_ml_bound_ratio_available": False,
        "missing_for_true_gap": [
            "mean energy above ground for the same physical evolution",
            "proof that the compared evolution matches the orthogonal-state ML setting",
            "pulse/control resource accounting",
            "wall-plug and cryogenic energy accounting",
        ],
    }
