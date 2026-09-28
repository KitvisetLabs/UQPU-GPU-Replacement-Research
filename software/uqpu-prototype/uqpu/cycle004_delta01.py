"""Cycle 004 Delta 01 reproducible baselines and evidence gates.

The module records local classical/software measurements, source-backed metadata,
and protocol contracts. It does not run a QPU, measure physical materials,
authorize spending, or promote a model or synthetic fixture into empirical
hardware, economic, biological, or SCM evidence.
"""
from __future__ import annotations

from decimal import Decimal
import hashlib
from itertools import product
import json
import math
import os
from pathlib import Path
import platform
import statistics
import tempfile
from time import perf_counter_ns
from typing import Any

from .cycle003_delta01 import (
    ER6_CONTRACT_ID,
    ER6_ISING_SHA256,
    canonical_json_bytes,
)
from .qaoa import qubo_to_ising
from .scalable_qubo import seeded_erdos_renyi_maxcut


AWS_BRAKET_PRICING_URL = "https://aws.amazon.com/braket/pricing/"
ZENODO_QEC_RECORD_URL = "https://zenodo.org/records/14257632"
ASTM_D4935_URL = "https://store.astm.org/standards/d4935"


def _sha256(value: Any) -> str:
    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _timing_summary(samples_ns: list[int]) -> dict[str, int | float]:
    if not samples_ns or any(type(value) is not int or value < 0 for value in samples_ns):
        raise ValueError("timing samples must be non-negative integer nanoseconds")
    return {
        "repetitions": len(samples_ns),
        "minimum_ns": min(samples_ns),
        "median_ns": statistics.median(samples_ns),
        "maximum_ns": max(samples_ns),
    }


def _er6_instance(frozen_contract: dict):
    fixture = frozen_contract["fixture"]
    generator = fixture["generator"]
    if fixture["case_id"] != "er6":
        raise ValueError("expected ER6 frozen contract")
    if frozen_contract["output_contract"]["contract_id"] != ER6_CONTRACT_ID:
        raise ValueError("unexpected output contract")
    instance = seeded_erdos_renyi_maxcut(
        generator["node_count"], generator["edge_probability"], generator["seed"]
    )
    if qubo_to_ising(instance).instance_sha256 != ER6_ISING_SHA256:
        raise ValueError("ER6 instance hash drift")
    return instance


def _solve_er6(frozen_contract: dict) -> dict:
    instance = _er6_instance(frozen_contract)
    variables = instance.variables
    best = math.inf
    accepted: list[str] = []
    states = 0
    for values in product((0, 1), repeat=len(variables)):
        bits = dict(zip(variables, values))
        energy = instance.energy(bits)
        states += 1
        bitstring = "".join(str(bits[index]) for index in reversed(variables))
        if energy < best:
            best = energy
            accepted = [bitstring]
        elif energy == best:
            accepted.append(bitstring)
    expected = [
        row["bits_v5_to_v0"]
        for row in frozen_contract["output_contract"]["accepted_outputs"]
    ]
    if best != frozen_contract["output_contract"]["accepted_objective"]:
        raise ValueError("exact objective drift")
    if sorted(accepted) != sorted(expected):
        raise ValueError("accepted-output drift")
    return {
        "method": "complete_binary_enumeration",
        "variables": len(variables),
        "states_evaluated": states,
        "best_objective": best,
        "accepted_bitstrings_v5_to_v0": sorted(accepted),
    }


def benchmark_er6_classical_baseline(
    frozen_contract: dict, repetitions: int = 101
) -> dict:
    """Measure the complete 64-state Python baseline on the current local host."""
    if type(repetitions) is not int or repetitions < 3:
        raise ValueError("repetitions must be an integer of at least 3")
    samples: list[int] = []
    reference = None
    for _ in range(repetitions):
        started = perf_counter_ns()
        current = _solve_er6(frozen_contract)
        samples.append(perf_counter_ns() - started)
        if reference is None:
            reference = current
        elif current != reference:
            raise ValueError("non-deterministic exact baseline output")
    return {
        "schema": "uqpu-er6-classical-baseline-measurement-v1",
        "contract_id": ER6_CONTRACT_ID,
        "instance_sha256": ER6_ISING_SHA256,
        "result": reference,
        "timing": _timing_summary(samples),
        "clock": "time.perf_counter_ns",
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
            "processor": platform.processor() or None,
            "logical_cpu_count": os.cpu_count(),
        },
        "evidence_class": "LOCAL_HOST_WALL_CLOCK_MEASUREMENT_EXACT_TOY_BASELINE",
        "limitations": [
            "ER6 is a toy with only 64 states and is not a competitive large-instance benchmark.",
            "Timing includes Python interpreter and function-call overhead.",
            "No energy, power, memory-residency or hardware-neutral performance was measured.",
            "This classical result does not establish quantum disadvantage or advantage.",
        ],
    }


