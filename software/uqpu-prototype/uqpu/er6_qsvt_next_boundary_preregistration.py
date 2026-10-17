"""Preregister the last ER6 QSVT prefix below frozen absolute ceilings.

The 1/2/3/5/8-query hosted certificates are the only measured inputs.  The
planner scans integer query counts without changing the existing 900-second,
750 MB and 500,000-byte stops.  It selects ten queries because the conservative
QASM envelope is below 500,000 bytes there and above it at eleven queries.

This is MODEL_ONLY experiment planning.  It is not a ten-query execution,
degree-81 feasibility result, provider authorization, or advantage evidence.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from statistics import median
from typing import Any

from .er6_qsvt_prefix_growth_falsifier import (
    ABSOLUTE_SAFETY_CEILINGS,
    DETERMINISTIC_METRICS,
    DIAGNOSTIC_METRICS,
    RESIDUAL_TOLERANCE,
    load_measured_series,
)


WORK_ID = "QOS-AUDIT-010B14"
UPSTREAM_WORK_ID = "QOS-AUDIT-010B13"
ROOT = Path(__file__).resolve().parents[3]
EIGHT_QUERY_CERTIFICATE = (
    ROOT / "benchmarks/results/cycle008-delta12-er6-qsvt-eight-query-qiskit.json"
)
MEASURED_QUERY_COUNTS = [1, 2, 3, 5, 8]
SCAN_QUERY_COUNTS = list(range(9, 82))


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def _fit(points: list[tuple[int, int]], query_count: int) -> dict[str, float]:
    slopes = [
        (right_y - left_y) / (right_x - left_x)
        for index, (left_x, left_y) in enumerate(points)
        for right_x, right_y in points[index + 1 :]
    ]
    slope = float(median(slopes))
    intercept = float(median([value - slope * queries for queries, value in points]))
    residual = float(
        max(abs(value - (intercept + slope * queries)) for queries, value in points)
    )
    prediction = intercept + slope * query_count
    return {
        "method": "Theil-Sen median pairwise slope with median intercept",
        "slope_per_query": slope,
        "intercept": intercept,
        "max_observed_abs_residual": residual,
        "prediction": prediction,
        "conservative_upper": float(math.ceil(prediction + 3.0 * residual)),
    }


def load_boundary_series() -> tuple[dict[int, dict[str, int]], list[dict[str, Any]]]:
    series, sources = load_measured_series()
    document = json.loads(EIGHT_QUERY_CERTIFICATE.read_text(encoding="utf-8"))
    if document.get("passed") is not True:
        raise ValueError("eight-query source certificate did not pass")
    resources = document["resources"]
    if resources.get("queries") != 8:
        raise ValueError("eight-query source certificate query mismatch")
    if resources.get("provider_jobs") != 0 or resources.get("shots") != 0:
        raise ValueError("eight-query source must remain zero-provider-job evidence")
    series[8] = {
        metric: int(resources[metric])
        for metric in DETERMINISTIC_METRICS + DIAGNOSTIC_METRICS
    }
    sources.append({
        "path": str(EIGHT_QUERY_CERTIFICATE.relative_to(ROOT)),
        "sha256": _sha256_bytes(EIGHT_QUERY_CERTIFICATE.read_bytes()),
        "work_id": document["work_id"],
        "evidence_class": document["evidence_class"],
        "provenance": document["provenance"],
    })
    return series, sorted(sources, key=lambda item: item["path"])


def _scan(series: dict[int, dict[str, int]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for query_count in SCAN_QUERY_COUNTS:
        models = {
            metric: _fit(
                [(queries, series[queries][metric]) for queries in MEASURED_QUERY_COUNTS],
                query_count,
            )
            for metric in DETERMINISTIC_METRICS + DIAGNOSTIC_METRICS
        }
        absolute_failures = [
            metric
            for metric, ceiling in ABSOLUTE_SAFETY_CEILINGS.items()
            if models[metric]["conservative_upper"] > ceiling
        ]
        rows.append({
            "queries": query_count,
            "conservative_upper": {
                metric: int(models[metric]["conservative_upper"])
                for metric in DETERMINISTIC_METRICS + DIAGNOSTIC_METRICS
            },
            "planning_absolute_failures": absolute_failures,
            "planning_feasible": not absolute_failures,
        })
    return rows


def build_preregistration() -> dict[str, Any]:
    series, sources = load_boundary_series()
    scan = _scan(series)
    feasible = [row for row in scan if row["planning_feasible"]]
    selected = feasible[-1]
    first_blocked = next(row for row in scan if row["queries"] > selected["queries"])
    result = {
        "schema": "uqpu-er6-qsvt-next-boundary-preregistration-v1",
        "work_id": WORK_ID,
        "upstream_work_id": UPSTREAM_WORK_ID,
        "date": "2026-10-17",
        "evidence_class": "MODEL_ONLY",
        "measured_query_counts": MEASURED_QUERY_COUNTS,
        "source_certificates": sources,
        "measured_series": {str(key): value for key, value in sorted(series.items())},
        "selection": {
            "method": "largest integer query count whose conservative envelopes remain below every unchanged absolute ceiling",
            "selected_query_count": selected["queries"],
            "selected_conservative_upper": selected["conservative_upper"],
            "first_blocked_query_count": first_blocked["queries"],
            "first_blocked_metrics": first_blocked["planning_absolute_failures"],
            "scan_upper_query_count": SCAN_QUERY_COUNTS[-1],
        },
        "acceptance": {
            "workload_sectors_required": 64,
            "unique_eigenvalues_required": 7,
            "matrix_and_state_recurrences_required": True,
            "raw_residual_tolerance": RESIDUAL_TOLERANCE,
            "deterministic_metric_model_limits": {
                metric: selected["conservative_upper"][metric]
                for metric in DETERMINISTIC_METRICS
            },
            "absolute_safety_ceilings": ABSOLUTE_SAFETY_CEILINGS,
            "stop_on_any_residual_or_absolute_safety_failure": True,
            "no_threshold_change_after_execution": True,
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "nonclaims": [
            "not an executed ten-query circuit",
            "not degree-81 synthesis or feasibility evidence",
            "not target-aware, real-QPU, energy, cost, advantage, or replacement evidence",
            "host runtime and memory are shared-runner planning diagnostics",
        ],
    }
    result["contract_sha256"] = _sha256_json(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id_mismatch")
    if contract.get("measured_query_counts") != MEASURED_QUERY_COUNTS:
        errors.append("measured_query_counts_mismatch")
    selection = contract.get("selection", {})
    if selection.get("selected_query_count") != 10:
        errors.append("selected_query_count_mismatch")
    if selection.get("first_blocked_query_count") != 11:
        errors.append("first_blocked_query_count_mismatch")
    if "serialized_openqasm2_bytes" not in selection.get("first_blocked_metrics", []):
        errors.append("qasm_boundary_not_proven")
    acceptance = contract.get("acceptance", {})
    if acceptance.get("absolute_safety_ceilings") != ABSOLUTE_SAFETY_CEILINGS:
        errors.append("absolute_safety_ceiling_mismatch")
    if acceptance.get("no_threshold_change_after_execution") is not True:
        errors.append("threshold_freeze_missing")
    authorization = contract.get("authorization", {})
    if authorization.get("provider_submission") is not False:
        errors.append("provider_submission_must_be_false")
    if authorization.get("paid_execution") is not False:
        errors.append("paid_execution_must_be_false")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256_json(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))
