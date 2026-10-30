# Research gap DG-AGENTIC-CODESIGN-001 — differentiable full-simulation design transfer

**Opened:** 2026-10-30  
**Primary owner:** Lane D — device/chip/process/packaging  
**Co-owner:** Lane G — manufacturing equipment/software/factory systems  
**Interfaces:** A/B/C/E/F/H; INV-034/035  
**Status:** LITERATURE_ONLY / SOURCE_REPRODUCTION_NOT_RUN / UQPU_TRANSFER_NOT_RUN  
**Source:** Chung et al., arXiv:2604.21804v3, revised 2026-10-20.  
**Canonical watch:** docs/literature_watch/2026-10-30-agentic-differentiable-detector-codesign.md

## Objective

Determine whether an agent-guided, differentiable/full-simulation co-design workflow can improve a bounded quantum-device or manufacturing-process design under equal evaluation budgets, hard physical/manufacturing constraints and held-out regimes. The first task is to reproduce the source study; the second, separate task is to test a UQPU-specific D/G transfer.

## Source facts and unresolved points

- The source uses VIBRATO to couple DD4hep/Geant4 geometry simulation, digitization and reconstruction objectives with ROOT I/O.
- The agent proposes geometry points and interprets results; the simulator, inner-loop optimization, bookkeeping and digitization scan execute in the toolchain.
- The source reports three trajectories, each with 48 geometry evaluations, under a fixed protocol.
- The search is staged. It is not a proof of joint global optimality.
- The static ADC-power model uses assumed coefficients and is explicitly not device-calibrated absolute power.
- Exact source-code revision, environment, input event samples, detector tables, full configuration and output hashes have not been pinned or independently rebuilt by UQPU.

## Gates

### Gate 0 — source provenance and clean reproduction

Retrieve and pin arXiv v3, VIBRATO repository commit, license, dependencies, simulation configuration, event data/inputs, detector geometry/material definitions, objective functions, seeds and reported outputs. Record byte lengths and cryptographic hashes. Build a clean environment. Stop if required data, licenses or code cannot be verified.

### Gate 1 — source result reproduction

Reproduce the fixed-protocol three-trajectory study. Report all 48-per-trajectory candidate evaluations, objective values, failed simulations, feasibility decisions, staged digitization choices and source-reported endpoint metrics. Separate the modeled ADC-power estimate from measured power. Reconcile the stated grid optimum with the plateau/offset ambiguity.

### Gate 2 — bounded UQPU D/G benchmark

Define one device/process problem with explicit physical meaning and a trusted simulator or synthetic oracle. Freeze:
- design variables, units, ranges and manufacturability/process constraints;
- physical model, domain and calibration provenance;
- downstream accepted-device function and objective normalization;
- Pareto and feasibility acceptance rules;
- held-out geometry/process regimes and independent seeds;
- equal budgets for full simulations, CPU/GPU time, memory, wall-clock, agent tokens/API calls and money.

Compare at minimum exhaustive enumeration where feasible, random/LHS, one established derivative-free or Bayesian optimizer, expert-designed baseline and agent-guided search. The agent may propose candidates and explain outputs; deterministic code owns simulation, constraint checking, scoring and retention.

### Gate 3 — device and factory validation

For selected candidates, require measured device/process outputs: electrical/optical performance, control/readout fidelity, coherence or relevant lifetime, power, thermal load, critical dimensions, process window, defectivity, repeatability, packaging compatibility, wafer/device yield and lifecycle cost. Use held-out lots/devices where available.

## Required metrics

- accepted objective and Pareto hypervolume/regret under frozen normalization;
- number of full simulations and failed/invalid candidates;
- physical and manufacturing constraint violations;
- held-out generalization and counterexample rate;
- repeatability across seeds and agent runs;
- CPU/GPU hours, peak memory, wall-clock, data movement and energy where measurable;
- token/API usage, human expert hours and total search cost;
- device-level performance, power, yield and cost only after measurement.

## Falsifiers and stop rules

Reject an agentic advantage if it disappears under equal expensive-simulation budgets; if a baseline reaches the same or better held-out Pareto set; if selected candidates are physically or manufacturably infeasible; if model discrepancy invalidates the ranking; if performance depends on uncalibrated power/cost coefficients; or if full agent/simulation/verification expense erases the gain.

## Evidence boundary

This gap is LITERATURE_ONLY. No UQPU reproduction, quantum-device fabrication, manufacturing-yield improvement, Pangola material substitution, accepted bio-oil, net fusion electricity, project-finance result or new physical law is established. Do not transfer calorimeter-specific equations, costs or power coefficients to quantum chips.
