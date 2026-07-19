# DriveCore Traceability

**Document ID:** DOC-TRACE-001  
**Version:** 1.3.1  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1 / CR-002-R2 · **ADR:** ADR-015 · **WP:** WP-007 / WP-007-R2

## Purpose

Controlled location for requirement–implementation–test traceability artifacts.

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6 (Requirement–implementation–test traceability).

## Chain

```text
Requirement ID
→ Architecture or interface reference
→ Implementation artifact
→ Verification method
→ Verification result
```

## Contents

| Artifact | Path |
|----------|------|
| Traceability matrix (scaffold) | [TRACEABILITY_MATRIX.md](TRACEABILITY_MATRIX.md) |
| Verification evidence template | [../templates/Verification_Evidence_Template.md](../templates/Verification_Evidence_Template.md) |
| Filled verification records | [../records/verification/](../records/verification/) |
| Change impact analysis template | [../templates/Change_Impact_Analysis_Template.md](../templates/Change_Impact_Analysis_Template.md) |
| Filled CIA records | [../records/change_impact/](../records/change_impact/) |

## Rules

- Primary matrix: **atomic** Requirement IDs only.
- Wildcard families: pending-import section only.
- Do not invent requirement links to fill empty cells.
- Use `TBD`, `OPEN ISSUE`, or `NOT VERIFIED` where evidence is missing.
- Do not reconstruct all historical traceability in a single change request.
- Orphan implementation is prohibited unless explicitly approved.

## Related

- `docs/SRS/` — system requirements (structure)
- `docs/ADR/`, `docs/EDL/` — architectural decisions
- [`docs/standards/REVISION_IDENTITY_STANDARD.md`](../standards/REVISION_IDENTITY_STANDARD.md) — composite baseline for verification evidence (ADR-015)
- `docs/records/` — filled engineering records
- `.cursor/ENGINEERING_CONSTITUTION.mdc` — authoritative policy

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | CR-002 scaffold |
| 1.1 | 2026-07-19 | CR-002-R1 atomic IDs; records links |
| 1.1.1 | 2026-07-19 | Link revision-identity standard (ADR-015) |
| 1.1.2 | 2026-07-19 | ADR-015-R1 — canonical ADR-015 reference |
| 1.2 | 2026-07-19 | WP-007 — DevKit `REQ-DCC-V-DK-*` imported to primary matrix (NOT VERIFIED) |
| 1.3 | 2026-07-19 | WP-007-R1 — active system vs governance traceability subsections |
| 1.3.1 | 2026-07-19 | WP-007-R2 — note TBD register authority in System Requirements §4 |
