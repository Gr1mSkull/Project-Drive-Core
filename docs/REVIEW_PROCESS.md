# Review Process

**Document ID:** DOC-REV-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-001

## 1. Purpose

Ensure every change is reviewed before acceptance.

## 2. Rule

**Every change requires review.**

## 3. Review types

| Type | When | Template |
|------|------|----------|
| Code / doc change | Every PR or work package completion | Completion report in WP |
| Architecture | ADR-level impact | `docs/templates/Architecture_Review_Template.md` |
| Component | BOM or qualification change | `docs/templates/Qualification_Report_Template.md` |

## 4. Review checklist

| Area | Criterion |
|------|-----------|
| Requirements | Scope matches work package |
| Architecture | No unauthorized ADR-level changes |
| Tests | Validation reported accurately |
| Documentation | Affected docs updated |
| Risks | Open questions documented |

## 5. Roles

| Role | Authority |
|------|-----------|
| Implementation Engineer | Execute and report |
| System Architect | Approve architecture and ADRs |
| Reviewer | Accept or reject deliverable |

## 6. Outcomes

- **Accepted** — merge / proceed
- **Revision required** — fix and resubmit
- **Blocked** — architectural decision needed

## 7. Related documents

- [.cursor/ENGINEERING_CONSTITUTION.mdc](../.cursor/ENGINEERING_CONSTITUTION.mdc) — §18 Review Process
- [ENGINEERING_WORKFLOW.md](ENGINEERING_WORKFLOW.md)

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 foundation |
