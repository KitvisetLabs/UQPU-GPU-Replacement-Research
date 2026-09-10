#!/usr/bin/env python3
"""Emit the Batch-028 scoped QOS D.16 adversarial certificate as JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.qos_adversarial_audit import d16_repeated_pair_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = d16_repeated_pair_certificate()
    text = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
