# Research gap RG-STATEPREP-NATURAL-001 — natural-proof barrier scope for state-preparation lower bounds

**Opened:** 2026-10-27  
**Primary owner:** Lane A — quantum programming and proof/equation tooling  
**Cross-lane owners:** Lane C memory/state/data movement; Lane F evidence/integration; Lane H publication  
**Status:** OPEN / METHODOLOGY_ONLY / CONDITIONAL_THEOREM_SCOPE  
**Source:** Li and Parham, arXiv:2610.06826v1, submitted 2026-10-05  
**Related:** RG-STATEPREP-SPARSE-001, RG-QROM-SPARSE-001, FND-002, FND-006, EQN-004, EQN-005, INV-034/035

## Question

For any candidate state-preparation lower-bound argument under review, does the proof strategy satisfy both naturalness criteria in Li and Parham's definition, and does the exact circuit model and cryptographic assumption place the argument within the theorem's scope?

## Current evidence

The source defines a natural property using both largeness over Haar-random states and constructivity from a complete finite-precision amplitude list. Its theorem is conditional on a classically subexponentially secure pseudorandom-function family with polynomial-size, depth-d threshold-circuit implementations, and applies to a fixed level of the Magic Hierarchy for superpolynomial state-preparation lower bounds at the stated approximation regime. The paper identifies several existing proof techniques as natural, but UQPU has not independently audited those classifications.

This gap is about proof-method admissibility, not whether a target theorem is true. The barrier does not automatically invalidate the sparse-state-preparation or sparse-QROM bounds, and it does not supply a new circuit lower bound by itself.

## Required acceptance gate

- Pin the official source version and extract the exact theorem, assumptions, approximation error and circuit-class level.
- Review the full proof method for each candidate; never infer naturalness from a title, abstract or numerical fit.
- Record largeness and constructivity separately, with explicit evidence and an UNRESOLVED state where necessary.
- Record whether the stated cryptographic assumption is adopted, rejected or unresolved for the proof audit; do not treat it as an empirical fact.
- Run the methodology contract and its negative tests; tampering, inconsistent classifications and missing scope fields must fail closed.
- Independently review the theorem-model alignment in RG-STATEPREP-SPARSE-001 and search for counterexamples or edge cases.
- If the barrier applies, restrict the conclusion to the proof strategy under the stated assumption. Keep theorem truth, proof correctness, physical semantics and technology value as separate gates.

## Explicit nonclaims

No theorem is proved by this gap record. No lower-bound claim is automatically rejected. The contract does not establish physical truth, quantum advantage, classical-memory equivalence, a device limit, energy/material/fuel/electricity performance, project financing advantage or Data-Center-to-One-Phone compression. No provider job is authorized by this artifact.
