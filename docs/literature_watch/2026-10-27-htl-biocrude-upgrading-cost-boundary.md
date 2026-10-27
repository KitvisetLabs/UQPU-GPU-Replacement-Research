# Literature watch — bio-oil upgrading and accepted-fuel cost boundary

**Date reviewed:** 2026-10-27  
**Primary lane:** E — biomass, materials, energy and infrastructure  
**Evidence/integration owner:** F — reproducibility, energy economics and financing  
**Publication/strategy owner:** H  
**Cross-cutting:** BIO-001, FIN-001, INV-030, INV-031, INV-033–035  
**Evidence class:** peer-reviewed review + peer-reviewed batch experiment; no Pangola reproduction or commercial-cost claim

## Sources and what is genuinely relevant

1. Dimitriadis, Tuler and Bezergianni, “Hydrotreatment Upgrading of Hydrothermal Liquefaction Biocrude toward Advanced Fuels: A State-of-the-Art Review,” *ACS Omega*, published online 2026-10-01. DOI: https://doi.org/10.1021/acsomega.6c05037. This review reinforces that HTL biocrude is an intermediate; downstream hydrotreatment and final fuel acceptance remain inside the process boundary.
2. Jensen et al., “Hydrotreating of Bio-Oil from Updraft Pyrolysis of Straw and Its Miscibility with Ultralow-Sulfur Fuel Oil,” *Energy & Fuels* 40(16), 8910–8927, published online 2026-04-08. DOI: https://doi.org/10.1021/acs.energyfuels.6c00722. The study reports 24 batch hydrotreatment experiments using wheat-straw pyrolysis oil and a sulfided NiMo/Al2O3 catalyst over varied temperature, hydrogen pressure, stirring and residence time. These are experimental data for that feedstock/apparatus, not Pangola data or continuous commercial-scale proof.

The material project delta is an accounting gate, not a fuel breakthrough: raw-oil yield is not accepted-fuel yield. Upgrading severity, hydrogen, catalyst behavior, residence time, utilities and product specification can change accepted output and total cost.

## Implementation boundary

The new batch-level calculator is in `software/uqpu-prototype/uqpu/energy_finance.py` as `BioOilBatchCostInputs`, `BioOilBatchCostResult` and `bio_oil_batch_cost`. It normalizes cost to accepted MJ and, when density is provided, accepted litre. It includes wet/dry feedstock, preprocessing/logistics, hydrogen, catalyst, utilities, other OPEX, plant CAPEX recovery, capacity factor/lifetime, separate R&D principal-lockup interest and disjoint net coproduct credits. Rejected batches cannot claim accepted fuel cost. Outputs are always MODEL_ONLY.

## Limitations

- No traceable Pangola batch has been measured through complete mass/energy closure.
- No project-specific accepted-product assay, density/LHV, catalyst-life, hydrogen/utility-energy or rejected-product dataset is supplied.
- Local feedstock/logistics quotes, verified coproduct markets and commercial CAPEX/OPEX/financing terms remain missing.
- A synthetic test fixture and calculator do not certify fuel quality or demonstrate commercial economics.

## Falsifiable follow-up: BIO-001 / FIN-001

1. Pin one Pangola/residue lot, source records, calibration/assay provenance and frozen acceptance-spec SHA-256.
2. Record calibrated wet feed, moisture/ash, every liquid/solid/gas/aqueous stream, accepted/rejected fractions, final assay, density/LHV, hydrogen, catalyst, electricity, heat and all variable costs.
3. Close mass and energy ledgers within a preregistered tolerance and repeat independently; failed acceptance or unexplained imbalance blocks cost/MJ.
4. Compare HTL and pyrolysis only for the same accepted product and lifecycle boundary. Separate plant CAPEX recovery from R&D capital-lockup interest; do not infer a lower WACC from lower principal.
5. Credit coproducts only with distinct stream IDs and verified net incremental revenue/costs, with no double counting.

**Stop rule:** any claim based only on crude-liquid volume, missing upgrading inputs, failed product acceptance, unknown costs treated as zero, or overlapping coproduct credits is rejected. No commercial ultra-low-cost bio-oil result is established.
