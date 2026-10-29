# Batch 125 — time-dependent PDE generalization and total-resource gate

**Date:** 2026-10-29  
**Starting main SHA:** ee547aecfa1454f1f07adf16e13d150634a557c2  
**Primary owner:** Lane A — model/workload acceptance contract  
**Literature/publication owner:** Lane H  
**Cross-lane interfaces:** C, D, E, F, G; INV-034/035  
**Evidence class:** OFFICIAL PMLR PAPER + PREREGISTERED EVALUATION DESIGN; UQPU REPRODUCTION NOT RUN

## 1. Starting-state audit

Resolved the current main head dynamically and inspected the charter, version invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, current Batch 124 and its exact-statement split guard, latest integration/gap/worklog records, the proof-DAG and equation-discovery contracts, fundamental_limits.py, frontier_hypothesis.py, equation_discovery.py, and available Actions runs. The current starting-head core/invariant and cold-start handoff workflows were green before this commit.

## 2. Lane A: preregistered TINN acceptance contract

The new contract identifies conventional PINN, TINN, a compatible neural-operator-splitting comparator if available, and a converged numerical reference. It requires regime/trajectory-level holdouts, immutable provenance, matched optimizer/resource budgets, median and worst-case errors, PDE residuals, conservation/bounds, solver convergence, failure rates, memory/I/O, energy when measured, and cost per accepted result. It reuses existing PDE-surrogate and equation-discovery contracts instead of duplicating generic metric code.

No TINN implementation, dataset or external source revision was run. This is a benchmark protocol, not an implementation result.

## 3. Literature-surveillance delta

New-to-repository source: Dai et al., “TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs,” ICML 2026 / PMLR 306, https://proceedings.mlr.press/v306/dai26a.html. The publisher reports up to 4× relative L2-error improvement and up to 10× faster convergence on its tested tasks. The distinct mechanism is time-conditioned weights optimized via nonlinear least squares/Levenberg–Marquardt. The paper is not a new governing equation, does not guarantee arbitrary out-of-distribution generalization, and was not reproduced by UQPU. The source-specific watch records limitations and a falsifiable follow-up.

## 4. Explicit A–H status

| Lane | This-cycle disposition | Evidence class | Next gate |
|---|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Added TINN comparison and acceptance contract; reused existing metrics | Preregistered design only | Pin source/data and execute known-law PDE with grouped holdouts |
| B — cloud/QPU/provider integration | Provider-neutral routes maintained; no SDK/target or paid job | No new execution | Simulator/dry-run and target-matched accepted-task accounting |
| C — RAM/VRAM/HBM/storage/state/data movement | Added memory/checkpoint/transfer accounting requirements | No new measurement | Instrument peak memory and bytes moved in matched runs |
| D — device/chip/process/fabrication/packaging | TINNs may later model transients only after validation | No device evidence | Target-native physical observable and process data |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | Candidate future thermal/reactor/cooling use; BIO-001 and FUS-001 unchanged | No commercial evidence | Pangola mass/energy/accepted-liquid evidence and net reliable delivered-electricity envelope |
| F — economics/benchmarks/evidence/integration | Cost-per-accepted-result boundary specified | No measured economics | Equal budget, failures included, uncertainty disclosed |
| G — manufacturing equipment/software/factory systems | D/G co-design preserved; no manufacturing model qualified | No factory evidence | Validate a device/process regime before cost-per-good-unit use |
| H — strategy/finance/publication | Published source-specific watch; master-plan context preserved | Literature only | Independent replication and capital/time-to-evidence accounting |

## 5. Foundational and equation-discovery status

FND-006 advances only through a more explicit known-law model-evaluation protocol. FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-quantum-speed-limit measurement, FND-004 alternative physical primitives and FND-005 QFT/particle mechanism scans remain active without a new result. EQN-001–006 remain evidence-gated. No candidate physical equation, new theorem about nature, or improved physical bound is claimed.

## 6. INV-029–035 and evidence boundary

- **INV-029:** no physical Data-Center-to-One-Phone compression or service/energy/lifecycle-cost result.
- **INV-030:** no Pangola-carbon substitution or critical-material reduction result.
- **INV-031:** no accepted saleable-liquid/biofuel cost result; crude bio-oil is not finished fuel.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no measured reduction in financed principal, interest per accepted milestone or WACC.
- **INV-034:** foundational physics remains upstream; no new lower bound.
- **INV-035:** a model architecture and its fitted error do not establish a physical law.

INV-025/026/027 and the 100×/100,000,000× targets remain falsifiable goals. No paid QPU job was authorized or submitted. No phone-class physical-compression, universal subsystem replacement, elemental transmutation, commercial fuel/fusion, lower WACC or new-law claim is made.

## 7. Next highest-value gate

Pin TINN source/data and licenses; execute the preregistered synthetic known-law PDE benchmark with a converged independent numerical reference, frozen regime-level holdouts and equal resource budgets. Require exact-head CI for the documentation commit, then independent reproduction before downstream material, device, energy or economic use.

Research-Sync: main
