"""Cycle 005 Delta 01 reproducible measurements and fail-closed gates.

This module advances all twelve synchronized research lanes without promoting a
model, source lookup, synthetic fixture, or local software measurement into a
QPU, materials, economic, biological, or physical-law result.  Provider
submission, fabrication, purchases, funding, and human/physical SCM work are
deliberately outside the executable surface.
"""
from __future__ import annotations

import hashlib
from itertools import product
import json
import os
from pathlib import Path
import platform
import re
import resource
import statistics
import tempfile
from time import perf_counter, perf_counter_ns
import tracemalloc
from typing import Any

from .cycle003_delta01 import canonical_json_bytes
from .cycle004_delta01 import validate_scm_handoff
from .scalable_qubo import greedy_bitflip, seeded_erdos_renyi_maxcut


BRAKET_CREATE_TASK_URL = (
    "https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html"
)
PYTHON_RESOURCE_URL = "https://docs.python.org/3/library/resource.html"
ZENODO_RECORD_URL = "https://zenodo.org/records/14257632"


def _sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _timing(samples: list[int]) -> dict[str, int | float]:
    if not samples or any(type(item) is not int or item < 0 for item in samples):
        raise ValueError("timing samples must be non-negative integer nanoseconds")
    return {
        "repetitions": len(samples),
        "minimum_ns": min(samples),
        "median_ns": statistics.median(samples),
        "maximum_ns": max(samples),
    }


def exact_enumeration_with_cap(
    instance,
    *,
    max_states: int,
    deadline_seconds: float,
) -> dict:
    """Enumerate a QUBO only while both explicit safety bounds remain open."""
    if type(max_states) is not int or max_states < 1:
        raise ValueError("max_states must be a positive integer")
    if not isinstance(deadline_seconds, (int, float)) or deadline_seconds <= 0:
        raise ValueError("deadline_seconds must be positive")
    variables = instance.variables
    started = perf_counter()
    best = float("inf")
    best_assignment: dict[int, int] | None = None
    states = 0
    stop_reason = "COMPLETE"
    total_states = 1 << len(variables)
    for values in product((0, 1), repeat=len(variables)):
        if states >= max_states:
            stop_reason = "STATE_CAP"
            break
        if states and perf_counter() - started >= deadline_seconds:
            stop_reason = "DEADLINE"
            break
        assignment = dict(zip(variables, values))
        objective = instance.energy(assignment)
        states += 1
        if objective < best:
            best = objective
            best_assignment = assignment
    elapsed = perf_counter() - started
    complete = stop_reason == "COMPLETE" and states == total_states
    return {
        "method": "complete_binary_enumeration_with_state_and_wall_clock_caps",
        "variables": len(variables),
        "total_state_space": total_states,
        "states_evaluated": states,
        "max_states": max_states,
        "deadline_seconds": float(deadline_seconds),
        "elapsed_seconds": elapsed,
        "stop_reason": "COMPLETE" if complete else stop_reason,
        "complete": complete,
        "best_objective": best if best_assignment is not None else None,
        "best_assignment_vn_to_v0": (
            "".join(str(best_assignment[index]) for index in reversed(variables))
            if best_assignment is not None
            else None
        ),
        "optimum_claim_allowed": complete,
    }


