# Change Impact Analysis Template

**Document ID:** TPL-CIA-001  
**Version:** 1.1  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6 (Change impact analysis — proportional).

**Use this template only for Impact Level 2 — Full CIA.**

| Level | Artifact |
|-------|----------|
| 0 | Completion report statement only |
| 1 | Lightweight Impact Note in WP or Completion Report |
| 2 | **This template** → filled record in `docs/records/change_impact/` |

**Storage convention (filled records only):**

```text
docs/records/change_impact/CIA-YYYY-NNN_<short-title>.md
```

Templates remain in `docs/templates/`. Do not invent missing impacts — use `TBD` / `OPEN ISSUE` / escalate.

---

## Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-YYYY-NNN |
| **Impact Level** | 2 — Full CIA |
| **Title** | |
| **Author** | |
| **Author role** | Implementation Engineer |
| **Date** | YYYY-MM-DD |
| **Status** | Draft \| Under Review \| Accepted \| Rejected |
| **Related WP / CR** | |

### Reason for Change

|

### Current Behaviour

|

### Proposed Behaviour

|

### Affected Requirements

| Requirement ID | Source | Impact |
|----------------|--------|--------|
| | | |

### Affected Modules

|

### Affected Interfaces

| Interface | Current version | Proposed version | Breaking? |
|-----------|-----------------|------------------|-----------|
| | | | YES / NO / TBD |

### Affected Files

|

### Affected Tests

|

### Affected Documentation

|

### Compatibility Assessment

| Aspect | Assessment |
|--------|------------|
| Backward compatibility | Compatible \| Breaking \| TBD |
| Forward compatibility | Compatible \| Breaking \| TBD |
| Silent field reinterpretation risk | None \| Present — **prohibited** |

### Migration Requirements

|

### Rollback Method

|

### Safety Impact

| Area | Impact |
|------|--------|
| Safe states | None \| Changed \| TBD |
| Kill / isolation | None \| Changed \| TBD |
| Fail-operational behaviour | None \| Changed \| TBD |

### Validation Required

|

### Open Questions

|

### Approvals (architecture / policy)

| Field | Value |
|-------|-------|
| **ADR Required** | YES / NO / TBD |
| **Architect Approval Required** | YES / NO / TBD |
| **ADR / EDL reference** | |
| **Architect approver (name/agent)** | |
| **Architect role** | System Architect |
| **Architect approval date** | YYYY-MM-DD or TBD |

### Review acknowledgment (not architecture approval)

| Field | Value |
|-------|-------|
| **Reviewer (name/agent)** | |
| **Reviewer role** | Independent Reviewer |
| **Review date** | YYYY-MM-DD or TBD |
| **Evidence / CIA review note** | |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 initial template |
| 1.1 | 2026-07-19 | CR-002-R1 Level 2 scope; records path; approval fields |
