# Research gap RG-A-QUESTAB-EXTENDED-TABLEAU-REPRO-001 — exact multi-GPU extended-tableau reproduction

**Opened:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** B (backend portability), C (state/memory/data movement), F (evidence/economics), D/G (GPU/device/manufacturing co-design), H (publication)  
**Status:** OPEN / LITERATURE_ONLY / SOURCE-PINNING-NOT-STARTED  
**Source:** https://doi.org/10.1145/3797905.3816723  
**Related:** RG-QAOA-PARITY-001, RG-A-QUASARQ-STABILIZER-REPRO-001, INV-025/026/027, INV-029, INV-034/035

## Objective

Determine whether the published quEStab extended-stabilizer-tableau simulator can be reproduced on a bounded, preregistered circuit set and whether its memory/runtime behavior remains useful for parity-QAOA and broader simulation gates after exactness, non-Clifford row growth, host work, memory movement and energy are counted.

## Current evidence

The ACM ICS '26 paper (published 2026-07-05) reports an extended tableau that represents non-Clifford evolution through weighted Pauli-row branching and merging and distributes rows across GPUs. It reports 100/128 QASMBench circuits completed (78.1%) and very large memory savings against state-vector baselines on selected cases. A separate passage in the publisher-indexed text reports 69/97 (71.1%); these may describe different benchmark stages/subsets, but the transition needs table-level reconciliation before the values are compared or reused.

No UQPU reproduction, pinned upstream source commit, target-specific benchmark, or measured UQPU cost/energy result is established by this gap.

## Acceptance contract

- Pin upstream source commit, license, dependencies, compiler/CUDA/driver versions, GPU/CPU models, build flags and input hashes.
- Predeclare circuit families and splits: Clifford-only; non-Clifford T-gate; parameterized rotations; small parity-QAOA instances at fixed graph/depth tiers; one held-out circuit family and one held-out non-Clifford-density regime.
- Compare outputs with independent exact state-vector or analytic references while tractable. Check probability distributions, selected expectation values, decoded objective values and argmax-set equivalence as appropriate.
- Record qubits, gate counts by class, depth, parameter precision, shots/measurements, transpilation/setup, warm-up, wall time, throughput, peak host/device memory, active tableau-row count, transfer bytes/time, host compute, reconstruction, failures, retries and energy boundary/instrumentation.
- Pair every baseline with its own version, hardware and configuration. Stim/QuaSARQ are Clifford-only comparators unless a circuit is within their supported semantics; do not label them general non-Clifford baselines.
- Reconcile each reported coverage numerator and denominator with its exact subset, preprocessing stage, timeout and completion criterion.
- Use held-out tests and preserve negative results. Unknown costs/energy stay UNKNOWN rather than zero.

## Falsifiers and unlock criteria

Reject a correctness claim if any tractable output fails the independent reference or declared tolerance. Reject a scaling claim if active-row growth, memory exhaustion, transfer/setup/host overhead or the held-out regime erases the claimed benefit. Reject a coverage comparison whose denominators, circuit transformations or timeout rules are not aligned. Close the gap only after a pinned, repeatable run produces a source-linked result manifest and independent review.

## Current alternative and next cheapest decisive experiment

Keep the exact small-instance parity-QAOA objective/argmax certificate as the primary Lane A gate. In parallel, pin quEStab and run a small deterministic circuit suite before attempting the paper's larger benchmark. No paid QPU execution is required or authorized for this work.

## Nonclaims

This gap establishes no real-QPU advantage, no universal simulator scaling, no readable classical-memory equivalence, no 100x/100,000,000x economics, no Data-Center-to-One-Phone result, no new physical law, no Pangola material substitution, no accepted commercial bio-oil, no net fusion electricity and no reduction in WACC.
