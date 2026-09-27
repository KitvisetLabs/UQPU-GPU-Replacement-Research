"""Cycle 003 Delta 01 provider-neutral resources and source-backed gates.

All outputs are protocol/model/literature artifacts. This module does not run a
QPU, make a physical measurement, authorize spending, or promote an evidence
state.
"""
from __future__ import annotations

from collections import Counter
from decimal import Decimal
import hashlib
import json
import math
import random
import re
from typing import Any

from .qaoa import qaoa_program, qubo_to_ising
from .scalable_qubo import seeded_erdos_renyi_maxcut
from .scm_null_characterization import DEFAULT_CHANNELS
from .scm_trial_ledger import CalibrationRecord, TrialRecord, sha256_bytes, validate_trial
from .scm_replication_contract import (
    REQUIRED_ENVIRONMENT_FIELDS,
    ReplicationManifest,
    validate_manifest,
)


ER6_ISING_SHA256 = "bc3fb615b6fd2530694b097fde804e62f165fd7d0953bf66aff4602cd77fa201"
ER6_CONTRACT_ID = "8efaa94bb3306d25"
AWS_BRAKET_RIGETTI_TASK_USD = Decimal("0.30")
AWS_BRAKET_RIGETTI_SHOT_USD = Decimal("0.000425")
NATURE_QEC_DOI = "10.1038/s41586-025-08642-7"
ZENODO_QEC_DOI = "10.5281/zenodo.14257632"
ASTM_D4935_URL = "https://store.astm.org/standards/d4935"


def canonical_json_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")


def _qasm3(program: Any) -> str:
    lines = [
        "OPENQASM 3.0;",
        'include "stdgates.inc";',
        f"qubit[{program.qubits}] q;",
        f"bit[{program.qubits}] c;",
    ]
    for inst in program.instructions:
        if inst.op in {"h", "rx", "rz"}:
            if len(inst.targets) != 1:
                raise ValueError(f"invalid target count for {inst.op}")
            args = ""
            if inst.params:
                if len(inst.params) != 1 or not math.isfinite(inst.params[0]):
                    raise ValueError(f"invalid rotation parameter for {inst.op}")
                args = f"({inst.params[0]:.17g})"
            lines.append(f"{inst.op}{args} q[{inst.targets[0]}];")
        elif inst.op == "cx":
            if len(inst.controls) != 1 or len(inst.targets) != 1:
                raise ValueError("CX requires one control and one target")
            lines.append(f"cx q[{inst.controls[0]}], q[{inst.targets[0]}];")
        elif inst.op == "measure_all":
            lines.extend(f"c[{q}] = measure q[{q}];" for q in range(program.qubits))
        else:
            raise ValueError(f"unsupported portable instruction: {inst.op}")
    return "\n".join(lines) + "\n"


