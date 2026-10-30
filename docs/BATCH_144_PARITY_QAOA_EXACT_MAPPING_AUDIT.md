# Batch 144 — exact logical/physical parity-map audit for held-out QAOA fixtures

**Date:** 2026-10-30  
**Starting main SHA:** `9f89bc2d4295a17d7c4d51858603e5e98bf8eab6`  
**Newest batch at cold start:** Batch 143, resolved from current README/tree  
**Primary owner:** Lane A; integration owner Lane F  
**Evidence:** SOFTWARE_CONTRACT + MODEL_ONLY_EXACT_SMALL_INSTANCE_REFERENCE  
**Status:** implementation added; exact-head CI pending at publication time. No QAOA optimizer, SDK, target simulation, paid QPU, material, fuel, fusion or financing experiment was performed.

## 1. Canonical preservation

Inspected the current charter, invariants, goals, README, Research Operating System, Open Frontier directive, Kanusanan Pongpananna Model, strategic references, root directives 00/00A/01–06, newest batches, gaps, A–H lanes, integration hub and Actions state. All six public master-plan languages (Thai, English, Chinese, Japanese, Korean and German) and strategic AI-agent/funding references remain preserved. INV-025/026/027 and INV-029–035 remain binding.

Starting-head core [#2138](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/41002150810) passed 15/15 jobs; cold-start audit [#1428](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/41002150777) passed. These validate the starting SHA only; this new commit needs exact-head CI.

## 2. Lane A — exact mapping/reference audit

Batch 143 froze 10 signed-Max-Cut instances (4 train / 3 validation / 3 test) and exact logical references for 688 assignments. This batch adds an independent exhaustive test that:

- reconstructs the direct objective (\max \sum_e w_e(x_u\oplus x_v)) and equivalent QUBO (\min -\sum_e w_e(x_u\oplus x_v));
- reconstructs the edge-parity objective (\min \sum_e(-w_e)z_e+\lambda N_{odd\ cycles}), with (\lambda>2\sum_e|w_e|);
- checks every logical assignment maps to a feasible edge string and decodes to the same cut value;
- exhausts every physical parity string: valid strings decode, invalid strings fail closed;
- compares the direct-QUBO optimum, parity exact certificate and complete frozen argmax set;
- checks the feasible parity-string count (2^{|V|-c}), from cycle-constraint rank (|E|-|V|+c).

New test: `software/uqpu-prototype/tests/test_qaoa_parity_heldout_mapping.py`. This is a correctness/certificate audit, not an optimizer or QAOA performance run.

## 3. Structural resource observations — not device measurements

| Fixture | V / direct qubits | E / parity qubits | Cycle rank | Dense complex128 direct payload | Dense complex128 parity payload |
|---|---:|---:|---:|---:|---:|
| train-star5 | 5 | 4 | 0 | 512 B | 256 B |
| train-cycle4 | 4 | 4 | 1 | 256 B | 256 B |
| train-path6 | 6 | 5 | 0 | 1,024 B | 512 B |
| train-branch6 | 6 | 5 | 0 | 1,024 B | 512 B |
| validation-grid2x4 | 8 | 10 | 3 | 4,096 B | 16,384 B |
| validation-prism6 | 6 | 9 | 4 | 1,024 B | 8,192 B |
| validation-k23 | 5 | 6 | 2 | 512 B | 1,024 B |
| test-wheel5 | 5 | 8 | 4 | 512 B | 4,096 B |
| test-wheel6 | 6 | 10 | 5 | 1,024 B | 16,384 B |
| test-k6-minus-matching | 6 | 12 | 7 | 1,024 B | 65,536 B |

Total logical assignments: 688. Total parity-register basis strings before feasibility filtering: 7072. The payload formula (16\times2^q) is a dense complex128 representation size only, not measured RAM/VRAM/HBM, not readable classical storage, and not a physical memory equivalence.

## 4. Literature surveillance

Fresh searches rechecked symbolic/neural-symbolic equation discovery, AI theorem/proof search, differentiable/physics-informed modeling, automated experiment design, constitutive laws, lower bounds/no-go results, QEC, quantum circuit discovery, biomass, fusion and finance. The initial computing/foundational scan found the main AlphaProof, quantum-circuit co-design, SymbolFit, natural-proof and SPARC sources already indexed. A supplemental finance-specific scan found one new-to-main peer-reviewed article, now recorded in [the FIN-001 literature watch](literature_watch/2026-10-30-flexible-financing-innovation-risk.md):

- Tsoukalas et al., *Science* (2026-10-08), DOI 10.1126/science.aej2213 / arXiv:2605.22763, already covered by the Oct 25/26 formal-proof watches.
- Gu et al., arXiv:2610.22367 (2026-10-15), evaluator-guided LLM quantum-circuit co-design, already covered by the Oct 21 watch.
- SymbolFit v2, arXiv:2607.19750 revised 2026-10-19; state-preparation natural-proof barrier, arXiv:2610.06826; SPARC, arXiv:2609.06887; and neural-QEC decoder work are already represented in main.
- Pan et al. (2026-10-14 early online), “One size doesn't fit all: Flexible financing as a catalyst for innovation,” *Journal of Corporate Finance* 102, 103099, DOI 10.1016/j.jcorpfin.2026.103099, introduces a risk-/collateral-/institution-dependent bank/equity/hybrid financing model and testable R&D subsidy versus guarantee predictions. The full PDF was not retrieved in this pass; no UQPU financing result is inferred.
- The CoSR journal-acceptance versus withdrawn-arXiv status conflict remains tracked; no positive validation is inferred.

No external result was promoted to project evidence or a new physical law.

## 5. A–H status

| Lane | This cycle | Boundary / next gate |
|---|---|---|
| **A — Programming/workloads/compiler/runtime** | Exhaustive logical/physical mapping, direct-QUBO and exact argmax audit added for all 10 fixtures. | Software correctness only; next paired direct/parity QAOA optimizer/sampler, independent SDK/operator checks and target-aware simulation. |
| **B — Cloud/QPU/providers** | Provider-neutral routes preserved. | No SDK target/job or paid execution. |
| **C — RAM/VRAM/HBM/storage/data movement** | Basis-size and dense-statevector payload formulas recorded. | Formula only; no physical memory/I/O measurement. |
| **D — Device/chip/fabrication/packaging** | Cycle-rank and edge-register structure exposed for later phase-gadget co-design. | No native topology, routed depth, device or fabrication evidence. |
| **E — Biomass/materials/bio-oil/fusion/cooling** | BIO-001, Pangola and FUS-001 gaps reviewed. | No material substitution, accepted liquid fuel or net reliable fusion electricity. |
| **F — Economics/benchmarks/evidence** | Direct-QUBO and parity exact references aligned under one signed objective. | No provider price, energy, latency or cost/task measurement. |
| **G — Manufacturing equipment/factory** | D/G co-design retained. | No equipment/process/yield/cost-per-good-device evidence. |
| **H — Strategy/finance/publication** | Batch/report/record linked; six-language plan and strategic AI/funding references preserved. | Strategic context is not technical or financing evidence. |

## 6. Foundational and equation-discovery progress

- FND-001: Batch 141 nonequilibrium thermodynamics remains a resource-boundary/model audit; no full bit-plus-controller measurement was reproduced.
- FND-002: output-information bounds remain active; finite state counts are not readable classical-memory claims.
- FND-003: matched control-versus-QSL measurement remains open.
- FND-004: alternative physical primitives remain hypothesis/theorem gated.
- FND-005: particle/QFT/EveNet remains source/runtime/provenance gated; no inference reproduction.
- FND-006: mathematics-first invention and formal proof tooling remain active; formal proof or symbolic fit does not promote a physical law.
- EQN-001–006: surveillance, benchmark, constraint-aware generation, counterexample/falsification, escalation and equation-to-technology traceability remain active; no AI equation is promoted.

Current physics remains binding for engineering claims. Any challenge must identify the incumbent assumption, alternative equation, dimensions/symmetries/conservation/causality, limiting cases, held-out prediction, counterexample/falsifier, discriminating experiment/proof and independent validation.

## 7. INV-029–035 and legacy moonshots

- INV-029: no Data-Center-to-One-Phone physical-compression, service, energy or lifecycle-cost milestone.
- INV-030: no Pangola substitution or elemental transmutation; only function/minimization/recovery/hybridization/redesign is admissible.
- INV-031: no accepted Pangola liquid fuel or commercial cost evidence.
- INV-032: no net reliable delivered fusion electricity or commercial lifecycle cost.
- INV-033: no measured project principal/interest/hurdle/WACC/risk-premium reduction; principal and rate pathways remain separate.
- INV-034/035: foundations and AI equation discovery remain active and evidence-gated.
- INV-025/026/027: 100,000,000-GPU and universal subsystem moonshots remain falsifiable goals; Hilbert/state-space size is not readable classical memory; NPU comparisons require workload-level semantics and cost.

## 8. Sync and next gate

README, A-lane README, focused RG-QAOA-PARITY-001 gap, integration index, cold-start handoff manifest, WORKLOG and RESEARCH_GAPS were updated. The large append-only files were fetched in full and appended without replacing historical prefixes. Exact-head CI for this commit remains pending.

**Next gate:** paired direct-versus-parity p=1 QAOA on the frozen manifest with 8,192 shots, 32 optimizer evaluations and 10 repetitions per instance/method; exact references for scoring only; independent operator/bit-order/decoder and SDK checks; then target-aware simulation and complete accepted-task resource/cost accounting. No paid QPU job without explicit consent, credentials and bounded budget.


## Supplemental FIN-001 literature delta — 2026-10-30

The new [flexible-financing literature watch](literature_watch/2026-10-30-flexible-financing-innovation-risk.md) records Pan et al. (Journal of Corporate Finance; early online 2026-10-14; DOI 10.1016/j.jcorpfin.2026.103099). It adds an instrument-choice layer to FIN-001 (debt/equity/hybrid, collateral, asset composition, R&D risk, institutional quality, subsidies/guarantees). The article is an external intertemporal model; its PDF, equations and calibration were not independently audited, and no project-specific financing outcome is established. FIN-001 now requires matched milestone cashflows and held-out financing events before any instrument-choice inference.
