# Research gap RG-QEC-PLANAR-BOUNDARY-001 — reproducible planar qLDPC boundary synthesis

**Opened:** 2026-10-30 · **Primary owner:** Lane A · **Co-owners:** D/G device/layout/manufacturing; B/C/F execution and resource evidence  
**Status:** LITERATURE_ONLY / ALGORITHM REIMPLEMENTATION NOT RUN  
**Evidence:** PEER-REVIEWED MATHEMATICAL/ALGORITHMIC PAPER; NO PUBLIC SOURCE DATA/SOFTWARE IDENTIFIED  
**Source:** Liang et al., *PRX Quantum* 7, 043016 (2026-10-23), DOI 10.1103/989h-xjqv.  
**Related:** INV-025/026/027/029/034/035; FND-002/005; QEC-TRANSFER-001.

## Objective

Reimplement and independently validate the paper's construction of gapped boundaries/defects for two-dimensional topological Pauli stabilizer codes, then determine whether any constructed planar code gives a measurable physical-resource benefit after layout, decoder and control costs. The paper is a mathematical construction, not an implemented UQPU code or hardware result.

## Source scope and pinned facts

- The method truncates a bulk code, derives boundary gauge operators and boundary anyons/string operators, then constructs boundary Hamiltonians by anyon condensation and topological-order completion.
- It establishes a one-to-one bulk–boundary correspondence and derives fusion, topological spin and braiding from boundary operator algebra.
- Translation-invariant cases use Laurent polynomials and Hermite/Smith normal forms for Z_d qudits of prime or composite dimension.
- Demonstrations: Z2/Z4 toric, color, double-semion, six-semion, anomalous three-fermion and bivariate-bicycle codes.
- The paper reports a (3,3)-BB planar family with expected parameters [[288L²; 8; d=12L−O(1)]] on a 12L×12L square; a (2,−3)-BB example has anyon-string translation period 1023.
- The paper states no publicly available research data or software support the manuscript. UQPU has not reproduced the algebra or examples.

## Gate 0 — mathematical/source reconstruction

1. Pin the published PDF and DOI; transcribe assumptions and algorithm steps into a versioned executable specification.
2. Implement generalized Pauli/symplectic representations for Z2 and Z4 and the required Laurent-polynomial/Hermite/Smith-normal-form routines.
3. Record translation-invariance, straight-boundary, finite-unit-cell and two-dimensional topological-Pauli-code assumptions. Do not silently extend to arbitrary geometry, 3D, non-Pauli codes or all qLDPC families.
4. Preserve exact source examples and all failed/degenerate cases.

## Gate 1 — independent correctness

For small toric/color and selected BB examples:
- independently compute the truncated bulk stabilizer group and boundary gauge commutant;
- verify all claimed generators, commutation relations and ranks;
- enumerate local operators to confirm topological-order completion removes local logical operators;
- compute boundary anyon classes, fusion, topological spins and braiding from independent string-operator commutators;
- verify logical dimension and minimum distance by exhaustive bounded search where feasible;
- cross-check the cited [[288L²;8;12L−O(1)]] family at multiple finite L, and preserve finite-size deviations from the asymptotic expression.

## Gate 2 — compiler and device mapping

Emit a machine-readable code/layout contract: physical qubits/qudits, logical dimension, stabilizer/check count, weight and degree distribution, geometric span, routing, native-gate depth, ancillas, measurement schedule, boundary/defect operation sequence and decoder interface. Keep prime/composite qudit assumptions separate from qubit hardware capability.

## Gate 3 — accepted-output and economics

Compare with a matched planar baseline using identical code distance, logical operation, noise model and accepted logical-error threshold. Record physical-qubit overhead, cycle time, decoder p50/p95/p99, throughput, memory/I/O, host compute, energy and cost per accepted logical operation. Do not infer low overhead from code parameters alone.

## Falsifiers and nonclaims

Reject the construction transfer if independent algebra fails, local logical operators remain, finite-size distance does not match the claim, boundary strings/checks destroy locality, decoder/control deadlines fail, or physical overhead erases the theoretical advantage. No UQPU code, hardware, QEC threshold, manufacturing yield, material, fuel, fusion, financing or Data-Center-to-One-Phone result is established.
