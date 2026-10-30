# Research gap RG-FUS001-MAINTENANCE-NET-COST-001 — maintenance-aware net-electric cost envelope

**Opened:** 2026-10-30  
**Primary owner:** Lane E — biomass/materials/bio-oil/fusion/cooling/infrastructure  
**Economics owner:** Lane F  
**Device/factory interfaces:** D/G  
**Evidence class:** PEER-REVIEWED SCENARIO MODEL + OPEN-SOURCE MODEL AUDIT / NOT REPRODUCED  
**Status:** LITERATURE-ONLY; MODEL REPRODUCTION AND DATA AUDIT OPEN

## Why this gap matters

FUS-001 must optimize reliable net delivered electricity, not gross fusion power or availability alone. Schwartz et al. (2026), DOI 10.1007/s10894-026-00551-5, show in a specific GenX 2050 Eastern Interconnection scenario that maintenance timing and component replacement patterns change plant value; the reported up-to-15% effect is a market-value result, not an LCOE reduction or measured plant output. The 1cFE open models expose net/gross recirculating power, capacity factor, construction-time financing, recurring replacement and O&M variables, but remain model tools with assumptions and exclusions.

## Current source pins and limits

- Schwartz et al., *Journal of Fusion Energy* 45:15 (2026), accepted 2026-01-19; peer-reviewed scenario analysis. Model includes 100 GW net-nameplate fusion capacity, a circa-2050 Eastern Interconnection, GenX hourly dispatch, and scenario-specific active/passive parasitic loads. The selected parasitic fractions are described by the authors as optimistic.
- 1costingfe code commit `44434d9fa95a1105621edc9927a8abe587703e81`, MIT, Python >=3.10, NumPy/Pydantic/PyYAML with optional JAX and tests. The released build disables built-in sizing and 0D models; it costs a supplied physics operating point.
- one-cent-envelope commit `b317102fcd19ae63ac7a49712ec924ef64d00e33`, MIT, generic screening equation. It excludes taxes, decommissioning, land, fuel-price risk, grid/firming costs and heat/other-product revenue.
- The 1cFE residency concluded in September 2026; its models/tools remain available. Its target of sub-1¢/kWh is an initiative backcasting target, not a demonstrated commercial result.

## Required model variables

1. Gross fusion/thermal/electric power and conversion efficiency.
2. Recirculating loads by subsystem during operation and maintenance; distinguish active from passive loads.
3. Net export power and net delivered MWh after cooling, cryogenics, pumps, plasma heating/current drive, tritium systems, maintenance, restart and grid interfaces.
4. Capacity factor and explicit maintenance calendar: outage duration, frequency, start/stop/recommissioning time, seasonal timing and partial versus full component replacement.
5. Component-specific cost, lifetime/durability (including full-power-year/neutron-fluence basis), replacement fraction, replacement facility/hot-cell/remote-handling capital and labour.
6. Construction time, interest during construction, financing rate, working capital, plant life, decommissioning and residual value.
7. Fuel cycle, breeding ratio, tritium processing, materials damage, waste, cooling and balance-of-plant.
8. Hourly/seasonal grid value and firming interfaces; do not confuse marginal market value with plant LCOE.

## Reproduction and falsification sequence

- Pin the GenX source/version, all input data and Schwartz paper case parameters. Reproduce at least one published maintenance case before varying assumptions.
- At pinned 1costingfe and one-cent-envelope commits, run clean installs and the declared tests. Reproduce one documented 1costingfe example and the envelope's published arithmetic check.
- Independently implement the envelope equation and test dimensional consistency, (f\to0), (CF\to0^+), zero replacement share, zero construction time and positive/negative parameter monotonicity where mathematically applicable.
- Compare naive availability scaling against price-aware scheduling and full system optimization. Sweep maintenance block length/frequency, seasonal start, parasitic load during maintenance, replacement cost, component durability, remote-handling time, construction duration and discount rate.
- Report net delivered MWh, annualized replacement cost, LCOE, capital, O&M, fuel-cycle cost, decommissioning, uncertainty, marginal market value and model residuals separately.
- Preserve failed cases and counterexamples. Independent reproduction and source/default audit are required before any model is promoted beyond MODEL_ONLY.

## Open blockers

- Full primary model inputs/defaults and all cost-account provenance have not been audited.
- The 1costingfe release disables internal sizing/0D physics; a supplied operating point is not a validated design.
- The 1¢ Envelope excludes several lifecycle categories and does not describe a specific plant.
- Schwartz's 15% value result is scenario-dependent and cannot be transferred as a generic availability multiplier.
- No measured component lifetime, neutron damage, maintenance duration, remote-handling throughput, recirculating load, net output, energy or plant cost exists in this project.

## Nonclaims

No commercial fusion electricity, ultra-low LCOE, net-electricity advantage, validated fusion architecture, material lifetime, or reduced WACC is demonstrated. All model results remain MODEL_ONLY until validated against measured plant/component data and independent replication.
