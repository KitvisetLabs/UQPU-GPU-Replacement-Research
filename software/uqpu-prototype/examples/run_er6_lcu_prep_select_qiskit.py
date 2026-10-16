"""Emit the QOS-AUDIT-010B7 pinned-Qiskit PREP/SELECT certificate."""
from __future__ import annotations

import argparse
from pathlib import Path

from uqpu.er6_lcu_prep_select_qiskit import dumps_reproduction


parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path)
args = parser.parse_args()
payload = dumps_reproduction() + "\n"
if args.output:
    args.output.write_text(payload, encoding="utf-8")
print(payload, end="")
