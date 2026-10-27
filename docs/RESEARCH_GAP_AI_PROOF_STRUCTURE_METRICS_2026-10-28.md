# Research gap RG-048 — proof-structure metrics for AI-assisted equation discovery

**Opened:** 2026-10-28  
**Primary owner:** Lane A — quantum programming/runtime and formal/equation evidence tooling  
**Cross-lane owners:** Lane F — benchmark/evidence/resource accounting; Lane H — literature publication  
**Status:** OPEN — literature-derived specification; no metric implementation or corpus reproduction claimed  
**Related:** INV-034/035; FND-006; EQN-001–006; existing formal-proof evidence contract  
**Source watch:** `docs/literature_watch/2026-10-28-ai-proof-structure-compression-audit.md`

## Objective

Determine whether reproducible proof-structure diagnostics can help evaluate AI-assisted mathematical/equation-discovery workflows without conflating proof efficiency with correctness, novelty or physical truth.

## Current evidence

Aryal (arXiv:2610.25357, 2026-10-18) proposes corpus-level analysis of proof terms, redundancy and logical compression, reporting differences between selected AI-generated and Mathlib proof corpora. These are external preprint results. UQPU has not independently reconstructed the metrics or reproduced the corpus-level values. The current UQPU formal-proof contract binds exact artifacts and checker metadata but does not itself measure proof quality or prove source/model adequacy.

## Proposed diagnostic record

Before implementation, freeze a versioned schema containing:

- claim ID, exact statement hash, proof-artifact hash and immutable source revision;
- proof assistant/version, Mathlib or library revision, compiler/options, environment hash and extraction-tool revision;
- raw proof-term/AST size and the unit used to count it;
- each transformed-size measure with the exact transformation named (for example, automation-expanded versus automation-collapsed, or a declared sharing/cut-free transform);
- intermediate-claim count, dependency/use counts and a reproducible rule for classifying a claim as unused;
- parser status, exclusions, failed transformations and counterexamples to expected metric behavior;
- checker correctness status, independent reproduction count and empirical-adequacy status as separate fields;
- wall time, CPU/GPU time, inference/token use, peak memory, retries and energy only when actually measured.

Any normalized compression ratio must identify numerator, denominator and transformation version. A project-defined metric is not to be described as a reproduction of the source paper until the source definition and implementation have been reconstructed.

## Unlock criteria

1. Pin the source/corpus, license, toolchain, reference library and extraction code.
2. Reproduce metric values on a small held-out sample before a broad comparison.
3. Pass positive controls (shared lemmas should expose reuse) and negative/adversarial controls (redundant claims, changed compiler/tactic settings, malformed terms and subject-matter imbalance).
4. Report uncertainty, excluded examples and failed parses; do not report only aggregate averages.
5. Keep kernel correctness, independent mathematical reproduction, theorem novelty, held-out generalization, physical-model validity and economic benefit as distinct gates.
6. Integrate optional diagnostics without changing the allowed proof statuses in `formal_proof_evidence.py` or weakening EQN-001–006 / INV-035.

## Falsifiers and stop rules

Reject a metric as a decision signal if it changes materially under benign compilation/tactic transformations without a defensible normalization, cannot distinguish known redundant controls, is confounded by theorem mix, or fails independent reconstruction. Do not rank candidate equations as physically better merely because their proofs are shorter.

## Cross-lane implications

- **A:** candidate optional proof-structure audit, downstream of exact-byte proof binding.
- **B:** no provider or real-QPU execution is implied.
- **C:** proof-term bytes/counts are not a readable-memory or storage-replacement claim.
- **D/G:** no device, fabrication, process-window or manufacturing result.
- **E:** no Pangola substitution, accepted bio-oil or net fusion-electricity result.
- **F:** only measured proof-generation/checking resources may enter cost-per-accepted-task accounting.
- **H:** publish methods and negative results while preserving the six-language master-plan and strategic AI-agent/funding references.

**Evidence class:** `LITERATURE_ONLY` until pinned data and reproducible local results exist. Any future synthetic metric test is a software contract, not evidence of a new physical law.
