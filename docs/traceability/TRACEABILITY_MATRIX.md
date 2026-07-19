# DriveCore Traceability Matrix

**Document ID:** DOC-TRACE-MAT-001  
**Version:** 1.0  
**Status:** Proposed  
**Change Request:** CR-002

Controlled **scaffold**. Do not invent historical links. Empty cells use `TBD` / `OPEN ISSUE` / `NOT VERIFIED`.

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6.

## Matrix

| Requirement ID | Requirement Source | Architecture / Interface Reference | Implementation Artifact | Verification Method | Evidence Reference | Status | Notes |
| -------------- | ------------------ | ---------------------------------- | ----------------------- | ------------------- | ------------------ | ------ | ----- |
| TBD | TBD | TBD | TBD | TBD | TBD | NOT VERIFIED | Scaffold — populate per approved WP/CR |
| DC-DCC-PWR-* | `docs/DCC/Power_Channel_Requirements.md` | `docs/DCC/Power_Channel_Architecture.md` | TBD | TBD | TBD | NOT VERIFIED | WP-004 — implementation pending |
| DC-DCC-ARCH-* | `docs/DCC/DCC_Internal_Architecture.md` | `docs/DCC/DCC_Module_Map.md` | TBD | TBD | TBD | NOT VERIFIED | WP-005 — firmware mapping pending |
| E30LD-* | `docs/Vehicle_Integration/E30_Gen1_Load_Inventory.md` | `config/vehicles/e30_gen1_loads.yaml` | TBD | Measurement plan | TBD | NOT VERIFIED | WP-003 — measurements pending |

## Status values

| Status | Meaning |
|--------|---------|
| NOT VERIFIED | No executed verification with evidence |
| PARTIAL | Some evidence exists; incomplete |
| PASS | Verified with reproducible evidence |
| FAIL | Verification executed; failed |
| OPEN ISSUE | Traceability or requirement gap |

## How to extend

1. Add a row when a requirement is implemented or a WP/CR creates a new requirement ID.
2. Link Evidence Reference to a filled `Verification_Evidence_Template` instance or evidence path.
3. Do not mark PASS without revision identity and actual results (constitution §6).

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 initial scaffold |
