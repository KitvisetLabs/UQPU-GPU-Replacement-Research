# Cycle 001 Delta 05 — Literature Snapshot: Biomass EMI + Bosonic QEC

**Date:** 2026-09-28  
**Status:** EXTERNAL-LITERATURE SNAPSHOT / NOT PANGOLA MEASUREMENT / NOT UQPU HARDWARE EVIDENCE

## Table of Contents — สารบัญ
1. [Purpose](#1-purpose)
2. [DMF-BIOCARBON-EMI-001](#2-dmf-biocarbon-emi-001)
3. [FND-BOSONIC-QEC-001](#3-fnd-bosonic-qec-001)
4. [Cross-lane consequences](#4-cross-lane-consequences)
5. [Next tests](#5-next-tests)

## 1. Purpose
Replace generic named pathways with current external anchors while preserving the distinction between literature feasibility, Pangola-specific material qualification, and project hardware evidence.

## 2. DMF-BIOCARBON-EMI-001
Recent reviews report biomass-derived carbon/material routes for EMI shielding across polymer composites, porous foams/aerogels and other structures. The literature emphasizes conductivity, porous/microstructural design, absorption/reflection behavior, thickness, frequency range, process route, scalability and environmental durability as relevant variables.

Sources:
- Gokce et al., *Materials Chemistry and Physics* 317 (2024) 129165, DOI 10.1016/j.matchemphys.2024.129165.
- Review, *New Carbon Materials* 40 (2025) 293–316, DOI 10.1016/S1872-5805(25)60965-6.
- Venkatagiri et al., *Discover Polymers* 2 (2025), agricultural/forestry/marine biomass EMI review.
- Wang et al., *Journal of Materials Science & Technology* 243 (2026) 28–44, DOI 10.1016/j.jmst.2025.04.019.

**Inference permitted:** biomass-derived materials are a legitimate candidate family for an EMI functional-unit experiment.

**Inference not permitted:** Pangola-derived carbon has achieved any cited shielding value. No Pangola coupon has been measured by this project.

### First coupon gate
Freeze feedstock provenance; moisture/ash; pyrolysis/carbonization conditions; purification/activation; binder/filler fraction; thickness/density. Measure conductivity and shielding effectiveness across a predeclared frequency band, plus thermal/mechanical stability. Compare with a named incumbent at equal functional constraints. Record energy, chemicals, yield and cost.

## 3. FND-BOSONIC-QEC-001
Named alternative physical primitive: bosonic encoded qubits / oscillator Hilbert space for hardware-efficient QEC.

Current experimental anchors include:
- Putterman et al., *Nature* 638 (2025) 927–934: concatenated bosonic cat qubits plus repetition code; below-threshold phase-flip correction was reported and logical-error behavior was measured.
- Brock et al., *Nature* 641 (2025) 612–618: GKP logical qutrit/ququart error correction beyond break-even was reported.
- integrated photonic GKP source, *Nature* 642 (2025) 587–591: generated optical GKP states on an integrated photonic platform; authors identify further optical-loss reduction as necessary for fault-tolerant-regime states.

### INV-036 record
- **difference:** oscillator/bosonic encoding uses a larger local Hilbert space and can engineer noise bias/redundancy differently from bare two-level qubits.
- **distinguishability:** compare logical error/lifetime/resource overhead under matched logical task and physical error model.
- **preparation/control:** encoded cat/GKP state preparation plus gates/stabilization.
- **retention:** logical memory lifetime/error per cycle.
- **readout:** logical-state/syndrome measurement.
- **useful function:** lower physical-resource or error-correction overhead at matched logical reliability.
- **scaling resource:** photons/excitation, oscillator quality, ancillae, control bandwidth, loss, fabrication and decoding.
- **falsifier for UQPU route:** once full state-preparation/control/readout/QEC/factory cost is included, no useful-output resource/economic advantage remains against competitive alternatives.

This is established as an active physical research route, not proof of the UQPU moonshot.

## 4. Cross-lane consequences
- D receives a named device primitive with measurable logical-error/resource variables.
- G must map bosonic hardware requirements to fabrication/control/metrology rather than assuming lower qubit count means cheaper factory.
- A/C/QOS must charge state preparation and readout against useful output.
- E/F can compare materials/energy/cooling requirements only after platform requirements are explicit.
- H can fund bounded reproduction/modeling gates without promoting mission-level advantage.

## 5. Next tests
1. Pangola EMI coupon protocol + incumbent definition.
2. Bosonic-QEC resource ledger under one matched logical-memory/function target.
3. Feed both into lifecycle economics and capital gate.
