"""Materialize the fail-closed real-QPU pilot preregistration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_qsvt_real_qpu_preregistration import build_preregistration


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = json.dumps(build_preregistration(), indent=2, sort_keys=True) + "\n"
    args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
