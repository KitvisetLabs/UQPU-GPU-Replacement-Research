# INT-20261024-001 — Fail-closed equation-discovery metric guard

**Date:** 2026-10-24  
**Status:** TESTING — hosted CI pending  
**Primary implementation owner:** Lane F — economics / evidence / integration  
**Contributing lanes:** A, F, H; cross-cutting FND-006 and EQN-001–006  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Inputs and provenance

- `software/uqpu-prototype/uqpu/equation_discovery.py` — source commit `aba0b3c16fd666d52cf83895b0c1024ccc36babd`
- `software/uqpu-prototype/tests/test_equation_discovery.py` — source commit `48cbfec10b5d5c97e7ee9de8ad5738b6190db349`
- `docs/literature_watch/2026-10-24-ai-math-verification-pipeline.md` — source commit `91ff69db0fce29b2b68897891c6f950989ebf465`
- Lane A target-gate checkpoint: `research_lanes/A_quantum_programming_runtime/DAILY_GATE_2026-10-24.md`, source commit `26f64608835f8fc41e19e8bac0aba3702bd753d7`

These are branch/source SHAs. They are **not yet main-synchronized** at the time of this record.

## Hypothesis and causal mechanism

**Hypothesis:** preventing non-finite held-out errors and invalid replication counts from entering the equation-candidate contract will close a concrete false-promotion path before model selection or physical-candidate discussion.

Previously, `heldout_baseline_error=float("inf")` and a finite candidate error passed the non-negative check, making `has_heldout_improvement` true. A fractional value such as `independent_validation_count=1.5` also passed the old non-negative check and could satisfy the `>= 1` replication condition. These are metadata/validation defects, not evidence of a false physical law.

## Interface and checks

The `EquationHypothesis` public interface is unchanged. Validation now requires:
- each supplied held-out error to be numeric, finite and non-negative; `None` remains the explicit “not measured” state;
- `independent_validation_count` to be a non-negative integer, rejecting booleans and fractional counts.

New adversarial tests cover positive infinity, NaN, fractional/boolean counts and the physical-candidate gate. Existing tests still cover missing falsifiers, unknown evidence labels, and the requirement for held-out improvement plus independent validation.

## Baseline and expected/observed effect

- **Baseline:** non-finite held-out metrics and non-integer validation counts were not rejected at validation time.
- **Expected:** these malformed records fail closed; no scientific or performance gain is presumed.
- **Observed:** code and regression tests are committed on the source branch. Hosted test outcome is pending and must be reported after PR CI.
- **Physical units:** held-out error uses the existing caller-defined metric and units; this change does not normalize or compare unlike error metrics.
- **Economics/energy/materials:** no energy, material, fuel, fusion, finance, or useful-task cost measurement is produced by this metadata guard.

## Cross-lane edges

- **A↔F:** compiler/runtime candidate acceptance can consume only well-formed held-out evidence; no target route or useful-output contract is changed.
- **F↔H:** discovery cost and evidence quality should inform experiment selection, while strategic ambition or novelty scores cannot promote claims.
- **FND/EQN↔A–I:** finite metric validity is a prerequisite only; dimension, symmetry, conservation, causality, limiting cases, counterexamples, proof/simulation, discriminating experiment, and independent replication remain separate gates.
- **E↔F↔H:** BIO-001, FUS-001 and FIN-001 may use candidate models for prioritization, but MODEL_ONLY remains non-commercial evidence.
- **D↔G:** no device/process integration claim is affected; any future model transfer must carry measured process-window and manufacturing uncertainty.

## Falsifier, rollback and safety

**Falsifier:** a test demonstrates that a NaN/Infinity or non-integer/boolean validation count still passes `validate()`, or that the physical-candidate gate returns true for such a record.

**Rollback:** revert only the validation guard and its tests if the repository's declared contract proves incompatible; do not weaken the frozen model or silently alter evidence labels.

No QPU submission, provider session, purchase, material experiment, fusion experiment, or hazardous testing is authorized by this change.

## Next gate

Run the repository's full test suite and cold-start handoff audit on the exact PR head. If both pass, merge with a `Research-Sync: main` trailer, then record source-to-main SHA mapping and update the canonical handoff manifest. Separately pursue `QOS-AUDIT-010B25` only in an authorized read-only environment.
