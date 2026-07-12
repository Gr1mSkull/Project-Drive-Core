# Component Lifecycle Policy

**Document ID:** CQP-LC-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define how component lifecycle status affects qualification and BOM eligibility.

## 2. Scope

All semiconductors, passives, connectors, and modules in DriveCore designs.

## 3. Responsibilities

Implementation Engineer records lifecycle from manufacturer sources; System Architect accepts risk for non-active parts.

## 4. Inputs

- Manufacturer PCN, product status page, distributor lifecycle field
- [Qualification_Report_Template.md](Qualification_Report_Template.md)

## 5. Outputs

- Lifecycle field in qualification report
- Risk entry when lifecycle is not **Active**

## 6. Lifecycle categories

| Category | Definition | Default BOM policy |
|----------|------------|-------------------|
| **Active** | In production, orderable | Eligible after full qualification |
| **NRND** | Not recommended for new designs | Requires risk acceptance + migration plan |
| **EOL** | End of life announced | Not for new baseline; replacement required |
| **Unknown** | Not verified | TBD — not approved |

## 7. Automotive qualification (AEC)

AEC-Q100 / Q101 / Q200 status shall be recorded where applicable. Absence of automotive grade shall be documented as risk for vehicle deployment.

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Lifecycle categories defined |
| AC-2 | NRND/EOL require documented exception path |

## 9. Related documents

- [Availability_Policy.md](Availability_Policy.md)
- [.cursor/rules/05_component_selection.mdc](../../.cursor/rules/05_component_selection.mdc)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
