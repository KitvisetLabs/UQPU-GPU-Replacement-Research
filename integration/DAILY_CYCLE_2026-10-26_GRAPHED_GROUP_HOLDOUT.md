# Eight-Lane UQPU research cycle — 2026-10-26 — GraphED method and grouped-holdout contract

**Canonical starting main:** `6bc5b29b846c29c2c3fabd729c1bc62362b24e3e`  
**Primary execution owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence and integration owner:** Lane F — benchmarks, uncertainty, economics and cross-lane accounting  
**Publication owner:** Lane H — literature surveillance and strategic context  
**Cross-lane consumers:** B/C provider and state/I/O accounting; D/G device/material/manufacturing co-design; E materials/energy/cooling  
**Evidence class:** PEER-REVIEWED LITERATURE WATCH + SOFTWARE CONTRACT + REGRESSION TESTS  
**Promotion boundary:** no physical law, real-QPU advantage, qualified material, saleable fuel, net fusion electricity, financing effect or Data-Center-to-Phone result promoted.

## 1. Canonical-state and preservation audit

Read the current PROJECT_CHARTER.md, VERSION_INVARIANTS.md (including INV-025–037), GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root directives 00, 00A and 01–06, Batch 066 plus Batches 065/064/063, the latest FND-003/Planckian and FND-001/RG040 artifacts, RG-EQN-007/008, the current comparator implementation/tests, the current CI state, and open-PR/collision context.

The current canonical numbered batch is Batch 066. Batch 067 is already proposed in an open PR, so this cycle did not create a conflicting numbered batch. The six public master-plan editions (Thai, English, Chinese, Japanese, Korean and German), strategic AI-agent/funding references, and all eight root directives remain preserved. The auxiliary Lane I directory does not replace A–H. The recursive tree audit previously reported maximum directory depth 4, below the <=16 limit. Large append-heavy RESEARCH_GAPS.md and WORKLOG.md were not rewritten from partial reads; their synchronization debt remains explicit.

## 2. Fresh literature surveillance

Added `docs/literature_watch/2026-10-26-graph-based-constitutive-law-discovery.md` for Xu, Chen and Zhang, “Beyond empirical models: Discovering constitutive laws in solids with graph-based equation discovery,” *Science Advances* 12(37), eaec0989, published 2026-09-11, DOI 10.1126/sciadv.aec0989.

GraphED uses equation-as-graph structure with edge-carried constants/material-specific parameters, graph templates and genetic-programming search. The paper reports constitutive-model case studies for rate-dependent alloy steel, lithium deformation and filled-rubber hyperelasticity. Its relevance is a candidate equation-discovery family for multicase material constitutive models, not evidence of a new fundamental law or any UQPU material result.

The search also checked recent results already indexed in the current tree: the PISR delayed-interface closure, the Planckian thermalization bound, the controlled optical strong-Mpemba experiment, progressive symbolic discovery and formal proof-search work. The Mpemba and Planckian sources were already covered by existing watches, so no duplicate articles were created. No newly found source closes an end-to-end mission or economic gate.

## 3. Lane A implementation and tests

Advanced `software/uqpu-prototype/uqpu/equation_discovery_comparison.py` from comparison schema v2 to v3. Each run now declares a group-holdout unit, positive held-out group count, split-policy SHA-256 and held-out-group-manifest SHA-256. The validator rejects random-point-only holdout labels, inconsistent holdout units/counts, mismatched policy/manifest hashes, and invalid group counts. The summary exposes the shared holdout metadata.

Regression tests were added for random-point rejection, metadata mismatches, positive group counts and output-schema reporting. This makes the intended generalization boundary explicit and comparable across methods.

**Important limitation:** this code checks declared metadata and hash equality only. It does not parse the manifest or prove that train/validation/test records are actually disjoint. The manifest-bound partition certificate in the open RG-045 PR #69 remains a separate gate; that PR is not treated as canonical main. The open MorphingNet PR #117 and earlier equation-discovery PRs were inspected for overlap; their unmerged claims/code are not treated as main-branch evidence. No external method was run, and no method ranking is reported.

## 4. Explicit A–H status

- **A — Quantum programming/workloads/compiler/runtime:** active; grouped-holdout metadata added to the matched equation-discovery comparator. Next: validate actual partition manifests, then execute a frozen accepted-useful-output workload with CPU/GPU/NPU baselines and reference/bound certificates.
- **B — Cloud/QPU/provider integration:** provider-neutral paths remain the target; simulator/dry-run first. No paid QPU job was submitted and no provider bill or real-QPU quality result was created.
- **C — RAM/VRAM/HBM/storage/state/data movement:** still requires physical bytes, movement, I/O, host reconstruction and accepted-task accounting. Hilbert-space dimension is not treated as readable classical memory.
- **D — Devices/chips/process/fabrication/packaging:** continuous lane remains active; GraphED is only a possible future material-model method. No device/process window or fabrication advantage is established.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** no Pangola-carbon qualification, accepted bio-oil yield/cost, or reliable net-electric fusion result. GraphED transfer requires measured material-specific data and blind validation.
- **F — Economics/benchmarks/evidence/integration:** matched comparison now makes declared group-holdout provenance explicit; the actual partition certificate, independent reproduction and total cost per accepted useful task remain open.
- **G — Quantum-chip manufacturing equipment/software/factory systems:** D/G co-design is preserved; no manufacturing-equipment or factory-yield result is added.
- **H — Kanusanan Pongpanna Model strategy/finance/future industries:** the new source is recorded with limits and a falsifiable follow-up. The strategic plan, multilingual links and funding/AI-agent references remain unchanged.

