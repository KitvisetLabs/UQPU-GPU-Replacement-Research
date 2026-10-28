# Literature watch — pyFECONs architecture-neutral fusion cost accounts and uncertainty

**Date checked:** 2026-10-28  
**Primary owner:** Lane F — economics, benchmarks, energy economics and integration  
**Technical owner:** Lane E — fusion energy and infrastructure  
**Cross-lane consumers:** D/G (hardware/manufacturing cost drivers), H (strategic finance)  
**Evidence class:** OFFICIAL ARXIV PREPRINTS + PUBLIC REFERENCE-CODE DISCOVERY  
**Related:** INV-032/033, FUS-001, FIN-001, FND-001, EQN-001–010

## Primary sources

1. Simon Woodruff, “A costing framework for fusion power plants,” arXiv:2601.21724, submitted 2026-01-29: https://arxiv.org/abs/2601.21724.
2. Simon Woodruff, Alicia Durham, Alex Higginbottom and Chris Raastad, “Extension of the fusion power plant costing standard,” arXiv:2602.19389, submitted 2026-02-22: https://arxiv.org/abs/2602.19389.
3. Public reference implementation: [Woodruff-Scientific-Ltd/PyFECONs-GoogleColab](https://github.com/Woodruff-Scientific-Ltd/PyFECONs-GoogleColab), described by its repository as a standard costing tool spanning magnetic, magneto-inertial and inertial fusion with IAEA/Gen-IV cost-account structures.

## Genuine novelty for UQPU

The baseline framework moves from older top-down/scaling estimates toward auditable cost accounts connected to power balance, engineering-constrained geometry and bottom-up dominant subsystem drivers. The extension adds controlled driver-specific accounts for MFE/IFE/MIFE, uncertainty propagation for materials prices, technology maturity and learning rates, safety-to-account mapping, regulatory/insurance assumptions, and finance/value metrics including NPV, IRR/MIRR and WACC-based annualization.

This is useful for FUS-001 because it provides a stable accounting vocabulary across architectures while allowing the physics and dominant subsystem drivers to differ. It also offers a disciplined way to carry uncertainty into FIN-001 rather than presenting one deterministic LCOE point as certain.

## Limitations and evidence boundary

- The arXiv papers document costing methods and example analyses; they do not demonstrate that any proposed fusion plant has delivered reliable net electricity at a particular price.
- The cost output remains conditional on design, power balance, recirculating loads, component lifetime, capacity factor, construction schedule, fuel cycle, replacement/remote handling, materials damage, cooling, grid interface, financing and decommissioning assumptions.
- Some detailed engineering, vendor/EPC and megaproject data are proprietary or incomplete; FOAK/NOAK learning rates remain uncertain without deployment history.
- The public repository is a notebook/Colab-centered reference workflow. Its exact revision, dependencies, license, input provenance and reproducibility must be checked before integrating it as a software dependency.
- WACC, discount-rate or learning-curve scenarios are assumptions or model outputs, not evidence that UQPU has reduced a project's market rate or risk premium.

## Exact UQPU relevance

- **FUS-001 / INV-032:** map net delivered electricity and recirculating power to a common denominator; preserve architecture-specific magnet/laser/pulsed-power drivers and common balance-of-plant accounts.
- **D/G co-design:** connect magnet/conductor, laser, pulsed-power, blanket/divertor, power-supply and factory-yield assumptions to measurable quantities, component lifetime and replacement cadence.
- **FIN-001 / INV-033:** separate financed principal, construction duration, working capital, loan tenor and absolute interest from WACC/risk-premium assumptions. A lower principal reduces absolute interest only at unchanged financing terms.
- **INV-029:** reliable low-cost net electricity is an enabling constraint for extreme computing compression, not proof of physical compression.
- **INV-034/035:** a cost model is not a physical law; its engineering inputs and equations remain falsifiable model assumptions.

## Falsifiable follow-up

1. Pin the arXiv versions, public code commit, license, dependencies, benchmark cases and all input-data hashes.
2. Build an adapter that maps FUS-001 fields into the published cost-account structure without dropping recirculating power, capacity factor, construction time, component replacement, fuel cycle, remote maintenance, conversion/cooling, grid connection or decommissioning.
3. Reproduce one public benchmark case exactly before altering assumptions; preserve the published output and input hash.
4. Compare MFE/IFE/MIFE using a common net-electric denominator and explicitly separate FOAK from NOAK. Propagate material, TRL, schedule, learning and financing uncertainty.
5. Audit double counting between contingency, risk, financing and learning factors; report sensitivity and uncertainty distributions rather than a single winning architecture.
6. Treat any modeled WACC change as a scenario until independent financial evidence supports it.

**Disposition:** strong candidate reference framework for FUS-001/FIN-001; no new commercial fusion-electricity or lower-WACC evidence.
