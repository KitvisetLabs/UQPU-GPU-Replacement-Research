# Literature Watch — AI-Generated Mathematical Instruments

**Access date:** 2026-10-17  
**Source:** [Ying Xie, *What the Machine Invented: Mining New Mathematical
Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*,
arXiv:2610.17090](https://arxiv.org/abs/2610.17090), submitted 2026-10-12.  
**Evidence class:** `LITERATURE_ONLY`

## Material delta

The preprint studies 38 families selected from a larger public collection of
AI-written mathematics and proposes extracting reusable lemmas, constructions,
inequalities and proof mechanisms before separately judging validity, novelty
and reuse. That separation is directly relevant to INV-035: an AI-generated
mathematical object can be a candidate instrument without being a theorem,
physical law or engineering result.

## Limits

The paper states that novelty assessments are provisional and that no Lean
development was compiled or kernel-checked for the survey. It is not an
independent certification of the underlying manuscripts, does not validate a
UQPU equation, and provides no QPU, materials, energy, vehicle or economic
measurement. Counts or claimed solutions from the collection are not imported
as project evidence.

## Project decision and falsifiable follow-up

Add a `MATHEMATICAL_INSTRUMENT_CANDIDATE` stage beneath `THEORY`. A candidate
may advance only after its assumptions are frozen, counterexamples are searched,
the exact claim is independently proved or proof-assistant checked where
practical, and a held-out consequence is verified. For UQPU, the first bounded
follow-up is to select at most one instrument relevant to polynomial
approximation or circuit lower bounds, reproduce its antecedents, formalize the
claim, and test it on a repository-owned finite case before connecting it to a
resource or economics statement.

This surveillance result changes governance for EQN/FND hypothesis intake; it
does not change the current QSVT acceptance threshold or establish new physics.
