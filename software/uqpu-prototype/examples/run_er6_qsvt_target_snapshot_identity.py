"""Fingerprint the pinned saved target snapshot without provider submission."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_qsvt_target_snapshot_identity import reproduce_target_identity


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = reproduce_target_identity()
    payload = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
