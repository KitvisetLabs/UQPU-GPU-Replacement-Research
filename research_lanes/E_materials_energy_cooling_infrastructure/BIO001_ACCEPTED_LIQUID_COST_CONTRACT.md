# BIO-001 — accepted-liquid cost contract

**Date:** 2026-10-27  
**Primary owner:** Lane E — biomass, materials, energy and infrastructure  
**Accounting/integration owner:** Lane F  
**Status:** MODEL_ONLY CONTRACT / DATA GATE OPEN  
**Stable IDs:** BIO-001, FIN-001, RG-BIO-001, INV-030, INV-031, INV-033–035

## Contract boundary

The product is the final liquid that passes a frozen acceptance specification, not raw pyrolysis condensate or HTL biocrude. Cost outputs are normalized to accepted MJ and, when density is supplied, accepted litre.

The shared implementation is software/uqpu-prototype/uqpu/energy_finance.py:
- BioOilBatchCostInputs and bio_oil_batch_cost record feedstock wet mass/moisture, dry-mass yields, feedstock and preprocessing cost, logistics, hydrogen, catalyst, utilities, other OPEX, plant CAPEX recovery, capacity factor and lifetime.
- Final accepted liquid mass and LHV determine accepted product energy. A rejected batch has zero accepted output and no cost/MJ result.
- R&D/evidence financing principal is accounted separately with simple interest over the declared lock-up period. The caller must declare that this principal is excluded from plant CAPEX; plant capital recovery uses a separate capital-charge-rate scenario. This is not evidence that WACC changed.
- Coproduct credits require distinct stream IDs and net incremental-cost accounting. The accepted-liquid stream cannot also be credited as a coproduct.
- Optional feedstock LHV and utility electricity/heat produce separate energy ledger fields. The helper deliberately does not claim a closed energy balance if inputs are missing.

## Reproducibility

From the repository root, install the prototype package in editable mode, then run:

    cd software/uqpu-prototype
    python -m pip install -e .
    python -m unittest discover -s tests -v

The new test module is software/uqpu-prototype/tests/test_bio_oil_batch_cost_contract.py. The expected initial record is synthetic and used only for regression tests; no Pangola data is embedded or implied.

## Evidence and limitations

Every calculated result is labeled MODEL_ONLY. Input evidence labels are preserved for provenance but cannot promote a calculated scenario to a lab result or commercial claim. No dataset, calibration record, fuel assay, plant quote or financing contract was collected by this change.

## Required next gate

Acquire one traceable Pangola/residue lot and freeze the accepted-fuel specification. Independently record feedstock moisture/ash, every output stream, raw and accepted liquid mass, density/LHV, hydrogen, catalyst, utility energy, rejected fraction, uptime and all cost inputs. Reconcile mass/energy closure within preregistered tolerances and repeat the batch independently before any TEA claim. Compare HTL and pyrolysis only under the same accepted-product and cost boundary.
