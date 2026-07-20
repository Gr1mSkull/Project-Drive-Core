# DriveCore — Current Phase

**Updated:** WP-008 Accepted — DevKit P0 ADRs ADR-016…023 (2026-07-20)

## Documentation

| Stage | Status |
|-------|--------|
| 1 Architecture (001, 004, 005) | ✅ v0.1 |
| 2 Hardware (002, 007) | ✅ v0.1 |
| 3 ECU + UI (003, 006) | ✅ v0.1 |
| 4 Validation (008) | ✅ v0.1.2 strategy overview (WP-007/R1) |
| 5 Implementation scaffold | ✅ v0.1 (`firmware/shared`, tools, web/ui) |
| WP-001…WP-006 / CR-001 / CR-002 / ADR-015 | ✅ on `main` (see git history) |
| **WP-007 DevKit requirements + verification plan** | ✅ Accepted (2026-07-20) — structure/governance/plan/traceability; evidence still NOT VERIFIED |
| **WP-008 DevKit P0 architecture decisions** | ✅ Accepted (2026-07-20) — ADR-016…023; ADR-021/022 numerics Open |

## DevKit (WP-007 / WP-008)

| Item | Status |
|------|--------|
| Active system `REQ-DCC-V-DK-*` (93) + `DK-GOV-*` (25) | **Accepted** (structure); NOT VERIFIED (evidence) |
| Verification plan DK-A…DK-D | **Accepted** structure (cases NOT EXECUTED / BLOCKED) |
| P0 ADRs ADR-016…023 (ADR-DK-001…007, 010) | **Accepted** (ADR-021/022 numeric limits Open) |
| Hardware design approved | **No** |
| Firmware bring-up complete | **No** (NOT IMPLEMENTED) |
| Physical verification | **NOT VERIFIED** |
| Remaining open requests | ADR-DK-008, 009, 011, 012 |
| Thresholds | TBD-DK-001…022 **Open** |

## SRS

`docs/SRS/Volume_2_DCC.md` §8.1 points to `docs/DevKit/DevKit_System_Requirements.md`. Other SRS chapters remain largely structural.

## Next expected work (after WP-008 acceptance)

1. Threshold-analysis WP (TBD-DK currents/timings)  
2. DevKit electrical / representative power-channel architecture  
3. Test fixture and load-bank requirements  
4. Component qualification as authorized  
5. PCB design and firmware bring-up (only after electrical architecture approval)

## Active branch

`cursor/wp008-devkit-p0-architecture-decisions-3bb9` (PR #12 approved for merge)

## Do not start without approval

New architecture beyond Accepted ADRs · new components in BOM · firmware feature work · PCB/schematics · marking DevKit Verified / Approved for Prototype · closing TBD numerics without analysis
