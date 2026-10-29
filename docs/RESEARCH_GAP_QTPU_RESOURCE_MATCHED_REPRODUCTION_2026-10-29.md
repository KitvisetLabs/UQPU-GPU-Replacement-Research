# Research gap RG-QTPU-RESOURCE-MATCHED-REPRO-001

**Opened:** 2026-10-29  
**Primary owner:** Lane A — workload/compiler contract  
**Interfaces:** Lane B — target/provider; Lane C — state/memory/transfer; Lane F — evidence and economics; Lane H — source provenance  
**Status:** LITERATURE-ONLY / ARTIFACT-INSPECTED / UQPU REPRODUCTION NOT RUN

The USENIX OSDI 2026 qTPU paper introduces a hybrid tensor-network representation, compiler trade-off between classical contraction overhead and quantum error, and a heterogeneous runtime. The official proceedings page and the public artifact were inspected. The artifact README and REPRODUCE guide describe pre-collected logs for figures and a hardware arm requiring IBM Quantum credentials. No benchmark was run by UQPU, and no source claim is promoted to UQPU evidence.

## Missing evidence

- Exact paper/artifact revision and data/log provenance for each result row; source revision inspected: `TUM-DSE/qtpu@3f68fc96e5de9c336c96e82d4af0a2f7a96b5a22`.
- Independently checked useful-output reference and quality tolerance shared across all comparison arms.
- Competitive current UQPU baseline, strong classical tensor-network/contraction baseline, and optional hTN-inspired arm under identical workload and compute/shot/time/memory ceilings.
- Held-out circuit families and target/noise regimes; failed runs and null results retained.
- End-to-end accounting for compilation, shots, target-specific quantum error/quality, host compute, peak memory, transfers, retries, reconstruction, billable usage, energy where measurable and cost per accepted useful task.
- Provider-neutral lowering and target-specific evidence; no cross-provider probability/price mixing.
- Permission/interface review before adapting any external code; this cycle copied no code.

## Unlock

1. Add a small machine-readable matched-output manifest before implementing a new hTN adapter.
2. Run deterministic classical references and dry-run/simulation first.
3. Compare output quality and resource accounting at the same target; keep external IBM results distinct from simulation and other providers.
4. Independently reproduce selected plots from pinned logs and then regenerate a bounded subset from source where feasible.
5. Do not schedule paid hardware without credentials, explicit owner consent and a bounded budget.

**Non-claims:** no UQPU quantum advantage, 100×/100,000,000× cost advantage, universal GPU/CPU/NPU/memory/storage replacement, material/fuel/fusion result, lower WACC, or INV-029 mission closure.
