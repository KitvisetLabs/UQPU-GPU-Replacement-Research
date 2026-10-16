"""Emit the QOS-AUDIT-010B5 pinned-Qiskit reproduction certificate."""
from __future__ import annotations

import argparse
from pathlib import Path

from uqpu.qos_d23_qsvt_qiskit_reproduction import dumps_reproduction


parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path)
args = parser.parse_args()
payload = dumps_reproduction() + "\n"
if args.output:
    args.output.write_text(payload, encoding="utf-8")
print(payload, end="")
