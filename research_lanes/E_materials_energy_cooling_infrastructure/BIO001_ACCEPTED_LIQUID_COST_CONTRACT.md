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


## 2026-10-30 — HTL–AD–HDO literature comparator

Hussaini et al. (Chemical Engineering Journal: Green and Sustainable 3 (2026), 100080; DOI 10.1016/j.cejgas.2026.100080) is added as an external process-simulation/TEA comparator. It models potato–okra food waste, not Pangola. Treat reported bio-crude yields, HHV, energy recovery, NPV, IRR and payback as model outputs until the source model, supplement and financial assumptions are independently reconstructed. Resolve the reported 36.9 versus 31.6 wt% yield basis and ~US$11.24M deterministic versus ~US$2.79M Monte Carlo mean NPV before transfer. A product HHV/ERR is not net plant energy; count water handling, heat/electricity, HDO hydrogen/catalyst, AD, wastewater, downtime and financing. Do not transfer negative feedstock gate fees or Nigeria-specific 2025 prices to Pangola.

Matched Pangola HTL-versus-pyrolysis comparison must use the same measured feedstock lot and final accepted-liquid specification, close every mass/energy stream, and report credit-free and non-double-counted coproduct cases separately.
