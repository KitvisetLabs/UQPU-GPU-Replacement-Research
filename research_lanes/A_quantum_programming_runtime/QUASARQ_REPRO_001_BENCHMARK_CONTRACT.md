# QUASARQ-REPRO-001 — matched useful-output benchmark contract

**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** Lane C memory/data movement; Lane F evidence/benchmark/cost; Lane H source publication  
**Related:** INV-004, INV-007, INV-019–027, INV-034/035; RG-QUASARQ-001  
**Status:** PREREGISTERED DESIGN ONLY — no source build or benchmark executed by this record

## Question

Can the published QuaSARQ GPU stabilizer simulator reproduce its claimed runtime/energy scaling under a pinned, correctness-gated and resource-matched comparison with a competitive classical baseline?

This question is intentionally narrower than “does UQPU replace GPUs?” The tested function is classical simulation of Clifford/stabilizer circuits, not execution of a general quantum workload on a QPU.

## Immutable inputs required before a run

- Paper: Quantum 10, 2225 (2026), DOI 10.22331/q-2026-10-01-2225; arXiv version 2603.14641v2.
- Exact QuaSARQ source commit, license, submodules, dependencies and build flags.
- Exact Stim/Qiskit-Aer source versions and runtime settings.
- Circuit generator version, seed list, raw circuit SHA-256, gate count, depth, qubit count, measurement count, shot count and expected output semantics.
- Host and accelerator model, memory sizes, operating system, drivers, compiler/toolchain, clocks/power policy, thermal state and background-load policy.
- Frozen timeouts, warmup policy, repeat counts, measurement protocol and cost basis.
- A sealed held-out circuit/seed set. Do not tune on it.

A manifest that merely declares these values is not proof that a public dataset was downloaded, that a license is satisfied, or that the split is valid. Raw bytes and hashes must be independently checked.

## Workload tiers

1. **Correctness tier:** small deterministic and stochastic Clifford circuits; exact checks where available; independent reference; negative control containing a known circuit/output mismatch.
2. **Scaling tier:** frozen random Clifford circuits with varied qubit count, depth and measurement density. Keep each circuit identical across methods.
3. **Sampling tier:** same circuit and shot count, comparing detector/observable distributions and observable error rates. Include the paper’s 1,024-shot setting as a source-reproduction point, not as the only operating point.
4. **Stress tier:** large circuits only after the smaller tiers pass; declare GPU-memory and runtime ceilings in advance. Count all timeouts, out-of-memory errors and incomplete cases in the denominator.
5. **Generalization tier:** held-out circuit seeds and at least one non-random but licensed/public workload family where the same stabilizer semantics are supported. Do not generalize beyond Clifford/stabilizer circuits.

## Acceptance predicates

A trial is accepted only if:
- source/input identities and environment hashes match the preregistered manifest;
- deterministic outputs match exactly where the algorithm promises deterministic equivalence;
- stochastic output passes a predeclared distributional check with confidence interval and no post-hoc test selection;
- all required detector/observable/logical-output fields are present and validated;
- the run respects the declared resource/time budget;
- all failed runs, retries and rejected outputs are retained.

A completed process or returned exit code is not sufficient.

## Required ledger fields

For every method × circuit × seed × trial, record:
- method/version/source SHA, environment identity, workload/circuit SHA and semantic output contract;
- accepted/rejected status and reason, correctness result, observable/detector statistics and confidence intervals;
- wall time end-to-end and per phase (parse, allocation, scheduling, transfer, kernel, synchronization, output/reconstruction);
- CPU/GPU model, host RAM/VRAM peak and allocation, transfer bytes/time, output bytes and temporary state;
- shots, seeds, retries, timeouts, errors and all failed runs;
- energy value, unit, sensor/source, calibration, sampling interval, idle correction and boundary (device-only versus whole-system wall-plug);
- throughput, latency distribution, accepted outputs per second, energy per accepted output;
- hardware cost/amortization assumptions, utilization, energy tariff and cost per accepted output only when supported by measured or explicitly modeled inputs;
- raw record hashes, preprocessing/config hashes and reproducibility command.

Use the existing provider-matched execution-record policy for any later QPU comparator; do not create a second provider/pricing schema. This simulator-only contract does not authorize QPU jobs.

## Resource and statistical rules

- Use the same circuit bytes, semantic output, shot count and declared timeout across methods.
- Use the same seed set for paired stochastic trials where supported.
- Run at least 5 timed repeats per feasible deterministic case after warmup and at least 30 paired sampling seeds where the declared budget permits. If a tier cannot meet these counts, mark it underpowered and report all trials.
- Report medians and dispersion plus confidence intervals; include all failed/time-out trials and define censoring before looking at results.
- Do not treat runtime × nominal TDP as measured energy. Prefer calibrated wall-plug metering for whole-system energy and separately report validated device telemetry.
- Do not compare a GPU run on one machine with a CPU run on another and call it a controlled same-host comparison. If same-host operation is impossible, explicitly label a cross-system comparison and publish the hardware/cost boundary.
- Do not multiply subsystem gains or equate qubit counts with readable RAM/VRAM/storage.

## Falsification and stop rules

Stop promotion if correctness fails, output semantics differ, exact inputs cannot be pinned, license terms are unresolved, a baseline is not competitive, repeated runs overturn the claimed effect, energy boundaries differ, or advantage exists only in selected successful instances. Preserve the negative results and failures.

Even a successful reproduction is limited to the stated stabilizer-simulation workload and hardware boundary. It does not establish QPU speedup, universal GPU/CPU/NPU replacement, 100,000,000× cost advantage, readable quantum memory, a new physical law, commercial bio-oil, net fusion electricity, lower WACC, or phone-class physical compression.
