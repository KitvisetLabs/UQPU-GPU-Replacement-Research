# Lane A contract — planar qLDPC gapped-boundary synthesis

**Date:** 2026-10-30 · **Primary owner:** Lane A · **Work item:** QEC-PLANAR-BOUNDARY-001  
**Co-owners:** D/G device/layout/manufacturing; B provider/QEC; C memory/I/O; F evidence/economics  
**Status:** LITERATURE_ONLY / REIMPLEMENTATION NOT RUN.

## Source

Liang et al., *PRX Quantum* 7, 043016 (2026-10-23), DOI https://doi.org/10.1103/989h-xjqv. The paper supplies an algorithmic framework for gapped boundaries and defects of 2D topological Pauli stabilizer codes using boundary gauge algebra, anyon condensation, topological-order completion and Laurent-polynomial/Hermite/Smith-normal-form calculations. It states no public research data or software are available.

## Input/output contract

**Input:** pinned bulk stabilizer generators, qudit dimension, translation/unit-cell assumptions, finite boundary geometry, selected Lagrangian subgroup/condensate and defect specification.

**Output:** explicit bulk and boundary stabilizer/gauge generators, boundary anyon/string operators, commutation/rank certificates, fusion/topological-spin/braiding data, logical operators, finite-patch code parameters and a machine-readable planar layout.

## Correctness gates

1. Independently validate generalized-Pauli commutation and Laurent-polynomial algebra.
2. Verify boundary gauge commutant and stabilizer rank.
3. Verify topological-order completion removes local logical operators.
4. Reconstruct boundary anyon equivalence classes, fusion, topological spins and braiding using independent string commutators.
5. Recompute source examples, including Z2/Z4 toric and selected BB codes; test finite-size distance independently.
6. Preserve assumptions: 2D topological Pauli stabilizer codes, translation-invariant bulk and straight boundary segments. General geometries/3D are not assumed.

## Resource/device interface

For each code, emit physical qubits/qudits, logical dimension, distance, check count/weight/degree, geometric span, routing, native-gate depth, ancillas, measurement schedule, decoder interface and classical syndrome bytes. D/G must translate these into planar connectivity, process, metrology, packaging and yield constraints. F compares cost per accepted logical operation under matched distance/quality.

## Acceptance and falsification

No "low-overhead" claim until independent algebra, finite-size code distance, mapped native-gate resources, decoder latency, memory/I/O, energy and cost are measured against a matched planar baseline. Reject if local logical operators survive, locality is lost, routing/decoder costs dominate or the code's physical-resource advantage disappears. No QPU job or hardware claim is implied.
