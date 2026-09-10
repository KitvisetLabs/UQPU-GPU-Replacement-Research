from __future__ import annotations

from collections import Counter, defaultdict
import math


def _stats(values: list[float]) -> dict | None:
    values = sorted(float(v) for v in values if v is not None and math.isfinite(float(v)))
    if not values:
        return None
    n = len(values)
    return {
        "count": n,
        "min": values[0],
        "median": values[n // 2],
        "max": values[-1],
        "mean": sum(values) / n,
    }


def active_instruction_calibration(backend, circuit) -> dict:
    """Extract snapshot properties only for instruction instances used by a routed circuit.

    The circuit is assumed to have already been transpiled for ``backend`` so its
    qubit indices are physical backend indices. Missing target properties remain
    explicit ``None`` and never count as measured success.
    """
    rows = []
    active_qubits: set[int] = set()
    op_counts = Counter()
    errors_by_op: dict[str, list[float]] = defaultdict(list)
    durations_by_op: dict[str, list[float]] = defaultdict(list)

    for item in circuit.data:
        name = item.operation.name
        if name == "barrier":
            continue
        qargs = tuple(circuit.find_bit(q).index for q in item.qubits)
        active_qubits.update(qargs)
        op_counts[name] += 1

        prop = None
        if name in backend.target.operation_names:
            table = backend.target[name]
            try:
                prop = table.get(qargs)
            except AttributeError:
                try:
                    prop = table[qargs]
                except (KeyError, TypeError):
                    prop = None

        error = getattr(prop, "error", None) if prop is not None else None
        duration = getattr(prop, "duration", None) if prop is not None else None
        if error is not None and math.isfinite(float(error)):
            errors_by_op[name].append(float(error))
        if duration is not None and math.isfinite(float(duration)):
            durations_by_op[name].append(float(duration))

        rows.append({
            "operation": name,
            "physical_qubits": list(qargs),
            "error": None if error is None else float(error),
            "duration_seconds": None if duration is None else float(duration),
        })

    return {
        "active_physical_qubits": sorted(active_qubits),
        "active_qubit_count": len(active_qubits),
        "operation_counts": dict(sorted(op_counts.items())),
        "used_instruction_instances": rows,
        "used_error_summary": {
            name: _stats(values) for name, values in sorted(errors_by_op.items())
        },
        "used_duration_summary_seconds": {
            name: _stats(values) for name, values in sorted(durations_by_op.items())
        },
    }
