#!/usr/bin/env python3
"""Generate Cycle 010's bounded synchronized 12-lane acceptance artifact."""

from __future__ import annotations

from copy import deepcopy
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
ROOT = Path(__file__).resolve().parents[3]
FIXTURE_PATH = ROOT / "benchmarks/experiments/cycle010-delta01-preregistered-gates.json"
DEFAULT_OUTPUT = ROOT / "benchmarks/results/cycle010-delta01-executable-acceptance.json"
TEST_IDS = {
    "A": "test_lane_a_three_preregistered_instances_keep_restart_prefix",
    "B": "test_lane_b_duplicate_keys_reject_and_supported_versions_migrate",
    "C": "test_lane_c_named_process_scopes_and_interruption_rows_are_labeled",
    "D": "test_lane_d_zip64_bounds_and_valid_unsatisfied_range_response",
    "E": "test_lane_e_material_provenance_mutations_fail_closed",
    "F": "test_lane_f_correlated_cost_interval_separates_cost_from_uncertainty",
    "G": "test_lane_g_uncertainty_budget_checks_scope_units_expiry_and_psd",
    "H": "test_lane_h_larger_assumed_grid_records_sensitivity_and_no_capital",
    "FND/EQN": "test_lane_fnd_eqn_source_linked_cost_and_energy_units_are_exact",
    "SCM": "test_lane_scm_versioned_graph_requires_all_volume_links_consent_and_firewall",
    "AI-COST": "test_lane_ai_cost_manifest_binds_raw_synthetic_bytes_before_scoring",
    "QOS/QSVT": "test_lane_qos_er6_certificate_checks_source_register_measurement_and_bounds",
}
EVIDENCE_CLASSES = {
    "A": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
    "B": "SYNTHETIC_SCHEMA_MIGRATION_AND_DUPLICATE_KEY_GATE",
    "C": "LOCAL_SOFTWARE_FILESYSTEM_SCREEN_ONLY",
    "D": "SYNTHETIC_ZIP64_METADATA_VALIDATION",
    "E": "SYNTHETIC_MATERIAL_PROVENANCE_MUTATION_GATE",
    "F": "SYNTHETIC_COST_AND_COVARIANCE_MODEL",
    "G": "SYNTHETIC_UNCERTAINTY_BUDGET",
    "H": "ILLUSTRATIVE_ASSUMPTION_GRID_ONLY",
    "FND/EQN": "SOURCE_LINKED_EXACT_DERIVED_UNIT_DECLARATIONS",
    "SCM": "FICTION_ONLY_VERSIONED_GRAPH",
    "AI-COST": "SYNTHETIC_IMMUTABLE_SOURCE_MANIFEST",
    "QOS/QSVT": "FROZEN_ER6_SEMANTIC_RESOURCE_CERTIFICATE",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_tests() -> dict:
    inherited = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = os.pathsep.join([str(PROTOTYPE), inherited] if inherited else [str(PROTOTYPE)])
    records = {}
    for name, command in (
        ("cycle010_focused", [sys.executable, "-m", "unittest", "tests.test_cycle010_delta01", "-v"]),
        ("full_prototype_suite", [sys.executable, "-m", "unittest", "discover", "-s", "tests"]),
    ):
        completed = subprocess.run(command, cwd=PROTOTYPE, capture_output=True, text=True, timeout=360, check=False)
        output = completed.stdout + completed.stderr
        summary = re.search(r"Ran (\d+) tests? in [^\n]+", output)
        skipped = re.search(r"skipped=(\d+)", output)
        if completed.returncode or summary is None:
            raise RuntimeError(f"{name} failed or emitted no unittest summary:\n{output[-6000:]}")
        if name == "cycle010_focused":
            missing = [test_id for test_id in TEST_IDS.values() if test_id not in output]
            if missing:
                raise RuntimeError("focused test run omitted lane test(s): " + ", ".join(missing))
        records[name] = {
            "command": command[1:],
            "status": "PASS",
            "tests_run": int(summary.group(1)),
            "optional_skips": int(skipped.group(1)) if skipped else 0,
        }
    return records


def build_artifact() -> dict:
    from uqpu.cycle010_delta01 import (
        LANES,
        build_ai_source_manifest,
        canonical_sha256,
        derive_dimension_vector,
        migrate_request_envelope,
        parse_json_reject_duplicates,
        propagate_cost_interval,
        rank_assumed_gate_grid,
        run_local_atomic_write_protocol,
        run_maxcut_restart_sweep,
        sha256_bytes,
        validate_ai_source_manifest,
        validate_er6_register_certificate,
        validate_fictional_state_graph,
        validate_http_range_response,
        validate_material_provenance,
        validate_request_replay,
        validate_sourced_quantity,
        validate_uncertainty_budget,
        validate_zip64_metadata,
    )

    fixtures = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    tests = run_tests()
    lanes = fixtures["lanes"]

    # A — Exact control and deterministic restart-prefix sweep.
    a = run_maxcut_restart_sweep(lanes["A"]["instances"], lanes["A"]["restart_budgets"], lanes["A"]["exact_state_cap"])
    a_passed = len(a["instances"]) >= 3 and all(
        all(row["exact_complete"] and row["gap_to_exact"] >= 0 for row in instance["results"])
        and instance["results"][1]["restart_start_sha256"][:1] == instance["results"][0]["restart_start_sha256"]
        and instance["results"][2]["restart_start_sha256"][:4] == instance["results"][1]["restart_start_sha256"]
        and instance["results"][3]["restart_start_sha256"][:16] == instance["results"][2]["restart_start_sha256"]
        for instance in a["instances"]
    )

    # B — Duplicate-key failure precedes migration and canonical hashing.
    b = lanes["B"]
    duplicate_rejected = False
    try:
        parse_json_reject_duplicates('{"schema_version":1,"schema_version":2}')
    except ValueError as exc:
        duplicate_rejected = "duplicate_json_key" in str(exc)
    migrated = migrate_request_envelope(b["schema_v1"])
    reordered_v1 = {"request": b["schema_v1"]["request"], "source_commit": b["schema_v1"]["source_commit"], "idempotency_token": b["schema_v1"]["idempotency_token"], "schema_version": 1}
    changed = deepcopy(b["schema_v1"]); changed["request"]["shots"] += 1
    replay = validate_request_replay(b["schema_v1"], reordered_v1)
    changed_replay = validate_request_replay(b["schema_v1"], changed)
    b_result = {"duplicate_keys_rejected_before_parse": duplicate_rejected, "migrated_schema_version": migrated["schema_version"], "migrated_payload_sha256": migrated["payload_sha256"], "key_order_invariant": migrated == migrate_request_envelope(reordered_v1), "unchanged_replay_accepted": replay["valid"], "payload_change_rejected": not changed_replay["valid"], "network_submission_enabled": False}
    b_result["passed"] = duplicate_rejected and b_result["migrated_schema_version"] == 2 and b_result["key_order_invariant"] and replay["valid"] and not changed_replay["valid"]

    # C — Same-process, child-process and named exception boundary outcomes.
    c = run_local_atomic_write_protocol()
    c["passed"] = c["all_hashes_match"] and c["all_interrupted_payloads_preserved"] and len(c["rows"]) == 2

    # D — Offline ZIP64 directory records and valid/invalid HTTP range semantics.
    d = lanes["D"]
    zip_valid = validate_zip64_metadata(d["zip64"])
    bad_offset = deepcopy(d["zip64"]); bad_offset["zip64_locator_offset"] += 1
    bad_overflow = deepcopy(d["zip64"]); bad_overflow["entries"][0]["zip64_extra"]["compressed_size"] = 1 << 64
    bad_local = deepcopy(d["zip64"]); bad_local["entries"][0]["zip64_extra"]["local_header_offset"] = bad_local["central_directory_start"] + 1
    valid_416 = validate_http_range_response(**d["valid_unsatisfied_range"])
    invalid_416 = validate_http_range_response(416, "bytes */127", 128, 0)
    invalid_body = validate_http_range_response(206, "bytes 0-7/128", 128, 7, start=0, end=7)
    d_result = {"valid_zip64": zip_valid, "zip64_locator_mutation_rejected": not validate_zip64_metadata(bad_offset)["valid"], "zip64_uint64_overflow_rejected": not validate_zip64_metadata(bad_overflow)["valid"], "zip64_local_offset_rejected": not validate_zip64_metadata(bad_local)["valid"], "valid_unsatisfied_range": valid_416, "inconsistent_416_rejected": not invalid_416["valid"], "short_206_body_rejected": not invalid_body["valid"], "archive_downloaded": False, "payload_read": False}
    d_result["passed"] = bool(zip_valid["valid"] and d_result["zip64_locator_mutation_rejected"] and d_result["zip64_uint64_overflow_rejected"] and d_result["zip64_local_offset_rejected"] and valid_416["valid"] and d_result["inconsistent_416_rejected"] and d_result["short_206_body_rejected"])

    # E — Synthetic material provenance positives and adversarial mutations.
    e = lanes["E"]
    as_of = date.fromisoformat(e["as_of"])
    e_valid = validate_material_provenance(e["record"], as_of)
    e_mutations = {
        "sample_control_identity": dict(e["record"], control_id=e["record"]["sample_id"]),
        "missing_issuer": dict(e["record"], calibration_issuer=""),
        "scope_mismatch": dict(e["record"], calibration_scope=["density"]),
        "expired_calibration": dict(e["record"], calibration_expiry="2020-01-01"),
        "uncertainty_unit_mismatch": dict(e["record"], uncertainty_unit="mS/m"),
    }
    e_negatives = {name: validate_material_provenance(row, as_of)["errors"] for name, row in e_mutations.items()}
    e_result = {"valid_record": e_valid, "mutation_errors": e_negatives, "physical_measurement_claim": False, "passed": e_valid["valid"] and all(errors for errors in e_negatives.values())}

    # F — Cost interval and distinct correlated/independent covariance cases.
    f = lanes["F"]
    f_independent = propagate_cost_interval(dict(f, correlation_matrix=f["independent_correlation_matrix"]))
    f_correlated = propagate_cost_interval(dict(f, correlation_matrix=f["correlated_correlation_matrix"]))
    f_non_psd = propagate_cost_interval(dict(f, correlation_matrix=f["non_psd_correlation_matrix"]))
    f_missing_covariance = propagate_cost_interval(f)
    f_zero = propagate_cost_interval(dict(f, accepted_outputs=0, correlation_matrix=f["independent_correlation_matrix"]))
    f_incomplete = propagate_cost_interval(dict(f, required_components=["compute", "data", "unavailable"], correlation_matrix=f["independent_correlation_matrix"]))
    f_result = {"independent": f_independent, "correlated": f_correlated, "non_psd": f_non_psd, "missing_covariance": f_missing_covariance, "zero_outputs": f_zero, "incomplete_cost": f_incomplete, "passed": f_independent["uncertainty"] is not None and f_correlated["uncertainty"] is not None and f_non_psd["uncertainty"] is None and f_missing_covariance["uncertainty"] is None and f_zero["total_interval"] is None and f_incomplete["total_interval"] is None}

    # G — Certificate-style scope, unit, expiry, method, component and PSD checks.
    g = lanes["G"]
    g_budget = g["budget"]
    g_as_of = date.fromisoformat(g["as_of"])
    g_valid = validate_uncertainty_budget(g_budget, g_as_of)
    g_mutations = {
        "components_incomplete": dict(g_budget, components=g_budget["components"][:1]),
        "method_missing": dict(g_budget, method="UNDECLARED"),
        "scope_mismatch": dict(g_budget, scope="other"),
        "unit_mismatch": dict(g_budget, expected_unit="kg"),
        "expired": dict(g_budget, certificate_expiry="2020-01-01"),
        "non_psd": dict(g_budget, correlation_matrix=[[1, 1.5], [1.5, 1]]),
    }
    g_errors = {name: validate_uncertainty_budget(row, g_as_of)["errors"] for name, row in g_mutations.items()}
    g_result = {"valid_budget": g_valid, "mutation_errors": g_errors, "passed": g_valid["valid"] and all(errors for errors in g_errors.values())}

    # H — Full 3^6 sensitivity grid over preregistered assumed effort/impact factors.
    h = lanes["H"]
    h_result = rank_assumed_gate_grid(h["gates"], h["multipliers"])
    h_result["passed"] = h_result["scenario_count"] == 729 and h_result["reversal_scenario_count"] > 0 and h_result["capital_authorized"] is False and h_result["capital_amount"] is None

    # FND/EQN — Derive exact vectors from registered USD/W/s/count units and source equations.
    q = lanes["FND/EQN"]
    registry_path = ROOT / q["unit_registry"]
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    registry = deepcopy(registry)
    registry["unit_registry"]["USD/count"] = {"dimension_vector": derive_dimension_vector(registry, ["USD"], ["count"])}
    registry["unit_registry"]["J/count"] = {"dimension_vector": derive_dimension_vector(registry, ["W", "s"], ["count"])}
    fnd_rows = []
    for item in q["quantities"]:
        vector = derive_dimension_vector(registry, item["numerator_units"], item["denominator_units"])
        source_locator = q["primary_sources"][item["source_index"]]
        source_file = source_locator.split("#", 1)[0]
        declaration = {"quantity_id": item["quantity_id"], "quantity_kind": item["quantity_kind"], "unit_code": item["unit_code"], "dimension_vector": vector, "domain_sort": "REAL_MODEL", "source_locator": source_locator, "source_sha256": sha256(ROOT / source_file)}
        valid = validate_sourced_quantity(declaration, registry)
        wrong = dict(declaration, dimension_vector={name: "0" for name in registry["dimension_basis"]})
        fnd_rows.append({"declaration": declaration, "valid": valid, "counterexample_errors": validate_sourced_quantity(wrong, registry)["errors"]})
    fnd_result = {"quantities": fnd_rows, "source_registry_sha256": sha256(registry_path), "passed": len(fnd_rows) == 2 and all(row["valid"]["valid"] and row["counterexample_errors"] for row in fnd_rows)}

    # SCM — Complete versioned fictional state graph and five-volume equation coverage.
    scm = qscm = lanes["SCM"]["graph"]
    scm_valid = validate_fictional_state_graph(scm, used_nonces=set())
    scm_mutations = {}
    for name, mutate in (
        ("unknown_node", lambda x: x["edges"][0].update(to_state="unknown")),
        ("unknown_equation", lambda x: x["edges"][0].update(equation_id="UNKNOWN")),
        ("version_mismatch", lambda x: x["edges"][0].update(canon_version="old")),
        ("cross_sort", lambda x: x["edges"][0].update(domain_sort="REAL_MODEL")),
        ("missing_consent", lambda x: x["edges"][0].update(consent_required=False)),
        ("incomplete_volume", lambda x: x["volume_equation_links"].pop("V5")),
    ):
        copy = deepcopy(scm); mutate(copy); scm_mutations[name] = validate_fictional_state_graph(copy, used_nonces=set())["errors"]
    scm_result = {"valid_graph": scm_valid, "mutation_errors": scm_mutations, "replay_errors": validate_fictional_state_graph(scm, used_nonces={"fic-010-nonce-a"})["errors"], "passed": scm_valid["valid"] and all(errors for errors in scm_mutations.values()) and bool(validate_fictional_state_graph(scm, used_nonces={"fic-010-nonce-a"})["errors"]) and scm_valid["empirical_coupling"] is None}

    # AI-COST — Hash the canonical bytes of each immutable synthetic split source.
    ai = lanes["AI-COST"]
    ai_manifest, ai_bytes = build_ai_source_manifest(ai["source_records"], ai["record_ids"], ai["required_metrics"])
    ai_valid = validate_ai_source_manifest(ai_manifest, ai_bytes)
    ai_changed = dict(ai_bytes, train=ai_bytes["train"] + b"mutated")
    ai_overlap = deepcopy(ai_manifest); ai_overlap["splits"]["test"]["record_ids"] = [ai_manifest["splits"]["train"]["record_ids"][0]]
    ai_missing = deepcopy(ai_manifest); ai_missing["splits"]["validation"]["metrics"].pop("energy_complete")
    ai_unsupported = dict(ai_manifest, schema_version=2)
    ai_result = {"manifest": ai_manifest, "raw_synthetic_source_sha256": {name: sha256_bytes(payload) for name, payload in ai_bytes.items()}, "valid_manifest": ai_valid, "byte_mutation_errors": validate_ai_source_manifest(ai_manifest, ai_changed)["errors"], "split_overlap_errors": validate_ai_source_manifest(ai_overlap, ai_bytes)["errors"], "metric_missing_errors": validate_ai_source_manifest(ai_missing, ai_bytes)["errors"], "unsupported_schema_errors": validate_ai_source_manifest(ai_unsupported, ai_bytes)["errors"], "scoring_performed": False}
    ai_result["passed"] = ai_valid["valid"] and all((ai_result["byte_mutation_errors"], ai_result["split_overlap_errors"], ai_result["metric_missing_errors"], ai_result["unsupported_schema_errors"]))

    # QOS/QSVT — Source-bound frozen register, measurement and resource certificate.
    qo = lanes["QOS/QSVT"]
    candidate = {"source_sha256": canonical_sha256(qo["source"]), "registers": {"qubit_count": qo["source"]["qubit_count"], "bit_count": qo["source"]["bit_count"]}, "measurement_destinations": qo["source"]["measurement_destinations"], "resources": qo["candidate_resources"]}
    qos_valid = validate_er6_register_certificate(qo["source"], candidate, qo["resource_bounds"])
    qos_mutations = {}
    for name, mutate in (
        ("source_hash", lambda x: x.update(source_sha256="0" * 64)),
        ("register_bounds", lambda x: x["registers"].update(qubit_count=qo["resource_bounds"]["qubit_count"] + 1)),
        ("measurement_map", lambda x: x["measurement_destinations"][0].update(bit="c[1]")),
        ("resource_bounds", lambda x: x["resources"].update(depth=qo["resource_bounds"]["depth"] + 1)),
    ):
        copy = deepcopy(candidate); mutate(copy); qos_mutations[name] = validate_er6_register_certificate(qo["source"], copy, qo["resource_bounds"])["errors"]
    qos_result = {"candidate": candidate, "valid_certificate": qos_valid, "mutation_errors": qos_mutations, "hardware_receipt": None, "passed": qos_valid["valid"] and all(errors for errors in qos_mutations.values())}

    lane_results = {
        "A": {"passed": a_passed, "evidence_class": EVIDENCE_CLASSES["A"], "result": a},
        "B": {"passed": b_result["passed"], "evidence_class": EVIDENCE_CLASSES["B"], **b_result},
        "C": {"passed": c["passed"], "evidence_class": EVIDENCE_CLASSES["C"], **c},
        "D": {"passed": d_result["passed"], "evidence_class": EVIDENCE_CLASSES["D"], **d_result},
        "E": {"passed": e_result["passed"], "evidence_class": EVIDENCE_CLASSES["E"], **e_result},
        "F": {"passed": f_result["passed"], "evidence_class": EVIDENCE_CLASSES["F"], **f_result},
        "G": {"passed": g_result["passed"], "evidence_class": EVIDENCE_CLASSES["G"], **g_result},
        "H": {"passed": h_result["passed"], "evidence_class": EVIDENCE_CLASSES["H"], **h_result},
        "FND/EQN": {"passed": fnd_result["passed"], "evidence_class": EVIDENCE_CLASSES["FND/EQN"], **fnd_result},
        "SCM": {"passed": scm_result["passed"], "evidence_class": EVIDENCE_CLASSES["SCM"], **scm_result},
        "AI-COST": {"passed": ai_result["passed"], "evidence_class": EVIDENCE_CLASSES["AI-COST"], **ai_result},
        "QOS/QSVT": {"passed": qos_result["passed"], "evidence_class": EVIDENCE_CLASSES["QOS/QSVT"], **qos_result},
    }
    failed = [name for name, row in lane_results.items() if not row["passed"]]
    if failed or set(lane_results) != set(LANES):
        raise RuntimeError("Cycle 010 lane acceptance failed: " + ", ".join(failed or ["lane-set-mismatch"]))

    return {
        "schema": "uqpu-cycle010-delta01-executable-acceptance-v1",
        "cycle": "010",
        "delta": "01",
        "reviewed_date": date.today().isoformat(),
        "base_closeout_commit": fixtures["base_closeout_commit"],
        "status": "PASS_LOCAL_GATES_CYCLE_CLOSEOUT_PENDING_EXACT_SHA_CI",
        "lane_count": len(lane_results),
        "lanes": {name: {"status": "PASS", "lane_status": "BLOCKED_WITH_PROGRESS", "test": TEST_IDS[name], **row} for name, row in lane_results.items()},
        "test_runs": tests,
        "fixtures_artifact": "benchmarks/experiments/cycle010-delta01-preregistered-gates.json",
        "provenance": {
            "fixtures_sha256": sha256(FIXTURE_PATH),
            "implementation": "software/uqpu-prototype/uqpu/cycle010_delta01.py",
            "implementation_sha256": sha256(ROOT / "software/uqpu-prototype/uqpu/cycle010_delta01.py"),
            "tests": "software/uqpu-prototype/tests/test_cycle010_delta01.py",
            "tests_sha256": sha256(ROOT / "software/uqpu-prototype/tests/test_cycle010_delta01.py"),
            "runner": "software/uqpu-prototype/examples/run_cycle010_delta01.py",
            "runner_sha256": sha256(ROOT / "software/uqpu-prototype/examples/run_cycle010_delta01.py"),
            "handoff": "docs/SYNCHRONIZED_CYCLE_010_HANDOFF_2026-09-28.md",
            "handoff_sha256": sha256(ROOT / "docs/SYNCHRONIZED_CYCLE_010_HANDOFF_2026-09-28.md"),
        },
        "primary_source_basis": [
            {"url": "repo:docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md#1-typed-project-quantities", "access_date": "2026-09-28", "evidence_class": "PROJECT_PRIMARY_SOURCE_DOCUMENT", "scope": "Source locator for accepted-output definitions; the cycle adds exact derived units for cost and energy per accepted output."},
            {"url": "repo:00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md#4-functional-equivalence-and-accepted-outputs", "access_date": "2026-09-28", "evidence_class": "PROJECT_PRIMARY_SOURCE_DOCUMENT", "scope": "UMRL-007 defines cost and energy per accepted output and their null-on-zero/unknown rule."},
            {"url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT", "access_date": "2026-09-28", "publication_date": "2022-11-01", "version": "6.3.10 FINAL", "evidence_class": "OFFICIAL_FORMAT_SPECIFICATION", "scope": "ZIP64 end-of-central-directory, locator and extra-field structure vocabulary only; no archive bytes were downloaded or checked."}
        ],
        "assumptions": [
            "A uses three fixed-seed eight-node unit-weight graphs, exact enumeration capped at 512 states, and deterministic greedy local search; host timings depend on this machine.",
            "F/G covariance entries, component values and coverage factors are synthetic model inputs; the covariance matrix is restricted to a 2x2 correlation example.",
            "H explores a preregistered 729-point Cartesian grid of assumed multipliers; gate ranking is a project heuristic, not a measured quantity.",
            "C software exception injection is not process termination or power-loss testing; filesystem cache is uncontrolled.",
            "FND/EQN derives USD/count and J/count vectors from declared source units and equations; this tests dimensional consistency only."
        ],
        "uncertainty": [
            "Host runtime varies by environment and is reported separately from objective/gap.",
            "The 2x2 expanded uncertainty is a synthetic calculation; no metrology result or coverage guarantee is inferred.",
            "The H stability grid is conditional on the stated assumptions and does not estimate real gate cost or value."
        ],
        "nonclaims": fixtures["nonclaims"],
        "external_gates_remaining": [
            "No provider authorization, submission, provider receipt, or bill.",
            "No controlled cache, service durability, device flush, or power-loss evidence.",
            "No authorized archive download or experimental payload read.",
            "No physical material sample, calibration, or property measurement.",
            "No measured lifecycle economics, candidate hardware performance, or capital authorization.",
            "No empirical SCM coupling, new physical law, quantum advantage, GPU replacement, or QPU execution."
        ]
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    artifact = build_artifact()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "cycle": artifact["cycle"], "lane_count": artifact["lane_count"], "status": artifact["status"], "focused_tests": artifact["test_runs"]["cycle010_focused"]["tests_run"], "full_suite_tests": artifact["test_runs"]["full_prototype_suite"]["tests_run"]}, sort_keys=True))


if __name__ == "__main__":
    main()
