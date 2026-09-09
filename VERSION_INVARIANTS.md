# Version Invariants

Every UQPU release must preserve the following project-level guarantees in its documentation and architecture.

| ID | Invariant | Required in every version |
|---|---|---|
| INV-001 | Provider-agnostic UQPU core | Yes |
| INV-002 | Extensible quantum-cloud adapters | Yes |
| INV-003 | Full GPU functional-domain research scope | Yes |
| INV-004 | End-to-end cost accounting | Yes |
| INV-005 | >=100× cost/task research target | Yes |
| INV-006 | Up to 100,000,000× workload-specific moonshot | Yes |
| INV-007 | No unsupported quantum-advantage claims | Yes |
| INV-008 | Develop-test-inspect-improve loop | Yes |
| INV-009 | External-user usability and documentation | Yes |
| INV-010 | Continuous provider-market surveillance | Yes |
| INV-011 | VRAM/HBM and host-memory/data-movement replacement scope | Yes |
| INV-012 | CPU/storage/network/full-system research scope | Yes |
| INV-013 | Hardware/photonics/device-physics research scope | Yes |
| INV-014 | Biomass/agricultural-residue advanced-materials strategy | Yes |

## Release rule

A version should not be considered compliant if it removes or weakens these invariants without an explicit research decision documenting why.

## CI enforcement

The repository includes an automated policy test that checks for the presence of these permanent mission markers in core project documentation.

| INV-015 | Complete chip-fabrication equipment/process research scope | Yes |
| INV-016 | Parallel fab workstreams with cross-system integration | Yes |
