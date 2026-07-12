# Component Qualification — Documentation Index

**Work Package:** WP-002  
**Version:** 1.0  
**Status:** Proposed

## Purpose

Central index for DriveCore component qualification methodology, policies, templates, and status definitions.

## Document map

| Document | Authority |
|----------|-----------|
| [COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md) | **Overview** — navigation only |
| [Qualification_Methodology.md](Qualification_Methodology.md) | **Normative** — execution methodology |
| [Qualification_Workflow.md](Qualification_Workflow.md) | Process stages |
| [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md) | Status enum and transitions |
| [Qualification_Checklist.md](Qualification_Checklist.md) | Per-component review checklist |
| [Component_Lifecycle_Policy.md](Component_Lifecycle_Policy.md) | Active, NRND, EOL |
| [Supplier_Policy.md](Supplier_Policy.md) | Supplier and distributor rules |
| [Availability_Policy.md](Availability_Policy.md) | Stock and lead-time |
| [Second_Source_Policy.md](Second_Source_Policy.md) | Alternate MPN strategy |
| [Risk_Assessment.md](Risk_Assessment.md) | Qualification risk framework |
| [Thermal_Validation.md](Thermal_Validation.md) | Thermal evidence requirements |
| [Qualification_Status.md](Qualification_Status.md) | Program-level status dashboard |
| [Qualification_Report_Template.md](Qualification_Report_Template.md) | Per-component report |
| [Engineering_Decision_Matrix_Template.md](Engineering_Decision_Matrix_Template.md) | Scored comparison (when authorized) |

## Hardware records

Category folders: [hardware/qualification/](../../hardware/qualification/README.md)

Report path template:

```
hardware/qualification/{category}/{manufacturer}_{mpn}_qualification.md
```

## Related

- [docs/COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md)
- [.cursor/rules/05_component_selection.mdc](../../.cursor/rules/05_component_selection.mdc)
- [docs/007_Component_Selection.md](../007_Component_Selection.md) — conceptual only, not qualified BOM

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 framework |
| 1.1 | 2026-07-12 | CR-001 document authority and path template |
