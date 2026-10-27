# QAOA parity comparison contract — 2026-10-27

**Primary owner:** Lane A — workload/algorithm/compiler/runtime  
**Evidence and integration owner:** Lane F  
**Cross-lane consumers:** B, C, D, G, H and INV-034/035  
**Status:** comparison schema implemented and locally tested; algorithm reproduction and matched benchmark remain open.

## Purpose

The 2026-10-27 literature watch identifies higher-order parity constraints as a candidate QAOA encoding for sparse signed Max-Cut. Before adding a parity implementation or spending on hardware, UQPU needs a fail-closed record contract that prevents an apparent quality improvement from being compared against a different workload, target, calibration, price schedule or resource budget.

The new module is software governance and measurement infrastructure. It does not implement parity encoding, run a QPU, authenticate external hashes by itself, or establish a performance advantage.

## Record and pairing requirements

Each QAOARunRecord binds:

- SHA-256 identities for the workload contract, held-out test manifest, acceptance contract, reference certificate and target configuration;
- method, provider and target identity, plus the evidence class;
- total shots, optimizer evaluations, repetitions, accepted outputs and a shared quality gate;
- physical qubits, two-qubit gates, circuit depth, host compute, end-to-end latency, accepted-task throughput, input/output/transfer bytes, peak memory, state-representation kind/bytes, reconstruction time and retries;
- provider billable units and unit kind, recorded separately from shot count;
- optional measured energy with a named measurement method;
- for REAL_QPU records, job ID, run-log hash, pricing snapshot and calibration epoch;
- all-in USD cost components: provider, host compute, input preparation, data movement, mitigation/retries, output reconstruction, energy and capital allocation.

The paired comparator rejects mismatched workload/test/acceptance/reference identities, provider, target/configuration, evidence class, shots, optimizer evaluations or repetitions. It rejects test-optimum leakage. Saved-calibration simulations must use the same calibration snapshot. REAL_QPU pairs must use the same pricing snapshot and calibration epoch.

Unknown cost is not silently treated as zero. A cost component is zero only when explicitly inapplicable; missing values or a listed unpriced component block the all-in cost and economic-claim eligibility. A quality pass requires the frozen acceptance contract to be satisfied. Successful execution alone is insufficient. A billable-unit count is not inferred from the number of shots.

## Claim boundary

The comparator reports matchedness, acceptance probability, latency, throughput and billable usage for any evidence class. It permits an economic comparison only when both records are REAL_QPU, both pass the same quality contract, both have accepted tasks and every required cost component is priced. Even then, the returned ratio is a comparison candidate that requires audit of the source manifests and independent reproduction; it is not a project-wide claim by itself.

The contract does not assume equal qubit count or equal gate count: those are method-dependent resources to be recorded and compared, not hidden. The same total-shot and optimizer-evaluation budgets are enforced for the current equal-budget experiment. Other budget regimes must be preregistered as separate comparisons.

## Local validation

The focused test file covers matched simulation, provider and target mismatch, pricing mismatch, equal-budget enforcement, test-optimum leakage, saved-calibration identity, required real-job and billable-usage provenance, incomplete costs, accepted-output counts, latency/throughput reporting, state/I/O/transfer fields, energy measurement metadata and empty identity fields. Local isolated run: **16 tests passed**. Exact-head repository CI remains the release gate.

## Next gate

Implement or independently import a parity encoder behind the existing provider-neutral workload path, then run exact small-instance checks and target-aware simulation using a frozen manifest. Do not submit a paid QPU job without credentials, a bounded budget and explicit user consent. No physical-law, material, fuel, fusion, financing-rate or Data-Center-to-Phone claim follows from this contract.