def benchmark_manifest_io(manifest: dict, repetitions: int = 101) -> dict:
    """Measure local JSON serialization, cached file I/O and decoding."""
    if type(repetitions) is not int or repetitions < 3:
        raise ValueError("repetitions must be an integer of at least 3")
    expected = canonical_json_bytes(manifest)
    expected_hash = hashlib.sha256(expected).hexdigest()
    serialize_ns: list[int] = []
    write_ns: list[int] = []
    read_ns: list[int] = []
    decode_ns: list[int] = []
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle004-") as temporary:
        path = Path(temporary) / "manifest.json"
        for _ in range(repetitions):
            started = perf_counter_ns()
            payload = canonical_json_bytes(manifest)
            serialize_ns.append(perf_counter_ns() - started)
            if payload != expected:
                raise ValueError("serialization drift")

            started = perf_counter_ns()
            path.write_bytes(payload)
            write_ns.append(perf_counter_ns() - started)

            started = perf_counter_ns()
            recovered = path.read_bytes()
            read_ns.append(perf_counter_ns() - started)
            if hashlib.sha256(recovered).hexdigest() != expected_hash:
                raise ValueError("persistence hash mismatch")

            started = perf_counter_ns()
            decoded = json.loads(recovered)
            decode_ns.append(perf_counter_ns() - started)
            if decoded != manifest:
                raise ValueError("decode mismatch")
    return {
        "schema": "uqpu-cycle004-local-manifest-io-measurement-v1",
        "payload": {
            "canonical_json_utf8_bytes": len(expected),
            "canonical_json_sha256": expected_hash,
        },
        "timing": {
            "serialize": _timing_summary(serialize_ns),
            "file_write": _timing_summary(write_ns),
            "file_read": _timing_summary(read_ns),
            "json_decode": _timing_summary(decode_ns),
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "filesystem_path_kind": "temporary_local_path",
        },
        "evidence_class": "LOCAL_HOST_SOFTWARE_IO_MEASUREMENT_NOT_PROVIDER_IO",
        "limitations": [
            "File writes are not followed by fsync and do not prove durable media persistence.",
            "Operating-system caching is uncontrolled.",
            "No cloud transfer, QPU readout, provider serialization, network or energy is measured.",
        ],
    }


def provider_and_cost_gate() -> dict:
    task = Decimal("0.30")
    shot = Decimal("0.000425")
    tasks = 2
    shots_per_task = 8192
    narrow = task * tasks + shot * tasks * shots_per_task
    return {
        "pricing_source": AWS_BRAKET_PRICING_URL,
        "access_date": "2026-09-28",
        "provider": "AWS Braket",
        "qpu_family": "Rigetti Cepheus",
        "region_in_official_example": "US West (N. California)",
        "task_price_usd": str(task),
        "shot_price_usd": str(shot),
        "reservation_price_usd_per_hour": "4100.00",
        "tasks": tasks,
        "shots_per_task": shots_per_task,
        "task_plus_shot_tariff_usd": str(narrow),
        "separately_billed_services_noted_by_source": ["Amazon S3", "managed notebooks", "hybrid-job classical resources"],
        "quote_obtained": False,
        "provider_selected": None,
        "backend_selected": None,
        "credentials_used": False,
        "paid_job_submitted": False,
        "authorization_status": "NOT_AUTHORIZED",
        "complete_cost_ledger": {
            "provider_qpu_task_and_shot_tariff": str(narrow),
            "provider_actual_bill": None,
            "classical_host_orchestration": None,
            "queue": None,
            "network_transfer": None,
            "storage": None,
            "retry_failure": None,
            "mitigation_decoder": None,
            "energy_cooling": None,
            "labor": None,
            "capital_amortization": None,
            "observed_accepted_outputs": None,
            "total_cost_usd": None,
            "cost_per_accepted_output_usd": None,
        },
        "rg028_status": "OPEN_DATA_CREDENTIAL_AND_AUTHORIZATION_BLOCKED",
        "evidence_class": "OFFICIAL_TARIFF_SNAPSHOT_AND_COMPLETENESS_GATE_NOT_QUOTE_OR_BILL",
    }


