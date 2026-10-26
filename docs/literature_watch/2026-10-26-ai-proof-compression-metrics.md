# Literature watch — 2026-10-26: measuring proof structure in AI-generated mathematics

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — research publication and strategic context  
**Implementation owner:** Lane A — formal/equation-discovery tooling  
**Evaluation owner:** Lane F — reproducibility, quality and cost accounting  
**Feeds:** FND-006; EQN-001–007; INV-034/035  
**Evidence class:** OFFICIAL ARXIV PREPRINT / METHODOLOGY AND ANALYSIS OF FORMAL-PROOF CORPORA  
**UQPU reproduction:** none; no physical claim promoted

## Source and date

Safal Raman Aryal, “Studying proof data with proof theory: the case of AI-generated mathematics,” arXiv:2610.25357, submitted 2026-10-18. Official preprint: https://arxiv.org/abs/2610.25357.

The author analyzes 96 projects drawn from OpenAI's AI-written mathematics library, smaller AI-written corpora, and human research projects against the same Lean mathlib version. The paper measures checked proof terms and compares proof structure with a reference library, cut-free forms, expected theorems, and compilation controls. It reports that intermediate claims can be redundant and that the AI-generated proof terms in the selected corpus realize less of the measured available logical compression than the human mathlib reference. The paper also reports that some initial differences shrink after automated tactics are collapsed.

## Genuine methodological delta

This is a measurement framework for the **structure and reuse efficiency of formally checked proof artifacts**, not simply a count of solved problems. It suggests useful audit variables for UQPU's mathematics-first path: theorem-statement hash, import/library snapshot, axiom/admission policy, proof-checker/toolchain version, proof-term size, redundant intermediate claims, tactic/automation handling, and a declared compression baseline.

## Limitations and evidence boundary

- This is an arXiv preprint, not treated here as peer-reviewed or independently replicated.
- The sampled projects do not represent every AI-generated mathematical manuscript or every domain.
- Subject matter, automation, library dependencies and compilation choices can affect proof-structure comparisons.
- A shorter or more compressible proof is not necessarily more novel, more useful, or better connected to physical reality.
- Kernel-checked validity applies to a frozen formal statement and its declared axioms/imports; it does not establish that the statement models nature or that a proposed equation is a physical law.
- UQPU did not rerun the paper's analysis or inspect its corpus.

## Exact UQPU relevance and falsifiable follow-up

For EQN-007/FND-006, extend proof provenance records only when a proof-checker run is actually performed. Freeze the theorem statement, import hashes, Lean version, axiom/admission policy, resource budget and corpus split. Compare proof-term size and redundancy only across matched theorem families and equivalent automation policies; retain failed and rejected proofs. A mutated invalid theorem/control must be rejected by the pinned checker. If a claimed compression benefit disappears after tactic normalization or matched-library controls, record the null result. No proof-structure metric may substitute for a held-out physical prediction, discriminating experiment, independent replication, or end-to-end economic measurement.

## Mission and invariant boundary

- **INV-029:** no Data-Center-to-Phone physical-compression evidence.
- **INV-030/031:** no Pangola functional substitution or accepted liquid-fuel evidence.
- **INV-032/033:** no net delivered fusion-electricity or measured financing-rate result.
- **INV-034:** formal mathematics and proof provenance can strengthen the search process.
- **INV-035:** AI-generated equations remain hypotheses until their distinct predictions survive independent tests.
