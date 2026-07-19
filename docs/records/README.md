# DriveCore Engineering Records

**Document ID:** DOC-REC-001  
**Version:** 1.0.1  
**Status:** Proposed  
**Change Request:** CR-002-R1 / CR-002-R2

## Purpose

Canonical storage for **filled** engineering-quality records.

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6, §13, §18.

**Templates** remain in `docs/templates/`.  
**Filled records** belong only under `docs/records/`.

Do not fabricate example evidence records.

## Directories

| Path | Contents | Naming |
|------|----------|--------|
| [change_impact/](change_impact/) | Full Change Impact Analysis (Level 2) | `CIA-YYYY-NNN_<short-title>.md` |
| [verification/](verification/) | Verification evidence | `VE-YYYY-NNN_<short-title>.md` |
| [review_handoffs/](review_handoffs/) | Review Handoff Packages | `RHP-YYYY-NNN_<short-title>.md` |

## Impact Level reminder

| Level | Where recorded |
|-------|----------------|
| 0 | Completion report statement only |
| 1 | Lightweight Impact Note in WP or Completion Report (default — see below) |
| 2 | Full CIA file in `change_impact/` |

## Level 1 Lightweight Impact Note retention

- Level 1 Lightweight Impact Notes remain in the **Work Package or Completion Report** by default.
- Do **not** create a separate archived record for every Level 1 change.
- A separate record may be created only when the note:
  - applies to multiple Work Packages or pull requests;
  - is referenced by verification evidence;
  - is referenced by an ADR or EDL;
  - must remain independently discoverable after the originating task is closed.

Do not create a dedicated Level 1 directory unless a future Change Request authorizes it.

## Related

- Templates: [../templates/](../templates/)
- Traceability: [../traceability/](../traceability/)

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002-R1 canonical record storage |
| 1.0.1 | 2026-07-19 | CR-002-R2 Level 1 retention policy |
