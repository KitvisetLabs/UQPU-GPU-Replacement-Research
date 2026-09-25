from __future__ import annotations

import argparse
import json
import platform
import sys
import time
from pathlib import Path

from uqpu.qos_d23_phase_reconstruction_v040 import synthesize_with_pinned_qsppack_v040


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    started = time.perf_counter()
    result = synthesize_with_pinned_qsppack_v040()
    result["execution_provenance"] = {
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "machine": platform.machine(),
        "wall_seconds": time.perf_counter() - started,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
