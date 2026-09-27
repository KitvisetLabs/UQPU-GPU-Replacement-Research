"""Rebuild Cycle 003 Delta 01 review artifacts from frozen repository inputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from uqpu.cycle003_delta01 import build_cycle003_manifest, build_synthetic_cal001_fixture


ROOT = Path(__file__).resolve().parents[3]
FREEZE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
PROTOCOL = ROOT / "benchmarks/experiments/batch020-er6-mean-vs-cvar-real-qpu-protocol.json"
DEFAULT_CIRCUIT = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
DEFAULT_SCM = ROOT / "benchmarks/results/cycle003-delta01-scm-cal001-synthetic.json"


def _write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n"
    path.write_text(payload, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-commit", required=True, help="40-character commit that contains the generator")
    parser.add_argument("--circuit-output", type=Path, default=DEFAULT_CIRCUIT)
    parser.add_argument("--scm-output", type=Path, default=DEFAULT_SCM)
    args = parser.parse_args()

    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    circuit = build_cycle003_manifest(freeze, protocol)
    scm = build_synthetic_cal001_fixture(code_commit=args.code_commit)
    _write_json(args.circuit_output, circuit)
    _write_json(args.scm_output, scm)
    print(f"circuit_manifest={args.circuit_output}")
    print(f"scm_fixture={args.scm_output}")
    print(f"scm_dataset_bundle_sha256={scm['dataset_bundle_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
