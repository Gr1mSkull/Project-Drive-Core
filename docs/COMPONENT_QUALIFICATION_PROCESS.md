# Component Qualification Process

**Document ID:** DOC-CQP-001  
**Version:** 1.1  
**Status:** Proposed  
**Work Package:** WP-001 · **Change Request:** CR-001

## 1. Purpose

Provide a **short overview and navigation entry point** for how components enter the approved BOM.

This document does **not** contain detailed procedural requirements.

## 2. Document authority

| Document | Role |
|----------|------|
| **This document** (`COMPONENT_QUALIFICATION_PROCESS.md`) | Overview, rule statement, navigation, record location |
| **[Qualification_Methodology.md](Component_Qualification/Qualification_Methodology.md)** | **Normative** detailed methodology for qualification execution |
| `docs/Component_Qualification/*` | Supporting policies, checklists, templates, status definitions |

When this overview and the methodology differ, **Qualification_Methodology.md** is authoritative for execution steps and evidence requirements.

## 3. Rule

**No BOM without qualification.**

## 4. Process (summary)

```
Requirement → Candidate → Datasheet review → Electrical / thermal / manufacturing / supply chain evaluation
    → Engineering review → Prototype validation (when required) → Approval
```

Detailed stages: [Qualification_Workflow.md](Component_Qualification/Qualification_Workflow.md) (normative).

## 5. Qualification record location

```
hardware/qualification/{category}/{manufacturer}_{mpn}_qualification.md
```

Category folders: [hardware/qualification/README.md](../hardware/qualification/README.md).

## 6. Where to go next

| Need | Document |
|------|----------|
| Execute qualification | [Qualification_Methodology.md](Component_Qualification/Qualification_Methodology.md) |
| Fill report | [Qualification_Report_Template.md](Component_Qualification/Qualification_Report_Template.md) |
| Status rules | [Qualification_Status_Definitions.md](Component_Qualification/Qualification_Status_Definitions.md) |
| Checklist | [Qualification_Checklist.md](Component_Qualification/Qualification_Checklist.md) |

## 7. Provisional status

**Lab Validation** and other pre-approval statuses do **not** authorize BOM use. See [Qualification_Status_Definitions.md](Component_Qualification/Qualification_Status_Definitions.md).

## 8. Reference (not qualification)

Conceptual BOM: [007_Component_Selection.md](007_Component_Selection.md) — does not substitute qualification records.

## 9. Related documents

- [.cursor/rules/05_component_selection.mdc](../.cursor/rules/05_component_selection.mdc)
- [hardware/qualification/README.md](../hardware/qualification/README.md)
- [Component_Qualification/README.md](Component_Qualification/README.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 foundation |
| 2.0 | 2026-07-12 | WP-002 link to Component_Qualification/ |
| 1.1 | 2026-07-12 | CR-001 document authority; brace path template; de-duplicate normative detail |
