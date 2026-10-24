# Literature watch — 2026-10-24: top-down quantum compiler configuration selection

**Primary owner:** Lane H — research publication and provenance  
**Technical consumer:** Lane A — workloads/compiler/runtime; Lane B — target/provider integration  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`  
**UQPU reproduction:** `NOT EXECUTED`  
**Provider/QPU jobs:** `0`  
**Related:** INV-025–029, INV-034–035, EQN-001–006, `QCOMP-CONFIG-001`

## Source and date

Ming Zhong, Xiangyu Ren, Kangyu Zheng, Zhi Zeng, Shenggen Zheng, Shaohua Li and Zhiding Liang, **“Turning Quantum Compiler Configuration Selection Upside Down: A Top-Down Paradigm,”** arXiv:2610.29170, submitted **2026-10-21**.  
Primary preprint record: https://arxiv.org/abs/2610.29170  
DOI-style record: https://doi.org/10.48550/arXiv.2610.29170

The preprint proposes choosing hardware target and compiler settings jointly, using offline configuration-oracle results to distill reusable rules and predictors rather than always choosing a device first and then tuning compiler options with an online search loop. The abstract reports a benchmark covering 268 quantum circuits, evaluates ten LLMs, and describes a rule-guided predictor framework intended to balance configuration quality and selection latency.

## Genuine novelty for UQPU

The relevant hypothesis is **joint target/configuration selection can be a compiler/runtime optimization problem in its own right**. A provider-neutral UQPU planner should not assume that target selection and compiler-option tuning are independent sequential decisions if the admissible configuration space is small enough to characterize offline.

This can complement the existing UQPU ladder—semantic workload contract, provider-neutral lowering, target-aware simulation, output acceptance and total cost per accepted task—by inserting a measured configuration-selection stage. An offline oracle can serve as an upper bound on selection quality; it must not be confused with an executable policy or an achievable production result.

## Evidence class and limitations

- This is a third-party preprint, not peer-reviewed project evidence and not a UQPU reproduction.
- The abstract is not a full methods audit. The exact configuration-space size, hardware/compiler versions, data splits, objective, noise model, ablations, time accounting and license must be checked in the full paper and released artifacts before any reproduction.
- Better estimated fidelity or proximity to an oracle does not automatically mean better accepted application output, lower cost, higher throughput, lower latency or lower energy.
- Configuration labels derived from exhaustive search can leak circuit- or device-specific information. A random split alone may overstate generalization; held-out circuit families and held-out target/device families are required.
- A learned rule can be brittle under backend calibration drift, compiler-version changes, new circuits, different objectives or provider pricing. Any offline result must carry target, compiler, calibration and workload provenance.
- No UQPU circuit, SDK, simulator, provider, QPU, shots, energy, billable usage or accepted-task cost was measured for this watch.

## Falsifiable follow-up: QCOMP-CONFIG-001

1. Audit the full preprint, code/data availability, licensing, exact configuration axes, fidelity/quality definition and all train/test partitions.
2. Freeze a small set of representative UQPU circuits and identical useful-output contracts. Record source-circuit hashes, target/SDK/compiler versions, noise/calibration snapshot identity where applicable, and the accepted output-quality predicate.
3. Compare at least four policies on the same frozen configuration space: (a) fixed/default configuration, (b) target-first then compiler tuning, (c) offline exhaustive oracle as an upper bound, and (d) top-down rule-guided/ML selection. A direct LLM selector may be added as a separately budgeted baseline.
4. Split by circuit family and by target/device family; reserve a blind out-of-distribution set. Never train or tune rules on blind targets/circuits.
5. Use a matched search/evaluation budget and report selection latency, compile time, one-/two-qubit gate counts, depth, routing overhead, predicted and observed quality, held-out regret relative to the oracle, timeout/failure rate, and reproducibility across seeds.
6. Only after the simulator/dry-run gate passes, consider provider-specific execution if credentials, a bounded budget and explicit user consent are available. Bind every observed quality result to the same provider/target whose price is used.
7. For any accepted application task, report total cost per accepted useful output with host compute, state preparation, shots, retries, reconstruction, transfer/I/O and energy where measured. Unknown values remain unknown, not zero.

**Falsifiers:** the joint policy does not outperform the simpler target-first baseline on blind circuits/targets; its gain disappears when compiler versions or calibration contexts shift; selection overhead outweighs compile-time savings; oracle proximity fails to predict accepted task quality; or total cost per accepted task does not improve. Any of these closes or narrows the hypothesis without changing the acceptance threshold after seeing held-out results.

## Exact lane and mission relevance

- **A — workloads/compiler/runtime:** primary consumer; joint target/compiler configuration selection becomes a testable stage in the software-first pipeline.
- **B — cloud/QPU/provider integration:** provider-neutral metadata and target identity are mandatory; no provider call is authorized by this paper.
- **C — memory/state/data movement:** include circuit serialization, host memory, state/input loading, output reconstruction and transfer; fidelity alone does not establish memory replacement.
- **D — devices/chips/process/packaging:** a target-selection result does not prove a new device requirement or device-level physical improvement.
- **E — biomass/materials/bio-oil/fusion/cooling:** no direct material, fuel, net-electricity or cooling result; any future energy claim needs measured full-system boundaries.
- **F — economics/evidence/integration:** oracle regret and selection latency are intermediate metrics; final acceptance is matched useful-output quality and total cost/energy per accepted task.
- **G — manufacturing equipment/software/factory systems:** no yield/process-window/manufacturing consequence until a repeatable device requirement is independently validated; maintain D/G co-design.
- **H — strategy/finance/publication:** prioritize a cheap offline benchmark before expensive experimental work; no capital/WACC claim follows from the preprint.
- **Repository Lane I:** no demonstrated causal connection to the specialist vehicle-lift lane; leave it explicitly unchanged.

## Foundational and permanent-invariant boundary

- **FND-001:** no energy-per-accepted-task measurement.
- **FND-002:** output-information and readout requirements remain binding.
- **FND-003:** no matched control/quantum-speed-limit experiment.
- **FND-004/005:** no new physical primitive or particle/QFT mechanism.
- **FND-006 / EQN-001–006:** this is compiler configuration selection, not equation discovery or a new law. Current physics remains binding.
- **INV-029:** no data-center-to-phone compression or lifecycle-cost evidence.
- **INV-030–033:** no material substitution, accepted bio-oil, net fusion electricity, principal/interest or WACC evidence.
- **INV-034–035:** no foundational physical limit is displaced and no AI-generated equation is promoted.
- **INV-025–027:** the 100,000,000-GPU and universal 100,000,000-unit moonshots remain falsifiable goals.

The permanent root directives 00–06, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and Thai/English/Chinese/Japanese/Korean/German master-plan links remain canonical. This watch does not alter them.
