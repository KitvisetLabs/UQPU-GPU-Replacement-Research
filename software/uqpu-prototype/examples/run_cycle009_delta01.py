#!/usr/bin/env python3
"""Regenerate the Cycle 009 Delta 01 bounded twelve-lane gate artifact."""

from __future__ import annotations

from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PROTOTYPE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOTYPE))

from uqpu.cycle007_delta01 import validate_content_range
from uqpu.cycle009_delta01 import (
    LANES,
    build_three_way_ai_manifest,
    build_versioned_request_receipt,
    canonical_json_sha256,
    compare_preregistered_restart_budgets,
    compute_cost_interval_with_uncertainty,
    measure_local_io_scope_screen,
    rank_evidence_gate_sensitivity_grid,
    simulate_interrupted_atomic_publication,
    validate_er6_semantic_certificate,
    validate_fictional_state_transition,
    validate_io_process_record,
    validate_offline_zip_metadata,
    validate_synthetic_material_provenance,
    validate_synthetic_uncertainty_budget,
    validate_three_way_ai_manifest,
    validate_typed_quantity_declaration,
    validate_versioned_request_envelope,
    validate_versioned_request_replay,
)

ROOT = Path(__file__).resolve().parents[3]
FIXTURE_PATH = ROOT / "benchmarks/experiments/cycle009-delta01-preregistered-gates.json"
DEFAULT_OUTPUT = ROOT / "benchmarks/results/cycle009-delta01-executable-acceptance.json"
TEST_IDS = {
    "A": "test_lane_a_preregistered_budgets_include_a_falsifying_gap",
    "B": "test_lane_b_canonical_order_is_stable_and_payload_mutation_fails",
    "C": "test_lane_c_labels_process_scope_and_injected_interruption_boundaries",
    "D": "test_lane_d_offline_range_and_zip_mutations_reject",
    "E": "test_lane_e_material_control_calibration_and_units_are_scoped",
    "F": "test_lane_f_zero_outputs_and_incomplete_cost_keep_totals_null",
    "G": "test_lane_g_uncertainty_budget_requires_method_coverage_scope_and_all_components",
    "H": "test_lane_h_assumption_grid_records_rank_reversal_without_capital",
    "FND/EQN": "test_lane_fnd_eqn_requires_source_linked_explicit_dimension_type",
    "SCM": "test_lane_scm_version_state_volume_links_consent_and_replay_fail_closed",
    "AI-COST": "test_lane_ai_cost_three_way_splits_hashes_and_metrics_are_checked",
    "QOS/QSVT": "test_lane_qos_er6_register_measurement_and_resource_mutations_reject",
}
EVIDENCE_CLASS = {
    "A": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
    "B": "SYNTHETIC_VERSIONED_REQUEST_RECEIPT_GATE",
    "C": "LOCAL_REPEATED_FRESH_PROCESS_AND_FAULT_INJECTION_SOFTWARE_SCREEN_ONLY",
    "D": "OFFLINE_SYNTHETIC_HTTP_RANGE_AND_ZIP_METADATA_GATE",
    "E": "SYNTHETIC_MATERIAL_PROVENANCE_MUTATION_GATE",
    "F": "SYNTHETIC_COST_INTERVAL_WITH_UNCERTAINTY",
    "G": "SYNTHETIC_UNCERTAINTY_BUDGET",
    "H": "ILLUSTRATIVE_ASSUMPTION_GRID_ONLY",
    "FND/EQN": "BOUNDED_SOURCE_LINKED_TYPED_DECLARATION_AUDIT",
    "SCM": "FICTIONAL_VERSIONED_TRANSITION_MUTATION_GATE",
    "AI-COST": "SYNTHETIC_THREE_WAY_MANIFEST_GATE",
    "QOS/QSVT": "FROZEN_ER6_SEMANTIC_AND_RESOURCE_CERTIFICATE",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run_tests() -> dict:
    inherited = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = os.pathsep.join([str(PROTOTYPE), inherited] if inherited else [str(PROTOTYPE)])
    records = {}
    for name, command in (
        ("cycle009_focused", [sys.executable, "-m", "unittest", "tests.test_cycle009_delta01", "-v"]),
        ("full_prototype_suite", [sys.executable, "-m", "unittest", "discover", "-s", "tests"]),
    ):
        completed = subprocess.run(command, cwd=PROTOTYPE, capture_output=True, text=True, timeout=300, check=False)
        output = completed.stdout + completed.stderr
        summary = re.search(r"Ran (\d+) tests? in [^\n]+", output)
        skipped = re.search(r"skipped=(\d+)", output)
        if completed.returncode or summary is None:
            raise RuntimeError(f"{name} failed or emitted no unittest summary:\n{output[-5000:]}")
        if name == "cycle009_focused":
            missing = [test_id for test_id in TEST_IDS.values() if test_id not in output]
            if missing:
                raise RuntimeError("focused output omitted lane test(s): " + ", ".join(missing))
        records[name] = {
            "command": command[1:], "status": "PASS", "tests_run": int(summary.group(1)),
            "optional_skips": int(skipped.group(1)) if skipped else 0,
        }
    return records


def build_artifact() -> dict:
    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    tests = _run_tests()
    lane = fixtures["lanes"]

    a = lane["A"]
    result_a = compare_preregistered_restart_budgets(
        seed=a["seed"], node_count=a["node_count"], edge_probability=a["edge_probability"],
        budgets=tuple(a["restart_budgets"]), state_cap=a["exact_state_cap"])

    b = lane["B"]
    envelope = build_versioned_request_receipt(b["request"], source_commit=fixtures["base_closeout_commit"])
    result_b = validate_versioned_request_envelope(envelope)
    permuted = dict(envelope, request={key: envelope["request"][key] for key in reversed(list(envelope["request"]))})
    changed_payload = json.loads(json.dumps(envelope["request"]))
    changed_payload["payload"]["value"] += 1
    changed_payload["payload_sha256"] = canonical_json_sha256(changed_payload["payload"])
    changed = dict(envelope, request=changed_payload)
    replay_result = validate_versioned_request_replay(envelope["request"], permuted["request"])
    changed_replay = validate_versioned_request_replay(envelope["request"], changed["request"])
    result_b.update({"key_order_invariant": validate_versioned_request_envelope(permuted)["valid"],
                     "payload_mutation_rejected": "request_hash_mismatch" in validate_versioned_request_envelope(changed)["errors"] and "same_token_payload_mutated" in changed_replay["errors"],
                     "unchanged_replay_accepted": replay_result["valid"],
                     "request_sha256": envelope["receipt"]["request_sha256"]})

    c = lane["C"]
    expected = hashlib.sha256(b"cycle009-local-io-fixture").hexdigest()
    process_rows = {scope: validate_io_process_record({
        "process_scope": scope, "cache_state": c["cache_state"], "device_flush_claim": False,
        "power_loss_claim": False, "readback_sha256": expected, "expected_sha256": expected,
    }) for scope in c["process_scopes"]}
    interruption_rows = {stage: simulate_interrupted_atomic_publication(
        c["old_payload"].encode(), c["new_payload"].encode(), interrupt_after=stage)
        for stage in c["injected_boundaries"]}
    io_probe = measure_local_io_scope_screen({"cycle": "009", "fixture": "synthetic-local-io"})

    d = lane["D"]
    range_result = validate_content_range(**d["range"])
    zip_result = validate_offline_zip_metadata(d["zip_metadata"])
    bad_range = validate_content_range(status=200, content_range="bytes 0-7/64", start=0, end=7, total=64, body_length=8)
    bad_zip = json.loads(json.dumps(d["zip_metadata"]))
    bad_zip["entries"][0]["local_header_offset"] = bad_zip["central_start"]
    bad_zip_result = validate_offline_zip_metadata(bad_zip)

    e = lane["E"]
    result_e = validate_synthetic_material_provenance(e["record"], as_of=date.fromisoformat(e["as_of"]))
    changed_e = dict(e["record"], uncertainty_unit="cm")

    f = lane["F"]
    result_f = compute_cost_interval_with_uncertainty(f)
    zero_f = compute_cost_interval_with_uncertainty(dict(f, accepted_outputs=0))
    incomplete_f = dict(f, components={"compute": f["components"]["compute"]})
    incomplete_f = compute_cost_interval_with_uncertainty(incomplete_f)

    g = lane["G"]
    result_g = validate_synthetic_uncertainty_budget(g["budget"], as_of=date.fromisoformat(g["as_of"]))
    missing_g = validate_synthetic_uncertainty_budget(
        dict(g["budget"], reported_component_ids=["u1"]), as_of=date.fromisoformat(g["as_of"]))

    h = lane["H"]
    result_h = rank_evidence_gate_sensitivity_grid(h["gates"], h["scenarios"])

    eqn = lane["FND/EQN"]
    result_eqn = validate_typed_quantity_declaration(eqn["declaration"], eqn["unit_registry"])
    unclassified_eqn = validate_typed_quantity_declaration(
        dict(eqn["declaration"], unit_code=None, dimension_vector=None), eqn["unit_registry"])

    scm = lane["SCM"]
    transition = scm["transition"]
    result_scm = validate_fictional_state_transition(
        transition, states=set(scm["states"]), equations=set(scm["equations"]), used_nonces=set())
    replay_scm = validate_fictional_state_transition(
        transition, states=set(scm["states"]), equations=set(scm["equations"]), used_nonces={transition["consent_nonce"]})

    ai = lane["AI-COST"]
    computed_source_hashes = {name: canonical_json_sha256(payload) for name, payload in ai["source_payloads"].items()}
    source_hashes_match = computed_source_hashes == ai["source_hashes"]
    manifest = build_three_way_ai_manifest(ai["split_ids"], ai["source_hashes"], ai["required_metrics"])
    manifest["metric_values"] = ai["metric_values"]
    result_ai = validate_three_way_ai_manifest(manifest, expected_source_hashes=ai["source_hashes"])
    overlap_ids = json.loads(json.dumps(ai["split_ids"]))
    overlap_ids["test"] = [overlap_ids["train"][0]]
    overlap = build_three_way_ai_manifest(overlap_ids, ai["source_hashes"], ai["required_metrics"])
    overlap["metric_values"] = ai["metric_values"]
    overlap_result = validate_three_way_ai_manifest(overlap, expected_source_hashes=ai["source_hashes"])

    qos = lane["QOS/QSVT"]
    result_qos = validate_er6_semantic_certificate(qos["source"], qos["candidate"], qos["resource_bounds"])
    changed_qos = dict(qos["candidate"], measurement_destinations=[{"qubit": "q[0]", "bit": "c[1]"}])
    changed_qos_result = validate_er6_semantic_certificate(qos["source"], changed_qos, qos["resource_bounds"])
    bounded_qos = json.loads(json.dumps(qos["candidate"])); bounded_qos["resources"]["depth"] = qos["resource_bounds"]["depth"] + 1
    over_qos_result = validate_er6_semantic_certificate(qos["source"], bounded_qos, qos["resource_bounds"])

    lane_results = {
        "A": {"passed": True, "exact_control": result_a["exact_control"], "budget_results": result_a["budget_results"], "fixture": result_a["fixture"]},
        "B": {"passed": result_b["valid"] and result_b["key_order_invariant"] and result_b["unchanged_replay_accepted"] and result_b["payload_mutation_rejected"], **result_b},
        "C": {"passed": all(not errors for errors in process_rows.values()) and all(row["sha256_matches"] for row in io_probe["rows"]) and all(row["old_or_new_payload_preserved"] for row in interruption_rows.values()), "process_scope_errors": process_rows, "io_probe": io_probe, "interruption_rows": interruption_rows, "cache_state": c["cache_state"]},
        "D": {"passed": not range_result and not zip_result and "http_status_must_be_206" in bad_range and any(x.startswith("zip_local_header_offset_invalid") for x in bad_zip_result), "valid_range_errors": range_result, "valid_zip_errors": zip_result, "http_200_rejected": bad_range, "malformed_zip_rejected": bad_zip_result, "archive_downloaded": False, "payload_read": False},
        "E": {"passed": result_e["valid"] and "uncertainty_unit_mismatch" in validate_synthetic_material_provenance(changed_e, as_of=date.fromisoformat(e["as_of"]))["errors"], "valid_record": result_e, "physical_measurement_claim": False},
        "F": {"passed": result_f["complete"] and zero_f["total_interval"] is None and incomplete_f["total_interval"] is None, **result_f, "zero_output_totals": zero_f["total_interval"], "incomplete_component_totals": incomplete_f["total_interval"]},
        "G": {"passed": result_g["valid"] and "unreported_uncertainty_component" in missing_g["errors"], **result_g, "unreported_component_errors": missing_g["errors"]},
        "H": {"passed": len({tuple(row["ranking"]) for row in result_h["rankings"]}) > 1 and not result_h["capital_authorized"], **result_h},
        "FND/EQN": {"passed": result_eqn["valid"] and "unit_unclassified_or_unregistered" in unclassified_eqn["errors"], "typed_declaration": result_eqn, "unclassified_declaration_errors": unclassified_eqn["errors"]},
        "SCM": {"passed": result_scm["valid"] and "transition_consent_nonce_replayed" in replay_scm["errors"], "transition": result_scm, "replay_errors": replay_scm["errors"], "empirical_coupling": None},
        "AI-COST": {"passed": result_ai["valid"] and source_hashes_match and any(error.startswith("split_overlap:") for error in overlap_result["errors"]), "valid_manifest": result_ai, "source_hashes_match_synthetic_payloads": source_hashes_match, "computed_source_hashes": computed_source_hashes, "overlap_rejected": overlap_result["errors"], "scoring_performed": False},
        "QOS/QSVT": {"passed": result_qos["valid"] and "er6_semantics_changed:measurement_destinations" in changed_qos_result["errors"] and "er6_resource_bound_exceeded:depth" in over_qos_result["errors"], "valid_certificate": result_qos, "measurement_mutation_errors": changed_qos_result["errors"], "resource_overrun_errors": over_qos_result["errors"], "hardware_receipt": None},
    }
    failed = [name for name, row in lane_results.items() if not row["passed"]]
    if failed or set(lane_results) != set(LANES):
        raise RuntimeError(f"lane artifact gate failure: {failed or 'lane set mismatch'}")

    return {
        "schema": "uqpu-cycle009-delta01-executable-acceptance-v1",
        "cycle": "009", "delta": "01", "reviewed_date": date.today().isoformat(),
        "base_closeout_commit": fixtures["base_closeout_commit"],
        "status": "PASS_LOCAL_GATES_CYCLE_CLOSEOUT_PENDING_EXACT_SHA_CI",
        "lane_count": len(lane_results),
        "lanes": {name: {"status": "PASS", "lane_status": "BLOCKED_WITH_PROGRESS",
                         "evidence_class": EVIDENCE_CLASS[name], "test": TEST_IDS[name], **row}
                  for name, row in lane_results.items()},
        "test_runs": tests,
        "fixtures_artifact": "benchmarks/experiments/cycle009-delta01-preregistered-gates.json",
        "provenance": {
            "fixtures_sha256": sha256(FIXTURE_PATH),
            "implementation": "software/uqpu-prototype/uqpu/cycle009_delta01.py",
            "implementation_sha256": sha256(ROOT / "software/uqpu-prototype/uqpu/cycle009_delta01.py"),
            "tests": "software/uqpu-prototype/tests/test_cycle009_delta01.py",
            "tests_sha256": sha256(ROOT / "software/uqpu-prototype/tests/test_cycle009_delta01.py"),
            "runner": "software/uqpu-prototype/examples/run_cycle009_delta01.py",
            "runner_sha256": sha256(ROOT / "software/uqpu-prototype/examples/run_cycle009_delta01.py"),
            "handoff": "docs/SYNCHRONIZED_CYCLE_009_HANDOFF_2026-09-28.md",
            "handoff_sha256": sha256(ROOT / "docs/SYNCHRONIZED_CYCLE_009_HANDOFF_2026-09-28.md"),
        },
        "primary_source_basis": [
            {"url": "repo:docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md#1-typed-project-quantities", "access_date": "2026-09-28", "retrieval_status": "VERIFIED_GITHUB_SOURCE", "evidence_class": "PROJECT_PRIMARY_SOURCE_DOCUMENT", "scope": "UMRL-007 declares accepted throughput as accepted count per elapsed time; this cycle only adds a linked exact unit/type declaration."},
            {"url": "https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html", "access_date": "2026-09-28", "retrieval_status": "DIRECT_FETCH_SUCCESS", "evidence_class": "OFFICIAL_PROVIDER_API_DOCUMENTATION", "scope": "Request field names only; no job was submitted."},
            {"url": "https://www.nist.gov/pml/nist-technical-note-1297/nist-guidelines-evaluating-and-expressing-uncertainty-nist-measurement", "access_date": "2026-09-28", "retrieval_status": "FETCH_FAILED_SERVER_ERROR", "evidence_class": "OFFICIAL_METROLOGY_REFERENCE_NOT_RETRIEVED", "scope": "Direct fetch returned a server error on 2026-09-28; retained as a reference only, with no NIST-specific guidance attributed in this cycle."},
            {"url": "https://openqasm.com/versions/3.1/language/insts.html", "access_date": "2026-09-28", "retrieval_status": "DIRECT_FETCH_SUCCESS", "evidence_class": "LANGUAGE_SPECIFICATION", "scope": "ER6 measurement destination semantics for a frozen subset only."},
            {"url": "https://docs.python.org/3/library/os.html#os.replace", "access_date": "2026-09-28", "retrieval_status": "DIRECT_FETCH_SUCCESS", "evidence_class": "OFFICIAL_LANGUAGE_LIBRARY_DOCUMENTATION", "scope": "Local rename API behavior; no power-loss or hardware durability claim."},
        ],
        "assumptions": [
            "Every positive material, cost, uncertainty, SCM, AI, QOS, and provider-shaped record is synthetic.",
            "The H-lane effort and blocker-impact values are illustrative assumptions and are not measurements.",
            "The A-lane exact enumeration is restricted to 256 states under a 1,024-state cap.",
            "The interrupted-write tests inject software exceptions at named boundaries; they do not kill power or validate a storage device.",
        ],
        "uncertainty": [
            "A finite seeded MaxCut fixture and local runtimes do not establish general solver behavior.",
            "The cost RSS output assumes independent components; its variance and expanded uncertainty are model-only.",
            "The offline archive fixtures test declared metadata consistency only; no archive bytes are fetched.",
        ],
        "nonclaims": fixtures["nonclaims"],
        "external_gates_remaining": [
            "No provider authorization, task, receipt, or bill.",
            "No cache control, service durability, device flush, or power-loss evidence.",
            "No physical material sample, operational calibration, or measured uncertainty.",
            "No measured lifecycle economics, capital authorization, or candidate-system performance.",
            "No new physical law, quantum advantage, GPU replacement, or empirical SCM coupling.",
            "No provider transpilation or hardware execution of ER6/QSVT workloads.",
        ],
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    artifact = build_artifact()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "cycle": artifact["cycle"],
                      "lane_count": artifact["lane_count"], "status": artifact["status"],
                      "focused_tests": artifact["test_runs"]["cycle009_focused"]["tests_run"],
                      "full_suite_tests": artifact["test_runs"]["full_prototype_suite"]["tests_run"]}, sort_keys=True))


if __name__ == "__main__":
    main()
