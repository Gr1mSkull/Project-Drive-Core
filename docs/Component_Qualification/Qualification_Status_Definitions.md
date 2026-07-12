# Qualification Status Definitions

**Document ID:** CQP-STAT-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define allowed qualification statuses and transition rules for DriveCore components.

## 2. Scope

All records in `hardware/qualification/` and entries in [Qualification_Status.md](Qualification_Status.md).

## 3. Responsibilities

| Role | May set status |
|------|----------------|
| Implementation Engineer | Candidate, Under Review, Lab Validation (with evidence) |
| System Architect / Reviewer | Approved for Prototype, Approved for Production, Deprecated, Rejected |

## 4. Status definitions

| Status | Definition |
|--------|------------|
| **Candidate** | MPN identified for evaluation; datasheet not yet fully reviewed |
| **Under Review** | Active datasheet and checklist analysis in progress |
| **Lab Validation** | Prototype or bench testing in progress; electrical/thermal evidence partial |
| **Approved for Prototype** | Sufficient evidence for DevKit/prototype BOM; production use not authorized |
| **Approved for Production** | Full qualification complete including validation where required |
| **Deprecated** | Previously approved but superseded; retain record for traceability |
| **Rejected** | Failed qualification; shall not enter BOM |

## 5. Transition diagram

```
Candidate → Under Review → Lab Validation → Approved for Prototype → Approved for Production
                ↓              ↓                    ↓
            Rejected       Rejected            Deprecated
```

## 6. BOM usage rules

| Status | BOM (prototype) | BOM (vehicle/production) |
|--------|-----------------|---------------------------|
| Candidate | No | No |
| Under Review | No | No |
| Lab Validation | No | No |
| Approved for Prototype | Yes, labeled | No |
| Approved for Production | Yes | Yes |
| Deprecated | No (use replacement) | No |
| Rejected | No | No |

## 7. Inputs / outputs

- **Input:** Qualification report, checklist, validation records
- **Output:** Status field in report header and program dashboard

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | All WP-002 statuses defined |
| AC-2 | BOM rules explicit per status |

## 9. Related documents

- [Qualification_Report_Template.md](Qualification_Report_Template.md) — Status field
- [docs/COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
