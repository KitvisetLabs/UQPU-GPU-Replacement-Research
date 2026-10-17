#!/usr/bin/env python3
"""Emit the immutable ER6 next-boundary preregistration."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.er6_qsvt_next_boundary_preregistration import build_preregistration


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = build_preregistration()
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