def benchmark_scale_case(
    node_count: int,
    seed: int,
    *,
    edge_probability: float = 0.5,
    max_states: int = 1 << 20,
    deadline_seconds: float = 30.0,
    heuristic_restarts: int = 16,
) -> dict:
    """Measure one deterministic MaxCut case on the current local process."""
    if type(node_count) is not int or node_count < 2:
        raise ValueError("node_count must be an integer of at least two")
    instance = seeded_erdos_renyi_maxcut(node_count, edge_probability, seed)
    exact = exact_enumeration_with_cap(
        instance, max_states=max_states, deadline_seconds=deadline_seconds
    )
    heuristic_started = perf_counter()
    heuristic_assignment, heuristic_objective = greedy_bitflip(
        instance, restarts=heuristic_restarts, seed=seed
    )
    heuristic_elapsed = perf_counter() - heuristic_started
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    gap = None
    if exact["complete"] and exact["best_objective"] is not None:
        gap = heuristic_objective - exact["best_objective"]
        if gap < -1e-12:
            raise AssertionError("heuristic objective is better than a declared exact optimum")
    return {
        "schema": "uqpu-cycle005-local-maxcut-scale-case-v1",
        "generator": "seeded_erdos_renyi_maxcut",
        "node_count": node_count,
        "edge_probability": edge_probability,
        "seed": seed,
        "edge_count": len(instance.quadratic),
        "exact": exact,
        "heuristic": {
            "method": "deterministic_seeded_greedy_bitflip",
            "restarts": heuristic_restarts,
            "objective": heuristic_objective,
            "assignment_vn_to_v0": "".join(
                str(heuristic_assignment[index]) for index in reversed(instance.variables)
            ),
            "elapsed_seconds": heuristic_elapsed,
            "objective_gap_to_exact": gap,
            "quality_ratio": None,
        },
        "process_peak_rss": {
            "value": peak_rss,
            "unit": "KiB on Linux; platform-dependent elsewhere",
            "semantics": "ru_maxrss high-water mark for this process, not incremental case memory",
            "source": PYTHON_RESOURCE_URL,
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "logical_cpu_count": os.cpu_count(),
        },
        "evidence_class": "LOCAL_HOST_CLASSICAL_SOFTWARE_MEASUREMENT_NOT_COMPETITIVE_BENCHMARK",
        "limitations": [
            "Cases are small deterministic screening fixtures, not established benchmark-suite instances.",
            "Peak RSS is a process high-water mark and must be measured in a fresh process for per-case comparison.",
            "No power or energy was measured and the timings are not hardware-neutral.",
            "The heuristic quality ratio is intentionally null because negative MaxCut QUBO objectives make naive ratios misleading.",
        ],
    }


def benchmark_durable_io(payload: dict, repetitions: int = 21) -> dict:
    """Measure fsync-bounded local writes plus explicitly unverified cache labels."""
    if type(repetitions) is not int or repetitions < 3:
        raise ValueError("repetitions must be an integer of at least three")
    encoded = canonical_json_bytes(payload)
    digest = hashlib.sha256(encoded).hexdigest()
    write_fsync: list[int] = []
    first_read: list[int] = []
    repeat_read: list[int] = []
    decode: list[int] = []
    peaks: dict[str, list[int]] = {
        "write_fsync": [],
        "first_read": [],
        "repeat_read": [],
        "json_decode": [],
    }

    def measure_memory_and_time(operation):
        tracemalloc.reset_peak()
        before_current, _ = tracemalloc.get_traced_memory()
        started = perf_counter_ns()
        value = operation()
        elapsed = perf_counter_ns() - started
        _, peak = tracemalloc.get_traced_memory()
        return value, elapsed, max(0, peak - before_current)

    tracemalloc.start()
    try:
        with tempfile.TemporaryDirectory(prefix="uqpu-cycle005-") as temporary:
            path = Path(temporary) / "payload.json"
            for _ in range(repetitions):
                def durable_write():
                    with path.open("wb") as handle:
                        handle.write(encoded)
                        handle.flush()
                        os.fsync(handle.fileno())

                _, elapsed, peak = measure_memory_and_time(durable_write)
                write_fsync.append(elapsed)
                peaks["write_fsync"].append(peak)

                recovered, elapsed, peak = measure_memory_and_time(path.read_bytes)
                first_read.append(elapsed)
                peaks["first_read"].append(peak)
                if hashlib.sha256(recovered).hexdigest() != digest:
                    raise ValueError("first-read persistence hash mismatch")

                repeated, elapsed, peak = measure_memory_and_time(path.read_bytes)
                repeat_read.append(elapsed)
                peaks["repeat_read"].append(peak)
                if repeated != recovered:
                    raise ValueError("repeat-read payload mismatch")

                decoded, elapsed, peak = measure_memory_and_time(
                    lambda: json.loads(repeated)
                )
                decode.append(elapsed)
                peaks["json_decode"].append(peak)
                if decoded != payload:
                    raise ValueError("decoded payload mismatch")
    finally:
        tracemalloc.stop()
    return {
        "schema": "uqpu-cycle005-local-durable-io-measurement-v1",
        "payload": {"canonical_json_utf8_bytes": len(encoded), "sha256": digest},
        "timing": {
            "write_flush_file_fsync": _timing(write_fsync),
            "post_fsync_first_read_uncontrolled_cache_state": _timing(first_read),
            "immediate_repeat_read_unverified_cache_hit": _timing(repeat_read),
            "json_decode": _timing(decode),
        },
        "python_allocation_incremental_peak_bytes": {
            name: _timing(values) for name, values in peaks.items()
        },
        "durability_boundary": {
            "file_data_fsync_called": True,
            "directory_fsync_called": False,
            "storage_device_flush_verified": False,
            "power_loss_survival_tested": False,
        },
        "cache_labels": {
            "first_read": "NOT_VERIFIED_OS_COLD",
            "repeat_read": "NOT_VERIFIED_CACHE_HIT",
        },
        "evidence_class": "LOCAL_HOST_FILE_FSYNC_AND_SOFTWARE_MEMORY_MEASUREMENT_NOT_CLOUD_IO",
        "limitations": [
            "A file fsync call is recorded, but directory durability, device flush, and power-loss survival are not verified.",
            "Neither first nor repeated read has controlled kernel/page-cache state.",
            "tracemalloc measures Python allocations, not process RSS or device memory.",
            "No provider transfer, QPU readout, network, storage service, power, or energy is measured.",
        ],
    }


