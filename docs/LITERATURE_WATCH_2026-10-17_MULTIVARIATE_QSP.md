# Literature Watch — Multivariate Quantum Signal Processing

**Accessed:** 2026-10-17  
**Primary source:** Guang Hao Low, *Multivariate Quantum Signal Processing*, arXiv:2610.01125, submitted 2026-10-01, <https://arxiv.org/abs/2610.01125>  
**Evidence class:** `LITERATURE_ONLY`

## Material delta

The preprint develops a transfer-function framework for transformations of
multiple noncommuting, nonnormal block-encoded matrices and reports analytic
uniform bounds and multi-oracle application results. This is materially
different from the repository's present single-operator ER6 LCU fragment, and
it may become relevant if a future accepted workload requires multiple
interacting operator oracles rather than one MaxCut cost operator.

## Exact project decision

No result from the paper is transferred into UQPU evidence or resource counts.
`QOS-AUDIT-010B8` continues with the simpler univariate gate: explicitly verify
the multi-ancilla projector-phase convention around one ER6 block query. A
multivariate route may be compared later only after freezing the same oracle
set, normalization vector, workspace, error budget, success probability and
accepted useful output.

## Limits and falsifiable follow-up

- This preprint does not validate UQPU's ER6 circuit, phase sequence, provider
  execution, cost, energy, advantage or Data-Center-to-Phone mission.
- The claimed query improvements are not device gate counts and cannot be
  combined with unrelated provider pricing.
- Follow-up trigger: an accepted UQPU workload must demonstrably require at
  least two noncommuting block encodings. Then construct matched univariate
  decomposition and multivariate candidates, synthesize both under one error
  and workspace contract, and compare total accepted-task resources.

The equation-discovery surveillance search did not identify a newer primary
result that changes `RG-034`'s frozen held-out/identifiability experiment. This
is a dated search result, not proof that no relevant publication exists.
