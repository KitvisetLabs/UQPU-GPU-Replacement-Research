# Literature watch — Planckian bound on quantum dynamical entropy

**Reviewed:** 2026-10-28  
**Primary source:** Xiangyu Cao, “Planckian bound on quantum dynamical entropy,” arXiv:2507.20914 (first submitted 2025-07-28; manuscript text dated 2026-07-15), published as *Physical Review Letters* 137, 030402 on 2026-07-13.  
**Official manuscript:** https://arxiv.org/abs/2507.20914  
**Peer-reviewed record:** https://journals.aps.org/prl/abstract/10.1103/wd91-v58h  
**DOI:** https://doi.org/10.1103/wd91-v58h  
**Evidence class:** PEER_REVIEWED_THEORY + AUTHOR-REPORTED FINITE-SIZE NUMERICS; not an independent UQPU reproduction. The broad universal bound remains a conjecture.

## What the paper says

Cao defines a simplified Connes–Narnhofer–Thirring (CNT) dynamical entropy for continuously monitoring an observable: it accounts for the information gained about an initial condition while retaining an entropy-defect term for measurement back-action. For a **mesoscopic observable** (Q=V^{-1/2}sum_x Q_x) in a noncritical thermal many-body system, with a specified Gaussian weak-measurement scheme and the thermodynamic limit taken before the long-time/continuous-monitoring limits, the paper derives an entropy-rate expression in terms of Keldysh and retarded two-point Green functions (main-text Eq. 16). The author argues that emergent Gaussianity follows from cluster decomposition for the stated regime and also derives a related purification-rate expression (Eq. 19).

The paper obtains an explicit (eta s_{mathrm{CNT}}lesssim 0.57) bound by maximizing the rate expression while ignoring the fluctuation-dissipation-theorem (FDT) constraint. With FDT imposed, the end matter reports a numerically optimized tighter value (eta s_{mathrm{CNT}}lesssim 0.375). The author then **conjectures** that a Planckian bound extends to a broader class of many-body systems, operators and measurement schemes. The conjectured generality is not the same as the bound derived for the specified expression and assumptions.

The paper reports finite-size numerical comparisons for a non-integrable mixed-field Ising chain with (L=6,8,10), including scaling in (t/sqrt{L}). The manuscript explicitly notes deviations at fixed finite size/time step and motivates the ordered thermodynamic/long-time/continuous-measurement limits. These are the authors' results; UQPU has not reproduced them.

## Genuine novelty for this project

This is an observable-specific information-acquisition-rate model for FND-001/FND-003, distinct from the already recorded *Nature Physics* proof of a Planckian timescale for a universal thermalization machine. The two works use different objects and assumptions and must not be merged into a generic quantum-speed-limit formula.

## Limitations and evidence boundary

- The rate formula is scoped to the paper's measurement definition, mesoscopic observable, Gaussian scheme, noncritical thermal regime and ordered limits. The broad extension to arbitrary systems/operators/measurement schemes is explicitly conjectural.
- The finite-size numerics do not independently establish the thermodynamic-limit claim or universal conjecture. The supplemental derivation should be checked as part of a faithful reproduction.
- The bound concerns this dynamical-entropy rate, not arbitrary gate duration, QAOA runtime, fault-tolerant runtime, accepted-useful-task latency, output-information lower bounds, or total wall-plug energy.
- The monitored entropy includes outcome statistics and a measurement-back-action correction; it is not automatically useful classical output. Readout, controller computation, state preparation, memory/I/O, reset, QEC, transfer, reconstruction and cooling remain separate system costs.
- This is external theory and author-reported numerical evidence, not a UQPU experiment, new physical law, or demonstrated computing/energy advantage.

## Exact relevance to UQPU

- **FND-001:** keep intrinsic entropy/information distinct from heat, work, reset, cooling and wall-plug energy; this result does not replace Landauer accounting.
- **FND-002:** continuous-monitoring information is not automatically readable output bits or a storage-equivalence result.
- **FND-003:** it suggests a matched-observable/control research direction only after reconstructing the exact definition and ordered limits. A theorem about monitored entropy rate is not a generic gate-speed limit.
- **Lanes A/B/C/F:** any later system test must freeze the Hamiltonian, state, observable, temperature, monitoring strength/bandwidth, time window and output-quality gate; report readout/host/transfer/reset costs and uncertainty.
- **INV-029:** no physical Data-Center-to-One-Phone compression follows without a device/system-level accepted-service and lifecycle-cost result.
- **INV-031/032/033:** no accepted-liquid fuel, net fusion electricity, reduced principal/absolute interest, or lower WACC result follows.

## Falsifiable follow-up

1. Reconstruct Eq. 16 and Eq. 19 from the arXiv manuscript and supplement, recording units, sign conventions, FDT assumptions, Gaussianity premise and the order of limits.
2. Reproduce the published mixed-field Ising-chain comparison at (L=6,8,10) with pinned code/dependencies, then add at least one independent exactly solvable or independently implemented case.
3. Preregister finite-size, finite-time-step, measurement-strength and temperature sweeps; reserve held-out regimes; directly test the full CNT rate (including outcome Shannon entropy and entropy defect), not just one component.
4. Search counterexamples near criticality, in the classical/large-(N) limits, under alternative measurement schemes, and when connected higher-order correlations fail to become negligible.
5. Treat (eta s_{mathrm{CNT}}lesssim0.375) as the paper's FDT-constrained numerical optimization result under its assumptions, not as a universally proven constant. Record failures/nulls before proposing an experiment.
6. Only after the derivation and simulation gate passes should a controlled measurement experiment be designed. Keep detector/controller/reset/cooling energy separate from the system entropy-rate observable.

**Disposition:** use as a constrained FND-003 theory/reproduction target; do not promote the broad Planckian conjecture to a universal law.