def build_er6_circuit_manifest(frozen_contract: dict, provider_protocol: dict) -> dict:
    """Lower the frozen p=1 pair to provider-neutral QASM 3 and a logical ledger."""
    fixture = frozen_contract["fixture"]
    generator = fixture["generator"]
    if fixture["case_id"] != "er6":
        raise ValueError("expected frozen ER6 fixture")
    if frozen_contract["output_contract"]["contract_id"] != ER6_CONTRACT_ID:
        raise ValueError("unexpected useful-output contract")
    if provider_protocol["workload"]["contract_id"] != ER6_CONTRACT_ID:
        raise ValueError("provider protocol contract mismatch")
    if provider_protocol.get("real_qpu_executed") or provider_protocol.get("paid_job_submitted"):
        raise ValueError("Cycle 003 packet must not claim or submit a paid execution")

    instance = seeded_erdos_renyi_maxcut(
        generator["node_count"], generator["edge_probability"], generator["seed"]
    )
    ising = qubo_to_ising(instance)
    if ising.instance_sha256 != fixture["qubo_to_ising_sha256"] or ising.instance_sha256 != ER6_ISING_SHA256:
        raise ValueError("frozen ER6 content hash mismatch")
    edges = [
        [u, v]
        for (u, v), weight in sorted(instance.quadratic.items())
        if weight == 2.0
    ]
    if edges != fixture["edges"]:
        raise ValueError("frozen ER6 edge list mismatch")

    shots = provider_protocol["execution_plan"]["initial_shots_per_candidate"]
    if shots <= 0:
        raise ValueError("shots must be positive")
    protocol_candidates = {row["id"]: row for row in provider_protocol["frozen_candidates"]}
    circuits = []
    for frozen in frozen_contract["frozen_p1_candidates"]:
        candidate_id = frozen["id"]
        protocol = protocol_candidates.get(candidate_id)
        if protocol is None or protocol["gamma"] != frozen["gamma"] or protocol["beta"] != frozen["beta"]:
            raise ValueError(f"candidate drift for {candidate_id}")
        program = qaoa_program(
            instance,
            [frozen["gamma"]],
            [frozen["beta"]],
            shots=shots,
            contract_id=ER6_CONTRACT_ID,
        )
        counts = Counter(inst.op for inst in program.instructions)
        qasm = _qasm3(program)
        circuits.append({
            "candidate_id": candidate_id,
            "selection_objective": frozen["selection_objective"],
            "gamma": frozen["gamma"],
            "beta": frozen["beta"],
            "shots": shots,
            "qubits": program.qubits,
            "logical_gate_counts": {name: counts[name] for name in ("h", "cx", "rz", "rx")},
            "logical_gate_instruction_count": sum(counts[name] for name in ("h", "cx", "rz", "rx")),
            "measure_all_instructions": counts["measure_all"],
            "measured_bits_per_shot": program.qubits,
            "portable_ir_contract_id": program.metadata["contract_id"],
            "portable_ir_instance_sha256": program.metadata["instance_sha256"],
            "openqasm_3": qasm,
            "openqasm_3_sha256": hashlib.sha256(qasm.encode("utf-8")).hexdigest(),
            "openqasm_3_utf8_bytes": len(qasm.encode("utf-8")),
            "provider_transpilation": None,
            "physical_layout": None,
            "physical_depth": None,
            "physical_two_qubit_gate_count": None,
            "evidence_class": "PROVIDER_NEUTRAL_LOGICAL_CIRCUIT_MODEL_NOT_EXECUTION",
        })

    if len(circuits) != 2 or len({c["shots"] for c in circuits}) != 1:
        raise ValueError("paired equal-shot contract was not preserved")
    accepted = frozen_contract["output_contract"]["accepted_outputs"]
    return {
        "schema": "uqpu-cycle003-er6-provider-neutral-circuit-ledger-v1",
        "cycle": "003",
        "delta": "01",
        "status": "PROVIDER_NEUTRAL_CIRCUIT_AND_RESOURCE_PACKET_NO_HARDWARE_EVIDENCE",
        "source_contract": {
            "instance_case_id": "er6",
            "instance_sha256": ising.instance_sha256,
            "output_contract_id": ER6_CONTRACT_ID,
            "accepted_objective": frozen_contract["output_contract"]["accepted_objective"],
            "accepted_output_count": len(accepted),
            "accepted_bitstrings_v5_to_v0": [row["bits_v5_to_v0"] for row in accepted],
            "bit_order": "qubit_0_is_integer_lsb; displayed strings are v5..v0",
        },
        "paired_circuits": circuits,
        "readout_payload_bounds": {
            "shots_per_candidate": shots,
            "candidate_count": len(circuits),
            "measured_bits_per_shot": 6,
            "raw_measurement_bits_per_candidate": shots * 6,
            "packed_raw_measurement_bytes_per_candidate": (shots * 6 + 7) // 8,
            "packed_raw_measurement_bytes_for_pair": (shots * 6 * len(circuits) + 7) // 8,
            "minimum_bits_to_label_one_of_four_accepted_outputs": math.ceil(math.log2(len(accepted))),
            "provider_result_serialization_bytes": None,
            "transfer_time_seconds": None,
            "persistence_time_seconds": None,
            "readout_time_seconds": None,
            "decode_time_seconds": None,
            "scope": "Exact logical payload arithmetic; no host/provider I/O time or compression assumption.",
        },
        "provider_execution": {
            "provider_selected": None,
            "backend_selected": None,
            "transpilation_performed": False,
            "calibration_snapshot": None,
            "real_qpu_executed": False,
            "paid_job_submitted": False,
            "authorization_required": True,
        },
        "non_claims": [
            "no real-QPU result",
            "no provider transpilation or physical gate count",
            "no measured end-to-end latency, energy, memory or I/O",
            "no cost per accepted output",
            "no quantum advantage or subsystem-replacement claim",
        ],
    }


