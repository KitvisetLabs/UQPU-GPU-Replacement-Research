# Literature watch — 2026-10-28: evolutionary thermodynamic logic gates and control heat

**Source:** Stephen Whitelam, “Evolutionary design of thermodynamic logic gates and their heat emission,” *Physical Review E* 114, 034135. Published 2026-09-21. DOI: https://doi.org/10.1103/9lv8-drtp. Official publisher page: https://journals.aps.org/pre/abstract/10.1103/9lv8-drtp.  
**Accessed:** 2026-10-28  
**Publication owner:** Lane H  
**Technical owners:** Lane E (thermodynamic/energy boundary), Lane A (accepted logic-task contract), Lane F (total-energy evidence)  
**Evidence class:** PEER_REVIEWED_SIMULATION / LITERATURE_ONLY for UQPU  
**Feeds:** FND-001, FND-004, FND-006, EQN-001–006, INV-034/035; potential future Lane D/G co-design

## What is genuinely new

The paper uses evolutionary search in a simulated thermodynamic computer to design logic operations whose control-system heat emission is reported to be of a similar order to the heat emitted by information-bearing degrees of freedom. It also reports simulated designs that move dissipation away from the information-bearing subsystem and into the control unit. This makes control architecture and where heat is released part of the candidate computation design, rather than treating only the logical state variables as the thermodynamic system boundary.

The publisher abstract explicitly describes simulations. The accessible material inspected for this watch does not constitute an independent reconstruction of the full model, an experimental device result, or a measured wall-plug energy advantage.

## Why it matters to UQPU

- **FND-001:** reinforces the need to measure the entire operation boundary, not infer energy from a state variable or a Landauer floor alone.
- **FND-004:** provides an alternative-primitive lead for thermodynamic/probabilistic computing. It does not demonstrate a UQPU physical primitive.
- **Lane A:** a logic operation must be compared under the same truth table, output-error threshold, throughput and input/output contract.
- **Lanes D/G:** if a physical prototype is later proposed, the control medium, readout, reset, thermal path, fabrication yield and metrology are device/factory variables, not free overhead.
- **Lane F:** heat emission, energy supplied by power rails, measurement/feedback, initialization, reset, cooling and energy per accepted task are distinct quantities. A lower heat emission in one subsystem is not necessarily lower total electricity or lifecycle cost.
- **INV-029–033:** no phone-compression, Pangola material, accepted bio-oil, net fusion electricity, financing or cost result follows from this paper.

## Limitations and evidence boundary

The source-reported result is simulation-level and model-specific. This cycle did not reproduce the source equations, search settings, initial-state distribution, error rates, control-energy accounting or heat trajectories. A thermodynamic bound such as Landauer's principle remains a lower bound under its stated conditions; the paper does not make the bound disappear, and the UQPU project does not promote a new physical law.

Do not infer that control heat can be eliminated, that heat transfer equals reduced wall-plug electricity, or that the reported regime transfers to quantum processors, Pangola conversion, fusion auxiliaries or semiconductor fabrication.

## Falsifiable follow-up

1. Pin the exact paper version, model equations, search code if available, environment, initial distributions, gate truth tables, seeds and all hyperparameters.
2. Reconstruct one small gate and publish raw trajectories plus the exact definition of heat for information-bearing and control degrees of freedom.
3. Compare with a preregistered baseline implementing the same truth table, output-error rate, throughput, duration and initial-state distribution.
4. Account separately for information-bearing heat, controller heat, external measurement/feedback, actuation, initialization, reset, readout, power-supply energy and cooling. Report wall-plug energy only when measured or explicitly modeled with a validated conversion boundary.
5. Test held-out initial states and compositions of gates; preserve failed seeds and counterexamples.
6. Require independent replication before proposing device consequences or economic transfer.

**Decision:** retain as a literature-derived candidate for a controlled FND-001/FND-004 reproduction. Status remains LITERATURE_ONLY. No new equation, physical law, device advantage or mission milestone is claimed.
