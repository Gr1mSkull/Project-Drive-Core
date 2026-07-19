# DriveCore — Current Phase

**Updated:** WP-007 Gen1 DevKit requirements baseline (2026-07-19)

## Documentation

| Stage | Status |
|-------|--------|
| 1 Architecture (001, 004, 005) | ✅ v0.1 |
| 2 Hardware (002, 007) | ✅ v0.1 |
| 3 ECU + UI (003, 006) | ✅ v0.1 |
| 4 Validation (008) | ✅ v0.1.1 strategy overview (WP-007) |
| 5 Implementation scaffold | ✅ v0.1 (`firmware/shared`, tools, web/ui) |
| WP-001…WP-006 / CR-001 / CR-002 / ADR-015 | ✅ on `main` (see git history) |
| **WP-007 DevKit requirements + verification plan** | 🔄 Proposed — Architecture Review |

## DevKit (WP-007)

| Item | Status |
|------|--------|
| Requirements `REQ-DCC-V-DK-001…118` | Proposed |
| Verification plan DK-A…DK-D | Proposed (NOT EXECUTED) |
| Hardware design approved | **No** |
| Firmware bring-up complete | **No** (NOT IMPLEMENTED) |
| Physical verification | **NOT VERIFIED** |
| Blocking ADRs | ADR-DK-001…012 |

## SRS

`docs/SRS/Volume_2_DCC.md` §8.1 points to `docs/DevKit/DevKit_System_Requirements.md`. Other SRS chapters remain largely structural.

## Next expected work (after Architecture Review of WP-007)

1. Resolve ADR-DK blocking decisions and priority thresholds  
2. DevKit electrical / representative power-channel architecture  
3. Test fixture and load-bank requirements  
4. Component qualification as authorized  
5. PCB design and firmware bring-up (only after architecture approval)

## Active branch

`cursor/wp007-gen1-devkit-requirements-3bb9`

## Do not start without approval

Architecture changes · new components in BOM · firmware feature work · PCB/schematics · marking DevKit Verified / Approved for Prototype
