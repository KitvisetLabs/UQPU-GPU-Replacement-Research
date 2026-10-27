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

The source branch's Python 3.10/3.11/3.12 matrix and cold-start handoff audit passed before porting. The original PR #139 was closed as superseded after its additive work was ported onto current main; it is not canonical. Next highest-value gate: collect a traceable Pangola batch with calibrated mass/energy/product acceptance records, then run independent repeat and cost uncertainty analysis. In parallel, FUS-001 remains an architecture-neutral model with no commercial net-electric evidence and FIN-001 must separate principal reduction from rate/WACC claims.


## Exact-head CI failure and repair — 2026-10-27

Main run [#1808](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40495180708) caught a porting omission: the new calculator referenced the accepted-input evidence-class set, but the constant was omitted from the extracted code section. Python 3.11 reported 14 NameErrors with the same root cause; Python 3.10 was cancelled during workflow concurrency and Python 3.12 had not finished at inspection. The constant is added in the follow-up repair commit. The failed run remains in the audit trail; only the repaired head's own exact CI can validate the port. The original PR #139 was closed as superseded after the code/docs were ported onto current main.


## Repair validation update — 2026-10-27

Repair commit [890ec206](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/890ec20616a90ee763e50d28bf79a449fcec7fd4) restores the omitted `_BIO_OIL_INPUT_EVIDENCE_CLASSES` constant. Its Python 3.10, 3.11 and 3.12 matrix jobs passed; autonomous cold-start audit [#1017](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40495417570) passed. Extended QSP/QSVT/Qiskit/reference jobs in core run [#1809](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40495417564) remained in progress at last inspection. The prior run #1808 failure remains in the audit trail. Do not call the full workflow green until those extended jobs conclude.