def build_braket_dry_run_packet(manifest: dict) -> dict:
    """Build, but never submit, a fail-closed CreateQuantumTask request draft."""
    candidate = manifest["lane_a_b_c_qos"]["paired_circuits"][0]
    action = json.dumps(
        {
            "braketSchemaHeader": {"name": "braket.ir.openqasm.program", "version": "1"},
            "source": candidate["openqasm_3"],
        },
        separators=(",", ":"),
        sort_keys=True,
    )
    body = {
        "action": action,
        "clientToken": None,
        "deviceArn": None,
        "outputS3Bucket": None,
        "outputS3KeyPrefix": None,
        "shots": candidate["shots"],
    }
    required = [
        "action",
        "clientToken",
        "deviceArn",
        "outputS3Bucket",
        "outputS3KeyPrefix",
        "shots",
    ]
    missing = [name for name in required if body.get(name) in (None, "")]
    return {
        "schema": "uqpu-cycle005-braket-create-task-dry-run-v1",
        "api_reference": BRAKET_CREATE_TASK_URL,
        "access_date": "2026-09-28",
        "required_fields_from_api": required,
        "request_body": body,
        "action_sha256": hashlib.sha256(action.encode("utf-8")).hexdigest(),
        "validation": {
            "missing_required_fields": missing,
            "locally_complete": not missing,
            "provider_validated": False,
            "submit_method_present": False,
            "submission_allowed": False,
        },
        "authorization": {
            "credentials_used": False,
            "network_submission_attempted": False,
            "paid_job_submitted": False,
            "status": "NOT_AUTHORIZED",
        },
        "provider_observations": {
            "task_arn": None,
            "backend": None,
            "queue_time_seconds": None,
            "execution_time_seconds": None,
            "result": None,
            "bill": None,
        },
        "evidence_class": "OFFICIAL_API_SCHEMA_DRY_RUN_NOT_PROVIDER_VALIDATION_OR_EXECUTION",
    }


COST_COMPONENTS = (
    "provider_actual_bill",
    "classical_host_orchestration",
    "queue",
    "network_transfer",
    "storage",
    "retry_failure",
    "mitigation_decoder",
    "energy_cooling",
    "labor",
    "capital_amortization",
)


def complete_cost_gate(ledger: dict) -> dict:
    """Compute totals only when every lifecycle and matching prerequisite exists."""
    missing = [name for name in COST_COMPONENTS if ledger.get(name) is None]
    accepted = ledger.get("observed_accepted_outputs")
    if not isinstance(accepted, int) or accepted <= 0:
        missing.append("observed_accepted_outputs_positive_integer")
    if ledger.get("same_provider_execution_and_bill") is not True:
        missing.append("same_provider_execution_and_bill")
    if ledger.get("matched_classical_baseline") is not True:
        missing.append("matched_classical_baseline")
    total = None
    cost_per_accept = None
    if not missing:
        values = [ledger[name] for name in COST_COMPONENTS]
        if any(not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0 for value in values):
            raise ValueError("complete cost components must be non-negative numbers")
        total = sum(values)
        cost_per_accept = total / accepted
    return {
        "schema": "uqpu-cycle005-complete-cost-gate-v1",
        "required_cost_components": list(COST_COMPONENTS),
        "missing_or_invalid": missing,
        "complete": not missing,
        "total_cost_usd": total,
        "cost_per_accepted_output_usd": cost_per_accept,
        "refusal_active": bool(missing),
        "rg028_status": (
            "READY_FOR_REVIEW_NOT_AN_ECONOMIC_CLAIM"
            if not missing
            else "OPEN_DATA_CREDENTIAL_AUTHORIZATION_AND_COMPLETENESS_BLOCKED"
        ),
        "non_claim": "A locally complete synthetic ledger would test arithmetic only; it would not establish commercial economics.",
    }


