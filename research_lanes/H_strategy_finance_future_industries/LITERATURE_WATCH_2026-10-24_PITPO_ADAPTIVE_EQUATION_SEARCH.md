# Literature watch: adaptive physics-informed equation search and theorem-scope audit

Date: 2026-10-24
Primary owner: Lane H - strategy, finance and future-industry research
Work ID: PITPO-WATCH-001
Evidence class: LITERATURE_ONLY
Status: REVIEWED; UQPU REPRODUCTION NOT EXECUTED
Canonical main at cycle start: c7b5958af58fad04a101ef5c6abf6a29293c867e
Source branch at cycle start: research/2026-10-24-equation-discovery-audit-v2
Source head at cycle start: 76f6f5957e280893e713f1983f0390a4995675a9

## Primary source and genuine novelty

Wang et al., "LLM-Based Scientific Equation Discovery via Physics-Informed Token-Regularized Policy Optimization," arXiv:2602.10576v2, revised 2026-07-27 and listed as accepted at KDD 2026. The paper introduces PiT-PO: an LLM is adapted during the symbolic-search loop using policy optimization, while a candidate evaluator supplies hierarchical physical-constraint rewards and token-level penalties intended to discourage redundant terms. The authors report benchmark improvements and a periodic-hill turbulence-closure case study. These are author-reported external results; UQPU has not independently reproduced them.

Primary references:
- Official preprint and revision history: https://arxiv.org/abs/2602.10576
- Full text, including the Support Exclusion Theorem assumptions: https://arxiv.org/html/2602.10576v2
- Authors' implementation and experiment configuration: https://github.com/CAS-CLab/PiT-PO
- Related evaluator-guided quantum-circuit search preprint, submitted 2026-10-15: https://arxiv.org/abs/2610.22367
- Related peer-reviewed graph-based solid constitutive-law discovery: https://www.science.org/doi/10.1126/sciadv.aec0989

## What is genuinely new for UQPU

The relevant change is not a new physical law. It is a candidate search-controller design: evaluation feedback can update the generator itself, rather than only being returned through prompts or an external evolutionary population. This creates a concrete comparison for EQN-002 and EXP-DESIGN work.

The full-text paper also makes an important distinction that must be preserved. Its Support Exclusion Theorem is conditional on a finite candidate dictionary, a sparse true support, bounded nonzero true coefficients, a positive empirical Gram diagonal, a partially correct active support, and a specific interference inequality. The paper's practical normalized-coefficient threshold rho = 1e-2 is a heuristic for identifying potentially redundant terms; it is not, by itself, the theorem's guarantee. In addition, comparing raw coefficient magnitudes can be unit- or basis-scaling-sensitive unless the representation is normalized and the normalization is documented.

## Limitations and evidence class

- The KDD paper is peer-reviewed method evidence, not UQPU project evidence.
- Reported benchmark scores, OOD errors and turbulence-model results have not been independently reproduced by this project.
- A lower symbolic-regression error does not establish causality, a fundamental physical law, a better quantum algorithm, or an engineering/economic advantage.
- The upstream repository describes GPU-based training requirements; no GPU training run, model API call or external experiment was executed in this cycle.
- Any use of a theorem-derived penalty must check the theorem's assumptions for the actual dictionary, data, coefficient bounds and Gram/interference quantities. If any assumption is unverified, the penalty remains heuristic and must be ablated.
- The graph-based constitutive-law paper concerns external material datasets and does not establish any Pangola-derived material performance.
- The October 15 quantum-circuit-search preprint reports circuit-resource reductions on its tasks, not an end-to-end UQPU useful-task advantage.

## Exact UQPU relevance

- Lane A: compare static prompting, adaptive in-search policy updates, classical symbolic-regression search and a shuffled-feedback control under identical declared resource caps.
- Lane F: count evaluator calls, generation/fine-tuning time, tokens, retries, storage, independent replay, measured energy and total direct cost per accepted useful model. If energy or direct cost is unknown, the corresponding comparison is unavailable rather than zero.
- Lane C: keep dataset hashes, split boundaries, intermediate-state storage and reconstruction costs visible; no quantum-state or classical-memory equivalence follows.
- Lanes D/G: only a reproducible constitutive relation can become an input to device/process co-design, and then only after target-specific material or device validation.
- Lane E: no Pangola carbon, accepted bio-oil, net fusion electricity or cooling result follows from these equation-search methods.
- Lane B: this is an offline research path; no provider call or QPU submission is required.
- Lane H: record method provenance, capital/time requirements and negative results without turning literature into a funding or WACC claim.
- INV-034/035: mathematics and AI may generate hypotheses, but established physical constraints remain binding for engineering claims.

## Proposed falsifiable follow-up: PITPO-AUDIT-001 / EQN-002C

Run a preregistered synthetic pilot with known ground-truth equations, fixed train/validation/held-out digests and held-out whole trajectories or parameter groups. Compare:
1. static LLM symbolic-regression baseline;
2. adaptive in-search policy optimization;
3. a classical symbolic-regression baseline;
4. a shuffled-feedback/no-signal control.

Use the same declared caps for wall time, evaluator calls, generated tokens, optional energy and optional direct cost. The initial proposed cap is 900 seconds, 3,000 evaluator calls and 100,000 generated tokens per method/task/seed; energy and cost caps remain null until they can be measured defensibly. Use three fixed seeds across three frozen synthetic tasks for the first pilot. Count all fine-tuning, evaluation, retries and independent replay in total time/cost.

Primary metrics: exact symbolic recovery where ground truth is known; held-out and OOD error; physical-constraint violations; false-discovery count; candidate count; accepted useful models; independent replay count; wall time; evaluator calls; generated tokens; measured energy when available; direct cost per accepted model.

Mandatory counterexamples:
- a true but small coefficient term that falls below the rho threshold;
- correlated or nearly collinear basis functions;
- a missing true basis term;
- equivalent data expressed under rescaled units or basis normalization;
- shuffled feedback and no-signal controls.

A term may be labelled theorem-certified redundant only when the theorem's assumptions and full inequality are actually checked. Otherwise label the pruning decision heuristic and include an ablation. Equivalent unit changes must not silently change a claimed physical conclusion; if the threshold classification changes under an equivalent rescaling, reject universal theorem-promotion for that heuristic.

Falsifiers include no practically meaningful held-out gain, worse OOD generalization, higher false-discovery rate, failure of independent replay, resource-cap violations, or unit/basis rescaling that changes a claimed theorem guarantee. Report paired uncertainty intervals and cost per accepted useful model; do not claim an improvement if the accepted-model denominator is zero or cost is unknown.

Status: PROPOSED / NOT EXECUTED. No physical law, real-QPU advantage, material substitution, fuel/electricity result, project-finance result or Data-Center-to-Phone achievement is claimed.
