# RG-042 — Progressive symbolic discovery versus one-shot equation search

**Status:** `PREREGISTERED / NOT EXECUTED / MODEL_ONLY`  
**Date:** 2026-10-24  
**Primary owner:** Lane A; Lane H owns external literature context; Lane F owns benchmark accounting.  
**Related:** INV-034, INV-035, FND-006, EQN-001–006, `EQN-COSR-001`.

## Objective

Determine whether progressive composition of interpretable equation units improves exact recovery or genuinely held-out generalization over a one-shot symbolic-regression baseline under matched resource caps.

## Current evidence

- External method signal: Xia and Zhang, “Data-driven progressive discovery of physical laws,” *Physical Review Research*, accepted 2026-10-06, DOI 10.1103/f2kp-pp4q; arXiv:2603.13727.
- Local proposed validator and its 18 focused tests passed in an isolated temporary harness. This is test evidence for the proposed schema guard only; it is not an exact checkout of the repository and is not hosted CI evidence.
- No CoSR reproduction, equation-search benchmark, external dataset execution, independent scientific replication, or physical experiment has been run by UQPU.

## Blockers

- No frozen benchmark dataset/grammar/evaluator/split digests are committed for this experiment.
- No equal-budget one-shot versus staged result exists.
- No independent replay exists.
- The accepted-paper abstract is not sufficient to audit all algorithm details, ablations, datasets or compute accounting.

## Required unlock criteria

1. Exact equality of candidate-evaluation, wall-clock, expression-size and training-data caps across arms.
2. Distinct SHA-256 hashes for train, validation and held-out data; held-out data remains blind until the search is frozen.
3. Explicit dimensional, symmetry, conservation and causality review for every stage, with reasons for non-applicable checks.
4. At least two ordered progressive stages, with every later stage depending only on earlier units and total stage evaluations equal to the declared progressive budget.
5. Mandatory noise, distractor, non-identifiability, unit-rescaling, small-true-term and shuffled-feedback counterexamples.
6. Report exact recovery, held-out/OOD error, structural distance, constraint violations, false-discovery rate, runtime, memory, energy/cost when measured, and failed candidates.
7. Independent replay before a positive method claim. A method result never promotes an AI-generated equation to physical law.

## Next experiment

Run the offline synthetic known-law benchmark after the protocol and grammar are frozen. Compare one-shot and progressive search under the same budgets. If the staged method fails to generalize, requires more resources, or is sensitive to equivalent unit changes, retain the failure and close or revise the hypothesis rather than relaxing the acceptance criteria.

## Mission/evidence boundary

This gap does not change any current physical limit and does not demonstrate quantum advantage, Data-Center-to-One-Phone feasibility, universal RAM/VRAM/storage replacement, Pangola-carbon material performance, commercial low-cost bio-oil, commercial low-cost fusion, or reduced project WACC. Provider calls and QPU jobs remain zero.
