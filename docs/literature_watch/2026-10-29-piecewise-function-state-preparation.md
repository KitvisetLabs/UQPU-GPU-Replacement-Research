# Literature watch — explicit state preparation for piecewise-continuous functions

**Access date:** 2026-10-29  
**Primary source:** Nikita Guseynov and Nana Liu, “Efficient explicit circuit for quantum state preparation of piecewise continuous functions,” *Physical Review A* 113, 012604 (2026), published 2026-01-02.  
**Publisher:** https://journals.aps.org/pra/abstract/10.1103/plc3-2jyx  
**DOI:** https://doi.org/10.1103/plc3-2jyx  
**Evidence class:** PEER-REVIEWED ALGORITHMIC RESULT / PUBLISHER ABSTRACT REVIEWED; UQPU REPRODUCTION NOT PERFORMED  
**Primary owner:** Lane A — workload/compiler/state preparation; interfaces with Lane C state/data representation and Lane F evidence/economics.

## Genuine result and distinction from sparse-state preparation

The paper gives an explicit circuit construction for encoding discretized polynomial-function values as quantum-state amplitudes. The publisher abstract reports O(n log n) scaling in qubit count n, linear scaling with polynomial degree Q, examples with polynomial degree up to 10^4, and an extension to piecewise-polynomial functions with cost scaling linearly in the number of pieces. The construction relies on four real polynomials satisfying stated parity and boundedness conditions and targets function profiles that can be efficiently approximated by polynomial series and are not extremely localized.

This result is new-to-repository in the 2026-10-29 search. It concerns **function-structured amplitudes**, not arbitrary sparse amplitude vectors. It complements—but must not be merged into—the sparse-isometry/Toffoli result by Rupprecht and Wölk, the Luo–Li sparse-state-preparation theorem, or sparse-QROM bounds. The input representations and cost metrics differ.

## Limitations and evidence boundary

- The complexity claims apply to the paper's function representation, approximation conditions and circuit construction. They do not establish efficient preparation for arbitrary data or arbitrary amplitude profiles.
- Polynomial degree, number of pieces, approximation error, amplitude localization, coefficient representation, classical preprocessing and gate-decomposition cost all affect practical resources.
- A gate/resource analysis in a paper is not a measured UQPU workload, real-QPU advantage, reduced energy use or lower cost per accepted useful task.
- Efficient state preparation does not remove the cost of obtaining the function coefficients, moving input data, measuring outputs, reconstructing classical answers or meeting the workload's accuracy requirements.
- It does not alter general output-information lower bounds or establish that Hilbert-space dimension is equivalent to readable classical memory/storage.

## Exact UQPU relevance

- **Lane A:** candidate path for structured numerical workloads—such as smooth function profiles, selected PDE/wavefunction initial states, or piecewise-polynomial data—only when the application's input and output contracts fit the method.
- **Lane C:** account for coefficient storage, classical preprocessing, state preparation and I/O separately; state-space dimension is not a byte-capacity claim.
- **Lane F:** compare cost per accepted useful output, not qubit count or asymptotic gate expression alone.
- **Lane B:** provider-neutral target compilation is downstream; no QPU execution is authorized by this paper.
- **Lanes D/G:** translate logical gates and approximation precision to depth, routing, ancillas, noise and manufacturing requirements.
- **Lanes E/H:** no direct biomass, critical-material, fusion, finance or strategic-market result follows from this algorithm.

## Falsifiable follow-up

1. Pin the publisher paper and exact circuit/resource tables; record the source version and license.
2. Implement an independent small-register reference for Gaussian, Kaiser-window and piecewise-polynomial profiles.
3. Freeze held-out function families, polynomial degrees, piece counts, localization regimes and approximation tolerances before testing.
4. Compare against direct small-n preparation, function-aware/QSVT methods, sparse-isometry preparation only where the sparse support model applies, and classical alternatives for the same useful output.
5. Record fidelity/error, gate counts by metric, depth, ancillas, classical preprocessing and coefficient bytes, transfer, measurement/reconstruction and total accepted-task cost.
6. Retain negative controls with highly localized or non-polynomial profiles that violate the method's efficient-approximation conditions.

**Decision:** track this as a separate function-structured state-preparation gap. Do not use its complexity claim to bypass sparse-state or output-information limits, and do not promote it to UQPU performance or physical evidence.
