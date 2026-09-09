from __future__ import annotations

import argparse
import json

from .provider_adapters import adapter_for, adapter_health_matrix
from .provider_runtime import RuntimeConfig


def health_payload():
    return [
        {
            "provider_id": h.provider_id,
            "readiness": h.readiness.value,
            "sdk": h.sdk,
            "sdk_installed": h.installed,
            "credentials_present": h.credentials_present,
            "target": h.target,
            "notes": h.notes,
        }
        for h in adapter_health_matrix()
    ]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="UQPU quantum-cloud adapter diagnostics")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("health", help="show adapter SDK/credential readiness")

    p = sub.add_parser("dry-run", help="validate provider lowering without submission")
    p.add_argument("provider_id")
    p.add_argument("--target", default="")
    p.add_argument("--shots", type=int, default=1000)

    args = parser.parse_args(argv)

    if args.command == "health":
        print(json.dumps(health_payload(), indent=2, default=str))
        return 0

    from .cloud import ExecutionRequirements, QuantumParadigm
    adapter = adapter_for(
        args.provider_id,
        RuntimeConfig(args.provider_id, target=args.target, shots=args.shots),
    )
    program = adapter.lower(
        {"uqpu_portable_program": "diagnostic"},
        ExecutionRequirements(QuantumParadigm.GATE_MODEL),
    )
    print(json.dumps(adapter.dry_run(program), indent=2, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