## 5. Foundational and equation-discovery status

- **FND-001:** finite-state work-capacity experiments remain MODEL_ONLY; no calibrated physical work/heat or accepted-task energy result.
- **FND-002:** output-information lower-bound and reconstruction accounting remain open; no conversion of quantum state-space size to classical storage.
- **FND-003:** the Planckian thermalization lower-bound helper is scoped to the universal-thermalizer assumptions; no matched device experiment or observed-to-bound ratio is claimed.
- **FND-004:** no alternative physical primitive is experimentally demonstrated.
- **FND-005:** no new experimentally validated QFT/particle mechanism.
- **FND-006:** the hypothesis/proof/experiment separation is preserved; a formal proof cannot replace physical validation.
- **EQN-001–006:** GraphED joins the candidate-method watch list. Any comparison must proceed through generator, explicit constraints, held-out/generalization test, counterexample search, proof/simulation where applicable, discriminating experiment, independent replication, system consequence and economics. False discoveries and failed searches remain reportable outputs.

## 6. INV-029 through INV-035 and moonshot boundaries

- **INV-029:** no phone-class physical compression or lifecycle-cost evidence; the US$10T–US$100T proxy remains an ambition scale, not a current valuation or result.
- **INV-030:** no elemental transmutation or Pangola-carbon functional substitution.
- **INV-031:** no accepted saleable liquid-energy/fuel yield or full process-cost result.
- **INV-032:** no reliable net delivered fusion-electricity or lifecycle-cost result.
- **INV-033:** no measured reduction in financed principal, absolute interest, WACC or economy-wide rates.
- **INV-034:** advances a reproducible, falsifiable method-comparison contract.
- **INV-035:** AI/symbolic equations remain hypotheses; dimensional/symmetry/conservation/causality, held-out prediction, falsifier and independent-validation gates remain mandatory.
- **INV-025/026/027:** 100,000,000-GPU and universal 100,000,000-unit targets remain falsifiable goals, not demonstrated advantages.

## 7. GitHub synchronization and CI

At the starting main SHA, the prototype workflow run `40329247542` completed successfully across Python 3.10, 3.11 and 3.12 plus the listed QSP/QSVT/reference/target-snapshot jobs; the cold-start handoff audit `40329247325` also passed. The optional synthetic finite-shot sensitivity and equal-budget QAOA objective-selection steps were skipped by their workflow conditions. These runs validate the starting commit, not this cycle's new v3 changes. Exact-head Actions must validate the resulting commit before v3 is described as CI-passing.

The starting-head cold-start run passed on `6bc5b29b846c29c2c3fabd729c1bc62362b24e3e`. The first commit from this cycle (`ad848e75313cd60145edff462ba85de41c0b2f57`) then failed the handoff audit solely because its commit message omitted the required `Research-Sync: main` trailer; the prototype workflow was still running when that failure was inspected. This follow-up records the governance repair with the required trailer; it does not alter the research claims or code. The new head's own Actions must be checked before reporting final CI status. No paid QPU jobs, funding actions or physical experiments were authorized or executed.

## 8. Next highest-value gate

1. Implement and independently test the RG-045 manifest-bound partition certificate: canonical dataset identity, stable record/group IDs, duplicate and overlap rejection, deterministic serialization, digest/manifest binding and adversarial fixtures with different file hashes but overlapping IDs.
2. Pin GraphED source/code/data revisions and licenses; compare it under the shared v3 contract on family-disjoint material/geometry/loading-regime holdouts with identical total-resource budgets and at least 30 preregistered seeds where feasible.
3. Keep Lane A's primary computing gate active in parallel: one frozen accepted-useful-output workload, competitive CPU/GPU/NPU baselines, reference/bound certificate, provider-neutral lowering and a complete accepted-task ledger including quality, latency, throughput, shots/billing, state/I/O/transfer/memory, retries, reconstruction, host compute, measurable energy and total cost.
4. Leave RG040, RG-EQN-007/008, BIO-001, FUS-001 and FIN-001 open until their independent physical/economic gates pass.

This report and the literature watch are incremental canonical artifacts. The large RESEARCH_GAPS.md and WORKLOG.md were not rewritten; aggregate-gap synchronization remains debt. No paid QPU submission, material/fuel/fusion claim, new physical law, lower WACC claim or Data-Center-to-Phone success is asserted.
