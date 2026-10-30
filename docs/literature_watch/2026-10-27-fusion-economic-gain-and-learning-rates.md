# Literature watch — 2026-10-27: fusion economic-gain accounting and learning-rate uncertainty

**Access date:** 2026-10-27  
**Primary owner:** Lane E (energy/infrastructure); cross-lane owners Lane F (economics/evidence) and Lane H (publication)  
**Evidence class:** `LITERATURE_ONLY`; any future parameter sweep is `MODEL_ONLY` until validated against project-specific evidence

## Sources and dates

1. D. G. Whyte, A. Lo, R. Bielajew, M. Hancock, R. Moeykens et al., “Criteria for the economic viability of fusion power plants,” *Journal of Fusion Energy* 45, article 49, published 2026-07-10. DOI: https://doi.org/10.1007/s10894-026-00577-9. Official publisher page: https://link.springer.com/article/10.1007/s10894-026-00577-9.
2. Lingxi Tang, Bessie Noll, Anurag Panda et al., “Fusion power experience rates are overestimated,” *Nature Energy* 11, 926–934, published 2026-03-23. DOI: https://doi.org/10.1038/S41560-026-02023-8. Official publisher page: https://www.nature.com/articles/s41560-026-02023-8.

## Genuine novelty and complementarity

Whyte et al. propose a technology-neutral economic-gain framework normalized to the surface through which fusion energy is extracted. Its ten normalized controlling parameters include net energy conversion, utilization, surface energy-fluence limit/component life, replacement time and cost, target cost where relevant, financing and energy price. The paper defines (Q_{econ}\geq1) as necessary but insufficient for commercial viability and explicitly notes simplifying temporal-equilibrium assumptions and incomplete real-world cost coverage.

Tang et al. challenge the 8–20% learning-rate range commonly used in fusion cost projections. Using technology-characteristic evidence and expert elicitation for magnetic and laser inertial fusion, they argue that 2–8% is more defensible, with 5% used as an illustrative central case. This is a reason to widen scenario analysis and scrutinize extrapolation, not a measured learning curve for commercial fusion plants.

## Limitations and evidence boundaries

- The economic-gain framework is a screening model, not a validated commercial plant LCOE or investment return.
- Its normalized boundary and temporal-equilibrium assumptions must be reconciled with actual construction schedules, staged commissioning, outages, grid delivery and financing cash flows.
- The learning-rate estimate uses analog technologies and expert judgments because commercial fusion deployment data are absent; uncertainty and technology heterogeneity remain large.
- Neither paper proves fusion is economically viable or impossible. Neither provides project-specific net delivered electricity or commercial cost evidence.
- The papers do not establish a lower project WACC. A lower financed principal reduces absolute interest at fixed terms, while risk premium/WACC changes require separate evidence.

## Exact UQPU/FUS-001 relevance

Use Whyte et al. as a candidate architecture-neutral cross-check for the normalized engineering/cost-driver ledger, not as a replacement for full lifecycle net-electric accounting. Use Tang et al. to prevent optimistic learning assumptions from being silently embedded in future cost scenarios. Preserve gross fusion gain, recirculating power, conversion/cooling, capacity factor, maintenance, component replacement, fuel cycle, remote handling, construction time, grid interfaces, financing and decommissioning as distinct quantities.

## Falsifiable follow-up

Create a source-pinned sensitivity envelope with learning-rate scenarios of 2%, 5%, 8%, 13% and 20%; these are scenario values, not probability weights or forecasts. For each architecture, report assumptions and units for FOAK CAPEX, deployment doublings, construction schedule, utilization, net-electric efficiency, recirculating power, surface/component lifetime, replacement downtime/cost, fuel/blanket cycle, maintenance/remote handling, fixed and variable O&M, grid delivery, financing and decommissioning. Do not double-count heat/fuel coproduct credits or treat gross plasma gain as net electricity.

Acceptance requires a reproducible model, source-linked inputs, sensitivity/uncertainty propagation, independent arithmetic checks, and explicit missing-data flags. Any output built from unvalidated inputs remains `MODEL_ONLY`; it cannot be reported as commercial ultra-low-cost fusion evidence.


## 2026-10-30 supplemental comparator

Böhnlein et al., arXiv:2606.26536 (2026-06-25), now has a separate [stochastic fusion-cost watch](2026-10-30-fusion-stochastic-cost-projections.md). Its abstract reports mature-stage mean LCOE values of US$110–144/MWh across MCF/ICF/MIF and implied learning rates above 30%, while describing the projections as optimistic. This preprint is not a measured plant cost and its learning-rate method differs from Tang et al.'s 2–8% estimate. Keep both source methods separate until FOAK/NOAK, deployment doublings, starting CAPEX, WACC and net-electric boundaries are reconciled; do not average them.
