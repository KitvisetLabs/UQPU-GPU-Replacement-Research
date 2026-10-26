# Literature watch — 2026-10-26: strong-coupling thermodynamics, coherence, and finite-time dissipation

**Recorded:** 2026-10-26  
**Primary owner:** Lane H — literature surveillance/publication  
**Cross-lane consumers:** Lane A (workload/runtime contracts), Lane B (provider-neutral validation), Lane C (state/memory/data movement), Lane D/G (device and control co-design), Lane E (energy/cooling boundaries), Lane F (evidence/economics), INV-034/035 (foundational and equation-discovery gates)  
**Evidence class:** recent peer-reviewed theoretical frameworks + a published controlled optical experiment  
**Promotion:** literature only. No UQPU performance, energy, cost, fusion, material, or new-physical-law claim is promoted.

## Material delta

The 2026-10-25 literature-watch set already covers active environmental memory, memory-order inference, fault-tolerance spacetime accounting, equation-discovery verification, and several fusion/effective-law questions. This cycle adds three relevant primary-source records that were not indexed in the current watch directory at cycle start:

1. **Strong-coupling thermodynamic definitions.** González, Chakraborty and Rivas, “Intrinsic Hamiltonian of Mean Force and Strong-Coupling Quantum Thermodynamics,” *PRX Quantum* **7**, 043014, published **2026-10-21**, DOI [10.1103/pwws-21cx](https://doi.org/10.1103/pwws-21cx); official publisher record: [APS](https://journals.aps.org/prxquantum/abstract/10.1103/pwws-21cx), preprint [arXiv:2506.02888](https://arxiv.org/abs/2506.02888). The authors formulate thermodynamic quantities from a controlled system's reduced state for systems strongly coupled to a structured bosonic reservoir, with explicit initial-condition requirements, and test the framework on a model reservoir.

2. **Coherence-dependent relaxation in a controlled optical system.** Zhan et al., “Genuine Quantum Strong Mpemba Effect by Eliminating Coherence,” *Physical Review Letters* **137**, 170403, published **2026-10-22**, DOI [10.1103/z9t9-mwgv](https://doi.org/10.1103/z9t9-mwgv); official publisher record: [APS](https://journals.aps.org/prl/abstract/10.1103/z9t9-mwgv). The authors implement an optical setup simulating a Davies map and report a single-qubit strong Mpemba effect in which eliminating coherence changes the relaxation behavior. This is an experiment on a controlled optical quantum simulator, not a demonstration of UQPU energy savings or useful-task advantage.

3. **Finite-time entropy-production geometry.** Movilla Miangolarra, Sabbagh and Kolchinsky, “Wasserstein-2 gradient flows and the geometry of entropy production in classical and quantum stochastic thermodynamics,” accepted by *Physical Review Research* on **2026-10-19**, DOI [10.1103/t5yf-qr2h](https://doi.org/10.1103/t5yf-qr2h); public preprint [arXiv:2606.00698](https://arxiv.org/abs/2606.00698). This is a mathematical/theoretical treatment that derives finite-time entropy-production bounds from Wasserstein-2 structures and extends the geometry to Hamiltonian-dissipative dynamics under stated mobility assumptions. The accepted-paper status is not experimental validation.

## Genuine novelty and limitations

The useful combined lesson is not that a new thermodynamic loophole has appeared. Rather, thermodynamic accounting for controlled or quantum systems must state the system boundary and coupling regime, admissible initial states, measurement/feedback operations, coherence, reset/control costs, and the observable used to infer work or entropy production. These are distinct model assumptions that can change a calculated bound or a protocol's ranking.

- The strong-coupling framework is a theoretical accounting framework tested on a specified reservoir model; it does not remove the need to measure the actual system-reservoir interaction or calibrate work/heat in a concrete device.
- The optical strong-Mpemba result supports a specific coherence-dependent relaxation effect in its implemented map. Relaxation time is not automatically energy per accepted useful computation, and no universal compute-efficiency benefit follows.
- The Wasserstein-2 result provides conditional theoretical bounds, not a device-specific watt-hour estimate. Its mobility, state-space, and dynamical assumptions must be checked before applying it to UQPU workloads.
- None of the three papers establishes a new physical law, a better-than-known fundamental limit for a UQPU workload, a real-QPU economic advantage, a biomass-material substitution, accepted bio-oil, net fusion electricity, lower project WACC, or Data-Center-to-One-Phone compression.

## Exact UQPU relevance

- **FND-001 / Lane A-C-F:** extend the thermodynamic-gap ledger so that normalized work capacity, Shannon entropy, logical memory order, physical bytes, physical work, calibrated joules, reset/control energy, and accepted useful outputs remain separate quantities. Do not convert (k_B T\ln 2) per round into measured joules without a physical mapping and full boundary.
- **FND-003:** a control-time/quantum-speed-limit comparison must match initial-state preparation, reservoir coupling, measurement, feedback, resets, output quality, and control overhead. An ideal bound and a device's actual wall-clock or energy are different measurements.
- **FND-004 / Lane D-G:** coherence- and reservoir-sensitive behavior may motivate a future device/control hypothesis only after a specific controllable primitive and observable are identified. No fabrication or packaging consequence is established here.
- **FND-006 / EQN-003–004 / INV-035:** candidate equations or effective laws may be generated, but must retain the incumbent model, assumptions, dimensional and conservation checks, limiting cases, counterexample search, held-out prediction, and an independent validation path.
- **INV-029:** this work improves the proposed accounting needed for a future physical-compression contract; it is not evidence that a phone can replace remote data-center infrastructure.
- **INV-030–033:** no direct material, saleable-fuel, fusion-net-electricity, principal/interest, or financing-rate result follows. Lane E and Lane F must use separate measured functional units and lifecycle boundaries.

## Falsifiable follow-up

1. Add an explicit regime tag to each future FND-001/FND-003 model: weak coupling, strong coupling, passive input tape, active percept-action feedback, or controlled coherent relaxation. Reject comparisons that mix tags without a derivation.
2. For a finite-state memoryful agent/environment benchmark, freeze transition matrices, initial-state distribution, horizon, policy class, output-quality predicate, and all host/device/control/reset costs before evaluation. Compare memoryless, predictive, and bounded-memory policies on held-out transition parameters and seeds.
3. Keep a passive or memoryless control with matched output requirements. Search for counterexamples where a policy's work-capacity ranking reverses when the coupling regime or initial-state constraints change; record negative results.
4. If a physical experiment becomes feasible, preregister a discriminating observable, calibration, uncertainty budget, and independent replication. Measure physical work/energy and accepted useful-task quality separately; a relaxation-time or normalized-information result alone cannot pass the gate.
5. For any proposed alternative effective equation, recover established limits when coupling tends to zero, coherence is removed, feedback is disabled, and the relevant equilibrium/steady-state conditions are restored. A failed limit, violated conservation law, or absence of a distinct observable rejects promotion.

**Disposition:** literature-only. This watch sharpens the assumptions and falsifiers for FND-001/FND-003; it does not change the binding status of present physical limits or any commercial/engineering claim.
