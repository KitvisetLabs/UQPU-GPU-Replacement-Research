# Literature watch — 2026-10-24: AI-mathematics ranking is not proof or physical evidence

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy / mathematical discovery and publication  
**Feeds:** A, C, D, E, F, G, H, I; FND-001–006; EQN-001–006; INV-029–035  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`  
**Project evidence promotion:** none

## Surveillance result and date boundary

The 2026-10-24 searches did not identify a material primary result posted after the 2026-10-23 OptScientist/ancilla-QFI watch that changes UQPU's physics, provider, or economics gates. This article integrates a distinct, previously unconnected mathematical-discovery signal into the permanent equation-discovery pipeline; the source papers below retain their actual publication dates. It is not presented as a discovery published today.

## Sources reviewed

1. Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*, arXiv:2610.17090, submitted 2026-10-12. The survey reports that the public release on 2026-10-06 contained 722 AI-written mathematical manuscripts across 372 problem families. It explicitly says the survey did not compile or kernel-check a Lean development, and describes novelty judgments as provisional.  
   Source: https://arxiv.org/abs/2610.17090  
   Corpus: https://github.com/openai/math

2. Niket Patel, Ahmad Rammal, Amaury Hayat, Remi Munos and Julia Kempe, *Learning to Discover Interesting Mathematics*, arXiv:2609.28603, submitted 2026-09-23. The work studies ranking candidate theorems by a proof-difficulty/description-length proxy and reports reduced overlap with Mathlib under its evaluation. That is a candidate-selection result, not a claim that the selected mathematics changes physical law.  
   Source: https://arxiv.org/abs/2609.28603

3. Pavel Tikhonov et al., *LANTERN: Illuminating Hidden Mathematical Knowledge in Language Models*, arXiv:2609.32264, submitted 2026-09-26. The reported pipeline ranks sequence-relation candidates, then filters, generates hypotheses and applies executable and analytical checks. Its 62 reported verified relations are in the OEIS sequence-relation domain; they do not demonstrate physical-equation discovery.  
   Source: https://arxiv.org/abs/2609.32264

## Genuine method delta

These sources sharpen the separation between **candidate generation/ranking**, **mathematical verification**, **novelty/priority assessment**, and **physical validation**. A ranking model can allocate search effort, but its score is not a proof. A proof assistant can certify a formal statement from its encoded definitions and assumptions, but that alone does not show the definitions model nature or that an experiment confirms the intended physical system. Literature novelty checks are also fallible and must retain provenance.

The UQPU consequence is to treat discovery-interest scores as an optional queue-ordering feature only. Candidate promotion must remain governed by the existing `EquationHypothesis` contract, including an explicit incumbent model, units, assumptions, constraints, limiting cases, falsifier, discriminating observable, held-out result, proof/simulation/experiment provenance, and independent validation plan. The 2026-10-24 software delta additionally rejects non-finite held-out errors and non-integer/boolean independent-validation counts; otherwise an infinite baseline or a fractional “replication” could incorrectly satisfy a promotion gate.

## Limits and failure modes

- The Xie survey is a survey of selected source manuscripts; it does not independently certify the surveyed claims, and it reports no Lean kernel check for its own extracted inventory.
- Proof-difficulty and statement-length are proxies for mathematical interestingness, not measures of truth, usefulness, physical relevance, or downstream engineering value.
- LANTERN's application domain is mathematical sequence relations. Transfer to physical equations is untested.
- The three papers do not establish a new physical law, QPU advantage, memory compression, material property, fuel yield, fusion output, project WACC change, or commercial economics.
- Formal verification can faithfully prove a proposition under incorrect, incomplete, or physically irrelevant assumptions; domain adequacy and empirical tests remain separate gates.

## UQPU integration and falsifiable follow-up

**Proposed work item:** `EQN-OPT-001` — compare equation discovery with optimization-law discovery and candidate-ranking.

1. Freeze hashes for the generator/controller version, operator grammar, unit rules, train/validation/test splits, and known synthetic ground-truth models before search.
2. Include known dimensional equations, conservation/symmetry fixtures, ODE/PDE cases, and deliberately non-optimization counterexamples.
3. Compare direct equation search, optimization-law search, a conventional symbolic-regression baseline, and a null/random candidate generator under matched wall-clock, host-energy, token and search budgets.
4. Separate candidate-ranking metrics from proof/check success, held-out predictive error, identifiability, counterexample survival and independent replication.
5. Record false discoveries and failed candidates. Reject promotion if an alternative model with materially different mechanism remains observationally indistinguishable on the preregistered tests.
6. Report total cost of discovery as well as output quality; do not treat fewer model-output tokens as lower total compute or economic cost.
7. Only after the computational benchmark passes, design a domain-specific discriminating experiment. Passing a synthetic benchmark remains computational evidence, not empirical physics.

**Falsifier:** under matched budgets, ranking does not improve the rate of independently verified, identifiable candidates on held-out fixtures, or apparent gains disappear under negative controls and counterexample search.

## Lane A–I and pillar relevance

- **A — Quantum programming/runtime:** candidate ranking may prioritize compiler/runtime objective hypotheses, but accepted useful-output contracts and competitive classical baselines remain binding. Current real-target gate remains blocked pending authorized read-only target metadata.
- **B — Cloud/QPU:** no provider state or price can be inferred from these papers; keep provider/target provenance paired.
- **C — Memory/state/data movement:** include input/output size, state materialization, transfer and reconstruction in any objective; Hilbert-space dimension is not readable classical storage.
- **D and G — Devices/manufacturing:** symbolic fits can prioritize process hypotheses, but material/device claims require units, physical constraints, process-window evidence and independent measurement.
- **E — Biomass/materials/bio-oil/fusion:** candidate models may organize mass/energy balances and net-electric cost drivers; no feedstock, fuel, material or fusion measurement is added here.
- **F — Economics/evidence:** include search, proof, experiment, host, energy, financing, lifecycle and uncertainty costs; do not double-count coproduct credits or equate lower principal with lower WACC.
- **H — strategy/finance/future industries:** rank next experiments by expected uncertainty reduction per fully accounted cost, not by novelty score or ambition alone.
- **I — field-agnostic levitation research:** the same proof/physics/experiment separation applies; no vehicle lift or gravity-control claim is supported by these sources.

## Invariant contribution

- **INV-029:** no data-center-to-phone compression evidence; the follow-up is a possible search-efficiency tool only.
- **INV-030:** no elemental transmutation or universal carbon substitution claim.
- **INV-031:** no commercial bio-oil/biofuel cost claim.
- **INV-032:** no reliable net-delivered fusion-electricity claim.
- **INV-033:** no lower financing-rate/WACC claim; principal and time-to-evidence remain separately measurable.
- **INV-034:** reinforces the mathematics-first ladder and records false discoveries as first-class outcomes.
- **INV-035:** reinforces that generated equations are hypotheses until the incumbent assumption, changed prediction, falsifier, proof/experiment and independent validation path are explicit.

## Evidence and synchronization boundary

This article is `LITERATURE_ONLY`. It adds no project physical, material, device, real-QPU, fuel, electricity or economic evidence. The implementation tests described above are pending CI at authoring time. The canonical large append-only `WORKLOG.md` and `RESEARCH_GAPS.md` are not overwritten from partial connector reads; a dated cycle/gap artifact records this run and the remaining sync debt.
