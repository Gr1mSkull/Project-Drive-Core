# DriveCore — Current Phase

**Updated:** WP-013 Proposed — component-class qualification and symbolic calculations (2026-07-20)

## Documentation

| Stage | Status |
|-------|--------|
| 1 Architecture (001, 004, 005) | ✅ v0.1 |
| 2 Hardware (002, 007) | ✅ v0.1 |
| 3 ECU + UI (003, 006) | ✅ v0.1 |
| 4 Validation (008) | ✅ v0.1.2 strategy overview (WP-007/R1) |
| 5 Implementation scaffold | ✅ v0.1 (`firmware/shared`, tools, web/ui) |
| WP-001…WP-006 / CR-001 / CR-002 / ADR-015 | ✅ on `main` (see git history) |
| **WP-007 DevKit requirements + verification plan** | ✅ Accepted (2026-07-20) — evidence NOT VERIFIED |
| **WP-008 DevKit P0 architecture decisions** | ✅ Accepted (2026-07-20) — ADR-016…023 |
| **WP-009 DevKit threshold analysis** | ✅ Accepted (2026-07-20) — methods Accepted; numeric Open |
| **WP-010 DevKit functional electrical architecture** | ✅ Accepted (2026-07-20) — WP-010-R1 Accepted |
| **WP-011 EDL-011 + component-class prep** | ✅ Accepted (2026-07-20) — WP-011-R1 Accepted |
| **WP-012 electrical sizing architecture framework** | ✅ Accepted (2026-07-20) — WP-012-R1/R2 Accepted |
| **WP-013 component-class qualification + symbolic calcs** | ⏳ Proposed — Architecture Review pending |

## DevKit (WP-007 … WP-013)

| Item | Status |
|------|--------|
| Active system `REQ-DCC-V-DK-*` (93) + `DK-GOV-*` (25) | **Accepted** (structure); NOT VERIFIED (evidence) |
| Verification plan DK-A…DK-D | **Accepted** structure (cases NOT EXECUTED / BLOCKED) |
| P0 ADRs ADR-016…023 | **Accepted** |
| Threshold analysis methods | **Accepted** (WP-009) |
| Threshold numeric values | **Open** (TBD-DK-001…022) |
| Functional electrical architecture | **Accepted** (WP-010 / WP-010-R1) |
| TBD-DK-007 | **BLOCKED_BY_EDL_CLARIFICATION** — not Resolved; numeric Open; verification Not Verified |
| Component-class qualification prep | **Accepted** (WP-011) |
| Electrical sizing framework | **Accepted** (WP-012) |
| Component-class recommendations | **Proposed** (WP-013) — not Accepted |
| Concrete component qualification | **Not started** |
| MPN selection | **Not authorized** |
| Symbolic preliminary calculations | **Proposed** (WP-013) |
| Numeric baseline | **Not created** |
| Hardware design approved | **No** — NOT IMPLEMENTED |
| Detailed electrical sizing | **NOT COMPLETED** |
| Schematics / PCB | **NOT AUTHORIZED** |
| Firmware bring-up complete | **No** (NOT IMPLEMENTED) |
| Physical verification | **NOT VERIFIED** |
| Remaining open requests | ADR-DK-008, 009, 011, 012; OI-PROT-001/002 |

## Next authorized work (after WP-013 acceptance)

Fixture / load-bank requirements · ADR-DK-011 / ADR-DK-012 · concrete MPN qualification preparation · provisional design-baseline preparation (Architect only).

## Active branch

`cursor/wp013-devkit-component-class-qualification-3bb9` — PR #17 (Architecture Review pending)

## Do not start without approval

MPN selection · BOM · schematics · PCB · numeric threshold approval · EDL file edit · firmware · fixture construction · Verification Evidence creation
