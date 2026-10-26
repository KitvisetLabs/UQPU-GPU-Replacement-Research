# Research gap RG-QUASARQ-001 — independent, accepted-output reproduction of GPU stabilizer simulation

**Opened:** 2026-10-27  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** Lane C (memory/data movement), Lane F (benchmark/evidence/cost), Lane H (literature publication); D/G co-design review  
**Related work item:** QUASARQ-REPRO-001  
**Status:** OPEN — literature located; no source-exact build, benchmark or independent energy measurement completed

## Observed gap

Osama, Thanos and Laarman published “GPU-Accelerated Quantum Simulation of Stabilizer Circuits” in Quantum 10, 2225 on 2026-10-01 (DOI 10.22331/q-2026-10-01-2225; arXiv:2603.14641v2). The paper reports GPU-based parallel stabilizer simulation and sampling, including large Clifford circuits and substantial author-reported runtime/energy improvements. The public repository is visible at https://github.com/System-Verification-Lab/QuaSARQ.

The result is material for Lane A because a strong specialized classical baseline can change the denominator in any future quantum/hybrid cost comparison. It is material for Lane C because layout, transposes, tableau storage, memory allocation and transfers are algorithmically important. It is material for Lane F because the reported energy method is runtime multiplied by average processing-unit power and the CPU/GPU experiments use different systems.

## Unknowns and limitations

- The paper/source/dependency revisions have not been frozen for a UQPU reproduction.
- No public circuit files have been pinned into this project, and no source dataset/license audit was completed.
- No independent correctness, timing, memory, transfer or energy trial was run in this cycle.
- The paper’s one-run-per-circuit measurement experiment does not by itself quantify run-to-run uncertainty.
- Device-average-power × runtime is not equivalent by default to full system wall-plug energy or lifecycle cost.
- The benchmark domain is stabilizer/Clifford simulation; it cannot support claims about non-Clifford general-purpose workloads, quantum hardware advantage or system-wide GPU replacement.

## Required next gate

1. Pin immutable source commits and all licenses/dependencies; hash circuit bytes and environment metadata.
2. Build a small correctness suite with exact/independent references and a deliberate negative control before attempting large cases.
3. Compare QuaSARQ with Stim as the primary specialized CPU baseline and Qiskit-Aer CPU/GPU where available, with identical circuit semantics, shots, seeds and timeouts.
4. Measure repeated end-to-end latency, phase timings, host RAM, VRAM, transfers, output/reconstruction and all failed/time-out trials.
5. Measure device energy and whole-system wall-plug energy separately, with calibrated sensors and declared idle/boundary corrections.
6. Use sealed held-out circuit seeds and a non-random supported workload family; preserve failures and statistical uncertainty.
7. Publish a source-pinned result ledger and independent review before changing any UQPU baseline or economics claim.

## Falsifier

Reject the claimed reproduced gain if accepted outputs differ, gains vanish under matched baselines or repeated trials, the energy reduction disappears under a common system boundary, the result depends on selective timeout exclusion, or the method fails held-out supported circuits. If the result reproduces, the claim remains bounded to the stated classical stabilizer simulator workload.

## Mission and invariant disposition

- **INV-025/026:** no 100,000,000-GPU or universal subsystem replacement evidence is added.
- **INV-029:** no phone-class physical compression, service-capability or lifecycle-cost gate is closed.
- **INV-030:** no Pangola/biomass-carbon functional substitution or recovery result.
- **INV-031:** no accepted saleable liquid-energy/fuel result or complete bio-oil cost.
- **INV-032:** no net reliable fusion-electricity or lifecycle-cost result.
- **INV-033:** no measured financed-principal, absolute-interest, project WACC or macro-rate change.
- **INV-034:** no new foundational physics mechanism or physical limit is established.
- **INV-035:** no candidate equation or physical law is proposed; established physics remains binding.
- **INV-036/037:** no particle/spacetime primitive, Pangola-diamond technology result, or new mathematical truth claim follows.

The large append-heavy RESEARCH_GAPS.md and WORKLOG.md are deliberately untouched. This standalone gap remains open until safe index reconciliation and the independent benchmark gate.
