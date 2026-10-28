# Literature watch — AI-assisted derivation of a cosmic-string radiation integral

**Date recorded:** 2026-10-28  
**Primary owner:** Lane H — research publication and strategic-plan integration  
**Cross-cutting:** Lane A (deterministic evaluator and failure handling), Lane F (evidence/benchmarking), FND-005/006, EQN-001–006, INV-034/035  
**Evidence class:** OFFICIAL_PREPRINT / EXTERNAL_METHOD_REPORT; not independently reproduced by UQPU  
**Source:** Michael P. Brenner, Vincent Cohen-Addad, and David Woodruff, *Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery*, arXiv:2603.04735, submitted 2026-03-05. [Official arXiv record](https://arxiv.org/abs/2603.04735)

## What is materially useful

The authors report a neuro-symbolic workflow combining an LLM reasoning engine, tree search with a PUCT-style selection policy, and executable Python checks against high-precision numerical evaluations. They report exploring about 600 candidate nodes, pruning more than 80% after algebraic or numerical failures, and finding six derivation routes for an integral used in a cosmic-string gravitational-radiation power-spectrum calculation. A Gegenbauer/spectral route yields the paper's preferred closed form; the paper also compares methods with numerical calculations and discusses cancellation/conditioning problems in less stable expansions.

The useful UQPU lesson is not that AI has discovered a new law of nature. It is a concrete example of **search control plus deterministic verification**: candidate generation is broad, while acceptance is constrained by executable checks and explicit failure feedback. This aligns with INV-035's separation of imaginative hypothesis generation from evidence-governed promotion and with the fail-closed numeric-range work in Batch 090.

## Evidence boundary and limitations

- This is an external preprint report. UQPU has not independently reproduced the derivation, code, parameter sweep, complexity claims, or runtime measurements.
- Agreement with numerical quadrature at selected points is valuable falsification evidence but is not by itself a symbolic proof over the full parameter domain. Singular limits, conditioning, parity, and large-harmonic asymptotics need separate tests.
- The preprint itself says it is not claiming that the integral's resolution has deep physical significance. The work is a methodological case study, not a new particle, interaction, constitutive law, or experimental anomaly.
- Candidate code that errors, diverges, returns NaN/Inf, or exceeds a resource budget must be recorded as FAILED or UNDECIDED, never silently converted into a favorable score. A fallback numerical precision path must not hide failure.
- No UQPU physical, QPU, materials, fuel, fusion, energy, or economic advantage follows from this publication.

## Exact project relevance

- **INV-035 / EQN-006:** supports testing a generator → constrained search → evaluator → counterexample → held-out test → proof/experiment pipeline. It does not establish a new physical equation.
- **INV-034 / FND-005:** offers a reproducible mathematics-first example in a cosmological calculation. It does not validate a new QFT/particle mechanism.
- **FND-006:** the most direct contribution is a workflow hypothesis: search diversity plus explicit numerical failure feedback may reduce wasted derivation paths. That hypothesis still needs a controlled benchmark.
- **Lane A / Batch 090:** candidate evaluators should use finite-value checks, explicit error classes, and deterministic acceptance rules. The signed-Max-Cut overflow counterexample shows why apparently finite inputs can still produce invalid downstream values.
- **Lanes B–D/G:** no provider, SDK, device, fabrication, or packaging result. If the workflow is later used to generate Hamiltonian mappings, independent SDK reconstruction and exact tiny-instance energy/argmax checks remain mandatory.
- **Lane E / BIO-001 / FUS-001:** only a possible future method transfer to reaction-yield, upgrading, thermal, or net-electricity models; no fuel, material, fusion, or cost claim is supported.
- **Lane F / FIN-001:** search cost and time-to-evidence could be benchmarked, but no project R&D-cost or financing reduction has been measured.
- **INV-029:** no contribution to phone-class physical compression has been demonstrated. Remote infrastructure and all input/output, memory, energy, cooling, and lifecycle burdens remain in scope.

## Proposed falsifiable reproduction

1. Pin the exact arXiv version and transcribe the target integral and the claimed closed-form identity into a version-controlled reference.
2. Build an independent high-precision evaluator, with a second numerical route that does not reuse the candidate's derivation or implementation. Declare tolerances before running.
3. Use a frozen discovery set and held-out combinations of integer harmonic (N) and opening angle α. Include even/odd (N), moderate and large (N), and stress points approaching α = 0 and π where conditioning may change.
4. Compare the preferred Gegenbauer route with at least one independent spectral/recurrence route and direct high-precision quadrature. Track convergence, precision, runtime, memory, exceptions, NaN/Inf, and all rejected candidates.
5. Search counterexamples at boundary points and larger (N); verify limiting behavior and dimensional/analytic assumptions. Independently check the key identities symbolically or by a separate derivation.
6. Have an independent reviewer reproduce a subset from the source equations. Only then classify the *mathematical derivation* as independently reproduced; do not promote it to a new physical law or UQPU technology advantage.

**Pass criterion:** all predeclared held-out residuals meet tolerance, the independent route agrees, limiting cases are handled, failures remain visible, and the derivation has an independent symbolic/proof review. A numerical fit alone fails the gate.

## Decision

Add this source to the candidate-method ledger for EQN-006/FND-006 and to the fail-closed evaluator design discussion. Do not duplicate it as evidence of a new law. The next project gate is a controlled reproduction protocol, followed by an independent Lane A pinned-SDK Hamiltonian check for the signed-Max-Cut workload; no paid QPU execution is authorized.
