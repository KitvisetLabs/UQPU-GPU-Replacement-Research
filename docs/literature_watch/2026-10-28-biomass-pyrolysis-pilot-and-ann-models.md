# Literature watch — pilot-scale biomass pyrolysis, biochar recovery and ANN yield modeling

**Date checked:** 2026-10-28  
**Primary owner:** Lane E — biomass, materials, bio-oil and infrastructure  
**Evidence/integration owner:** Lane F — mass/energy/cost accounting  
**Method interface:** Lane A — temporal holdout and model generalization  
**Evidence class:** PEER-REVIEWED LITERATURE + AUTHOR-REPORTED PILOT DATA + MODEL-ONLY TEA  
**Related:** INV-030/031, BIO-001, FIN-001, FND-006, EQN-001–010

## Source 1 — pilot-scale dual-fluidized-bed pyrolysis

Yang et al., “Pilot-scale biomass pyrolysis dual fluidized bed with in-situ biochar recovery for high-quality bio-oil and negative carbon emissions,” *Bioresource Technology* 459 (2026), 135235. Online publication: 2026-06-24. DOI: https://doi.org/10.1016/j.biortech.2026.135235. PubMed record: https://pubmed.ncbi.nlm.nih.gov/42341955/.

### Reported result and genuine novelty

The authors report a 1 tonne/day pilot-scale pine-sawdust pyrolysis-separation dual-fluidized-bed system. Continuous operation at 500 °C produced 61.5 wt% bio-oil and 13.2 wt% recovered biochar; the paper reports very low solids/ash in the liquid and states that its bio-oil met the study's cited ASTM D7544 Grade D indicators. An Aspen Plus/techno-economic scenario with 90% biochar recovery reports heat-carrier regeneration exergy efficiency rising from 26.8% to 49.6%, avoided biochar-combustion CO₂ of 54.2%, a modeled minimum bio-oil selling price decreasing from 1.14 to 0.94 CNY/kg, and a five-year payback.

The project-relevant novelty is the explicit coupling of in-situ char recovery, process heat integration and saleable-liquid quality rather than treating crude liquid yield as the sole objective.

### Limits

- The feedstock is pine sawdust, not Pangola grass or a locally measured agricultural-residue blend.
- The minimum selling price and payback are model outputs under the authors' process, finance and coproduct assumptions, not independently verified market prices or a guarantee of commercial economics.
- A cited Grade D pyrolysis-oil specification is not interchangeable with every finished transport-fuel specification. Upgrading, hydrogen/catalyst demand, product acceptance, logistics and financing must remain explicit.
- The negative-carbon result depends on the modeled biochar recovery/use and emissions boundary; it is not a universal property of pyrolysis.

## Source 2 — ANN-assisted thermokinetic model for bagasse pyrolysis

Sudha, Saravanakumar and Raj, “Artificial neural network-assisted thermokinetic modeling of sugarcane bagasse fast pyrolysis for enhanced bio-oil production,” *Bioresource Technology* 453 (2026), 134690. Epub: 2026-04-21. DOI: https://doi.org/10.1016/j.biortech.2026.134690. PubMed record: https://pubmed.ncbi.nlm.nih.gov/42025881/.

The authors report a rotary-screw reactor handling 50 kg/h of sugarcane bagasse at below 20% moisture and 500–600 °C, with 30–38 L/h bio-oil and a reported maximum yield of 75% under a stated particle-size/residence-time regime. Their ANN reports R² of 0.958 for bio-oil yield and 0.941 for biochar yield, with RMSE below 2 wt% over the evaluated range.

The model's reported fit is not evidence of future-time, feedstock-family or scale generalization. Mass-yield and volumetric-throughput figures require a common moisture/dry-mass basis and measured liquid density before being combined in BIO-001. The repository did not reproduce the model or independently inspect its raw data/code/license.

## Exact UQPU relevance

- **BIO-001 / INV-031:** candidate measurements for mass/energy balance, char recovery, liquid quality and cost-account boundaries. Do not transfer pine/bagasse yields to Pangola without matched characterization and experiments.
- **INV-030:** recovered char may motivate functional carbon-material tests, but no Pangola-derived electronic/structural material performance is established and no elemental transmutation is implied.
- **Lane A / INV-035:** the new temporal-holdout certificate can guard ANN/surrogate comparisons against random-row leakage; add feedstock-family, particle-size, reactor-scale and time-block holdouts.
- **Lane F / FIN-001:** separate measured pilot data from Aspen/TEA scenarios and count CAPEX, utilities, upgrading, hydrogen, catalyst replacement, downtime, logistics, financing and non-double-counted coproduct credits.
- **INV-029:** cheaper accepted liquid energy and recoverable carbon could be enabling inputs, but no phone-class physical-compression evidence follows.

## Falsifiable follow-up

1. Pin the article, data/code availability, licenses, process diagram and all reported basis definitions.
2. Obtain Pangola and residue samples with measured moisture, ash, volatile/fixed carbon and elemental composition; preserve feedstock-lot IDs.
3. Close a dry-feed mass balance and lower-heating-value energy balance across liquid, char, gas, water and losses. Reconcile wt% yield with L/h using measured density and moisture basis.
4. Test a time-block holdout plus leave-one-feedstock-family/reactor-scale-out tests before ANN model selection; compare with a transparent thermokinetic baseline and independent lab measurements.
5. Price final accepted liquid-energy function after required upgrading, hydrogen/catalysts, utilities, CAPEX/OPEX, logistics, financing and defensible coproduct credits.
6. Preserve failed batches and counterexamples. No target-cost or carbon-negative claim is accepted without independent replication and a full boundary.

**Disposition:** actionable literature leads for BIO-001; no UQPU/Pangola reproduction, commercial fuel-price proof or material-substitution result.
