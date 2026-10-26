# EQN-PURIFY-001 — independent purification resource-law reproduction contract

**Date:** 2026-10-26  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane dependencies:** B (target/provider evidence), C (state and output representation), F (resource/cost accounting), H (publication)  
**Status:** READY — literature-only; implementation and independent proof review not yet started  
**Source baseline:** He, Xiong & Wang, arXiv:2607.08626 (2026-07-09); related peer-reviewed two-copy no-go theorem, *Phys. Rev. Lett.* 136, 090204 (2026-03-04)  
**Evidence class:** RESEARCH_SPECIFICATION / LITERATURE_ONLY

## 1. Objective

Independently reproduce the scoped mathematical boundary and quantitative resource claims for universal quantum-state purification, then decide whether any candidate protocol can satisfy a frozen accepted-output contract at lower end-to-end cost. This task does **not** assume that the preprint is correct, that nonstabilizerness measures equal hardware cost, or that purification is representative of general UQPU workloads.

## 2. Work-item contract

- **ID / lane:** EQN-PURIFY-001 / A
- **Objective:** independently verify the two-copy no-go/resource-law boundary and separate proof-level claims from numerical SDP evidence.
- **Inputs:** exact source version and theorem statements; definitions of universal purification, fidelity, success probability, mana and robustness; source-provided maps; pinned solver/proof dependencies.
- **Outputs:** source-to-claim matrix; reproducible proof/SDP artifacts; positive and negative fixtures; held-out counterexample report; resource ledger; independent-review record.
- **Acceptance:** exact agreement with source assumptions and theorem scope; independent reproduction or documented counterexample; explicit separation of theorem, numerical result, model and physical measurement; no resource-to-cost conversion without a separately justified mapping.
- **Status:** READY.
- **Blocker / unlock:** full source details, solver/proof environment and exact theorem assumptions must be frozen before implementation.
- **Next action:** retrieve and hash the exact preprint source, transcribe definitions and assumptions, and preregister the reproduction matrix.
- **Artifact:** this contract; follow-on code/results must be separate versioned artifacts.

## 3. Mathematical contract

Let \(\rho\) denote an input noisy state, \(\mathcal{P}\) a candidate purification protocol, \(\sigma\) its conditional output state, \(F(\sigma,\rho_\star)\) the agreed fidelity measure to the target/principal-eigenstate criterion, and \(p_{\mathrm{succ}}\) the protocol's declared success probability. Let \(M(\rho)\) denote the source-defined mana measure where applicable and \(R(\rho)\) the source-defined robustness measure where applicable.

The source claim is to be transcribed exactly; this contract intentionally does not invent a formula for the reported linear law. The reproduction must identify:
- state dimension and number of input copies;
- allowed deterministic/probabilistic operations and ancillary resources;
- whether universality quantifies over all admissible input states or a restricted ensemble;
- fidelity definition, target condition and conditioning on success;
- the resource monotone and normalization convention;
- the exact theorem versus numerical-SDP status;
- proof/solver assumptions and numerical tolerance/certificate requirements.

### Null and alternative hypotheses

- **H0 (scoped no-go/resource boundary):** under the exact source assumptions, classically simulable/stabilizer-only operations do not provide universal two-to-one purification in the stated dimensions; quantitative resource claims hold only in their stated task/resource domain.
- **H1 (candidate extension):** a broader claim or constructive protocol may hold under a separately stated changed assumption or added resource. Any extension must name that changed assumption and predict a distinguishable output/fidelity/success/resource relation.
- **No implicit alternative:** a fit to selected states or numerical SDP result is not a proof of a universal theorem.

## 4. Preregistered test matrix

1. **Theorem extraction:** transcribe source definitions, assumptions and theorem statements into a machine-readable claim manifest.
2. **Two-copy cases:** independently reproduce the qubit and odd-dimensional theorem boundary using proof-level reasoning or a certified formulation; test deterministic and probabilistic cases separately.
3. **Three/four-copy cases:** reproduce the reported SDP/numerical observations, archive solver versions, primal/dual residuals and tolerances, and label the results NUMERICAL unless a certified proof is available.
4. **Known-map controls:** test source-provided constructive maps against the stated input ensembles and fidelity/success criteria.
5. **Held-out states:** reserve state families and parameter regimes not used for implementation tuning.
6. **Counterexamples:** search for counterexamples to every proposed extension beyond the source's quantifiers, dimensions, operations and resource assumptions.
7. **Independent implementation:** use a second implementation or independent proof review with no shared derived test fixtures where feasible.
8. **Cost translation:** only after mathematical reproduction, derive a separate mapping from resource monotones to an explicit circuit/resource model. Keep mana, robustness, nonstabilizer-state count, gates, shots, joules and currency as distinct typed quantities.

## 5. Accepted-output and economics gate

A candidate is not accepted merely because it increases fidelity on one example. Before any provider experiment, freeze:
- workload/state-task ID and target-state semantics;
- required fidelity metric, threshold and direction;
- success probability and minimum accepted-output rule;
- number of input copies, repetitions, failures and discarded outputs;
- output reconstruction and host preprocessing/postprocessing;
- provider, target, circuit/compilation digest, calibration snapshot and SDK versions;
- latency, memory, I/O/transfer, billable usage and energy where measurable;
- the competitive baseline and full cost per accepted useful output.

Do not combine a success probability or calibration from one provider/target with another provider's price. A zero-accepted-output run has undefined cost per accepted output, not zero cost. No paid QPU execution is authorized by this specification.

## 6. Falsifiers and stop conditions

Reject or narrow the candidate if:
- source assumptions or quantifiers cannot be reproduced exactly;
- an independent proof/implementation contradicts the stated result;
- an alleged theorem depends on an uncertified numerical SDP;
- held-out states violate a proposed generalization;
- a claimed resource improvement disappears when failures and success probability are included;
- mana/robustness is treated as hardware cost without a justified conversion;
- output reconstruction, host work, state/I/O, energy or provider charges are omitted;
- the candidate fails the same accepted-useful-output contract as the baseline.

All failed hypotheses and counterexamples remain part of the research record.

## 7. Integration map

- **A:** resource-bound preflight for algorithms that include state purification or error-reduction steps.
- **B:** provider-neutral target and calibration provenance only after a bounded simulation passes.
- **C:** state representation, copy count, intermediate materialization and reconstruction; no equivalence between Hilbert-space dimension and readable classical storage.
- **D/G:** only if a validated protocol changes measurable device, control, readout or fabrication requirements.
- **E:** no current biomass, accepted-fuel, material-substitution or fusion-electricity implication.
- **F:** uncertainty-aware cost per accepted output; distinguish principal reduction from rate/WACC claims.
- **H:** publish scoped conclusions and retain the strategic plan as context, not evidence.
- **FND/EQN:** feeds FND-006 and EQN-001/004/005/006; does not close FND-001/002/003/004 or establish new physics.

## 8. Evidence boundary

The current evidence is literature-only. No UQPU code implementation, proof assistant, numerical SDP, simulator run, real-QPU job, lab experiment, energy/cost measurement or physical-law promotion has occurred. INV-029–035 remain mission targets/principles; the present physical and mathematical limits remain binding unless a discriminating proof or experiment establishes otherwise.
