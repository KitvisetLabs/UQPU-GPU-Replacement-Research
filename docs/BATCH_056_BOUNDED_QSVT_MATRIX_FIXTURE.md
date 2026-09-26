# Eight-Lane Research Batch 056 — bounded QSVT matrix fixture

**Date:** 2026-09-26  
**Canonical starting commit:** `6e97fe31e190055332bc44c3e7299a86f7802ffc`  
**Starting CI:** GitHub Actions run 36082931611, successful  
**Primary owner:** Lane A; integration/evidence owner: Lane F

## Priority #1 result

QOS-AUDIT-010B4 lifts the Batch-055 scalar QSP convention into a constructed
Hermitian 2x2 contraction with eigenvalues 0.2 and 0.8, rotated by 0.37 radians.
The repository constructs the 4x4 one-ancilla block encoding
`[[A, i sqrt(I-A^2)], [i sqrt(I-A^2), A]]`, applies the 82 frozen phase rotations
and 81 signal queries, and independently compares the projected real block with
spectral polynomial calculus.

Measured numerical residuals:

- block-encoding top-left residual: `0.0`;
- block-encoding unitarity residual: `1.1102230246251565e-16`;
- transformed real-block residual: `5.440092820663267e-15`;
- transformed-unitary residual: `1.021405182655144e-14`.

The predeclared transform and unitarity tolerances are `2e-12` and `2e-13`.
A 0.01-radian perturbation of one phase fails the transform gate. Evidence is
`SIMULATION`: this is not a compiled circuit, independent SDK result, provider
run, accepted workload, hardware requirement or economic advantage.

A local full-suite run passed 375 tests with 6 optional skips. The dedicated
matrix fixture suite passed 4 tests, including the perturbed-phase rejection.
The fresh isolated QSPPACK 0.4.0 environment passed all 9 combined phase and
matrix tests.

## Resource and state ledger

The bounded model records degree 81, 81 signal/block-encoding queries, 82 phase
rotations, one signal ancilla, one fixture system qubit, 656 binary64 phase bytes,
64 complex128 statevector bytes and 256 complex128 dense-operator bytes. Shots
and provider jobs are zero; gate decomposition, energy and cost are explicitly
`NOT_PERFORMED` / `NOT_MEASURED`. These tiny fixture payloads are not evidence of
RAM/VRAM/storage replacement.

## Eight-lane status

| Lane | Advance or reviewed blocker | Boundary / next gate |
|---|---|---|
| A | matrix block-encoding convention and polynomial transform pass | independent SDK + explicit circuit |
| B | no cloud/provider submission | provider-neutral serialized circuit first |
| C | phase/state/operator payload ledger added | measure host/I/O after lowering; no memory equivalence |
| D | query/rotation demand is now explicit | no device requirement before target-aware gates/depth |
| E | Pangola, BIO-001, FUS-001 and cooling inputs reviewed | no material/fuel/net-electric measurement |
| F | stable contract, residuals, negative test and resource ledger | competitive accepted-task baseline absent |
| G | D/G handoff names required future circuit metrics | factory response remains blocked |
| H | software-first capital gate published | no paid escalation or finance claim |

## Literature, foundations and equation discovery

Fresh surveillance on 2026-09-26 reviewed equation discovery, symbolic
regression, theorem discovery and primary QSVT sources. No newer material result
was found that changes this gate. The dated watch records exact sources and a
future held-out/counterexample experiment. FND-001–006 and EQN-001–006 were
reviewed; the matrix computation changes no thermodynamic, information,
speed-limit, symmetry, conservation or causality boundary and proposes no new
physical law.

## Mission and permanent-invariant contribution

- INV-029 and INV-025–027: one compiler-semantic gate advances, but neither
  Data-Center-to-Phone nor any 100M-unit useful-output contract is satisfied.
- INV-030: no elemental-transmutation or qualified material substitution claim.
- INV-031: BIO-001 remains MODEL_ONLY/DATA_BLOCKED; no saleable fuel evidence.
- INV-032: FUS-001 remains MODEL_ONLY/DATA_BLOCKED; no net-electric evidence.
- INV-033: the next software-first gate limits premature capital exposure, but
  no interest, principal or WACC effect is measured.
- INV-034/035: established mathematics/physics and the full falsification chain
  remain binding; no generated equation is promoted.

Priority #1, all A–H lanes, all permanent invariants, the Kanusanan Pongpanna
Model, strategic AI-agent/funding references, and Thai/English/Chinese/Japanese/
Korean/German master-plan links were preserved.

## Next highest-value gate

**QOS-AUDIT-010B5:** independently reproduce the same matrix transform in a
pinned SDK, explicitly decompose/serialize the circuit, and record logical
qubits, ancillas, one-/two-qubit gates, depth, bytes, host runtime and memory.
Only after that should an accepted-workload fixture and target-aware simulation
be considered; paid QPU execution remains prohibited without consent and budget.
