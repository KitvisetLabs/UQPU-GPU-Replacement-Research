#!/usr/bin/env python3
"""Run the pinned-Qiskit ER6 three/five-query bounded-prefix gate."""

import argparse
from pathlib import Path

from uqpu.er6_lcu_qsvt_bounded_prefix import dumps_reproduction


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = dumps_reproduction()
    if args.output:
        args.output.write_text(payload + "\n", encoding="utf-8")
    print(payload)


if __name__ == "__main__":
    main()
