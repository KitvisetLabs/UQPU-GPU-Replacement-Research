# Eight-Lane integration — 2026-10-26 — source-provenance preflight and helicon current-drive boundary

**Canonical starting main SHA:** 5879e658587a5d45bf8f85bda8077340e04b4bd3  
**Primary integration owner:** Lane F  
**Lane A implementation owner:** equation-discovery and reproducible benchmark tooling  
**Lane E technical owner:** fusion, cooling and infrastructure  
**Lane H publication owner:** strategic research and literature surveillance  
**Evidence class:** SOFTWARE CONTRACT + UNIT TESTS PENDING CI + PEER-REVIEWED EXTERNAL LITERATURE ONLY

## Integrated changes

1. Added a source-provenance bundle contract that links an explicit source/revision/license/acquisition record and raw-file digests to the canonical split manifest's dataset hash and row count.
2. The preflight composes provenance validation with raw-record-bound split verification. It rejects changed records, mismatched dataset hashes, malformed provenance digests, mutable branch aliases, missing license identifiers, non-HTTPS source URLs and unsafe/duplicate raw-file paths.
3. Published a dated watch for the peer-reviewed DIII-D helicon current-drive result (PRL 137, 155101, 2026-10-09). Its exact use is to expand the FUS-001 candidate architecture/evidence map, not to claim net-electricity advantage.
4. Retained source-to-record authenticity, license review, representative sampling, independent audit and a matched >=30-seed equation-discovery run as OPEN gates. The code's PASS means internal contract consistency only.

## Cross-lane interface

- **A:** raw-record and source-provenance preflight; still requires a pinned dataset and actual matched comparison.
- **B:** no provider execution or pricing mix.
- **C:** row count, record hashes and provenance metadata are not physical RAM/VRAM/HBM or readable quantum-state capacity.
- **D/G:** helicon antenna, RF source, diagnostic, metrology, maintainability and manufacturing interfaces are candidate cost drivers; no fabrication/yield result.
- **E:** plasma-control evidence is kept distinct from net fusion electricity; biomass carbon and bio-oil evidence remain separate.
- **F:** provenance hashes, row counts, matched resource budgets and complete power boundaries are integration requirements.
- **H:** external literature is source-bounded and the strategic model remains preserved.

## Fusion accounting contract

For any future architecture comparison, report wall-plug electrical input separately from RF power delivered to the plasma, coupling losses and the measured current-drive/plasma response. The plant net-electric ledger must subtract recirculating loads and balance-of-plant loads once, including current drive, cooling, pumps, cryogenics where applicable, fuel-cycle systems and grid interfaces. The DIII-D paper does not provide enough plant data to evaluate that ledger.

## Evidence and non-claims

No real-QPU job was submitted. No QPU speedup, accepted-task cost advantage, physical memory replacement, new physical law, qualified biomass material, accepted bio-oil, net fusion electricity, lower financing principal/interest, lower WACC, or Data-Center-to-One-Phone compression is demonstrated by this integration.

## Open gates

- **RG-046:** pin and independently audit a public benchmark source, then run the matched equation-discovery comparison.
- **FUS-001:** acquire detailed helicon source data and quantify wall-plug versus plasma-coupled power, uncertainty, control-matched response and plant-level propagation.
- **FND-003:** still lacks a matched control-versus-quantum-speed-limit experiment.
- **INV-029:** remains a mission with physical-boundary and end-to-end service/cost requirements, not a completed device.

## CI and synchronization

The starting exact-head Actions run had all three Python matrix tests and the reference benchmark passing; Qiskit verification and one bounded-prefix job were still running, while the cold-start handoff audit passed. This commit's exact-head Actions result must be checked after publication. The combined-status endpoint exposed no legacy status rows.

Large append-heavy RESEARCH_GAPS.md and WORKLOG.md were not rewritten. The RG-046 standalone gap is the detailed canonical blocker; aggregate reconciliation remains explicit sync debt.
