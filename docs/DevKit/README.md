# DriveCore Gen1 DevKit — Document Set

**Document ID:** DOC-DK-INDEX-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-007  
**Date:** 2026-07-19

```text
The DevKit is a controlled verification platform.
It is not a reduced production DCC and not a substitute for DCC Gen1 acceptance.
```

## Purpose

This folder holds the **verification-ready Gen1 DevKit requirements baseline**, interface matrix, verification plan, and current-state gap assessment produced by WP-007.

It defines **what the DevKit must accomplish and how it will be verified**.  
It does **not** define the final circuit, PCB, component set, enclosure, or BOM.

## Document map

| Document | Authority role | Status |
|----------|----------------|--------|
| [DevKit_System_Requirements.md](DevKit_System_Requirements.md) | Normative atomic requirements (`REQ-DCC-V-DK-NNN`) | Proposed |
| [DevKit_Interface_Matrix.md](DevKit_Interface_Matrix.md) | Interface boundaries and testability | Proposed |
| [DevKit_Verification_Plan.md](DevKit_Verification_Plan.md) | Phase A–D cases and gates DK-A…DK-D | Proposed |
| [DevKit_Current_State_Gap_Assessment.md](DevKit_Current_State_Gap_Assessment.md) | Audit of existing claims vs baseline | Proposed |
| This README | Navigation and authority statement | Proposed |

## Relationship to EDL-014

**EDL-014** (Accepted): DCC Gen1 shall not be installed in the vehicle until Phase A–D are passed on DevKit and Phase E critical items are passed on full DCC Gen1.

WP-007 normalizes Phase A–D into gates **DK-A…DK-D**. Passing those gates:

* supports readiness for DCC Gen1 hardware/firmware progression;
* does **not** authorize vehicle installation;
* does **not** replace Phase E evidence.

## Relationship to DCC Gen1

| Topic | Statement |
|-------|-----------|
| Architecture family | Same three-board DCC concept (Logic + Power + Radio) — EDL-007 |
| Production fidelity | Exact “identical board / same binary” rules are **ARCHITECTURAL DECISION REQUIRED** (ADR-DK-001…003) |
| Power domain | Representative capability for laboratory verification; not full production channel population by default |
| Acceptance | DevKit ≠ DCC Gen1 product acceptance |

## Relationship to `docs/008`

`docs/008_Testing_and_Validation.md` remains the **system-level validation strategy** (Phase A–F overview) and navigates here for detailed DevKit requirements and Phase A–D verification cases.

After WP-007, `docs/008` is **not** a competing normative source for detailed DevKit test cases.

## Relationship to ADR-015 / STD-REV-001

Every DevKit gate evidence package shall record a **composite system baseline** per Approved `STD-REV-001` (ADR-015 Accepted). Incomplete identity ⇒ certification `NOT VERIFIED` or `PARTIAL`.

## Related records

| Record | Path |
|--------|------|
| CIA | [`docs/records/change_impact/CIA-2026-002_wp007-devkit-requirements.md`](../records/change_impact/CIA-2026-002_wp007-devkit-requirements.md) |
| Review Handoff | [`docs/records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md`](../records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md) |
| Traceability | [`docs/traceability/TRACEABILITY_MATRIX.md`](../traceability/TRACEABILITY_MATRIX.md) |
| SRS pointer | [`docs/SRS/Volume_2_DCC.md`](../SRS/Volume_2_DCC.md) §8.1 |

## Current status

| Item | Status |
|------|--------|
| Requirements baseline | Proposed — Architecture Review required |
| Verification plan | Proposed — no cases executed |
| Hardware design | Not approved by WP-007 |
| Firmware bring-up | NOT IMPLEMENTED |
| Physical verification | NOT VERIFIED |
| Filled VE records | None (WP-007 creates none) |

## Known blocking decisions

See requirements §6 and Architect Review Package:

`ADR-DK-001` … `ADR-DK-012`, plus open thresholds `TBD-DK-001` … `TBD-DK-022`.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 DevKit document set |
