"""Generate Cycle 006 Delta 01 measurements and integrated gate artifacts."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

from uqpu.cycle006_delta01 import (
    benchmark_directory_durable_io,
    benchmark_scale_case,
    build_cycle006_packet,
    build_zenodo_range_evidence,
    summarize_scale_repetitions,
)


ROOT = Path(__file__).resolve().parents[3]
PROTOTYPE = ROOT / "software/uqpu-prototype"
MANIFEST = ROOT / "benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json"
AI_BASELINE = ROOT / "benchmarks/results/batch039-ai-cost-002-classical-baseline.json"
AI_GENERATOR = PROTOTYPE / "uqpu/ai_training_baseline.py"
CYCLE005_PACKET = ROOT / "benchmarks/results/cycle005-delta01-integrated-gates.json"
SOURCE_OBSERVATIONS = ROOT / "benchmarks/evidence/cycle006-delta01-zenodo-http-observations.json"
DEFAULT_SOURCE = ROOT / "benchmarks/evidence/cycle006-delta01-zenodo-range-metadata.json"
DEFAULT_PACKET = ROOT / "benchmarks/results/cycle006-delta01-integrated-gates.json"
DEFAULT_SCORER = ROOT / "benchmarks/experiments/cycle006-delta01-scm-scorer-package.json"
DEFAULT_CUSTODIAN = ROOT / "benchmarks/results/cycle006-delta01-scm-custodian-package.json"
DEFAULT_REVEAL_AUDIT = ROOT / "benchmarks/results/cycle006-delta01-scm-reveal-audit.json"


def _read(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False)
        + "\n",
        encoding="utf-8",
    )


def _worker_environment() -> dict[str, str]:
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(PROTOTYPE)
    return environment


def _run_json_worker(arguments: list[str]) -> dict:
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), *arguments],
        cwd=PROTOTYPE,
        env=_worker_environment(),
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def _fresh_process_scale_summary(
    node_count: int,
    seed: int,
    *,
    max_states: int,
    deadline_seconds: float,
    repetitions: int,
) -> dict:
    rows = []
    for _ in range(repetitions):
        rows.append(
            _run_json_worker(
                [
                    "--scale-worker",
                    "--node-count",
                    str(node_count),
                    "--seed",
                    str(seed),
                    "--max-states",
                    str(max_states),
                    "--deadline-seconds",
                    str(deadline_seconds),
                ]
            )
        )
    return summarize_scale_repetitions(rows)


def _capture_source(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    required = {
        "--api-json": args.api_json,
        "--tail": args.tail,
        "--tail-start": args.tail_start,
        "--readme-range": args.readme_range,
        "--readme-start": args.readme_start,
        "--code-commit": args.code_commit,
    }
    missing = [name for name, value in required.items() if value is None]
    if missing:
        parser.error("--capture-source requires " + ", ".join(missing))
    api_bytes = args.api_json.read_bytes()
    observations = _read(SOURCE_OBSERVATIONS)
    if hashlib.sha256(api_bytes).hexdigest() != observations["api_response_sha256"]:
        raise ValueError("Zenodo API response hash does not match the observation record")
    result = build_zenodo_range_evidence(
        json.loads(api_bytes),
        args.tail.read_bytes(),
        tail_range_start=args.tail_start,
        readme_range_bytes=args.readme_range.read_bytes(),
        readme_range_start=args.readme_start,
        http_observations=observations,
        capture_code_commit=args.code_commit,
    )
    _write(args.source_output, result)
    print(f"source_evidence={args.source_output}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--code-commit")
    parser.add_argument("--deadline-seconds", type=float, default=60.0)
    parser.add_argument("--scale-repetitions", type=int, default=3)
    parser.add_argument("--io-repetitions", type=int, default=11)
    parser.add_argument("--packet-output", type=Path, default=DEFAULT_PACKET)
    parser.add_argument("--scorer-output", type=Path, default=DEFAULT_SCORER)
    parser.add_argument("--custodian-output", type=Path, default=DEFAULT_CUSTODIAN)
    parser.add_argument("--reveal-audit-output", type=Path, default=DEFAULT_REVEAL_AUDIT)

    parser.add_argument("--scale-worker", action="store_true")
    parser.add_argument("--node-count", type=int)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--max-states", type=int, default=1 << 20)
    parser.add_argument("--io-worker", action="store_true")

    parser.add_argument("--capture-source", action="store_true")
    parser.add_argument("--api-json", type=Path)
    parser.add_argument("--tail", type=Path)
    parser.add_argument("--tail-start", type=int)
    parser.add_argument("--readme-range", type=Path)
    parser.add_argument("--readme-start", type=int)
    parser.add_argument("--source-output", type=Path, default=DEFAULT_SOURCE)
    args = parser.parse_args()

    if args.scale_worker:
        if args.node_count is None or args.seed is None:
            parser.error("--scale-worker requires --node-count and --seed")
        row = benchmark_scale_case(
            args.node_count,
            args.seed,
            max_states=args.max_states,
            deadline_seconds=args.deadline_seconds,
        )
        print(json.dumps(row, sort_keys=True, allow_nan=False))
        return 0

    if args.io_worker:
        row = benchmark_directory_durable_io(_read(MANIFEST), args.io_repetitions)
        print(json.dumps(row, sort_keys=True, allow_nan=False))
        return 0

    if args.capture_source:
        return _capture_source(args, parser)

    if not args.code_commit:
        parser.error("--code-commit is required outside worker mode")
    if args.scale_repetitions < 3:
        parser.error("--scale-repetitions must be at least three")
    if not DEFAULT_SOURCE.exists():
        parser.error(f"source evidence missing: {DEFAULT_SOURCE}")

    manifest = _read(MANIFEST)
    scale_rows = [
        _fresh_process_scale_summary(
            18,
            45,
            max_states=1 << 20,
            deadline_seconds=args.deadline_seconds,
            repetitions=args.scale_repetitions,
        ),
        _fresh_process_scale_summary(
            24,
            46,
            max_states=1 << 16,
            deadline_seconds=args.deadline_seconds,
            repetitions=args.scale_repetitions,
        ),
    ]
    durable_io = _run_json_worker(
        ["--io-worker", "--io-repetitions", str(args.io_repetitions)]
    )
    archive_evidence = _read(DEFAULT_SOURCE)
    cycle005 = _read(CYCLE005_PACKET)
    packet, scorer, custodian, reveal_audit = build_cycle006_packet(
        code_commit=args.code_commit,
        scale_rows=scale_rows,
        durable_io=durable_io,
        manifest=manifest,
        batch039=_read(AI_BASELINE),
        batch039_sha256=_sha(AI_BASELINE),
        ai_generator_module_sha256=_sha(AI_GENERATOR),
        archive_evidence=archive_evidence,
        archive_evidence_sha256=_sha(DEFAULT_SOURCE),
        cycle005_scm=cycle005["lanes"]["SCM"],
    )
    _write(args.packet_output, packet)
    _write(args.scorer_output, scorer)
    _write(args.custodian_output, custodian)
    _write(args.reveal_audit_output, reveal_audit)
    print(f"packet={args.packet_output}")
    print(f"scorer={args.scorer_output}")
    print(f"custodian={args.custodian_output}")
    print(f"reveal_audit={args.reveal_audit_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
