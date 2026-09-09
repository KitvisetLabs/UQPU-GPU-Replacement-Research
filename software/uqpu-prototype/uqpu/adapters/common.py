from __future__ import annotations

from typing import Any

from ..portable import PortableProgram


SUPPORTED_GATES = {"x","y","z","h","s","sdg","t","tdg","rx","ry","rz","cx","cz","swap","measure_all"}


def validate_gate_program(program: PortableProgram) -> None:
    program.validate()
    unsupported = sorted({i.op for i in program.instructions if i.op not in SUPPORTED_GATES})
    if unsupported:
        raise ValueError(f"unsupported portable gate(s): {', '.join(unsupported)}")


def to_openqasm3(program: PortableProgram) -> str:
    """Serialize the portable gate subset into portable OpenQASM 3 text."""
    validate_gate_program(program)
    lines = [
        "OPENQASM 3.0;",
        'include "stdgates.inc";',
        f"qubit[{program.qubits}] q;",
        f"bit[{program.qubits}] c;",
    ]
    measured = False
    for inst in program.instructions:
        op = inst.op
        if op == "measure_all":
            lines.append("c = measure q;")
            measured = True
            continue
        if op in {"x","y","z","h","s","sdg","t","tdg"}:
            lines.append(f"{op} q[{inst.targets[0]}];")
        elif op in {"rx","ry","rz"}:
            if len(inst.params) != 1:
                raise ValueError(f"{op} requires one parameter")
            lines.append(f"{op}({inst.params[0]}) q[{inst.targets[0]}];")
        elif op in {"cx","cz"}:
            if len(inst.controls) != 1 or len(inst.targets) != 1:
                raise ValueError(f"{op} requires one control and one target")
            lines.append(f"{op} q[{inst.controls[0]}], q[{inst.targets[0]}];")
        elif op == "swap":
            if len(inst.targets) != 2:
                raise ValueError("swap requires two targets")
            lines.append(f"swap q[{inst.targets[0]}], q[{inst.targets[1]}];")
    if not measured:
        lines.append("c = measure q;")
    return "\n".join(lines) + "\n"


def dry_run_payload(provider_id: str, program: PortableProgram, fmt: str, payload: Any) -> dict[str, Any]:
    return {
        "provider_id": provider_id,
        "program_name": program.name,
        "format": fmt,
        "qubits": program.qubits,
        "shots": program.shots,
        "payload": payload,
        "evidence_level": "DRY_RUN_ONLY",
        "paid_job_submitted": False,
    }
