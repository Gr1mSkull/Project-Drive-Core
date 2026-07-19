# DriveCore Traceability Matrix

**Document ID:** DOC-TRACE-MAT-001  
**Version:** 1.2  
**Status:** Proposed  
**Change Request:** CR-002 / CR-002-R1 / CR-002-R2 · **Work Package:** WP-007

Controlled matrix. Do not invent historical links.

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` §6.

**Rules:**

- Primary matrix rows shall use **atomic** Requirement IDs only.
- Wildcard requirement families belong in § Requirement Families Pending Atomic Import — not in the primary matrix.
- Do not invent atomic requirements or verification links.
- Incomplete entries remain `NOT VERIFIED`.

## Coverage check (WP-007 DevKit)

```text
DevKit requirements with verification mapping: 100 %
DevKit requirements with implementation evidence: 0 %
Verified DevKit requirements: 0
```

## Primary matrix (atomic Requirement IDs)

| Requirement ID | Requirement Source | Architecture / Interface Reference | Implementation Artifact | Configuration / Data Artifact | Verification Method | Evidence Reference | Status | Notes |
| -------------- | ------------------ | ---------------------------------- | ----------------------- | ----------------------------- | ------------------- | ------------------ | ------ | ----- |
| REQ-DCC-V-DK-001 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-002 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-003 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-020 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-004 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Analysis: VER-DCC-DK-A-001, VER-DCC-DK-A-010 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-005 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-006 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-020 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-007 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Demonstration: VER-DCC-DK-A-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-008 | docs/DevKit/DevKit_System_Requirements.md | EDL-014; docs/DevKit/README.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-020 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-009 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-010, VER-DCC-DK-D-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-010 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-014, VER-DCC-DK-D-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-011 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test / Inspection: VER-DCC-DK-A-008 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-012 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-009, VER-DCC-DK-B-006 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-013 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis / Test: VER-DCC-DK-D-003, VER-DCC-DK-D-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-014 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis / Test: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-015 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-016 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-015, VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-017 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test / Inspection: VER-DCC-DK-A-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-018 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011; ADR-015; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-012, VER-DCC-DK-D-013 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-019 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Demonstration: VER-DCC-DK-A-002, VER-DCC-DK-A-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-020 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Analysis: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-021 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-022 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-023 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-003, VER-DCC-DK-A-014 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-024 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-025 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-026 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Demonstration: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-027 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-028 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis: VER-DCC-DK-A-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-029 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-030 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Interface_Matrix.md; safety policy | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Demonstration: VER-DCC-DK-A-003, VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-031 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-032 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test / Demonstration: VER-DCC-DK-A-013 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-033 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-034 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-035 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-008, VER-DCC-DK-C-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-036 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-037 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-012, VER-DCC-DK-B-013 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-038 | docs/DevKit/DevKit_System_Requirements.md | EDL-011; constitution safety | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-011 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-039 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-001, VER-DCC-DK-C-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-040 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-041 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-042 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-010, VER-DCC-DK-C-011 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-043 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-004 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-044 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-045 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-006 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-046 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-007 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-047 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-008 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-048 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-009 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-049 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-005, VER-DCC-DK-C-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-050 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-051 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-004, VER-DCC-DK-B-009 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-052 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Analysis: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-053 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-054 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-011 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-055 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/Power_Channel_Requirements.md (Proposed); DC-DCC-PWR-108 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-010 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-056 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-004 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-057 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-004 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-058 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-011 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-059 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-010 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-060 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-014 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-061 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-003, VER-DCC-DK-D-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-062 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-063 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-016 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-064 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-017 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-065 | docs/DevKit/DevKit_System_Requirements.md | docs/DCC/DCC_Internal_Architecture.md; docs/001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-066 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-067 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-006, VER-DCC-DK-B-007 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-068 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-007, VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-069 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-009 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-070 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-010 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-071 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-011 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-072 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-012 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-073 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-013 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-074 | docs/DevKit/DevKit_System_Requirements.md | EDL-002; EDL-010; docs/004; docs/006 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Test: VER-DCC-DK-B-014 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-075 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-076 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Test: VER-DCC-DK-B-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-077 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-078 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-004 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-079 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-080 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-014 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-081 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Demonstration: VER-DCC-DK-B-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-082 | docs/DevKit/DevKit_System_Requirements.md | EDL-008; EDL-012; docs/004 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-083 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-B-007, VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-084 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-085 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-086 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis / Test: VER-DCC-DK-D-003, VER-DCC-DK-D-005 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-087 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-088 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-089 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Test: VER-DCC-DK-B-007 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-090 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-091 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Test: VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-092 | docs/DevKit/DevKit_System_Requirements.md | docs/005; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-093 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-094 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-003 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-095 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-004 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-096 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-009 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-097 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-C-004, VER-DCC-DK-B-009 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-098 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Demonstration: VER-DCC-DK-B-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-099 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-B-008 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-100 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis / Test: VER-DCC-DK-C-005, VER-DCC-DK-C-006 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-101 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Test: VER-DCC-DK-A-014 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-102 | docs/DevKit/DevKit_System_Requirements.md | docs/DevKit/DevKit_Verification_Plan.md | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Demonstration: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-103 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-104 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-105 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-106 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-015 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-107 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-108 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-109 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-110 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-111 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-112 | docs/DevKit/DevKit_System_Requirements.md | ADR-015; STD-REV-001 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-113 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis / Inspection: VER-DCC-DK-A-008 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-114 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Analysis: VER-DCC-DK-A-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-115 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-A-002 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-116 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection: VER-DCC-DK-C-001 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-117 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Demonstration: VER-DCC-DK-A-001, VER-DCC-DK-D-019 | TBD | NOT VERIFIED | WP-007 import |
| REQ-DCC-V-DK-118 | docs/DevKit/DevKit_System_Requirements.md | EDL-007; EDL-011 | TBD | config/vehicles/devkit.yaml (profile scaffold) | Inspection / Demonstration: VER-DCC-DK-B-007, VER-DCC-DK-D-015 | TBD | NOT VERIFIED | WP-007 import |

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
| 1.2 | 2026-07-19 | WP-007 — import REQ-DCC-V-DK-001..118; all NOT VERIFIED |
