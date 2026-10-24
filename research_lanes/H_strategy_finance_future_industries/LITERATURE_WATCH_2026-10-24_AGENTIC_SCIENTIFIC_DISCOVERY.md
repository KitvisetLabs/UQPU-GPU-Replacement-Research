# Literature watch — 2026-10-24: agentic scientific discovery needs traceable evidence workflows

**Published:** 2026-10-22  
**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, research orchestration and scientific publication  
**Cross-lane consumers:** A–H; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Evidence class:** PEER-REVIEWED METHODS PRIMER / LITERATURE_ONLY  
**UQPU project evidence promotion:** none  
**Canonical starting main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e

## Primary source

Bin Feng and colleagues, “Agentic AI systems for scientific discovery,” Nature Reviews Methods Primers 6, Article 81 (2026), version of record published 22 October 2026. DOI: [10.1038/s43586-026-00534-y](https://www.nature.com/articles/s43586-026-00534-y).

The primer describes agentic systems as traceable workflows connecting literature retrieval, data, theory, physics-based simulation and automated experimentation. It discusses task decomposition, memory, tool use, single- versus multi-agent systems, autonomous versus human-in-the-loop control, and reproducible evaluation/reporting. It also identifies failure modes including hallucination, tool misuse, limited interpretability and safety risk.

## Genuine novelty and project relevance

This is a methods primer, not a new equation-discovery algorithm, physical law, quantum-computing result or demonstration of autonomous scientific reliability. Its value for UQPU is architectural: the agent's output must be a provenance-bearing research workflow whose claims can be inspected and reproduced, not a fluent narrative or a successful tool invocation.

The project already has a cold-start handoff manifest and an audit workflow. Those artifacts check structural discoverability and declared evidence boundaries, but the repository itself states that the audit does not validate scientific claims. The useful next question is therefore whether a memoryless agent can correctly recover the latest canonical state, identify the next evidence gate, reproduce a deterministic test, and avoid promoting literature/model outputs to physical or economic claims.

## Limitations

- The paper is a broad methods primer, not a controlled UQPU benchmark.
- General workflow guidance does not show that an agent's scientific conclusions are correct, complete or independently reproducible.
- Automated tool execution may produce valid files or successful jobs while the underlying hypothesis is false, the data are leaked, or the result fails the useful-output contract.
- Agent communication and orchestration do not remove the need for independent reviewers, safety boundaries, exact commit provenance, blinded tests, counterexamples and measured system economics.
- No source in this watch establishes a new physical law, quantum advantage, material substitution, commercial fuel/electricity advantage or lower financing rate.

## Eight-lane implications

- **A — quantum programming/runtime:** treat each workflow as a typed task graph with a workload contract, pinned tool versions, input/output hashes, budget caps, failure retention and a separately evaluated useful-output result.
- **B — cloud/QPU integration:** preserve dry-run-first behavior. An agent must not infer provider access or submit a paid job without credentials, bounded budget and explicit authorization.
- **C — memory/state/data movement:** record dataset, artifact and state materialization boundaries; a large mathematical state space is not readable classical memory.
- **D — devices/chips/process/packaging:** require physical design assumptions, calibration provenance and a manufacturable process window before translating software discoveries into device requirements.
- **E — biomass/materials/bio-oil/fusion/cooling:** laboratory automation must use safe approved protocols and measured mass/energy/product acceptance; a generated plan is not a material, fuel or net-electricity result.
- **F — economics/evidence/integration:** log compute, tool calls, retries, human review, experiment cost, energy when measured, failed hypotheses and cost per accepted result. Unknown quantities stay unknown.
- **G — manufacturing equipment/factory systems:** distinguish a proposed process-control workflow from measured yield, equipment throughput, maintenance and cost-per-good-device.
- **H — strategy/finance/publication:** stage capital against the cheapest decisive evidence gate; publish traceable results and failed hypotheses so later agents can continue without relying on private chat context.

## Falsifiable follow-up — HANDOFF-AGENT-001

Preregister a small, no-purchase, no-QPU cold-start benchmark using a fixed main SHA and five tasks drawn from different lanes.

1. Give an independent agent only the canonical repository and task statement, not prior chat history or private notes.
2. Require it to identify the current main SHA, read the permanent mission/invariant directives, locate the newest batch/gap/CI state, and name the next gate for its assigned lane.
3. Ask it to reproduce one deterministic, dependency-pinned test or model-only artifact and report exact commands, commit, output hash and evidence class.
4. Score source/commit accuracy, missed blockers, false scientific/economic claims, invariant omissions, reproducibility and time-to-correct-handoff. Treat unsafe actions or unsupported evidence promotion as hard failures.
5. Repeat with at least two independent cold starts and retain failed outputs. The audit passes only if every critical claim is source-linked and no test execution is confused with scientific acceptance.
6. Keep all provider calls, paid QPU jobs, purchases and hazardous physical experiments at zero.

A pass would validate the handoff protocol for the tested tasks only. It would not validate any scientific hypothesis or prove autonomous agents generally reliable.

## Relation to INV-029–035 and foundational work

- **INV-029:** a reproducible research handoff may reduce wasted R&D effort; no phone-class physical-compression result follows.
- **INV-030/031/032:** no Pangola-material, accepted-fuel or net-fusion-electricity result follows.
- **INV-033:** the proposed benchmark may measure time-to-evidence and review cost; no lower project WACC or economy-wide interest-rate claim follows.
- **INV-034/035:** the workflow must preserve present physical laws as binding for engineering, while allowing alternative mathematics only through dimensional/symmetry/conservation/causality checks, scaling limits, falsifiers, held-out predictions, proof/experiment and independent validation.
- **FND-001–006 / EQN-001–006:** candidate generation, constraint checking, held-out evaluation, counterexample search, proof/simulation, discriminating experiment, replication and economic consequence remain separate stages. Tool success cannot skip a stage.

## Integration boundary

This watch does not modify the permanent root directives, strategic master-plan links or canonical operating policy. It proposes an auditable cold-start experiment as a future integration edge; the current manifest audit remains a structural check, not scientific-claim validation.
