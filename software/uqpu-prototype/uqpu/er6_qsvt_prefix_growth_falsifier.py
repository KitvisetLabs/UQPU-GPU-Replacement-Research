"""Pre-register the next ER6 QSVT prefix resource-growth falsifier.

This module consumes only persisted, provenance-bearing 1/2/3/5-query
certificates.  It freezes an eight-query experiment and separate model-growth
and absolute-safety gates before that experiment is run.  Its predictions are
MODEL_ONLY planning controls, not degree-81, provider, energy, cost, advantage,
or replacement evidence.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
from statistics import median
from typing import Any


WORK_ID = "QOS-AUDIT-010B12"
ROOT = Path(__file__).resolve().parents[3]
NEXT_QUERY_COUNT = 8
SOURCE_FILES = {
    1: ROOT / "benchmarks/results/cycle008-delta07-er6-lcu-qsvt-one-query-qiskit.json",
    2: ROOT / "benchmarks/results/cycle008-delta08-er6-lcu-qsvt-two-query-qiskit.json",
    3: ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-qiskit.json",
    5: ROOT / "benchmarks/results/cycle008-delta10-er6-lcu-qsvt-bounded-prefix-qiskit.json",
}
DETERMINISTIC_METRICS = (
    "decomposed_depth",
    "decomposed_size",
    "serialized_openqasm2_bytes",
    "cx",
    "rz",
    "sx",
    "x",
)
DIAGNOSTIC_METRICS = ("host_runtime_ns", "host_peak_traced_bytes")
ABSOLUTE_SAFETY_CEILINGS = {
    "host_runtime_ns": 900_000_000_000,
    "host_peak_traced_bytes": 750_000_000,
    "serialized_openqasm2_bytes": 500_000,
}
RESIDUAL_TOLERANCE = 2e-12


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    )


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _resources_for_query(document: dict[str, Any], queries: int) -> dict[str, Any]:
    if "prefix_results" in document:
        matches = [item for item in document["prefix_results"] if item["queries"] == queries]
        if len(matches) != 1:
            raise ValueError(f"expected exactly one {queries}-query prefix result")
        return matches[0]["resources"]
    resources = document["resources"]
    if resources["logical_block_queries"] != queries:
        raise ValueError(f"source certificate does not contain {queries} queries")
    return resources


def load_measured_series() -> tuple[dict[int, dict[str, int]], list[dict[str, Any]]]:
    series: dict[int, dict[str, int]] = {}
    sources: list[dict[str, Any]] = []
    loaded: dict[Path, dict[str, Any]] = {}
    for queries, path in SOURCE_FILES.items():
        document = loaded.setdefault(path, _load_json(path))
        if document.get("passed") is not True:
            raise ValueError(f"source certificate did not pass: {path.name}")
        resources = _resources_for_query(document, queries)
        if resources.get("provider_jobs") != 0 or resources.get("shots") != 0:
            raise ValueError("source must remain a zero-provider-job simulation certificate")
        row = {
            "decomposed_depth": int(resources["decomposed_depth"]),
            "decomposed_size": int(resources["decomposed_size"]),
            "serialized_openqasm2_bytes": int(resources["serialized_openqasm2_bytes"]),
            "host_runtime_ns": int(resources["host_runtime_ns"]),
            "host_peak_traced_bytes": int(resources["host_peak_traced_bytes"]),
        }
        counts = resources["decomposed_operation_counts"]
        row.update({gate: int(counts.get(gate, 0)) for gate in ("cx", "rz", "sx", "x")})
        series[queries] = row
    for path, document in loaded.items():
        sources.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": _sha256_bytes(path.read_bytes()),
            "work_id": document["work_id"],
            "evidence_class": document["evidence_class"],
            "provenance": document["provenance"],
        })
    return series, sorted(sources, key=lambda item: item["path"])


def _robust_affine_fit(points: list[tuple[int, int]]) -> dict[str, float]:
    slopes = [
        (right_y - left_y) / (right_x - left_x)
        for index, (left_x, left_y) in enumerate(points)
        for right_x, right_y in points[index + 1 :]
    ]
    slope = float(median(slopes))
    intercept = float(median([value - slope * queries for queries, value in points]))
    residuals = [abs(value - (intercept + slope * queries)) for queries, value in points]
    prediction = intercept + slope * NEXT_QUERY_COUNT
    max_abs_residual = float(max(residuals))
    return {
        "method": "Theil-Sen median pairwise slope with median intercept",
        "slope_per_query": slope,
        "intercept": intercept,
        "max_observed_abs_residual": max_abs_residual,
        "prediction_at_next_query": prediction,
        "model_rejection_upper": float(math.ceil(prediction + 3.0 * max_abs_residual)),
    }


def build_preregistration() -> dict[str, Any]:
    series, sources = load_measured_series()
    query_counts = sorted(series)
    models = {}
    for metric in DETERMINISTIC_METRICS + DIAGNOSTIC_METRICS:
        fit = _robust_affine_fit([(queries, series[queries][metric]) for queries in query_counts])
        fit["gate_role"] = (
            "model_growth_falsifier" if metric in DETERMINISTIC_METRICS
            else "diagnostic_only_due_to_shared_runner_variance"
        )
        models[metric] = fit
    result = {
        "schema": "uqpu-er6-qsvt-prefix-growth-preregistration-v1",
        "work_id": WORK_ID,
        "upstream_work_id": "QOS-AUDIT-010B11",
        "date": "2026-10-17",
        "evidence_class": "MODEL_ONLY",
        "measured_query_counts": query_counts,
        "next_query_count": NEXT_QUERY_COUNT,
        "source_certificates": sources,
        "measured_series": {str(key): value for key, value in series.items()},
        "models": models,
        "acceptance": {
            "workload_sectors_required": 64,
            "unique_eigenvalues_required": 7,
            "matrix_and_state_recurrences_required": True,
            "raw_residual_tolerance": RESIDUAL_TOLERANCE,
            "deterministic_metric_model_limits": {
                metric: int(models[metric]["model_rejection_upper"])
                for metric in DETERMINISTIC_METRICS
            },
            "absolute_safety_ceilings": ABSOLUTE_SAFETY_CEILINGS,
            "stop_on_any_residual_or_absolute_safety_failure": True,
            "model_rejection_does_not_retroactively_change_thresholds": True,
        },
        "interpretation": {
            "model_accepted_if": "all deterministic metrics are at or below their frozen model limits",
            "model_rejected_if": "any deterministic metric exceeds its frozen model limit",
            "experiment_stopped_if": "residual or any absolute safety ceiling fails",
            "runtime_and_memory": "recorded but excluded from model acceptance because shared-runner noise is not controlled",
        },
        "authorization": {"provider_submission": False, "paid_execution": False},
        "nonclaims": [
            "not an executed eight-query circuit",
            "not degree-81 synthesis or a degree-81 feasibility estimate",
            "not target-aware, real-QPU, energy, cost, advantage, or replacement evidence",
        ],
    }
    result["contract_sha256"] = _sha256_json(result)
    return result


def validate_preregistration(contract: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if contract.get("work_id") != WORK_ID:
        errors.append("work_id_mismatch")
    if contract.get("measured_query_counts") != [1, 2, 3, 5]:
        errors.append("measured_query_ladder_mismatch")
    if contract.get("next_query_count") != NEXT_QUERY_COUNT:
        errors.append("next_query_count_mismatch")
    acceptance = contract.get("acceptance", {})
    if set(acceptance.get("deterministic_metric_model_limits", {})) != set(DETERMINISTIC_METRICS):
        errors.append("deterministic_metric_limits_mismatch")
    if acceptance.get("absolute_safety_ceilings") != ABSOLUTE_SAFETY_CEILINGS:
        errors.append("absolute_safety_ceiling_mismatch")
    if acceptance.get("stop_on_any_residual_or_absolute_safety_failure") is not True:
        errors.append("stop_on_failure_missing")
    auth = contract.get("authorization", {})
    if auth.get("provider_submission") is not False or auth.get("paid_execution") is not False:
        errors.append("authorization_must_fail_closed")
    digest = contract.get("contract_sha256")
    body = {key: value for key, value in contract.items() if key != "contract_sha256"}
    if digest != _sha256_json(body):
        errors.append("contract_digest_mismatch")
    return sorted(set(errors))


def evaluate_eight_query_result(contract: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    if validate_preregistration(contract):
        raise ValueError("invalid preregistration contract")
    if result.get("queries") != NEXT_QUERY_COUNT:
        raise ValueError("result query count does not match preregistration")
    deterministic_failures = [
        metric
        for metric, limit in contract["acceptance"]["deterministic_metric_model_limits"].items()
        if int(result[metric]) > int(limit)
    ]
    safety_failures = [
        metric
        for metric, limit in contract["acceptance"]["absolute_safety_ceilings"].items()
        if int(result[metric]) > int(limit)
    ]
    residual_failed = float(result["max_raw_residual"]) > RESIDUAL_TOLERANCE
    authorization_failed = result.get("provider_jobs") != 0 or result.get("shots") != 0
    return {
        "model_growth_accepted": not deterministic_failures,
        "deterministic_metric_failures": deterministic_failures,
        "absolute_safety_failures": safety_failures,
        "residual_failed": residual_failed,
        "authorization_failed": authorization_failed,
        "experiment_accepted": not (
            safety_failures or residual_failed or authorization_failed
        ),
    }

