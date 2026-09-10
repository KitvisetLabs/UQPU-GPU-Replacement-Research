# Lane B — Batch 018

The IBM/Qiskit target-aware path now executes both 3- and 6-qubit fixtures against the saved FakeKingston snapshot. ER6 transpiles to depth 76 and 26 CZ operations on active physical qubits 138, 148, 149, 150, 151 and 152.

This strengthens provider-target plumbing but does not verify IBM cloud execution. The next Lane B gate remains provider-matched: freeze a real accessible backend, preserve the contract and QASM mapping, obtain a dated live calibration, then run a bounded authorized job with job ID and billing provenance.

No paid job was submitted.
