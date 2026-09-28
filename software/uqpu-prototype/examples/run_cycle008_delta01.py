#!/usr/bin/env python3
"""Run the bounded local Cycle 008 comparison and fresh-process I/O probes."""
from __future__ import annotations

import argparse
from datetime import date
import json
import os
from pathlib import Path
import re
import subprocess
import sys

PROTOTYPE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROTOTYPE))

from uqpu.cycle007_delta01 import measure_fresh_process_durability
from uqpu.cycle008_delta01 import compare_deterministic_solver_restarts


ROOT = Path(__file__).resolve().parents[3]
DEFAULT_OUTPUT = ROOT / "benchmarks/results/cycle008-delta01-executable-acceptance.json"

LANE_ACCEPTANCE = {
    "A": {"evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON", "test": "test_lane_a_restart_sensitivity_keeps_exact_completion_separate"},
    "B": {"evidence_class": "SYNTHETIC_HASH_LINKED_REQUEST_RECEIPT_GATE", "test": "test_lane_b_hash_link_and_idempotency_mutation_fail_closed"},
    "C": {"evidence_class": "FRESH_PROCESS_LOCAL_FILESYSTEM_SCREEN_CACHE_UNCONTROLLED", "test": "test_lane_c_process_scope_does_not_imply_cache_or_durability"},
    "D": {"evidence_class": "RESOURCE_GUARDED_ARCHIVE_PLAN_NO_DOWNLOAD", "test": "test_lane_d_archive_plan_enforces_resource_cap_and_never_downloads"},
    "E": {"evidence_class": "SYNTHETIC_FUNCTION_SPECIFIC_MATERIAL_RECORD", "test": "test_lane_e_material_record_requires_unit_matched_uncertainty"},
    "F": {"evidence_class": "SYNTHETIC_COST_INTERVAL_SCHEMA", "test": "test_lane_f_cost_interval_requires_common_currency_and_outputs"},
    "G": {"evidence_class": "SYNTHETIC_CALIBRATION_UNCERTAINTY_GATE", "test": "test_lane_g_calibration_gate_checks_scope_expiry_and_uncertainty"},
    "H": {"evidence_class": "ILLUSTRATIVE_SENSITIVITY_RANKING_NO_CAPITAL", "test": "test_lane_h_gate_ranking_is_assumption_bound_and_never_authorizes"},
    "FND/EQN": {"evidence_class": "EXACT_RATIONAL_DIMENSION_COUNTEREXAMPLE_GATE", "test": "test_lane_fnd_eqn_accepts_exact_homogeneous_units_and_keeps_counterexample"},
    "SCM": {"evidence_class": "FICTIONAL_FIVE_VOLUME_INVARIANT_TEST", "test": "test_lane_scm_five_volume_fixture_is_typed_and_real_null"},
    "AI-COST": {"evidence_class": "SYNTHETIC_CANDIDATE_EVALUATION_REJECTION_GATE", "test": "test_lane_ai_cost_rejects_split_leakage_and_incomplete_candidate_evidence"},
    "QOS/QSVT": {"evidence_class": "FROZEN_ER6_SEMANTIC_CERTIFICATE_SCHEMA", "test": "test_lane_qos_semantics_certificate_rejects_changed_measurement_map"},
}


