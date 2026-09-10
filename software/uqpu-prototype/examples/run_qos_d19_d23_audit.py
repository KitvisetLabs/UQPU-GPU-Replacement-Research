#!/usr/bin/env python3
"""Emit the Batch-032 QOS D.19 -> D.23 dependency certificate as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.qos_d19_d23_audit import (
    d19_shared_realization_certificate,
    d23_dependency_certificate,
    qos_machine_size_memory_translation_gate,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--bit-count", type=int, default=8)
    parser.add_argument("--epsilon", type=float, default=1.0e-3)
    args = parser.parse_args()

    result = {
        "batch": 32,
        "qos_d19_shared_realization": d19_shared_realization_certificate(
            bit_count=args.bit_count,
            target_epsilon=args.epsilon,
        ),
        "qos_d23_dependency": d23_dependency_certificate(),
        "qos_machine_size_memory_translation": qos_machine_size_memory_translation_gate(),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
