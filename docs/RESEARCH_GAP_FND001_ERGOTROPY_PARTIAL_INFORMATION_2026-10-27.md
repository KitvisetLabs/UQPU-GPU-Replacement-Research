# Research gap RG-FND001-ERGOTROPY-PARTIAL-INFO-001 — partial-information work certificate

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / STATISTICAL_HELPER_IMPLEMENTED / SDP_REPRODUCTION_NOT_RUN  
**Primary owner:** Lane F — evidence and thermodynamic accounting  
**Implementation owner:** Lane A — bounded-observable confidence helper  
**Publication owner:** Lane H  
**Related:** FND-001, FND-003, INV-034/035  
**Literature watch:** docs/literature_watch/2026-10-27-ergotropy-partial-information-certification.md

## Objective

Determine whether the partial-information ergotropy certificate from Pagliaro et al. can be independently reproduced on small quantum systems and whether it can provide a properly scoped energy-resource certificate without being confused with total energy use.

## Known

- Pagliaro et al., *Physical Review Letters* 137, 130401, DOI 10.1103/pl26-g6vy (published online 2026-09-21; author preprint arXiv:2603.18828), give a two-stage SDP method for a lower bound on ergotropy when the Hamiltonian is known and the quantum state is constrained by measured observable expectations.
- For K observables with eigenvalues in [-1,1], N_i independent shots for observable i, and a union-bound confidence allocation with total failure probability delta, the paper's Hoeffding radius is epsilon_i = sqrt(2 ln(2K/delta) / N_i).
- The project added a strict helper for these statistical radii. It does not solve an SDP, estimate ergotropy, or validate the paper's full certificate.
- The authors report an IBM-processor proof-of-principle. UQPU did not run a quantum job and has not reproduced the paper.

## Blocking unknowns

- Independent reconstruction of the full SDP formulation and solver tolerances.
- Confidence coverage and bound validity across a frozen small-system test matrix.
- Sensitivity to noncommuting observables, measurement grouping, shot allocation, solver residuals and Hamiltonian mismatch.
- The relationship, if any, between the certified extractable work and an actual UQPU workload's total energy boundary.
- Measurement, state-preparation, control, reset, cooling, readout, host and I/O overheads are not part of the ergotropy certificate by default.

## Unlock criteria

1. Pin source/version, Hamiltonian and observable conventions, dependencies, test cases and a frozen seed manifest.
2. Compare the SDP certificate with exact spectral ergotropy for small systems where the state is fully known to the evaluator but hidden from the certificate.
3. Validate the confidence formula for heterogeneous N_i, multiple K, delta boundaries and invalid inputs; use simulation to check coverage without calling simulation experimental evidence.
4. Require certificate <= exact ergotropy within tolerance, and report zero/trivial bounds and solver failures rather than discarding them.
5. Keep a separate measured energy ledger for all preparation, execution, measurement, control, reset, cooling, reconstruction and host/data movement costs.

## Falsification / stop rules

Reject the reproduction if a valid test case yields a lower certificate above exact ergotropy beyond declared tolerance, if confidence coverage fails under the declared sampling model, or if source assumptions cannot be mapped to the implementation. Stop any technology/economic claim if the only result is an ideal work bound or a simulated confidence interval.

## Evidence boundary

The helper is SOFTWARE_CONTRACT; the paper is PEER_REVIEWED_THEORY with an author-reported IBM experiment. The complete certificate remains NOT_YET_REPRODUCED. No new physical law, net energy gain, QPU advantage, commercial fuel/electricity, material substitution, WACC reduction, or Data-Center-to-Phone milestone is established.
