# SCM-GATE-003 — Prospective Cryptographic Challenge-Response Protocol

**Date:** 2026-09-28  
**Status:** PROTOCOL_ONLY / NO SOURCE CLAIM / NO CROSS-REALM RESULT  
**Purpose:** establish a leakage-resistant path from ambiguous anomaly research toward testable source-dependent information.

## Table of Contents — สารบัญ

1. [Question](#1-question)
2. [Protocol sequence](#2-protocol-sequence)
3. [Commitment model](#3-commitment-model)
4. [Scoring](#4-scoring)
5. [Leakage audit](#5-leakage-audit)
6. [Source-identity boundary](#6-source-identity-boundary)
7. [Promotion criteria](#7-promotion-criteria)
8. [Failure conditions](#8-failure-conditions)
9. [Software](#9-software)
10. [Canon integration](#10-canon-integration)
11. [Next gate](#11-next-gate)

## 1. Question

Can a candidate channel return **prospective information generated after isolation** at a rate that survives precommitted scoring, ordinary information-leakage analysis, null controls and independent replication?

This question is deliberately weaker than “is the source a deceased person?” A positive anomalous-information result would not by itself identify the source.

## 2. Protocol sequence

```text
define label space + scoring rule
-> isolate operators/decoder
-> generate unpredictable target
-> cryptographically commit target + scoring rule
-> collect response
-> freeze response commitment
-> close trial
-> reveal target + salts
-> verify commitments
-> score mechanically
-> leakage audit
-> aggregate against preregistered null
-> independent replication
```

No target-dependent feedback is allowed before the response is frozen.

## 3. Commitment model

The prototype uses SHA-256 salted commitments:

```text
C_target = SHA256(salt_target || 0x00 || target)
C_score  = SHA256(salt_score  || 0x00 || scoring_rule)
C_resp   = SHA256(salt_resp   || 0x00 || response)
```

The commitment is an integrity primitive, not proof that isolation was physically achieved. Real trials require trusted timestamps, access logs and independent custody.

## 4. Scoring

Version 1 uses a finite equiprobable label set and `exact-match-v1`.

For K labels:

```text
p_chance = 1/K
hit_rate = exact_hits/N
```

The prototype additionally reports a conservative descriptive `verified_bits` credit for exact hits above expected chance. It is **not** a p-value, Bayes factor, proof of communication or source identifier.

Future empirical analysis must precommit statistical tests, stopping rules, multiplicity correction, minimum effect size and replication criteria.

## 5. Leakage audit

Before interpreting any excess information, audit:
- filenames, metadata and target IDs;
- clocks/timing and trial order;
- network traffic and cloud logs;
- acoustic/visual cues;
- operator behavior;
- random-number generation/custody;
- prior target corpus exposure;
- AI training/retrieval contamination;
- side channels in software or hardware;
- post-selection and excluded trials.

A failed leakage audit blocks promotion regardless of statistical score.

## 6. Source-identity boundary

The evidence ladder remains:

```text
unexpected hit
!= anomalous information
!= bidirectional communication
!= deceased-agent identity
!= physical mechanism
```

Identity requires additional unpredictable, source-specific authentication that distinguishes ordinary leakage, fraud, inference, living-agent hypotheses and unknown non-agent processes.

## 7. Promotion criteria

A future SCM-E4 candidate requires:
1. prospective targets generated after isolation;
2. precommitted label space and scoring;
3. immutable target/response commitments;
4. complete trial accounting;
5. effect above preregistered null with appropriate uncertainty;
6. passed leakage audit;
7. held-out replication.

SCM-E5 additionally requires repeated bidirectional challenge-response and independent replication. The present repository has **no E4/E5 result**.

## 8. Failure conditions

Automatic failure includes target reveal before response freeze, changed scoring after reveal, unverifiable commitments, missing trials, selective reporting, discoverable target metadata, uncontrolled operator contact or inability to reproduce the protocol independently.

## 9. Software

- `software/uqpu-prototype/uqpu/scm_challenge_response.py`
- `software/uqpu-prototype/tests/test_scm_challenge_response.py`

The code implements commitment/freeze/reveal verification and exact-match scoring. It does not conduct a paranormal experiment.

## 10. Canon integration

In *คำภีร์โลกาธิบดี*, this becomes the scientific turning point between SCM-2 imagery and SCM-3 communication. Characters must stop asking whether a signal “looks spiritual” and instead ask whether a sealed, unpredictable challenge returns authenticated information.

Volume 3 can make commitment custody, spoofing and adversarial leakage central plot mechanics; Volume 4 can require independent replication before institutions act; Volume 5 can cross the fictional E5 threshold only after those controls survive.

## 11. Next gate

**SCM-GATE-004 — Independent Replication Contract:** freeze protocol version, data schema, randomization, exclusions, scoring, environment logs and reproducibility package so a second team can attempt the same test without privileged knowledge.
