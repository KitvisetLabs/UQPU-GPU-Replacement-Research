# Literature watch — 2026-10-26: formal proof search as an auditable scientific subroutine

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — strategy, research publication and future-industry context  
**Implementation owner:** Lane A — proof-aware equation-discovery/runtime tooling  
**Evaluation owner:** Lane F — reproducibility, statistical comparison and evidence policy  
**Feeds:** FND-006; EQN-001–006; INV-034/035; compiler/resource certificates across A–H  
**Evidence class:** PEER-REVIEWED FORMAL-PROOF-SEARCH RESULT + OFFICIAL PREPRINT CONTEXT; no UQPU reproduction

## Source and reported result

George Tsoukalas et al., “Advancing mathematics research with AI-driven formal proof search,” *Science* 394(6820), 234–239, published 2026-10-08, DOI [10.1126/science.aej2213](https://doi.org/10.1126/science.aej2213). Bibliographic record: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42848891/).

The article reports an AI proof-search agent resolving 9 of 353 open Erdős problems and proving 44 of 492 On-Line Encyclopedia of Integer Sequences conjectures in its evaluated setup. Its core engineering significance for UQPU is the pairing of model-generated proof candidates with a formal checker such as Lean, so each accepted proof step is checked against a declared formal statement and environment.

This is evidence that formal proof search can contribute to mathematical discovery on selected benchmarks. It is not a blanket verification of every generated claim, a demonstration that an AI-generated equation describes nature, or a measured UQPU performance/economic result.

## Genuine novelty and limitations

The relevant distinction is between **candidate generation** and **machine-checked derivation**. A formal kernel can validate a proof relative to its theorem statement, imported library, axioms and definitions. It cannot by itself establish that the formal statement captures the intended physical system, that the premises are empirically true, or that a proposed effective law applies outside its declared domain.

The reported benchmark counts are source claims; this cycle did not reproduce them. They do not imply a universal solve rate. Benchmark contamination, theorem-family overlap, compute budgets, timeout policy, library dependencies, proof-assistant versions and the definition of an “open” problem all affect interpretation. Proof success should therefore be reported alongside failures, resource usage and statement/dependency audits.

Related open preprint context: Ye et al., “ProofEvolve: Neuro-Symbolic Evolution for Formal Automated Theorem Proving,” arXiv:2608.26334 (submitted 2026-08-26), [official arXiv record](https://arxiv.org/abs/2608.26334). It describes retaining and recombining Lean-kernel-checked proof substructures; its reported benchmark results remain the authors' claims until independently reproduced. This related work is not treated as independent confirmation of the *Science* result.

## Exact UQPU relevance

- **EQN-001–006 / FND-006:** use formal proof search to generate candidate derivations, prove algebraic identities and bounds, and check compiler/workload transformations. Keep proof status, counterexample search, held-out prediction and physical validation as separate fields.
- **Lane A:** suitable initial targets include finite-state stationary-distribution identities, exact small-instance QUBO/reference certificates, and QSP/QSVT algebraic identities. Freeze statements and assumptions before search.
- **Lane F:** compare systems under a common theorem set, exact toolchain, held-out theorem families, identical wall-clock/CPU/accelerator/memory budgets and a declared cost basis. Record proof completion, kernel check, axiom/import audit, retries, failed proofs and total resource use.
- **Lanes B–E and G:** no provider, device, material, fuel or fusion conclusion follows until a proved mathematical result is connected to a validated physical model and a discriminating observation.
- **Lane H:** proof-search throughput is a possible research productivity input, not a direct valuation, funding outcome or WACC reduction.

## Falsifiable follow-up

Preregister a small theorem suite containing (i) known algebraic identities, (ii) exact reference/bound lemmas for frozen small workloads, and (iii) at least one deliberately false or over-strong statement. Pin Lean, Mathlib and all imported dependencies; hash each theorem statement; give each candidate system the same per-problem resource ceiling and seed set; and hold out theorem families from prompt tuning. A proof counts only if the exact statement compiles without placeholder proofs or unapproved axioms and passes dependency/statement-faithfulness review. Preserve all failures.

The method hypothesis is weakened or rejected if apparent gains vanish under matched resources, require stronger hidden assumptions, fail independent clean-room compilation, or merely solve training-family variants. For a physical-law proposal, even a checked theorem must still identify the changed incumbent assumption, dimensional/symmetry/conservation/causality checks, limiting cases, a held-out physical prediction, a discriminating experiment and independent replication.

## Non-claims

No UQPU proof-search benchmark was run in this cycle. No new physical law, quantum advantage, real-QPU result, Data-Center-to-Phone compression, Pangola material substitution, accepted bio-oil, commercial net fusion electricity, lower financed principal/interest or lower WACC is demonstrated.