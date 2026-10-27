# Daily Eight-Lane UQPU research cycle — 2026-10-27 — BIO-001 accepted-liquid cost gate

**Canonical starting main SHA:** bc6140d667168d4d210961bea5c9122777b0c744  
**Primary owner:** Lane E — biomass/materials/energy/infrastructure  
**Integration/evidence owner:** Lane F — benchmarks/economics/reproducibility  
**Publication/strategy owner:** Lane H  
**Evidence class:** peer-reviewed literature + MODEL_ONLY accounting contract tests; no commercial or physical advantage accepted.

## Canonical inspection and preservation

This follow-on started from the current main after Batch 075. The stale BIO-001 branch was based on an older main; its additive calculator/tests and source records were reviewed and ported onto the current canonical head rather than merging stale README/append-only snapshots. The current charter, invariants, goals, README, A–H operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, newest batches/gaps, energy-finance code, lane E track and CI state were inspected.

The six multilingual Thai/English/Chinese/Japanese/Korean/German master-plan references and strategic AI-agent/funding context remain preserved. INV-025/026/027 and INV-029–035 remain in force.

## Implemented contract

Added `BioOilBatchCostInputs`, `BioOilBatchCostResult`, `bio_oil_batch_cost` and `simple_interest_for_capital_lockup` to the shared energy-finance module, plus a focused regression suite. Cost is normalized to final accepted liquid MJ and, if density is supplied, accepted litres. The accounting boundary includes wet/dry feedstock, preprocessing/logistics, hydrogen/catalyst, utilities, other OPEX, annualized plant CAPEX, capacity factor/lifetime, separately allocated R&D principal-lockup interest and disjoint net coproduct credits. Rejected batches cannot claim accepted-fuel cost; outputs remain MODEL_ONLY.

## Literature delta

The watch records the ACS Omega HTL-biocrude upgrading review (online 2026-10-01, DOI 10.1021/acsomega.6c05037) and the Energy & Fuels wheat-straw bio-oil hydrotreatment batch study (online 2026-04-08, DOI 10.1021/acs.energyfuels.6c00722). These justify including upgrading and product acceptance in the boundary; neither is Pangola-specific commercial evidence.

## A–H status

- **A:** no quantum-workload change; shared cost-accounting module only.
- **B:** provider-neutral QPU paths unchanged; no cloud/QPU job.
- **C:** no memory/storage-equivalence claim.
- **D:** no device/material qualification; D/G co-design remains active.
- **E:** BIO-001 accepted-liquid cost contract implemented; Pangola mass/energy/product data remain missing.
- **F:** fail-closed cost boundary, provenance fields and non-overlapping finance/coproduct ledgers added; no commercial TEA accepted.
- **G:** no manufacturing/process/yield result.
- **H:** dated literature watch, gap, batch and strategic links preserved.

## FND/EQN and permanent invariants

FND-001 remains MODEL_ONLY; FND-002 remains a lower-bound path; FND-003 lacks a matched physical control/quantum measurement; FND-004 has no demonstrated alternative primitive; FND-005 has no validated QFT/particle mechanism; FND-006 advances through accounting contracts only. EQN-001–006 remain evidence-gated. INV-029 has no phone-boundary result; INV-030 has no Pangola material substitution; INV-031 has no accepted-fuel or target-cost evidence; INV-032 has no net fusion-electricity result; INV-033 has no measured reduction in financed principal/interest duration or WACC; INV-034/035 remain cross-cutting research principles. No paid QPU job or material experiment was run.

## CI, sync and next gate

The source branch's Python 3.10/3.11/3.12 matrix and cold-start handoff audit passed before porting. The new main commit requires its own exact-head CI; do not infer its result from the old branch. The original stale PR remains unmerged until this main-branch integration is validated. Next highest-value gate: collect a traceable Pangola batch with calibrated mass/energy/product acceptance records, then run independent repeat and cost uncertainty analysis. In parallel, FUS-001 remains an architecture-neutral model with no commercial net-electric evidence and FIN-001 must separate principal reduction from rate/WACC claims.
