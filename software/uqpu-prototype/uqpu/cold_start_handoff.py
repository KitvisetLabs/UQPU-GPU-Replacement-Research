"""Fail-closed audit for an autonomous cold-start research handoff.

The audit checks repository discoverability and evidence-boundary metadata.  It
does not validate scientific claims, reproduce provider execution, or prove
that inaccessible branches/forks have been synchronized.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


EXPECTED_LANES = tuple("ABCDEFGHI")
EXPECTED_LANGUAGES = ("Thai", "English", "Chinese", "Japanese", "Korean", "German")
REQUIRED_PROGRAMS = (
    "FND-001..006", "EQN-001..006", "BIO-001", "FUS-001", "FIN-001",
)
VALID_EVIDENCE = {
    "CONCEPT", "THEORY", "MODEL_ONLY", "SIMULATION", "DEVICE_MODEL",
    "FABRICATION_PROPOSAL", "LAB_RESULT", "PUBLISHED_EXPERIMENT", "PROTOTYPE",
    "PRODUCTION_DATA", "ROADMAP", "DRY_RUN_ONLY", "RESOURCE_BLOCKED",
    "TOOL_BLOCKED", "DATA_BLOCKED", "CURRENTLY_INFEASIBLE",
    "SIMULATION_INDEPENDENT_SDK_CHECK",
    "SIMULATION_ALGEBRAIC_BLOCK_ENCODING_CONTRACT",
    "SIMULATION_PROVIDER_NEUTRAL_CIRCUIT_CONTRACT",
    "SIMULATION_PROVIDER_NEUTRAL_ONE_QUERY_CONTRACT",
    "SIMULATION_INDEPENDENT_SDK_ONE_QUERY_CHECK",
    "SIMULATION_PROVIDER_NEUTRAL_TWO_QUERY_CONTRACT",
    "SIMULATION_INDEPENDENT_SDK_TWO_QUERY_CHECK",
    "SIMULATION_INDEPENDENT_SDK_CIRCUIT_CHECK",
    "LITERATURE_ONLY",
}


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_commit_message(message: str, branch: str) -> list[str]:
    """Validate the repository's explicit source-to-main synchronization trailer."""
    expected = "Research-Sync: main" if branch == "main" else "Research-Sync: pending-main"
    return [] if expected in message.splitlines() else [f"missing_commit_trailer:{expected}"]


def audit_repository(repo_root: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    handoff_path = repo_root / "integration/COLD_START_HANDOFF_MANIFEST.json"
    lane_path = repo_root / "integration/eight_lane_manifest.json"

    for path in (handoff_path, lane_path):
        if not path.is_file():
            errors.append(f"missing_manifest:{path.relative_to(repo_root)}")
    if errors:
        return {"status": "HANDOFF_INCOMPLETE", "errors": errors, "warnings": warnings}

    handoff = _load_json(handoff_path)
    lanes = _load_json(lane_path)

    if handoff.get("canonical_branch") != "main":
        errors.append("canonical_branch_must_be_main")
    if handoff.get("priority_lane") != "A":
        errors.append("priority_lane_must_be_A")
    if tuple(sorted(handoff.get("lanes", {}))) != EXPECTED_LANES:
        errors.append("handoff_lanes_must_equal_A_through_I")
    if tuple(sorted(lanes.get("lanes", {}))) != EXPECTED_LANES:
        errors.append("integration_lanes_must_equal_A_through_I")

    expected_pairs = len(EXPECTED_LANES) * (len(EXPECTED_LANES) - 1) // 2
    if len(lanes.get("integration_review_pairs", [])) != expected_pairs:
        errors.append(f"integration_pair_count_must_be_{expected_pairs}")

    for lane, record in handoff.get("lanes", {}).items():
        for field in ("owner_path", "status", "evidence_class", "next_gate"):
            if not record.get(field):
                errors.append(f"lane_{lane}:{field}_missing")
        owner = record.get("owner_path")
        if owner and not (repo_root / owner).exists():
            errors.append(f"lane_{lane}:owner_path_missing")
        if record.get("evidence_class") not in VALID_EVIDENCE:
            errors.append(f"lane_{lane}:evidence_class_invalid")

    for relpath in handoff.get("required_reading", []):
        if not (repo_root / relpath).is_file():
            errors.append(f"required_reading_missing:{relpath}")

    languages = tuple(handoff.get("master_reference_languages", []))
    if languages != EXPECTED_LANGUAGES:
        errors.append("multilingual_reference_set_incomplete_or_reordered")
    programs = tuple(handoff.get("cross_cutting_programs", []))
    for program in REQUIRED_PROGRAMS:
        if program not in programs:
            errors.append(f"cross_cutting_program_missing:{program}")

    boundaries = handoff.get("evidence_boundaries", {})
    for forbidden in (
        "real_qpu_execution", "quantum_advantage", "gpu_replacement",
        "data_center_to_phone_achieved", "commercial_bio_oil",
        "commercial_fusion", "new_physical_law", "lane_i_vehicle_demonstrated",
    ):
        if boundaries.get(forbidden) is not False:
            errors.append(f"evidence_boundary_must_be_false:{forbidden}")

    agents = (repo_root / "AGENTS.md").read_text(encoding="utf-8").splitlines()[:10]
    if not any("00_AUTONOMOUS_RESEARCH_HANDOFF_FIRST_PRINCIPLE.md" in line for line in agents):
        errors.append("prime_directive_not_visible_at_agents_entry")

    if handoff.get("branch_fork_audit_scope") != "REGISTERED_AND_ACCESSIBLE_ONLY":
        errors.append("branch_fork_scope_must_fail_closed")
    if handoff.get("paid_execution_authorized") is not False:
        errors.append("paid_execution_must_remain_disabled")
    if handoff.get("hazardous_testing_authorized") is not False:
        errors.append("hazardous_testing_must_remain_disabled")

    if not handoff.get("latest_verified_ci", {}).get("url"):
        warnings.append("latest_verified_ci_url_missing")

    return {
        "schema": "uqpu-cold-start-audit-v1",
        "status": "READY_FOR_COLD_START" if not errors else "HANDOFF_INCOMPLETE",
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "lanes_checked": list(EXPECTED_LANES),
        "integration_pairs_checked": expected_pairs,
        "scientific_claim_validation": "OUT_OF_SCOPE",
        "inaccessible_branch_fork_coverage": "NOT_CLAIMED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository-root", type=Path, required=True)
    parser.add_argument("--branch")
    parser.add_argument("--commit-message-file", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    report = audit_repository(args.repository_root.resolve())
    if args.branch and args.commit_message_file:
        report["errors"].extend(validate_commit_message(
            args.commit_message_file.read_text(encoding="utf-8"), args.branch
        ))
        report["errors"] = sorted(set(report["errors"]))
        report["status"] = "READY_FOR_COLD_START" if not report["errors"] else "HANDOFF_INCOMPLETE"
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 0 if report["status"] == "READY_FOR_COLD_START" else 1


if __name__ == "__main__":
    raise SystemExit(main())
