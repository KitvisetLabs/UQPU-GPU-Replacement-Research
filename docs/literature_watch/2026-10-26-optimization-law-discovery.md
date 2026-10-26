# Literature watch — 2026-10-26: optimization-law discovery as a distinct equation-search family

**Source date:** 2026-10-20  
**Accessed:** 2026-10-26  
**Source:** Ma ZhenYao, Yue Liang and Jian-Qiao Zhu, “OptScientist: Automated Discovery of Optimization Laws,” arXiv:2610.28562v1.  
**Official preprint:** https://arxiv.org/abs/2610.28562  
**Evidence class:** OFFICIAL PREPRINT / AUTHOR-REPORTED SYNTHETIC-BENCHMARK AND HELD-OUT-PREDICTION RESULTS  
**UQPU reproduction:** none; no physical law or technology advantage promoted.

## Genuine novelty

OptScientist targets a different discovery object from ordinary input-output symbolic regression: it first learns a representation of an optimization problem and then distills a compact symbolic objective/constraint law. An agentic loop combines literature priors, candidate discovery, interpretation and suggestions for further data collection. The authors introduce OptFeynman, a set of 99 optimization tasks derived from physics equations, and report high exact preference-order recovery on held-out contexts. They also report held-out predictive results on human risky-choice and central-bank policy datasets.

The useful methodological distinction is **objective-and-constraint recovery**, not simply fitting a compact formula to observed outputs. This is potentially relevant to UQPU's optimization workloads, QUBO/QAOA objective construction and FND-006 mathematics-first search, but it does not replace exact workload semantics, feasible-set validation, reference certificates or competitive classical baselines.

## Limitations and evidence boundary

- This is an arXiv v1 preprint, not a peer-reviewed result as of the access date.
- OptFeynman is generated from known physics equations and known optimization structure; successful recovery on that benchmark does not establish discovery of an unknown natural law.
- Real-data applications are predictive and interpretive. A compact optimization objective need not be the unique or true causal mechanism behind decisions.
- The method assumes that a useful optimization representation exists; the paper acknowledges that discovery can fail when the underlying structure deviates substantially from that assumption.
- The reported token-efficiency advantage is not a total-compute or energy comparison. Training, latent representation learning, symbolic search, rejected candidates, wall time, memory and energy must be accounted for.
- UQPU has not reproduced the preprint, run its models, independently verified the datasets or established any new equation.

## Exact relevance across A–H

- **A — Workloads/compiler/runtime:** add optimization-law discovery as a separate candidate family. Require objective-value and feasible-set equivalence, not only matching preferred choices, before a candidate can enter a QUBO/QAOA pipeline.
- **B — Cloud/QPU:** any later quantum comparison must use one frozen workload contract, provider-neutral lowering, the same target's results and pricing, and a simulator/dry-run gate before authorized hardware execution.
- **C — State/memory/data movement:** record raw and latent data sizes, reconstruction, memory, transfers and host work; a compact symbolic objective is not equivalent to a smaller physical memory footprint.
- **D/G — Device and factory co-design:** constitutive/process optimization may be a later test domain only with measured variables, units, constraints, held-out material/device families and independent validation.
- **E — Biomass/materials/fusion:** the method could generate candidate process objectives for pyrolysis, upgrading or net-electric plant optimization, but this paper supplies no Pangola-carbon qualification, accepted bio-oil, fusion availability or net-electricity evidence.
- **F — Evidence/economics:** compare discovery cost per accepted useful model, counting model training, search, validation, failed runs, wall time, memory and measured energy. Do not treat fewer generated tokens as lower lifecycle cost.
- **H — Strategy/publication:** preserve provenance and the distinction between strategic hypotheses, model results and experimentally supported claims.

## Falsifiable follow-up

1. Add OptScientist as a separate arm only after source/version, code, license, data and dependency provenance are pinned.
2. Use law-family-disjoint and held-out-scale splits with a canonical record/group manifest; keep test groups sealed during method selection.
3. Compare one-shot symbolic regression, progressive composition, search-controlled SR, structural guidance and optimization-law discovery under the same total wall-time, CPU/GPU, memory and evaluation budgets.
4. Use at least 30 preregistered seeds where compute permits. Report exact-law/equivalence recovery where ground truth is known, held-out prediction, constraint violations, counterexamples, failed searches and cost per accepted candidate.
5. For real physical data, preregister a discriminating experiment and compare against a non-optimization model; reject the optimization-law hypothesis if it fails held-out predictions, violates dimensions/symmetries/conservation or cannot survive independent replication.

## Project disposition

**Status: LITERATURE_ONLY / METHOD HYPOTHESIS.** This source broadens EQN-002/003's candidate family. It does not relax INV-035: current physics remains binding, and any candidate must pass constraints, held-out generalization, counterexample search, proof/experiment and independent validation before technology or economic claims can be made.
