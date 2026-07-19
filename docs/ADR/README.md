# Architecture Decision Records (ADR)

DriveCore records architectural decisions in two linked locations:

| Location | Format | Status |
|----------|--------|--------|
| **This folder** | `ADR-NNN-*.md` (new decisions) | Active from WP-001 |
| **`docs/EDL/`** | EDL-001..014 in [README.md](../EDL/README.md) | Accepted Gen1 decisions |

## Policy

- New ADR-level decisions shall use `docs/templates/ADR_Template.md`.
- Legacy **EDL** entries remain authoritative; they may be migrated to `ADR-NNN` files without changing substance.
- Supersede — do not delete — prior ADRs.
- Normative detail that follows an accepted ADR may live under [`docs/standards/`](../standards/README.md); the ADR remains the rationale source.
- Canonical ADR identifiers use the `ADR-NNN` form. Originating decision-request or Change Request aliases are not second active ADR IDs.

## Index (EDL → ADR equivalent)

| ID | Title | Status |
|----|-------|--------|
| EDL-001 | STM32G474 in Logic | Accepted |
| EDL-002 | Separate Radio Board (ESP32) | Accepted |
| EDL-003 | Smart High Side switches | Accepted |
| EDL-004 | Web UI Gen1 | Accepted |
| EDL-005 | ECU engine-only boundary | Accepted |
| EDL-006 | VCM in DCC | Accepted |
| EDL-007 | Three-board DCC | Accepted |
| EDL-008 | One CAN FD bus Gen1 | Accepted |
| EDL-009 | DriveCore Protocol naming | Accepted |
| EDL-010 | Binary SPI / DCPI | Accepted |
| EDL-011 | J_LP Logic↔Power interface | Accepted |
| EDL-012 | ECU simulator / third-party ECU | Accepted |
| EDL-013 | Web UI auth model | Accepted |
| EDL-014 | DevKit gate before vehicle | Accepted |

## New ADR files

| Canonical ADR ID | Title | Status | Originating request (alias) |
|------------------|-------|--------|-----------------------------|
| [ADR-015](ADR-015-platform-revision-identity.md) | DriveCore Platform Revision Identity and System Baseline | Accepted | ADR-CR002-001 (CR-002) |

Normative standard: [`docs/standards/REVISION_IDENTITY_STANDARD.md`](../standards/REVISION_IDENTITY_STANDARD.md) (STD-REV-001 — Approved).

Next sequential ADR: `ADR-016-*.md`.

Historical EDL numbering is unchanged. General EDL↔ADR migration numbering remains outside ADR-015 scope.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 ADR/EDL index |
| 1.1 | 2026-07-19 | ADR-015 revision identity formalization |
| 1.1.1 | 2026-07-19 | ADR-015-R1 — canonical ID ADR-015; Accepted |
