# Lane E/F literature watch — auditable fusion plant costing frameworks

**Accessed:** 2026-10-23  
**Primary owner:** Lane E — energy/infrastructure; Lane F owns economic integration  
**Related invariants:** INV-032, INV-033, FUS-001, FIN-001  
**Evidence class:** OFFICIAL_PREPRINTS / COST-MODEL-METHODOLOGY  
**UQPU evidence promotion:** none

## Primary sources

1. Simon Woodruff, “A costing framework for fusion power plants,” arXiv:2601.21724, submitted 2026-01-29: https://arxiv.org/abs/2601.21724. It documents an ARPA-E-supported evolution from capital-focused scaling studies toward an auditable, standards-aligned chart of accounts and physics-to-economics workflow, implemented in FECONs and released as the open-source pyFECONs framework.
2. Simon Woodruff, Alicia Durham, Alex Higginbottom and Chris Raastad, “Extension of the fusion power plant costing standard,” arXiv:2602.19389, submitted 2026-02-22: https://arxiv.org/abs/2602.19389. It documents extensions for architecture-specific cost drivers across magnetic, inertial and magneto-inertial fusion, probabilistic uncertainty, safety-related scope, and finance/value metrics including NPV, IRR/MIRR and WACC-based annualization.

These are cost-model methods and scenario frameworks, not observed commercial fusion plant performance or measured LCOE. The extension describes a CATF-supported branch and optional modules; UQPU must verify the exact public code/version and license before attempting reuse.

## Genuine methodological delta

The strongest project-relevant contribution is traceability from physics/engineering assumptions through subsystem quantities and standardized accounts into rolled-up capital and annualized costs. The papers emphasize net-electric output as the normalization basis, explicit plant power balance, engineering-constrained geometry, subsystem cost drivers, indirect/owner/financial accounts and uncertainty propagation. This aligns with the permanent requirement that fusion cost analysis cannot be reduced to a single headline LCOE or gross thermal output.

## Limitations and evidence boundary

- Cost outputs depend on architecture, design point, cost bases, maturity, learning curves, materials prices, construction schedule, availability and financial assumptions.
- Fusion power plants do not yet provide a commercial fleet from which a robust fusion-specific reference class can be estimated; reference-class transfers and learning curves require explicit uncertainty.
- A model that is standards-aligned and auditable is not automatically calibrated or validated for every architecture.
- These sources do not demonstrate ultra-low-cost fusion, reliable net delivered electricity, lower project WACC, or an interest-rate reduction.

## Proposed FUS-001 / FIN-001 follow-up

Build a schema crosswalk between FUS-001 and the public pyFECONs baseline account structure before importing any model. Preserve one shared net-electric normalization basis and explicit fields for recirculating power, capacity factor, component lifetime/replacement, fuel cycle, materials damage, maintenance/remote handling, conversion/cooling, grid interfaces, decommissioning, construction schedule, financing and uncertainty. Track all unknown inputs as null with provenance rather than substituting optimistic defaults.

For FIN-001, separately report financed principal, capital lock-up time, milestone/evidence duration, risk-adjusted scenarios and absolute interest under fixed terms. A lower principal may lower absolute interest at unchanged rates; a lower WACC/risk premium requires separate evidence. Do not double-count learning, coproduct or risk adjustments. Validate the crosswalk on published examples and adversarial accounting cases before any scenario is called decision-grade.

## Invariant contribution

This improves the costing/evidence method for INV-032/033 only. It does not advance commercial fuel, net fusion electricity or finance outcomes without validated inputs and an independently reviewed end-to-end model.
