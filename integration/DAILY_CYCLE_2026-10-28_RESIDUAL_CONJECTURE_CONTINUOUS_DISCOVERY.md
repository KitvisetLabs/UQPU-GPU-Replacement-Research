# Daily Eight-Lane integration — 2026-10-28 — equation-discovery method families

**Batch:** 099  
**Starting SHA:** 87d3d332478fac15cf1b1dc76de54de2ff6f284d  
**Status:** literature synthesis and protocol update; exact-head CI repair pending verification  
**Primary owner:** Lane F for integration/evidence; Lane A owns the comparator protocol

## Shared contract

The shared interface remains `software/uqpu-prototype/uqpu/equation_discovery_comparison.py` (schema v4) and its tests. This cycle adds no code or benchmark result. The protocol must distinguish:
- static expression recovery and held-out predictive validity;
- conjecture-level reasoning and interactive experiment design;
- continuous parameterization and post-fit structure recovery;
- search-width/resource allocation from the choice of method family.

Do not pool incompatible benchmark scores. Require authentic retrievable artifact bytes, not hashes alone, and verify record-level group disjointness.

## A–H interface matrix

| Pair | Integration decision |
|---|---|
| A↔B | Method evaluation stays provider-neutral; later QPU tests require target-specific costs and authorized access. |
| A↔C | Candidate/residual tensors, tokens, memory, I/O and reconstruction count toward total resources. |
| A↔D | Equation candidates that alter device models need dimensional/causal checks and measured device evidence. |
| A↔E | Candidate methods may later model biomass conversion or energy subsystems only on appropriate measured data. |
| A↔F | Matched budgets, accepted-output metrics, provenance and full-cost accounting are mandatory. |
| A↔G | GPU-friendly continuous fitting is not itself factory/device evidence; manufacturing constraints stay explicit. |
| A↔H | Published methods become reproducible handoff items, not authority for UQPU claims. |
| B↔C | Provider-specific state limits, transfers and reconstruction remain separated by target. |
| B↔D | Hardware target details and device modality must be pinned for later execution. |
| B↔E | Cooling/power are not inferred from symbolic-regression accuracy. |
| B↔F | No mixed-target probability/pricing economics; preserve target-specific cost bases. |
| B↔G | Provider roadmaps do not demonstrate manufacturing equipment readiness. |
| B↔H | Provider/funding references remain strategic context until verified. |
| C↔D | Memory and data movement constrain device/control architecture; no state-space/storage equivalence. |
| C↔E | Thermal and material models need measured properties and boundary conditions. |
| C↔F | Memory, transfer, retries and reconstruction are cost terms, not omitted overhead. |
| C↔G | Test/metrology data and process-control pipelines have storage/throughput requirements. |
| C↔H | Infrastructure compression must count persistent state and external storage honestly. |
| D↔E | Materials/energy coupling requires functional units and measured properties. |
| D↔F | Device models require yield, lifetime and lifecycle-cost evidence. |
| D↔G | Continuous co-design: process windows, metrology, packaging and yield. |
| D↔H | Device/fab strategy is a roadmap until manufacturing evidence exists. |
| E↔F | BIO-001/FUS-001 need accepted function and full lifecycle economics, not model fit alone. |
| E↔G | Biomass/material process equipment requires mass/energy balance and operability data. |
| E↔H | Feedstock/energy programs may inform industrial strategy, but no commercial claim follows. |
| F↔G | Factory economics need cost per good die/package and validated process/yield data. |
| F↔H | FIN-001 separates principal/time/risk effects from unproven WACC changes. |
| G↔H | Future-industry scale-up remains gated by equipment capability, yield, cost and finance. |

## Foundation and permanent mission boundary

INV-034/035 feed every lane. FND-001–006 and EQN-001–008 remain active. INV-025/026/027 and INV-029–035 remain preserved. The phone-class physical-compression objective, extreme cost multipliers, material substitution, accepted commercial bio-oil, reliable net fusion electricity and lower project WACC are not demonstrated.

## CI repair record

On starting SHA 87d3d332478fac15cf1b1dc76de54de2ff6f284d, core/invariant run #1933 passed while cold-start audit #1183 failed solely for the missing `Research-Sync: main` commit trailer. This integration commit includes that trailer. The new exact-head core and cold-start runs are the acceptance gate; the failure is not marked repaired until the resulting Actions runs confirm it.
