# Literature Watch — Quantum strong Mpemba effect by coherence elimination

**Watch date:** 2026-10-26  
**Primary source date:** 2026-10-22 (Physical Review Letters publication; accepted 2026-10-02)  
**Primary owner:** Lane A — quantum programming/runtime and accepted-task resource accounting  
**Cross-cutting links:** FND-001 thermodynamic-gap accounting; FND-003 matched control-versus-quantum-speed-limit protocol; Lane C state preparation/readout; Lane F evidence and economics  
**Evidence class:** PEER-REVIEWED_PRIMARY_SOURCE / LITERATURE_ONLY_FOR_UQPU  
**Promotion:** no UQPU performance, wall-plug-energy, quantum-advantage, new-law, material, fuel, fusion or financing claim promoted

## Primary source

Xiang Zhan, Huixia Gao, Lei Xiao and Peng Xue, “Genuine Quantum Strong Mpemba Effect by Eliminating Coherence,” *Physical Review Letters* **137**, 170403 (2026), published 22 October 2026, DOI: 10.1103/z9t9-mwgv.  
Official article: https://journals.aps.org/prl/abstract/10.1103/z9t9-mwgv

## Genuine novelty

The authors analyze a Davies-map relaxation model in which the slowest decay modes can be degenerate and purely coherent. Their mechanism removes the relevant coherence so the initial state has reduced overlap with the slow modes, allowing a strong-Mpemba-type relaxation advantage without requiring a unique slowest mode. They report a controllable optical implementation simulating the Davies map and check the semigroup property of the dynamics. The demonstrated system is a minimal single qubit.

This is a useful, concrete reminder that state preparation can alter relaxation dynamics. It is not evidence that the preparation protocol is free, that net energy consumption falls, or that a computational task finishes sooner at equal accepted-output quality.

## Limitations and evidence boundary

- The optical apparatus simulates an open-system map; this is not a demonstration of a commercial thermal engine, a scalable quantum processor, or a general-purpose compute workload.
- A faster selected relaxation metric does not by itself imply lower total wall-clock time, lower heat, lower wall-plug energy, greater work extraction, or lower cost.
- The preparation/control/readout/reset overhead, optical-source and detector energy, repeated-trial yield, accepted-output fidelity and lifecycle cost must be measured before a UQPU-relevant benefit can be claimed.
- A relaxation-time observation is not an entropy-production or energy measurement. These quantities must remain separately typed and reported.
- No project experiment, independent reproduction, provider job or external expenditure was performed for this watch.

## Exact UQPU relevance

- **FND-001:** extend the resource ledger to distinguish a relaxation metric from entropy production, heat and wall-plug energy. The entire state-preparation-to-accepted-output boundary must be included.
- **FND-003:** any future speed comparison must use matched initial/output contracts and include preparation, control, relaxation, measurement, reset and failure/retry costs; a protocol-level acceleration is not a quantum-speed-limit violation.
- **Lane A:** only consider this mechanism for a workload if a concrete state-initialization, reset, or open-system runtime bottleneck is identified and the final accepted useful output is unchanged.
- **Lane C:** record state preparation, coherence manipulation, readout, reset, persistence and reconstruction explicitly. Hilbert-space size is not readable classical storage.
- **Lanes D/G:** the optical implementation is a platform lead, not a fabrication requirement. Device/process consequences require target-specific control, stability, readout and resource evidence.
- **Lanes E/F:** no direct Pangola-carbon, bio-oil, fusion-electricity or financing result follows. If a later system-level energy claim is proposed, include cooling, control electronics, utilization, capital and lifetime costs where applicable.
- **Lane H:** the result is a peer-reviewed research lead; strategic and funding decisions remain gated on reproducible function and full-system economics.

## Falsifiable follow-up: FND-001-QMP-001

1. Freeze the source version, equations, Davies-map parameters, initial states, observable, relaxation metric, acceptance threshold and code/data hashes before reproducing the result.
2. Reproduce the single-qubit dynamics with an independently implemented solver and compare against an analytic or exact small-system reference where available.
3. Pre-register held-out generator parameters and initial states, including null controls where coherence removal does not reduce overlap with the slowest mode. Keep the baseline and candidate final-state/observable acceptance criteria identical.
4. Measure or explicitly mark unavailable each term in
   \[
   t_{\rm accepted}=t_{\rm prep}+t_{\rm control}+t_{\rm relax}+t_{\rm readout}+t_{\rm reset}+t_{\rm retries}.
   \]
   For energy, record the analogous component ledger separately; do not infer energy from time or entropy from a fitted relaxation curve.
5. Report all trials, failures, uncertainty, output quality, total time and energy per accepted result. Compare against a matched protocol, not a relaxation-only denominator.
6. Reject a claimed UQPU benefit if the apparent relaxation improvement disappears after overheads, fails on held-out parameters, changes the accepted output, or cannot be independently reproduced.

**Stop condition:** remain LITERATURE_ONLY until the reproduction and matched-overhead gate passes. Any later real-QPU work remains simulator/dry-run first and requires separate credentials, a bounded budget and explicit user consent.

## Cross-lane status at this watch

A: candidate use is conditional on a concrete runtime bottleneck; no workload result.  
B: no provider or target change; no job submitted.  
C: preparation/readout/reset accounting highlighted; no memory-capacity result.  
D: no device/process result.  
E: no biomass/material/fuel/fusion result.  
F: full accepted-task time/energy/cost boundary specified; no measured economics.  
G: no manufacturing result; D/G co-design remains required if a device path emerges.  
H: dated primary-source watch recorded; multilingual strategic references remain canonical.

## Invariant disposition

INV-029 remains an unclosed physical-compression mission. INV-030 has no new material-substitution evidence. INV-031 has no accepted low-cost liquid-fuel result. INV-032 has no reliable net delivered fusion-electricity result. INV-033 has no measured principal/interest/WACC effect. INV-034 remains an active foundational agenda under current physical constraints. INV-035 remains hypothesis-generation plus falsification, proof and independent-validation discipline; this paper is not a new physical law or a bypass of established limits.

**Next highest-value gate:** complete a source-exact, independently checked, held-out reproduction with preparation/control/readout/reset accounting before considering any system-level consequence.
