# Cycle 008 Delta 05 — ER6 sparse LCU block-encoding contract

**Date:** 2026-10-16
**Priority:** Lane A / RG-033
**Work ID:** `QOS-AUDIT-010B6`
**Evidence class:** `SIMULATION_ALGEBRAIC_BLOCK_ENCODING_CONTRACT`

## Result

The frozen six-variable ER6 MaxCut contract now has an explicit workload-derived
LCU operator rather than a supplied dense signal unitary:

\[
A=H_{cut}/\alpha,\qquad
H_{cut}=\sum_{(u,v)\in E}(I-Z_uZ_v)/2,\qquad \alpha=9.
\]

The construction has 10 active terms (one identity and nine signed `ZZ`
terms), four select qubits and 16 padded select states. Exhaustive evaluation of
all 64 computational-basis states agrees with the frozen normalized cut-value
contract to maximum residual `1.1102230246251565e-16`. The four accepted
assignments remain indices `11`, `14`, `49`, and `52`, each with normalized cut
`7/9`. PREP probabilities sum to one with zero recorded residual.

The artifact is provenance-bound to the frozen ER6 Ising instance and accepted
output contract, and mutation tests reject altered digests or resource fields.
The committed machine-readable result is
`benchmarks/results/cycle008-delta05-er6-sparse-lcu-block-encoding.json`.

## Resource contract and boundary

For the existing degree-81 phase sequence, the logical contract requires 81
block-encoding queries. Before work registers it exposes six system qubits plus
four select qubits; each query has nine non-identity `ZZ` SELECT branches and
two PREP calls. Concrete PREP/SELECT gate counts, fault-tolerant T count,
serialized circuit bytes, target routing, runtime, energy and provider cost are
deliberately null.

This is an algebraic block-encoding contract, not a synthesized unitary or a
scalability result. No sparse-QROM bound is applied because neither a concrete
PREP/QROM implementation nor fault-tolerant precision is fixed. It is not QSVT
execution, real-QPU evidence, quantum advantage, GPU/NPU/RAM/storage
replacement, or an economic result.

## Literature surveillance

Fresh surveillance on 2026-10-16 found no primary result newer than the prior
checkpoint that changes this experiment. Recent end-to-end GQSP/QSVT work
reinforces the required separation between target operator, block encoding,
spectral domain, polynomial, phase synthesis and executable circuit. Published
sparse-QROM T-count results remain comparison envelopes only; they are not
transferred into measured project resources here.

## A–I and cross-cutting status

| Lane | Delta | Honest boundary / next gate |
|---|---|---|
| A | Explicit ER6 workload-derived LCU contract passes exhaustive algebraic verification | Synthesize provider-neutral PREP/SELECT and independently reproduce the projected operator |
| B | Provider-neutral operator description retained | No target compilation, submission, receipt or bill |
| C | Logical system/select registers and query counts exposed | No RAM/VRAM/storage equivalence; measure serialization and transfer after circuit synthesis |
| D | Logical branch structure is visible | No calibrated device or packaging requirement |
| E | BIO-001, FUS-001 and materials tracks reviewed | No new physical or commercial measurement |
| F | Digest, output contract, null resources and mutation gates are executable | No cost/energy advantage; accepted-task economics remain blocked |
| G | SELECT branch shape is available for later mapping | No target gate schedule, process window or factory evidence |
| H | Result and negative boundaries are publication-ready and cold-start recoverable | No capital/WACC claim or authorization |
| I | Matched-mission plan preserved | `MODEL_ONLY`; no vehicle/levitation result |

FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 were inspected and
preserved. No equation, fit, roadmap or ideal bound was promoted to a physical
law or commercial evidence. INV-029–035 remain goals/principles: this delta
improves the computing evidence chain and autonomous handoff, but does not
demonstrate Data-Center-to-Phone, critical-material substitution, commercial
bio-oil, net fusion electricity, financing compression or new physics.

## Validation and next gate

Focused unit tests cover exhaustive agreement, fail-closed resource fields,
mutation rejection and committed-artifact equality. The next highest-value gate
is `QOS-AUDIT-010B7`: synthesize PREP and SELECT in a provider-neutral circuit,
reconstruct the projected operator with a pinned independent SDK, record actual
decomposition/serialization scaling, and only then attempt dated target-aware
no-submit transpilation. Paid/provider execution remains disabled.
