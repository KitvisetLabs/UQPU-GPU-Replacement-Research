# Lane A track — test-time scaling for scientific equation discovery

**Date:** 2026-10-28  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Cross-lane interfaces:** Lane F evidence/benchmark/cost contract; Lane H literature/handoff; INV-034/035  
**Status:** PROTOCOL_ONLY; no matched run executed

## Purpose

Operationalize the EMNLP 2026 paper “Test-Time Scaling for Scientific Equation Discovery” as a falsifiable search-width factor in the canonical matched-comparison gap [RG-EQN-008](../../docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md). The paper is an external method result, not UQPU evidence. See the [literature watch](../../docs/literature_watch/2026-10-28-test-time-scaling-equation-discovery.md) and [Batch 098](../../docs/BATCH_098_TEST_TIME_SCALING_EQUATION_DISCOVERY.md).

## Current interface

Use `software/uqpu-prototype/uqpu/equation_discovery_comparison.py` and its tests as the canonical contract. Schema v4 requires:
- matching dataset/source provenance, preprocessing, grammar, units, acceptance rules and group-disjoint split metadata across arms;
- a shared set of at least 30 preregistered seeds;
- per-arm source revision, configuration and runtime-environment hashes fixed across that arm's seeds;
- equal hard resource ceilings and consistent cost basis;
- explicit reporting of held-out error, accepted candidates, constraint violations, counterexamples, false discoveries and resource usage.

Declared hashes do not authenticate artifact bytes. Store or resolve the exact dataset/source/license/acquisition manifest, source tree, model/checkpoint, prompt/operator bundle, lockfile/container and held-out group manifest; independently verify those bytes and actual record-level disjointness.

## Preregistered experiment

1. Select and license a source-accessible equation-discovery dataset. Freeze its version, acquisition path, preprocessing and raw-data hash before method tuning.
2. Reserve whole law families and scales for blind testing. A random-point split is insufficient for the primary generalization claim.
3. Freeze one controller/model/checkpoint and define width as the sole experimental factor. Candidate arms may use widths 1, 2, 4, 8 and 16 only if this grid is declared before registration and fits the pinned environment.
4. Give every arm identical per-run ceilings for wall clock, CPU-core seconds, peak memory, accelerator seconds, candidate evaluations, generated tokens and total cost. Use the same 30+ seed set and no cross-arm reuse of held-out labels.
5. Apply one independent acceptance gate to every candidate: dimensional consistency, relevant symmetries/conservation/causality, known limits, held-out prediction, counterexample search, uncertainty and provenance. Retain failed searches and retries.
6. Report uncertainty for accepted-candidate rate and held-out error; also report false discoveries, counterexamples, constraint violations, total resources, cost per accepted candidate and energy where measurable. Do not rank arms using the source paper's results.

## Falsifier and stop rules

Do not accept a width advantage if it vanishes on held-out law families/scales, depends on leakage or unequal total resources, increases false-discovery/constraint-failure rates, or improves wall-clock alone without improving accepted output per total resource/cost. If data provenance or group-disjointness cannot be verified, the comparison remains blocked.

## Immediate priority order

1. Verify exact-head prototype/invariant and cold-start CI for the current main SHA.
2. Pin the dataset/source/license, model/source/runtime manifests and group-disjoint partition certificate.
3. Run the preregistered matched comparison only after gates 1–2 pass.
4. Separately continue Lane A's Priority-1 provider-neutral lowering and exact classical/reference plus target-aware simulator comparison on the frozen signed-Max-Cut useful-output contract.
5. Real-QPU execution remains later and requires target-specific credentials, bounded budget and explicit user consent. No paid job is authorized by this track.

## Evidence boundary

This track establishes a reproducible protocol only. It does not establish a new physical law, quantum advantage, energy saving, material/fuel/fusion outcome, financing improvement or Data-Center-to-Phone compression.


## 2026-10-28 follow-up — additional equation-discovery method families

The Batch 099 watch adds three distinct families to the future candidate set:
- **RISR** (https://arxiv.org/abs/2610.11387): residual-conditioned formula proposal and correction utility;
- **SCOPE/ClosureBench** (https://arxiv.org/abs/2610.18938): conjecture-level trajectories and interactive experiment design;
- **MorphingNet** (https://arxiv.org/abs/2610.19942): continuous formula parameterization followed by structure recovery.

These are external preprint results, not UQPU measurements. Do not pool their headline metrics. Keep the existing width sweep as a separate preregistered factor: first establish a matched width/resource baseline, then compare static method families under the same whole-law-family/scale-held-out contract and fixed total budgets. Active-experiment methods need a separate task suite and equal experiment-call budgets.

Before any run, verify code/data/model/license availability, hash actual artifacts and certify record-level disjointness. The existing schema-v4 contract already checks declared provenance fields and shared budgets, but declared hashes alone do not authenticate source bytes. Include training plus inference costs and preserve failures, counterexamples and false discoveries. The immediate CI gate remains exact-head prototype/invariant and cold-start audit; no paid QPU job is authorized.
