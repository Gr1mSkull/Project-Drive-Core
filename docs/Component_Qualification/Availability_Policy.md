# Availability Policy

**Document ID:** CQP-AVL-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define how stock availability and lead time are evaluated during qualification.

## 2. Scope

All BOM components. Evaluation occurs at qualification time; market conditions change — re-check before production builds.

## 3. Responsibilities

Implementation Engineer records availability snapshot with date; Architect assesses program risk.

## 4. Inputs

- Distributor or manufacturer lead-time data (dated)
- Production volume assumptions (from work package or SRS — TBD)

## 5. Outputs

- **Availability** field in qualification report
- Risk flag when lead time or MOQ threatens program

## 6. Evaluation parameters

| Parameter | Shall record |
|-----------|--------------|
| Stock status | In stock / limited / allocation / obsolete |
| Lead time | Weeks; date of quote |
| MOQ | Minimum order quantity |
| Geographic risk | Single-region dependency (TBD criteria) |

## 7. Thresholds

Specific numeric thresholds (weeks, MOQ) — **TBD** by program management. Until defined, report factual data without pass/fail.

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Parameters to record are defined |
| AC-2 | No fabricated availability data |

## 9. Related documents

- [Component_Lifecycle_Policy.md](Component_Lifecycle_Policy.md)
- [Second_Source_Policy.md](Second_Source_Policy.md)

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
