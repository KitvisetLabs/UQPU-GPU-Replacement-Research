# Research gap — FUS-001 architecture-neutral economic gain and learning-rate sensitivity

**Opened:** 2026-10-27  
**Primary owner:** Lane E — biomass/energy/cooling/infrastructure  
**Cross-lane owners:** Lane F — evidence/economics/financing; Lane H — literature and strategic publication  
**Status:** OPEN / literature-derived model specification only  
**Related:** INV-032, INV-033, FUS-001, FIN-001, RG-FUS001-HIDRA-LI-VAPOR-001

## Objective

Build an architecture-neutral, auditable sensitivity envelope for fusion plant economics that keeps net delivered electricity, component lifetime/replacement, deployment learning and financing assumptions explicit. The objective is not to select a winning fusion architecture from paper scenarios; it is to identify which measured quantities and uncertainty ranges control the net-electric cost floor.

## Pinned sources

- Whyte et al., *Criteria for the economic viability of fusion power plants*, *Journal of Fusion Energy* 45, 49 (2026-07-10), https://doi.org/10.1007/s10894-026-00577-9.
- Tang et al., *Fusion power experience rates are overestimated*, *Nature Energy* 11, 926–934 (2026-03-23), https://doi.org/10.1038/S41560-026-02023-8.

## Model contract

Every architecture row must distinguish:
- gross fusion/plasma gain from net electric power delivered at the grid boundary;
- recirculating power, thermal/electric conversion and cooling loads;
- capacity/utilization factor, availability and construction/commissioning time;
- FOAK CAPEX and financing drawdown, interest during construction and working capital;
- component energy-fluence/lifetime, replacement cost, downtime, remote handling and waste/decommissioning;
- fuel-cycle and breeding/retention costs where applicable;
- fixed/variable O&M, grid connection and delivery constraints;
- coproduct revenue only when separately measured and allocated without double counting;
- principal, financing duration, interest rate and risk premium/WACC as separate variables.

## Preregistered sensitivity grid

Evaluate learning-rate scenarios at 2%, 5%, 8%, 13% and 20% per cumulative deployment doubling. These are a deliberately broad scenario grid, not probability weights or a claim that any one rate is correct. Include at least low/base/high values for initial CAPEX, construction time, component lifetime, replacement downtime, net conversion, recirculating power, utilization and financing. Preserve source and assumption provenance per input.

## Acceptance and falsifiers

1. Independent reviewer reproduces arithmetic and units from the pinned sources.
2. Every cost and energy stream has one boundary and is counted once.
3. Uncertainty propagation is shown; do not report only a point estimate.
4. Scenario rankings must be stress-tested against the learning-rate and component-lifetime assumptions.
5. A result is rejected if it uses gross gain as net electricity, omits recirculating/cooling power, double-counts coproducts, or silently treats a literature assumption as measured plant data.
6. The economic-gain threshold (Q_{econ}\geq1) is only a necessary screening condition under the source model, not proof of commercial viability.

## Evidence class and nonclaims

Current status is `LITERATURE_ONLY`. Any calculated envelope is `MODEL_ONLY` until all critical inputs have independent source evidence and plant-level data support. No commercial fusion plant, ultra-low-cost electricity, reduced WACC or INV-029 milestone is established. For INV-033, lower principal or shorter capital lock-up may reduce absolute interest at fixed terms; lower rates/risk premia require separate evidence.

## Next action

Implement a reproducible scenario-input schema and unit checks after the architecture-neutral cost-driver interface is inspected. Do not overwrite existing FUS-001 work; integrate through its current cost ledger and keep this gap as the source/assumption specification.
