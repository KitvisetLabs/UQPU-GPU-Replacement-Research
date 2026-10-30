# Research gap — reproducible agentic scientific discovery and cold-start handoff

**Opened:** 2026-10-30  
**Work item:** AGENTIC-HANDOFF-001  
**Gap ID:** RG-AGENTIC-HANDOFF-001  
**Primary owner:** Lane H — research operating model/publication  
**Cross-lane owners:** A (task/evaluator), B (tool/provider provenance), C (artifact/memory), D/E (physics/material constraints), F (evidence/cost), G (workflow/manufacturing)  
**Status:** PROTOCOL_ONLY / REPRODUCTION_NOT_RUN  
**Related:** INV-034, INV-035, EQN-001–006

## Objective

Measure whether an independent agent can resume a research task from canonical GitHub memory without private chat history or verbal briefing, and whether a role-specialized multi-agent workflow improves independently accepted results over a single-agent baseline under identical task, data and resource budgets.

## Source basis

- Feng et al., Nature Reviews Methods Primers 6, 81 (published 2026-10-22), DOI 10.1038/s43586-026-00534-y.
- Jiang and Karniadakis, npj Artificial Intelligence 2, 57 (published 2026-04-30), DOI 10.1038/s44387-026-00102-5.
- See [literature watch](literature_watch/2026-10-30-agentic-ai-scientific-discovery-primer.md).

## Proposed benchmark

Freeze two tasks separately:

**Task A — known-law recovery.** Use a public/synthetic known-law dataset with grouped train/validation/test regimes and a frozen equation-discovery evaluator. The task tests methodology and false-discovery control, not new physical-law discovery.

**Task B — cold-start continuation.** Give a fresh agent only the canonical README, PROJECT_CHARTER, VERSION_INVARIANTS, GOALS, research operating system, open-frontier directive, current handoff manifest, latest batch/gap and linked lane artifacts. Do not provide prior chat messages.

Compare:
- single-agent baseline;
- role-specialized multi-agent workflow with proposer, critic, source retriever, physics-constraint checker, counterexample search, independent evaluator, reproducer and integration publisher.

## Frozen controls

Hold model versions, prompts, retrieval corpus, tool permissions, dataset, split certificate, evaluator, wall-clock ceiling, token/API budget, compute budget and stopping rules constant. Freeze the evaluator before candidate generation. Keep test regimes inaccessible to prompt/method selection. Every agent output must include source hashes, owner, stable ID, evidence class and next independent action.

## Metrics

- exact known-law recovery and held-out error by law family/scale/regime;
- dimensional/symmetry/conservation/causality/limiting-case violations;
- false-discovery rate, counterexample recall and justified abstention;
- independent reproduction rate and source/hash integrity;
- cold-start task reconstruction accuracy and ability to identify current main SHA, newest committed batch, open/unmerged PRs, evidence status, blockers and next gate;
- wall time, human correction time, tool calls, tokens/API cost, CPU/GPU time, memory, energy where measurable, retries and cost per independently accepted result.

## Pass/fail rules

A candidate is not accepted because agents agree, vote for it or produce a plausible explanation. Acceptance requires the frozen evaluator, held-out tests, counterexample search and independent reproduction. Physical claims additionally require experiment/proof and independent validation. A cold-start pass requires correct reconstruction from GitHub artifacts alone; any dependence on hidden chat memory is a failure.

## Nonclaims

The paper-reported 10–11,000x loss ratios and API cost figures from AgenticSciML are not UQPU performance estimates. No agentic workflow has been benchmarked by this project in this cycle. This gap does not establish autonomous scientific discovery, a new physical law or reduced R&D cost.
