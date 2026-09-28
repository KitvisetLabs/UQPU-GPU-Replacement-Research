"""Record bounded Cycle 007 local A-lane and fresh-process C-lane controls."""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path

from uqpu.cycle005_delta01 import benchmark_scale_case
from uqpu.cycle006_delta01 import summarize_scale_repetitions
from uqpu.cycle007_delta01 import measure_fresh_process_durability


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "benchmarks/results/cycle007-delta01-local-reproducibility.json"


def capture() -> dict:
    workload_fixtures = []
    for fixture_id, node_count, seed in (
        ("seeded-maxcut-8", 8, 7101),
        ("seeded-maxcut-9", 9, 7102),
    ):
        rows = [
            benchmark_scale_case(
                node_count,
                seed,
                max_states=1 << node_count,
                deadline_seconds=10,
                heuristic_restarts=64,
            )
            for _ in range(3)
        ]
        summary = summarize_scale_repetitions(rows)
        summary["fixture_id"] = fixture_id
        summary["evidence_boundary"] = (
            "Generated local CPU fixture. Exact completion applies only to this finite case; "
            "64-restart greedy objective is reported separately."
        )
        workload_fixtures.append(summary)

    storage = measure_fresh_process_durability(
        {"cycle": "007", "fixture": "fresh-process-readback"},
        repetitions=3,
    )
    return {
        "schema": "uqpu-cycle007-delta01-local-reproducibility-v1",
        "cycle": "007",
        "delta": "01",
        "access_date_utc": datetime.now(timezone.utc).date().isoformat(),
        "lane_a": {
            "fixtures": workload_fixtures,
            "evidence_class": "SEEDED_LOCAL_CLASSICAL_SOFTWARE_SCREEN_NOT_COMPETITIVE_BENCHMARK",
        },
        "lane_c": storage,
        "cross_references": {
            "lane_d_primary_source_range": "benchmarks/evidence/cycle007-delta01-zenodo-range-verification.json",
            "fnd_eqn_dimension_audit": "benchmarks/results/cycle007-delta01-umrl-dimension-audit.json",
            "synchronized_12_lane_ledger": "benchmarks/results/cycle007-delta01-synchronized-lane-ledger.json",
        },
        "nonclaims": [
            "No GPU or QPU comparison, advantage, energy measurement, or scaling law is established.",
            "No cache-state label is inferred; cache control was not attempted.",
            "Local fsync/readback is not device-flush or power-loss evidence.",
        ],
    }


def main() -> int:
    result = capture()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "A_fixtures": len(result["lane_a"]["fixtures"]),
        "A_exact_complete": [row["exact"]["complete"] for row in result["lane_a"]["fixtures"]],
        "A_restarts": [row["heuristic"]["restarts"] for row in result["lane_a"]["fixtures"]],
        "C_fresh_process_repetitions": result["lane_c"]["repetitions"],
        "C_cache_control_attempted": result["lane_c"]["platform_capabilities"]["cache_control_attempted"],
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
