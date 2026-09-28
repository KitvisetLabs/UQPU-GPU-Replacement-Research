#!/usr/bin/env python3
"""Run Cycle 011's frozen twelve-lane software/synthetic acceptance gates."""
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
ROOT = Path(__file__).resolve().parents[3]
FIXTURE_PATH = ROOT / "benchmarks/experiments/cycle011-delta01-preregistered-gates.json"
OUTPUT_PATH = ROOT / "benchmarks/results/cycle011-delta01-executable-acceptance.json"
TEST_IDS = {
    "A": "test_lane_a_fourth_weighted_graph_is_exact_capped_and_deterministic",
    "B": "test_lane_b_v2_migration_rejects_unknown_and_rebound_token",
    "C": "test_lane_c_atomic_publication_cleans_temp_and_preserves_old_or_new",
    "D": "test_lane_d_zip64_multi_entry_order_overlap_truncation_and_locator",
    "E": "test_lane_e_custody_chain_rejects_disconnection_and_superseded_method",
    "F": "test_lane_f_covariance_matrix_partial_non_psd_units_and_zero_outputs_fail_closed",
    "G": "test_lane_g_multimeasurand_budget_checks_scope_dimension_expiry_and_psd",
    "H": "test_lane_h_four_gate_grid_reports_held_out_rankings_without_capital",
    "FND/EQN": "test_lane_fnd_eqn_source_intervals_bind_exact_units_and_primary_docs",
    "SCM": "test_lane_scm_revocation_invalidates_replayed_and_later_transitions",
    "AI-COST": "test_lane_ai_cost_migration_binds_second_bytes_and_heldout_metrics",
    "QOS/QSVT": "test_lane_qos_qsvt_second_er6_source_migrates_append_only_certificate",
}


def file_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_tests() -> dict:
    inherited = os.environ.get("PYTHONPATH", "")
    os.environ["PYTHONPATH"] = os.pathsep.join([str(PROTOTYPE), inherited] if inherited else [str(PROTOTYPE)])
    results = {}
    for label, command in (
        ("cycle011_focused", [sys.executable, "-m", "unittest", "tests.test_cycle011_delta01", "-v"]),
        ("full_prototype_suite", [sys.executable, "-m", "unittest", "discover", "-s", "tests"]),
    ):
        proc = subprocess.run(command, cwd=PROTOTYPE, capture_output=True, text=True, timeout=420, check=False)
        output = proc.stdout + proc.stderr
        match = re.search(r"Ran (\d+) tests? in [^\n]+", output)
        if proc.returncode or not match:
            raise RuntimeError(f"{label} failed or had no unittest summary:\n{output[-6000:]}")
        if label == "cycle011_focused":
            missing = [test_id for test_id in TEST_IDS.values() if test_id not in output]
            if missing:
                raise RuntimeError("focused run omitted lane tests: " + ", ".join(missing))
        skip_match = re.search(r"skipped=(\d+)", output)
        results[label] = {"status": "PASS", "tests_run": int(match.group(1)),
                          "optional_skips": int(skip_match.group(1)) if skip_match else 0,
                          "command": command[1:]}
    return results


def build_ai_inputs(spec: dict, canonical_bytes, sha256_bytes, canonical_sha256):
    records1, records2 = {}, {}
    for split, record_ids in spec["splits"].items():
        records1[split] = [{"id": item, "source_version": 1, "input": f"synthetic-{item}"} for item in record_ids]
        records2[split] = [{"id": item, "source_version": 2, "input": f"synthetic-{item}"} for item in record_ids]
    required = spec["required_metrics"]
    def manifest(schema_version, records):
        payloads = {split: canonical_bytes(rows) for split, rows in records.items()}
        obj = {"schema_version": schema_version, "required_metrics": required, "splits": {}}
        for split, rows in records.items():
            obj["splits"][split] = {"record_ids": [row["id"] for row in rows],
                "source_sha256": sha256_bytes(payloads[split]), "source_bytes_length": len(payloads[split]),
                "metrics": {metric: {"complete": True, "value": 0.5} for metric in required}}
        return obj, payloads
    previous, previous_bytes = manifest(1, records1)
    current, current_bytes = manifest(2, records2)
    current["lineage_from"] = canonical_sha256(previous)
    return previous, current, previous_bytes, current_bytes


