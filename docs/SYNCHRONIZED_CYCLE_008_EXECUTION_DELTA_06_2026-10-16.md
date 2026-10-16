# Cycle 008 Delta 06 — ER6 provider-neutral PREP/SELECT circuit

**Date:** 2026-10-16
**Work ID:** `QOS-AUDIT-010B7`
**Evidence before hosted SDK execution:** `SIMULATION_PROVIDER_NEUTRAL_CIRCUIT_CONTRACT`

## Implemented contract

The QOS-AUDIT-010B6 algebraic LCU is now expressed as an executable logical
sequence `PREP -> SELECT -> PREP_DAGGER`. PREP contains 16 amplitudes on four
little-endian select qubits: one `sqrt(1/2)`, nine `sqrt(1/18)` and six padded
zeros. SELECT has ten declared branches and applies the coefficient sign and
corresponding Pauli-Z pair to the six system qubits. The complete circuit uses
ten logical qubits before any target-specific work ancillas.

The provider-neutral artifact is
`benchmarks/results/cycle008-delta06-er6-lcu-prep-select-contract.json`. Its
digest binds the prior LCU certificate, amplitude vector, branch table,
endianness, projected 64-state diagonal and authorization locks. Core tests
verify deterministic construction, semantics, committed-artifact equality and
mutation rejection.

## Independent SDK gate

A pinned Qiskit 2.5.2 implementation constructs PREP with state preparation,
SELECT with explicitly addressed conditional phase/Pauli-Z branches, and the
inverse PREP. It projects the ten-qubit SDK operator onto select state zero and
compares the resulting 64x64 block with the frozen ER6 normalized-cut operator.
It also decomposes to `rz/sx/x/cx`, compares the decomposed full operator and
exports OpenQASM 2 resource counts. Hosted execution is required because Qiskit
is an isolated optional dependency; this document does not predeclare its
result.

## Evidence boundary

This is not a backend target, route, schedule, calibration, shot, QPU execution
or bill. Generic decomposition is not a fault-tolerant T-count and does not
establish scalable advantage. The 81-query QSVT composition has not yet been
executed with this block encoding. Provider submission and paid execution stay
false.

## A–I integration

| Lane | Status this delta | Boundary / next gate |
|---|---|---|
| A | PREP/SELECT circuit contract implemented | Await pinned-SDK projection/decomposition; then integrate with QSVT |
| B | Provider-neutral serialization path added | No backend, submission, receipt or bill |
| C | Ten logical qubits and serialization measurement surface defined | No RAM/VRAM/storage equivalence |
| D | Logical control/Pauli structure exposed | No calibrated device requirement |
| E | BIO-001/FUS-001/materials reviewed | No new measurement or commercial evidence |
| F | Digest, authorization and identical-output gates retained | No accepted-task cost or advantage |
| G | Generic gate decomposition can inform later mapping | No process-window/factory result |
| H | Cold-start report plus literature decision published | No capital or WACC authorization |
| I | Quiet/high-thrust matched-mission program preserved | `MODEL_ONLY`; I-012 remains open |

FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 were inspected. No fit,
equation, ideal bound, literature claim or logical circuit was promoted to a new
physical law, device result or commercial outcome. INV-029–035 and the six
multilingual master-plan contexts remain active but unachieved.

## Literature delta

The 2026-10-01 dense-QROM preprint is recorded separately as `LITERATURE_ONLY`.
Its reported leading-cost improvements are not transferred to this circuit.
The falsifiable next comparison freezes the table, precision and workspace and
counts restoration plus complete downstream resources.

## Next gate

First require exact-commit hosted Qiskit agreement and measured generic-basis
resources. If it passes, persist the provenance-bound SDK certificate and then
compose one block-encoding query into the frozen QSVT sequence before any dated
target-aware no-submit transpilation.

## First hosted negative result

Run #731 found that the logical projected block agrees at
`5.397791942558855e-14`, while the decomposed raw projected and full-operator
residuals are `1.5555555555555465` and `1.9444444444443676`. The pattern is
consistent with a global phase near pi. The follow-up records raw and
phase-aligned comparisons separately. Phase-aligned equivalence may validate an
un-controlled quantum operation and its generic resource count; it does not
authorize controlled/QSVT composition until a relative-phase test passes.

Run #732 then measured a phase offset of only
`-9.726339682289133e-14` radians and found no phase-aligned improvement, so the
single-global-phase hypothesis was rejected. The next implementation expresses
each branch-conditioned system Z directly as a five-qubit `MCPhase(pi)` and
returns raw projected/full matrix equality to the acceptance gate.
