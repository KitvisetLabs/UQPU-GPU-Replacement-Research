# Lane E literature watch — symbolic-regression inverse design of multi-principal-element alloys

**Date accessed:** 2026-10-24  
**Primary owner:** Lane E — materials, biomass, energy, cooling and infrastructure  
**Co-design consumers:** Lanes D (devices/chips/process/packaging), G (manufacturing equipment/factory systems), F (evidence and economics), H (strategy/publication)  
**Related invariants:** INV-030, INV-034, INV-035  
**Evidence class:** PEER-REVIEWED-ARTICLE / SURROGATE-AND-INVERSE-DESIGN METHOD CLAIM  
**UQPU project evidence promotion:** none

## Primary source and date

Peiyi Li, “Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression,” *Scientific Reports* (2026), published online 2026-10-23, accepted 2026-09-29, DOI [10.1038/s41598-026-74491-7](https://doi.org/10.1038/s41598-026-74491-7). [Publisher article](https://www.nature.com/articles/s41598-026-74491-7).

The article combines a genetic-programming symbolic-regression stage for descriptor construction, a CatBoost hardness surrogate, and three metaheuristic search methods (genetic algorithm, particle swarm optimization, and whale optimization). The publisher abstract reports a 39-feature starting library reduced by 33%, test-set R² = 0.885 and RMSE = 77.2 HV, plus 22 candidate compositions that pass the paper's physical/domain screening with predicted hardness of 716.6–783.1 HV.

## Genuine novelty relevant to UQPU

The method is a current example of an interpretable feature-discovery stage feeding a downstream inverse-composition search. It provides a useful *workflow pattern* for Lane E: discover compact descriptors, predict a declared functional metric, search a constrained design space, and then pass candidates through physical and experimental gates. Agreement among several optimizers is a robustness diagnostic for the shared surrogate, not proof of a global optimum.

The reported W/Mo strengthening role is also an important boundary for INV-030: the work is not evidence that biomass-derived carbon replaces refractory elements, noble-metal catalysts, copper interconnects, or any other critical material. It concerns a specific alloy-hardness objective and must not be generalized into a universal substitution claim.

## Limitations and evidence class

- The publisher describes an early accepted article that may be further edited before the final version of record.
- R² and RMSE characterize the reported surrogate test set; they do not prove causal mechanisms or reliability outside the sampled domain.
- Three search algorithms converging on candidates under the same surrogate does not establish global optimality or eliminate shared model bias.
- The abstract identifies processing and microstructure variables as future work. The 22 screened candidates are not treated here as experimentally fabricated and validated.
- The paper does not test Pangola-derived carbon, biomass chars, carbon composites, carbon-supported catalysts, memory/interconnect/contact functions, device lifetime, process yield, or lifecycle cost.
- No project dataset, material experiment, fuel run, fusion run, device measurement, quantum job, or cost advantage was produced by this literature review.

## Exact relevance to INV-030 and D/G co-design

The correct transfer is methodological: use interpretable descriptors and constrained inverse search to rank candidate material architectures against a declared incumbent functional unit. The correct transfer is **not** the alloy hardness values or the assumption that a high-performing composition can satisfy another application's requirements.

For Pangola/residue-derived carbon, the functional unit must be application-specific. Examples include:
- contact/interconnect: conductivity, contact resistance, electromigration/stability, current density, temperature and lifetime;
- thermal interface/spreader: thermal conductivity, anisotropy, interface resistance, mechanical integrity and cycling;
- structural/composite reinforcement: modulus, strength, fatigue, density, moisture/oxidation stability and process yield;
- recovery/sorbent/catalyst support: selectivity, capacity, kinetics, regeneration, active-material loading and cycles;
- electrode/material architecture: power/energy density, cycle life, safety, manufacturing yield and full system cost.

Lane D must translate the accepted function into device/process/packaging constraints. Lane G must add process windows, equipment capability, throughput, yield, contamination controls, maintenance, consumables and factory CAPEX/OPEX. Lane F must compare lifecycle cost per accepted functional unit with uncertainty and non-double-counted coproduct accounting. A predicted material property alone does not close any of those links.

## Falsifiable follow-up

1. Freeze the exact incumbent material and application-level functional unit before generating candidates.
2. Freeze the raw dataset version, stable sample IDs, composition/process metadata, train/validation/held-out split, feature-generation code, surrogate version, and search budget. Use the repository's split-membership contract where available; the numeric-grid fingerprints in EQN-OPT-001 do not prove raw-data split provenance.
3. Compare symbolic-regression descriptors against (a) raw descriptors, (b) standard semi-empirical features, and (c) a simple baseline model under identical data and compute budgets.
4. Hold out entire material families and processing regimes, not only random samples; include uncertainty/calibration and adversarial counterexamples.
5. Apply explicit dimensional/physical constraints where relevant and reject candidates that violate known chemistry, phase, manufacturability, safety or incumbent functional requirements.
6. Evaluate multi-objective trade-offs: function/quality, mass/volume, lifetime, yield, process energy, recoverability/recyclability, supply risk, CAPEX/OPEX and cost per accepted functional unit.
7. Fabricate and independently measure a preregistered small candidate set. Keep surrogate-only candidates MODEL_ONLY until those measurements exist.
8. A negative result is informative: if carbon candidates cannot meet the incumbent function, record direct substitution as unsuitable and test minimization, recovery, hybridization or architecture redesign instead. Never invoke elemental transmutation.

## Cross-cutting evidence boundaries

- **INV-029:** this is not evidence of physical Data-Center-to-One-Phone compression.
- **INV-030:** no critical-material substitution or Pangola-carbon function has been demonstrated.
- **INV-031:** no accepted biomass liquid fuel, yield, upgrading, or cost evidence.
- **INV-032:** no net delivered fusion electricity or cost evidence.
- **INV-033:** no reduction in financed principal, absolute interest, WACC or economy-wide rates measured.
- **INV-034/035:** symbolic regression is a hypothesis/descriptor generator. Current physics and chemistry remain binding; any proposed new constitutive relation needs dimensional/symmetry/conservation checks as applicable, limiting cases, falsifier, held-out prediction, discriminating experiment, and independent replication.

**Next gate:** obtain the paper's final version and available code/data, then define one carbon-based functional-unit benchmark with a known incumbent, leakage-resistant split, declared search budget and an explicit experimental falsifier. No commercial or universal material claim is authorized by this literature result.
