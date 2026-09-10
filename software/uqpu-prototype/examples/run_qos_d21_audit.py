#!/usr/bin/env python3
"""Emit the Batch-030 QOS D.21 composition/sensitivity certificate as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.qos_d21_audit import d20_downstream_inflation_certificate, d21_error_budget_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--dimension", type=int, default=2**20)
    parser.add_argument("--row-sparsity", type=int, default=1024)
    parser.add_argument("--epsilon", type=float, default=0.01)
    args = parser.parse_args()

    result = {
        "batch": 30,
        "qos_d21_error_budget": d21_error_budget_certificate(
            dimension=args.dimension,
            row_sparsity=args.row_sparsity,
            epsilon=args.epsilon,
        ),
        "qos_d20_downstream_sensitivity": d20_downstream_inflation_certificate(),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
