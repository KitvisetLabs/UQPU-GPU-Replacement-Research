#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_lcu_qsvt_two_query import reproduce_with_qiskit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = reproduce_with_qiskit()
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
