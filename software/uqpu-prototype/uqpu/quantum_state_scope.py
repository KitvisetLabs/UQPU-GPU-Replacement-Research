"""Scope guards for selected quantum-information no-go results.

This module records theorem applicability preconditions only. A True result
from a scope predicate is not a proof that an input state satisfies the
theorem's distributional assumptions and is not a claim about a physical
device or workload.
"""
from __future__ import annotations


def tripartite_haar_no_go_size_condition_applies(
    n_a: int, n_b: int, n_c: int
) -> bool:
    """Check the strict subsystem-size condition in Li, Mori & Yoshida (PRX, 2026).

    The cited theorem considers a tripartite Haar-random pure state where each
    subsystem contains fewer than half of the total qubits. Under the paper's
    state, operation, fidelity and asymptotic assumptions, its result bounds
    the possibility of distilling EPR-like bipartite entanglement.

    This function checks *only* the size condition 2*n_i < n_total. It does
    not verify that a state is Haar-random, that the local-operation model
    matches, that a target fidelity is covered, or that any theorem has been
    independently reproduced. False means only that this size condition is
    not satisfied; it does not imply distillability.
    """
    dimensions = (n_a, n_b, n_c)
    names = ("n_a", "n_b", "n_c")
    for name, value in zip(names, dimensions):
        if type(value) is not int or value <= 0:
            raise ValueError(f"{name} must be a positive integer")

    total_qubits = sum(dimensions)
    return all(2 * value < total_qubits for value in dimensions)
