# Batch 073 — exact graph-parity encoding baseline for the QAOA path

**Date:** 2026-10-27  
**Canonical starting main SHA:** a4b606e3e19a820931aa4852e4f38dc734ae2170  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Evidence/integration owner:** Lane F  
**Publication/strategy owner:** Lane H  
**Related:** INV-025/026/027, INV-029, INV-034/035, RG-QAOA-PARITY-001, FND-006, EQN-004  
**Evidence class:** SOFTWARE + EXHAUSTIVE SMALL-GRAPH ENUMERATION; no circuit, QPU or economic result

## Research question

Before building a higher-order parity-QAOA circuit, can the project independently validate the logical-to-edge-parity representation and its cycle constraints on exact small graphs?

## Implemented artifact

The new provider-neutral classical reference is software/uqpu-prototype/uqpu/parity_encoding.py. It canonicalizes a simple undirected graph, maps logical vertex bits x_v to edge bits z_(u,v) = x_u XOR x_v, constructs a deterministic spanning-forest cycle basis, checks even XOR parity on every fundamental cycle, and decodes a valid physical assignment while fixing the smallest vertex of each connected component to zero.

Each non-tree edge contributes one fundamental cycle containing that edge and only spanning-tree edges otherwise. These constraints are independent by construction. For a graph with n vertices, m edges and c connected components, the cycle rank is m - n + c. Valid edge assignments are in one-to-one correspondence with logical assignments modulo one global bit flip per connected component, so the exact valid-assignment count is 2^(n-c).

## Validation performed

The new focused suite has seven tests and exhaustively enumerates small edge-bit spaces:

- triangle: one three-edge cycle constraint, valid encode/decode, and rejection of an odd-parity assignment;
- connected four-vertex/five-edge graph: two independent cycle constraints; 8 valid assignments among 32 physical bitstrings, matching 2^(4-1);
- disconnected graph with a cycle, a tree component and an isolated vertex: valid-assignment count matches 2^(n-c);
- tree: no cycle constraints;
- canonical edge order, invalid vertices/edges and malformed bit inputs.

The focused tests were run in an isolated Python environment during this cycle: 7 passed, 0 failed. The initial test draft had two fixture expectation errors (an edge-order XOR expectation and a valid bit sequence incorrectly marked invalid); those were corrected before publishing. This negative development history is retained here. The tests establish the behavior of this classical mapping oracle only.

## Fresh literature delta

The new-to-repository literature watch for Zhao, Zhang and Preskill, “Learning to erase quantum states: thermodynamic implications of quantum learning theory,” npj Quantum Information 12, 137 (published 2026-05-27; version of record 2026-08-20), identifies a peer-reviewed theorem connecting quantum-state learning, reversible computation and the work cost of erasure. It feeds FND-001/FND-002 but does not change the graph-parity result or UQPU performance claims. See the dedicated literature-watch record.

The existing 2026-10-27 higher-order parity-QAOA preprint watch remains the algorithmic motivation. Its reported IBM Heron results are external evidence, not a UQPU reproduction.

## Cross-lane status

- **A — Programming/workloads/runtime:** advanced with an exact graph-parity encoding/decoder reference. No QAOA circuit or optimizer is implemented.
- **B — Cloud/QPU/provider integration:** provider-neutral representation only; no provider adapter was invoked and no QPU job was submitted.
- **C — RAM/VRAM/HBM/storage/state/data movement:** edge-variable count and cycle constraints are algorithmic state representations, not readable RAM or storage capacity. No memory equivalence is claimed.
- **D — Device/chip/fabrication/packaging:** no native gate synthesis, routing, physical-qubit or device result. D/G co-design remains open.
- **E — Biomass/materials/bio-oil/fusion/cooling:** no new material, fuel or net-electric evidence. BIO-001 and FUS-001 remain evidence-gated.
- **F — Economics/benchmarks/evidence/integration:** exact enumeration and explicit evidence boundaries added; no accepted-task cost or measured energy result.
- **G — Manufacturing equipment/factory systems:** no manufacturing result; future native-gate and yield accounting must remain linked to D.
- **H — Strategy/finance/future industries:** strategic model, funding/agent references and multilingual master-plan links preserved; no financing-rate or commercialization claim.

## Foundational and invariant traceability

FND-001 remains MODEL_ONLY; the new learning-to-erase source suggests a memory-aware follow-up but no energy measurement. FND-002 remains an output-information lower-bound path. FND-003 still lacks a matched physical control-versus-quantum measurement. FND-004 has no demonstrated alternative primitive. FND-005 has no validated new QFT/particle mechanism. FND-006 gains a finite, exactly enumerable representation check. EQN-001–006 remain evidence-gated; this work adds no candidate physical equation.

INV-029 remains an unmet long-horizon physical-compression goal. INV-030/031/032 remain active research pillars without new commercial material/fuel/electricity evidence. INV-033 receives no new financing result. INV-034 is advanced only at the reproducible mathematical-method level; INV-035 is respected by keeping algorithmic identities separate from physical-law claims. INV-025/026/027 and all 100,000,000-unit moonshots remain falsifiable targets.

## Remaining gaps and next gate

1. Independently check the cycle-basis implementation against a second graph library or a separate GF(2) rank implementation.
2. Add signed-Max-Cut objective preservation and exhaustive objective-value equality between logical assignments and decoded parity assignments, including global-flip degeneracy.
3. Only then implement a paper-aligned higher-order parity encoding and circuit behind the existing workload path.
4. Freeze disjoint graph families/seeds, use equal shots and optimizer evaluations, and compare against direct QAOA with the existing fail-closed QAOA comparison contract.
5. Run exact-head hosted CI and inspect its final result. Any live/paid QPU run still requires credentials, a bounded budget and explicit user consent.

No paid QPU jobs were submitted.
