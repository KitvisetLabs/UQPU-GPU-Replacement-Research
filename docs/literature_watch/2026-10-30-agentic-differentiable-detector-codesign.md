# Literature watch — 2026-10-30: agentic detector co-design in differentiable full simulation

**Primary source:** Wonyong Chung, Qibin Liu, Liangyu Wu and Julia Gonski, “Agentic AI Detector Co-design and Optimization in Vertically Integrated Differentiable Full Simulations,” arXiv:2604.21804v3, revised 2026-10-20. Official record: https://arxiv.org/abs/2604.21804. Full text: https://arxiv.org/html/2604.21804v3.  
**Primary owner:** Lane D. **Continuous co-design:** Lane G. **Interfaces:** A/B/C/E/F/H and INV-034/035.  
**Evidence class:** OFFICIAL PREPRINT / SOURCE-REPORTED FULL-SIMULATION STUDY; NOT INDEPENDENTLY REPRODUCED BY UQPU.  
**Work item:** DG-AGENTIC-CODESIGN-001. **Focused gap:** ../RESEARCH_GAP_DG_AGENTIC_DETECTOR_COSIGN_REPRODUCTION_2026-10-30.md.

## Genuine methodological novelty

The paper introduces VIBRATO, a vertically integrated bilevel optimization workflow connecting detector geometry, front-end digitization and downstream reconstruction parameters through DD4hep/Geant4 full simulation and ROOT I/O. A reasoning agent proposes candidate geometries and interprets returned results; the simulation, inner-loop optimization, bookkeeping and digitization scans remain deterministic toolchain operations.

The case study is a dual-readout segmented-crystal electromagnetic calorimeter. The paper reports three agent trajectories under a fixed protocol, each with 48 geometry evaluations. The outer geometry search is staged separately from digitization selection; the authors explicitly do not claim that this staged decomposition proves joint optimality.

The source reports a selected geometry/digitization point with cost-weighted SNR 0.347 ± 0.002, 4.9% per-crystal mean absolute relative error for the fitted scintillation-photon count, and an estimated static ADC power of 2.8 kW for 68,608 channels. The reported ADC power uses assumed per-channel and conversion-energy coefficients; the paper explicitly says absolute values require calibration against device-level implementations.

## Important limitations and negative evidence

- This is an arXiv preprint (v3), not a peer-reviewed version-of-record claim.
- The detector-specific simulation and objective are not a quantum-chip or semiconductor-process model.
- The agent is a proposal/interpretation component, not an autonomous authority over physics, constraints or acceptance.
- The three trajectories are not independent physical replications. They use the same fixed protocol and a modelled design space.
- The staged search is not proof of joint global optimality. The source notes that tested projective offsets were unresolved on the selected width/length plateau; one reported endpoint differs from the stated optimum in the quantized grid on that axis.
- The 2.8 kW ADC estimate depends on assumed 10 mW/channel front-end floor and 30 fJ/conversion-step figure of merit. It is not measured wall-plug power.
- A reported reduction in search evaluations is not, by itself, a reduction in total R&D cost; agent tokens/API calls, simulation compute, data handling, expert review and failed trajectories must be counted.
- No UQPU chip, device, packaging, process window, yield, energy, cost or Pangola-material experiment was performed.

## Exact UQPU relevance

**Lane D/G:** the transferable idea is a closed-loop, simulation-backed co-design interface between geometry/process choices and downstream device/readout/control objectives. Candidate quantum-chip variables could include resonator/coupler geometry, photonic routing, electrode layout, package/interposer geometry, lithography/process-window variables and metrology settings—but each requires its own validated physics and process model.

**Lane A/B/C:** downstream circuit/readout/decoder objectives can be included only when they use identical accepted-output contracts and expose memory, I/O, latency and precision costs.

**Lane E/F:** objective functions must include material consumption, cryogenic and control power, yield-adjusted CAPEX, replacement/maintenance and lifecycle cost. Do not transfer the calorimeter's cost or power coefficients.

**INV-034/035:** differentiable simulators and agents can generate candidate designs or effective model hypotheses. Existing physical equations remain binding; any changed constitutive/device model must pass dimensional, symmetry, conservation, causality, limiting-case, held-out and independent experimental gates.

## Proposed falsifiable follow-up

1. Pin the exact arXiv v3 source, VIBRATO code revision, licenses, dependencies, simulation geometry, detector/material tables, input events and objective definitions; verify hashes and clean installation.
2. Reproduce the paper's three fixed-protocol trajectories and all reported endpoints before adapting the method.
3. For a UQPU D/G toy problem, begin with a fully specified, bounded device/process design space and a validated simulator or synthetic known-model oracle. Do not substitute a calorimeter model for a quantum-device model.
4. Compare agent-guided search against exhaustive enumeration where feasible, random/LHS, Bayesian or derivative-free optimization, and an expert-designed baseline under equal expensive-simulation, wall-clock, CPU/GPU, memory, token/API and monetary budgets.
5. Freeze the objective normalization and Pareto acceptance rule before the run. Use held-out geometries/process regimes and independent seeds. Report feasibility, Pareto hypervolume/regret, accepted-device metrics, constraint violations, counterexamples, repeatability and total search cost.
6. Calibrate every power/cost/material/yield model against device-level measurements before using it in a technology or finance claim.
7. Stop if agent-selected candidates violate physical/process constraints, fail held-out regimes, are Pareto-dominated, or lose their advantage after complete compute/energy/capital accounting.

**Promotion rule:** this watch remains LITERATURE_ONLY. A successful software reproduction would establish only a bounded optimization-workflow result, not a quantum-device advantage, new physical law, manufacturing yield improvement, Pangola substitution, lower project WACC or Data-Center-to-One-Phone progress.