def logical_memory_service_contract() -> dict:
    cycles = 100
    total_failure_target = 0.05
    source_error = 0.0165
    independent_limit = 1.0 - (1.0 - total_failure_target) ** (1.0 / cycles)
    union_bound_limit = total_failure_target / cycles
    source_independent_projection = 1.0 - (1.0 - source_error) ** cycles
    return {
        "schema": "uqpu-logical-memory-screening-contract-v1",
        "project_chosen_service_contract": {
            "logical_qubits": 1,
            "syndrome_cycles": cycles,
            "maximum_total_logical_failure_probability": total_failure_target,
            "basis_scope": "logical memory survival; basis-resolved acceptance must be reported",
            "decoder_and_erasure_policy_must_be_frozen": True,
            "classification": "PROJECT_SCREENING_REQUIREMENT_NOT_A_SOURCE_CLAIM",
        },
        "source_anchor": {
            "paper": "Putterman et al., Nature 638, 927-934 (2025)",
            "doi": "10.1038/s41586-025-08642-7",
            "reported_overall_logical_error_per_cycle_central": source_error,
            "reported_error_bar_percentage_points": 0.03,
            "reported_cycle_microseconds": 2.8,
        },
        "model_only_translation": {
            "required_per_cycle_error_if_stationary_independent": independent_limit,
            "sufficient_per_cycle_error_by_union_bound": union_bound_limit,
            "source_central_value_over_independent_limit_ratio": source_error / independent_limit,
            "source_central_value_independent_100_cycle_failure_projection": source_independent_projection,
            "union_bound_at_source_central_value": min(1.0, cycles * source_error),
        },
        "assumptions": [
            "The independent projection assumes identical stationary and independent per-cycle failures.",
            "The union bound does not assume independence but can be loose.",
            "The reported overall per-cycle error is used only at its central value.",
            "The project screening target is a chosen falsification gate, not a published threshold.",
        ],
        "conclusion": "SOURCE_CENTRAL_VALUE_DOES_NOT_MEET_PROJECT_SCREEN_UNDER_EITHER_SIMPLE_BOUND",
        "project_reproduction": False,
    }


def bosonic_data_record_gate() -> dict:
    return {
        "record_url": ZENODO_QEC_RECORD_URL,
        "doi": "10.5281/zenodo.14257632",
        "published_date": "2024-12-03",
        "version": "v1",
        "resource_type": "Dataset",
        "description_scope": "bit-flip and logical phase-flip rates of the logical memory",
        "file": {
            "name": "data_upload.zip",
            "displayed_size": "145.5 MB",
            "md5": "d4f051ba40bf3d1940f90f9da4e9953c",
        },
        "access_date": "2026-09-28",
        "raw_archive_downloaded": False,
        "raw_archive_inspected": False,
        "access_result": "RECORD_METADATA_RESOLVED_PREVIEW_RATE_LIMITED_ARCHIVE_NOT_INGESTED",
        "evidence_class": "PRIMARY_DATA_RECORD_METADATA_NOT_RAW_DATA_REANALYSIS",
        "non_claims": [
            "No source data point was re-fit or reproduced.",
            "The MD5 is publisher-displayed metadata, not a locally recomputed digest.",
            "No project logical-memory result or confidence interval is created by this record lookup.",
        ],
    }


def materials_and_fabrication_readiness_gate() -> dict:
    requirements = [
        ("current_full_method_text", False, "Only official catalog metadata is available."),
        ("authenticated_pangola_species_and_lot", False, "No chain-of-custody or lot record."),
        ("feedstock_moisture_and_ash", False, "No same-lot measurements."),
        ("resin_hardener_sku_and_ratio", False, "No exact resin system frozen."),
        ("cure_schedule", False, "No resin-specific cure schedule."),
        ("coupon_dimensions_and_uncertainty", False, "No verified fixture/metrology capability."),
        ("vna_fixture_calibration_and_dynamic_range", False, "No instrument or calibration booking."),
        ("same_protocol_incumbent_coupon", False, "No matched comparator fabrication or run."),
        ("safety_and_waste_review", False, "No authorized fabrication review."),
    ]
    rows = [
        {"requirement": name, "satisfied": satisfied, "evidence": evidence}
        for name, satisfied, evidence in requirements
    ]
    return {
        "study_id": "DMF-BIOCARBON-EMI-001",
        "standard_catalog": {
            "source_url": ASTM_D4935_URL,
            "access_date": "2026-09-28",
            "displayed_edition": "ASTM D4935-18(2026)",
            "catalog_designation": "D4935-18R26",
            "full_text_available_to_project": False,
            "compliance_claim_allowed": False,
        },
        "requirements": rows,
        "satisfied_count": sum(row["satisfied"] for row in rows),
        "required_count": len(rows),
        "readiness_status": "NOT_READY_NO_FABRICATION_AUTHORIZED",
        "capital_at_risk_thb": None,
        "evidence_class": "DOCUMENT_AND_METROLOGY_READINESS_GATE_NO_MATERIAL_MEASUREMENT",
    }


