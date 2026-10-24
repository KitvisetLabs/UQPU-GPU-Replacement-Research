# Literature watch — 2026-10-24: bio-oil process economics and fusion economic-gain criteria

**Accessed:** 2026-10-24  
**Primary owner:** Lane F — economics, benchmarks and evidence integration  
**Feeds:** Lane E (biomass/energy), D/G (materials/process requirements), H (strategic finance), BIO-001, FUS-001, FIN-001, INV-029–033  
**Evidence class:** `LITERATURE_ONLY / PEER_REVIEWED_TECHNO_ECONOMIC_MODELS`  
**Project evidence promotion:** none

## Source 1 — process-level biomass pyrolysis economics

Geetanjali Yadav and Patrick Lamers, “Process Feasibility Analysis of Waste Biomass Valorization to Biochar and Bio-Oil via Slow and Fast Pyrolysis,” *Energy & Fuels* 40(9), 4670–4682 (2026), online 2025-12-25 / issue 2026-03-05. DOI: https://doi.org/10.1021/acs.energyfuels.5c05655. The work is associated with NREL's Catalytic Carbon Transformation and Scale-Up Center and Strategic Energy Analysis Center.

**Genuine relevance:** the process model explicitly includes feedstock preprocessing, slow/fast pyrolysis and separation into bio-oil, biochar and gaseous products. The paper identifies feedstock cost, yield and plant capacity as important economic levers. Its reported conclusions distinguish slow-pyrolysis biochar economics from fast-pyrolysis bio-oil, which remains more expensive than fossil-derived fuel under the modeled cases. That distinction supports the project's rule that a coproduct or carbon-credit scenario must not be used to hide the delivered liquid-fuel cost.

**Limits:** this is a techno-economic model, not a measured Pangola conversion plant, a sale contract, or a certified fuel specification. Results depend on feedstock, process boundary, scale, product quality, energy integration, prices and coproduct-credit assumptions. Raw pyrolysis liquid is not automatically an accepted upgraded fuel. The paper does not prove ultra-low-cost commercial bio-oil.

## Source 2 — an architecture-neutral fusion economic-gain criterion

D. G. Whyte, A. Lo, R. Bielajew, M. Hancock, R. Moeykens, G. Shaw and colleagues, “Criteria for the economic viability of fusion power plants,” *Journal of Fusion Energy* 45, article 49 (published 2026-07-10). DOI: https://doi.org/10.1007/s10894-026-00577-9.

**Genuine relevance:** the authors propose a normalized economic-gain framework, `Q_econ`, built around a control surface and factors including power density, energy fluence, component lifetime, energy capture, cost and financing. The paper states `Q_econ >= 1` is necessary but insufficient for commercial viability. This is useful as a second diagnostic beside a full auditable cost-account framework such as FECONs/pyFECONs; it may expose designs whose material fluence, replacement interval or component economics make them unattractive even if plasma gain looks promising.

**Limits:** `Q_econ` is a model criterion, not observed net-electric output or a commercial price. The framework assumes temporal equilibrium and a mature plant with production and component-replacement periods; the authors explicitly describe the threshold as necessary but insufficient because not all real-world costs are necessarily included. A normalized criterion must not replace a plant boundary, net-power balance, uncertainty analysis or full lifecycle costing.

## Exact UQPU / energy / materials / finance relevance

- **BIO-001 / INV-031:** use the pyrolysis TEA as a published process-model replication control. Build a separate Pangola/agricultural-residue mass-and-energy balance; track wet/dry feedstock basis, preprocessing, yields, upgrading, hydrogen/catalysts, utilities, CAPEX/OPEX, logistics, financing and accepted final liquid-energy/fuel function. Credit biochar or gases only for demonstrated, saleable coproducts and avoid double counting.
- **INV-030:** biomass carbon may be a useful coproduct/material stream, but these sources do not establish Pangola-derived carbon properties or any functional substitution for critical technology materials. No elemental transmutation is claimed.
- **FUS-001 / INV-032:** crosswalk `Q_econ` to the auditable FECONs/pyFECONs cost accounts. Preserve net delivered electricity as the denominator and explicitly include recirculating power, capacity factor, construction schedule, component life/replacement, fuel cycle, materials damage, maintenance/remote handling, conversion/cooling, grid interfaces, financing and decommissioning.
- **FIN-001 / INV-033:** report financed principal, capital lock-up time, milestone/evidence duration and absolute interest under fixed terms separately from risk-premium/WACC sensitivity. Neither paper demonstrates a lower financing rate.
- **INV-029:** cheaper energy/material inputs can be candidate enabling levers only; neither study demonstrates data-center-to-phone physical compression or phone-boundary lifecycle economics.
- **INV-034/035:** these are cost-model and process-model contributions, not alternative fundamental laws. Current physics remains binding; any generated equation or new constitutive relation must pass the established falsification and independent-validation ladder.

## Falsifiable follow-up gates

### BIO-TEA-001 — replicate then specialize

1. Reproduce the published model's declared basis and key mass/energy/cost outputs from available primary data or a fully specified input table.
2. Freeze a separate Pangola/residue dataset with moisture, composition, preprocessing energy, yield uncertainty and logistics.
3. Distinguish raw bio-oil from accepted upgraded liquid fuel; account for upgrading hydrogen/catalysts, utilities, separations, CAPEX/OPEX and financing.
4. Run sensitivity and break-even analysis with no coproduct credit, then add only separately evidenced net saleable coproduct credits.
5. Reject an ultra-low-cost claim if accepted fuel specifications, energy balance, mass balance, cost boundary or independent reproduction fail.

### FUS-ECON-001 — reconcile normalized gain with full plant economics

1. Freeze the `Q_econ` equation, variables, units, control surface and assumptions from the source before implementing it.
2. Independently calculate `Q_econ` on small hand-checkable cases and verify limiting cases; retain cases where `Q_econ >= 1` while omitted lifecycle costs still prevent a commercial conclusion.
3. Crosswalk every included term against FUS-001 and FECONs/pyFECONs, identifying duplicated, omitted and architecture-specific accounts.
4. Sweep component lifetime/fluence, capacity factor, recirculating power, construction duration and financing uncertainty. Preserve uncertainty intervals rather than single-point optimism.
5. Keep net delivered electricity, full lifecycle cost and commercial viability as separate acceptance gates. No commercial claim is accepted from `Q_econ` alone.

Both follow-ups are proposed and **NOT EXECUTED** in this cycle. No laboratory work, fuel sale, fusion plant, provider, QPU, paid model API, purchase or funding action was used.
