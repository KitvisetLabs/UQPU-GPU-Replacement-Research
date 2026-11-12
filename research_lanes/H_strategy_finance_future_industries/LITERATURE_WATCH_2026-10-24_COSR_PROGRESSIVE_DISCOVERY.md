# Literature watch — 2026-10-24: progressive symbolic discovery of physical laws

**Primary owner:** Lane H — Ketskaew Chulamani / Kanusanan Pongpan­na strategy, finance and future-industry research  
**Evidence class:** `LITERATURE_ONLY`  
**Project reproduction:** `NOT EXECUTED`  
**Related work:** INV-034, INV-035, FND-006, EQN-001–006, `EQN-COSR-001`

## Primary sources and date

1. Mingkun Xia and Weiwei Zhang, **“Data-driven progressive discovery of physical laws,”** *Physical Review Research*, accepted 6 October 2026, DOI `10.1103/f2kp-pp4q`. The American Physical Society accepted-paper page describes Chain of Symbolic Regression (CoSR). Official journal record: https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q
2. Official preprint: https://arxiv.org/abs/2603.13727, submitted 14 March 2026.

The APS accepted-paper record says the framework composes interpretable knowledge units progressively rather than searching for one long expression in a single end-to-end pass. It reports demonstrations involving recovery of the Kepler-to-Newton discovery path, Rayleigh–Bénard convection, pipe flow, laser–metal interaction, and aircraft aerodynamic-coefficient scaling.

## Genuine novelty for this project

The new methodological hypothesis is that **the order and semantic decomposition of equation search may matter independently of the expression grammar**. The method is complementary to the adaptive-generator and evaluator-feedback work already tracked in the pending 2026-10-24 equation-discovery branch: those approaches adapt search from feedback, while CoSR motivates an explicit comparison of staged knowledge-unit composition against one-shot search.

This is relevant because UQPU's equation-discovery stack must not choose a candidate solely by one aggregate fit score. Intermediate units can expose assumptions, units, limiting cases and falsifiers earlier. But this benefit is a hypothesis to test, not an established advantage for UQPU.

## Evidence and limitations

- Evidence is an accepted peer-reviewed external method report, not UQPU project evidence. The APS page reviewed for this watch is an accepted-paper abstract; it states that supplementary material will be available upon publication of the version of record. This watch therefore does not claim to have independently audited the complete method, datasets, ablations or implementation.
- The reported examples cover selected physical/engineering tasks. They do not prove that progressive search wins across equation classes, noise regimes, units, non-identifiable models, or equal compute budgets.
- Recovering a known law is a method benchmark, not discovery of a new law. A more accurate empirical scaling relation is not automatically a fundamental equation.
- A staged method may accumulate early-stage bias, lock in a wrong intermediate unit, or consume more total evaluations than a one-shot baseline. These are explicit failure hypotheses, not details to hide.
- No UQPU model run, external API/model call, QPU job, material experiment, fuel test, fusion test, energy measurement or cost measurement was performed for this watch.

## Exact relevance across the eight lanes

- **A — Programming/workloads/compiler/runtime:** implement a reproducible offline comparison contract for progressive versus one-shot symbolic search; keep workload/evaluator semantics fixed.
- **B — Cloud/QPU/provider integration:** no provider interaction is required. Preserve provider-neutral architecture and zero paid jobs.
- **C — Memory/state/data movement:** commit split hashes and report storage/reconstruction overhead; equation search does not imply quantum state is readable classical memory.
- **D — Devices/chips/process/packaging:** a validated constitutive relation may later inform a device/process model, but only after independent physical validation.
- **E — Biomass/materials/bio-oil/fusion/cooling:** future candidates could model measured Pangola-carbon properties, biomass conversion yields, heat transfer or fusion subsystem response. No current result changes material suitability, accepted liquid-fuel cost or net fusion-electricity cost.
- **F — Economics/benchmarks/evidence/integration:** compare under identical evaluation, wall-time, expression-complexity and data caps; report false discoveries, failed searches, energy and cost only when measured.
- **G — Manufacturing equipment/software/factory systems:** only a validated, process-window-specific model could later influence D/G co-design; no fabrication or yield claim follows now.
- **H — Strategy/finance/publication:** the next capital gate is a cheap synthetic benchmark and independent replay before expensive experimental or model-training work. No WACC reduction is inferred.

## Falsifiable follow-up: EQN-COSR-001

1. Freeze a known-law synthetic benchmark, primitive grammar hash, evaluator version, train/validation/held-out SHA-256 digests, metric and all resource caps.
2. Compare one-shot symbolic regression with a staged chain under exactly equal candidate-evaluation count, wall-clock cap, maximum expression nodes and training-row cap. Include a shuffled-feedback/no-signal control in the full benchmark.
3. Measure exact recovery, held-out and out-of-domain error, structural distance, physics-constraint violations, false-discovery rate, expression complexity, runtime, memory and independent rerun agreement.
4. Include noise, dimensionally consistent distractors, correlated terms, a small true term, equivalent unit rescaling and a hidden held-out regime. Retain all failed equations and counterexamples.
5. Require independent replay before interpreting a positive result. If the staged chain fails under matched budgets or its gain disappears on held-out data, record that negative result and do not use the method as a project advantage claim.
6. Only after the synthetic gate passes should the team select a version-pinned, licensed public dataset. Experimental claims require an additional discriminating measurement and independent validation.

## Contribution to INV-029–035

- **INV-029:** creates a low-cost method-evaluation gate only; no phone-class capability, physical compression or lifecycle-cost evidence.
- **INV-030:** no elemental transmutation or Pangola-material substitution claim.
- **INV-031:** no accepted-fuel, yield, upgrading-cost or commercial bio-oil evidence.
- **INV-032:** no net delivered fusion electricity or plant-cost evidence.
- **INV-033:** no change in financing rate/WACC; a staged software gate may reduce capital at risk only if it actually falsifies a costly idea earlier.
- **INV-034:** advances mathematics-first search methodology while preserving known limits.
- **INV-035:** adds a falsifiable generator-organization hypothesis; incumbent equations remain binding and all generated relations remain hypotheses until validated.

## Surveillance boundary

The 2026-10-23 repository watch already records optimization-law discovery and an assumption-scoped ancilla-QFI boundary; pending 2026-10-24 work also covers adaptive equation search, formal proof search, constitutive-law methods, and a Gaussian-repeater no-go theorem. This article adds the distinct progressive-chain comparison. No newly reviewed result justifies changing established physical laws or promoting a UQPU, materials, fuel, fusion, or financing claim.
