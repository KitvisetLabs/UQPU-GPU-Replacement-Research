# Batch 140 — fusion maintenance economics and R&D finance frontier

**Date:** 2026-10-30  
**Starting canonical main SHA:** cef917ec1b7f0130a5cbe86681695f1c4c33753a  
**Newest committed batch at start:** Batch 139  
**Primary owners:** Lane E (FUS-001), Lane F (FIN-001)  
**Publication/strategy owner:** Lane H  
**Cross-lane interfaces:** A workload cost contracts; B provider/accounting; C data/energy metering; D device/material durability; G manufacturing/remote handling; INV-034/035 cross-cutting  
**Evidence class:** PEER-REVIEWED SCENARIO MODEL + OPEN-SOURCE COSTING MODEL + OFFICIAL WORKING PAPER / NOT REPRODUCED

## 1. Canonical state

Started from the newest main commit and inspected the current charter, invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, permanent root directives, latest committed batches and drafts, focused gaps, evidence, integration manifest and CI. Batch 139 was the newest committed numbered batch at start; Batch 138 remains draft/open in PR #152. PR #153 remains an open pending-main synchronization PR and is not merged. No inaccessible branch/fork audit is claimed complete.

The current starting-head cold-start audit #1385 passed. Core/invariant run #2105 was in progress at the last observation. The previous Batch 139 head had a passing cold-start audit; its Python 3.10/3.11/3.12 unit matrix passed while extended jobs remained in progress. This is not a fully green current-head CI result.

## 2. Literature delta and source audit

Published a new combined watch for:
- Schwartz et al. (2026), DOI 10.1007/s10894-026-00551-5, on scheduled fusion maintenance, component replacement and time-varying electricity-system value.
- The 1cFE open-source 1costingfe and one-cent-envelope models at pinned commits; both inspected repositories declare MIT.
- Chikis, Goldberg and López-Salido, Banco de España Working Paper 2628 (2026-09-22), on internal innovation hurdle rates versus financial cost of capital.

The new source watch records source/date, evidence class, genuine novelty, model assumptions, exclusions, exact FUS-001/FIN-001 relevance and falsifiable follow-up. Existing 2026-10-29 R&D delay/continuation-bias and flash-Joule biomass watches remain canonical; no duplicate was created.

### FUS-001 source findings

The peer-reviewed maintenance paper uses a GenX scenario for a decarbonized Eastern Interconnection circa 2050, 100 GW net-nameplate fusion capacity, 563 resource clusters and 20 zones. It finds that seasonal scheduling can make plant value up to 15% higher than a naive estimate proportional to annual availability; some partial-replacement strategies can outperform one long outage despite lower average availability. The 15% is a scenario-specific market-value result, not a measured LCOE reduction or plant output.

The paper models active and passive parasitic loads and varies passive load during maintenance. The selected loads are described as optimistic relative to contemporary designs. Component replacement cost and blanket durability are model inputs; real neutron damage, remote-handling throughput, hot-cell cost and recommissioning remain unmeasured.

The 1cFE one-cent-envelope model exposes gross capital, cost of capital, construction time, plant life, capacity factor, recirculating fraction, recurring replacement share/interval, fixed O&M and variable O&M/fuel in a generic screening equation. It explicitly excludes taxes, decommissioning, land, fuel-price risk, grid/firming costs and heat/other-product revenue. It is not a specific plant forecast.

The pinned 1costingfe model is a five-layer cost-accounting tool with CAS accounts, sensitivity/backcasting and annualized replacement costs. The inspected release disables built-in sizing and 0D physics models; it therefore costs a supplied operating point rather than proving a self-consistent design. No external test suite or example was run in this cycle.

### FIN-001 source finding

The Banco de España working paper models a gap between internal hurdle rates and financial cost of capital caused by undiversifiable innovation risk and imperfect pledgeability. It shows in its calibrated model that higher innovation risk can lower financial cost of capital while internal hurdle rates remain sticky or rise. This is a working-paper mechanism, not UQPU financing data or evidence of lower WACC.

## 3. A–H status

