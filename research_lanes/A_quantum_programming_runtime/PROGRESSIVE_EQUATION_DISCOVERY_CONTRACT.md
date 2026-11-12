# EQN-COSR-001 — Progressive Symbolic Discovery Comparison Contract

**Primary owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-cutting:** INV-034, INV-035, FND-006, EQN-001–006; Lane H owns the literature watch and Lane F owns benchmark accounting.  
**Status:** `MODEL_ONLY / PREREGISTERED-CONTRACT / NOT EXECUTED`  
**Date:** 2026-10-24  
**Canonical starting main:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Question

Does progressive composition of interpretable knowledge units improve equation recovery or held-out generalization over a one-shot symbolic-regression search when the two methods receive the same data, grammar, evaluator, and declared resource caps?

This is a test of a **search strategy**, not a proposal to replace any established physical law. The accepted-paper abstract for Xia and Zhang's Chain of Symbolic Regression (CoSR) motivates the question; this artifact is not an implementation of CoSR and does not reproduce the paper.

## Comparison arms

1. **One-shot baseline:** search one expression against the frozen training split.
2. **Progressive chain:** discover at least two ordered, interpretable units; later units must reference earlier units. The final composition is scored only after its form is frozen.
3. **No-signal / shuffled-feedback control:** required in the full benchmark to detect gains caused by leakage, chance, or the evaluator rather than useful stage structure.

The first software gate validates only the two primary arms' preregistration metadata. The full benchmark remains `NOT EXECUTED` until datasets, grammar, evaluator, and budgets are frozen and a runner records results.

## Hard comparability requirements

- Same incumbent model, primitive grammar hash, training data, validation data, held-out data, evaluator version, metric and optimization direction.
- Three separate SHA-256 digests for train, validation and held-out data; all must be distinct.
- Exact equality of resource caps across arms: candidate evaluations, wall-clock seconds, maximum expression nodes, and maximum training rows.
- The progressive stage evaluation counts must sum exactly to the progressive-arm candidate-evaluation budget.
- The held-out split remains blind until model selection, repair, and all stage decisions are frozen. It must not be used for prompt selection, pruning, parameter fitting, or stage construction.
- Every stage records variables with units, dimensional-consistency review, symmetry review, conservation review, causality review, limiting cases, a falsifier and a discriminating observable. A non-applicable constraint requires a specific reason.
- Candidate failures, invalid equations, counterexamples, timeout, resource exhaustion and null results are retained. Do not report only the best fit.
- The evaluator and expression grammar must be version-pinned. Any later change creates a new experiment ID and new split/budget commitments.
- Offline preregistration must make zero provider calls and zero QPU jobs.

## Primary metrics

1. Exact symbolic recovery on known-law fixtures.
2. Held-out and out-of-domain prediction error.
3. Normalized structural distance when exact recovery fails.
4. Dimensional/symmetry/conservation/causality constraint violations.
5. False-discovery rate and counterexample count.
6. Expression complexity, candidate evaluations, wall time, peak memory and failed-search rate.
7. Independent rerun agreement.
8. Energy and direct cost only when measured with provenance; unknown values remain unknown, not zero.

## Mandatory adversarial fixtures

- Noiseless known law with a known limiting case.
- Noisy observations and unit-consistent distractor terms.
- Correlated or non-identifiable terms.
- A real but small coefficient that a parsimony threshold might incorrectly remove.
- Equivalent unit or basis rescaling.
- A hidden held-out regime that differs from the training distribution.
- A shuffled-feedback/no-signal control.

## Pass/fail interpretation

A pass requires a preregistered, held-out improvement over the matched one-shot baseline without an increase in unreported constraint violations or false discoveries, followed by independent replay. A result that improves only training fit, only one seed, or only under a larger budget fails the comparison. If both methods fail, record the failure and preserve the counterexample.

A pass validates at most this equation-search workflow on the tested datasets. It does not establish a new physical law, quantum advantage, material substitution, lower fuel/electricity cost, lower WACC, or Data-Center-to-One-Phone feasibility. Any physical-law challenge must separately identify the incumbent assumption, alternative equation, dimensional and symmetry/conservation/causality checks, limiting/scaling cases, falsifier, discriminating observable, held-out prediction, proof/experiment and independent validation path.

## Implementation

`software/uqpu-prototype/uqpu/progressive_equation_discovery.py` provides a dependency-free preregistration guard. `software/uqpu-prototype/tests/test_progressive_equation_discovery.py` covers malformed splits, unequal budgets, incorrect stage accounting, dependency errors, held-out leakage, incomplete physics checks, evidence promotion and provider/QPU execution attempts.

The validator is a schema gate, not the search algorithm, a paper reproduction, or evidence that progressive discovery performs better. The first full benchmark should begin with deterministic synthetic known-law fixtures and only then expand to version-pinned public datasets with documented license and provenance.

## RG-045 split-membership certificate

The plan now carries a versioned DataSplits membership manifest with a frozen source-dataset SHA-256, an explicit sample-ID namespace, stable train/validation/held-out IDs, pinned schema and canonicalization versions, per-split manifest digests, and a full certificate digest. Canonical JSON uses sorted keys, UTF-8, compact separators, and sorted sample IDs.

Validation fails closed on pairwise split overlap, duplicate IDs within a split, empty splits, non-string or non-normalized IDs, unsupported schema/canonicalization versions, malformed digests, and manifest/data digest mismatch. The adversarial case with different declared digests but an overlapping record ID is explicitly tested.

**Evidence boundary:** this is an offline structural protocol guard (MODEL_ONLY), not proof that IDs were honestly extracted from raw dataset bytes. The actual dataset loader must independently verify the frozen source-byte digest and derive IDs from that exact dataset before a benchmark may consume the certificate. No QPU/provider calls are made.