MATERIAL_REQUIREMENTS = (
    "current_full_method_text",
    "authenticated_pangola_species_and_lot",
    "feedstock_moisture_and_ash",
    "resin_hardener_sku_and_ratio",
    "cure_schedule",
    "coupon_dimensions_and_uncertainty",
    "vna_fixture_calibration_and_dynamic_range",
    "same_protocol_incumbent_coupon",
    "safety_and_waste_review",
)


def build_material_evidence_registry() -> dict:
    slots = []
    for index, requirement in enumerate(MATERIAL_REQUIREMENTS, start=1):
        slots.append(
            {
                "prerequisite_id": f"DMF-PR-{index:02d}",
                "requirement": requirement,
                "acceptance": {
                    "artifact_uri_required": True,
                    "sha256_required": True,
                    "issuer_or_operator_required": True,
                    "observation_or_effective_date_required": True,
                    "reviewer_required": True,
                },
                "evidence": {
                    "artifact_uri": None,
                    "sha256": None,
                    "issuer_or_operator": None,
                    "date": None,
                    "reviewer": None,
                },
                "satisfied": False,
                "immutability_status": "EMPTY_SLOT_FAILS_CLOSED",
            }
        )
    return {
        "schema": "uqpu-cycle005-material-evidence-registry-v1",
        "study_id": "DMF-BIOCARBON-EMI-001",
        "slots": slots,
        "satisfied_count": 0,
        "required_count": len(slots),
        "readiness_status": "NOT_READY_NO_FABRICATION_AUTHORIZED",
        "fabrication_authorized": False,
        "evidence_class": "IMMUTABLE_EVIDENCE_SLOT_SCHEMA_NO_MATERIAL_MEASUREMENT",
    }


def build_chain_of_custody_schema() -> dict:
    stages = [
        "feedstock_receipt",
        "feedstock_preparation",
        "resin_mix",
        "cure",
        "coupon_metrology",
        "vna_measurement",
    ]
    return {
        "schema": "uqpu-cycle005-material-chain-of-custody-v1",
        "required_event_fields": [
            "event_id",
            "stage",
            "timestamp_utc",
            "actor",
            "input_lot_ids",
            "output_lot_ids",
            "procedure_revision",
            "artifact_sha256",
            "previous_event_sha256",
        ],
        "required_stages": stages,
        "events": [],
        "measurement_uncertainty": {
            "measurand": None,
            "estimate": None,
            "standard_uncertainty": None,
            "expanded_uncertainty": None,
            "coverage_factor": None,
            "components": [],
        },
        "calibration": {
            "certificate_sha256": None,
            "valid_from": None,
            "valid_until": None,
            "valid_at_measurement": None,
            "fixture_dynamic_range": None,
        },
        "matched_control": {
            "control_coupon_id": None,
            "same_protocol_revision": None,
            "same_instrument_session": None,
        },
        "ready": False,
        "remaining_dependency": "Populate a hash-linked custody chain, valid calibration, uncertainty budget, and matched control after authorization.",
        "evidence_class": "CHAIN_OF_CUSTODY_AND_UNCERTAINTY_SCHEMA_NO_PHYSICAL_SAMPLE",
    }


def build_capital_dependency_graph() -> dict:
    gates = [
        {
            "gate_id": "CAP-DMF-EMI-001",
            "prerequisite_ids": [f"DMF-PR-{index:02d}" for index in range(1, 10)],
            "capital_at_risk_thb": None,
            "status": "NOT_AUTHORIZED",
        },
        {
            "gate_id": "CAP-BOSONIC-001",
            "prerequisite_ids": [
                "BOS-DATA-LOCAL-CHECKSUM",
                "BOS-DATA-LICENSE",
                "BOS-DATA-FORMAT",
                "BOS-DATA-COLUMNS",
                "BOS-BASIS-UNCERTAINTY-MAP",
                "BOS-MATCHED-DEVICE-RESOURCES",
            ],
            "capital_at_risk_thb": None,
            "status": "NOT_AUTHORIZED",
        },
    ]
    return {
        "schema": "uqpu-cycle005-capital-dependency-graph-v1",
        "gates": gates,
        "all_prerequisites_machine_resolvable": True,
        "all_prerequisites_satisfied": False,
        "funding_or_purchase_authorized": False,
        "decision": None,
        "evidence_class": "CAPITAL_GATE_DEPENDENCY_SCHEMA_NO_FINANCIAL_DECISION",
    }


