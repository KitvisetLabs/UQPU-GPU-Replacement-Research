# FUS-001 maintenance-aware net-electric cost contract

**Date:** 2026-10-30  
**Primary owner:** Lane E  
**Integration owner:** Lane F  
**Evidence class:** MODEL_ONLY_PREREGISTRATION until independently reproduced and calibrated

## Objective

Estimate reliable net delivered electricity and full lifecycle cost for an architecture-neutral fusion plant while exposing maintenance and recirculating-power interactions. Gross fusion power, capacity factor or a headline LCOE alone is not an accepted output.

## Inputs and units

- Gross fusion/thermal/electric power: MW with explicit boundary.
- Thermal-to-electric conversion efficiency: dimensionless, cycle specified.
- Active and passive recirculating loads: MW and fraction of gross output, separately during operation, dwell, maintenance, cooldown and restart.
- Net export power: MW at the grid boundary; integrate hourly to net MWh.
- Availability: time-resolved schedule, not only one annual scalar.
- Component durability: full-power years, neutron fluence or another measured degradation variable, with uncertainty.
- Maintenance: start month/hour, outage duration, frequency, exchange/commissioning time, partial-replacement fraction and remote-handling throughput.
- Component and replacement cost: currency/year/base, cost account, replacement fraction, facility/hot-cell/robotics cost and labour.
- Construction duration, financing terms, working capital, plant life, fuel cycle, cooling, grid interfaces, decommissioning and residual value.
- Electricity-price/market scenario: source, region, year, hourly time series and uncertainty.

## Required outputs

1. Gross and net generation, recirculating energy by subsystem, net delivered MWh and annual time series.
2. Capacity factor and scheduled/forced outage decomposition.
3. Replacement calendar, component life consumption, annualized replacement cost and remote-handling time/cost.
4. CAPEX, construction interest, fixed/variable O&M, fuel cycle, cooling, grid, decommissioning and total lifecycle cost.
5. Net LCOE and marginal market value as separate metrics.
6. Uncertainty intervals, sensitivity, failed scenarios and input provenance.

## Reproduction sequence

1. Reproduce one published Schwartz et al. GenX maintenance case at pinned source/data.
2. Reproduce the one-cent-envelope equation and one 1costingfe example at pinned commits.
3. Independently test gross-to-net power, CRF, IDC, SFF, replacement discounting and limiting cases.
4. Compare availability-only valuation to seasonal maintenance scheduling and full hourly system optimization.
5. Sweep replacement cost/durability, maintenance timing/duration/frequency, recirculating power, maintenance parasitic load, construction time and financing.
6. Keep all outputs MODEL_ONLY until independent reproduction and measured component/plant calibration.

## Guardrails

The published up-to-15% result is a scenario-specific market-value result, not an LCOE reduction. The 1¢/kWh target is a backcasting ambition, not a demonstrated commercial outcome. No plant design, physics solution, material lifetime or net-electric advantage is inferred from a cost model.


## Learning-rate disagreement and source-pinned reconciliation — 2026-10-30

Add Böhnlein et al., arXiv:2606.26536, as an external stochastic comparator alongside the existing Tang et al. Nature Energy analysis. The preprint abstract reports mature-stage mean LCOE values of US$114.6/MWh MCF, US$110.3/MWh ICF and US$143.9/MWh MIF and implied learning rates above 30%. Tang et al. report a 2–8% experience-rate range for the dominant magnetic and laser-inertial designs. These are methodologically distinct external projections, not observed commercial learning curves.

Before scenario use, pin the preprint version/data/code, reconstruct currency/year, FOAK/NOAK definitions, initial CAPEX, deployment doublings, maturity transitions, WACC and uncertainty distributions. Compare matched technology families and cost boundaries; do not average or silently select the more optimistic estimate. Confirm whether the model covers recirculating power, thermal/electric conversion, cooling, component life/replacement, fuel cycle, maintenance/remote handling, grid interface and decommissioning. Any missing term stays explicit and unpriced; it is not zero.

All outputs remain MODEL_ONLY until project-specific engineering evidence exists. A lower assumed WACC is not a UQPU finance result; INV-033 keeps principal, interest, capital lock-up, WACC and risk premium distinct.