| Lane | This cycle | Next gate |
|---|---|---|
| **A — Quantum programming/workloads/compiler/runtime** | HEP-EVENET-002 source/runtime/data preflight remains open; no inference reproduction. | Pin checkpoint/data assets and reproduce one bounded task before CPU/GPU/NPU comparison. |
| **B — Cloud/QPU/provider integration** | Provider-neutral routes maintained; no provider/SDK/target job and no paid QPU. | Simulator/dry-run first; no QPU mapping without a matched accepted-output contract. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | EveNet dataset metadata remains source-only; no local bytes/memory. Fusion metering boundaries specified, not measured. | Measure net MWh, recirculating energy, RAM/VRAM and transfer at declared boundaries. |
| **D — Device/chip/process/fabrication/packaging** | No new device result; component durability and neutron damage remain input requirements, not measured. | Connect measured fluence/damage/lifetime to replaceable component specifications. |
| **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure** | Advanced FUS-001 with maintenance calendar, parasitic load during outage, component replacement/durability and open cost-model source pins. No new Pangola/bio-oil result. | Reproduce a published GenX maintenance case and the pinned costing examples; then independently test net-electric cost envelopes. |
| **F — Economics/benchmarks/evidence/energy economics/finance** | Advanced FIN-001 by separating internal hurdle rate, debt coupon, WACC, innovation premium, principal and time-to-evidence. No project financing result. | Build project-level tranche/interest ledger and fixed-terms principal counterfactual; test risk and hurdle-rate effects separately. |
| **G — Manufacturing equipment/software/factory systems** | D/G co-design retained; maintenance/remote-handling requirements are now explicit cost drivers, but no throughput/yield/tool evidence. | Measure replacement/remote-handling cycle time and equipment/facility cost before factory claims. |
| **H — Kanusanan Pongpanna Model strategy/finance/future-industry research/publication** | Published source-specific FUS/FIN watch, contracts and gaps; six-language strategic references and AI-agent/funding context preserved. | Publish only independently reproduced engineering/economic evidence. |

## 4. FND/EQN status

FND-001 through FND-006: no new thermodynamic measurement, output-information bound, matched QSL experiment, alternative physical primitive, QFT/particle mechanism or established mathematics-first theory.

EQN-001 through EQN-006: no new equation promoted. Cost-model equations are audited engineering/economic representations, not replacements for physical laws. The equation-discovery chain and all dimensional/symmetry/conservation/causality/limiting-case/falsification/replication gates remain binding.

## 5. INV-029 through INV-035

- **INV-029:** no Data-Center-to-One-Phone service, physical-compression, energy or lifecycle-cost gate passed.
- **INV-030:** no Pangola-carbon functional substitution or critical-material reduction; no transmutation.
- **INV-031:** no accepted Pangola-derived liquid fuel or commercial-cost result.
- **INV-032:** maintenance, component lifetime, replacement and recirculating power are better specified as FUS-001 variables; no net reliable delivered fusion electricity or commercial LCOE is demonstrated.
- **INV-033:** internal hurdle rate is now explicitly separated from financial cost of capital/WACC and debt interest; no UQPU principal, absolute-interest, WACC or risk-premium reduction is measured.
- **INV-034:** foundational physics/mathematics agenda remains active and evidence-gated.
- **INV-035:** no AI equation or model formula is promoted to a physical law; all physical challenges remain subject to the permanent falsification/validation protocol.

INV-025/026/027, the 100,000,000-GPU goal and universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage moonshots remain falsifiable goals with subsystem-specific equivalent-useful-output contracts. Hilbert-space dimension is not readable classical memory. NPU comparisons require actual neural-workload semantics, quality, precision, latency, throughput, memory/data movement and cost.

## 6. Integration, sync and next gate

New work IDs:
- **FUS-001-MAINT-001** — maintenance-aware net-electric cost contract.
- **FIN-001-RISK-001** — hurdle-rate versus financial-cost-of-capital contract.
- **RG-FUS001-MAINTENANCE-NET-COST-001** — focused fusion gap.
- **RG-FIN001-INNOVATION-RISK-PREMIUM-001** — focused finance gap.
- **INT-20261030-FUSION-FINANCE-DELTA** — machine-readable integration record.

README, integration hub and cold-start manifest are updated. Large append-only WORKLOG.md and RESEARCH_GAPS.md remain untouched; focused gaps are canonical pending safe aggregate reconciliation. No paid QPU job, fusion experiment or hazardous test was performed.

**Next highest-value gate:** reproduce one Schwartz/GenX maintenance case and the pinned 1costingfe/one-cent-envelope examples; audit gross/net power, recirculating loads, component replacement and financing units; then build an independently tested FUS-001 scenario envelope. In parallel, populate FIN-001 with actual tranche/principal/interest/hurdle/WACC/time-to-evidence records. Keep all model-only outputs separate from commercial evidence.
