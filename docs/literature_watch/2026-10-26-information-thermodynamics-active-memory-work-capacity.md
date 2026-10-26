# Literature watch — 2026-10-26: active memory, prediction and work capacity

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — foundational research publication and strategic integration  
**Implementation/benchmark owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Cross-lane owners:** Lane C — state/memory/data movement; Lane F — evidence and economics  
**Feeds:** FND-001, FND-002, FND-006, EQN-001–006, INV-029, INV-033–035  
**Evidence class:** `PEER_REVIEWED_THEORETICAL_FRAMEWORK + PROPOSED_BENCHMARK_CONTRACT`  
**UQPU project evidence promoted:** none  
**Canonical starting main:** `412403efebabd7186dcbfca286d8481308dab176`

## Primary source and genuine delta

Lukas J. Fiderer, Paul C. Barth, Isaac D. Smith and Hans J. Briegel, “Information Thermodynamics of Agents: The Work Capacity of Channels with Memory,” *Physical Review X* **16**, 041004, published 2026-10-05. DOI: [10.1103/7nds-tjr8](https://doi.org/10.1103/7nds-tjr8). [Publisher record](https://journals.aps.org/prx/abstract/10.1103/7nds-tjr8).

The paper develops an information-thermodynamic framework for agents coupled to environments through **percept–action loops**, modeled using hidden Markov channels. Unlike a passive input tape, the environment may react to the agent's actions, so actions can influence future observations. Its work-capacity objective is a model-defined maximum expected work-extraction rate. In some active-feedback regimes, maximally predictive agents are not work-efficient; retaining information about past actions can reduce the modeled work rate, and an intermediate prediction/forgetting balance can be better.

The useful novelty for UQPU is not a new universal “forgetting saves energy” rule. It is a sharper experiment design: **passive-stream memory results must not be assumed to transfer to action-coupled workloads**, and memory retention policy should be varied independently from task semantics.

## Limitations and evidence boundary

- This is a theoretical information-thermodynamics framework, not a measurement of a CPU, GPU, NPU, QPU, AI agent or UQPU runtime's wall-plug energy.
- The conclusions depend on the specified channel, agent classes, thermodynamic implementation assumptions and objective. They do not say that prediction is always inefficient or that arbitrary data deletion is beneficial.
- A logical state count, Shannon entropy, memory bit, software reset or estimated operation count is **not** itself measured RAM footprint, joules, cost or accepted-task performance.
- The result does not overturn Landauer's principle, quantum thermodynamics, or any current physical law; it refines the question to an action-dependent model class.
- No UQPU implementation, physical experiment, independent reproduction or economic advantage is claimed.

## Exact UQPU relevance

- **FND-001 / Lane C:** extend thermodynamic-gap accounting so that retained state, memory updates, state I/O and actual irreversible resets are distinguished. The current conditional-mutual-information calibration remains synthetic; this paper does not validate that estimator.
- **Lane A:** add a falsifiable workload/runtime experiment comparing memoryless, predictive and bounded-memory policies under one frozen useful-output contract.
- **FND-002 / INV-029:** count only accepted outputs and include reconstruction and side-information costs; do not convert information-theoretic quantities directly into physical memory or phone-class capability.
- **INV-033 / Lane F:** include measured energy, host work and capital/operating cost only when sourced from the same run and comparable boundary. This paper supplies no financing-rate result.
- **INV-030–032 / Lanes D, E and G:** no direct material, biomass-fuel, fusion-electricity or manufacturing result follows. A future physical implementation could motivate memory/device measurements, but not a present materials or energy claim.
- **INV-034–035:** use the paper as a model-generation and falsification prompt while keeping established physics binding for engineering claims.

## Proposed falsifiable follow-up — FND001-ACTIVE-MEMORY-001

1. Freeze a finite-state toy environment with an exact transition matrix and a fixed accepted-output contract. Include both a passive-tape control, where future inputs are action-independent, and active-feedback environments where actions change the next-observation distribution.
2. Compare `MEMORYLESS`, `PREDICTIVE` and `BOUNDED_MEMORY` policies with the same task, horizon, seeds, interaction budget, quality threshold and train/held-out environment split.
3. On small channels, compare a direct implementation against an independently coded evaluator of the paper's model-defined work-capacity objective. Record convergence and uncertainty; do not treat a finite-horizon estimator as the exact supremum.
4. Search counterexamples: deterministic feedback, noisy feedback, passive tape, different memory caps, and policy families outside the paper's stated classes. Preserve cases where prediction is best or where no robust difference appears.
5. Only after the model gate passes, run a separate host/device implementation experiment measuring actual memory bytes, reads/writes, state transfer, wall time and calibrated energy. Keep logical entropy and physical joules in separate columns.
6. Report failed attempts, retries and all resource budgets. Require independent replication before any physical or system-level promotion.

**Falsifier:** the proposed UQPU-specific memory-policy effect is not supported if held-out active-feedback environments show no reproducible policy-dependent change after task quality and total resource budgets are matched, or if the effect vanishes under an independent evaluator. The source paper's theorem is not falsified by a failed UQPU implementation.

## Synchronization note

A separate open PR already tracks L2G-SR structural-guidance work (PR #104); this watch does not duplicate that artifact or claim that pending branch is canonical. Large append-only `RESEARCH_GAPS.md`, `WORKLOG.md` and `README.md` were not rewritten from partial reads.
