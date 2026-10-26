# Research Gap RG-052 — principled expansion without post-hoc equation claims

**Opened:** 2026-10-26  
**Primary owner:** Lane A  
**Integration owner:** Lane F  
**Publication owner:** Lane H  
**Status:** LITERATURE_ONLY / READY_FOR_PREREGISTRATION / NOT_EXECUTED

## Objective

Determine whether principle-space expansion improves equation recovery/generalization under equal search resources without allowing anomaly-driven post-hoc accommodation or weakening physical evidence requirements.

## Evidence and source

Pu, Lin and Chen, “Principle-Evolvable Scientific Discovery via Uncertainty Minimization,” ICML 2026, PMLR 306:99931–99964, reports an expanding-principle-space discovery method and author-reported gains across four benchmarks. The paper is peer-reviewed, but UQPU has not reproduced its results. See the dated literature watch and EQN-PIEVO-001.

## Blockers

1. No source-exact reproduction, pinned environment or matched-budget ablation has been run by UQPU.
2. No sealed holdout or OOD result establishes whether principle updates generalize rather than accommodate observed anomalies.
3. No UQPU total-cost-per-accepted-formula result includes model calls, failed runs, candidate evaluation and human/compute resources.
4. The new metadata gate does not inspect mathematical truth; an independent evaluator, proof/simulation and domain-specific evidence remain necessary.

## Unlock criteria

- Freeze paper/code/data/dependency hashes and all splits.
- Compare static and expanding principle-space modes on the same synthetic ground-truth tasks, seeds, evaluator and resource budgets.
- Restrict expansion triggers to training/validation data and seal the held-out/extrapolation set.
- Retain failed runs, retries, counterexamples, false discoveries and all costs.
- Independently reproduce the accepted-formula scoring and uncertainty analysis.
- For physical candidates, check dimensions, symmetry, conservation, causality and limiting cases, then require falsifier, discriminating observable, experiment/proof and independent validation.

## Evidence boundary

The current work provides a literature watch, preregistration contract and metadata-only validator with nine focused unit tests. It does not reproduce PiEvo, generate a candidate physical equation, establish a new physical law, or demonstrate UQPU/energy/material/fuel/fusion/finance advantage. No QPU job or physical experiment was run.

The large append-only RESEARCH_GAPS.md was not rewritten from a partial extract. This is a supplemental gap artifact until reviewed and merged; canonical gap-ledger synchronization remains debt.
