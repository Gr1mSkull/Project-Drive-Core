# DriveCore Gen1 DevKit — Document Set

**Document ID:** DOC-DK-INDEX-001  
**Version:** 1.2  
**Status:** Accepted  
**Work Package:** WP-007 / WP-007-R1  
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
| [DevKit_System_Requirements.md](DevKit_System_Requirements.md) | Normative **system** requirements (`REQ-DCC-V-DK-NNN`) | Accepted |
| [DevKit_Verification_Governance.md](DevKit_Verification_Governance.md) | Evidence/claim/gate process rules (`DK-GOV-NNN`) | Accepted |
| [DevKit_Interface_Matrix.md](DevKit_Interface_Matrix.md) | Interface boundaries and testability | Accepted |
| [DevKit_Verification_Plan.md](DevKit_Verification_Plan.md) | Phase A–D + governance inspection; gates DK-A…DK-D | Accepted |
| [DevKit_Current_State_Gap_Assessment.md](DevKit_Current_State_Gap_Assessment.md) | Audit of existing claims vs baseline | Accepted |
| [DevKit_P0_Decision_Crosswalk.md](DevKit_P0_Decision_Crosswalk.md) | WP-008 P0 Proposed ADR-016…023 crosswalk | Proposed |
| This README | Navigation and authority statement | Accepted |

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
| Production fidelity | Exact “identical board / same binary” rules: Proposed ADR-016…018 (originating ADR-DK-001…003) — **not Accepted** until Architecture Review |
| Power domain | Representative capability for laboratory verification; not full production channel population by default |
| Acceptance | DevKit ≠ DCC Gen1 product acceptance |

## Relationship to `docs/008`

`docs/008_Testing_and_Validation.md` remains the **system-level validation strategy** (Phase A–F overview) and navigates here for detailed DevKit requirements and Phase A–D verification cases.

After WP-007, `docs/008` is **not** a competing normative source for detailed DevKit test cases.

## Relationship to ADR-015 / STD-REV-001

Every DevKit gate evidence package shall record a **composite system baseline** per Approved `STD-REV-001` (ADR-015 Accepted). Incomplete applicable identity ⇒ gate outcome `BLOCKED` or `NOT ASSESSED` (not `PASS`).

## Related records

| Record | Path |
|--------|------|
| CIA (WP-007) | [`docs/records/change_impact/CIA-2026-002_wp007-devkit-requirements.md`](../records/change_impact/CIA-2026-002_wp007-devkit-requirements.md) |
| CIA (WP-008) | [`docs/records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md`](../records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md) |
| Review Handoff (WP-007) | [`docs/records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md`](../records/review_handoffs/RHP-2026-001_wp007-devkit-requirements.md) |
| Review Handoff (WP-008) | [`docs/records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md`](../records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md) |
| P0 ADR package | [`docs/ADR/README.md`](../ADR/README.md) — ADR-016…023 Proposed |
| Traceability | [`docs/traceability/TRACEABILITY_MATRIX.md`](../traceability/TRACEABILITY_MATRIX.md) |
| SRS pointer | [`docs/SRS/Volume_2_DCC.md`](../SRS/Volume_2_DCC.md) §8.1 |

## Current status

| Item | Status |
|------|--------|
| Requirements baseline | **Accepted** — Architecture Review (2026-07-20); verification evidence still NOT VERIFIED |
| Governance rules | **Accepted** (`DK-GOV-*`) |
| Verification plan | **Accepted** (structure) — cases NOT EXECUTED / BLOCKED; no PASS claims |
| Hardware design | Not approved by WP-007 |
| Firmware bring-up | NOT IMPLEMENTED |
| Physical verification | NOT VERIFIED |
| Filled VE records | None (WP-007 creates none) |

## Known blocking decisions

P0 decision **requests** ADR-DK-001…007 and ADR-DK-010 now have canonical **Proposed** ADRs ADR-016…023 (WP-008). They remain **not Accepted**.

Still open without WP-008 ADR files: `ADR-DK-008`, `ADR-DK-009`, `ADR-DK-011`, `ADR-DK-012`.

Open thresholds: `TBD-DK-001` … `TBD-DK-022` (Status Open — WP-008 does not resolve numerics).

Hardware design remains **not** approved.

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-19 | WP-007 DevKit document set |
| 1.1 | 2026-07-19 | WP-007-R1 — governance document; taxonomy/gate corrections |
| 1.1.1 | 2026-07-19 | WP-007-R1 — identity gate language aligned (no PARTIAL PASS) |
| 1.2 | 2026-07-20 | Architecture Review — ACCEPTED; PR #11 approved for merge (requirements structure, governance, verification-plan structure, traceability baseline) |
| 1.3 | 2026-07-20 | WP-008 — P0 Proposed ADR package navigation (ADR-016…023); CIA-2026-003 / RHP-2026-002 |
