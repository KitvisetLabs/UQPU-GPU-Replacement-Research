# Daily integration — 2026-10-29 — parity-QAOA implementation

**Canonical starting SHA:** 6eafdd40f73c4db40fc78ec553bb8eb426c156ff  
**Primary owner:** Lane A; integration owner Lane F  
**Interfaces:** B/C/D/E/G/H, FND-001–006, EQN-001–EQN-010  
**Evidence class:** PROTOTYPE + EXACT SMALL-INSTANCE CLASSICAL CERTIFICATE  
**Hardware:** no real QPU, no paid job, no physical experiment

## Change

The repository now has a higher-order parity-QAOA circuit generator, an exact bounded objective certificate, and a dense-statevector regression test for the CNOT/RZ phase gadget. The model uses an even-parity penalty for each fundamental cycle and a standard RX mixer. The mixer is not feasibility-preserving, so measurement outputs must be filtered/decoded under the same accepted-output contract.

## Integration contract

- A: exact objective and argmin-set certificate precede matched parity-versus-direct QAOA comparisons.
- B: provider-neutral lowering only; no hardware submission.
- C: report physical edge qubits, state bytes, output and reconstruction; do not equate qubit count with readable memory.
- D/G: native gate decomposition, noise, yield and device costs remain separate, future gates.
- E: BIO-001 and FUS-001 are unchanged and not supported by this prototype.
- F: all future comparisons require identical workload/acceptance/reference hashes, equal budgets and complete resource/cost records.
- H: preserve this batch, literature watches, strategic model and multilingual references.

The triangle certificate is exact for its bounded instance only. It is not evidence of QPU advantage or scalable resource reduction.

## Next gate

Run CI and independently review the penalty proof and circuit semantics. Then benchmark parity and direct QAOA on held-out graphs under equal shots/optimizer budgets and full resource accounting.
