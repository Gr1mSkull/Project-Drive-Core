# DriveCore Traceability Matrix

**Document ID:** DOC-TRACE-MAT-001  
**Version:** 1.1.1  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1 / CR-002-R2

Controlled **scaffold**. Do not invent historical links.

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6.

**Rules:**

- Primary matrix rows shall use **atomic** Requirement IDs only.
- Wildcard requirement families belong in § Requirement Families Pending Atomic Import — not in the primary matrix.
- Do not invent atomic requirements or verification links.
- Incomplete entries remain `NOT VERIFIED`.

## Primary matrix (atomic Requirement IDs)

| Requirement ID | Requirement Source | Architecture / Interface Reference | Implementation Artifact | Configuration / Data Artifact | Verification Method | Evidence Reference | Status | Notes |
| -------------- | ------------------ | ---------------------------------- | ----------------------- | ----------------------------- | ------------------- | ------------------ | ------ | ----- |

<!-- Add rows only when atomic Requirement IDs are formally imported. -->

## Requirement Families Pending Atomic Import

| Requirement family | Source document | Responsible future WP | Current status | Notes |
| ------------------ | --------------- | --------------------- | -------------- | ----- |
| DC-DCC-PWR-* | `docs/DCC/Power_Channel_Requirements.md` | Future SRS / requirements import WP | NOT VERIFIED | Atomic IDs exist in source doc; not yet imported as matrix rows |
| DC-DCC-ARCH-* | `docs/DCC/DCC_Internal_Architecture.md` | Future SRS / requirements import WP | NOT VERIFIED | Atomic IDs exist in source doc; firmware mapping pending |
| E30LD-* | `docs/Vehicle_Integration/E30_Gen1_Load_Inventory.md` | Future measurement / SRS import WP | NOT VERIFIED | Load inventory IDs; measurements pending. Data artifact: `config/vehicles/e30_gen1_loads.yaml` (not an architecture interface) |

## Status values

| Status | Meaning |
|--------|---------|
| NOT VERIFIED | No executed verification with evidence |
| PARTIAL | Some evidence exists; incomplete |
| PASS | Verified with reproducible evidence (Independent Reviewer / Test Owner certification) |
| FAIL | Verification executed; failed |
| OPEN ISSUE | Traceability or requirement gap |

## How to extend

1. Add a primary-matrix row only for an **atomic** Requirement ID.
2. Place Architecture / Interface Reference only when an approved architecture or interface definition justifies it.
3. Use Configuration / Data Artifact for YAML, load inventories, and similar non-interface data.
4. Link Evidence Reference to `docs/records/verification/VE-YYYY-NNN_<short-title>.md`.
5. Do not mark PASS without revision identity, actual results, and appropriate verification authority (constitution §4 / §6).

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 initial scaffold |
| 1.1 | 2026-07-19 | CR-002-R1 — atomic IDs only; families section; config column |
| 1.1.1 | 2026-07-19 | CR-002-R2 — remove TBD placeholder row from primary matrix |
