# Lane A work item — equation-discovery audit guard (2026-10-24)

**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-cutting IDs:** EQN-002, EQN-003, EQN-004, FND-006, INV-034/035  
**Source baseline:** `main` at `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Status:** implementation on research branch; CI pending  
**Evidence class:** SOFTWARE_CONTRACT / UNIT_TEST

## Finding

The existing equation candidate contract rejected negative held-out errors but did not reject non-finite numeric values. An infinite baseline error paired with a finite candidate error could satisfy the comparison `candidate < baseline`, and a record with otherwise qualifying metadata could appear eligible for physical-candidate discussion. A validation counter also accepted non-integer values such as 1.5 because it checked only negativity.

## Change

- Reject NaN, positive/negative infinity, boolean or negative held-out metrics.
- Require independent validation count to be a nonnegative integer, not a boolean.
- Add regression tests for each invalid metric and counterexample.

## Validation plan / expected interpretation

CI must execute the exact branch commit and the complete existing unit/invariant suite. The tests check metadata integrity only; passing them does not prove a candidate equation correct, establish a physical law, or provide a real-QPU, material, fuel, fusion, or economic result.

## Cross-lane edges

- Lane H literature watch proposes matched-budget generator comparison and formal proof-status provenance.
- Lane F must include generator + evaluator compute, retries and accepted-result denominator in any cost/task comparison.
- FND-006 / EQN-004 require held-out tests and counterexample search before promotion.
- Lane C must not treat mathematical state-space size or formula compression as readable classical memory.


## Post-CI adversarial review — 2026-10-24

The prior head `6ebc1591bd5b859251a8cca91d2a1c9c8df188fb` passed the exact-head prototype/invariant workflow (run 960) and cold-start handoff audit. A follow-up review found a remaining type-integrity gap: converting an input with `float(value)` during validation could accept a numeric string even though the improvement property compared the original, unnormalized values. The guard now requires a real numeric type (excluding booleans), validates finite/nonnegative values through one helper, and makes the improvement property fail closed on malformed types. Tests cover numeric strings and arbitrary objects. The new commit must pass exact-head CI again; the prior green run does not validate this follow-up.

**Evidence class:** software-contract hardening only. No equation truth, physical law, QPU advantage or economic result is established.
