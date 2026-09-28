"""Generate Cycle 004 Delta 01 measurement and synthetic handoff artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from uqpu.cycle004_delta01 import build_cycle004_packet, build_scm_two_party_handoff


ROOT = Path(__file__).resolve().parents[3]
FREEZE = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
CYCLE003 = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
CYCLE003_SCM = ROOT / "benchmarks/results/cycle003-delta01-scm-cal001-synthetic.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
DEFAULT_PACKET = ROOT / "benchmarks/results/cycle004-delta01-er6-classical-io-and-gates.json"
DEFAULT_PUBLIC = ROOT / "benchmarks/experiments/cycle004-delta01-scm-cal001-public-handoff.json"
DEFAULT_TRUTH = ROOT / "benchmarks/results/cycle004-delta01-scm-cal001-custodian-truth.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--repetitions", type=int, default=101)
    parser.add_argument("--packet-output", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--public-output", type=Path, default=DEFAULT_PUBLIC)
    parser.add_argument("--truth-output", type=Path, default=DEFAULT_TRUTH)
    args = parser.parse_args()

    ai_raw = AI_BASELINE.read_bytes()
    packet = build_cycle004_packet(
        _read(FREEZE),
        _read(CYCLE003),
        json.loads(ai_raw),
        hashlib.sha256(ai_raw).hexdigest(),
        repetitions=args.repetitions,
        code_commit=args.code_commit,
    )
    public, truth = build_scm_two_party_handoff(
        _read(CYCLE003_SCM),
        salt="cycle004-synthetic-custodian-demo-v1",
    )
    _write(args.packet_output, packet)
    _write(args.public_output, public)
    _write(args.truth_output, truth)
    print(f"packet={args.packet_output}")
    print(f"scm_public={args.public_output}")
    print(f"scm_custodian_truth={args.truth_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
