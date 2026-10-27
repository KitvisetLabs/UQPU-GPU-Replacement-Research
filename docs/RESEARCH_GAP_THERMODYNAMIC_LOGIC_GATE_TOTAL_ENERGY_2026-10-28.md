# Research gap — thermodynamic logic-gate total-energy reproduction

**Opened:** 2026-10-28  
**Primary owner:** Lane E — biomass/materials/energy/cooling/infrastructure methods  
**Cross-lane owners:** Lane A (identical useful-output contract), Lane D/G (device/control/factory boundary), Lane F (energy/economic evidence), Lane H (publication)  
**Status:** OPEN / LITERATURE_ONLY / MODEL RECONSTRUCTION NOT RUN  
**Related:** FND-001, FND-004, FND-006, EQN-001–006, INV-029–035  
**Primary source:** Whitelam, *Physical Review E* 114, 034135 (published 2026-09-21), https://doi.org/10.1103/9lv8-drtp

## Question

Can an evolved thermodynamic logic implementation lower total energy per accepted logic task when the full controller, measurement, actuation, initialization, reset, readout, power and cooling boundary is included, while matching a conventional baseline's truth table, output error and throughput?

## Current evidence

The publisher describes a simulation in which a genetic algorithm designs thermodynamic logic gates and reports control-system heat of similar order to the information-bearing degrees of freedom, with some designs moving heat into the control unit. UQPU has not independently reconstructed the model, source equations, search settings or heat accounting. This is a literature-derived lead only.

## Blocking unknowns

- Exact model equations, implementation/code revision, parameters, seeds and initial-state distribution.
- Definition of heat for information-bearing and control degrees of freedom and whether any external controller/feedback is outside the model.
- Truth-table accuracy, error rate, throughput, latency and gate-composition behavior under held-out conditions.
- Complete energy boundary: actuation, measurement, feedback, initialization, reset, readout, power rails, thermal management and rejected/failed tasks.
- Fair conventional baseline under the same function, error tolerance, throughput and environment.
- Independent replication and device-specific feasibility/cost evidence.

## Unlock protocol

1. Pin and independently reconstruct one source case, recording all assumptions and missing source artifacts.
2. Freeze the logic-task input/output contract, accuracy threshold, temperature/environment, throughput and evaluation split before tuning.
3. Measure or transparently model all energy/heat channels, keeping heat emitted distinct from wall-plug energy.
4. Compare full accepted-task energy and cost with a matched baseline; include failures, resets and controller overhead.
5. Run held-out initial states and composed gates; preserve nulls, failed seeds and counterexamples.
6. Require independent replication before moving from LITERATURE_ONLY to any lab/device claim.

## Falsifiers and stop rules

- Reject an advantage claim if the same truth table or output-error contract is not met.
- Reject total-energy claims that omit control, measurement, feedback, reset, power-supply or cooling terms without bounding them.
- Reject generalization if the effect vanishes on held-out states or composed gates.
- Do not transfer the result to quantum hardware, Pangola materials, bio-oil, fusion electricity or semiconductor fabrication without separate causal and domain-specific evidence.

No new physical law, lower total electricity cost, alternative UQPU device, or INV-029–033 achievement is established by this gap.
