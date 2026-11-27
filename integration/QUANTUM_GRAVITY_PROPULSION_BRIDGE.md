# Cross-Repository Research Bridge: Quantum Gravity ↔ Propulsion

**Status:** Research interface and work plan only. No quantum-gravity propulsion mechanism, antigravity effect, reactionless drive, practical levitation, fusion propulsion, or vehicle performance is demonstrated by this document.

## Purpose
Connect foundational quantum-gravity research to the engineering goal of developing a propulsion system. Integration is bidirectional: fundamental physics may suggest testable constraints or mechanisms; propulsion requirements may expose precise questions for mathematical and experimental physics. All repositories may exchange relevant hypotheses, models, code, datasets, test protocols and negative results through traceable interface records.

## Repository roles
- [Quantum-Gravity-Research](https://github.com/KitvisetLabs/Quantum-Gravity-Research): own quantum-gravity literature, mathematical foundations, candidate-framework comparison, consistency checks, observational constraints and falsifiable predictions.
- [Contactless-Propulsion-Research](https://github.com/KitvisetLabs/Contactless-Propulsion-Research): own propulsion/lift engineering, conventional baselines, atmospheric EHD/ionic wind, field interactions, energy/thrust/noise accounting, safety and mission-level testing.
- [UQPU-GPU-Replacement-Research](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research): provide computational methods, AI-assisted equation/model search, simulation, optimization, data provenance and cross-lane integration infrastructure.

## Bidirectional research questions
1. What experimentally constrained, covariant and mathematically consistent predictions do candidate quantum-gravity approaches make in regimes relevant to propulsion engineering?
2. Are any proposed gravity/quantum-field couplings distinguishable from known electromagnetic, electrostatic, aerodynamic, thermal, acoustic, vibration, measurement and environmental effects?
3. What is the strongest conventional-physics baseline for each proposed lift or propulsion effect, including momentum conservation and complete energy/momentum accounting?
4. Can a candidate model produce a quantitative, falsifiable prediction with a measurable signal above calibrated noise and known systematic effects?
5. Which results are invariant across coordinate choices, gauge choices, numerical resolution and independent implementations?

## Work packages
- BR-01 — Evidence map: catalogue established physics, peer-reviewed constraints, open theoretical proposals and unsupported claims separately.
- BR-02 — Mathematical interface: define variables, units, assumptions, domains, symmetries, conservation laws and limiting cases for any proposed coupling.
- BR-03 — Conventional baseline: calculate and measure ordinary EHD/ionic, electromagnetic, electrostatic, aerodynamic and thermal forces before invoking new physics.
- BR-04 — Falsifiable prediction: preregister predicted magnitude, sign, scaling, controls, uncertainty budget, detection threshold and explicit falsifier.
- BR-05 — Simulation cross-check: compare independent numerical methods against analytic limits and benchmark cases; publish code, parameters and seeds.
- BR-06 — Safe experiment ladder: begin with desk analysis and low-risk benchtop calibration. High-voltage/high-field, vacuum, cryogenic, radiation, fusion-related, outdoor or occupied-vehicle testing requires separate expert safety review and explicit human authorization.
- BR-07 — Integration review: publish a machine-readable record linking source commit, artifact, evidence class, owner repository, dependencies, status and next gate.

## Evidence and claim controls
Use explicit labels: ESTABLISHED_PHYSICS, PEER_REVIEWED_THEORY, HYPOTHESIS, MODEL_ONLY, SIMULATION, BENCHTOP_EXPERIMENT, INDEPENDENT_REPLICATION, DATA_BLOCKED, FALSIFIED or UNRESOLVED. A simulation is not an experiment. A mathematical consistency result is not evidence of a realizable device. Do not describe a concept as antigravity, reactionless propulsion or a working quantum-gravity engine without reproducible evidence that excludes conventional explanations.

Every candidate mechanism must:
- conserve energy and momentum or explicitly identify and test the physical system boundary and exchange channel;
- state the source of thrust and reaction momentum, not merely a force reading;
- include complete input, conversion, waste-heat and wall-plug energy accounting;
- include matched controls, blinded analysis where practical, calibration, uncertainty and environmental monitoring;
- be independently reproducible before any performance claim.

## Cross-repository change protocol
1. Keep scientific evidence in its owning repository; link rather than silently duplicate canonical datasets.
2. When a result affects another project, open/update a cross-repository issue and add an integration record containing exact commit SHA and artifact path.
3. Preserve source files and history; record provenance for copied artifacts.
4. Update each affected repository's README/WORKLOG/main summary on every integrated milestone.
5. Record negative results and rejected hypotheses; do not silently remove failed approaches.
6. No paid compute, external spending or hazardous physical test without explicit authorization.

## Initial next steps
- QGR: build a source-backed map of quantum-gravity candidate theories and experimentally constrained observables; identify whether any credible propulsion-relevant coupling is even permitted.
- Propulsion: establish calibrated conventional EHD/electromagnetic/aerodynamic thrust baselines and full momentum/energy accounting.
- UQPU: create reproducible simulation/optimization and equation-candidate validation workflows shared by both projects.
- Joint gate: do not advance a proposed quantum-gravity propulsion mechanism to hardware testing until it has a quantitative prediction, a conventional null model, independent review and an approved safety case.