def braket_rigetti_tariff_sensitivity(
    task_count: int,
    shots_per_task: int,
    task_usd: Decimal = AWS_BRAKET_RIGETTI_TASK_USD,
    shot_usd: Decimal = AWS_BRAKET_RIGETTI_SHOT_USD,
) -> dict:
    if type(task_count) is not int or task_count <= 0:
        raise ValueError("task_count must be a positive integer")
    if type(shots_per_task) is not int or shots_per_task <= 0:
        raise ValueError("shots_per_task must be a positive integer")
    if task_usd < 0 or shot_usd < 0:
        raise ValueError("tariffs cannot be negative")
    task_component = Decimal(task_count) * task_usd
    shot_component = Decimal(task_count * shots_per_task) * shot_usd
    total = task_component + shot_component
    return {
        "provider": "AWS Braket",
        "qpu_family": "Rigetti Cepheus",
        "pricing_source": "https://aws.amazon.com/braket/pricing/",
        "access_date": "2026-09-28",
        "task_count": task_count,
        "shots_per_task": shots_per_task,
        "total_shots": task_count * shots_per_task,
        "task_price_usd": format(task_usd.normalize(), "f"),
        "shot_price_usd": format(shot_usd.normalize(), "f"),
        "task_component_usd": format(task_component.normalize(), "f"),
        "shot_component_usd": format(shot_component.normalize(), "f"),
        "qpu_task_plus_shot_tariff_usd": format(total.normalize(), "f"),
        "full_aws_bill_usd": None,
        "host_queue_transfer_storage_retry_mitigation_energy_usd": None,
        "cost_per_accepted_output_usd": None,
        "evidence_class": "OFFICIAL_TARIFF_ARITHMETIC_SENSITIVITY_NOT_QUOTE_OR_BILL",
    }


def end_to_end_cost_result(components_usd: dict[str, Decimal | None], accepted_outputs: int | None) -> dict:
    required = (
        "provider_qpu", "host_orchestration", "queue", "transfer_storage",
        "mitigation_decoder", "retry_failure", "energy_cooling", "capital_amortization",
    )
    missing = [name for name in required if components_usd.get(name) is None]
    if accepted_outputs is None or accepted_outputs <= 0:
        missing.append("accepted_output_count")
    if missing:
        return {
            "total_cost_usd": None,
            "accepted_output_count": accepted_outputs,
            "cost_per_accepted_output_usd": None,
            "missing_components": missing,
            "status": "BLOCKED_WITH_NULLS_PRESERVED",
        }
    values = [components_usd[name] for name in required]
    if any(value < 0 for value in values):
        raise ValueError("cost components cannot be negative")
    total = sum(values, Decimal("0"))
    per_output = total / Decimal(accepted_outputs)
    return {
        "total_cost_usd": format(total.normalize(), "f"),
        "accepted_output_count": accepted_outputs,
        "cost_per_accepted_output_usd": format(per_output.normalize(), "f"),
        "missing_components": [],
        "status": "COMPLETE_ARITHMETIC_INPUTS",
    }


def bosonic_qec_source_analysis() -> dict:
    overall = Decimal("0.0165")
    cycle_us = Decimal("2.8")
    phase_upper = 2 * overall
    tx_lower = cycle_us / (2 * phase_upper)
    return {
        "source": "Putterman et al., Nature 638, 927-934 (2025)",
        "doi": NATURE_QEC_DOI,
        "data_doi": ZENODO_QEC_DOI,
        "alpha_squared": 1.5,
        "distance": 5,
        "storage_cat_modes": 5,
        "syndrome_ancilla_transmons": 4,
        "reported_qec_cycle_us": float(cycle_us),
        "reported_overall_logical_error_per_cycle": float(overall),
        "reported_uncertainty_percentage_points": 0.03,
        "uncertainty_interpretation": "Paper-reported error bar; no confidence level is inferred.",
        "reported_overall_error_definition": "epsilon_L = (epsilon_L_phase_flip + epsilon_L_bit_flip) / 2",
        "source_equation_for_phase_error": "epsilon_L_phase_flip = T_cycle / (2 T_X)",
        "derived_phase_error_upper_bound_from_central_value": float(phase_upper),
        "derived_T_X_lower_bound_us_from_central_value": float(tx_lower),
        "derivation_assumptions": [
            "use the paper's stated central overall error value only",
            "logical bit-flip error probability is nonnegative",
            "apply the paper's definitions without a confidence-bound interpretation",
        ],
        "project_logical_error_target": None,
        "project_retention_horizon_cycles": None,
        "target_gate": "Freeze a useful logical-memory service contract and acceptance horizon before selecting a project target.",
        "zenodo_raw_files_fetched": False,
        "zenodo_access_note": "Primary paper data DOI recorded; record/API fetch was rate-limited during this run, so raw-file fields were not re-extracted.",
        "evidence_class": "PRIMARY_PUBLISHED_EXPERIMENT_PLUS_CENTRAL_VALUE_ARITHMETIC_INFERENCE_NOT_PROJECT_REPRODUCTION",
        "source_url": "https://www.nature.com/articles/s41586-025-08642-7",
    }


