# Literature watch — EvolProver and robustness of formal theorem search

**Date checked:** 2026-10-29  
**Primary owner:** Lane H / FND-006, with Lane A formal-validation interface  
**Stable ID:** LIT-2026-ICLR-EVOLPROVER-ROBUSTNESS  
**Evidence class:** ICLR 2026 conference paper; third-party benchmark claims; not reproduced by UQPU

## Source and date

Yuchen Tian, Ruiyuan Huang, Xuanwu Wang, Jing Ma, Zengfeng Huang, Ziyang Luo, Hongzhan Lin, Da Zheng and Lun Du, “EvolProver: Advancing Automated theorem proving by Evolving Formalized Problems via Symmetry and Difficulty,” official ICLR 2026 proceedings page:

https://proceedings.iclr.cc/paper_files/paper/2026/hash/5dd362ce4612db239b1b755d86819ef6-Abstract-Conference.html

## Genuine novelty

The authors describe a training-data evolution pipeline that broadens formal theorem-proving tasks along two axes: syntactic symmetry via abstract-syntax-tree transformations, semantic symmetry via translations across mathematical domains, and a controlled range of theorem difficulty. The official proceedings page reports a 7B non-reasoning prover with pass@32 of 53.8% on FormalMATH-Lite, 69.8% on MiniF2F-Test and 34.0% on Ineq-Comp-Transformed, among its reported results.

The useful UQPU delta is a concrete robustness test design for formalized equation-discovery work: a candidate theorem or proof should survive semantics-preserving statement transformations, not only one canonical prompt or expression form. This is a method lead, not evidence that a physical equation is true.

## Limitations and evidence boundary

- The published benchmark claims are third-party results; UQPU has not independently reproduced the data, training recipe, model, proof search or reported pass rates.
- Pass@32 is a benchmark metric, not a guarantee of correctness for every generated proof or a measure of physical-model validity.
- Syntactic equivalence is not automatically semantic equivalence; domain translation requires an independently checked mapping and preservation of assumptions.
- A proof assistant can certify a theorem relative to its formal statement and axioms. It cannot by itself establish that those definitions faithfully encode a physical experiment or that the physical premises are true.
- The result does not demonstrate quantum advantage, a new physical law, a device/material/fuel/electricity improvement, or project economics.

## Exact relevance to UQPU

- **FND-006 / EQN-006:** motivates testing formal proof workflows against equivalent reformulations, held-out theorem families and difficulty shifts.
- **INV-035:** reinforces the generator-versus-verifier boundary. AI may propose variants and candidate lemmas; deterministic equivalence checks and kernel-checked proofs govern formal acceptance.
- **INV-034:** supports mathematics-first search infrastructure while keeping formal truth conditional on explicit axioms and semantics.
- **Lane A:** equation-hypothesis records already require incumbent assumptions, physical constraints, limiting cases, falsifiers, held-out predictions and counterexample searches. A proof-robustness test can complement, but not replace, those gates.
- **Lanes D/E/F and INV-030–033:** no direct material, bio-oil, fusion-electricity or financing evidence follows. Any later constitutive/material-model use needs measured data, material-family holdouts, prospective tests and full cost boundaries.
- **INV-029:** no Data-Center-to-One-Phone milestone follows from a theorem-proving benchmark.

## Proposed falsifiable follow-up

1. Pin a public formal theorem corpus, proof-assistant version, dependency lock and source/data/license hashes.
2. Generate syntactic AST variants known to preserve the statement; separately generate domain-translated variants only where a checked mapping exists.
3. Freeze train/validation/test theorem families before tuning. Include transformed and difficulty-shifted held-out subsets.
4. Score kernel-checked proof rate, semantic-equivalence verification, invalid-statement rate, counterexample/failure classification, proof-search compute/time and reproducibility under equal resource budgets.
5. Retain every failed or undecided proof. A timeout or unverified proof is not success.
6. For physics-facing equation hypotheses, keep formal proof, physical validity, independent experiment and engineering/economic consequence as separate gates.

**Decision:** add a formal-robustness benchmark lead to FND-006. No UQPU reproduction, physical-law promotion or mission-level advantage is claimed.
