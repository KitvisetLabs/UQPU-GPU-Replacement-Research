#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from uqpu.er6_lcu_qsvt_one_query import dumps_reproduction


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = dumps_reproduction() + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
