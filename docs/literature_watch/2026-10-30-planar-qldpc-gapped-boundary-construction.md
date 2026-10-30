# Literature watch — 2026-10-30: algorithmic gapped boundaries for planar qLDPC codes

**Primary source:** Zijian Liang, Bowen Yang, Joseph T. Iosue and Yu-An Chen, “Algorithmic Construction of Gapped Boundaries for Topological Stabilizer Codes: A Route to Low-Overhead Planar qLDPC Codes,” *PRX Quantum* 7, 043016, published 2026-10-23. DOI: https://doi.org/10.1103/989h-xjqv.  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime. **Co-owners:** D/G device/layout/manufacturing; B/C/F evidence and resource interfaces.  
**Evidence:** PEER-REVIEWED MATHEMATICAL/ALGORITHMIC CODE-CONSTRUCTION PAPER; NOT REPRODUCED BY UQPU.  
**Work item:** QEC-PLANAR-BOUNDARY-001. **Gap:** ../RESEARCH_GAP_QEC_PLANAR_GAPPED_BOUNDARY_REPRODUCTION_2026-10-30.md.

## Genuine novelty

The paper gives an operator-algebraic framework and computational algorithms for constructing all gapped boundaries and defects of two-dimensional topological Pauli stabilizer codes. Starting from a truncated bulk code, it derives boundary gauge operators, boundary anyons and string operators, then constructs microscopic boundary Hamiltonians through anyon condensation and topological-order completion. The paper proves a one-to-one bulk–boundary correspondence for anyon types and extracts fusion rules, topological spins and braiding from boundary operators.

For translation-invariant codes, Laurent-polynomial representations reduce the construction to finite matrix operations using Hermite and Smith normal forms, for Z_d qudits of prime or composite dimension. Demonstrations include Z2/Z4 toric codes, color, double-semion, six-semion and anomalous three-fermion codes, plus bivariate-bicycle examples.

The paper reports a (3,3)-BB planar construction on a 12L×12L square with expected parameters [[288L²; 8; d=12L−O(1)]]. For a (2,−3)-BB example it reports anyon translation period 1023 and 20 independent generators of the boundary-anyon fusion group. These are source-reported mathematical/code parameters, not UQPU hardware measurements.

## Scope and limitations

- The method is for two-dimensional topological Pauli stabilizer codes. The paper assumes translation invariance in the bulk and along straight boundary segments; broader geometries and higher dimensions are future directions, not established coverage.
- The paper's “low-overhead” motivation is not a measured hardware overhead or production result. The reported [[288L²;8;12L−O(1)]] family still requires an explicit physical-layout, gate, ancilla, decoder and cost comparison.
- Long anyon-string translation periods (including 1023 in the cited BB example) can create nontrivial layout/routing/decoder burdens; do not equate locality of bulk checks with short boundary operations.
- The paper explicitly states that no research data or software supporting the manuscript are publicly available. UQPU must implement the method from the paper and independently verify it.
- Qudit dimension, stabilizer weight, code distance and logical dimension are mathematical/code properties, not direct claims about physical qubit count, hardware fidelity or fault-tolerant advantage.

## Exact UQPU relevance

- **A:** candidate compiler/runtime transformation from periodic bulk-code specification to explicit planar boundary/defect Hamiltonians and logical operations.
- **B:** future provider-neutral QEC target only after native qudit/qubit support, measurement schedule and decoder interfaces are specified.
- **C:** report physical data/ancilla/check memory and classical syndrome storage separately; code dimension is not readable storage.
- **D/G:** derive planar connectivity, check weight/degree, routing, lithography/packaging and metrology requirements; no fab or yield result follows.
- **E:** no material, bio-oil, fusion or cooling-energy result.
- **F:** compare physical-qubit/logical-qubit overhead, gate depth, ancilla, decoder latency, energy and cost per accepted logical operation against a matched planar baseline.
- **H:** source-attributed future-industry research only.
- **INV-029/034/035:** a mathematical architecture lead, not physical Data-Center-to-One-Phone compression or a new physical law.

## Falsifiable follow-up

Implement the construction for small Z2/Z4 toric, color and selected bivariate-bicycle examples. Verify boundary gauge commutation, stabilizer rank, local-logical removal, boundary anyon classes, fusion, topological spin and braiding with an independent exact symplectic-algebra implementation and exhaustive finite-patch checks. Recompute the cited BB parameters for several L and test finite-size distance directly.

Then map the resulting checks and boundary/defect operations to a declared planar hardware topology. Record physical qubits, check weight/degree, routing, gate depth, ancillas, measurement schedule, decoder complexity/latency, memory/I/O, energy and cost per accepted logical operation. Reject a low-overhead claim if locality, distance, decoder or physical-resource costs erase the theoretical benefit.

No UQPU code reproduction, target simulation, QPU result, manufacturing result or quantum advantage is claimed.
