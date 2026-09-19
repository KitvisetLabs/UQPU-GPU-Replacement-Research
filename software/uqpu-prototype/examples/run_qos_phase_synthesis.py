from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.qos_d23_phase_synthesis_contract import coefficient_fingerprint, synthesize_with_pinned_qsppack


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = synthesize_with_pinned_qsppack()
    result["runtime_coefficient_fingerprint"] = coefficient_fingerprint()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    # Preserve solver failure as a research result; fail only contract integrity.
    if not result["contract"]["coefficient_fingerprint"] == result["runtime_coefficient_fingerprint"]:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
