# Literature watch — biomass-carbon functional transfer and thermochemical pathway economics

**Date reviewed:** 2026-10-30  
**Primary owner:** Lane E — materials, biomass, energy and infrastructure  
**Interfaces:** D/G device and manufacturing requirements; F cost/evidence; H industrial strategy; BIO-001; INV-030/031  
**Evidence class:** PEER-REVIEWED EXTERNAL STUDIES / NOT REPRODUCED FOR PANGOLA BY UQPU  
**Work item:** MAT-PANGOLA-CARBON-001  
**Canonical focused gap:** `docs/RESEARCH_GAP_PANGOLA_CARBON_THERMOCHEMICAL_TRANSFER_2026-10-30.md`

## Sources and genuine delta

### 1. Woodchip thermochemical pathway comparison

Ikhwan et al., “Enhancing woodchip utilization through resource circulation: environmental and economic trade-offs among thermochemical pathways,” *Bioresource Technology* 464 (2026), 136053, online 2026-10-11. Official PubMed record: https://pubmed.ncbi.nlm.nih.gov/42860226/ ; DOI: https://doi.org/10.1016/j.biortech.2026.136053

The paper compares combustion, pyrolysis and carbonization using process simulation, gate-to-gate CO₂ accounting and techno-economic sensitivity analysis. The abstract reports a trade-off: combustion is economically favored under its assumptions but has the highest CO₂ emissions; pyrolysis benefits from biochar sequestration but is constrained by biochar value; carbonization produces a higher-value carbon-black-like stream and has the lowest CO₂ result in the evaluated comparison. Its scenario estimates net income of about US$13 per tonne of woodchips at a carbon-black price of US$0.940/kg, with carbonization becoming economically comparable to combustion at US$1.42/kg.

These are model-specific scenario results for woodchips, not observed Pangola economics. Gate-to-gate boundaries, product specifications, carbon accounting and assumed prices must be checked before transferring the values.

### 2. Catalyst-assisted graphitization of biomass carbon

Hegazy et al., “Metal-carbide-assisted graphitization of biomass carbon and its impact on electrical and textural properties,” *Biomass and Bioenergy* 211 (2026), 109142, published 2026-03-02. Institutional repository with abstract and open-access link: https://oulurepo.oulu.fi/handle/10024/61213 ; DOI: https://doi.org/10.1016/j.biombioe.2026.109142

The study uses spruce bark and hydrothermally carbonized carbon, not Pangola. It reports Fe/Mo-assisted formation of metal-carbide intermediates and improved graphitic ordering; the repository abstract reports Raman (I_D/I_G) decreasing from 1.97 to 0.79 for the Mo condition, conductivity rising from 14 to 30 S/cm, and O/C falling from 0.49 to 0.03. Those figures are source-reported values for the tested material and conditions. They do not establish device-grade graphite, long-term stability, semiconductor compatibility or cost-effective substitution in UQPU hardware.

The two sources are complementary but not directly comparable: one is a pathway-level woodchip TEA/LCA; the other is a spruce-bark material-characterization study. Neither validates Pangola-to-technology material substitution.

## Exact UQPU / INV-030 relevance

- Pangola/agricultural residue remains a candidate feedstock, not a qualified material.
- Functional substitution must name the target component and accepted property envelope: e.g. conductivity/resistivity at defined geometry, thermal/electromagnetic performance, mechanical stability, purity/contamination, lifetime and manufacturability.
- Fe/Mo catalysis is not elemental transmutation. Catalysts introduce material cost, recovery, contamination and lifecycle burdens; do not claim that carbon creates or replaces metal atoms.
- Carbon-black-like material, graphitic carbon, electrode carbon, conductive filler and semiconductor-grade material are distinct specifications. No cross-category promotion is allowed.
- For BIO-001, any co-produced liquid stream must be costed as accepted liquid-energy/fuel after upgrading. Char/carbon credits cannot be double-counted or used to hide liquid yield/upgrading costs.
- For FUS-001/INV-032, no fusion-material or net-electricity consequence follows until a component-specific requirement and test are defined.

## Cheapest decisive follow-up

1. Define one real target function and reference material before selecting a biomass recipe.
2. Characterize a dry-basis Pangola/residue lot (moisture, ash, C/H/N/S/O, alkali/halogens and trace metals).
3. Run matched untreated/HTC/carbonization controls and a small Fe/Mo catalyst screen; freeze mass/energy balance, temperature/time, atmosphere, washing, catalyst recovery and batch identity.
4. Measure yield, XRD, Raman (I_D/I_G), elemental O/C, conductivity with defined geometry, surface area, residual metals/ash, leaching, stability and repeatability. Include blank and reference-material controls.
5. Calculate cost per accepted functional unit, including feedstock collection/drying, utilities, catalyst make-up/recovery, wastewater, CAPEX/OPEX, rejects, logistics, financing and end-of-life. Report lifecycle boundary and uncertainty.
6. Falsify transfer if the target property envelope is missed, contamination/stability fails, independent batches do not replicate, or catalyst/energy/processing cost removes the advantage.

**Status:** literature-only; no Pangola experiment, material substitution, commercial cost advantage or new physical law is established.
