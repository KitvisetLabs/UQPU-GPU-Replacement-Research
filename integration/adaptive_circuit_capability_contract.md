# Provider-neutral adaptive-circuit capability contract

**Contract owner:** Lane A — quantum programming/runtime  
**Integration owners:** Lane B (provider evidence), Lane F (acceptance/economics)  
**Status:** Implemented as a fail-closed metadata contract; no provider target has been certified by this artifact.

## Purpose

Adaptive quantum workloads may require mid-circuit measurement, reset, and classical conditional/feed-forward operations. A provider-neutral compiler must not infer these semantics from a provider name, simulator success, or a generic QPU label.

The executable interface is \`software/uqpu-prototype/uqpu/adaptive_circuit_contract.py\`. It records one provider/target/API-version tuple and requires an HTTPS source, source-check timestamp, and SHA-256 provenance digest.

## Required fields

- provider and target identity;
- API/version context;
- evidence class: \`OFFICIAL_PROVIDER_DOCUMENTATION\`, \`SIMULATION_ONLY\`, \`DRY_RUN_ONLY\`, or \`MODEL_ONLY\`;
- source URI, UTC timestamp and source digest;
- explicit True/False/unknown values for mid-circuit measurement, reset and classical conditionals;
- target limits for mid-circuit measurements and conditional depth when known;
- measurement/feed-forward latency when measured.

Unknown values fail closed. A documented capability may permit route lowering only. Hardware results require a separate execution certificate; this contract does not submit jobs, grant permission, or accept useful-output quality.

## Minimum workload acceptance path

1. Freeze an identical useful-output contract and exact circuit/workload digest.
2. Validate official target documentation and API version for all three dynamic-circuit primitives.
3. Run a simulator/dry-run first and test positive and negative branch paths.
4. Compare against a competitive classical feedback/control baseline.
5. If and only if separately authorized, execute on one named target with bounded jobs/shots/cost.
6. Record accepted-output quality, latency, throughput, measurement/reset counts, host compute, data movement, retries, billable usage, energy where measurable, and total cost per accepted useful task.
7. Keep result and pricing provenance bound to the same provider and target.

The published adaptive-circuit experiment is external literature, not evidence that any UQPU adapter or target passes these gates. No target is marked supported in this cycle.
