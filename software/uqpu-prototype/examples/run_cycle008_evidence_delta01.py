#!/usr/bin/env python3
"""Run Cycle 008 local screens and the executable lane-evidence test suites."""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import subprocess
import sys

PROTOTYPE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROTOTYPE))

from uqpu.cycle007_delta01 import measure_fresh_process_durability
from uqpu.cycle008_evidence_delta01 import compare_deterministic_solver_restarts


TESTS = {
    "A": "test_lane_a_exact_control_and_restart_sensitivity_are_separate",
    "B": "test_lane_b_hash_link_and_replay_mutation_fail_closed",
    "C": "test_lane_c_fresh_process_is_not_mislabeled_cold_or_durable",
    "D": "test_lane_d_full_archive_plan_respects_byte_cap",
    "E": "test_lane_e_property_record_rejects_uncertainty_unit_mismatch",
    "F": "test_lane_f_cost_intervals_fail_closed_on_currency_mix",
    "G": "test_lane_g_calibration_certificate_expiry_and_uncertainty_are_required",
    "H": "test_lane_h_ranking_is_sensitivity_bound_and_not_authorization",
    "FND/EQN": "test_registry_subset_has_exact_equation_dimensions",
    "SCM": "test_five_volumes_each_require_their_invariant_and_firewall",
    "AI-COST": "test_lane_ai_cost_rejects_leakage_and_incomplete_evidence",
    "QOS/QSVT": "test_lane_qos_semantics_certificate_rejects_map_change",
}


def _run_tests(command: list[str], name: str) -> dict:
    result = subprocess.run(command, cwd=PROTOTYPE, text=True, capture_output=True, timeout=300, check=False)
    output = result.stdout + result.stderr
    match = re.search(r"Ran (\d+) tests? in [^\n]+", output)
    if result.returncode or not match:
        raise RuntimeError(f"{name} failed:\n{output[-4000:]}")
    skipped = re.search(r"skipped=(\d+)", output)
    return {"name": name, "status": "PASS", "tests_run": int(match.group(1)),
            "optional_skips": int(skipped.group(1)) if skipped else 0,
            "command": command[1:]}


def build_artifact() -> dict:
    focused = _run_tests([sys.executable, "-m", "unittest", "tests.test_cycle008_evidence_delta01"], "Cycle 008 ten-lane focused suite")
    math_run = subprocess.run([sys.executable, "examples/run_cycle008_math_audit.py"], cwd=PROTOTYPE,
                              capture_output=True, text=True, timeout=120, check=False)
    if math_run.returncode:
        raise RuntimeError(f"typed-math/SCM audit failed:\n{math_run.stdout}\n{math_run.stderr}")
    math_tests = _run_tests([sys.executable, "-m", "unittest", "tests.test_cycle008_delta01"], "Cycle 008 typed-math/SCM suite")
    full = _run_tests([sys.executable, "-m", "unittest", "discover", "-s", "tests"], "full prototype suite")
    lane_a = compare_deterministic_solver_restarts()
    lane_c = measure_fresh_process_durability({"cycle": "008", "fixture": "synthetic"}, repetitions=3)
    math_artifact = json.loads((ROOT / "benchmarks/results/cycle008-delta01-typed-math-scm-audit.json").read_text(encoding="utf-8"))
    return {
        "schema": "uqpu-cycle008-executable-evidence-v1",
        "cycle": "008", "delta": "01", "review_date": date.today().isoformat(),
        "test_runs": {"focused": focused, "typed_math_scm": math_tests, "full": full},
        "lanes": {lane: {"test": test, "status": "PASS", "lane_status": "BLOCKED_WITH_PROGRESS"} for lane, test in TESTS.items()},
        "typed_math_scm_audit": {
            "artifact": "benchmarks/results/cycle008-delta01-typed-math-scm-audit.json",
            "status": math_artifact["status"],
            "dimension_equations_checked": math_artifact["dimension_equation_count"],
            "scm_equations_added": math_artifact["scm_equation_extensions"]["equation_ids"],
            "five_volume_contract_valid": math_artifact["five_volume_contract"]["valid"],
            "unvalidated_fiction_to_real_cast_rejected": math_artifact["fiction_to_real_cast"]["unvalidated_cast_rejected"],
        },
        "lane_a_solver_comparison": lane_a,
        "lane_c_fresh_process_probe": lane_c,
        "primary_sources": [
            {"url": "https://docs.aws.amazon.com/braket/latest/APIReference/API_CreateQuantumTask.html", "access_date": "2026-09-28", "supports": "required clientToken field and task ARN response schema only; no claim of provider-side idempotency"},
            {"url": "https://www.nist.gov/pml/nist-technical-note-1297/nist-guidelines-evaluating-and-expressing-uncertainty-nist-measurement", "access_date": "2026-09-28", "supports": "uncertainty record fields; no uncertainty propagation computed"},
            {"url": "https://openqasm.com/versions/3.1/language/insts.html", "access_date": "2026-09-28", "supports": "measurement-to-bit mapping scope only; not general semantic proof"},
        ],
        "assumptions": ["Positive material, calibration, cost and gate-ranking records in tests are synthetic.", "Mixed-currency conversion is intentionally unsupported and fails closed.", "Solver fixture is generated and local; host runtime is environment-dependent."],
        "uncertainty": ["One generated n=12 solver fixture does not estimate scaling uncertainty.", "Filesystem cache state is uncontrolled despite fresh child processes.", "Illustrative capital ranking assumptions have no empirical probability distributions."],
        "nonclaims": ["No provider task, bill, payment, paid job, or hardware measurement.", "No full archive hash or experimental payload analysis.", "No material result, funding, fabrication, human study, new physical law, advantage, GPU replacement, or empirical SCM result."],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "benchmarks/results/cycle008-delta01-executable-evidence.json")
    args = parser.parse_args()
    artifact = build_artifact()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(artifact, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(args.output), "focused_tests": artifact["test_runs"]["focused"]["tests_run"], "typed_math_scm_tests": artifact["test_runs"]["typed_math_scm"]["tests_run"], "full_tests": artifact["test_runs"]["full"]["tests_run"], "optional_skips": artifact["test_runs"]["full"]["optional_skips"]}, sort_keys=True))


if __name__ == "__main__":
    main()
