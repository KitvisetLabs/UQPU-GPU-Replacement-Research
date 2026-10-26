# FND001-ACTIVE-MEMORY-001 — Active-memory work-capacity benchmark contract

**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owners:** Lane C — state/memory/data movement; Lane F — evidence/economics  
**Publication owner:** Lane H  
**Date:** 2026-10-26  
**Status:** MODEL_ONLY_EXACT_CHANNEL_REPRODUCTION; no finite-memory policy comparison or physical result promoted  
**Source:** Fiderer et al., *Physical Review X* 16, 041004 (2026-10-05), DOI 10.1103/7nds-tjr8.

## Question

For a fixed useful-output task, does the memory policy that is best under a passive input stream remain best when the environment reacts to the runtime's actions? If not, can any policy-dependent effect be reproduced without sacrificing accepted output quality or hiding state-transfer, reset, host-compute or energy costs?

This is a proposed UQPU benchmark question, not an assumption that forgetting saves energy.

## Frozen comparison axes

### Environment mode

- `PASSIVE_TAPE`: future inputs are independent of the runtime's actions, conditional on the frozen data-generating process.
- `ACTIVE_FEEDBACK`: the next observation distribution depends on the runtime's action under a frozen transition model.
- `CONTROL_DETERMINISTIC_FEEDBACK` and `CONTROL_NOISY_FEEDBACK`: preregistered active-feedback controls, not interchangeable with the primary environment.

### Policy class

- `MEMORYLESS`
- `PREDICTIVE`
- `BOUNDED_MEMORY`

The paper's theoretical agent classes and the UQPU implementation classes must be mapped explicitly. Similar names do not prove identical mathematical assumptions.

### Matched contract

Every compared run must use the same:
- workload-contract ID and version;
- input/task distribution and accepted-output semantics;
- quality threshold, horizon and interaction budget;
- train/held-out environment split and preregistered seeds;
- target/runtime version for a given comparison;
- failure, retry and output-reconstruction accounting.

A run is not useful merely because it executes. Only outputs passing the frozen quality predicate count as accepted useful outputs.

## Required per-run record

Record at minimum:
- run ID, code/config hash, workload-contract ID, environment-model hash, policy class, seed and train/held-out designation;
- accepted output count, rejected output count, task-quality distribution and quality threshold;
- logical memory-state count and logical information metrics, clearly marked as model quantities;
- peak host/device memory bytes, state-I/O bytes, transfer bytes, update count, reset count and any measured irreversible-erasure event;
- wall-clock latency, throughput, host CPU/GPU time and retry/reconstruction cost;
- energy value, meter/sensor provenance, calibration and uncertainty **or explicit null / UNMEASURED**;
- cost value, pricing/billing provenance and accounting boundary **or explicit null / UNMEASURED**;
- failed searches, failed runs and all resource budgets.

Logical state count, entropy and reset count are not substitutes for measured bytes or joules. A reset must not automatically be classified as thermodynamic erasure without a physical mapping.

## Comparison and acceptance rules

1. Compare policies only within matched workload, environment, target and resource-budget strata.
2. Report both accepted-task quality and total resources; do not reward a policy that reduces memory by failing the useful-output contract.
3. Cost per accepted output is undefined when zero outputs pass the quality gate. Energy per accepted output is undefined when energy is unmeasured or no outputs pass.
4. Do not combine one target's quality/probability with another target's price or calibration.
5. Treat the paper's work-capacity objective as a theoretical model quantity. Report it separately from software wall time, measured hardware energy and economic cost.
6. Use independent scoring and an independent evaluator for the small exact-channel fixture.
7. Keep all negative and null results. No model fit or policy ranking is a physical law.

## Implementation note — 2026-10-26

The pure-Python evaluator in `software/uqpu-prototype/uqpu/active_memory.py` computes Shannon entropy and the memoryless-agent special case `W = H(A) - H(S)` for finite action-to-percept channels. It reproduces the published binary invariant channel and its analytic reference, then evaluates a separate passive IID-tape control with the same output marginal at one selected operating point. The regression tests are in `software/uqpu-prototype/tests/test_active_memory.py`; the machine-readable result is `benchmarks/results/fnd001-active-memory-exact-channel-2026-10-26.json`.

This is a model-level analytic reproduction only. It does not compare predictive and bounded-memory agents, implement the paper's general finite-memory theorem, measure accepted task quality, map logical entropy to physical memory bytes, or measure physical/software energy or cost.

## Test sequence

1. **Contract smoke:** reject missing hashes, mismatched workload IDs, unknown policy/environment labels, invalid quality thresholds and negative resource counters.
2. **Exact small-channel control:** freeze transition matrices and initial conditions; independently calculate the reference objective where analytically tractable.
3. **Finite-horizon convergence:** vary horizon and seeds; show confidence intervals and bias against the exact toy reference.
4. **Held-out generalization:** change feedback strength, noise and transition probabilities without tuning on held-out cases.
5. **Counterexamples:** include passive-tape cases, deterministic feedback, noisy feedback and cases where predictive policy wins or policy ranking is statistically unresolved.
6. **Physical measurement gate:** only after the model gate, instrument one controlled implementation; report actual memory, data movement, wall energy and calibration.
7. **Independent replication and economics:** freeze code/data, reproduce the ranking independently, then compute total cost per accepted useful output using a single comparable boundary.

## Falsifiers and stop conditions

- No reproducible policy-by-environment interaction under held-out tests.
- Apparent gain disappears when quality, horizon, seeds or total budget are matched.
- Independent evaluator disagrees with the primary result.
- Any proposed effect depends on treating logical bits/entropy as physical bytes/joules.
- Memory reduction is offset by state reconstruction, retries, host work or data movement.
- Model assumptions cannot be mapped to an actual runtime/environment without changing the useful-output contract.

Failure of this UQPU experiment does not refute the source theorem; it means the proposed application path is unsupported.

## Cross-lane outputs

- Lane A: matched useful-output policy benchmark and runtime-state accounting.
- Lane B: no provider change; if later executed on a QPU, use one provider/target/route's matching result and billing record.
- Lane C: distinguish logical state from physical memory and transfer.
- Lane D/G: only enter after a physical implementation creates a documented device/manufacturing bottleneck.
- Lane E: no biomass, bio-oil or fusion inference from this software experiment.
- Lane F: accepted-output, uncertainty and full-cost accounting.
- Lane H: publish positive, null and negative results with source provenance.

No paid QPU job, material experiment or funding action is authorized by this contract.
