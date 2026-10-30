# Literature watch — 2026-10-30: agentic scientific discovery, persistent memory and reproducible handoff

**Checked:** 2026-10-30  
**Primary owner:** Lane H — research operating model and publication  
**Cross-lane interfaces:** A (workload/equation evaluators), B (provider-neutral tools), C (memory/data provenance), D/E (physical/material constraints), F (evidence/cost), G (factory workflows); INV-034/035  
**Evidence class:** PEER-REVIEWED METHODS PRIMER + PEER-REVIEWED SCIENCE-METHOD PAPER; NOT REPRODUCED BY UQPU

## Sources

1. B. Feng, P. Walther, L. Zhang et al., “Agentic AI systems for scientific discovery,” Nature Reviews Methods Primers 6, article 81 (published 2026-10-22), DOI https://doi.org/10.1038/s43586-026-00534-y. This is a methods primer/review, not a new experimental result.
2. Qile Jiang and George Karniadakis, “AgenticSciML: collaborative multi-agent systems for emergent discovery in scientific machine learning,” npj Artificial Intelligence 2, article 57 (published 2026-04-30), DOI https://doi.org/10.1038/s44387-026-00102-5. Full text: https://www.nature.com/articles/s44387-026-00102-5. Code: https://github.com/Qile-J/AgenticSciML.

Existing UQPU watches cover adjacent SPARC, Maestro, A-SR, PiT-PO and AI theorem-discovery work. This watch adds the October 2026 methods primer and the specific AgenticSciML system; it does not duplicate those earlier sources.

## Genuine contribution

The Nature Reviews primer organizes agentic science around task decomposition, memory, tool use, agent communication, single- versus multi-agent configurations, autonomy versus human-in-the-loop control, reproducible reporting and failure modes such as hallucination, tool misuse, limited interpretability and safety risk.

AgenticSciML implements a concrete multi-agent scientific-machine-learning workflow with more than ten specialized roles, including proposer, critic, retriever, evaluator, engineer, debugger and result analyst. It maintains a persistent knowledge base of prior solutions, ablations, error analyses and reports; uses structured debate and ensemble-guided evolutionary search; and evaluates candidate implementations against a common evaluator contract.

Across six curated PDE/operator-learning tasks, the authors report that the champion loss was 10 to more than 11,000 times lower than the single-agent root-solution loss, depending on task. This ratio is a benchmark loss ratio, not a speedup, general scientific-discovery multiplier or UQPU performance result. The paper reports LLM API costs of US$2.07–US$11.30 per end-to-end experiment and GPU training on NVIDIA A6000 systems; selected PDE tasks used multiple hours of GPU training. These are source-reported costs for the paper's setup.

## Limitations and evidence boundaries

- The empirical evaluation comprises six curated benchmark problems; transfer to multi-physics systems, laboratory experiments and other scientific domains requires adaptation.
- The authors state that output quality depends on knowledge-base coverage and retrieval grounding. Irrelevant retrieval can degrade results.
- Debate and justifications are mediated by LLMs and may not be physically rigorous without numerical verification.
- Evolutionary search overhead grows with evaluator cost. The paper calls for stronger solver-in-the-loop/adjoint checks and low-fidelity proxies.
- The reported loss ratios are not equivalent to reduced wall time, energy, cost per accepted physical law or improved experimental success.
- The public repository warns that its prompts and model-interaction code were developed against older model versions and may need retuning because of prompt drift and API changes.
- UQPU has not reproduced the paper's benchmark, measured its current-model API costs or tested a fresh-agent cold start. The work does not establish a physical law.

## Exact UQPU relevance

The most useful transfer is governance and reproducibility, not copying an agent count or performance claim. The project's canonical GitHub README, charter, invariant ledger, lane ownership, focused gaps, evidence labels, integration records and cold-start manifest already provide a persistent memory substrate. This literature suggests making the handoff itself a measurable benchmark: can an independent agent reconstruct the current frontier and continue correctly using only canonical GitHub artifacts, without private chat history or verbal briefing?

For INV-035, the agentic loop can generate and critique alternative equations, but a separate evaluator must enforce dimensions, symmetries, conservation, causality, scaling limits, held-out predictions, counterexamples and proof/experiment requirements. A proposer, critic or voting ensemble cannot certify its own physical claim.

For A-H, retain one primary owner per artifact, stable IDs, source hashes, a frozen evaluation contract, explicit negative evidence and integration links. Keep the eight operational lanes A-H; do not turn the paper's 10+ agent roles into a ninth lane.

## Falsifiable UQPU follow-up

Create an AGENTIC-HANDOFF-001 benchmark with a frozen, known-law/equation-discovery task and a separate cold-start continuation task:

1. Compare a single-agent baseline with a role-specialized multi-agent workflow on the same frozen task, dataset, source corpus, model versions, tools, prompts, wall-clock ceiling and hard token/API/compute budget.
2. Freeze the evaluator before candidate generation. Keep train/validation/test families and literature retrieval partitions disjoint; no test data may select prompts, models, methods or candidate equations.
3. Freeze roles for proposer, critic, source retriever, physics-constraint checker, counterexample search, independent evaluator, implementation/reproducer and integration publisher. The evaluator and reviewer must not be the candidate generator.
4. Measure exact known-law recovery, held-out error, constraint violations, false-discovery rate, counterexample detection, abstention, reproducibility, retries, human correction time, wall time, tokens/API cost, compute/energy and cost per accepted result.
5. Give a fresh agent only the canonical README, charter, invariant ledger, current handoff manifest and linked artifacts. Score whether it correctly identifies the newest main SHA, current batch, unmerged PRs, evidence class, blockers and next independent action without chat memory.
6. Require independent reproduction before any candidate is promoted beyond its source evidence class. Human review remains mandatory for material, energy, fusion and foundational-physics claims.

**Disposition:** source literature only. The repository's autonomous handoff principle is a project requirement; this paper motivates a falsifiable test of it but does not demonstrate that UQPU's handoff process already passes.
