# FND-001 finite-state memory-policy preregistration

**Preregistered:** 2026-10-26  
**Owner:** Lane F — economics, benchmarks, evidence and integration; shared interface FND-001  
**Evidence class:** MODEL_ONLY protocol; no device, energy, or task-quality claim  
**Status:** Frozen before generating held-out result files

## Question

Can the existing FND-001 information-thermodynamic objective be evaluated reproducibly for a finite-state agent/environment loop, and do the selected toy policy rankings remain stable when held-out transition parameters change?

The primary metric is the model objective from Fiderer et al., *Information Thermodynamics of Agents: The Work Capacity of Channels with Memory*, Phys. Rev. X 16, 041004 (published 2026-10-05), DOI: https://doi.org/10.1103/7nds-tjr8:

`W/(k_B T \ln 2) = H(A_t\mid M_t)-H(S_t\mid M_t)`

with entropy measured in bits. This is a dimensionless idealized bound/objective per round, not measured joules or real hardware efficiency.

## Frozen environment family

There are two percept states, two actions, and finite agent memory. The current percept is the complete environment state in this toy model; any hidden environment state would need to be represented explicitly before use.

Let `p` vary for state-0 persistence and hold `q=0.70` fixed for state-1 persistence. For current percept `s=0`:
- action 0: `P(S'=0)=p`
- action 1: `P(S'=0)=1-p`

For current percept `s=1`:
- action 0: `P(S'=1)=q`
- action 1: `P(S'=1)=1-q`

Training/design point: `p=0.80`. Held-out points: `p ∈ {0.65, 0.75, 0.85, 0.95}`. No held-out value may be tuned after inspecting its result.

## Frozen policies

1. **MEMORYLESS:** one memory state; choose action 0 with probability `1/√2` independently of current percept; memory update is trivial.
2. **PREDICTIVE:** two memory states; memory records the current percept for the next round. Choose action 0 with probability 0.9 when current percept equals stored memory, and 0.1 otherwise.
3. **BOUNDED_MEMORY:** two memory states; memory records the previous action. Choose action 0 with probability 0.9 when stored memory is action 0, and 0.1 when stored memory is action 1, independently of current percept.

These are fixed illustrative policies, not optimized agents and not claims of matched useful-task performance.

## Evaluation and falsification gates

- Construct the joint transition matrix over `(M,S)` exactly from the frozen policy, memory-update, and environment kernels.
- Solve `πP=π` with normalization; fail closed if a unique stationary law cannot be established.
- Require all transition rows to sum to one and stationary residual ≤ `1e-9`.
- Compute `H(A|M)`, `H(S|M)`, and their difference directly from the stationary joint law.
- Independently check the solver against a closed-form two-state chain and a memoryless invariant-channel limit where the published optimum is approximately 0.272 bits per round.
- Held-out results are diagnostic only. If rankings disappear or reverse, report that as a result rather than tuning the policies.
- No end-to-end task semantics, quality threshold, physical memory cost, device/software energy, accepted-task rate, provider bill, or lifecycle cost is specified here. Therefore **no policy can pass a useful-task or energy-efficiency gate** from this experiment.

## Explicit non-claims

This protocol does not establish a new physical law, work extraction in a device, a real thermodynamic cycle, quantum advantage, reduced GPU/CPU/NPU/RAM/VRAM/storage demand, lower project WACC, or commercial economics. Any follow-up must add a matched useful-output contract and separately measured implementation costs.
