# Research gap RG-STATEPREP-SPIN-GLASS-001 — theorem-to-workload scope for profile-complexity bounds

**Created:** 2026-10-27  
**Primary lane:** A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lanes:** C, F, H; foundational links FND-002, FND-006, EQN-004  
**Source:** https://arxiv.org/abs/2610.02166 (Omar Al-Ghattas, David Gamarnik, Bobak T. Kiani; v1 submitted 2026-10-01)  
**Evidence class:** OFFICIAL PREPRINT / MATHEMATICAL COMPLEXITY RESULT; UQPU proof reconstruction pending  
**Status:** ACTIVE

## Question

Can the paper's effective-profile-complexity lower bounds be independently reconstructed and mapped to a clearly defined UQPU workload without extending the theorem beyond its dense random p-spin ensemble, state classes, energy objective, and asymptotic assumptions?

## Current evidence

The preprint introduces a profile-complexity approach based on metric entropy of p-local Pauli expectation profiles, combining a nonsymmetric quantum de Finetti argument with Gaussian-process entropy bounds. It states lower bounds on attainable energy/resource requirements for specified state classes, including an Ω(n²/log n) gate requirement for near-ground-state preparation in the paper's setting and a leading-order product-stabilizer benchmark for Clifford+T circuits with sublinear T-count.

These are source-reported mathematical claims. UQPU has not independently reconstructed the proof, run a formal checker, or mapped an actual benchmark workload to all hypotheses.

## Required acceptance gate

- Pin the exact v1 source and record theorem/definition locations and immutable digests.
- Record Hamiltonian ensemble, normalization, fixed p, state class, ancilla/discard model, gate alphabet, energy/approximation criterion, asymptotic limit, and probability qualifiers.
- Independently reconstruct the proof chain and verify the effective-profile-complexity condition and comparison benchmark.
- Run finite-size calculations only as diagnostics; clearly separate them from proof.
- Create a workload mapping with explicit PASS / FAIL / UNKNOWN for every hypothesis. Missing hypotheses must fail closed to UNKNOWN; mismatches must be OUTSIDE_SCOPE.
- Compare resource implications with a matched classical baseline only after the useful-output contract is fixed. Count preprocessing, input/state preparation, host work, memory/I/O, reconstruction, retries and accepted-task quality.
- Retain failed proof steps and counterexamples as first-class artifacts.

## Explicit nonclaims

This gap does not establish a general state-preparation lower bound, universal quantum inefficiency, a QUBO/QAOA result, physical-memory equivalence, new physics, real-QPU advantage, device/fabrication benefit, energy/material/fuel/electricity advantage, lower financing cost, or Data-Center-to-One-Phone achievement.
