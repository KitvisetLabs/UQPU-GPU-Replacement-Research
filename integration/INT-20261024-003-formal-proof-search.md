# INT-20261024-003 — formal proof search with model-to-physics boundary

**Date:** 2026-10-24  
**Primary owner:** Lane H — literature and strategic research integration  
**Cross-lane owners:** Lane A (formalizable contracts), Lane F (evidence and full-cost accounting)  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch before follow-up:** `research/2026-10-24-equation-discovery-audit-v2`  
**Work ID:** `FORMAL-PROOF-001`  
**Status:** PROPOSED  
**Evidence class:** `LITERATURE_ONLY` + `PROTOCOL_PROPOSAL`; no project evidence promotion

## Hypothesis

Formal proof search can strengthen selected mathematical subclaims when the exact proposition is checked by a declared proof assistant, dependencies and axioms are audited, and an independent reviewer maps premises to the repository's model. It cannot establish that the model describes nature merely because the theorem checks.

## Inputs and provenance

- Lane-H literature article: `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_FORMAL_PROOF_SEARCH.md`
- Peer-reviewed source: Tsoukalas et al., *Science* 394(6820), 234–239 (2026-10-08), DOI 10.1126/science.aej2213.
- Public preprint: arXiv:2605.22763, submitted 2026-05-21.
- Existing project contracts: `software/uqpu-prototype/uqpu/equation_discovery.py`, FND-006 and EQN-004/005.

## Interface and acceptance contract

A candidate theorem record must pin:
1. exact formal proposition and source commit;
2. Lean/proof-assistant version and reproducible environment;
3. imported libraries, axioms, definitions and dependency lock;
4. checker result and proof artifact digest;
5. mapping from every premise to the relevant model assumption;
6. independent review/replay result;
7. a mutated-premise negative control;
8. generation, checking, host and review costs.

Acceptance requires a clean proof check, explicit axiom/dependency audit, independent replay, and agreement that the formal proposition matches the intended model claim. A checked proof alone is not accepted as physical evidence.

## Falsifier and rollback

Reject the candidate if proof checking fails, a hidden/undeclared axiom is required, premise mapping is incomplete, the proposition differs from the intended statement, a mutated premise still passes unexpectedly, or independent replay fails. Preserve the failure and revert only the candidate proof artifact if the contract is defective.

## Cross-lane integration

- **A ↔ H:** AI may generate candidate lemmas; the checker and reviewer, not the generator, adjudicate formal validity.
- **A ↔ F:** include generation, checking, dependencies, failed attempts and independent review in total cost per accepted verified result.
- **FND-006 / EQN-004 / EQN-005:** separate candidate instrument, checked theorem, model-valid statement and empirically supported physical relation.
- **B/C/D/G:** no provider authorization, readable-memory inference, device feasibility or fabrication claim follows from a proof.
- **E/F/H:** no Pangola material, saleable fuel, net fusion-electricity, interest or WACC result follows from a proof.

## Current result and next gate

The literature watch is published on the research branch; no UQPU proof has been formalized in this cycle. Next, select one bounded lemma already used by a repository contract, pin its exact assumptions and dependencies, run a clean formal check, add a premise-mutation negative control, and require independent replay before connecting it to simulation or experiment.

**Evidence boundary:** literature/method evidence only. INV-029 through INV-035 remain unpromoted; no AI-generated equation is declared a physical law.
