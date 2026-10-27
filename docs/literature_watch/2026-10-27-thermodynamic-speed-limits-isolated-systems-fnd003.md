# Literature watch — 2026-10-27: thermodynamic speed limits for isolated quantum systems

**Accessed:** 2026-10-27  
**Primary source:** Rikuya Kobashi, “Thermodynamic speed limits in isolated quantum systems,” *Physical Review Research*, accepted 2026-10-06, DOI 10.1103/k16k-nx74; arXiv:2609.12520, submitted 2026-09-11.  
**Official sources:** https://journals.aps.org/prresearch/accepted/10.1103/k16k-nx74 and https://arxiv.org/abs/2609.12520  
**Evidence class:** PEER-REVIEWED THEORETICAL RESULT WITH NUMERICAL/ANALYTICALLY SOLVABLE EXAMPLES  
**Publication owner:** Lane H  
**Implementation owner:** Lane A — quantum workload/runtime and bound-comparison tooling  
**Evaluation owner:** Lane F — matched baselines, thermodynamic accounting and evidence integration  
**Feeds:** FND-001, FND-003, FND-006, EQN-003, INV-034/035  
**UQPU evidence promoted:** none

## Result and genuine novelty

The paper derives operation-time lower bounds for isolated quantum systems undergoing finite-time unitary driving. It uses generalized second-law inequalities for Gibbs entropy and several observational/coarse-grained entropies, with entropy production bounded using a function of the Vu–Saito quantum Wasserstein distance between initial and final coarse-grained states. The author discusses system-bath coarse-graining, local-energy coarse-graining and diagonal entropy, with numerical and analytically solvable examples.

The useful project delta is a candidate theoretical comparator for FND-003: it makes the chosen coarse-graining and entropy-production definition part of the speed-limit contract instead of treating “quantum speed limit” as a single universal scalar. It can also sharpen FND-001 bookkeeping by forcing the model to state which entropy production is being bounded and over what state transformation.

## Limitations and evidence boundary

- This is a theoretical result, not a measurement of UQPU runtime, energy, heat, irreversible reset cost, or accepted useful-task quality.
- The bounds depend on the stated dynamics and coarse-graining/entropy definitions. They must not be applied to a different workload or physical protocol without checking the assumptions.
- Entropy production is not automatically equal to useful work, wall-plug energy, heat dumped to a cooling system, or total lifecycle cost.
- A time lower bound is not a prediction that a quantum implementation achieves the bound, nor proof of speedup over a classical baseline.
- The paper does not establish a new physical law, a lower cost per accepted task, or a change to the project's present engineering constraints.

## Exact UQPU relevance

- **FND-003 / Lane A:** add the theorem as one candidate bound family in a matched control-versus-quantum-speed-limit measurement protocol. The same input/output task, initial/final coarse-grained states, accuracy threshold, and elapsed-time boundary must be declared for both paths.
- **FND-001 / Lane C:** keep entropy-production accounting separate from measured work, heat, reset, memory/state I/O and accepted-task quality. No joules may be inferred from the entropy inequality without a separately justified thermodynamic model and measurements.
- **FND-006 / INV-034/035:** represent the assumptions and domain explicitly, derive units and limiting cases, and preserve the result as an incumbent-theory reference rather than an AI-generated or newly promoted physical law.
- **Lane F / INV-033:** a tighter mathematical lower bound may inform experiment selection and time-to-evidence planning, but it does not demonstrate lower financed principal, absolute interest, project WACC or economy-wide rates.
- **INV-029:** this source supplies no phone-class physical-compression, service-capability, power or lifecycle-cost result.

## Falsifiable follow-up

1. Pin the paper version and transcribe the exact theorem statement, distance definition, entropy definition, dynamics assumptions and allowed coarse-graining.
2. Select a small finite-dimensional unitary-driving fixture with independently computed initial/final states. Calculate the stated distance and entropy-production terms from a separate reference implementation.
3. Before evaluating the candidate bound, preregister the task, state preparation/readout costs, quality threshold, elapsed-time boundary, classical control algorithm and held-out parameter points.
4. Check dimensions, limiting cases, and whether the bound is nontrivial relative to simpler known bounds on the same fixture. Search for counterexamples to any implementation-derived corollary.
5. Compare the same bound against matched classical and quantum control measurements only when the same task and time boundary are used. Record failed and inconclusive cases.
6. Require independent implementation/reproduction before integrating the bound into a system-level claim.

**Falsifier / rejection rule:** reject the implementation if it violates the source theorem's assumptions, fails exact small-instance checks, or reports a bound outside its declared coarse-graining/domain. If the bound is valid but no tighter or discriminating prediction is obtained, retain it as a reference result without claiming a useful UQPU advantage.

## Status

**LITERATURE_ONLY / FND-003 REFERENCE CANDIDATE.** No matched control-versus-bound experiment was added in this cycle. No physical, device, QPU, energy, material, fuel, fusion, financing or economic claim is promoted.
