"""Generate Cycle 005 Delta 01 measurement and gate artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

from uqpu.cycle005_delta01 import benchmark_scale_case, build_cycle005_packet


ROOT = Path(__file__).resolve().parents[3]
PROTOTYPE = ROOT / "software/uqpu-prototype"
MANIFEST = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
CYCLE004_PACKET = ROOT / "benchmarks/results/cycle004-delta01-er6-classical-io-and-gates.json"
CYCLE004_PUBLIC = ROOT / "benchmarks/experiments/cycle004-delta01-scm-cal001-public-handoff.json"
CYCLE004_TRUTH = ROOT / "benchmarks/results/cycle004-delta01-scm-cal001-custodian-truth.json"
PERSISTED_QISKIT = ROOT / "benchmarks/results/cycle005-delta01-cycle004-qiskit-ci-parse.json"
DEFAULT_PACKET = ROOT / "benchmarks/results/cycle005-delta01-integrated-gates.json"
DEFAULT_SCM = ROOT / "benchmarks/results/cycle005-delta01-scm-cal001-synthetic-rehearsal.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n",
        encoding="utf-8",
    )


def _fresh_process_scale_cases(deadline_seconds: float) -> list[dict]:
    rows = []
    for node_count, seed in ((6, 42), (10, 43), (14, 44)):
        command = [
            sys.executable,
            str(Path(__file__).resolve()),
            "--scale-worker",
            "--node-count",
            str(node_count),
            "--seed",
            str(seed),
            "--deadline-seconds",
            str(deadline_seconds),
        ]
        environment = dict(os.environ)
        environment["PYTHONPATH"] = str(PROTOTYPE)
        completed = subprocess.run(
            command,
            cwd=PROTOTYPE,
            env=environment,
            check=True,
            capture_output=True,
            text=True,
        )
        rows.append(json.loads(completed.stdout))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-commit")
    parser.add_argument("--io-repetitions", type=int, default=21)
    parser.add_argument("--deadline-seconds", type=float, default=30.0)
    parser.add_argument("--packet-output", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--scm-output", type=Path, default=DEFAULT_SCM)
    parser.add_argument("--scale-worker", action="store_true")
    parser.add_argument("--node-count", type=int)
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    if args.scale_worker:
        if args.node_count is None or args.seed is None:
            parser.error("--scale-worker requires --node-count and --seed")
        row = benchmark_scale_case(
            args.node_count,
            args.seed,
            deadline_seconds=args.deadline_seconds,
        )
        print(json.dumps(row, sort_keys=True, allow_nan=False))
        return 0

    if not args.code_commit:
        parser.error("--code-commit is required outside worker mode")
    manifest_raw = MANIFEST.read_bytes()
    ai_raw = AI_BASELINE.read_bytes()
    cycle004 = _read(CYCLE004_PACKET)
    packet = build_cycle005_packet(
        manifest=json.loads(manifest_raw),
        manifest_file_sha256=hashlib.sha256(manifest_raw).hexdigest(),
        batch039=json.loads(ai_raw),
        batch039_sha256=hashlib.sha256(ai_raw).hexdigest(),
        cycle004_cost_ledger=cycle004["lanes"]["F"],
        public_scm=_read(CYCLE004_PUBLIC),
        custodian_scm=_read(CYCLE004_TRUTH),
        public_scm_sha256=_sha(CYCLE004_PUBLIC),
        custodian_scm_sha256=_sha(CYCLE004_TRUTH),
        persisted_qiskit=_read(PERSISTED_QISKIT),
        scale_cases=_fresh_process_scale_cases(args.deadline_seconds),
        io_repetitions=args.io_repetitions,
        code_commit=args.code_commit,
    )
    _write(args.packet_output, packet)
    _write(args.scm_output, packet["lanes"]["SCM"])
    print(f"packet={args.packet_output}")
    print(f"scm_rehearsal={args.scm_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
