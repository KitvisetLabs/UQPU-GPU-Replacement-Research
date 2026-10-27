# BIO-001 — accepted-liquid cost contract

**Date:** 2026-10-27  
**Primary owner:** Lane E — biomass, materials, energy and infrastructure  
**Accounting/integration owner:** Lane F  
**Status:** MODEL_ONLY CONTRACT / DATA GATE OPEN  
**Stable IDs:** BIO-001, FIN-001, RG-BIO-001, INV-030, INV-031, INV-033–035

## Contract boundary

The product is the final liquid that passes a frozen acceptance specification, not raw pyrolysis condensate or HTL biocrude. Cost outputs are normalized to accepted MJ and, when density is supplied, accepted litre.

The shared implementation is `software/uqpu-prototype/uqpu/energy_finance.py`:
- `BioOilBatchCostInputs` and `bio_oil_batch_cost` record wet feedstock/moisture, dry-mass yields, feedstock and preprocessing, logistics, hydrogen, catalyst, utilities, other OPEX, plant CAPEX recovery, capacity factor and lifetime.
- Final accepted liquid mass and LHV determine accepted product energy. A rejected batch has zero accepted output and no cost/MJ result.
- R&D/evidence financing principal is accounted separately with simple interest over the declared lock-up period. The caller must declare that this principal is excluded from plant CAPEX; plant capital recovery uses a separate capital-charge-rate scenario. This does not evidence a WACC change.
- Coproduct credits require distinct stream IDs and net incremental-cost accounting. The accepted-liquid stream cannot also be credited as a coproduct.
- Optional feedstock LHV and utility electricity/heat produce separate energy-ledger fields. The helper deliberately does not claim a closed energy balance if inputs are missing.

## Reproducibility

From the repository root:

    cd software/uqpu-prototype
    python -m pip install -e .
    python -m unittest discover -s tests -v

The regression test fixture is synthetic and used only for contract validation; no Pangola data is embedded or implied.

## Evidence and limitations

Every calculated result is labeled MODEL_ONLY. Input evidence classes do not automatically promote the result. The helper does not authenticate provenance, certify fuel, prove a commercial minimum selling price, establish carbon-material substitution or show an energy/economic advantage. Unknown costs must not be entered as zero; failed acceptance, missing required data, duplicated capital or overlapping coproduct credits block the relevant claim.
