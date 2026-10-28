# Batch 100 — uncertainty-aware symbolic discovery for binned HEP fits

**Date:** 2026-10-28  
**Starting main SHA:** `28de5409eeac3e0244ee9231652eecec4c059da`  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** Lane F — evidence/resource/uncertainty accounting; Lane H — literature/publication  
**Cross-cutting:** INV-034 / INV-035; FND-001–006; EQN-001–008; BIO-001; FUS-001; FIN-001  
**Evidence class:** LITERATURE_ONLY + PREREGISTRATION_PROTOCOL; no independent reproduction  
**Execution boundary:** no UQPU benchmark, no real QPU, no paid cloud job, no material/fuel/electricity experiment

## 1. Canonical start and repository audit

The cycle started from the latest observed main commit rather than a fixed batch number. It inspected `PROJECT_CHARTER.md`, `VERSION_INVARIANTS.md`, `GOALS.md`, `README.md`, `docs/RESEARCH_OPERATING_SYSTEM.md`, `docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md`, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, the eight high-visibility root directives (`00`, `00A`, `01`–`06`), Batch 099 and its literature watch, Batch 098, Batch 097, the current RG-EQN-008 gap, the schema-v4 matched-comparison code/tests, Lane A equation-discovery track, cold-start handoff manifest, `WORKLOG.md`, and `RESEARCH_GAPS.md`.

The latest commit's combined-status query returned no status entries; the available workflow-run connector returned no applicable runs because its wrapper only exposes PR-triggered runs. Therefore exact-head CI at cycle start is **UNVERIFIED**, not green. The prior README records that cold-start audit #1184 passed on Batch 099 commit `b25c5fac504295fbede3a83d044203081fa10514`, while core/invariant run #1934 was still in progress at the last recorded observation. Those results do not automatically transfer to the newer head.

The six-language Thai/English/Chinese/Japanese/Korean/German master-plan links and recorded strategic AI-agent/funding context remain in `STRATEGIC_PLAN_REFERENCES.md`. Strategic intent is not treated as scientific, commercial or financing evidence.

## 2. Fresh literature surveillance

A repository search found no prior mention of SymbolFit or arXiv:2607.19750. The official arXiv record for Ho Fung Tsoi et al., “Machine Can Automatically Discover Parametric Functions to Model HEP Data,” shows v1 submitted 2026-07-22 and v2 revised **2026-10-19**. Source: https://arxiv.org/abs/2607.19750

The paper describes SymbolFit, a symbolic-regression workflow paired with uncertainty modeling for binned high-energy-physics spectra. Its abstract reports 560 independent seeded runs across seven fit configurations, more than 1,000 candidate functions, fits with chi-squared/NDF near one on CMS/ATLAS Run-2 dijet spectra, and rediscovery of previously used dijet/UA2 functions in 111 runs. These are external author-reported results. Rediscovering known functions is a positive control, not a new-law claim; a good chi-squared/NDF alone does not prove calibrated uncertainty, identifiability, absence of selection bias or physical interpretation.

The dated literature watch records the novelty, limitations, source-date distinction, UQPU relevance and falsifiable follow-up. No external result is imported as UQPU evidence.

## 3. Research decision and protocol delta

Use the existing `software/uqpu-prototype/uqpu/equation_discovery_comparison.py` schema-v4 contract and RG-EQN-008; do not create a parallel generic benchmark interface. Add a **separate task class** `HEP_BINNED_PARAMETRIC_FIT`. Do not pool its scores with general LLM-SRBench equation recovery, active-experiment-design benchmarks, or QPU workload results.

A machine-readable preregistration manifest is published at `research_lanes/A_quantum_programming_runtime/SYMBOLFIT_UNCERTAINTY_PROTOCOL_V1.json`. It pins the required provenance and pre-registration fields, known-function/null controls, minimum 30 shared seeds where feasible, equal hard resource ceilings, uncertainty metrics, stop rules and the explicit non-claim boundary. The JSON was parsed and checked for required fields in the cycle tooling; this is not a repository CI run or scientific benchmark.

Required metrics include held-out predictive score, nominal interval coverage, interval width, proper predictive score, parameter/function stability, residual diagnostics, false positives/false discoveries on null controls, counterexamples, constraint violations and total training-plus-inference resources/cost. Coverage tolerances, primary endpoint and paired analysis must be preregistered before unblinding. Wide intervals cannot win solely by achieving coverage.

## 4. A–H review

