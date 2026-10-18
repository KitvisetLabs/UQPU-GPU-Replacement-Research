"""Run QOS-AUDIT-010B21/22 and persist both pass and failure evidence."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_qsvt_independent_routed_probe import reproduce_with_qulacs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = reproduce_with_qulacs()
    except Exception as exc:
        result = {
            "schema": "uqpu-er6-qsvt-independent-routed-probe-v1",
            "work_id": "QOS-AUDIT-010B22",
            "evidence_class": "NEGATIVE_REPRODUCIBILITY_RESULT",
            "passed": False,
            "failure": {"type": type(exc).__name__, "message": str(exc)},
            "authorization": {
                "credentials_used": False,
                "live_service_initialized": False,
                "network_submission_attempted": False,
                "provider_jobs": 0,
                "shots": 0,
                "paid_execution_authorized": False,
            },
        }
    payload = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0 if result.get("passed") is True else 1


if __name__ == "__main__":
    raise SystemExit(main())
