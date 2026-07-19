# Review Handoff Package Template

**Document ID:** TPL-RHP-001  
**Version:** 1.1.1  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1 · **ADR:** ADR-CR002-001

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §18.

When interfaces or identity-bearing artifacts change, versions shall follow [`docs/standards/REVISION_IDENTITY_STANDARD.md`](../standards/REVISION_IDENTITY_STANDARD.md) (ADR-CR002-001).

**Storage convention (filled records only):**

```text
docs/records/review_handoffs/RHP-YYYY-NNN_<short-title>.md
```

Templates remain in `docs/templates/`.

The implementer shall not classify self-review as independent Engineering or Critical Review.

---

## Review Handoff Package

| Field | Value |
|-------|-------|
| **Review Package ID** | RHP-YYYY-NNN |
| **Change Scope** | |
| **Related Requirements** | |
| **Related Architecture** | |
| **Related WP / CR** | |
| **Impact Level** | 1 \| 2 (Level 0 does not require RHP) |
| **Date** | YYYY-MM-DD |
| **Implementer (name/agent)** | |
| **Implementer role** | Implementation Engineer |

### Changed Files

|

### Changed Interfaces

| Interface | From version | To version | CIA / Impact note |
|-----------|--------------|------------|-------------------|
| | | | |

### Changed Assumptions

|

### Change Impact Analysis

| Field | Value |
|-------|-------|
| **Impact classification** | Level 1 note \| Level 2 CIA-YYYY-NNN |
| **CIA / note path** | `docs/records/change_impact/...` or WP section |
| **ADR Required** | YES / NO / TBD |

### Validation Summary

|

### Evidence References

| Evidence ID | Raw result | Path | Certified? |
|-------------|------------|------|------------|
| | | `docs/records/verification/...` | YES / NO / TBD |

### Known Weaknesses

|

### Known Risks

|

### Open Questions

|

### Critical Review Focus Areas

Areas requiring adversarial review (do not confirm success — search for weaknesses):

-

### Rollback Considerations

|

### Review status

| Field | Value |
|-------|-------|
| **Implementer Self-Review Status** | Complete \| Incomplete |
| **Independent Review Status** | Not started \| In progress \| Complete |
| **Independent Reviewer (name/agent)** | (must differ from implementer) |
| **Independent Reviewer role** | Independent Reviewer \| Test Owner |
| **Independent review date** | YYYY-MM-DD or TBD |
| **Final Review Outcome** | Accepted \| Revision required \| Blocked |
| **Architecture / policy approval** | Separate — System Architect only; N/A unless required |

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 initial template |
| 1.1 | 2026-07-19 | CR-002-R1 records path; role/date fields |
| 1.1.1 | 2026-07-19 | ADR-CR002-001 — reference revision-identity standard |
