# Lane C — State / Memory / Storage Evidence Checklist

For any workload claiming replacement of RAM, VRAM/HBM or persistent-storage functions, record:

1. input-state size and loading path;
2. intermediate materialized classical bytes;
3. host RAM/accelerator memory footprint;
4. quantum/provider-side state lifetime and reuse assumptions;
5. output/readout bytes and reconstruction cost;
6. checkpoint/persistence semantics;
7. recovery after failure/retry;
8. host-device/network transfer volume and time;
9. whether recomputation substitutes for storage;
10. total cost/useful-task impact.

A quantum state is not counted as classical readable storage merely because it contains amplitudes.

**Evidence status:** ENGINEERING EVIDENCE CHECKLIST.