| Lane | Status this cycle | Next gate |
|---|---|---|
| **A — programming/workloads/compiler/runtime** | **Advanced: protocol/preregistration** | Verify exact source/data/license bytes; implement and test uncertainty-calibration metrics on synthetic known-function and null controls. Continue Priority-1 provider-neutral lowering and exact signed-Max-Cut reference/target-aware simulation in parallel. |
| **B — cloud/QPU/provider integration** | Maintained | Keep provider-neutral IBM Quantum, Braket, Azure Quantum, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging-provider paths dry-run-first. No paid job authorized. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Maintained | Count raw-data bytes, state preparation, addressability, I/O, transfer, reconstruction, host compute, memory and storage; state-space dimension is not readable classical memory. |
| **D — devices/chips/process/fabrication/packaging** | Maintained | Any later equation-derived process claim must bind to measured process windows, metrology, yield, reliability and packaging. |
| **E — biomass/materials/bio-oil/fusion/cooling/infrastructure** | Maintained; gates open | BIO-001 still needs accepted-liquid mass/energy/yield/upgrading/full-cost evidence; FUS-001 still needs reliable net delivered electricity and lifecycle cost. SymbolFit supplies neither. |
| **F — economics/benchmarks/evidence/integration** | **Advanced: uncertainty acceptance protocol** | Match total resources and one cost basis; report training plus inference, failed runs, uncertainty calibration and cost per accepted candidate. No economic advantage measured. |
| **G — manufacturing equipment/software/factory systems** | Maintained; continuous D/G co-design | Preserve D/G co-design; connect future process models to metrology, defectivity, yield and cost per good die/package. No factory result. |
| **H — strategic/finance/future industries/publication** | Advanced: literature publication and handoff | Publish source synthesis and preserve multilingual strategy/funding references as context, not evidence. |

All 28 unordered A–H interfaces remain in scope; INV-034 and INV-035 feed all lanes. D/G co-design remains continuous. No lane was suspended.

## 5. Foundations, invariants and cross-pillar implications

- **INV-029:** no change to the Data-Center-to-One-Phone objective. The US$10T–US$100T range remains an ambition-scale proxy; the required physical-compression capability/service, energy, reliability, form-factor and lifecycle-cost contract remains unmet.
- **INV-030:** no material-substitution evidence. Carbon can functionally substitute, minimize, recover/recycle, hybridize or enable redesign; it cannot transmute elements.
- **INV-031:** no accepted biomass liquid-energy/fuel or commercial-cost evidence.
- **INV-032:** no reliable net fusion electricity or lifecycle-cost evidence.
- **INV-033:** no financing-rate/WACC result. Lower financed principal can reduce absolute interest at unchanged terms; any rate or risk-premium effect requires separate evidence.
- **INV-034:** mathematics-first frontier work remains active, including FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/particle mechanism scans and FND-006 mathematics-first invention.
- **INV-035:** SymbolFit motivates testing uncertainty and selection stability; it does not change a physical equation. Any future physical candidate must still pass dimensional/symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search, proof/experiment and independent validation.

EQN-001–008 remain evidence-gated. No change is made to `fundamental_limits.py`, `frontier_hypothesis.py` or `equation_discovery.py`; no new law or bound is inferred.

INV-025/026/027 remain preserved. The 100,000,000-GPU and universal 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage goals remain falsifiable moonshots requiring subsystem-specific equivalent-useful-output contracts. NPU comparison still requires real neural-task semantics, quality, precision, latency, throughput, memory/data movement and total cost, not TOPS alone.

## 6. Evidence, gaps and exact next gate

**Positive evidence:** the official source exists and was revised 2026-10-19; the project now has a task-separated, machine-readable preregistration protocol and a literature watch. The manifest passes JSON parsing and required-field checks.

**Negative / missing evidence:** no source-code or dataset bytes have been independently verified; no matched run or uncertainty-calibration test was executed; no method winner, new physical law, QPU advantage, energy/material/fuel/electricity benefit or commercial result is established. Exact-head GitHub Actions remains unverified until the relevant runs can be inspected.

Next highest-value gate:
1. Verify the exact SymbolFit code, data, license and acquisition artifacts by bytes and freeze their hashes.
2. Add unit tests for interval coverage, interval width/proper-score joint acceptance, null-control false positives and failure retention.
3. Run deterministic synthetic known-function and null controls before any real HEP data comparison.
4. If controls pass, preregister a blind, group-disjoint, >=30-seed matched comparison under identical resource ceilings and one cost basis.
5. Continue the higher-priority signed-Max-Cut provider-neutral lowering/reference/target-aware simulator gate; do not let this literature protocol displace Lane A's primary computing path.

**CI/synchronization:** the latest observed starting head is `28de5409eeac3e0244ee9231652eecec4c059da`. Starting-head combined status had no entries and the available workflow-run query had no applicable runs; this is not a green result. Every created commit carries the repository-required `Research-Sync: main` trailer. The final README/worklog/gap synchronization must be checked on the resulting head.
