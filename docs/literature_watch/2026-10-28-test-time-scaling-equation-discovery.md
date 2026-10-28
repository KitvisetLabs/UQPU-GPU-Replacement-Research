# Literature watch — test-time scaling for scientific equation discovery

**Watch date:** 2026-10-28  
**Evidence class:** PEER_REVIEWED_METHOD_PAPER / EXTERNAL_LITERATURE_ONLY  
**Primary program:** INV-035, EQN-001, EQN-002, EQN-008; Lane A owner with Lane F evidence review and Lane H publication integration  
**Source reviewed:** official ACL Anthology record and abstract; a full independent reproduction has not been performed.

## Primary source

Haowei Lin, Hubert Lim, Xiangyu Wang, Letian Huang, and Di He, “Test-Time Scaling for Scientific Equation Discovery,” *Proceedings of EMNLP 2026*, pp. 8122–8143 (2026).  
Official publication page: https://aclanthology.org/2026.emnlp-main.354/  
Related preprint record: https://arxiv.org/abs/2608.28660

## What is genuinely new

The paper frames LLM-driven equation discovery as a common test-time compute-allocation problem covering Best-of-N sampling, sequential refinement, tree search, and evolution-style search. In the reported LLM-SRBench experiments, the authors state that search width is the dominant allocation parameter under their tested fixed-budget comparisons; the best width generally increases with available compute, while the population/branching split and controller choice matter less. Parallel width can improve wall-clock efficiency when the verifier supplies informative feedback.

This is a useful experimental-design hypothesis for UQPU's matched comparison, not a universal law about scientific discovery. It suggests that search width must be treated as a preregistered factor instead of allowing each method to use its own undocumented search policy.

## Limitations and evidence boundary

- The reported results belong to the paper's tasks, models, verifier, controller implementations and resource definitions. They do not establish that width dominates for every equation family, physics domain, or hardware budget.
- The UQPU project has not independently reproduced LLM-SRBench or the paper's results.
- A verifier can reward leakage, expression-form similarity or a narrow validation metric. More candidate throughput is not equivalent to more accepted equations.
- The paper does not establish a new physical law, defeat a physical lower bound, or demonstrate a QPU advantage, energy saving, material substitution, saleable bio-oil, net fusion electricity, lower financing rate, or Data-Center-to-Phone compression.
- The official publication page/abstract was the source reviewed for this watch. Exact protocol details and full-paper tables must be checked before claiming a faithful replication.

## Exact UQPU relevance

**Lane A / EQN-002 and RG-EQN-008:** add a controlled search-width sweep to the existing schema-v4 matched comparison. Keep model/checkpoint, source revision, prompt/operator bundle except the declared width factor, runtime, data provenance, preprocessing, grammar, unit rules, acceptance rules, group-disjoint split, seed set and hard resource ceilings pinned. Treat each width as a separate method/configuration arm; keep each arm's configuration hash constant across seeds.

**Lane F:** score accepted-candidate rate and held-out predictive error alongside constraint violations, counterexamples, false discoveries, failed searches/retries, wall-clock, CPU-core time, peak memory, generated tokens, candidate evaluations, measured total cost and energy where measurable. Do not mix cost bases or compare runs with unequal total resource ceilings.

**Lane H / INV-034–035:** preserve the source link and the distinction between a published method result and UQPU evidence. A successful symbolic fit or a formally valid derivation remains below the physical-law gate until assumptions, units, symmetries, conservation, causality, limiting cases, held-out prediction, counterexamples and independent validation are satisfied.

The immediate relevance to INV-029–033 is indirect: better discovery methodology could help explore computing, materials, fuel, fusion and finance hypotheses, but no downstream technical or economic gain follows until those hypotheses pass their own evidence gates.

## Proposed falsifiable follow-up

1. Before execution, freeze a source-accessible dataset and license/acquisition manifest; hash data, preprocessing, grammar, unit schema, acceptance rules, group-disjoint train/validation/test partitions and held-out group manifest.
2. Use one fixed LLM-SR controller and preregister width arms (for example 1, 2, 4, 8, and 16) under the **same** total per-run wall-clock, CPU-core, memory, accelerator, candidate-evaluation, token and cost ceilings. The exact width grid may be adjusted only before registration to fit the pinned environment.
3. Use at least 30 shared preregistered seeds per arm, with method source/config/runtime hashes fixed across each arm's seeds. Reserve whole law families and scales for blind tests; random-point splits alone are insufficient.
4. Apply the same independent equation-acceptance gate to every candidate. Retain all failures, counterexamples, retries and false discoveries. Report uncertainty intervals and full resource use; do not announce a winner from the paper's reported results.
5. Falsify a width advantage if it disappears on held-out law families/scales, is explained by unequal resources or leakage, worsens accepted-candidate quality/false-discovery rate, or only improves wall-clock while consuming more total resources without improving accepted output per cost.

**Disposition:** add as a candidate arm to RG-EQN-008. Literature-only; no UQPU benchmark ran and no equation or physical law is promoted.
