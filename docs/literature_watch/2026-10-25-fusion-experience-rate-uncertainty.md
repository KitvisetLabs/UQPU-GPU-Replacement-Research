# Literature watch — 2026-10-25: fusion cost experience rates and component-level uncertainty

**Search date:** 2026-10-25  
**Primary owner:** Lane E — energy, materials, cooling and infrastructure  
**Integration owner:** Lane F — economics, evidence and integration  
**Feeds:** FUS-001, FIN-001, INV-029, INV-032–033; D/G manufacturing co-design; Lane H capital sequencing  
**Evidence class:** LITERATURE_ONLY (peer-reviewed analysis; no UQPU project evidence promoted)  
**Canonical starting main:** 6af8ce896368ed993fe2b8278afa6082e1ecc916

## Executive delta

A targeted search found a peer-reviewed Nature Energy analysis that directly challenges treating optimistic fusion learning rates as a settled input. Tang et al., “Fusion power experience rates are overestimated,” published 2026-03-23, analyze assumptions used in fusion power-plant cost projections and report a broad spread in first-of-a-kind CAPEX estimates, about US$1,400–US$43,000 per kW. The authors attribute substantial uncertainty to low technology readiness and unresolved or untested plant subsystems, including heat extraction, tritium breeding and materials exposed to fusion conditions.

**Genuine novelty for this project:** the source is not a new fusion experiment or a measured commercial cost. It is a warning against collapsing learning-rate assumptions into a single forecast and then allowing that assumption to dominate an LCOE or investment conclusion. FUS-001 should expose learning-rate assumptions by component and scenario, with explicit provenance and uncertainty, rather than treating a generic percentage as a physical or economic fact.

Official publisher page: https://doi.org/10.1038/S41560-026-02023-8

## Evidence class and limitations

- **Source type:** peer-reviewed analysis in *Nature Energy* 11, 926–934 (2026), published 2026-03-23.
- The paper evaluates assumptions and expert/technology evidence; it does not demonstrate a commercial fusion plant or directly measure a universal fusion learning rate.
- Its reported CAPEX range is an uncertainty finding, not a price quotation for a specific architecture and not a levelized-cost-of-electricity result that can be transplanted into UQPU.
- Learning rates depend on component definition, deployment count, production volume, design maturity, supply chain, factory throughput, materials, construction strategy and whether apparent learning is confounded with redesign or scope change.
- A projected reduction in cost per unit does not guarantee lower total lifecycle cost if capacity factor, replacement intervals, maintenance, net electricity, construction duration, financing or decommissioning worsen.
- This paper supplies no evidence of Pangola-derived materials, commercial low-cost bio-oil, UQPU advantage, reduced project WACC or lower economy-wide interest rates.

## Falsifiable follow-up — FUS-LR-001

Extend the architecture-neutral FUS-001 envelope with a component-level learning-rate register. For each component class—magnets, breeding blanket, heat extraction/power conversion, plasma-facing materials, remote maintenance, shielding, fuel cycle and balance of plant—record the unit being learned, deployment count, cost boundary, source/provenance, maturity, uncertainty and whether the assumed change is manufacturing learning, scale, design improvement or scope reduction.

1. Freeze the net-delivered-electricity and lifecycle boundary: recirculating load, capacity factor, construction schedule, component lifetime/replacement, fuel cycle, material damage, maintenance/remote handling, conversion/cooling, grid interface, financing and decommissioning.
2. Run low/base/high learning scenarios with explicit source-backed ranges where available. Keep unknown ranges as UNKNOWN or MODEL_ONLY; do not silently fill them with a generic rate.
3. Prevent double counting between experience curves, component redesign, yield improvements and factory scale-up. Track total installed capacity and total plant count separately.
4. Recompute net delivered MWh, cost per net MWh, replacement outages, NPV/LCOE and financed principal/interest/time-to-evidence. Keep each scenario’s physical and financial assumptions linked.
5. Test whether architecture ranking and cost envelopes remain robust under plausible learning-rate ranges. Compare calibration against relevant historical manufacturing analogs only when the unit, scope and production context are genuinely comparable.
6. Record sensitivity, uncertainty, failed scenarios and the minimum observed evidence needed to update the prior. Independent operating data remain necessary before a model is called commercial evidence.

**Falsifier / decision rule:** if a candidate architecture is attractive only under an unsupported optimistic learning rate, the result stays MODEL_ONLY and does not support a low-cost fusion claim. If ranking and cost envelopes are stable across defensible ranges, learning-rate uncertainty is not the dominant discriminator for that comparison; it is not evidence that fusion electricity is already cheap.

## A–H status and interfaces

| Lane | Current contribution from this review | Boundary / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | No direct workload or algorithm change; remains Priority #1. | Continue the QOS-QSVT feasibility/reference gate independently of fusion economics. |
| B — cloud/QPU/provider integration | No provider change or execution. | Provider-neutral paths remain dry-run first; no paid QPU job without consent and bounded budget. |
| C — memory/state/storage/data movement | No new memory measurement. | Readable classical state and I/O remain explicit functional contracts. |
| D — device/chip/process/fabrication/packaging | Supplies a component list for future material/process requirements. | No qualified fusion material or device result from a cost-analysis paper. |
| E — biomass/materials/energy/cooling | Adds component-level learning-rate uncertainty to FUS-001. | No net reliable delivered fusion electricity or commercial cost result. |
| F — economics/benchmarks/evidence/integration | Links experience-rate assumptions to full lifecycle cost and sensitivity accounting. | No cost-per-net-MWh or investment case promoted without source-backed inputs and validation. |
| G — manufacturing equipment/factory systems | Separates manufacturing learning, yield, throughput and redesign effects. | D/G co-design remains active; no process-window or factory-yield evidence. |
| H — strategy/finance/future industries | Improves capital-sequencing discipline by exposing assumption-sensitive forecasts. | No measured principal reduction, interest-cost result or WACC/rate effect. |

Auxiliary Lane I remains auxiliary and does not replace the permanent A–H architecture.

## INV-029 through INV-035 and foundational/equation-discovery boundary

- **INV-029:** no Data-Center-to-One-Phone capability or physical-compression evidence; no remote infrastructure may be hidden outside the device boundary.
- **INV-030:** no Pangola carbon substitution or elemental-transmutation claim.
- **INV-031:** BIO-001 remains not demonstrated at target cost; no accepted saleable liquid-energy product or full process-cost result.
- **INV-032:** FUS-001 remains an architecture-neutral model/evidence program; no reliable net delivered fusion-electricity result is established here.
- **INV-033:** lower principal and shorter time-to-evidence remain project-level levers; this source does not prove a lower financing rate, WACC or economy-wide rate.
- **INV-034:** this is cost-model and uncertainty research, not new foundational physics.
- **INV-035 / EQN-001–006:** no new equation is proposed. Any equation-discovery tool may help audit model identities and assumptions, but no AI-generated equation or fit becomes a physical law by declaration.
- **FND-001–006:** no thermodynamic-gap, output-information, speed-limit, alternative-primitive, QFT/particle-mechanism or mathematics-first discovery gate is closed by this source.

The permanent root directives 00–06, INV-025/026/027, INV-029–035, the Kanusanan Pongpanna Model, and Thai/English/Chinese/Japanese/Korean/German public master-plan references remain preserved. No physical, commercial, financing or mission-level result is promoted.
