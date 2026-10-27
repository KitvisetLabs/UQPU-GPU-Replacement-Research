# Literature watch — SPARC human-agent experimental design with persistent failure memory

**Watch date:** 2026-10-28  
**Primary source:** Yu Liu, Boris Slautin, Ching-Che Lin, Jaegyu Kim, Lane W. Martin and Sergei V. Kalinin, “Human-agent discovery of reconfigurable in-plane ferroelectric superdomain control,” arXiv:2609.06887v1, submitted 2026-09-07.  
**Official record:** https://arxiv.org/abs/2609.06887  
**Evidence class:** external experimental preprint; **not reproduced by UQPU**.

## Genuine contribution

The paper introduces the Scanning Probe Agentic Research Cycle (SPARC), a human-agent workflow in which a coding agent and a human operator share a microscope, notebook and two persistent records: `FINDINGS.md` for graded conclusions and `PITFALLS.md` for analysis/instrument failure modes. In the reported study, a human-supervised analysis phase informed a later agent-controlled experiment campaign. The authors report reconfiguring superdomain direction in a particular (111)-oriented lead zirconate titanate film and identify spatial polarity alternation as the decisive directional-selection feature under their tested conditions. They also describe compiling known pitfalls into checks before a write operation.

The useful methodological point is instrument-grounded memory and pre-action validation, not a claim that a general-purpose autonomous scientist has been solved.

## Limitations and evidence boundary

- The source is an arXiv preprint; UQPU has not reproduced its material, microscope protocol or reported patterning result.
- The experiment concerns one specified ferroelectric film and scanning-probe setup. Its findings do not automatically transfer to Pangola-derived carbon, semiconductor processing, quantum devices, biomass conversion, fusion materials or other instruments.
- Agentic control remains bounded by instrument calibration, action limits, physical execution verification, operator supervision and the validity domain of stored findings.
- A persistent `PITFALLS.md` record is useful only if its checks are validated against new instrument data and do not silently block legitimate actions.

## Exact UQPU relevance

- **Lane A / INV-035:** the workflow suggests a reusable pattern for recording hypothesis provenance, failed attempts, pre-action checks and evidence grades. It does not validate a physical equation.
- **Lane D:** a possible future method for semiconductor/device/material process experiments, but only with instrument-specific action constraints and physical-write verification.
- **Lane E / INV-030–032:** it may inform how future Pangola-carbon or energy-material experiments record controls and failed runs. It provides no evidence of material substitution, fuel yield or fusion performance.
- **Lane F:** compare total operator/agent time, instrument use, failed writes, sample consumption, calibration overhead and reproducibility only after the same task and acceptance criteria are fixed.
- **Lane H:** its persistent findings/pitfalls separation is compatible with the project's cold-start continuity principle; strategic continuity remains separate from empirical proof.

## Falsifiable follow-up

1. Convert the idea into a generic experiment-protocol schema: observable, allowed actions, instrument state/calibration, pre-action checks, controls, abort conditions, provenance, failed attempts and replication status.
2. Test the schema first on a non-destructive simulator or archived data. Include positive, negative and adversarial controls.
3. If a suitable laboratory later becomes available, use a blinded protocol and verify that every commanded write corresponds to an independently recorded physical action.
4. Check whether the stored pitfalls reduce invalid actions without suppressing valid discoveries; report false blocks and missed failures.
5. For any material claim, require composition/structure/function tests and lifecycle economics independently of the agent workflow.

**Decision:** retain SPARC as an external experimental-design method watch. No UQPU lab result, Pangola substitution, new constitutive law, device improvement or economic advantage is claimed.
