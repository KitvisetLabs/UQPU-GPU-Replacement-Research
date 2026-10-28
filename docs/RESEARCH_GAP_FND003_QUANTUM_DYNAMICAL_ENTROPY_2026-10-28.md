# Research gap — quantum dynamical entropy and the conjectured Planckian rate

**Gap ID:** RG-FND003-QUANTUM-DYNAMICAL-ENTROPY-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane H — source provenance / literature  
**Cross-lane owners:** Lane A (matched control protocol), Lane B (provider/readout interface), Lane C (measurement/state/I/O), Lane F (evidence and cost gate)  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_PENDING  
**Sources:** arXiv:2507.20914; *Phys. Rev. Lett.* 137, 030402 (2026-07-13), DOI https://doi.org/10.1103/wd91-v58h

## Question

Can the source's CNT entropy-rate formula and its ordered thermodynamic/long-time/continuous-measurement limits be independently reproduced, and can the broad Planckian conjecture survive held-out regimes and counterexample search?

## Source-bounded baseline

The paper defines a simplified CNT dynamical entropy for continuous monitoring, including a measurement-back-action entropy defect. For a mesoscopic observable (Q=V^{-1/2}sum_x Q_x), a noncritical thermal many-body system and a specified Gaussian weak-measurement scheme, the author derives a rate formula in terms of Keldysh/retarded two-point functions under an emergent-Gaussianity argument. It reports (eta s_{mathrm{CNT}}lesssim0.57) when maximizing the formula without FDT and a numerically optimized FDT-constrained value near 0.375. It reports finite-size mixed-field Ising-chain calculations at (L=6,8,10).

The formula and bounds are scoped to these assumptions and limits. The extension to a broad class of systems/operators/measurement schemes is explicitly conjectural. The source is not the separate Planckian thermalization-machine theorem already tracked in FND-003.

## Missing evidence

1. Faithful reproduction of the supplementary derivation and exact conventions.
2. Pinned implementation of the full entropy rate, including outcome Shannon entropy and the entropy-defect/back-action term.
3. Reproduction of the reported finite-size scaling plus an independent model or independent implementation.
4. Held-out finite-size, time-step, temperature, measurement-strength and observable regimes.
5. Counterexample search near criticality, in classical/large-(N) limits, and where higher-order correlations do not satisfy the assumed Gaussian scaling.
6. Clear separation of system entropy-rate quantities from measurement/controller/reset/cooling energy and from accepted workload output.

## Acceptance contract

- Do not encode the broad conjecture as a universal lower-bound or gate-time helper in `fundamental_limits.py`.
- Preserve the source's ordered limits and regime assumptions in any implementation.
- Label source-reported results as external literature; a successful numerical reproduction remains SIMULATION until independently validated.
- A fitted constant or finite-size agreement is not proof of universal validity.
- Record nulls, failed formula reconstruction and counterexamples as first-class outputs.

## Next cheapest decisive action

Implement the paper's full rate formula from the manuscript/supplement in an isolated test harness, reproduce the published (L=6,8,10) comparison, then run preregistered held-out and adversarial regimes. No QPU submission is needed for this gate.
