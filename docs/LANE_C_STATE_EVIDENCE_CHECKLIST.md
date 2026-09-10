# Lane C — State / Memory / Storage Evidence Checklist

For any workload claiming replacement, reduction or semantic elimination of volatile-memory or persistent-storage functions, identify both the **memory role** and the **physical technology** being compared.

Memory roles include:
- system/host volatile memory — RAM commonly implemented with DDR/LPDDR/RDIMM/MRDIMM-class DRAM;
- accelerator-local volatile memory — VRAM/HBM/GDDR, including DRAM-based implementations;
- on-chip volatile memory — SRAM/cache/register-file roles;
- persistent storage — SSD/HDD and other nonvolatile tiers.

`DRAM` is therefore not treated as a separate peer subsystem beside RAM and HBM. It is an implementation technology family spanning multiple volatile-memory roles.

For every serious memory/state claim, record:

1. input-state size and loading path;
2. intermediate materialized classical bytes;
3. host/system-memory technology and peak capacity footprint;
4. accelerator-local memory technology and peak capacity footprint;
5. on-chip SRAM/cache assumptions when material to the comparison;
6. sustained and peak memory bandwidth relevant to the workload;
7. access latency / service-time assumptions relevant to the workload;
8. DRAM refresh, idle/standby and active-access energy where DRAM is in the baseline;
9. quantum/provider-side state lifetime and reuse assumptions;
10. output/readout bytes and reconstruction cost;
11. checkpoint/persistence semantics;
12. recovery after failure/retry;
13. host-device/network transfer volume and time;
14. whether recomputation substitutes for storage;
15. total memory-system cost per accepted useful task;
16. total end-to-end cost/useful-task impact.

A quantum state is not counted as classical readable storage merely because it contains amplitudes. A reduction in DRAM bytes is not itself a DRAM replacement claim unless the workload's required capacity, bandwidth, latency, persistence/recovery behavior and end-to-end economics remain acceptable.

**Evidence status:** ENGINEERING EVIDENCE CHECKLIST.
