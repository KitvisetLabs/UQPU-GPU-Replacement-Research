# Daily Eight-Lane integration — 2026-10-28 — method-provenance binding

**Cycle-start main SHA:** d04eb7987b2e3b0c82840b77e263cf2ae8e41285  
**Primary owner:** Lane F — reproducibility/evidence integration  
**Execution priority:** Lane A — compiler/workload and matched comparator  
**Publication/provenance owner:** Lane H  
**Evidence class:** SOFTWARE_CONTRACT; exact-head CI pending/unverified

## Canonical state and implementation

This cycle began from the latest observed main, read the required governance/strategy documents, root directives, Batch 096, the equation-discovery gap, the existing matched comparator and split-manifest verifier, plus the autonomous handoff and commit-sync policies. The concrete defect was in the comparator's per-run provenance boundary: a method's source revision could vary across its 30 seeds without being rejected, while configuration/model/prompt and runtime/dependency provenance were not separate fields.

The main-branch implementation now:
- adds `dataset_provenance_sha256` as a shared dataset/source/license/acquisition digest;
- adds per-method `method_config_sha256` and `runtime_environment_sha256`;
- requires method source/config/runtime digests to remain constant across seeds within each method;
- emits comparison schema v4 and reports provenance;
- tests drift and invalid hashes in both comparator and split-disjointness fixtures.

The detailed acceptance and limitations live in [Batch 097](../docs/BATCH_097_METHOD_PROVENANCE_BOUNDARY.md) and [RG-EQN-008](../docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md). The change does not run or rank SymFM, PiT-PO, STRIDE, LLM-PySR, MOSAIC-SR or any other external method.

## Cross-lane integration edges

| Edge | Shared interface | Result this cycle | Status / next experiment |
|---|---|---|---|
| A↔F↔H | Matched comparison schema v4 + source literature watch | Makes per-seed method drift detectable and provenance explicit | TESTING_PENDING_CI; verify exact-head tests, then execute preregistered comparison |
| C↔F | Dataset provenance, split hashes, grouped holdout and accepted output | Keeps dataset identity separate from memory/state-space size and output reconstruction | BLOCKED until raw data, license/source manifest and group-disjoint certificate are pinned |
| D↔G | Equation candidate → process-window/metrology/yield contract | No new device/process claim; any future discovered law must map to measurable process variables | BLOCKED until independent process data exist |
| E↔F↔H | BIO-001 accepted liquid; FUS-001 net delivered electricity; FIN-001 financed principal/time-to-evidence | No new mass/energy/cost or finance evidence; the same provenance discipline applies to any future surrogate | BLOCKED until process boundaries and independent measurements exist |
| INV-034/035→A–H | Candidate equation contract, falsifier, held-out prediction, counterexample search, independent validation | Method schema hardening only; present physics remains binding | OPEN; no equation promoted |

The all-pairs A–H review remains required (28 unordered pairs). The review found no evidence-backed reason to combine symbolic-regression fit scores with device/material/fusion/finance claims. D/G co-design remains continuous, not paused.

## CI and synchronization

Commits currently on main for the code/tests/gap/batch are linked from Batch 097. The combined-status endpoint returned no check entries for the new head and the available workflow-run connector exposes only PR-triggered runs. Thus exact-head CI is **unverified**, not green. Parent-state CI does not transfer. The next agent must inspect the actual Actions page for the latest main SHA and record the prototype/invariant and cold-start results.

`RESEARCH_GAPS.md` remains a large append-oriented file and was not rewritten from a partial read. The updated detailed RG-EQN-008 record is the owner source; aggregate append synchronization debt remains explicit.

## Mission boundary

No real-QPU job, paid provider call, physical experiment, new physical law, material substitution, commercial bio-oil, net fusion electricity, lower WACC, 100×/100,000,000× advantage, or physical Data-Center-to-Phone result is claimed. INV-025/026/027 and INV-029–035 remain preserved. All six language versions of the strategic master plan and recorded strategic AI-agent/funding references remain canonical context.
