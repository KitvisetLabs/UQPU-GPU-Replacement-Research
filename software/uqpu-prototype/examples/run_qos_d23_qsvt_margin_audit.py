#!/usr/bin/env python3
"""Emit the Batch-033 QOS D.23 QSVT endpoint/margin certificate as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.qos_d23_qsvt_margin_audit import batch033_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--sparsity", type=int, default=4)
    args = parser.parse_args()

    result = {"batch": 33, "qos_d23_qsvt_margin": batch033_certificate(sparsity=args.sparsity)}
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
