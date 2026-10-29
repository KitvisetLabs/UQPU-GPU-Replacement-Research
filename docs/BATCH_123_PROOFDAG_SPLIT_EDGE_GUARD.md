# Batch 123 — held-out proof-DAG dependency leakage guard

**Date:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** Lane F evidence/split integrity; Lane H provenance and literature; INV-034/035 foundations  
**Evidence class:** SOFTWARE METADATA CONTRACT + 4 NEW SYNTHETIC REGRESSION TESTS  
**Paid QPU execution:** not authorized or attempted

## Starting state and preservation

Started from the dynamically observed main head `210c10042b7ef7579d5345090d9c8a64ae440e0f`, the Batch 122 synchronization follow-up. The required charter, version invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, permanent root directives 00/00A/01–06, Batch 122, its focused FND-006 gap, integration record, validator/tests, living gaps and lane scoreboard were inspected. The six-language Thai/English/Chinese/Japanese/Korean/German plan links and INV-025/026/027 and INV-029–035 remain preserved.

## Lane A finding and change

Code inspection found that the proof-DAG validator checked that parents existed and that theorem-family IDs did not cross declared splits, but it did not constrain dependency edges themselves. A training node could depend on a held-out validation/test node; a test-family node could import a validation fragment from another held-out family. This left a graph-level leakage path despite the existing family/split checks.

The validator now permits:
- training nodes to depend on training nodes;
- validation/test nodes to depend on training nodes; and
- internal proof-DAG edges within the same theorem family and same held-out split.

It rejects dependencies from a training node into held-out data, and rejects cross-family or cross-split edges whose parent is not in training. Reuse of a declared schema remains separately restricted to a verified training-split source with explicit residual premises/closure.

Four regression cases cover: train-to-held-out leakage rejection, validation-to-test cross-family leakage rejection, same-family/same-split internal edge acceptance, and held-out-to-training dependency acceptance.

## Literature surveillance

Fresh public searches revisited symbolic/neural-symbolic equation discovery, formal theorem discovery, physics-informed modeling and quantum thermodynamic bounds. The currently relevant ProofEvolve, SymbolFit/LegoSR/RISR and quantum-feedback/measurement-only thermodynamics sources are already recorded in the repository. No new-to-repository primary result was found that changes this acceptance gate; no duplicate watch article was created. External benchmark claims remain third-party evidence and were not reproduced.

## Eight-lane status

| Lane | Status | Next evidence gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | **Advanced**: held-out dependency-leakage guard plus 4 regression tests | Exact-head CI; pinned theorem-family corpus; equal-budget baseline versus schema-reuse experiment |
| B — cloud/QPU/providers | Maintained; provider-neutral adapters preserved; no paid execution | Simulator/dry-run and provider/target-paired cost-quality evidence |
| C — RAM/VRAM/HBM/storage/state/I/O | Maintained; no classical-memory equivalence inferred from proof-DAG size | Measure peak memory, I/O, transfer, reconstruction and energy in a pinned run |
| D — devices/chips/process/packaging | Maintained; no new device evidence | Continue D/G co-design and require measured process/yield data |
| E — biomass/materials/bio-oil/fusion/cooling | Maintained; BIO-001 and FUS-001 remain open | Pangola function acceptance and full accepted-liquid/net-electric cost boundaries |
| F — economics/evidence/integration | Advanced at split-integrity contract level | Compare cost per independently accepted held-out result under matched budgets |
| G — manufacturing equipment/software/factory | Maintained with continuous D/G co-design | Cost per good device/package, process-window and yield measurements |
| H — strategy/finance/publication | Advanced by reproducible handoff and deduplicated surveillance record | Preserve six-language strategic references; do not treat strategy as scientific/finance evidence |

INV-034/035 continue to feed A–H. This cycle does not claim parallel independent-agent execution.

## Foundational and equation-discovery status

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-quantum-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/particle mechanism scans and FND-006 mathematics-first invention remain active. EQN-001–006 and their broader repository successors remain governed by dimensional/symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search, proof/simulation, discriminating experiment and independent validation. No equation or theorem claim was promoted to a physical law.

## Permanent mission and evidence boundaries

- **INV-029:** no physical Data-Center-to-One-Phone closure; remote-terminal infrastructure remains outside the final physical-compression success condition.
- **INV-030:** biomass carbon remains a functional substitution/minimization/recovery/recycling/hybridization/redesign strategy; no elemental transmutation.
- **INV-031:** BIO-001 accepted liquid-energy/fuel cost remains open; crude bio-oil is not automatically finished fuel.
- **INV-032:** FUS-001 net reliable delivered-electricity cost remains open; no commercial fusion-electricity claim.
- **INV-033:** no measured lower financed principal, interest expense or WACC.
- **INV-034/035:** foundational and AI-assisted equation discovery remain active, falsifiable and evidence-gated.
- **INV-025/026/027:** 100-million-unit replacement and open-frontier targets remain unproven goals.

## Acceptance, limitations and next gate

The new checks are metadata/split-integrity guards, not proof-kernel execution. The existing local clone path was previously blocked by DNS/network access; this cycle does not claim a local full-suite pass. GitHub Actions on the resulting exact commit is the acceptance gate. No real QPU, paid job, independent theorem corpus, physical experiment, material substitution, accepted fuel, net fusion electricity, financing-rate reduction or physical-compression result was produced.

**Next highest-value gate:** exact-head Prototype/Invariant and Autonomous Cold-Start Handoff Actions, then pin the external prover/kernel/corpus and compare schema reuse against baseline proof search under equal compute/time budgets and theorem-family-disjoint splits. Record failures, residual premises, changed statements, timeouts, memory, energy where measurable and cost per independently accepted result.

Research-Sync: main
