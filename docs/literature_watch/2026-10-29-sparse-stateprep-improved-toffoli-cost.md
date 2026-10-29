# Literature watch — sparse state preparation with improved Toffoli cost

**Access date:** 2026-10-29  
**Primary source:** Felix Rupprecht and Sabine Wölk, “Sparse quantum state preparation with improved Toffoli cost,” *Quantum* 10, 2208 (2026), published 2026-09-10.  
**Publisher:** https://quantum-journal.org/papers/q-2026-09-10-2208/  
**DOI:** https://doi.org/10.22331/q-2026-09-10-2208  
**Official preprint:** https://arxiv.org/abs/2601.09388  
**Code/assets record:** https://doi.org/10.5281/zenodo.18234600  
**Evidence class:** PEER-REVIEWED ALGORITHMIC RESULT / AUTHOR-REPORTED RESOURCE ANALYSIS; UQPU REPRODUCTION NOT PERFORMED  
**Primary owner:** Lane A — quantum programming/workloads/runtime; interfaces with Lane C state/data movement and Lane F evidence/economics.

## Genuine literature delta

The publisher record reports an improved circuit construction for preparing an s-sparse state on n qubits. The method first prepares a dense state on a ceil(log2(s))-qubit subregister, then maps it to the target using a sparse isometry. The authors report a worst-case isometry cost of approximately 2s Toffoli gates for sufficiently large n, described as roughly a log(s)/2 improvement factor over the prior state of the art; their random-state numerical benchmarks are closer to s. The paper also discusses moving work between the dense-state preparation and isometry stages for targets with real coefficients.

This is a new-to-repository, peer-reviewed state-preparation result discovered during the 2026-10-29 surveillance pass. Repository searches for the DOI, article identifier and title returned no matching file. The novelty is a better construction/resource analysis for a particular sparse-state preparation model—not a general quantum speedup or a new physical law.

## Model boundary and limitations

- The headline metric is **Toffoli count**, not total T-count, physical gate depth, wall-clock time, energy or provider cost. These metrics are not interchangeable without a gate-decomposition and hardware model.
- The stated construction uses a sparse-state representation and a dense subregister plus isometry. It does not automatically apply to arbitrary dense states, arbitrary data access, unknown amplitudes, or workloads whose support promise cannot be guaranteed.
- Numerical results for randomly chosen states are author-reported; UQPU has not independently reproduced them.
- The result must be kept distinct from Luo and Li, *Sparse Quantum State Preparation with Sublinear T-Count*, arXiv:2608.00414, and Li et al., *Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding*, arXiv:2607.28260v2. The papers use related but not yet fully reconciled synthesis/input models and different resource expressions. A Toffoli result must not be substituted directly for a T-count theorem.
- Classical description size, preprocessing, amplitude precision, support discovery, ancillas, routing, magic-state supply, measurement, output reconstruction and the complete accepted-task cost remain separate accounting items.

## Exact UQPU relevance

- **Lane A:** adds a candidate state-initialization algorithm to the workload/compiler comparison set. It may be useful only where the input contract supplies the required sparse support and amplitudes.
- **Lane C:** sparse state support, Hilbert-space dimension, classical table bytes and readable RAM/VRAM/HBM/storage are different quantities. Charge classical input storage and movement separately.
- **Lane B:** a provider run would need one target/run identity binding circuit, calibration, shots, output quality and billing. This paper alone authorizes no QPU job.
- **Lanes D/G:** translate Toffoli/T counts to the target's physical gate set, routing, depth, ancilla footprint, error correction and factory requirements before estimating hardware or manufacturing implications.
- **Lane F:** compare cost per accepted useful task, including preprocessing and all classical/quantum I/O; asymptotic or author-reported counts are not measured economics.
- **Lanes E/H:** no direct biomass, critical-material, fusion, financing or strategic-market result follows from this algorithmic paper. It may contribute indirectly only after an end-to-end computing contract passes.

## Falsifiable follow-up

1. Retrieve and hash the exact paper version and code/assets; record license and reproducibility conditions.
2. Independently reproduce small-n, small-s examples and compare the implementation against a classical state-vector reference.
3. Freeze disjoint held-out (n, s, epsilon) cases, including real and complex amplitudes, highly nonuniform amplitudes, boundary support sizes and cases that violate the sparse-support promise.
4. Build a theorem/algorithm alignment matrix for Rupprecht–Wölk, Luo–Li and the sparse-QROM result: target-state class, support promise, amplitude representation, access/oracle model, precision, gate set, preprocessing, ancillas and hidden factors.
5. Record Toffoli count, decomposed T-count, depth, ancillas, classical preprocessing, input-description bytes, fidelity/error, state-transfer and reconstruction costs separately.
6. Bind a reproduced preparation subroutine to a frozen useful-output workload only after correctness and held-out gates pass; keep simulator and paid-QPU stages separate and require explicit authorization for any paid run.

**Decision:** create a focused model-alignment gap and preregister a benchmark contract. Do not promote the result to UQPU hardware, energy, readable-memory, economic-advantage or mission-level evidence.
