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
| [ADR-016](ADR-016-devkit-logic-board-fidelity.md) | DevKit Logic Board Fidelity and Reuse | Accepted | ADR-DK-001 |
| [ADR-017](ADR-017-devkit-radio-board-fidelity.md) | DevKit Radio Board Fidelity and Reuse | Accepted | ADR-DK-002 |
| [ADR-018](ADR-018-devkit-firmware-equivalence.md) | DevKit Firmware Equivalence | Accepted | ADR-DK-003 |
| [ADR-019](ADR-019-devkit-represented-power-capabilities.md) | DevKit Represented Power Capabilities | Accepted | ADR-DK-004 |
| [ADR-020](ADR-020-devkit-high-current-verification-scope.md) | DevKit Highest-Current Verification Scope | Accepted | ADR-DK-005 |
| [ADR-021](ADR-021-devkit-input-current-architecture.md) | DevKit Input and Simultaneous-Current Architecture | Accepted | ADR-DK-006 |
| [ADR-022](ADR-022-devkit-kill-watchdog-timing-policy.md) | DevKit Kill and Watchdog Timing Policy | Accepted | ADR-DK-007 |
| [ADR-023](ADR-023-devkit-fault-injection-scope.md) | DevKit Fault Injection Scope and Fixture Boundary | Accepted | ADR-DK-010 |

Normative standard: [`docs/standards/REVISION_IDENTITY_STANDARD.md`](../standards/REVISION_IDENTITY_STANDARD.md) (STD-REV-001 — Approved).

DevKit P0 crosswalk: [`docs/DevKit/DevKit_P0_Decision_Crosswalk.md`](../DevKit/DevKit_P0_Decision_Crosswalk.md) (WP-008 **Accepted**).

ADR-021 / ADR-022: architecture/policy **Accepted**; numeric thresholds remain **Open**.

Next sequential ADR: `ADR-024-*.md`.

Remaining open DevKit decision **requests** (no canonical ADR in WP-008): ADR-DK-008, ADR-DK-009, ADR-DK-011, ADR-DK-012.

Historical EDL numbering is unchanged. General EDL↔ADR migration numbering remains outside ADR-015 scope.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 ADR/EDL index |
| 1.1 | 2026-07-19 | ADR-015 revision identity formalization |
| 1.1.1 | 2026-07-19 | ADR-015-R1 — canonical ID ADR-015; Accepted |
| 1.2 | 2026-07-20 | WP-008 — Proposed ADR-016…023 DevKit P0 package |
| 1.3 | 2026-07-20 | Architecture Review — ADR-016…023 Accepted; WP-008 Accepted; PR #12 approved for merge |
