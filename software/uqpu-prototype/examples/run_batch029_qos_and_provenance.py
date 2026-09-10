#!/usr/bin/env python3
"""Emit Batch-029 QOS D.20 and LLM-SRBench provenance certificates as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.external_benchmark_provenance import llm_srbench_public_count_certificate
from uqpu.qos_d20_audit import (
    d20_arithmetic_gap_certificate,
    d20_zero_sample_boundary_certificate,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = {
        "batch": 29,
        "qos_d20_zero_sample_boundary": d20_zero_sample_boundary_certificate(),
        "qos_d20_visible_arithmetic_gap": d20_arithmetic_gap_certificate(),
        "llm_srbench_public_count_reconciliation": llm_srbench_public_count_certificate(),
    }
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
