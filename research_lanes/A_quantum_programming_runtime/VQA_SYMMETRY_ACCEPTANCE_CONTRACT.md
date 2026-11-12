# VQA-SYMMETRY-001 — Symmetry-based execution-health and acceptance contract

**Primary owner:** Lane A — quantum programming / workload acceptance  
**Cross-lane owners:** Lane B (target semantics), Lane F (benchmark/evidence), Lane H (literature provenance)  
**Status:** `PROPOSED / NOT EXECUTED / MODEL_ONLY`  
**Date:** 2026-10-24  
**Motivation:** Yamaguchi & Ishikawa, arXiv:2610.29053 (2026-10-21)

## Objective

Test whether problem-derived symmetry diagnostics detect faults or invalid variational-quantum-algorithm outputs that objective-only acceptance misses, without treating symmetry as proof of optimality.

## Preconditions

- The workload's cost Hamiltonian and useful-output contract are frozen.
- Each symmetry operator is shown to commute with the specified Hamiltonian under the documented conventions; operator definitions and source digests are recorded.
- Tolerances, finite-shot estimator, seed schedule and fault-injection matrix are preregistered.
- If no useful symmetry exists, record `NOT_APPLICABLE` with a reason and continue with the existing reference/bound/output checks. Do not invent a symmetry after seeing results.

## Comparison arms

1. Objective/output-only acceptance.
2. Objective/output acceptance plus per-step commutator-oriented health checks.
3. Objective/output acceptance plus final-state symmetry-variance checks.
4. Combined diagnostics plus reference/bound certificate.

Small instances use exact solutions to calibrate the checks. Larger instances must use admissible bounds or certificates and must not pretend an unavailable exact answer exists.

## Required fault and counterexample set

- Omitted gate or altered gate parameter/sign.
- Wrong qubit mapping/layout.
- Optimizer-state or iteration-order corruption.
- Measurement-bit/readout error.
- Noise/drift matched to a declared simulator model.
- **Mandatory false-positive control:** a symmetry-preserving state/candidate that is nevertheless objectively wrong or outside the accepted task threshold.
- A problem with no applicable symmetry, to test explicit non-applicability behavior.

## Metrics

- Fault detection sensitivity and false-positive/false-negative rates.
- Symmetry commutator residual and final-state variance, with finite-shot uncertainty.
- Objective value and gap to exact solution or reference/bound certificate.
- Accepted useful-task rate and quality threshold.
- Added shots, runtime/latency, compile cost, host compute, state/I/O/transfer, retries and reconstruction.
- Energy and total cost per accepted useful task only when measured with provenance; unknown remains unknown.
- Reproducibility across blind problem instances and noise seeds.

## Pass/fail

A pass requires preregistered improvement in fault detection or false-acceptance reduction on blind cases without unacceptable loss of accepted-task throughput/quality or unreported overhead. Symmetry success alone never proves global optimality, physical correctness, quantum advantage or a new law. If the symmetry-preserving wrong-answer control is accepted, the method is explicitly insufficient as a standalone acceptance gate.

## Execution ladder and authorization

Run deterministic local/simulator tests first, then target-aware simulation and independent SDK checks. Do not submit any paid QPU job without credentials, a bounded budget and explicit user consent. Any measured quality and price must refer to the same provider/target.

## Non-claims

This contract has not been executed. It does not demonstrate quantum advantage, real-QPU performance, GPU/CPU/NPU or RAM/VRAM/storage replacement, Data-Center-to-One-Phone feasibility, material substitution, commercial bio-oil, net fusion-electricity cost, reduced principal/interest or reduced WACC.
