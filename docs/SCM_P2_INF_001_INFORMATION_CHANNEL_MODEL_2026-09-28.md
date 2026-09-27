# SCM-P2-INF-001 — Mathematical Information-Channel Model

**Date:** 2026-09-28  
**Status:** MODEL / FICTION-ENGINEERING BRIDGE / NO DEMONSTRATED CROSS-REALM CHANNEL

## Table of Contents — สารบัญ
1. [Question](#1-question)
2. [Channel abstraction](#2-channel-abstraction)
3. [Capacity and reliability](#3-capacity-and-reliability)
4. [Authentication](#4-authentication)
5. [Text-audio-video ladder](#5-text-audio-video-ladder)
6. [Latency and synchronization](#6-latency-and-synchronization)
7. [Identity continuity](#7-identity-continuity)
8. [SCM-3 terminal architecture](#8-scm-3-terminal-architecture)
9. [Falsifiers](#9-falsifiers)
10. [Canon progression](#10-canon-progression)

## 1. Question
If a future in-world experiment produced reproducible prospective information beyond ordinary channels, what engineering quantities would be required to turn that observation into communication?

## 2. Channel abstraction
Let X be a precommitted challenge symbol, Y the frozen recovered symbol and Z all measured ordinary side information. The key fictional research target is conditional information `I(X;Y|Z)`: recoverable target information remaining after modeled ordinary leakage.

A real-world SCM claim is not made by defining this quantity.

## 3. Capacity and reliability
For K equiprobable symbols with symbol error probability `p_e`, SCM tracks:
- symbol error rate;
- verified information per trial;
- verified bit rate `R_v = I_verified/T`;
- latency;
- erasure/abstention rate;
- replication stability.

A useful terminal requires `R_v` above zero under preregistered controls and enough margin for error correction. Statistical anomaly without usable rate is not a telephone.

## 4. Authentication
Separate channel existence from identity:
```text
channel test -> unpredictable challenge
identity test -> multiple source-specific prospective challenges
session auth -> nonce/challenge-response
message integrity -> commitment/hash/signature-like provenance
anti-replay -> unique trial/session IDs
```
Biographical facts, voice likeness or facial resemblance alone are weak authenticators because they can be copied or inferred.

## 5. Text-audio-video ladder
**SCM-3A Symbol/Text:** finite symbols, low bandwidth, easiest to score.
**SCM-3B Audio:** decoded temporal stream; requires bandwidth, synchronization and artifact controls.
**SCM-3C Video-like state reconstruction:** highest bandwidth. In fiction, do not require ordinary photons to travel from another realm; the terminal may reconstruct a visual state from an authenticated encoded channel. Reconstruction uncertainty must remain visible.

This progression makes “video call with the deceased” an earned engineering endpoint rather than the first experiment.

## 6. Latency and synchronization
Track one-way/round-trip latency, jitter, clock uncertainty and dropped/erased symbols. Apparent anticipation of a target is first treated as timestamp leakage or clock error.

## 7. Identity continuity
A persistent fictional identity requires repeated authentication across sessions, stable but non-public challenge knowledge, behavioral continuity and resistance to replay/deepfake attacks. The story can keep philosophical personal-identity questions distinct from protocol identity.

## 8. SCM-3 terminal architecture
```text
sensor front end
-> provenance/null filter
-> candidate-channel demodulator
-> error detection/correction
-> challenge-response authenticator
-> identity/session layer
-> semantic codec
-> text/audio/video renderer
-> immutable audit log
```
The renderer is never allowed to overwrite raw evidence.

## 9. Falsifiers
The channel hypothesis weakens/fails if performance returns to chance under isolation; tracks metadata/timing; vanishes under independent hardware; depends on post-selection; cannot answer unpredictable challenges; or cannot reproduce at a second site.

## 10. Canon progression
Vol 1 establishes signal vs meaning. Vol 2 discovers candidate modulation but fights artifacts. Vol 3 achieves low-rate authenticated symbols and confronts spoofing. Vol 4 scales bandwidth under governance/war pressure. Vol 5 reaches fictional bidirectional audio/video-like reconstruction only after independent replication, while SCM-4 transport remains separate.
