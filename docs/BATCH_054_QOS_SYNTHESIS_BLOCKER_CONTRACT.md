# Batch 054 — QOS synthesis blocker decision contract

**Date:** 2026-09-20  
**Gate:** QOS-AUDIT-010B2A

## Question

What can be concluded, reproducibly and without claim inflation, from the Batch-053 pinned `qsppack==0.3.0` Newton exception for the frozen degree-81 polynomial?

## Frozen input

`main` at `930624a5ce6ab95e4b78af068e00209ae1898464` reproduces the pinned Python 3.12 execution and records:

`ValueError: could not broadcast input array from shape (41,) into shape (42,)`

for coefficient fingerprint `4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a`.

Post-main CI #428 passed the repository gates, including the isolated `qsp-phase-synthesis` regression that reproduces this negative result.

## New executable contract

`uqpu.qos_d23_synthesis_blocker_contract.classify_batch053_result` makes the evidence boundary machine-checkable:

- the exact Batch-051 coefficient fingerprint is mandatory;
- the exact reproduced 41-to-42 exception classifies as `TOOL_BLOCKED_REPRODUCED`;
- no phase vector is usable from that state;
- independent reconstruction is not unlocked without a returned 82-phase vector;
- mathematical QSP infeasibility is never inferred from the implementation exception;
- even a future solver return only unlocks the separate repository-owned reconstruction gate.

The tests include wrong-provenance and wrong-phase-count adversarial cases so the contract fails closed.

## Public literature/interface context

QSPPACK's public repository describes optimization and direct phase-factor solvers for definite-parity bounded polynomials. Dong, Lin, Ni and Wang, *Robust iterative method for symmetric quantum signal processing in all parameter regimes* (arXiv:2307.12468), reports a Newton method designed to remain robust even with ill-conditioned Jacobians. Ni and Ying, *Fast Phase Factor Finding for Quantum Signal Processing* (arXiv:2410.06409), provides Half-Cholesky and fast fixed-point approaches that are useful independent algorithmic alternatives for a later audit.

These sources motivate testing an implementation-level dimensional contract or an independent solver; they do **not** prove that this repository's degree-81 candidate is realizable under the frozen convention.

## Evidence level

`PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_EXCEPTION_PLUS_FAIL_CLOSED_DECISION_CONTRACT`

This is stronger provenance/decision evidence than a prose-only blocker, but it is not phase synthesis, independent reconstruction, a theorem proof, or hardware evidence.

## Next gate

`QOS-AUDIT-010B2A`: isolate the odd-parity Jacobian dimension on a small known polynomial and either (a) test the smallest auditable correction without changing the frozen target polynomial/criterion, or (b) pin an independent maintained phase solver. Only a finite 82-phase result satisfying its declared residual criterion may proceed to `QOS-AUDIT-010B3` repository-owned 2x2 reconstruction.

## Non-claims

No real-QPU execution, quantum advantage, theorem-certified QSP/QSVT correctness, mathematical QSP infeasibility, full-channel D.23, GPU/NPU/RAM/DRAM/HBM replacement, >=100x, >=100,000,000x, measured economic advantage, or new physical law is claimed.