def ai_cost_equivalence_contract(batch039: dict, source_sha256: str) -> dict:
    workload = batch039["workload"]
    accepted = batch039["accepted_capability_contract"]
    if workload["name"] != "deterministic XOR-quadrant binary classification":
        raise ValueError("unexpected AI baseline workload")
    if accepted["held_out_accuracy_minimum"] != 0.98:
        raise ValueError("AI accuracy contract drift")
    if accepted["held_out_binary_cross_entropy_maximum"] != 0.19:
        raise ValueError("AI loss contract drift")
    return {
        "contract_id": "AI-COST-XOR-MLP-2-16-1-V1",
        "source_artifact": "benchmarks/results/batch039-ai-cost-002-classical-baseline.json",
        "source_artifact_sha256": source_sha256,
        "functionally_equivalent_task": {
            "dataset_generation": "same deterministic train/test generator and seeds",
            "train_examples": workload["train_examples"],
            "held_out_examples": workload["held_out_examples"],
            "target_label": "1 iff x1*x2 >= 0 else 0",
            "held_out_accuracy_minimum": accepted["held_out_accuracy_minimum"],
            "held_out_binary_cross_entropy_maximum": accepted["held_out_binary_cross_entropy_maximum"],
            "failed_or_slower_candidate_is_publishable": True,
        },
        "baseline_provenance": {
            "model": workload["model"],
            "epochs": workload["epochs"],
            "seed": workload["seed"],
            "reference_held_out_accuracy": accepted["reference_held_out_accuracy"],
            "reference_held_out_binary_cross_entropy": accepted["reference_held_out_binary_cross_entropy"],
            "operation_ledger": batch039["exact_source_level_training_operation_ledger"],
            "tensor_payload_ledger": batch039["logical_tensor_payload_ledger"],
        },
        "frontier_ai_baseline": False,
        "quantum_or_uqpu_candidate_measured_cost": None,
        "end_to_end_residual_cost_fraction": None,
        "status": "FUNCTIONAL_EQUIVALENCE_CONTRACT_FROZEN_COST_COMPARISON_BLOCKED",
        "evidence_class": "REPOSITORY_CLASSICAL_TOY_AI_BASELINE_CONTRACT_NOT_FRONTIER_AI_ECONOMICS",
    }


def build_scm_two_party_handoff(cycle003_fixture: dict, salt: str) -> tuple[dict, dict]:
    if not salt or len(salt) < 16:
        raise ValueError("synthetic custodian salt must be at least 16 characters")
    observations = cycle003_fixture["blinded_observations"]
    truth = cycle003_fixture["sealed_truth"]
    scores = cycle003_fixture["frozen_blinded_scores"]
    if len(observations) != len(truth) or len(scores) != len(truth):
        raise ValueError("SCM fixture row-count mismatch")
    for row in observations:
        if "condition" in row or "condition" in row.get("payload", {}):
            raise ValueError("condition leaked into public observation")
    truth_payload = {"salt": salt, "truth": truth}
    truth_commitment = _sha256(truth_payload)
    public = {
        "schema": "uqpu-scm-cal001-two-party-public-handoff-v1",
        "cycle": "004",
        "study_id": cycle003_fixture["study_id"],
        "protocol_id": cycle003_fixture["protocol_id"],
        "observations": observations,
        "frozen_scores": scores,
        "scoring_rule": {
            "threshold_sigma": cycle003_fixture["threshold_sigma"],
            "coincidence_channels": cycle003_fixture["coincidence_channels"],
            "rule": "per-channel abs(z)>=4; event at >=2 of 6 channels",
        },
        "truth_commitment_sha256": truth_commitment,
        "condition_labels_present": False,
        "handoff_role": "SCORER_PACKAGE",
        "evidence_class": "SYNTHETIC_TWO_PARTY_HANDOFF_DEMONSTRATION",
        "non_claims": [
            "No human or physical-sensor data.",
            "No paranormal or cross-realm source claim.",
            "A hash commitment provides integrity, not semantic evidence.",
        ],
    }
    custodian = {
        "schema": "uqpu-scm-cal001-custodian-truth-v1",
        "cycle": "004",
        **truth_payload,
        "truth_commitment_sha256": truth_commitment,
        "public_package_sha256": _sha256(public),
        "handoff_role": "CUSTODIAN_PACKAGE",
        "operational_status": "DEMONSTRATION_ONLY_BOTH_PACKAGES_COMMITTED_IN_SAME_REPOSITORY",
        "independent_site_status": "NOT_EXECUTED_NO_SECOND_SITE",
        "evidence_class": "SYNTHETIC_TRUTH_CUSTODY_SCHEMA_NOT_OPERATIONAL_BLINDING",
    }
    return public, custodian


