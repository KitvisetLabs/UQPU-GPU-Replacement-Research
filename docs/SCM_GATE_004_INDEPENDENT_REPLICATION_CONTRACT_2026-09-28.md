# SCM-GATE-004 — Independent Replication Contract

**Date:** 2026-09-28  
**Status:** REPLICATION_INFRASTRUCTURE_ONLY / NO EMPIRICAL SOURCE CLAIM

## Table of Contents — สารบัญ
1. [Objective](#1-objective)
2. [Frozen replication package](#2-frozen-replication-package)
3. [Required environmental record](#3-required-environmental-record)
4. [Integrity and protocol drift](#4-integrity-and-protocol-drift)
5. [Independent-team rule](#5-independent-team-rule)
6. [Evidence promotion](#6-evidence-promotion)
7. [SCM pipeline status](#7-scm-pipeline-status)
8. [Software](#8-software)
9. [Next research frontier](#9-next-research-frontier)

## 1. Objective
Make a claimed positive **or negative** SCM experiment reproducible by a second team without privileged knowledge, unpublished scoring choices or selective trial access.

## 2. Frozen replication package
Before replication, freeze: protocol ID/version; exact code commit; raw-data SHA-256; schema; randomization method; scoring rule; exclusions; required environment fields. A changed dataset must fail integrity verification rather than silently becoming a new run.

## 3. Required environmental record
Minimum contract records UTC start/end, coded location, hardware IDs, software commit, operator roles, network state and RF/acoustic/thermal/power logs. Future hardware-specific protocols may add magnetic, vibration, optical and calibration records.

## 4. Integrity and protocol drift
The validator distinguishes missing provenance from an experimental result. Cross-site comparison checks preregistered invariant fields so changes in scoring/label space/protocol cannot be hidden as “replication.”

## 5. Independent-team rule
A meaningful replication team should receive the frozen protocol and required materials, not target answers or discretionary post-hoc interpretation. Independence must be documented; software equality alone is not laboratory independence.

## 6. Evidence promotion
A replication package passing validation means only **the package is reproducible enough to attempt**. It does not promote SCM evidence. Promotion requires empirical data, passed controls and an independent result under the frozen contract.

## 7. SCM pipeline status
| Gate | Function | Current status |
|---|---|---|
| SCM-GATE-001 | multimodal ordinary-cause/null characterization | synthetic implementation |
| SCM-GATE-002 | blinded decoder / pareidolia control | synthetic implementation |
| SCM-GATE-003 | prospective commit-freeze-reveal challenge-response | protocol implementation |
| SCM-GATE-004 | independent replication contract | protocol implementation |

None of these statuses is evidence for spirits, post-mortem consciousness or cross-realm communication.

## 8. Software
- `uqpu/scm_replication_contract.py`
- `tests/test_scm_replication_contract.py`

## 9. Next research frontier
With GATE-001–004 infrastructure established, the next responsible step is **SCM-PHASE-2 Experimental Design**: define preregistered empirical protocol families without running or claiming a paranormal experiment. Candidate families should include ordinary-environment calibration, blinded ambiguous-signal controls and prospective information-channel tests. Human-participant work requires appropriate ethics/consent governance.
