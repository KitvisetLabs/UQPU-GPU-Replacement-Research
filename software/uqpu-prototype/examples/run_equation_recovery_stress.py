#!/usr/bin/env python3
"""Run the deterministic RG-031 noisy equation-recovery stress suite."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.equation_recovery_stress import run_stress_suite


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=256)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run_stress_suite(seed_count=args.seeds)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