def materials_readiness_gate() -> dict:
    return {
        "study_id": "DMF-BIOCARBON-EMI-001",
        "official_standard_title": "Standard Test Method for Measuring the Electromagnetic Shielding Effectiveness of Planar Materials",
        "current_displayed_edition": "ASTM D4935-18(2026)",
        "catalog_designation": "D4935-18R26",
        "official_scope_summary": "Normal-incidence, far-field, plane-wave measurement of shielding effectiveness for planar materials.",
        "official_page_price_usd": "80.00",
        "access_date": "2026-09-28",
        "full_standard_text_available_to_project": False,
        "purchase_authorized": False,
        "compliance_claim_allowed": False,
        "measurement_uncertainty_factors": [
            "material",
            "mismatches through the transmission-line path",
            "measurement-system dynamic range",
            "accuracy of ancillary equipment",
            "procedure deviations",
        ],
        "candidate_process": "unchanged proposal only; no feedstock authentication, resin/hardener/cure freeze, fabrication or VNA measurement",
        "next_gate": "Obtain authorized access to the current full method text, authenticate feedstock, freeze exact resin/cure, and resolve instrument uncertainty before fabrication.",
        "source_url": ASTM_D4935_URL,
        "evidence_class": "OFFICIAL_STANDARD_CATALOG_METADATA_AND_NO_FABRICATION_READINESS_GATE",
    }


def ai_cost_ceiling() -> dict:
    target_thb = Decimal("50000")
    fx = Decimal("33.045")
    target_usd = target_thb / fx
    base_10t = Decimal("10000000000000")
    base_100t = Decimal("100000000000000")
    return {
        "owner_defined_budget_thb": int(target_thb),
        "planning_fx_thb_per_usd": str(fx),
        "target_usd_before_other_costs": format(target_usd.quantize(Decimal("0.000000001")), "f"),
        "baseline_proxy_usd": {"10T": str(base_10t), "100T": str(base_100t)},
        "maximum_residual_share_if_every_fixed_cost_were_zero": {
            "10T": format((target_usd / base_10t), ".12E"),
            "100T": format((target_usd / base_100t), ".12E"),
        },
        "functional_equivalence_workload": None,
        "competitive_baseline_provenance": None,
        "adjusted_residual_share_after_fixed_costs": None,
        "status": "BOUND_ONLY_AI_WORKLOAD_AND_COSTS_UNVERIFIED",
        "evidence_class": "OWNER_PROXY_ARITHMETIC_NOT_AI_BENCHMARK_OR_ECONOMIC_RESULT",
    }


def build_cycle003_manifest(frozen_contract: dict, provider_protocol: dict) -> dict:
    circuit = build_er6_circuit_manifest(frozen_contract, provider_protocol)
    shots = provider_protocol["execution_plan"]["initial_shots_per_candidate"]
    task_count = len(circuit["paired_circuits"])
    cost = braket_rigetti_tariff_sensitivity(task_count, shots)
    return {
        "schema": "uqpu-cycle003-delta01-integrated-resource-gates-v1",
        "cycle": "003",
        "delta": "01",
        "status": "SOURCE_BACKED_PROTOCOL_AND_MODEL_NO_NEW_EMPIRICAL_CLAIM",
        "priority": "Lane A P0 useful-output contract; integrate B/C/F/QOS without provider mixing",
        "lane_a_b_c_qos": circuit,
        "lane_b_tariff_sensitivity": cost,
        "lane_f_full_stack_cost_gate": end_to_end_cost_result(
            {
                "provider_qpu": None,
                "host_orchestration": None,
                "queue": None,
                "transfer_storage": None,
                "mitigation_decoder": None,
                "retry_failure": None,
                "energy_cooling": None,
                "capital_amortization": None,
            },
            accepted_outputs=None,
        ),
        "lane_d_fnd_eqn": bosonic_qec_source_analysis(),
        "lane_e_g": materials_readiness_gate(),
        "lane_h_capital_gates": [
            {"gate_id": "CAP-DMF-EMI-001", "capital_at_risk_thb": None, "authorization_status": "NOT_AUTHORIZED"},
            {"gate_id": "CAP-BOSONIC-001", "capital_at_risk_thb": None, "authorization_status": "NOT_AUTHORIZED"},
        ],
        "lane_ai_cost": ai_cost_ceiling(),
        "evidence_boundary": [
            "QASM is provider-neutral logical lowering, not validated provider transpilation.",
            "Tariff arithmetic excludes service and project costs and is not a quote or bill.",
            "Bosonic values are a published result plus explicitly labeled central-value inference.",
            "Materials standard metadata do not establish method compliance or coupon performance.",
            "No functionally equivalent AI-training result is present.",
        ],
    }


