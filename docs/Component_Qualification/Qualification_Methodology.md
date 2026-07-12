# Qualification Methodology

**Document ID:** CQP-METH-001  
**Version:** 1.1  
**Status:** Proposed · **Normative**  
**Work Package:** WP-002 · **Change Request:** CR-001

## 0. Document authority

This document is the **authoritative source** for DriveCore component qualification **execution**: evidence requirements, analysis domains, roles, and outputs.

| Document | Role |
|----------|------|
| [COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md) | Short overview and navigation only — not normative for procedure detail |
| **This document** | Normative methodology |
| Other `Component_Qualification/*.md` | Policies, checklists, templates referenced herein |

## 1. Purpose

Define the standardized methodology by which every DriveCore electronic component is evaluated before inclusion in an approved BOM.

## 2. Scope

**In scope:** All electronic and electromechanical components in DCC, ECU, Button Box, and expansion modules.

**Out of scope:** Performing qualification (separate work packages); selecting or recommending specific MPNs (System Architect / authorized WP).

## 3. Responsibilities

| Role | Responsibility |
|------|----------------|
| Implementation Engineer | Execute qualification tasks; complete reports; record lab evidence; set status up to **Lab Validation** only |
| System Architect / authorized Reviewer | Grant **Approved for Prototype**, **Approved for Production**, **Deprecated**, **Rejected** |
| Reviewer | Verify evidence integrity; reject invented data |

## 4. Inputs

- Approved requirement or channel class (SRS, `docs/002`, work package)
- Manufacturer datasheet (primary source)
- [Qualification_Checklist.md](Qualification_Checklist.md)
- Category README in `hardware/qualification/{category}/`

## 5. Outputs

- Completed [Qualification_Report_Template.md](Qualification_Report_Template.md) per MPN
- Updated [Qualification_Status.md](Qualification_Status.md)
- Engineering decision matrix (when comparison authorized)

Report path:

```
hardware/qualification/{category}/{manufacturer}_{mpn}_qualification.md
```

## 6. Methodology principles

1. **Evidence-based** — no rating without datasheet citation.
2. **Condition-bound** — continuous current stated with voltage, temperature, PCB, duty.
3. **Lifecycle-aware** — NRND/EOL requires documented risk acceptance.
4. **Traceable** — report links to requirement ID and work package.
5. **Separable analysis** — electrical, thermal, manufacturing, supply chain evaluated independently.
6. **Evidence typing** — every value marked as datasheet fact, calculated, measured, assumption, or TBD (see report template).

## 7. Analysis domains

| Domain | Policy document |
|--------|-----------------|
| Electrical | [Qualification_Checklist.md](Qualification_Checklist.md) § electrical |
| Thermal | [Thermal_Validation.md](Thermal_Validation.md) |
| Lifecycle | [Component_Lifecycle_Policy.md](Component_Lifecycle_Policy.md) |
| Supply chain | [Supplier_Policy.md](Supplier_Policy.md), [Availability_Policy.md](Availability_Policy.md) |
| Alternates | [Second_Source_Policy.md](Second_Source_Policy.md) |
| Risk | [Risk_Assessment.md](Risk_Assessment.md) |

## 8. Workflow reference

Normative stage sequence: [Qualification_Workflow.md](Qualification_Workflow.md).

## 9. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Methodology documents exist and cross-reference without contradiction |
| AC-2 | Workflow and status definitions are usable without component data |
| AC-3 | No MPN selected or rated in methodology documents |

## 10. Related documents

- [Qualification_Workflow.md](Qualification_Workflow.md)
- [COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md) — overview only

## 11. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
| 1.1 | 2026-07-12 | CR-001 normative authority; brace paths; Lab Validation role boundary |
