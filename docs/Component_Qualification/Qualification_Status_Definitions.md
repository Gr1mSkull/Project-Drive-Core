# Qualification Status Definitions

**Document ID:** CQP-STAT-001  
**Version:** 1.1  
**Status:** Proposed  
**Work Package:** WP-002 · **Change Request:** CR-001

## 1. Purpose

Define allowed qualification statuses and transition rules for DriveCore components.

## 2. Scope

All records under `hardware/qualification/{category}/` and entries in [Qualification_Status.md](Qualification_Status.md).

## 3. Responsibilities

| Role | May set status |
|------|----------------|
| Implementation Engineer | **Candidate**, **Under Review**, **Lab Validation** (with evidence) |
| System Architect / authorized Reviewer | **Approved for Prototype**, **Approved for Production**, **Deprecated**, **Rejected** |

The Implementation Engineer **shall not** set **Approved for Prototype** or higher.

## 4. Status definitions

| Status | Definition |
|--------|------------|
| **Candidate** | MPN identified for evaluation; datasheet not yet fully reviewed |
| **Under Review** | Active datasheet and checklist analysis in progress |
| **Lab Validation** | Bench evaluation **in progress** or **partial evidence recorded**; see §5 |
| **Approved for Prototype** | Sufficient evidence for DevKit/prototype BOM; production use not authorized |
| **Approved for Production** | Full qualification complete including validation where required |
| **Deprecated** | Previously approved but superseded; retain record for traceability |
| **Rejected** | Failed qualification; shall not enter BOM |

## 5. Lab Validation — clarifications (CR-001)

**Lab Validation** means:

- Bench or prototype evaluation is **actively in progress**, **or**
- Test evidence (logs, measurements, reports) has been **attached** to the qualification record.

**Lab Validation does not:**

- Authorize BOM usage (prototype or production).
- Imply System Architect or Reviewer approval.
- Replace completion of [Qualification_Checklist.md](Qualification_Checklist.md) or engineering review.

**Roles during Lab Validation:**

| Role | Allowed action |
|------|----------------|
| Implementation Engineer | Run tests; attach **Prototype Validation References** and **Laboratory Test Report References** in the qualification report; maintain status at Lab Validation |
| System Architect / authorized Reviewer | Review evidence; advance to **Approved for Prototype** or higher; or set **Rejected** |

## 6. Transition diagram

```
Candidate → Under Review → Lab Validation → Approved for Prototype → Approved for Production
                ↓              ↓                    ↓
            Rejected       Rejected            Deprecated
```

## 7. BOM usage rules

| Status | BOM (prototype) | BOM (vehicle/production) |
|--------|-----------------|---------------------------|
| Candidate | No | No |
| Under Review | No | No |
| **Lab Validation** | **No** | **No** |
| Approved for Prototype | Yes, labeled | No |
| Approved for Production | Yes | Yes |
| Deprecated | No (use replacement) | No |
| Rejected | No | No |

## 8. Inputs / outputs

- **Input:** Qualification report, checklist, validation records
- **Output:** Status field in report header and program dashboard

## 9. Related documents

- [Qualification_Report_Template.md](Qualification_Report_Template.md) — Status and validation reference fields
- [COMPONENT_QUALIFICATION_PROCESS.md](../COMPONENT_QUALIFICATION_PROCESS.md) — overview

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
| 1.1 | 2026-07-12 | CR-001 Lab Validation clarifications and approval authority |
