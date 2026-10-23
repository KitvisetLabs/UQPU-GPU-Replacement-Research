# INT-20261024-005 — LLM-guided symbolic search and offline experiment-plan gate

**Date:** 2026-10-24  
**Primary owner:** Lane A for the plan validator; Lane H for the literature watch  
**Economics/evidence owner:** Lane F  
**Canonical main base:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Research branch before this delta:** d89e150d4a1d1984450d3f96a4d7b0e93ebbd0ab  
**Status:** SCHEMA IMPLEMENTED / FULL BENCHMARK NOT EXECUTED  
**Evidence class:** SOFTWARE_CONTRACT / UNIT_TEST + LITERATURE_ONLY; no project-science promotion

## Integration decision

The LLM-PySR paper makes search control a distinct experimental variable. UQPU should compare a fixed symbolic-regression configuration, a language-model-guided search controller and (where a runnable comparable implementation exists) a direct formula generator. All candidate retention remains under deterministic typed constraints, held-out tests and counterexample checks; an LLM cannot certify its own output.

Lane A now has a dependency-free offline schema guard in software/uqpu-prototype/uqpu/experiment_design.py. Its regression suite covers valid plans, split-hash separation, unit mismatch, invalid counters, budget overruns, hard-constraint violations, forbidden live modes, energy-null semantics, required planner roles and identical budget caps. An isolated scratch run passed 8/8 tests before commit. Exact-head GitHub Actions remains the required validation gate.

This change does not execute EXP-DESIGN-002 or EQN-002B. No LLM API, Julia/PySR pipeline, instrument, provider or QPU job was run. The reported external results remain literature evidence only.

## A–H review

| Lane | Current status | Integration consequence / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Offline plan-schema guard implemented; 8 scratch tests pass; full experiment-planning comparison not executed. | Exact-head CI, then frozen three-planner comparison with identical budget caps and held-out acceptance. |
| B — cloud/QPU/provider integration | Provider-neutral no-submit boundary preserved; no provider contact or job. | Read-only capability checks remain separate from any execution authorization. |
| C — memory/state/storage/data movement | Split hashes and transfer/reconstruction budgets are explicit; no memory equivalence. | Count output bytes, precision, transfer, reconstruction and persistence against accepted useful-output semantics. |
| D — device/chip/process/fabrication | No device/process evidence from equation-search literature. | Convert any surviving model to device requirements only after a mechanism-specific discriminating test; maintain D/G co-design. |
| E — biomass/materials/bio-oil/fusion/cooling | BIO-001 lacks a Pangola-specific closed mass/energy/saleable-liquid certificate; FUS-001 remains a model envelope without net-delivered-electricity evidence. | Reuse the method only with accepted liquid-energy or net-electric functional units; no material/fuel/fusion claim. |
| F — economics/evidence/integration | Exact matched resource caps and unknown-energy handling are encoded; no accepted-result economics measured. | Count generator/controller/search/evaluator failures, retries, replay and reconstruction in cost per accepted discriminating result. |
| G — manufacturing equipment/software/factory | Downstream blocked; no process-window/yield evidence. | D/G co-design stays tied to measured device constraints, not formula size or fit score. |
| H — strategic/finance/publication | Dated source watch and cross-lane interface recorded; no financing result. | Maintain source provenance and require independent replication before capital escalation. |

## Foundational and equation-discovery status

- **FND-001:** no matched physical energy/duration experiment added; any unmeasured energy remains null.
- **FND-002:** observable, precision and reconstruction remain separate; a formula or state-space size is not readable storage.
- **FND-003:** no matched control-vs-quantum-speed-limit experiment added.
- **FND-004:** no alternative physical primitive or credible anomaly established.
- **FND-005:** QFT/particle work remains model-scoped and must trace to a distinct observable/device consequence.
- **FND-006:** search controller is a candidate method layer; formal proof and empirical model adequacy remain separate.
- **EQN-001:** new public source/date/evidence-class record added.
- **EQN-002:** search-controller comparison proposed; not executed.
- **EQN-003:** typed units and hard constraints are validated as plan metadata, not as proof of candidate truth.
- **EQN-004:** held-out hashes and falsifiers are required; a full counterexample engine remains open.
- **EQN-005:** no formal proof or new-law promotion; proof status must map to explicit assumptions.
- **EQN-006:** no device/system/economic consequence is inferred from this software contract.

## INV-029 through INV-035

- **INV-029:** no physical-compression or phone-boundary closure; only the evidence workflow is tightened.
- **INV-030:** no Pangola material qualification; no elemental transmutation.
- **INV-031:** no saleable bio-oil mass/energy/cost result.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no financed-principal, interest, risk-premium or WACC result; accounting requirements remain explicit.
- **INV-034:** the mathematics-first search remains open, but present physical constraints remain binding.
- **INV-035:** generator/controller/evaluator/proof/experiment roles remain separate; no AI-generated equation is promoted to a physical law.

## Preservation and synchronization

The eight permanent top-level directives, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, six-language Thai/English/Chinese/Japanese/Korean/German public master-plan links, strategic AI-agent/funding references, INV-025/026/027 and the A–H architecture remain intact. The repository also has a separate Lane I extension; it does not replace or silently renumber A–H.

Canonical main remains c7b5958af58fad04a101ef5c6abf6a29293c867e. This delta is being added to PR #53 and remains branch-only until reviewed/merged. Open PRs #48–#51 have overlapping changes in the equation-discovery/test/handoff area; do not merge independently without conflict-aware reconciliation and exact-head CI. WORKLOG.md, DECISIONS.md and RESEARCH_GAPS.md are large append-only canonical files; they are not partially overwritten. Sync debt remains until a reconciled merge permits a safe dated append.

## Next highest-value gate

Pass exact-head prototype/invariant and cold-start handoff CI. Then freeze and execute the offline three-planner benchmark using immutable data/simulator/configuration hashes, matched compute and evaluation caps, held-out extrapolation and non-identifiability controls, and independent replay. If the required AI planner/runtime or full resource accounting is unavailable, keep the comparison NOT EXECUTED rather than substituting a hand-written plan and calling it an AI result.

No paid QPU execution is authorized.
