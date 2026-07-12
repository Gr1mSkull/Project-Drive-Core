# Qualification Program Status

**Document ID:** CQP-PRG-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Provide a program-level view of component qualification progress across DriveCore.

## 2. Scope

All categories under `hardware/qualification/`. Updated when individual reports change status.

## 3. Responsibilities

Implementation Engineer updates counts after qualification WPs; Architect reviews before milestone gates.

## 4. Inputs

- Individual qualification reports
- [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md)

## 5. Outputs

- Summary tables below (manual update until tooling exists)

## 6. Program summary

| Metric | Count |
|--------|-------|
| Total reports | 0 |
| Candidate | 0 |
| Under Review | 0 |
| Lab Validation | 0 |
| Approved for Prototype | 0 |
| Approved for Production | 0 |
| Deprecated | 0 |
| Rejected | 0 |

## 7. Status by category

| Category | Candidate | Under Review | Lab | Proto OK | Production OK | Rejected |
|----------|-----------|--------------|-----|----------|---------------|----------|
| high_side | 0 | 0 | 0 | 0 | 0 | 0 |
| low_side | 0 | 0 | 0 | 0 | 0 | 0 |
| power_supply | 0 | 0 | 0 | 0 | 0 | 0 |
| current_sense | 0 | 0 | 0 | 0 | 0 | 0 |
| protection | 0 | 0 | 0 | 0 | 0 | 0 |
| can | 0 | 0 | 0 | 0 | 0 | 0 |
| wireless | 0 | 0 | 0 | 0 | 0 | 0 |
| mcu | 0 | 0 | 0 | 0 | 0 | 0 |
| memory | 0 | 0 | 0 | 0 | 0 | 0 |
| connectors | 0 | 0 | 0 | 0 | 0 | 0 |
| passives | 0 | 0 | 0 | 0 | 0 | 0 |
| oscillators | 0 | 0 | 0 | 0 | 0 | 0 |
| sensors | 0 | 0 | 0 | 0 | 0 | 0 |
| power_distribution | 0 | 0 | 0 | 0 | 0 | 0 |
| mechanical | 0 | 0 | 0 | 0 | 0 | 0 |

## 8. Milestone gates

| Milestone | Minimum qualification |
|-----------|----------------------|
| DevKit build | Key paths **Approved for Prototype** per architect list (TBD) |
| DCC Gen1 vehicle | Per EDL-014 and architect list (TBD) |
| Production | **Approved for Production** for all BOM lines |

## 9. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Dashboard structure covers all WP-002 categories |
| AC-2 | Zero fabricated component entries |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