def build_synthetic_cal001_fixture(
    samples_per_condition: int = 128,
    seed: int = 20260928,
    *,
    code_commit: str | None = None,
) -> dict:
    """Create a deterministic synthetic CAL-001 packet with separated truth."""
    if type(samples_per_condition) is not int or samples_per_condition <= 0:
        raise ValueError("samples_per_condition must be a positive integer")
    if code_commit is not None and not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("code_commit must be a full lowercase Git SHA-1")

    channels = tuple(DEFAULT_CHANNELS)
    threshold_sigma = 4.0
    coincidence_channels = 2
    conditions = ["control"] * samples_per_condition + ["known-interference"] * samples_per_condition
    random.Random(seed).shuffle(conditions)
    noise_rng = random.Random(seed ^ 0x5F3759DF)
    calibration_objects = tuple(
        CalibrationRecord(
            calibration_id=f"cal-synthetic-{channel.name}",
            sensor_id=f"synthetic-{channel.name}",
            method="normalized Gaussian fixture; not a physical sensor calibration",
            reference_value="noise_sigma=1 normalized unit",
            utc_timestamp="SYNTHETIC_NOT_AN_ACTUAL_CALIBRATION",
            operator_role="fixture-generator",
        )
        for channel in channels
    )
    calibration_ids = tuple(item.calibration_id for item in calibration_objects)
    calibrations = [
        {
            "calibration_id": item.calibration_id,
            "sensor_id": item.sensor_id,
            "method": item.method,
            "reference_value": item.reference_value,
            "utc_timestamp": item.utc_timestamp,
            "operator_role": item.operator_role,
            "evidence_class": "SYNTHETIC_FIXTURE_NOT_METROLOGY",
        }
        for item in calibration_objects
    ]

    observations = []
    truth = []
    ledger = []
    frozen_scores = []
    for index, condition in enumerate(conditions):
        trial_id = f"CAL001-SYN-{index + 1:04d}"
        injected = condition == "known-interference"
        channels_z = {}
        for channel in channels:
            noise = noise_rng.gauss(0.0, channel.noise_sigma)
            injection = 10.0 * channel.interference_gain if injected else 0.0
            channels_z[channel.name] = round((noise + injection) / channel.noise_sigma, 8)
        raw_payload = {"trial_id": trial_id, "channels_z": channels_z}
        raw_hash = sha256_bytes(canonical_json_bytes(raw_payload))
        observations.append({"payload": raw_payload, "raw_sha256": raw_hash})
        truth.append({"trial_id": trial_id, "condition": condition})
        record = TrialRecord(
            trial_id=trial_id,
            condition=condition,
            raw_sha256=raw_hash,
            calibration_ids=calibration_ids,
            excluded=False,
            evidence_class="SYNTHETIC_FIXTURE",
        )
        validation_errors = validate_trial(record, calibration_objects)
        if validation_errors:
            raise ValueError(f"invalid synthetic trial: {validation_errors}")
        ledger.append({
            "trial_id": record.trial_id,
            "condition": record.condition,
            "raw_sha256": record.raw_sha256,
            "calibration_ids": list(record.calibration_ids),
            "excluded": record.excluded,
            "exclusion_reason": record.exclusion_reason,
            "evidence_class": record.evidence_class,
        })
        hits = sum(abs(value) >= threshold_sigma for value in channels_z.values())
        frozen_scores.append({"trial_id": trial_id, "coincidence_event": hits >= coincidence_channels})

    condition_by_id = {row["trial_id"]: row["condition"] for row in truth}
    tp = fp = tn = fn = 0
    for score in frozen_scores:
        condition = condition_by_id[score["trial_id"]]
        if condition == "known-interference":
            tp += int(score["coincidence_event"])
            fn += int(not score["coincidence_event"])
        else:
            fp += int(score["coincidence_event"])
            tn += int(not score["coincidence_event"])

    bundle = {
        "blinded_observations": observations,
        "sealed_truth": truth,
        "trial_ledger": ledger,
    }
    bundle_bytes = canonical_json_bytes(bundle)
    bundle_sha = sha256_bytes(bundle_bytes)
    replication_manifest = None
    manifest_errors = None
    replication_status = "WAITING_FOR_PUBLISHED_CODE_COMMIT"
    if code_commit is not None:
        manifest = ReplicationManifest(
            protocol_id="SCM-P2-CAL-001",
            protocol_version="1.0-synthetic",
            code_commit=code_commit,
            data_sha256=bundle_sha,
            schema_version="scm-cal001-synthetic-v1",
            randomization_method="seeded Python random.Random shuffle; synthetic reproducibility only; not cryptographic blinding",
            scoring_rule="per-channel abs(z)>=4; coincidence at >=2 of 6 channels",
            exclusion_rules=("raw-hash or calibration-integrity failure only",),
            environment_fields=REQUIRED_ENVIRONMENT_FIELDS,
            evidence_class="REPLICATION_INFRASTRUCTURE_ONLY_SYNTHETIC",
        )
        manifest_errors = list(validate_manifest(manifest))
        if manifest_errors:
            raise ValueError(f"invalid synthetic replication manifest: {manifest_errors}")
        replication_manifest = {
            "protocol_id": manifest.protocol_id,
            "protocol_version": manifest.protocol_version,
            "code_commit": manifest.code_commit,
            "data_sha256": manifest.data_sha256,
            "schema_version": manifest.schema_version,
            "randomization_method": manifest.randomization_method,
            "scoring_rule": manifest.scoring_rule,
            "exclusion_rules": list(manifest.exclusion_rules),
            "environment_fields": list(manifest.environment_fields),
            "evidence_class": manifest.evidence_class,
            "validation_errors": manifest_errors,
        }
        replication_status = "MANIFEST_VALID_SYNTHETIC_ONLY_NO_SECOND_SITE_RUN"

    return {
        "schema": "uqpu-scm-cal001-synthetic-fixture-v1",
        "study_id": "SCM-P2-CAL-001-SYNTHETIC",
        "protocol_id": "SCM-P2-CAL-001",
        "protocol_version": "1.0-synthetic",
        "evidence_class": "SYNTHETIC_PIPELINE_VALIDATION_ONLY",
        "seed": seed,
        "samples_per_condition": samples_per_condition,
        "condition_count": len(conditions),
        "threshold_sigma": threshold_sigma,
        "coincidence_channels": coincidence_channels,
        "channels": [
            {"name": channel.name, "noise_sigma": channel.noise_sigma,
             "interference_gain": channel.interference_gain,
             "units": "normalized synthetic z-score"}
            for channel in channels
        ],
        "calibrations": calibrations,
        **bundle,
        "frozen_blinded_scores": frozen_scores,
        "summary_after_truth_unseal": {
            "true_positive": tp,
            "false_negative": fn,
            "true_negative": tn,
            "false_positive": fp,
            "sensitivity": tp / (tp + fn) if tp + fn else None,
            "specificity": tn / (tn + fp) if tn + fp else None,
            "false_positive_rate": fp / (fp + tn) if fp + tn else None,
            "scope": "Synthetic fixture counts only; not estimates of physical detector performance.",
        },
        "dataset_bundle_sha256": bundle_sha,
        "replication_manifest": replication_manifest,
        "replication_manifest_validation_errors": manifest_errors,
        "independent_site_manifest": {
            "status": "NOT_EXECUTED_NO_SECOND_SITE",
            "primary_site_id": None,
            "replication_site_id": None,
            "independent_team": None,
            "required_environment_fields": list(REQUIRED_ENVIRONMENT_FIELDS),
            "source_claim_supported": False,
            "human_participants": False,
        },
        "blinding_boundary": "Observation payloads omit condition labels, but the same JSON bundle contains labeled truth and a labeled trial ledger; anyone with the artifact can unseal it. This is not operational blinding or a human study.",
        "non_claims": [
            "no physical sensor calibration",
            "no human-participant data",
            "no paranormal or cross-realm test",
            "no independent site replication",
            "no real-world sensitivity or specificity estimate",
        ],
    }
