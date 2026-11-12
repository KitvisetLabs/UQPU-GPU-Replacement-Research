# Literature watch — 2026-10-24: fusion cost-account integration and architecture-specific sensitivities

**Published online:** 2026-09-08  
**Accessed:** 2026-10-24  
**Primary owner:** Lane E — energy, materials and infrastructure  
**Cross-lane consumers:** Lane F economics/evidence; Lane D/G materials/manufacturing; Lane H finance/strategy  
**Feeds:** FUS-001, FIN-001, INV-032/033, INV-034/035  
**Evidence class:** PEER-REVIEWED COST-MODEL METHODOLOGY / LITERATURE_ONLY  
**UQPU project evidence promotion:** none  
**Canonical starting main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e

## Primary source

Matthew J. Nyberg, Virginia Lilly, Jia Zhou, Nicolas Stauff, Craig M. Jacobson and Ben A. Lindley, “Adaptation of Nuclear Fission Cost Estimation Tools for Fusion Energy Systems,” Fusion Science and Technology, published online 8 September 2026, DOI 10.1080/15361055.2026.2726713. Official records: [OSTI ID 3709681](https://www.osti.gov/pages/biblio/3709681) and [publisher article](https://www.tandfonline.com/doi/full/10.1080/15361055.2026.2726713).

The paper extends the Algorithm for the Capital Cost Estimation of Reactor Technologies (ACCERT) by integrating models from existing fusion codes, including PROCESS and TEAm, into a common Code of Accounts (COA) framework. It demonstrates comparative sensitivity analysis for tokamaks, stellarators and tandem mirrors, focusing on relative sensitivity to uncertain parameters rather than claiming absolute cost comparability across designs of different scale.

The authors report magnets and breeding blankets as major cost drivers across the three concepts, with sensitivity depending on confinement scheme and blanket technology. The publisher record discloses that one author is a co-founder and technical advisor to Realta Fusion; that relationship is relevant context for interpretation, not by itself a reason to reject the method.

## Genuine novelty for UQPU

The contribution is traceable mapping from physics/design assumptions into a standardized cost-account structure and sensitivity workflow. That supports FUS-001 by making architecture-specific cost drivers auditable rather than hiding them in a single plant-capital multiplier. It also provides a potential interface for future coupling to external physics codes and design optimization.

This is a cost-estimation methodology and scenario analysis. It is not a measured plant, an independently validated commercial LCOE, proof of net-electric operation, or evidence that any fusion architecture is already low-cost.

## Limitations and evidence boundary

- The paper focuses on relative cost sensitivities and explicitly avoids comparing absolute costs across systems of differing scale.
- Cost sensitivity is not equivalent to net delivered electricity, availability, commercial reliability, or lifecycle cost.
- The reported ranking depends on architecture, geometry, materials, technology readiness, supply chain, component lifetime, maintenance and assumptions. It must not be imported as a universal ranking for every fusion design.
- A common COA does not by itself prove that each subsystem model is accurate or that cost accounts are complete.
- The paper does not establish the project's net-electric denominator, recirculating power, capacity factor, construction duration, tritium/fuel-cycle performance, irradiation lifetime, remote maintenance, grid interface, decommissioning or project-specific financing.
- No UQPU fusion hardware, materials irradiation, fuel-cycle, net-electricity or commercial-cost experiment was performed.

## Exact relevance to INV-032 and INV-033

FUS-001 should preserve architecture-neutral output requirements while allowing architecture-specific modules for magnets, blankets, neutron multipliers, shielding, vacuum vessel and other dominant subsystems. A valid model must eventually report reliable net delivered electricity and include:
- recirculating power and plant auxiliaries;
- thermal-to-electric conversion and cooling;
- capacity factor and component replacement/lifetime;
- construction schedule and learning/scale assumptions;
- fuel cycle, materials damage, maintenance and remote handling;
- grid interface and decommissioning;
- CAPEX/OPEX, contingency, uncertainty, financing and time-to-evidence.

INV-033 remains separate: lower required principal or shorter capital lock-up can reduce absolute interest at unchanged terms, but a lower WACC/risk premium requires separate evidence. A sensitivity analysis does not establish either commercial cost or a financing-rate effect.

## Cross-lane relevance

- **D/G:** translate magnet, blanket, shield, vessel and manufacturing assumptions into process-window, material availability, yield, inspection, replacement and cost-per-good-component evidence.
- **E:** connect plasma/plant physics to net electricity, thermal loads, cooling and maintenance rather than fusion gain alone.
- **F:** propagate uncertainty through the COA, disclose scenario boundaries, avoid double-counting and normalize by accepted net MWh over a declared lifetime.
- **H:** stage capital on decisive subsystem evidence; compare cost of information and time-to-evidence without inferring lower WACC.
- **A/B/C:** software may help run sensitivity/optimization studies, but any quantum route must beat a competitive classical baseline on the same objective, data and total resource budget. No provider job is required by this watch.

## Falsifiable follow-up — FUS-001-COA-ADAPTER-001

1. Freeze one reference architecture, geometry, power-balance assumptions, cost year/currency, plant lifetime, financing convention and evidence sources.
2. Build a versioned adapter that maps the selected subsystem model into a declared COA; reject missing cost accounts rather than silently assigning zero.
3. Run sensitivity sweeps over superconductors, blanket materials, neutron multipliers, shielding, vessel and other architecture-relevant drivers. Preserve parameter provenance and correlations.
4. Report cost distributions and driver rankings separately from net-electric performance. Add recirculating power, availability, conversion, replacement, fuel cycle, remote maintenance, grid and decommissioning before computing lifecycle cost per net MWh.
5. Compare at least one subsystem estimate with an independent bottom-up estimate and hold out one scenario/parameter set for validation.
6. Record model version, assumptions, uncertainty, negative results and total finance assumptions. Keep the result MODEL_ONLY until engineering evidence and independent validation gates pass.

**Fail conditions:** missing accounts silently treated as zero; incompatible scale or price-year comparisons; sensitivity rank reverses under plausible held-out assumptions without being reported; net-electric or lifecycle terms omitted; or model output presented as commercial fusion performance.

## Integration boundary

A related fusion costing-framework watch is proposed in PR #49, but it does not yet appear on canonical main and this source was not in its two cited preprints. This article records the distinct September journal contribution without claiming that PR #49 or any UQPU fusion model is merged or validated.

No low-cost fusion, net-electricity advantage, new physical law, Pangola-material substitution, or lower WACC is established. Existing physical laws remain binding for present engineering claims.
