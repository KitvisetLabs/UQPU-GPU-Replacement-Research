# SCM PHASE 2 — Preregistered Experimental Design Program

**Date:** 2026-09-28  
**Status:** EXPERIMENT-DESIGN INFRASTRUCTURE / NO EMPIRICAL CROSS-REALM RESULT

## Table of Contents — สารบัญ
1. [Purpose](#1-purpose)
2. [Phase-2 rule](#2-phase-2-rule)
3. [Protocol families](#3-protocol-families)
4. [Preregistration minimum](#4-preregistration-minimum)
5. [Leakage audit](#5-leakage-audit)
6. [Human-participant boundary](#6-human-participant-boundary)
7. [Evidence promotion](#7-evidence-promotion)
8. [Phase-2 sequence](#8-phase-2-sequence)
9. [Software](#9-software)
10. [Next implementation](#10-next-implementation)

## 1. Purpose
Convert SCM Phase-1 controls into empirical-study designs whose hypotheses, outcomes and analysis are fixed before data collection.

## 2. Phase-2 rule
**No data first, hypothesis later.** Every empirical SCM run must identify its null, primary outcome, fixed sample size/stopping rule, randomization, blinding, exclusions, leakage audit, calibration, analysis and replication plan before collection.

Passing preregistration means the study is methodologically specified; it is not evidence for an anomalous source.

## 3. Protocol families
### P2-A — Ordinary-environment calibration
Known injected RF/acoustic/vibration/thermal/optical disturbances test detector false positives and attribution.

### P2-B — Ambiguous-signal decoder controls
Blinded noise/ambiguous samples quantify human/AI pareidolia, priming and post-selection risk.

### P2-C — Prospective information-channel test
Only after A/B controls are characterized: unpredictable post-isolation targets, commitment/freeze/reveal, fixed scoring and leakage audit.

P2-C can test information dependence; it cannot by itself establish deceased-agent identity.

## 4. Preregistration minimum
The executable contract requires study/protocol IDs, primary and null hypotheses, primary outcome, fixed N, stopping rule, randomization, >=2 blinding roles, exclusions, calibration, analysis, replication and the complete leakage checklist.

## 5. Leakage audit
Mandatory items: target metadata, filenames, trial timing, network traffic, operator contact, audio/visual cues, RNG custody, AI retrieval/training contamination and post-selection.

## 6. Human-participant boundary
The validator blocks a human-participant study without an ethics-approval/reference field. Actual ethical adequacy cannot be established by software alone and must follow applicable institutional/legal requirements and informed consent.

## 7. Evidence promotion
```text
valid preregistration
-> calibrated run
-> complete trial ledger
-> frozen raw data
-> preregistered analysis
-> leakage audit
-> result with uncertainty
-> held-out/independent replication
-> only then consider evidence-state promotion
```

No statistical result alone identifies a spiritual source.

## 8. Phase-2 sequence
1. **SCM-P2-CAL-001:** known-interference calibration study.
2. **SCM-P2-DEC-001:** blinded ambiguous-signal decoder study.
3. **SCM-P2-INF-001:** prospective information-channel protocol.
4. **SCM-P2-REP-001:** independent-site reproduction.

The safest first empirical target is CAL-001 because its ground truth is ordinary, injected interference.

## 9. Software
- `software/uqpu-prototype/uqpu/scm_preregistration.py`
- `software/uqpu-prototype/tests/test_scm_preregistration.py`

Evidence label: `PREREGISTRATION_ONLY_NO_EMPIRICAL_RESULT`.

## 10. Next implementation
Build a machine-readable **trial ledger + calibration record** for SCM-P2-CAL-001, with immutable trial IDs, condition randomization, sensor calibration provenance, exclusions and raw-data hashes. Generate synthetic fixtures first; do not label them empirical observations.
