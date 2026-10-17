"""Run the immutable ten-query ER6 QSVT boundary experiment."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_qsvt_ten_query import reproduce_with_qiskit


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = reproduce_with_qiskit()
    payload = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