def zenodo_archive_inventory_gate() -> dict:
    return {
        "schema": "uqpu-cycle005-primary-archive-inventory-gate-v1",
        "record_url": ZENODO_RECORD_URL,
        "doi": "10.5281/zenodo.14257632",
        "published_date": "2024-12-03",
        "version": "v1",
        "resource_type": "Dataset",
        "access_date": "2026-09-28",
        "archive": {
            "name": "data_upload.zip",
            "displayed_size": "145.5 MB",
            "response_content_length_bytes": 145469232,
            "publisher_displayed_md5": "d4f051ba40bf3d1940f90f9da4e9953c",
            "downloaded": False,
            "locally_recomputed_md5": None,
            "local_sha256": None,
            "download_result": "BLOCKED_BY_RETRIEVAL_SIZE_LIMIT",
        },
        "preview_inventory": {
            "scope": "SERVER_PREVIEW_ONLY_NOT_A_COMPLETE_LOCAL_ARCHIVE_WALK",
            "top_level_entries": [
                {"path": "README.md", "displayed_size": "3.1 kB"},
                {"path": "d5_bit_flip", "displayed_size": "2.3 MB"},
                {"path": "d5_phase_flip", "displayed_size": None},
                {"path": "first_d3_bit_flip", "displayed_size": "1.0 MB"},
                {"path": "first_d3_phase_flip", "displayed_size": None},
                {"path": "second_d3_bit_flip", "displayed_size": "1.0 MB"},
                {"path": "second_d3_phase_flip", "displayed_size": None},
            ],
            "sampled_directory_families": {
                "d5_phase_flip_nbar": [1.0, 1.5, 2.0, 2.5, 3.0, 3.5],
                "first_d3_phase_flip_nbar": [1.0, 1.5, 2.0, 2.5, 3.0],
                "second_d3_phase_flip_nbar": [1.0, 1.5, 2.0, 2.5, 3.0],
            },
        },
        "provenance_gates": {
            "license": None,
            "license_observation": "NOT_DISPLAYED_ON_RECORD_PAGE",
            "readme_contents_read": False,
            "file_formats": None,
            "column_definitions": None,
            "bit_flip_mapping_validated": False,
            "phase_flip_mapping_validated": False,
            "uncertainty_columns_validated": False,
        },
        "service_contract_mapping": {
            "bit_flip_directory_family_identified": True,
            "phase_flip_directory_families_identified": True,
            "basis_resolved_values_extracted": False,
            "uncertainty_extracted": False,
            "project_reproduction": False,
        },
        "evidence_class": "PRIMARY_RECORD_AND_SERVER_PREVIEW_INVENTORY_NOT_RAW_DATA_ANALYSIS",
        "non_claims": [
            "The archive was not downloaded, parsed, or statistically reanalyzed.",
            "The publisher MD5 was not recomputed locally.",
            "Directory names alone do not establish units, columns, uncertainty, or a project result.",
            "No device reproduction or logical-memory performance claim is made.",
        ],
    }


def _access_log(actor: str, actions: list[dict]) -> list[dict]:
    previous = "0" * 64
    rows = []
    for ordinal, action in enumerate(actions, start=1):
        event = {
            "ordinal": ordinal,
            "actor": actor,
            "action": action["action"],
            "artifact_sha256": action.get("artifact_sha256"),
            "previous_event_sha256": previous,
        }
        event["event_sha256"] = _sha256(event)
        previous = event["event_sha256"]
        rows.append(event)
    return rows


