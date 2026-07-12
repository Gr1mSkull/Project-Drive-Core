# Risk Assessment

**Document ID:** CQP-RISK-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Provide a consistent framework for identifying and recording risks during component qualification.

## 2. Scope

Per-component risks in qualification reports; program-level risks in [Qualification_Status.md](Qualification_Status.md).

## 3. Responsibilities

Implementation Engineer identifies risks with evidence; Reviewer accepts or escalates.

## 4. Inputs

- Qualification checklist results
- Lifecycle, availability, thermal, electrical gaps

## 5. Outputs

- **Supply Chain Risk** and **Engineering Notes** in report
- Risk register entry when severity is high (format TBD)

## 6. Risk categories

| Category | Examples |
|----------|----------|
| Technical | Margin insufficient, thermal TBD, diagnostic gap |
| Lifecycle | NRND, EOL, unknown status |
| Supply chain | Single source, long lead, allocation |
| Manufacturing | Non-standard package, rework difficulty |
| Safety | Misapplication in load profile |
| Compliance | Missing AEC for vehicle path |

## 7. Severity (qualitative)

| Level | Action |
|-------|--------|
| Low | Document; proceed if qualified |
| Medium | Architect awareness required |
| High | Block **Approved for Production** until mitigated |
| Critical | Reject or change requirement |

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Risk categories cover technical and supply chain |
| AC-2 | Severity levels tied to status gates |

## 9. Related documents

- [Qualification_Checklist.md](Qualification_Checklist.md)
- [Engineering_Decision_Matrix_Template.md](Engineering_Decision_Matrix_Template.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