def build_artifact() -> dict:
    from uqpu.cycle010_delta01 import exact_maxcut, generate_maxcut_instance, _greedy_maxcut
    from uqpu.cycle011_delta01 import (
        atomic_publish, canonical_bytes, canonical_sha256, migrate_er6_certificate,
        migrate_request_v2_to_current, propagate_component_covariance,
        rank_four_gate_priority, run_atomic_protocol, run_weighted_maxcut,
        sha256_bytes, validate_ai_source_migration, validate_consent_revocation,
        validate_material_custody, validate_multimeasurand_budget,
        validate_sourced_interval, validate_zip64_directory,
    )
    spec = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    lanes = spec["lanes"]
    tests = run_tests()

    # A — fourth unweighted instance preserves deterministic restart prefixes;
    # a second weighted instance is exactly enumerated under the declared cap.
    a_spec = lanes["A"]
    graph = generate_maxcut_instance(a_spec["fourth_unweighted_seed"], a_spec["node_count"], a_spec["fourth_density"])
    exact = exact_maxcut(graph, a_spec["state_cap"])
    import random, time
    rng = random.Random(a_spec["fourth_unweighted_seed"] ^ 0xA511)
    starts, scores, elapsed = [], [], []
    for _ in range(max(a_spec["restart_budgets"])):
        start = tuple(rng.randrange(2) for _ in range(graph["node_count"]))
        starts.append(start)
        tick = time.perf_counter_ns()
        scores.append(_greedy_maxcut(start, graph["edges"])[1])
        elapsed.append(max(0, time.perf_counter_ns() - tick))
    fourth_rows = [{"restarts": n, "best_objective": max(scores[:n]), "exact_objective": exact["best_objective"],
        "gap_to_exact": exact["best_objective"] - max(scores[:n]), "restart_prefix_sha256": canonical_sha256(starts[:n]),
        "host_elapsed_ns": sum(elapsed[:n])} for n in a_spec["restart_budgets"]]
    a_weighted = run_weighted_maxcut(a_spec["weighted_seed"], a_spec["state_cap"], a_spec["restart_budgets"])
    a = {"fourth_unweighted": {"graph": graph, "graph_sha256": canonical_sha256(graph), "exact": exact, "results": fourth_rows},
         "weighted": a_weighted, "valid": exact["complete"] and a_weighted["complete"] and all(row["gap_to_exact"] >= 0 for row in fourth_rows + a_weighted["results"]),
         "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON"}

    # B — v2-to-v3 strict migration and canonical token/payload binding.
    b_req = lanes["B"]["request"]
    b_input = {"schema_version": 2, "idempotency_token": lanes["B"]["idempotency_token"],
               "source_commit": lanes["B"]["source_commit"], "request": b_req,
               "payload_sha256": canonical_sha256(b_req)}
    b_out = migrate_request_v2_to_current(b_input)
    b = {"output": b_out, "valid": b_out["schema_version"] == lanes["B"]["current_schema"],
         "network_submission": False, "evidence_class": "SYNTHETIC_SCHEMA_MIGRATION_GATE"}

    # C — old/new and same/fresh-process integrity plus fsync and cleanup outcomes.
    c = run_atomic_protocol()
    c["valid"] = c["hashes_match"] and c["temp_cleanup_pass"] and c["injected_failure"]["integrity_preserved"]

    # D — central-directory order/overlap/truncation and locator boundaries.
    d = validate_zip64_directory(lanes["D"])

    # E — custody, identity and current synthetic method version.
    e_spec = lanes["E"]
    e = validate_material_custody(e_spec["record"], expected_method_version=e_spec["expected_method_version"], as_of=date.fromisoformat(e_spec["as_of"]))

    # F — synthetic interval plus covariance block; unknown covariance remains null.
    f = propagate_component_covariance(lanes["F"])
    f["valid"] = f["complete"] and f["expanded_uncertainty"] is not None

    # G — scoped synthetic multi-measurand uncertainty budget.
    g_spec = lanes["G"]
    g = validate_multimeasurand_budget(g_spec["budget"], date.fromisoformat(g_spec["as_of"]))

    # H — assumed 4-gate grid and separate held-out assumption scenarios.
    h_spec = lanes["H"]
    h = rank_four_gate_priority(h_spec["gates"], h_spec["levels"], h_spec["held_out_scenarios"])
    h["valid"] = h["scenario_count"] == 6561 and len(h["held_out_scenarios"]) == len(h_spec["held_out_scenarios"])

    # FND/EQN — source hashes are read from the exact project source bytes.
    fn_spec = lanes["FND/EQN"]
    source_bytes, fnd_results = {}, []
    for locator in fn_spec["source_locators"]:
        path = locator.split("#", 1)[0]
        source_bytes[locator] = (ROOT / path).read_bytes()
    for quantity in fn_spec["quantities"]:
        locator = fn_spec["source_locators"][1 if quantity["unit_code"] == "J/count" else 0]
        declaration = {**quantity, "source_locator": locator, "source_sha256": sha256_bytes(source_bytes[locator])}
        fnd_results.append(validate_sourced_interval(declaration, source_bytes))
    fnd = {"quantities": fnd_results, "source_hashes": {key: sha256_bytes(value) for key, value in source_bytes.items()},
           "valid": all(row["valid"] for row in fnd_results), "evidence_class": "SOURCE_HASH_BOUND_TYPED_INTERVAL_DECLARATION"}

    # SCM — fictional five-volume consent-revocation transition model.
    scm = validate_consent_revocation(lanes["SCM"]["events"])
    scm["five_volume_link_coverage"] = ["V1", "V2", "V3", "V4", "V5"]

    # AI-COST — two immutable synthetic source versions; no candidate is scored.
    ai_spec = lanes["AI-COST"]
    ai_old, ai_new, ai_old_bytes, ai_new_bytes = build_ai_inputs(ai_spec, canonical_bytes, sha256_bytes, canonical_sha256)
    ai = validate_ai_source_migration(ai_old, ai_new, ai_old_bytes, ai_new_bytes)

    # QOS/QSVT — append-only second frozen ER6 source certificate.
    q_spec = lanes["QOS/QSVT"]
    q1 = q_spec["source_v1"]
    q2 = {"grammar": "ER6_CYCLE011_FROZEN_SUBSET", "source_id": q_spec["source_v2_id"],
          "qubit_count": 7, "bit_count": 7,
          "measurement_destinations": q1["measurement_destinations"] + [{"qubit": "q[6]", "bit": "c[6]"}],
          "candidate_resources": q_spec["candidate_resources"]}
    q_certificate = {"source_sha256": canonical_sha256(q1), "resources": q_spec["previous_resources"]}
    qos = migrate_er6_certificate(q1, q2, q_certificate, q_spec["resource_bounds"])

    outputs = {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g, "H": h,
               "FND/EQN": fnd, "SCM": scm, "AI-COST": ai, "QOS/QSVT": qos}
    pass_by_lane = {key: bool(row.get("valid")) for key, row in outputs.items()}
    if set(pass_by_lane) != set(TEST_IDS) or not all(pass_by_lane.values()):
        raise RuntimeError(f"one or more lane gates failed: {pass_by_lane}")
    lane_progress = {
        "A": "Fourth seeded unweighted graph and weighted exact-cap case with restart-prefix hashes and exact gaps.",
        "B": "Strict deterministic v2-to-v3 migration binds canonical request bytes, payload hash, token and source commit.",
        "C": "Same/fresh-process atomic writes capture file/directory fsync capability, old/new integrity and temporary cleanup; cache uncontrolled.",
        "D": "Three-entry ZIP64 central directory rejects order, overlap, truncation and locator-boundary mutations before payload acceptance.",
        "E": "Synthetic identity custody chain detects broken transfers, superseded methods and uncertainty-unit mismatch.",
        "F": "Three-component cost interval and covariance propagate only with complete units/matrix; null cases remain null.",
        "G": "Synthetic joint two-measurand covariance block checks scope, dimensions, PSD, method and expiry.",
        "H": "Four-gate assumed grid covers 6,561 scenarios and three held-out assumption cases; capital stays null.",
        "FND/EQN": "Exact USD/count and J/count interval declarations bind source locator, byte hash and dimension vectors.",
        "SCM": "Fiction-only transition model revokes consent and rejects replay/cross-sort transitions; empirical coupling null.",
        "AI-COST": "Second immutable synthetic source version validates hash-linked migration, split identity and held-out metric completeness before scoring.",
        "QOS/QSVT": "Second frozen ER6 source migrates an append-only measurement map with source hash and bounded resource certificate."
    }
    dependencies = {
        "A": "Broader preregistered workload set and comparable CPU/GPU baselines.",
        "B": "Provider authorization and one real request/receipt/bill reconciliation.",
        "C": "Controlled cache, process or power-loss test, device flush and service durability evidence.",
        "D": "Authorized bounded archive access and independent full-byte digest/payload validation.",
        "E": "Physical sample/control, traceable method/calibration and measured property uncertainty.",
        "F": "Source-backed lifecycle cost, accepted outputs and justified covariance model.",
        "G": "Current operational calibration evidence and measured scoped covariance inputs.",
        "H": "Sourced effort/impact distributions and an owner decision; no capital authorization here.",
        "FND/EQN": "Additional sourced quantities and an independent falsifiable validity test beyond units.",
        "SCM": "Fiction-only boundary; ethical review and preregistration required before any empirical path.",
        "AI-COST": "Immutable real-data lineage and independent held-out quality, energy and cost evaluation.",
        "QOS/QSVT": "Independent parser/SDK reconstruction, provider transpilation and authorized hardware evidence."
    }
    classes = {key: row.get("evidence_class", "BOUNDED_SYNTHETIC_OR_MODEL") for key, row in outputs.items()}
    lane_ledger = {key: {"status": "BLOCKED_WITH_PROGRESS", "acceptance": "PASS_LOCAL",
                         "acceptance_test_id": TEST_IDS[key], "progress": lane_progress[key],
                         "remaining_dependency": dependencies[key], "evidence_class": classes[key]} for key in TEST_IDS}
    source_files = [FIXTURE_PATH, Path(__file__), PROTOTYPE / "uqpu/cycle011_delta01.py",
                    PROTOTYPE / "tests/test_cycle011_delta01.py"]
    artifact = {
        "schema": "uqpu-cycle011-delta01-executable-acceptance-v1", "cycle": "011", "delta": "01", "date": spec["date"],
        "branch": "research/cycle-011-delta-01-2026-09-28", "base_closeout_commit": spec["base_closeout_commit"],
        "all_lane_acceptance_passed": True, "all_lane_external_gates_closed": False, "lane_count": 12,
        "lanes": lane_ledger, "results": outputs, "tests": tests,
        "provenance": {str(path.relative_to(ROOT)): file_sha(path) for path in source_files},
        "external_gates_remaining": list(dependencies.values()),
        "assumptions": [
            "A uses fixed seed 17 for the fourth unweighted n=8 graph and seed 23 for an n=8 graph with positive integer edge weights 1 through 5; exhaustive control is capped at 512 states.",
            "B/C/D/E/F/G/AI-COST/QOS inputs are synthetic and validate software/schema gates only; filesystem cache and storage durability are not controlled.",
            "H uses illustrative effort/impact multipliers; held-out scenarios are assumptions, not forecasts, and capital is unauthorized.",
            "FND/EQN checks source-bound exact dimensions and intervals, not physical truth or measured lifecycle values.",
            "SCM records fiction-only consent state; no empirical coupling or human study is represented.",
            "QOS/QSVT is a frozen semantic/resource certificate; no provider transpilation or hardware run occurred."
        ],
        "primary_source_basis": [
            {"evidence_class": "PROJECT_PRIMARY_SOURCE_DOCUMENT", "access_date": "2026-09-28", "url": "repo:docs/CYCLE008_TYPED_MATH_AND_SCM_STATE_CONTRACT_2026-09-28.md#1-typed-project-quantities", "scope": "Accepted-output quantity types and source locator used for exact interval dimension checks."},
            {"evidence_class": "PROJECT_PRIMARY_SOURCE_DOCUMENT", "access_date": "2026-09-28", "url": "repo:00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md#4-functional-equivalence-and-accepted-outputs", "scope": "Accepted-output denominators and cost/energy quantity definitions; no measured values are inferred."},
            {"evidence_class": "OFFICIAL_FORMAT_SPECIFICATION", "publication_date": "2022-11-01", "access_date": "2026-09-28", "version": "PKWARE APPNOTE 6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT", "scope": "ZIP64 record, locator and central-directory format vocabulary only; no archive was downloaded or read."}
        ],
        "uncertainty": [
            "A host elapsed time depends on this runtime; exact objective and restart identity are separate fields.",
            "F/G uncertainty values are synthetic covariance calculations and do not imply metrological coverage.",
            "H ranking stability is conditional on the declared assumed-input grid and held-out scenarios.",
            "C fsync capability is local filesystem metadata; it does not establish device flush, power-loss safety or service durability."
        ],
        "nonclaims": spec["evidence_boundary"],
        "next_cycle_handoff": "docs/SYNCHRONIZED_CYCLE_012_HANDOFF_2026-09-28.md",
        "status": "PASS_LOCAL_ALL_12_LANE_ACCEPTANCE_EXACT_SHA_CI_PENDING"
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(artifact, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
    return artifact


if __name__ == "__main__":
    result = build_artifact()
    print(json.dumps({"cycle": result["cycle"], "lane_count": result["lane_count"],
                      "all_lane_acceptance_passed": result["all_lane_acceptance_passed"],
                      "tests": result["tests"], "artifact": str(OUTPUT_PATH.relative_to(ROOT)),
                      "artifact_sha256": file_sha(OUTPUT_PATH)}, indent=2))