def build_scm_rehearsal(
    public: dict,
    custodian: dict,
    *,
    public_file_sha256: str,
    custodian_file_sha256: str,
) -> dict:
    errors = validate_scm_handoff(public, custodian)
    if errors:
        raise ValueError(f"invalid Cycle 004 SCM handoff: {errors}")
    score_commitment = _sha256(public["frozen_scores"])
    scorer_log = _access_log(
        "synthetic_scorer_actor",
        [
            {"action": "RECEIVE_PUBLIC_PACKAGE", "artifact_sha256": public_file_sha256},
            {"action": "COMMIT_FROZEN_SCORES", "artifact_sha256": score_commitment},
            {"action": "REQUEST_REVEAL_AFTER_SCORE_COMMIT", "artifact_sha256": score_commitment},
        ],
    )
    custodian_log = _access_log(
        "synthetic_custodian_actor",
        [
            {"action": "VERIFY_SCORE_COMMITMENT", "artifact_sha256": score_commitment},
            {"action": "REVEAL_SYNTHETIC_TRUTH", "artifact_sha256": custodian_file_sha256},
        ],
    )
    return {
        "schema": "uqpu-cycle005-scm-two-actor-rehearsal-v1",
        "study_id": public["study_id"],
        "input_public_file_sha256": public_file_sha256,
        "input_custodian_file_sha256": custodian_file_sha256,
        "pre_registered_reveal_rule": {
            "rule": "custodian reveal only after scorer score-commit event is hash-linked and handoff validation passes",
            "score_commitment_sha256": score_commitment,
            "handoff_validation_errors": errors,
            "rule_satisfied_in_rehearsal": True,
        },
        "access_logs": {"scorer": scorer_log, "custodian": custodian_log},
        "separate_operating_system_principals": False,
        "independent_site": False,
        "human_or_physical_data": False,
        "operational_status": "SYNTHETIC_TWO_ACTOR_LOGIC_REHEARSAL_SAME_PROCESS_AND_REPOSITORY",
        "evidence_class": "SYNTHETIC_CHAINED_ACCESS_LOG_REHEARSAL_NOT_OPERATIONAL_BLINDING",
        "non_claims": [
            "Actor labels are logical roles, not independently authenticated people or systems.",
            "No human, biological, paranormal, cross-realm, or physical-sensor evidence exists.",
        ],
    }


def build_ai_candidate_gate(batch039: dict, source_sha256: str) -> dict:
    workload = batch039["workload"]
    acceptance = batch039["accepted_capability_contract"]
    return {
        "schema": "uqpu-cycle005-ai-candidate-result-gate-v1",
        "contract_id": "AI-COST-XOR-MLP-2-16-1-V1",
        "baseline_artifact_sha256": source_sha256,
        "required_inputs": {
            "dataset_generator": workload["name"],
            "dataset_or_generator_sha256": source_sha256,
            "seed": workload["seed"],
            "train_examples": workload["train_examples"],
            "held_out_examples": workload["held_out_examples"],
        },
        "quality_gate": {
            "held_out_accuracy_minimum": acceptance["held_out_accuracy_minimum"],
            "held_out_binary_cross_entropy_maximum": acceptance[
                "held_out_binary_cross_entropy_maximum"
            ],
        },
        "candidate_result": {
            "candidate_id": None,
            "dataset_or_generator_sha256": None,
            "seed": None,
            "train_examples": None,
            "held_out_examples": None,
            "held_out_accuracy": None,
            "held_out_binary_cross_entropy": None,
            "end_to_end_cost_usd": None,
            "end_to_end_energy_joules": None,
            "status": "NOT_RUN",
        },
        "publication_policy": {
            "failed_quality_gate_publishable": True,
            "slower_or_more_expensive_candidate_publishable": True,
            "missing_or_mismatched_inputs_rejected": True,
        },
        "validation": {
            "accepted": False,
            "errors": ["candidate_result_missing"],
        },
        "frontier_ai_baseline": False,
        "evidence_class": "MACHINE_CHECKABLE_TOY_AI_COMPARISON_SCHEMA_NO_CANDIDATE_RESULT",
    }


def validate_ai_candidate(gate: dict, result: dict) -> list[str]:
    required = gate["required_inputs"]
    quality = gate["quality_gate"]
    errors = []
    for field in ("dataset_or_generator_sha256", "seed", "train_examples", "held_out_examples"):
        if result.get(field) != required[field]:
            errors.append(f"{field}_mismatch")
    accuracy = result.get("held_out_accuracy")
    loss = result.get("held_out_binary_cross_entropy")
    if not isinstance(accuracy, (int, float)) or accuracy < quality["held_out_accuracy_minimum"]:
        errors.append("held_out_accuracy_gate_failed_or_missing")
    if not isinstance(loss, (int, float)) or loss > quality["held_out_binary_cross_entropy_maximum"]:
        errors.append("held_out_binary_cross_entropy_gate_failed_or_missing")
    for field in ("end_to_end_cost_usd", "end_to_end_energy_joules"):
        value = result.get(field)
        if value is not None and (not isinstance(value, (int, float)) or value < 0):
            errors.append(f"{field}_invalid")
    return errors


