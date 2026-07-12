# Component Qualification Process

**Document ID:** DOC-CQP-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-001

## 1. Purpose

Define how components enter the approved BOM.

## 2. Rule

**No BOM without qualification.**

## 3. Process

```
Requirement → Candidate list → Datasheet review → Electrical analysis
    → Thermal analysis → Availability → Lifecycle → Qualification record → BOM
```

## 4. Qualification record location

`hardware/qualification/<category>/` — one record per qualified or provisional component.

Methodology: [docs/Component_Qualification/](Component_Qualification/README.md)

Template: [docs/Component_Qualification/Qualification_Report_Template.md](Component_Qualification/Qualification_Report_Template.md).

## 5. Provisional components

Allowed only when work package explicitly authorizes **provisional** status.

Provisional parts shall not be used for final vehicle sign-off without full qualification.

## 6. Analysis requirements

Distinguish continuous, pulsed, inrush, and limit current. Thermal evaluation mandatory for power semiconductors.

Do not infer ratings from part numbers or marketing.

## 7. Reference documentation

Conceptual BOM (not qualification substitute): `docs/007_Component_Selection.md` — status per that document.

## 8. Related documents

- [.cursor/rules/05_component_selection.mdc](../.cursor/rules/05_component_selection.mdc)
- [hardware/qualification/README.md](../hardware/qualification/README.md)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 foundation |
| 2.0 | 2026-07-12 | WP-002 link to Component_Qualification/ |