def validate_scm_handoff(public: dict, custodian: dict) -> list[str]:
    errors: list[str] = []
    if public.get("condition_labels_present") is not False:
        errors.append("public package must declare no condition labels")
    if any(
        "condition" in row or "condition" in row.get("payload", {})
        for row in public.get("observations", [])
    ):
        errors.append("condition label leaked into observations")
    expected = _sha256({"salt": custodian.get("salt"), "truth": custodian.get("truth")})
    if public.get("truth_commitment_sha256") != expected:
        errors.append("truth commitment mismatch")
    if custodian.get("truth_commitment_sha256") != expected:
        errors.append("custodian commitment mismatch")
    if custodian.get("public_package_sha256") != _sha256(public):
        errors.append("public package hash mismatch")
    return errors


def build_cycle004_packet(
    frozen_contract: dict,
    cycle003_manifest: dict,
    batch039: dict,
    batch039_raw_sha256: str,
    *,
    repetitions: int = 101,
    code_commit: str,
) -> dict:
    if len(code_commit) != 40 or any(ch not in "0123456789abcdef" for ch in code_commit):
        raise ValueError("code_commit must be a full lowercase Git SHA-1")
    if cycle003_manifest["lane_a_b_c_qos"]["source_contract"]["output_contract_id"] != ER6_CONTRACT_ID:
        raise ValueError("Cycle 003 manifest contract drift")
    return {
        "schema": "uqpu-cycle004-delta01-integrated-baseline-and-gates-v1",
        "cycle": "004",
        "delta": "01",
        "status": "LOCAL_SOFTWARE_MEASUREMENT_AND_PROTOCOL_GATES_NO_NEW_HARDWARE_EVIDENCE",
        "generator_code_commit": code_commit,
        "lanes": {
            "A": benchmark_er6_classical_baseline(frozen_contract, repetitions),
            "B": provider_and_cost_gate(),
            "C": benchmark_manifest_io(cycle003_manifest, repetitions),
            "D": logical_memory_service_contract(),
            "E": materials_and_fabrication_readiness_gate(),
            "F": provider_and_cost_gate()["complete_cost_ledger"],
            "G": materials_and_fabrication_readiness_gate(),
            "H": {
                "capital_gates": [
                    {"gate_id": "CAP-DMF-EMI-001", "status": "NOT_AUTHORIZED", "capital_at_risk_thb": None},
                    {"gate_id": "CAP-BOSONIC-001", "status": "NOT_AUTHORIZED", "capital_at_risk_thb": None},
                ],
                "funding_or_purchase_authorized": False,
            },
            "FND/EQN": bosonic_data_record_gate(),
            "AI-COST": ai_cost_equivalence_contract(batch039, batch039_raw_sha256),
            "QOS/QSVT": {
                "input_manifest": "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json",
                "candidate_count": len(cycle003_manifest["lane_a_b_c_qos"]["paired_circuits"]),
                "independent_sdk": "qiskit==2.5.2",
                "required_checks": ["QASM 3 parse", "register widths", "operation counts", "terminal measurement map"],
                "provider_transpilation": None,
                "hardware_executed": False,
                "status": "PINNED_INDEPENDENT_SDK_PARSE_GATE_ATTACHED_TO_CI",
            },
        },
        "evidence_boundary": [
            "A/C timings are local software measurements on the recorded host only.",
            "Provider values are tariffs, not a quote, bill or provider-matched result.",
            "Logical-memory calculations are screening models, not measured retention.",
            "Materials entries are readiness gates; no coupon was fabricated or measured.",
            "SCM is emitted as separate synthetic demonstration packages and carries no source claim.",
            "AI-COST freezes a toy XOR equivalence contract, not frontier-AI economics.",
            "Independent SDK parsing is not provider acceptance, physical compilation or QPU execution.",
        ],
    }