_QASM_PATTERNS = {
    "header": re.compile(r"OPENQASM 3\.0;"),
    "include": re.compile(r'include "stdgates\.inc";'),
    "qubit": re.compile(r"qubit\[(\d+)\] q;"),
    "bit": re.compile(r"bit\[(\d+)\] c;"),
    "h": re.compile(r"h q\[(\d+)\];"),
    "cx": re.compile(r"cx q\[(\d+)\], q\[(\d+)\];"),
    "rz": re.compile(r"rz\(([-+0-9.eE]+)\) q\[(\d+)\];"),
    "rx": re.compile(r"rx\(([-+0-9.eE]+)\) q\[(\d+)\];"),
    "measure": re.compile(r"c\[(\d+)\] = measure q\[(\d+)\];"),
}


def grammar_check_openqasm3(text: str) -> dict:
    """Check only the small frozen grammar subset used by the ER6 pair."""
    counts = {name: 0 for name in ("h", "cx", "rz", "rx", "measure")}
    widths = {"qubits": None, "classical_bits": None}
    measurement_map: dict[int, int] = {}
    unsupported = []
    seen_header = False
    seen_include = False
    for line_number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        match = _QASM_PATTERNS["header"].fullmatch(line)
        if match:
            seen_header = True
            continue
        match = _QASM_PATTERNS["include"].fullmatch(line)
        if match:
            seen_include = True
            continue
        match = _QASM_PATTERNS["qubit"].fullmatch(line)
        if match:
            widths["qubits"] = int(match.group(1))
            continue
        match = _QASM_PATTERNS["bit"].fullmatch(line)
        if match:
            widths["classical_bits"] = int(match.group(1))
            continue
        matched = False
        for name in ("h", "cx", "rz", "rx"):
            if _QASM_PATTERNS[name].fullmatch(line):
                counts[name] += 1
                matched = True
                break
        if matched:
            continue
        match = _QASM_PATTERNS["measure"].fullmatch(line)
        if match:
            classical, qubit = int(match.group(1)), int(match.group(2))
            measurement_map[classical] = qubit
            counts["measure"] += 1
            continue
        unsupported.append({"line": line_number, "text": line})
    errors = []
    if not seen_header:
        errors.append("missing_openqasm_3_header")
    if not seen_include:
        errors.append("missing_stdgates_include")
    if widths["qubits"] is None or widths["classical_bits"] is None:
        errors.append("missing_register_declaration")
    if unsupported:
        errors.append("unsupported_statement")
    return {
        "grammar_subset": "ER6_OPENQASM3_STDGATES_DECLARATIONS_H_CX_RZ_RX_MEASURE_V1",
        "passed": not errors,
        "counts": counts,
        "widths": widths,
        "measurement_map": measurement_map,
        "unsupported": unsupported,
        "errors": errors,
        "semantic_or_provider_validation": False,
    }


def build_qos_gate(
    manifest: dict, persisted_qiskit: dict, manifest_file_sha256: str
) -> dict:
    expected_input_sha = manifest_file_sha256
    errors = []
    if persisted_qiskit.get("input_sha256") != expected_input_sha:
        errors.append("persisted_qiskit_input_hash_mismatch")
    if persisted_qiskit.get("all_passed") is not True:
        errors.append("persisted_qiskit_all_passed_false")
    sdk_by_id = {row["candidate_id"]: row for row in persisted_qiskit.get("rows", [])}
    grammar_rows = []
    for candidate in manifest["lane_a_b_c_qos"]["paired_circuits"]:
        candidate_id = candidate["candidate_id"]
        grammar = grammar_check_openqasm3(candidate["openqasm_3"])
        grammar_rows.append({"candidate_id": candidate_id, **grammar})
        if not grammar["passed"]:
            errors.append(f"grammar_failed:{candidate_id}")
        expected_counts = {**candidate["logical_gate_counts"], "measure": 6}
        if grammar["counts"] != expected_counts:
            errors.append(f"grammar_count_mismatch:{candidate_id}")
        if grammar["widths"] != {"qubits": 6, "classical_bits": 6}:
            errors.append(f"grammar_width_mismatch:{candidate_id}")
        if grammar["measurement_map"] != {index: index for index in range(6)}:
            errors.append(f"grammar_measurement_map_mismatch:{candidate_id}")
        sdk = sdk_by_id.get(candidate_id)
        if sdk is None or sdk.get("qasm_sha256") != candidate["openqasm_3_sha256"]:
            errors.append(f"persisted_sdk_row_mismatch:{candidate_id}")
        elif (
            sdk.get("num_qubits") != 6
            or sdk.get("num_clbits") != 6
            or sdk.get("operation_counts") != expected_counts
            or {int(key): value for key, value in sdk.get("measurement_map", {}).items()}
            != {index: index for index in range(6)}
            or sdk.get("parse_passed") is not True
        ):
            errors.append(f"persisted_sdk_semantic_summary_mismatch:{candidate_id}")
    return {
        "schema": "uqpu-cycle005-qasm-dual-check-gate-v1",
        "input_manifest_sha256": expected_input_sha,
        "persisted_ci_parse": persisted_qiskit,
        "stdlib_grammar_rows": grammar_rows,
        "all_checks_passed": not errors,
        "errors": errors,
        "provider_transpile": {
            "provider": None,
            "backend": None,
            "calibration_timestamp": None,
            "layout": None,
            "physical_depth": None,
            "physical_two_qubit_gate_count": None,
            "artifact_sha256": None,
        },
        "hardware_executed": False,
        "evidence_class": "PERSISTED_PINNED_SDK_PARSE_PLUS_LIMITED_GRAMMAR_CHECK_NOT_PROVIDER_VALIDATION",
    }


