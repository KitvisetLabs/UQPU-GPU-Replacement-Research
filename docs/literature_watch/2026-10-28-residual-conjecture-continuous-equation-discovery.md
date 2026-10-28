# Literature watch — residual-informed and conjecture-guided equation discovery

**Date:** 2026-10-28  
**Evidence class:** LITERATURE_ONLY  
**Project invariants:** INV-034 / INV-035  
**Primary owner:** Lane H for literature synthesis; Lane A owns the matched-comparison protocol; Lane F owns acceptance/economic accounting.

## Primary sources and the actual delta

1. **RISR — Residual-Informed Scientific Equation Discovery with Large Language Models** (Haobo Li et al., arXiv, posted 2026-10-08): https://arxiv.org/abs/2610.11387. The method encodes aligned inputs, observations, predictions and pointwise residuals to guide formula proposals, then estimates the utility of candidate corrections. The authors report ID/OOD equation-recovery metrics on LLM-SRBench and comparisons with reported baselines using the same backbone. The genuine methodological delta is richer, input-dependent feedback rather than only a scalar aggregate fit score. These are author-reported results, not UQPU replication.

2. **Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench** (Yuxiao Hu et al., arXiv, posted 2026-10-13): https://arxiv.org/abs/2610.18938. The paper shifts the unit of investigation from a single expression to competing scientific conjectures and interactive experiments. ClosureBench is described as 60 closure-discovery tasks across five domains embedded in known PDE systems, with OpenFOAM-controlled experimental conditions and metrics for evidence faithfulness, mechanism insight and experimental effectiveness. This is a different task class from static equation recovery; its scores must not be pooled with LLM-SRBench or static symbolic-regression scores.

3. **MorphingNet — Symbolic Regression Where the Network Is the Formula** (Jincheng Gao, Jiahe Yi and Shuo Sun, arXiv, posted 2026-10-14): https://arxiv.org/abs/2610.19942. The approach parameterizes formula units continuously (including rational and complex exponential–logarithm families) and performs structure recovery after fitting. The authors report strong SRBench recovery and large-data speedups. The potential novelty is a continuous-optimization route around a fixed operator-library search, not proof that the learned expression is a physical law. Its speed and accuracy claims require independent, hardware- and budget-matched reproduction.

## Synthesis

These sources motivate three distinct research axes, not a leaderboard:
- **residual feedback:** whether error structure guides useful corrections beyond a scalar score;
- **conjecture/experiment loop:** whether explicit competing explanations and active measurements improve the quality of scientific conclusions;
- **formula parameterization:** whether continuous parameterization changes recovery, complexity, scaling and compute cost.

Their tasks, models, datasets, resource budgets and reported metrics differ. Headline scores cannot establish cross-paper superiority. The official arXiv records are preprints and their claims remain external evidence until independently reproduced.

## UQPU relevance

- **Lane A:** candidate-generation and equation-search tooling; preserve the existing schema-v4 matched comparison and search-width experiment as separate factors.
- **Lane F:** include training plus inference, CPU/GPU/accelerator time, memory, candidate evaluations, generated tokens, retries, energy when measurable and cost per independently accepted candidate.
- **Lane C:** retain data movement, residual-tensor storage, peak memory and reconstruction costs.
- **Lanes D/G:** a discovered constitutive or process equation would still need measurement traceability, process-window/yield validation, metrology and manufacturability.
- **Lane E:** potential future applications include biomass conversion/upgrading kinetics, material-property models and fusion-system submodels only where suitable source data and a causal model exist. No BIO-001 or FUS-001 evidence is added by these papers.
- **Lanes B/H:** no provider claim or financing/market claim follows. Preserve provider neutrality and multilingual strategic references.

## Falsifiable follow-up

1. Freeze source, license, acquisition, preprocessing, model/checkpoint, code, prompt/operator bundle, runtime/container, units, acceptance rules and group-disjoint split manifests.
2. On a **static, source-accessible equation dataset**, compare an existing baseline, residual-informed correction and continuous-formula parameterization only after their code and license are verified. Use the same whole-law-family and scale-held-out data, at least 30 shared preregistered seeds, matched hard resource ceilings and one cost basis. Report held-out error, structural recovery where a target exists, complexity, constraint violations, counterexamples, false discoveries, failures and total resources.
3. Keep conjecture-guided active experimentation on a **separate interactive track**. Compare active versus passive acquisition under equal simulation/experiment-call and compute budgets; score evidence faithfulness, mechanism insight and experimental effectiveness alongside predictive/constraint metrics. Never pool these scores with static SR results.
4. Enforce dimensional, symmetry, conservation, causality and known-limit checks; run adversarial counterexample searches; preserve negative outcomes; independently reproduce any claimed method gain.
5. Reject a claimed gain if it disappears on held-out law families/scales, is explained by leakage or unequal budgets, or increases false discoveries/constraint violations. No AI-generated equation becomes a physical law by declaration.

**Status:** LITERATURE_ONLY / proposed experiment. No UQPU benchmark, real-QPU job, physical experiment, material/fuel/electricity result, new physical law or economic advantage is claimed.
