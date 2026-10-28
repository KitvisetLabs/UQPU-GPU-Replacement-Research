# Research gap — signed Max-Cut finite numeric range

**Gap ID:** RG-A-SIGNED-MAXCUT-NUMERIC-RANGE-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — objective/compiler/runtime semantics  
**Cross-lane owners:** B (SDK/target identity), C (output/state accounting), D/G (Hamiltonian/device mapping), F (reference/evidence/economics), H (handoff/publication)  
**Status:** FIX IMPLEMENTED; EXACT-HEAD CI REQUIRED  
**Related:** Batches 088–090; INV-025–027 and INV-029–035; FND-006

## Question

Does the signed-Max-Cut reference fail closed when finite inputs or derived terms exceed the representable range of its floating-point objective contract?

## Counterexample class

Finite input weights are not sufficient to guarantee finite intermediate and final values in binary64:

- `w = 10^308` may yield `-2w = -infinity` in the QUBO pair term.
- Three incident weights of `8×10^307` may make one accumulated linear coefficient unrepresentable even though each individual pair coefficient is finite.
- Three disjoint cut edges of weight `8×10^307` can produce a non-finite direct, QUBO and Ising objective score despite finite stored coefficients.
- An integer too large to convert to float may raise `OverflowError` before a finite-value check.

## Resolution in Batch 090

The signed-Max-Cut lowering now checks derived coefficients and accumulated coefficients, converts overflow into a clear `ValueError`, and guards all three score functions against non-finite sums. Regression tests cover each counterexample class. Existing objective equivalence, full maximizer-set and invalid-input tests remain in place.

## Acceptance gate

1. Exact-head prototype/invariant workflow passes, including the new regression tests.
2. Exact-head cold-start handoff audit passes.
3. A pinned SDK reconstruction independently checks the Ising sign/constant convention and agrees with exhaustive objective values and the full argmax set on small signed graphs.
4. Any failure remains recorded; no waiver based only on ordinary small-weight fixtures.

## Scope boundary

This closes a numeric-representation defect only. It does not implement QAOA, validate an SDK or target, demonstrate quantum advantage, infer readable classical memory from a quantum state, measure energy/cost, qualify Pangola-derived materials, produce accepted bio-oil, demonstrate fusion electricity, lower financing rates or achieve Data-Center-to-One-Phone physical compression.
