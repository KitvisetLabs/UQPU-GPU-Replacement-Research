# Literature watch — 2026-10-24: biomass-oil upgrading must be judged by accepted fuel function

**Accessed:** 2026-10-24  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure  
**Cross-lane consumers:** Lane F economics/evidence; Lane H strategic finance; Lane D/G catalyst, reactor and process-equipment co-design  
**Feeds:** BIO-001, FIN-001, INV-030–033, INV-034/035, EQN-001–006  
**Evidence class:** PEER-REVIEWED EXTERNAL EXPERIMENT + PEER-REVIEWED TECHNO-ECONOMIC MODEL  
**UQPU project evidence promotion:** none  
**Canonical starting main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e

## Primary sources and dates

1. Claus Dalsgaard Jensen, Magnus Zingler Stummann and colleagues, **“Hydrotreating of Bio-Oil from Updraft Pyrolysis of Straw and Its Miscibility with Ultralow-Sulfur Fuel Oil,”** Energy & Fuels 40(16), 8910–8927. Published online 8 April 2026; issue date 23 April 2026. DOI: [10.1021/acs.energyfuels.6c00722](https://pubs.acs.org/doi/abs/10.1021/acs.energyfuels.6c00722).
2. Sergio Martinez-Villarreal and colleagues, **“Multiobjective Optimization of the Hydrothermal Liquefaction of Microalgae for Cost-Effective Advanced Biofuels Production,”** Industrial & Engineering Chemistry Research 65(27). Published online 30 June 2026; issue date 15 July 2026. DOI: [10.1021/acs.iecr.6c00395](https://pubs.acs.org/doi/10.1021/acs.iecr.6c00395).

The first is a peer-reviewed batch-reactor study of straw-derived updraft-pyrolysis oil and hydrotreating conditions. The second combines process optimization, simulation and techno-economic analysis for microalgae hydrothermal liquefaction (HTL). They concern different feedstocks and routes; their numbers must not be transferred to Pangola as if they were Pangola measurements.

## Material delta 1 — upgrading can change the accepted-fuel outcome

The straw-oil study examined 24 hydrotreating experiments over 150–360 °C, 70–130 bar hydrogen pressure, 400–1500 rpm stirring and 2–12 hour reaction times. Higher temperature and hydrogen pressure increased deoxygenation/hydrogenation; higher stirring reduced mass-transfer limitations and suppressed coke formation. The paper reports that hydrotreated updraft oil could become miscible with ultralow-sulfur fuel oil under optimized conditions, while the overall oil yield relative to dry biomass was reported at about 6 wt% for the updraft route versus 18 wt% for the fast-pyrolysis comparison discussed by the authors. Nitrogen in some hydrotreated updraft samples was around 2 wt%, raising a potential NOx concern for marine-fuel use.

**What is genuinely useful:** a liquid product's crude mass yield is not the same as accepted fuel function. Hydrogen severity, mass transfer, coke, heteroatoms, post-treatment and compatibility can dominate whether a product is usable. The experimental result motivates a process-specific acceptance test, not a claim that the tested oil is drop-in finished fuel.

**Limits:** straw is not Pangola; a batch reactor is not a commercial continuous plant; miscibility with a marine fuel blendstock is not equivalent to meeting every finished-fuel specification. The study does not establish Pangola yield, full lifecycle cost, plant availability, commercial saleability, or ultra-low-cost fuel.

## Material delta 2 — maximum yield and minimum fuel cost are different objectives

The microalgae HTL study jointly considered temperature, residence time, product quality, scale and upgrading hydrogen. Its reported scale-specific optima were 287 °C and 30 minutes for the small-capacity case, and 304 °C and 12 minutes for the upscaled case. Compared with yield-based optimization, the authors report modeled minimum-fuel-selling-price reductions of 5.16% and 19.27%, respectively, and up to 4.50% lower hydrotreatment hydrogen demand. Despite the modeled improvement, reported minimum selling prices remained high: 13.04 €/L for the small-capacity case and 3.77 €/L for the upscaled case.

**What is genuinely useful:** process optimization should minimize cost per unit of final accepted fuel/energy under product-quality constraints, not maximize crude-liquid yield alone. Scale can change the optimum, and hydrogen demand is an explicit cost/energy coupling.

**Limits:** these are model/TEA results for microalgae and the paper's assumptions, not a Pangola plant measurement or a universal cost estimate. The reported reductions are not evidence of commercial ultra-low-cost bio-oil.

## Exact project relevance

- **INV-031 / BIO-001:** define the functional unit as a named, specification-accepted final liquid product. Keep crude liquid yield, upgrading yield, final acceptance rate, LHV, hydrogen consumption, catalyst use, utilities and rejected/off-spec fractions separate.
- **INV-030:** process residues and carbon-rich coproducts may be candidate material streams, but their quality and value require independent qualification. Do not infer elemental transmutation or critical-material substitution from these fuel papers.
- **INV-033 / FIN-001:** use the lowest-cost safe experiment that resolves a high-sensitivity parameter before plant CAPEX is committed. A shorter evidence cycle or lower principal can reduce absolute interest under unchanged borrowing terms; these papers do not establish a lower WACC or economy-wide interest rate.
- **Lane D/G:** catalyst selection, reactor mixing, pressure/temperature envelope, materials compatibility, corrosion, heat recovery and continuous-process equipment need an explicit process-window and metrology interface.
- **Lane F:** normalize costs to one accepted litre and to accepted MJ; include feedstock/collection/preprocessing, conversion yield, upgrading, hydrogen/catalysts, utilities, CAPEX/OPEX, uptime, logistics, compliance, working capital, financing and separately qualified non-double-counted coproduct credits.
- **Lane A + INV-034/035:** if equation discovery is used to model yield, upgrading severity or heat/mass transfer, retain known mass/energy balances and physical constraints; compare against a versioned baseline on blind data, counterexamples and independent measurements. Symbolic fit is not a new law.
- **INV-029:** lower-cost liquid energy may be an enabling input to infrastructure, but these papers provide no evidence for Data-Center-to-One-Phone physical compression.

## Falsifiable follow-up — BIO-001-UPGRADE-ACCEPTANCE-001

1. Select and document a defined Pangola/residue feedstock lot; measure moisture, ash, elemental composition, dry mass and preprocessing energy.
2. Freeze a route-specific process boundary and product specification before optimization. Compare candidate conversion/upgrading conditions on the same feedstock batch.
3. Measure dry-feed-to-crude-liquid yield, gas/solid coproducts, hydrogen uptake, catalyst replacement/deactivation, utilities, mass/energy closure, final accepted-liquid yield, LHV, heteroatoms, stability and off-spec fraction.
4. Compare yield-maximizing and accepted-fuel-cost-minimizing settings under equal experimental budgets; hold out conditions or feedstock lots and retain all failed/off-spec results.
5. Compute cost per accepted litre and accepted MJ with CAPEX, uptime, logistics, working capital and financing sensitivities. Report coproduct credits separately and only once.
6. Replicate the selected condition independently before any scale-up or commercial claim.

**Fail conditions:** incomplete mass/energy closure; product fails the preregistered specification; benefit disappears on held-out feedstock/conditions; required hydrogen/catalyst/utilities erase the cost gain; or economics depend on double-counted coproduct credits.

## Integration and current work boundary

The component-resolved BIO-001 accepted-liquid cost ledger is being proposed separately in PR #63; the fusion costing-framework review is being proposed separately in PR #49. Neither is on canonical main at this cycle start. This watch supplies feedstock/process-quality inputs and a falsifiable acceptance gate; it does not duplicate either artifact or claim their changes are merged.

No UQPU material/fuel experiment, commercial process, measured energy/cost result, real-QPU job, new physical law or lower financing rate is claimed. All cloud/provider and paid-execution boundaries remain unchanged.