def build_cycle005_packet(
    *,
    manifest: dict,
    batch039: dict,
    batch039_sha256: str,
    cycle004_cost_ledger: dict,
    public_scm: dict,
    custodian_scm: dict,
    public_scm_sha256: str,
    custodian_scm_sha256: str,
    persisted_qiskit: dict,
    manifest_file_sha256: str,
    scale_cases: list[dict],
    io_repetitions: int,
    code_commit: str,
) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("code_commit must be a full lowercase Git SHA-1")
    if [row["node_count"] for row in scale_cases] != [6, 10, 14]:
        raise ValueError("Cycle 005 requires ordered 6/10/14-node scale cases")
    dry_run = build_braket_dry_run_packet(manifest)
    cost_input = dict(cycle004_cost_ledger)
    cost_input.update(
        {
            "same_provider_execution_and_bill": False,
            "matched_classical_baseline": False,
        }
    )
    materials = build_material_evidence_registry()
    return {
        "schema": "uqpu-cycle005-delta01-integrated-gates-v1",
        "cycle": "005",
        "delta": "01",
        "status": "LOCAL_SOFTWARE_MEASUREMENT_SOURCE_INVENTORY_AND_FAIL_CLOSED_GATES_NO_EVIDENCE_PROMOTION",
        "generator_code_commit": code_commit,
        "lanes": {
            "A": {
                "scale_cases": scale_cases,
                "er6_regression_retained": True,
                "evidence_class": "LOCAL_DETERMINISTIC_CLASSICAL_SCALE_SCREEN",
            },
            "B": dry_run,
            "C": benchmark_durable_io(manifest, repetitions=io_repetitions),
            "D": {
                "primary_archive_inventory": zenodo_archive_inventory_gate(),
                "service_contract_mapping_advanced": True,
                "basis_resolved_values_extracted": False,
                "uncertainty_extracted": False,
                "project_reproduction": False,
            },
            "E": materials,
            "F": complete_cost_gate(cost_input),
            "G": build_chain_of_custody_schema(),
            "H": build_capital_dependency_graph(),
            "FND/EQN": zenodo_archive_inventory_gate(),
            "SCM": build_scm_rehearsal(
                public_scm,
                custodian_scm,
                public_file_sha256=public_scm_sha256,
                custodian_file_sha256=custodian_scm_sha256,
            ),
            "AI-COST": build_ai_candidate_gate(batch039, batch039_sha256),
            "QOS/QSVT": build_qos_gate(
                manifest, persisted_qiskit, manifest_file_sha256
            ),
        },
        "evidence_boundary": [
            "A/C are local software measurements on the recorded host; no power, cloud, provider, or hardware-neutral performance is inferred.",
            "B is an unsubmitted incomplete dry run with credentials, execution, observations, and billing all absent.",
            "D and FND/EQN inventory a primary record preview; the archive was not downloaded, parsed, or reanalyzed.",
            "E/G/H are empty evidence, custody, uncertainty, and capital gates; no material, fabrication, purchase, or decision exists.",
            "F refuses totals while lifecycle and same-provider prerequisites are missing.",
            "SCM is a same-process synthetic rehearsal with logical actor labels, not operational blinding or source evidence.",
            "AI-COST is a candidate schema tied to a toy baseline, not a measured candidate or frontier-AI economics.",
            "QOS/QSVT combines a persisted CI parse with a limited grammar check, not provider transpilation or QPU execution.",
        ],
    }
