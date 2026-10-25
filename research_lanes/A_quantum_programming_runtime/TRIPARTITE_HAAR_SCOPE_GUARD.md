# Lane A work item — tripartite Haar no-go scope guard

**ID:** QNS-SCOPE-001  
**Owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Status:** ACTIVE / SOFTWARE SCOPE GUARD; theorem reproduction BLOCKED  
**Source:** Li, Mori & Yoshida, PRX 16, 041013 (2026-10-13), DOI 10.1103/d7b9-ctw2  
**Implementation:** `software/uqpu-prototype/uqpu/quantum_state_scope.py`

## Contract

Input: three positive integer subsystem qubit counts `n_a,n_b,n_c`.  
Predicate: `2*n_i < n_a+n_b+n_c` for each subsystem, computed with integer arithmetic.  
Output: whether the paper's strict subsystem-size condition is satisfied.

The predicate does **not** establish Haar-randomness, the local-operation/fidelity assumptions, a no-go theorem for a concrete workload, or a usable resource. A false predicate does not imply distillability.

## Acceptance and tests

- All three subsystem sizes must be positive exact integers; booleans and floats are rejected.
- Equality at half the total is outside the strict condition.
- The predicate is invariant under subsystem permutation.
- The caller must separately supply state-family, operation, fidelity and resource provenance before any architecture claim.

## Next gate

Add this guard only to plans that explicitly model a tripartite state and a claim covered by the cited theorem. Then independently validate the theorem assumptions and run held-out, matched resource-accounting comparisons for Haar-random controls versus a specified structured-state family. No paid QPU job is authorized by this work item.
