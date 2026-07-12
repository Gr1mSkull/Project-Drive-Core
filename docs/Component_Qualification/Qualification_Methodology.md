# Qualification Methodology

**Document ID:** CQP-METH-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define the standardized methodology by which every DriveCore electronic component is evaluated before inclusion in an approved BOM.

## 2. Scope

**In scope:** All electronic and electromechanical components in DCC, ECU, Button Box, and expansion modules.

**Out of scope:** Performing qualification (separate work packages); selecting or recommending specific MPNs (System Architect / authorized WP).

## 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Implementation Engineer | Execute qualification tasks; complete reports and evidence |
| System Architect | Approve qualification for prototype/production |
| Reviewer | Verify evidence integrity; reject invented data |

## 4. Inputs

- Approved requirement or channel class (SRS, `docs/002`, work package)
- Manufacturer datasheet (primary source)
- [Qualification_Checklist.md](Qualification_Checklist.md)
- Category README in `hardware/qualification/<category>/`

## 5. Outputs

- Completed [Qualification_Report_Template.md](Qualification_Report_Template.md) per MPN
- Updated [Qualification_Status.md](Qualification_Status.md)
- Engineering decision matrix (when comparison authorized)

## 6. Methodology principles

1. **Evidence-based** — no rating without datasheet citation.
2. **Condition-bound** — continuous current stated with voltage, temperature, PCB, duty.
3. **Lifecycle-aware** — NRND/EOL requires documented risk acceptance.
4. **Traceable** — report links to requirement ID and work package.
5. **Separable analysis** — electrical, thermal, manufacturing, supply chain evaluated independently.

## 7. Analysis domains

| Domain | Policy document |
|--------|-----------------|
| Electrical | [Qualification_Checklist.md](Qualification_Checklist.md) § electrical |
| Thermal | [Thermal_Validation.md](Thermal_Validation.md) |
| Lifecycle | [Component_Lifecycle_Policy.md](Component_Lifecycle_Policy.md) |
| Supply chain | [Supplier_Policy.md](Supplier_Policy.md), [Availability_Policy.md](Availability_Policy.md) |
| Alternates | [Second_Source_Policy.md](Second_Source_Policy.md) |
| Risk | [Risk_Assessment.md](Risk_Assessment.md) |

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Methodology documents exist and cross-reference without contradiction |
| AC-2 | Workflow and status definitions are usable without component data |
| AC-3 | No MPN selected or rated in methodology documents |

## 9. Related documents

- [Qualification_Workflow.md](Qualification_Workflow.md)
- [docs/COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
