# Research gap — RG-BIO-001: accepted-liquid mass, energy and full-cost closure

**Opened:** 2026-10-27  
**Primary owner:** Lane E — biomass, materials, energy and infrastructure  
**Evidence/integration owner:** Lane F — economics and reproducibility  
**Status:** OPEN / MODEL_ONLY CONTRACT IMPLEMENTED / PANGOLA DATA MISSING  
**Related:** BIO-001, FIN-001, INV-030, INV-031, INV-033–035, RG-005, RG-006.

## Objective

For a traceable Pangola or agricultural-residue batch, determine the cost per accepted litre and per accepted GJ/MJ of final liquid fuel after the complete conversion/upgrading path, while closing the batch mass and energy ledgers and preserving source provenance.

## Current implementation

The batch-level contract is implemented in software/uqpu-prototype/uqpu/energy_finance.py as BioOilBatchCostInputs, BioOilBatchCostResult and bio_oil_batch_cost. It records wet feedstock and moisture, dry-feed basis, raw-oil and accepted-liquid yields, final liquid LHV/density, feedstock/preprocessing/logistics, hydrogen, catalyst, utilities, other OPEX, plant CAPEX recovery, capacity factor, explicit R&D principal/lock-up interest, and coproduct net credits with distinct stream IDs.

The calculator fails closed when acceptance metadata or SHA-256 specification identity is missing, a rejected batch claims accepted liquid, R&D principal overlaps plant CAPEX, or coproduct credits lack distinct stream IDs/net incremental-cost accounting. Calculated results are always labeled MODEL_ONLY; the code does not authenticate data, certify fuel quality, or demonstrate commercial economics.

## Literature basis and evidence class

- Dimitriadis, Tuler and Bezergianni, ACS Omega, published online 2026-10-01, DOI 10.1021/acsomega.6c05037: review of hydrotreatment upgrading for HTL biocrude.
- Jensen et al., Energy & Fuels, published online 2026-04-08, DOI 10.1021/acs.energyfuels.6c00722: batch hydrotreatment of wheat-straw pyrolysis oil.

These sources justify including the upgrading boundary; they do not supply Pangola-specific accepted yield, complete energy closure, commercial CAPEX/OPEX, or project finance terms.

## Blocking unknowns

- No traceable Pangola lot has been measured through a complete feedstock-to-accepted-liquid batch balance in this project.
- No raw liquid/aqueous/solid/gas mass closure, final product assay, density and LHV record is attached.
- Hydrogen consumption, catalyst lifetime/replacement, utility energy, process uptime and rejected-product rates are unmeasured for a project-specific route.
- Local delivered feedstock/preprocessing/logistics prices and validated plant CAPEX/OPEX remain missing.
- No independently verified coproduct revenue or financing terms exist for a commercial Pangola plant.

## Unlock and falsifier

Unlock only after raw source records, calibration/assay provenance and the exact acceptance specification are pinned; mass balance closes within a preregistered tolerance; accepted liquid passes the stated specification; an independent repeat batch reproduces yields within declared uncertainty; and the cost model uses non-overlapping cost and coproduct ledgers. A failed quality gate, unexplained mass imbalance, omitted upgrading input or double-counted coproduct rejects the accepted-fuel cost claim.

## Next action

1. Freeze one feedstock lot, acceptance-spec hash and batch protocol.
2. Record calibrated feed and all output-stream masses, moisture/ash, LHV, density, hydrogen, catalyst, electricity, heat, rejected fraction and all variable costs.
3. Run cd software/uqpu-prototype && python -m unittest discover -s tests -v for contract regression tests; add the measured record only after independent data review.
4. Compare HTL/pyrolysis only on the same accepted-fuel function and financing boundary.
