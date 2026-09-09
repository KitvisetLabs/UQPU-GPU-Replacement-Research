"""Optional Qiskit cross-check; no provider service or network initialization."""
from __future__ import annotations


def terminal_measurement_map(circuit) -> dict[int, int]:
    """Return physical-qubit -> classical-bit permutation for a full register.

    Reject partial/dynamic measurement instead of guessing result order.
    This bounded verifier deliberately excludes ancillary classical registers.
    """
    if circuit.num_qubits != circuit.num_clbits:
        raise ValueError('verification requires equal quantum/classical register widths')
    mapping = {}
    measured = False
    for item in circuit.data:
        op = item.operation.name
        if op == 'measure':
            measured = True
            q = circuit.find_bit(item.qubits[0]).index
            c = circuit.find_bit(item.clbits[0]).index
            if q in mapping or c in mapping.values():
                raise ValueError('measurements must be a one-to-one permutation')
            mapping[q] = c
        elif measured and op != 'barrier':
            raise ValueError('only terminal measurements are supported')
    if len(mapping) != circuit.num_qubits:
        raise ValueError('all qubits must be measured once')
    return mapping


def classical_probabilities(circuit) -> tuple[float, ...]:
    """Compute ideal distribution in classical-bit order after routing."""
    if not 0 < circuit.num_qubits <= 12:
        raise ValueError('SDK verification is capped at 12 qubits')
    mapping = terminal_measurement_map(circuit)
    from qiskit.quantum_info import Statevector
    state = Statevector.from_instruction(circuit.remove_final_measurements(inplace=False))
    output = [0.0] * (1 << circuit.num_clbits)
    for index, probability in enumerate(state.probabilities()):
        classical_index = sum(((index >> q) & 1) << c for q, c in mapping.items())
        output[classical_index] += float(probability)
    return tuple(output)
