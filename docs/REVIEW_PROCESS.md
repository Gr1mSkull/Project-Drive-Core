# Review Process

**Document ID:** DOC-REV-001  
**Version:** 1.1  
**Status:** Proposed  
**Work Package:** WP-001 · **Change Request:** CR-002

## 1. Purpose

Ensure every change is reviewed before acceptance.

**Authoritative policy:** [.cursor/ENGINEERING_CONSTITUTION.mdc](../.cursor/ENGINEERING_CONSTITUTION.mdc) §18 — this document is a navigation aid and shall not redefine policy.

## 2. Rule

**Every change requires review.**

## 3. Review sequence

| Stage | Who |
|-------|-----|
| Implementation Review | Implementer (self-check only) |
| Engineering Review | Independent reviewer — not the implementer |
| Critical Review | Independent reviewer — adversarial; not the implementer |

High-impact changes require a Review Handoff Package: `docs/templates/Review_Handoff_Package_Template.md`.

## 4. Review types

| Type | When | Template |
|------|------|----------|
| Code / doc change | Every PR or work package completion | Completion report in WP |
| High-impact change | Safety, protocols, shared formats, power, OTA, etc. | Review Handoff Package |
| Architecture | ADR-level impact | `docs/templates/Architecture_Review_Template.md` |
| Component | BOM or qualification change | `docs/templates/Qualification_Report_Template.md` |

## 5. Review checklist

See constitution §18. Summary: scope, architecture, evidence-backed tests, traceability, documentation, status authority, risks.

## 6. Roles

| Role | Authority |
|------|-----------|
| Implementation Engineer | Execute, Implementation Review, report |
| System Architect | Approve architecture, ADRs, and engineering-policy status |
| Reviewer | Independent Engineering / Critical Review; accept or reject |

Review completion and repository merge do **not** automatically approve documents.

## 7. Outcomes

- **Accepted** — merge / proceed
- **Revision required** — fix and resubmit
- **Blocked** — architectural decision needed

## 8. Related documents

- [.cursor/ENGINEERING_CONSTITUTION.mdc](../.cursor/ENGINEERING_CONSTITUTION.mdc) — §18 Review Process
- [ENGINEERING_WORKFLOW.md](ENGINEERING_WORKFLOW.md)
- [templates/Review_Handoff_Package_Template.md](templates/Review_Handoff_Package_Template.md)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 foundation |
| 1.1 | 2026-07-19 | CR-002 — independent review and handoff package |
