#!/usr/bin/env python3
"""Run Batch-040 AI-COST-003 VQC reproduction and print/write JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.ai_training_vqc_reproduction import VQCReproductionConfig, run_reproduction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = run_reproduction(VQCReproductionConfig())
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
