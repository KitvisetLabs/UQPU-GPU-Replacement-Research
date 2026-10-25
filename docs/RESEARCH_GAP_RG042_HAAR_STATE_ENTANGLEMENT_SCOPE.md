# Research Gap RG-042 — scope-safe use of tripartite Haar-state no-go results

**Opened:** 2026-10-25  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-cutting:** Lane B/C/F, FND-006, EQN-001–006  
**Evidence state:** PEER_REVIEWED_LITERATURE + SOFTWARE_SCOPE_GUARD; theorem reproduction not yet performed  
**Project evidence promoted:** none

## Objective

Prevent distributed-QPU or state-compression proposals from inferring usable pairwise entanglement from subsystem sizes or generic claims about random-state entanglement. The 2026-10-13 PRX theorem by Li, Mori and Yoshida applies to a specified tripartite Haar-random state, subsystem-size regime, operation model and EPR-like distillation task.

## Current delta

A small helper and five unit tests check only the strict subsystem-size condition. The helper deliberately does not verify state distribution, operations, fidelity, probability bound or physical realization. It cannot establish that a theorem applies to a real workload.

## Blockers

- No project workload currently supplies a verified Haar-random state-preparation model plus matching local-operation assumptions.
- No independent proof check or reproduction of the paper's asymptotic probability bound was performed.
- No distributed-QPU state preparation, network communication, decoder, error-rate, energy or cost measurement was added.
- No comparison of Haar-random and structured resource states was executed.

## Unlock criteria

1. Require explicit state-family provenance, subsystem partition, allowed operations, target fidelity, decoder, success/failure accounting and state-preparation/communication costs.
2. Reject invalid dimensions and identify the strict size-condition boundary exactly using integer arithmetic.
3. For any in-scope claim, independently verify the source theorem's assumptions and derivation; do not infer theorem truth from the helper.
4. Freeze held-out random seeds and compare Haar-random controls with a separately specified structured-state family using the same resource accounting.
5. Report finite-size simulations as MODEL_ONLY/SIMULATION, not theorem proof or hardware evidence.
6. If proposing a route outside the theorem, state the changed assumption, distinct observable and falsifier.

## Negative-result rule

If the state distribution or operation model is unknown, classify applicability as unresolved. If the strict size condition is false, conclude only that this theorem's size predicate is not satisfied—not that entanglement is distillable. Preserve counterexamples and failed state-family assumptions.

## Mission and invariant impact

This gap reinforces INV-034/035 and protects FND-002's distinction between internal state/correlation and application-visible information. It does not close INV-029, change INV-030–033, establish a new physical law or alter INV-036/037.
