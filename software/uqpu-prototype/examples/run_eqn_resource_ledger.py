#!/usr/bin/env python3
"""Validate EQN-002C resource ledgers from a JSON list of method records."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.eqn_resource_ledger import METHOD_ARMS, REQUIRED_LEDGER_FIELDS, resource_parity_summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path)
    args = parser.parse_args()

    if args.input is None:
        result = {
            "protocol": "EQN-002C-3",
            "method_arms": list(METHOD_ARMS),
            "required_ledger_fields": list(REQUIRED_LEDGER_FIELDS),
            "note": "Provide a JSON list of completed method records to evaluate candidate-budget and resource-ledger readiness.",
        }
    else:
        records = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(records, list):
            raise ValueError("input JSON must contain a list of method records")
        result = resource_parity_summary(records)

    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
