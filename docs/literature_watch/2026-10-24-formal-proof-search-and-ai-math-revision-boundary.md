# Literature watch — 2026-10-24: formal proof search, equation discovery, and revision-aware evidence

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, foundational research and publication  
**Cross-lane consumers:** Lane A; FND-006; EQN-001–006; Lane F; INV-034/035  
**Evidence class:** PEER-REVIEWED MATHEMATICAL-METHOD RESULT + OFFICIAL AI-MATHEMATICS RELEASE HISTORY  
**UQPU project evidence promotion:** none  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Primary sources and dated observations

1. George Tsoukalas et al., **“Advancing mathematics research with AI-driven formal proof search,”** *Science* 394(6820), 234–239, published 8 October 2026. DOI: [10.1126/science.aej2213](https://doi.org/10.1126/science.aej2213); bibliographic record: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42848891/).
2. OpenAI, **“Sharing AI progress in mathematics,”** released 6 October 2026 and updated 15 October 2026: [official announcement](https://openai.com/index/sharing-ai-progress-in-mathematics/); [official manuscript and Lean-artifact repository](https://github.com/openai/math).
3. The official repository's [revision history](https://github.com/openai/math/blob/main/history.md) records 7 October corrections and withdrawals. The current repository README reports 719 manuscripts in 372 families and approximately 42% of top-line results formalized; the initial announcement described 722 manuscripts.

## Material delta

The *Science* paper reports a formal-proof-search agent that resolved 9 of 353 open Erdős problems and proved 44 of 492 OEIS conjectures in the evaluated collections. Its central methodological contribution is the alternating loop of language-model candidate generation and Lean proof checking; the paper also reports that a basic alternating generator/checker reproduced the Erdős successes. These are reported mathematical-method results, not a claim that unconstrained model text is reliable.

The official OpenAI collection supplies an unusually concrete negative-evidence lesson. On 7 October, its public history records three manuscript withdrawals after a sign error invalidated an argument and affected dependent papers, plus revisions to 14 other manuscripts and additional formalizations. This is not a reason to dismiss the entire collection; it is evidence that versioned artifacts, explicit dependencies, corrections and withdrawn hypotheses must remain visible rather than being erased from the research record.

The new UQPU-relevant distinction is therefore **two different validity questions**:

1. **Formal/mathematical validity:** does a proof checker verify the stated theorem from its formal definitions and assumptions?
2. **Empirical/model validity:** do the definitions, variables, boundary conditions and observables faithfully represent the physical system, and does the candidate predict held-out measurements better than the incumbent model?

Passing the first question does not imply passing the second. A theorem about an encoded model cannot by itself establish a new physical law, a new device primitive, a QPU advantage or a cost reduction.

## Exact project relevance

- **Lane A / EQN-003 and EQN-004:** put formal checks and adversarial counterexamples into the candidate-evaluation pipeline where the claim is mathematical; require the record to include both provenance and an independent-validation plan. A missing field must fail closed.
- **FND-006 / EQN-006:** use mathematics-first invention to generate lemmas, encodings, bounds and candidate equations, but retain the incumbent assumptions, dimensions, symmetries, conservation/causality checks, limiting cases, held-out tests and falsifier.
- **Lane F / FIN-001:** track proof-search compute, expert review, failed attempts and elapsed time to a validated milestone if a later benchmark can measure them. Faster candidate generation alone is not a lower cost per accepted result, lower financed principal, lower interest expense or lower WACC.
- **INV-029:** mathematical progress can only be an upstream enabler; it provides no evidence of phone-class physical compression, service equivalence or full-system lifecycle cost.
- **INV-030 / INV-031:** no evidence here for Pangola-carbon material substitution or accepted bio-oil/fuel yield, quality or cost.
- **INV-032 / INV-033:** no evidence here for net delivered fusion electricity, plant economics, financing terms or interest-rate reduction.
- **INV-034 / INV-035:** supports formal proof and revision tracking as parts of the research method; it does not change established physical limits or promote an AI-generated equation to a physical law.

## Limitations and evidence boundary

The *Science* results concern mathematical problem sets, not UQPU workloads or experimental physics. The OpenAI release is a changing collection with different per-paper verification states; aggregate manuscript and formalization counts do not certify every claim. Lean checks a formal proposition relative to its formalization and axioms; it does not automatically certify that the formal model matches nature. No independent UQPU reproduction of the cited results was performed in this cycle.

Classification: `LITERATURE_ONLY / THIRD_PARTY MATHEMATICAL-METHOD EVIDENCE`. No QPU job, material test, fuel experiment, fusion-plant measurement, new physical law or economic advantage is claimed.

## Falsifiable follow-up

1. Harden `uqpu/equation_discovery.py` so a candidate cannot be considered testable without nonempty data/proof provenance **and** an independent-validation plan; reject blank tuple entries and non-finite/nonnumeric held-out errors. Add adversarial unit tests for absent provenance, absent validation plan, NaN, infinities, negative values and invalid validation counts.
2. In a later isolated benchmark, preregister a small fixed set of symbolic/math tasks and split manifests; compare an ordinary symbolic-regression baseline with an AI-assisted generator under the same search budget. Keep held-out examples sealed, run counterexample search, and formalize only claims whose definitions and assumptions are explicit.
3. Score formal proof success, held-out generalization, counterexamples, false discoveries, human review, compute cost and elapsed time separately. Any physical candidate must additionally name a discriminating observable, experiment, independent replication and system/economic consequence.
4. If a formalized candidate fails held-out or experimental validation, retain it as a false discovery; do not reinterpret proof-checker success as physical confirmation.

## A–H integration status for this delta

| Lane | Result / boundary |
|---|---|
| A — programming, workloads, compiler/runtime | Validator hardening and adversarial tests proposed in the same reviewable source branch; hosted CI is the acceptance gate. |
| B — cloud/QPU/provider integration | No provider calls, credentials, target queries or QPU jobs. |
| C — memory/state/data movement | Proof artifacts and classical records remain ordinary classical data; no Hilbert-space-to-readable-storage equivalence claim. |
| D — device/chip/fabrication | No device, process-window, packaging or fabrication evidence. |
| E — materials/energy/infrastructure | No Pangola, bio-oil, fusion, cooling or infrastructure measurement. |
| F — economics/evidence/integration | Separate proof success from accepted-task quality and total cost; FIN-001 remains measurement-gated. |
| G — manufacturing equipment/factory systems | No tooling, yield, inspection or factory-cost evidence; continuous D/G co-design unchanged. |
| H — strategy/publication/finance | Records the primary-source result, revision history, limitations and cross-lane falsifiable follow-up. |

## Next highest-value gate

Run the new equation-discovery tests on the exact PR commit, then use hosted CI and the cold-start audit to validate provenance. This is software/protocol evidence only. A later EQN-002 benchmark must separately establish held-out performance and false-discovery rates before any physics or economics claim can be considered.