def build_artifact() -> dict:
    inherited_pythonpath = os.environ.get("PYTHONPATH", "")
    pythonpath_parts = [str(PROTOTYPE)]
    if inherited_pythonpath:
        pythonpath_parts.append(inherited_pythonpath)
    os.environ["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
    test_records = {}
    for name, args in (
        ("cycle008_focused", [sys.executable, "-m", "unittest", "tests.test_cycle008_delta01", "-v"]),
        ("full_prototype_suite", [sys.executable, "-m", "unittest", "discover", "-s", "tests"]),
    ):
        completed = subprocess.run(
            args, cwd=PROTOTYPE, capture_output=True, text=True, timeout=300, check=False
        )
        output = completed.stdout + completed.stderr
        summary = re.search(r"Ran (\d+) tests? in [^\n]+", output)
        if completed.returncode != 0 or summary is None:
            raise RuntimeError(f"{name} did not pass:\n{output[-4000:]}")
        skipped = re.search(r"skipped=(\d+)", output)
        test_records[name] = {
            "status": "PASS",
            "tests_run": int(summary.group(1)),
            "optional_skips": int(skipped.group(1)) if skipped else 0,
            "command": args[1:],
        }
        if name == "cycle008_focused":
            missing_lane_tests = [
                row["test"] for row in LANE_ACCEPTANCE.values()
                if row["test"] not in output
            ]
            if missing_lane_tests:
                raise RuntimeError(
                    "focused test run did not report every lane acceptance: "
                    + ", ".join(missing_lane_tests)
                )
    lane_a = {
        "schema": "uqpu-cycle008-two-fixture-restart-comparison-v1",
        "evidence_class": "LOCAL_SEEDED_CLASSICAL_SOFTWARE_COMPARISON",
        "fixtures": [
            compare_deterministic_solver_restarts(node_count=12, seed=80812),
            compare_deterministic_solver_restarts(node_count=12, seed=80813),
        ],
        "nonclaims": [
            "Two generated finite fixtures do not establish a competitive benchmark suite.",
            "Restart sensitivity does not establish an asymptotic scaling law.",
            "No GPU, QPU, energy, provider, or hardware comparison is made.",
        ],
    }
    lane_c = measure_fresh_process_durability(
        {"cycle": "008", "payload": "synthetic reproducibility fixture"}, repetitions=3
    )
    return {
        "schema": "uqpu-cycle008-delta01-executable-acceptance-v1",
        "reviewed_date": date.today().isoformat(),
        "cycle": "008",
        "delta": "01",
        "lanes": {
            name: {
                **entry,
                "acceptance_status": "PASS",
                "lane_status": "BLOCKED_WITH_PROGRESS",
                "test_status": "PASS_IN_FOCUSED_RUN",
            }
            for name, entry in LANE_ACCEPTANCE.items()
        },
        "test_runs": test_records,
        "lane_a_solver_comparison": lane_a,
        "lane_c_fresh_process_probe": lane_c,
        "source_basis": [
            {
                "url": "https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html",
                "access_date": "2026-09-28",
                "evidence_class": "OFFICIAL_PROVIDER_API_DOCUMENTATION",
                "informs": "request shape and required field names only; no submitted job or receipt",
            },
            {
                "url": "https://www.nist.gov/pml/nist-technical-note-1297/nist-guidelines-evaluating-and-expressing-uncertainty-nist-measurement",
                "access_date": "2026-09-28",
                "evidence_class": "PRIMARY_METROLOGY_GUIDANCE",
                "informs": "uncertainty reporting and coverage factor context; no material property was measured",
            },
            {
                "url": "https://openqasm.com/versions/3.1/language/insts.html",
                "access_date": "2026-09-28",
                "evidence_class": "LANGUAGE_SPECIFICATION",
                "informs": "narrow measurement-map semantics; no provider or hardware execution",
            },
        ],
        "assumptions": [
            "Illustrative gate scores and all positive material/cost/custody records are synthetic fixtures.",
            "Cycle 007 Zenodo source artifact remains bounded-range metadata/README evidence; this cycle does not fetch the archive payload.",
            "The local solver and file-system probes describe only this execution environment and fixtures.",
        ],
        "uncertainty": [
            "Two fixed-seed finite solver fixtures; runtime varies by host and process load.",
            "Fresh processes do not imply cold cache; cache state is UNCONTROLLED.",
            "Synthetic schema acceptance does not establish physical, provider, or economic validity.",
        ],
        "nonclaims": [
            "No QPU/provider task, bill, paid job, or hardware measurement.",
            "No material measurement, fabrication, funding, or capital authorization.",
            "No new physical law, quantum advantage, GPU replacement, or empirical spiritual communication.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    artifact = build_artifact()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "lane_count": len(artifact["lanes"]), "evidence_class": "LOCAL_SOFTWARE_AND_SYNTHETIC_GATES"}, sort_keys=True))


if __name__ == "__main__":
    main()
