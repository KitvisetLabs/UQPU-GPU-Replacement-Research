from __future__ import annotations

import argparse
import json

from .benchmarks import run_benchmarks
from .compiler import SemanticCompiler
from .io import load_workload
from .ir import Operation, OperationKind, ResultContract, Workload, WorkloadDomain
from .version import __version__


def demo_workloads():
    return [
        Workload(
            name="monte-carlo-expectation",
            domain=WorkloadDomain.HPC,
            operations=[Operation(OperationKind.EXPECTATION, {"samples_equivalent": 1_000_000})],
            contract=ResultContract.BOUNDED_ERROR,
            input_bytes=8_000_000,
            output_bytes=64,
        ),
        Workload(
            name="exact-general-kernel",
            domain=WorkloadDomain.GENERAL,
            operations=[Operation(OperationKind.GENERAL_KERNEL, {"ops": 100_000})],
            contract=ResultContract.EXACT,
            input_bytes=1_000_000,
            output_bytes=1_000_000,
        ),
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description="UQPU semantic compiler research prototype")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("demo")
    sub.add_parser("plan")
    compile_p = sub.add_parser("compile")
    compile_p.add_argument("workload_json")
    args = parser.parse_args(argv)

    if args.command == "demo":
        gpu_costs = {"monte-carlo-expectation": 0.50, "exact-general-kernel": 0.01}
        results = run_benchmarks(demo_workloads(), gpu_costs)
        print(json.dumps([r.to_dict() for r in results], indent=2))
        return 0

    compiler = SemanticCompiler()
    workloads = [load_workload(args.workload_json)] if args.command == "compile" else demo_workloads()
    for workload in workloads:
        plan = compiler.compile(workload)
        selected = plan.selected
        print(json.dumps({
            "workload": workload.name,
            "backend": selected.assessment.backend,
            "mode": selected.assessment.mode,
            "estimated_cost_per_task": selected.cost.total,
            "estimated_seconds": selected.assessment.resources.total_seconds,
            "confidence": selected.assessment.resources.confidence,
            "evidence_level": "MODEL_ONLY",
            "reason": plan.reason,
        }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
