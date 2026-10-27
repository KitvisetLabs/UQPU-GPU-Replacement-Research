# Literature watch — 2026-10-27: DIGEST closes the symbolic-regression feedback loop

**Access date:** 2026-10-27  
**Source:** Kaifeng Jin, Ruizhong Qiu, Zihao Li, Xiao Lin, Dongqi Fu, Yinglong Xia, Hong Li and Hanghang Tong, “DIGEST: Discovery-Guided LLM Tuning for Symbolic Regression,” official arXiv:2610.33880, submitted 2026-10-24: https://arxiv.org/abs/2610.33880  
**Evidence class:** `LITERATURE_ONLY`; claims below are author-reported and not reproduced by UQPU  
**Primary owner:** Lane A; cross-lane review by Lane F and Lane H

## Genuine novelty

DIGEST uses a pretrained decoder block as a symbolic policy to seed genetic-programming populations, then feeds high-quality discovered expressions back to update that policy online. The substantive methodological delta is a closed loop between explicit symbolic search and the LLM generator, rather than one-shot prompting or a fixed search grammar alone.

The preprint reports up to 2.59% improved recovery over its strongest competitor on two ground-truth benchmarks; at least 54.91% relative recovery improvement over LLM-based baselines while using at most 17.4% of their mean search time; and top accuracy across 122 BlackBox datasets. These headline values must be re-derived from the paper's metric definitions, exact baselines and resource accounting before they inform any project decision.

## Limitations

- This is a recent preprint, not an independently reproduced UQPU result.
- Benchmark recovery, numerical prediction, exact structural recovery and scientific validity are different outcomes.
- Search-time comparisons can omit model training, token/inference cost, candidate-evaluation budget, peak memory, failed runs or hardware differences unless explicitly normalized.
- Synthetic/BlackBox success does not establish generalization to new physical law families, new scales or noisy experimental data.
- No equation from this work is thereby a physical law; no hardware, material, energy, fusion or economic advantage follows from its abstract.

## Exact UQPU relevance

RG-EQN-008 already compares progressive composition, transformer-guided generation, LLM search control, structural guidance, STRIDE and MOSAIC-SR through the shared `equation_discovery_comparison.py` contract. DIGEST should be another candidate arm in that same interface. Do not create a competing benchmark schema.

## Falsifiable follow-up

1. Pin the paper version, source/code/license, datasets, model checkpoint, prompt/policy initialization, grammar, optimizer and exact baselines.
2. Freeze law-family-disjoint train/validation/test groups and held-out scales before tuning; hash the split manifests.
3. Match total compute and inference budgets, including LLM tokens/training, GP candidate evaluations, CPU/GPU time, wall time, peak memory and energy when measurable.
4. Use at least 30 preregistered seeds where feasible; retain failed seeds, false discoveries and counterexamples.
5. Report exact structural recovery only where the target/equivalence class is known, separately from held-out prediction, unit consistency, symmetry/conservation/causality checks and counterexample survival.
6. Reject a claimed advantage if it vanishes under equal resources, family-disjoint holdouts or scale transformations, or if the acceptance metric rewards an accurate but structurally false surrogate.

**Decision:** material candidate added to RG-EQN-008; no method winner or new physical law established. No real-QPU execution, accepted-fuel result, fusion result, WACC reduction or Data-Center-to-One-Phone milestone is claimed.
