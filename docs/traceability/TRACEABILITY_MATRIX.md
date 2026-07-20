# DriveCore Traceability Matrix

**Document ID:** DOC-TRACE-MAT-001  
**Version:** 1.6.9  
**Status:** Accepted  
**Work Package:** WP-007 (Accepted); WP-010 architecture refs

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6.

## Coverage check (WP-007-R1)

```text
Active DevKit system requirements: 93
Governance rules: 25
Withdrawn requirement IDs: 25
System verification coverage (active req → case): 100 %
Governance inspection coverage: mapped via VER-DCC-DK-G-*
Implementation coverage (active system): 0 %
Evidence coverage: 0 %
Verified DevKit requirements: 0
Verification cases (system + governance): 67
Blocked cases (approx): 26
```

## Primary matrix — active system requirements

| Requirement ID | Requirement Source | Architecture / Interface Reference | Implementation Artifact | Configuration / Data Artifact | Verification Method | Evidence Reference | Status | Notes |
| -------------- | ------------------ | ---------------------------------- | ----------------------- | ----------------------------- | ------------------- | ------------------ | ------ | ----- |
| REQ-DCC-V-DK-001 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-004 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Analysis: `VER-DCC-DK-A-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-005 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-007 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (scaffold) | Demonstration: `VER-DCC-DK-A-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-009 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006; Accepted ADR-016 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-010` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-010 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006; Accepted ADR-017 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-005`, `VER-DCC-DK-D-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-011 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety; Accepted ADR-016 | TBD | config/vehicles/devkit.yaml (scaffold) | Test / Inspection: `VER-DCC-DK-A-007`, `VER-DCC-DK-A-008` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-012 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001; Accepted ADR-016/017 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-007`, `VER-DCC-DK-A-009`, `VER-DCC-DK-B-006` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-013 | docs/DevKit/DevKit_System_Requirements.md | docs/005; Accepted ADR-018 | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis / Test: `VER-DCC-DK-D-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-014 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-019 | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis / Test: `VER-DCC-DK-C-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-017 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test / Inspection: `VER-DCC-DK-A-015` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-018 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-019 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Demonstration: `VER-DCC-DK-A-002`, `VER-DCC-DK-A-007` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-020 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004; Accepted ADR-021 (TBD-DK-002 Open) | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Analysis: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-021 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety; Accepted ADR-022 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-022 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-023 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-023 (supply interruption DK-A) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-003`, `VER-DCC-DK-A-016` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-024 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-025 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-026 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Demonstration: `VER-DCC-DK-C-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-027 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Test: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-030 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Demonstration: `VER-DCC-DK-A-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-031 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-032 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test / Demonstration: `VER-DCC-DK-A-013` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-033 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-034 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-014` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-035 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety; Accepted ADR-022 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-008`, `VER-DCC-DK-C-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-036 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001; Accepted ADR-022 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-037 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-012`, `VER-DCC-DK-B-012`, `VER-DCC-DK-B-013` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-038 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004; Accepted ADR-022 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-011` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-039 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-001`, `VER-DCC-DK-C-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-040 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-041 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-042 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004; Accepted ADR-019 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-010` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-043 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-044 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-005` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-045 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-006` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-046 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-019 CONDITIONAL_ON_DEVKIT; Accepted ADR-023 CONDITIONAL_MANDATORY | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-007` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-047 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-008` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-048 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-009` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-049 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-014` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-050 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-016`, `VER-DCC-DK-C-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-051 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-009`, `VER-DCC-DK-C-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-054 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-010`, `VER-DCC-DK-C-011` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-055 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-013` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-056 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-057 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-058 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; Accepted ADR-022/023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-011` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-059 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-010` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-060 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001; Accepted ADR-023 (supply interruption DK-D / reset) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-014`, `VER-DCC-DK-D-017` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-061 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-062 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-063 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-016` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-064 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-016` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-065 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-066 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-005` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-067 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-009`, `VER-DCC-DK-B-006` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-068 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-007` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-069 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-009` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-070 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-010` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-071 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-011` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-072 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006; Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-012` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-073 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001; Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-013` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-075 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-076 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Test: `VER-DCC-DK-B-005` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-077 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-002`, `VER-DCC-DK-D-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-078 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-004`, `VER-DCC-DK-D-006` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-079 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-003`, `VER-DCC-DK-D-014` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-080 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-014` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-081 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Demonstration: `VER-DCC-DK-B-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-083 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-B-007` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-084 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-015`, `VER-DCC-DK-D-011` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-085 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-007`, `VER-DCC-DK-D-008` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-086 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis / Test: `VER-DCC-DK-D-003`, `VER-DCC-DK-D-005` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-087 | docs/DevKit/DevKit_System_Requirements.md | docs/005; Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-015`, `VER-DCC-DK-D-018` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-088 | docs/DevKit/DevKit_System_Requirements.md | docs/005 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-D-007`, `VER-DCC-DK-D-018` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-089 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Test: `VER-DCC-DK-B-007`, `VER-DCC-DK-B-015` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-093 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-094 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-003` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-095 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-004` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-096 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-C-009` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-097 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed) | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-B-009` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-098 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Demonstration: `VER-DCC-DK-B-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-099 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006; Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-009`, `VER-DCC-DK-B-008` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-100 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); Accepted ADR-023 | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis / Test: `VER-DCC-DK-C-005`, `VER-DCC-DK-C-006` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-101 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Test: `VER-DCC-DK-A-014`, `VER-DCC-DK-D-017` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-102 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Demonstration: `VER-DCC-DK-C-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-113 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis / Inspection: `VER-DCC-DK-A-008` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-114 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001; Accepted ADR-016/017 (not ADR-023) | TBD | config/vehicles/devkit.yaml (scaffold) | Analysis: `VER-DCC-DK-A-017` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-115 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-A-002` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-116 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection: `VER-DCC-DK-C-001` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-117 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Demonstration: `VER-DCC-DK-A-006`, `VER-DCC-DK-A-007`, `VER-DCC-DK-D-019` | TBD | NOT VERIFIED | WP-007-R1 active |
| REQ-DCC-V-DK-118 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (scaffold) | Inspection / Demonstration: `VER-DCC-DK-B-007` | TBD | NOT VERIFIED | WP-007-R1 active |

## Governance traceability (not implementation coverage)

| Rule ID | Title | Source | Verification | Method | Implementation | Status | Notes |
| ------- | ----- | ------ | ------------ | ------ | -------------- | ------ | ----- |
| DK-GOV-001 | Non-substitution of DevKit for product acceptance | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-001 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-002 | Gate completion does not authorize vehicle install | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-001 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-003 | Evidence-use limitation | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-001 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-004 | EDL-014 exceptions recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-001 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-005 | No coverage claims for unrepresented classes | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-002 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-006 | MPN prohibition in normative DevKit requirements | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-002 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-007 | No protocol layout redefinition during DevKit verification | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-002 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-008 | No invented encoded-version mappings | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-002 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-009 | Equivalence claims require Accepted ADR | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-004 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-010 | OTA gate-scope decision dependency | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-004 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-011 | Hot-reload assumption prohibition | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-004 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-012 | Composite baseline on verification records | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-013 | Configuration identity in evidence | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-* | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-014 | Baseline required for gate-exit cases | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-015 | Firmware identity recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-016 | Bootloader identity recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-017 | Hardware identity recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-018 | Configuration ID/schema/hash recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-019 | Protocol version recording without invented mapping | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-020 | Test equipment and fixture identity recording | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-021 | Evidence storage convention | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-022 | Raw result vs certification separation | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-023 | Physical Test Owner authority | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-003 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-024 | Voltage range freeze before power-test gate exit | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-004 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |
| DK-GOV-025 | Simultaneous load current freeze before multi-load DK-C | docs/DevKit/DevKit_Verification_Governance.md | VER-DCC-DK-G-004 | Process inspection | N/A (not implementation) | NOT VERIFIED | WP-007-R1 |

## Withdrawn system requirement IDs (preserved; not reused)

| Requirement ID | Status | Moved to | Implementation | Verification | Evidence | Matrix status | Notes |
| -------------- | ------ | -------- | -------------- | ------------ | -------- | ------------- | ----- |
| REQ-DCC-V-DK-002 | Withdrawn — moved to DK-GOV-001 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-003 | Withdrawn — moved to DK-GOV-002 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-006 | Withdrawn — moved to DK-GOV-003 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-008 | Withdrawn — moved to DK-GOV-004 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-015 | Withdrawn — moved to DK-GOV-009 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-016 | Withdrawn — moved to DK-GOV-012 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-028 | Withdrawn — moved to DK-GOV-024 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-029 | Withdrawn — moved to DK-GOV-025 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-052 | Withdrawn — moved to DK-GOV-005 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-053 | Withdrawn — moved to DK-GOV-006 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-074 | Withdrawn — moved to DK-GOV-010 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-082 | Withdrawn — moved to DK-GOV-007 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-090 | Withdrawn — moved to DK-GOV-013 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-091 | Withdrawn — moved to DK-GOV-011 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-092 | Withdrawn — moved to DK-GOV-008 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-103 | Withdrawn — moved to DK-GOV-014 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-104 | Withdrawn — moved to DK-GOV-015 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-105 | Withdrawn — moved to DK-GOV-016 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-106 | Withdrawn — moved to DK-GOV-017 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-107 | Withdrawn — moved to DK-GOV-018 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-108 | Withdrawn — moved to DK-GOV-019 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-109 | Withdrawn — moved to DK-GOV-020 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-110 | Withdrawn — moved to DK-GOV-021 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-111 | Withdrawn — moved to DK-GOV-022 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |
| REQ-DCC-V-DK-112 | Withdrawn — moved to DK-GOV-023 | See governance matrix | — | — | — | WITHDRAWN | Do not count as active system implementation |


## Fixture requirements matrix — WP-014 (Proposed)

Prefix `REQ-DCC-V-FX-*` newly allocated. All rows **NOT VERIFIED**. Implementation **NOT IMPLEMENTED**. No VE. Cases that consume fixture capabilities remain **NOT EXECUTED / BLOCKED**.

| Requirement ID | Requirement Source | Architecture / Interface Reference | Implementation Artifact | Verification Method | Evidence Reference | Status | Notes |
| -------------- | ------------------ | ---------------------------------- | ----------------------- | ------------------- | ------------------ | ------ | ----- |
| REQ-DCC-V-FX-001…004 | DevKit_Fixture_and_Load_Bank_Requirements.md | DOC-DK-FFA-001 states/identity | NOT IMPLEMENTED | Future fixture verification | None | NOT VERIFIED | PROPOSED; SAFE_OFF default; stale commands |
| REQ-DCC-V-FX-005 | DevKit_Fixture_and_Load_Bank_Requirements.md | FFA §5.1; OI-GND-001 | NOT IMPLEMENTED | Future EXT auth-only / combined-block inspection | None | NOT VERIFIED | PROPOSED; EXTERNAL_ENERGY_ARMED ≠ energized |
| REQ-DCC-V-FX-010…015 | DevKit_Fixture_and_Load_Bank_Requirements.md | FESB; ADR-022; PWR-A-004/005 | NOT IMPLEMENTED | Future E-stop/KILL/AUTH tests | None | NOT VERIFIED | PROPOSED; authorities distinct |
| REQ-DCC-V-FX-020…026 | DevKit_Fixture_and_Load_Bank_Requirements.md | ADR-021; WP-012 P0–P5; PWR-A-017 ACCEPTED | NOT IMPLEMENTED | Future base-source tests | None | NOT VERIFIED | PROPOSED; numerics Open |
| REQ-DCC-V-FX-030…034 | DevKit_Fixture_and_Load_Bank_Requirements.md | ADR-020/021; OI-GND-001; OI-FIX-001 | NOT IMPLEMENTED | Future EXT tests | None | NOT VERIFIED | PROPOSED; stuck-on upstream energy remove; GND BLOCKED |
| REQ-DCC-V-FX-040 | DevKit_Fixture_and_Load_Bank_Requirements.md | FIXTURE-AUX | NOT IMPLEMENTED | Future AUX-loss tests | None | NOT VERIFIED | PROPOSED |
| REQ-DCC-V-FX-050…056 | DevKit_Fixture_and_Load_Bank_Requirements.md | LFPC; ADR-023; WP-012 E_FAULT | NOT IMPLEMENTED | Future load/fault tests | None | NOT VERIFIED | PROPOSED; blocked faults explicit |
| REQ-DCC-V-FX-060…062 | DevKit_Fixture_and_Load_Bank_Requirements.md | FIMR; WP-012 sign convention | NOT IMPLEMENTED | Future measurement cal | None | NOT VERIFIED | PROPOSED |
| REQ-DCC-V-FX-070 | DevKit_Fixture_and_Load_Bank_Requirements.md | IF-FX-* | NOT IMPLEMENTED | Future interface inspection | None | NOT VERIFIED | PROPOSED; pinouts Open |
| REQ-DCC-V-FX-071 | DevKit_Fixture_and_Load_Bank_Requirements.md | H-FX-008; E-stop integrity | NOT IMPLEMENTED | Future design allocation review | None | NOT VERIFIED | PROPOSED; prelim design BLOCKED_BY_ARCHITECTURE |

Fixture-dependent DevKit cases (examples): VER-DCC-DK-A-011/012/014; VER-DCC-DK-C-002…014 — remain **NOT EXECUTED / BLOCKED**. Mapping: `DevKit_Fixture_Verification_Capability_Matrix.md`.

## Notes

* All DevKit statuses remain `NOT VERIFIED`. No Verification Evidence records created in WP-007 / R1 / R2 / WP-008.
* Governance rules are verified by document/process inspection only and are **not** counted toward implementation coverage.
* Threshold dependencies (`TBD-DK-*`) are references to the authoritative register in `docs/DevKit/DevKit_System_Requirements.md` §4 — not requirement replacements. **Status Open** unchanged by WP-008.
* Accepted ADR-016…023 may appear in Architecture / Interface Reference columns; Accepted ADR references do **not** mark requirements Verified; evidence remains NOT VERIFIED.
* WP-008-R1: open-load CONDITIONAL; ADR-023 excludes REQ-114; supply interruption maps to A-003 and D-017 only.
* WP-008 Architecture Review (2026-07-20): ADR-016…023 Accepted; TBD numerics remain Open; statuses remain NOT VERIFIED.
* WP-009 (2026-07-20): Threshold analysis references in TBD register §4 and DevKit analysis docs; **no** threshold Resolved; **no** requirement Verified; evidence NOT VERIFIED.
* WP-009-R1 (2026-07-20): EDL-011 ambiguity correction; symbolic current scenarios; profile/overlap simultaneous model; TBD-DK-007 BLOCKED_BY_EDL_CLARIFICATION.
* WP-009 Architecture Review (2026-07-20): **Accepted** — threshold analysis methods Accepted; numeric values Open; evidence NOT VERIFIED; functional electrical architecture authorized.
* WP-010 (2026-07-20): Functional electrical architecture **Accepted** — WP-010-R1 Accepted; architecture refs in DevKit FEA package; **no** threshold Resolved; **no** requirement Verified; evidence NOT VERIFIED; WP-011 authorized.
* WP-010 Architecture Review (2026-07-20): PR #14 merged (`c98ce56`); functional decomposition Accepted; sizing/schematic/PCB NOT AUTHORIZED.
* WP-011 Architecture Review (2026-07-20): EDL-011 clarification + component-class framework **Accepted** — WP-011-R1 Accepted; PR #15 merged (`07c550c`); EDL files unchanged; TBD-DK-007 **BLOCKED_BY_EDL_CLARIFICATION** (not Resolved); NOT VERIFIED unchanged.
* WP-012 (2026-07-20): Electrical sizing architecture framework **Proposed**; WP-012-R2 **Ready for Final Architecture Acceptance**; signed net `I_CH_IN_n` convention; Stage [D] qualification authority clarified; sizing methods Proposed; numeric Open; NOT VERIFIED unchanged; TBD-DK-007 BLOCKED retained.
* WP-012 Architecture Review (2026-07-20): Electrical sizing framework **Accepted** — WP-012-R1/R2 Accepted; PR #16 merged (`9c5c7e7` / `fe700d4`); sizing methods Accepted; numeric Open; NOT VERIFIED unchanged; TBD-DK-007 **BLOCKED_BY_EDL_CLARIFICATION** retained; WP-013 authorized.
* WP-013 (2026-07-20): Component-class qualification and symbolic preliminary calculations **Proposed**; class recommendations Proposed (not Accepted); no MPN; numeric Open; NOT VERIFIED unchanged; TBD-DK-007 BLOCKED retained.
* WP-013 Architecture Review (2026-07-20): Component-class qualification methodology **Accepted** — WP-013-R1 Accepted; PR #17 merged (`d1698a0` / `23bdb07`); evaluation directions Accepted; final HS/sense/BI/protection classes **Open**; OI-COMP/SENSE/PROT/BI remain Open; numeric Open; NOT VERIFIED unchanged; TBD-DK-007 **BLOCKED_BY_EDL_CLARIFICATION** retained; WP-014 authorized.
* WP-014 (2026-07-20): Fixture and load-bank requirements **Proposed**; REQ-DCC-V-FX-* NOT VERIFIED; fixture NOT IMPLEMENTED; no VE; no PASS; numeric Open; TBD-DK-007 BLOCKED retained; OI-GND-001 Open; WP-013 Accepted baseline retained.
* WP-014 Architecture Acceptance (2026-07-20): Fixture and load-bank requirements **Accepted** — R1/R2/R3 Accepted; PR #18 merged (`7c72181` / `e46aff4`; reviewed head `084f579`); REQ-DCC-V-FX-* Accepted as requirements but remain **NOT VERIFIED**; fixture **NOT IMPLEMENTED**; no VE; no case PASS; numeric Open; TBD-DK-007 BLOCKED_BY_EDL_CLARIFICATION retained; OI-GND-001/OI-PROT/OI-FIX/OI-SC/OI-BI remain Open; PWR-A-017/018/021…024 ACCEPTED_CONSTRAINT; WP-015 authorized.
* WP-014-R1 (2026-07-20): Architecture consistency corrections — EXTERNAL_ENERGY_ARMED authorization-only; OI-GND combined BASE/EXT block; load-bank stuck-on upstream energy remove; E-stop integrity REQ-DCC-V-FX-071; PWR-A-017/018 **ACCEPTED_CONSTRAINT**; PWR-A-021…024 remain PROPOSED_CONSTRAINT; NOT VERIFIED retained; TBD-DK-007 BLOCKED retained.
* WP-007-R4: Method:Test cases enforce semantic placeholder policy (unjustified placeholders remaining = 0).
* EDL-014 meaning unchanged.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | Initial platform matrix |
| 1.2 | 2026-07-19 | WP-007 DevKit import |
| 1.3 | 2026-07-19 | WP-007-R1 taxonomy split |
| 1.3.1 | 2026-07-19 | WP-007-R1 regenerated after case ID restorations |
| 1.3.2 | 2026-07-19 | WP-007-R2 — TBD register authority note (no status changes) |
| 1.3.3 | 2026-07-19 | WP-007-R3 — D-015 split verification refs |
| 1.3.4 | 2026-07-19 | WP-007-R4 — placeholder audit note (no requirement status changes) |
| 1.4 | 2026-07-20 | Architecture Review — WP-007 traceability baseline ACCEPTED; requirement rows remain NOT VERIFIED |
| 1.5 | 2026-07-20 | WP-008 — add Accepted ADR-016…023 architecture references; statuses remain NOT VERIFIED |
| 1.5.1 | 2026-07-20 | WP-008-R1 — conditional open-load; ADR-023 REQ alignment; supply interruption DK-A/DK-D; NOT VERIFIED retained |
| 1.5.5 | 2026-07-20 | WP-009 Architecture Review Accepted — methods Accepted; numeric Open; NOT VERIFIED retained |
| 1.5.6 | 2026-07-20 | WP-010 — functional electrical architecture Proposed; architecture refs; NOT VERIFIED retained |
| 1.5.7 | 2026-07-20 | WP-010 Architecture Review Accepted — functional architecture Accepted; NOT VERIFIED retained |
| 1.5.8 | 2026-07-20 | WP-011 — EDL-011 proposal + component-class refs; NOT VERIFIED retained |
| 1.5.9 | 2026-07-20 | WP-011-R1 — disposition separation; evaluation-class terminology; NOT VERIFIED retained |
| 1.6.0 | 2026-07-20 | WP-011 Architecture Review Accepted — TBD-DK-007 BLOCKED retained; NOT VERIFIED retained |
| 1.6.1 | 2026-07-20 | WP-012 — electrical sizing framework refs; NOT VERIFIED retained |
| 1.6.2 | 2026-07-20 | WP-012-R1 — iterative closure; measurement boundaries; NOT VERIFIED retained |
| 1.6.3 | 2026-07-20 | WP-012-R2 corrections; WP-012 Architecture Review Accepted — NOT VERIFIED retained; TBD-DK-007 BLOCKED retained |
| 1.6.4 | 2026-07-20 | WP-013 — class qualification refs Proposed; NOT VERIFIED retained; TBD-DK-007 BLOCKED retained |
| 1.6.5 | 2026-07-20 | WP-013 Architecture Review Accepted — methodology Accepted; final classes Open; NOT VERIFIED retained; TBD-DK-007 BLOCKED retained |
| 1.6.6 | 2026-07-20 | WP-014 — REQ-DCC-V-FX-* matrix (Proposed); NOT VERIFIED; TBD-DK-007 BLOCKED retained |
| 1.6.7 | 2026-07-20 | WP-014-R1 — FX-005/071; PWR-A-017/018 Accepted disposition notes; NOT VERIFIED retained |
| 1.6.8 | 2026-07-20 | WP-014 Architecture Acceptance — package Accepted; REQ-DCC-V-FX-* NOT VERIFIED retained; TBD-DK-007 BLOCKED retained |
| 1.6.9 | 2026-07-20 | WP-014 PR #18 merged (`7c72181` / `e46aff4`) — acceptance metadata on main |
