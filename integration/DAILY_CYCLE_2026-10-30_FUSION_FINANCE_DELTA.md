# Daily Eight-Lane cycle — 2026-10-30 — fusion maintenance and R&D finance delta

**Starting main:** cef917ec1b7f0130a5cbe86681695f1c4c33753a  
**Primary lanes:** E (FUS-001) and F (FIN-001)  
**Cross-cutting:** A–D/G/H, FND-001–006, EQN-001–006, INV-025–035  
**Evidence class:** PEER-REVIEWED SCENARIO MODEL + OPEN-SOURCE COSTING MODEL + OFFICIAL WORKING PAPER / NOT REPRODUCED  
**Observed:** 2026-10-30T01:19:26Z

## New source work

1. **Fusion maintenance:** Schwartz et al., *Journal of Fusion Energy* 45:15 (2026), DOI 10.1007/s10894-026-00551-5. Their GenX scenario shows maintenance timing and partial replacement can change market value beyond a simple annual-availability multiplier; the up-to-15% result is scenario-specific market value, not LCOE reduction or measured net output.
2. **Open costing models:** 1costingfe at commit 44434d9fa95a1105621edc9927a8abe587703e81 and one-cent-envelope at commit b317102fcd19ae63ac7a49712ec924ef64d00e33. Both inspected repos declare MIT. The envelope exposes CRF, IDC, SFF, net/gross recirculating fraction, capacity factor, replacement share/interval, O&M and fuel. 1costingfe provides CAS-account cost breakdowns and replacement costing, but its released build disables internal sizing and 0D physics; it costs a supplied operating point. Neither model was executed or independently reproduced.
3. **R&D finance:** Banco de España Working Paper 2628 (2026-09-22) models divergence between internal hurdle rates and financial cost of capital due to undiversifiable innovation risk and imperfect pledgeability. It is a working-paper hypothesis, not UQPU financing data.

## What changed in FUS-001 and FIN-001

FUS-001 now has explicit maintenance timing/frequency, outage/restart, partial replacement, component durability, replacement cost, active/passive parasitic loads during maintenance, recirculating power, seasonal grid value and net delivered MWh requirements. FIN-001 now separately records financed principal, debt coupon/interest, WACC/financial cost of capital, internal hurdle rate, innovation risk premium, collateral/pledgeability, capital lock-up and time-to-evidence.

No project model was run; no plant cost, net electricity, principal, interest, WACC or hurdle-rate reduction was measured. No biomass/Pangola-specific new result was found. The existing 2026-10-29 flash-Joule and R&D delay watches remain the canonical prior sources.

## A–H

- **A:** HEP-EVENET-002 remains source preflight only; no inference reproduction.
- **B:** provider-neutral and no-submit; no QPU job.
- **C:** data/energy/memory boundaries specified; no local data or meter result.
- **D:** no chip/device evidence; component durability requirements remain unmeasured.
- **E:** new maintenance-aware fusion cost drivers and pinned public model sources; no commercial fusion evidence.
- **F:** new hurdle-rate/WACC distinction and tranche-ledger contract; no UQPU financing outcome.
- **G:** remote handling/replacement equipment requirements are now explicit; no yield/throughput/cost-per-good-device result.
- **H:** new source-specific watches, contracts and gaps; strategic model and six-language public plans preserved.

## FND/EQN and invariants

FND-001–006 and EQN-001–006: no new physical measurement, lower bound, primitive, QFT mechanism or equation promoted. Costing equations remain engineering/economic models, not new physical laws.

INV-029: no one-phone physical-compression gate. INV-030: no Pangola substitution. INV-031: no accepted bio-oil. INV-032: maintenance and replacement costs better specified, but no net delivered fusion electricity. INV-033: hurdle rate/WACC/principal/interest separated, but no UQPU reduction measured. INV-034/035 preserved. INV-025/026/027 and the 100M-GPU/universal 100M-unit goals remain falsifiable and evidence-gated.

## GitHub and CI

Batch 140 starts from `cef917ec1b7f0130a5cbe86681695f1c4c33753a`; Batch 139 was newest committed at start. Starting-head cold-start audit #1385 passed; core run #2105 was in progress at last observation. The Batch 140 commit will require its own exact-head Actions. PR #152 remains draft/open; PR #153 remains open/unmerged. WORKLOG.md and RESEARCH_GAPS.md were not overwritten; focused gaps are canonical and aggregate sync debt remains explicit.

## Next gate

Reproduce the Schwartz/GenX maintenance case and the pinned 1costingfe/one-cent-envelope examples. Independently verify the net-electric boundary, recirculating power, component replacement, maintenance schedule, construction interest and all-in lifecycle cost. Populate FIN-001 from actual financing tranches and dated evidence milestones; keep principal, coupon, WACC and internal hurdle rate separate.
