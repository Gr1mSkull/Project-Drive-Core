# DevKit P0 Decision Crosswalk — WP-008

**Document ID:** DOC-DK-P0-XWALK-001  
**Version:** 1.2  
**Status:** Accepted  
**Work Package:** WP-008 / WP-008-R1 (Accepted)  
**Date:** 2026-07-20

> Maps Accepted ADR-016…023 recommendations to requirements, cases, TBDs, and next Work Packages.  
> Architecture Review Accepted (2026-07-20). Evidence remains **NOT VERIFIED**. ADR-021/022 numerics remain **Open**.

## 1. Decision summary table

| Topic | ADR | Accepted decision | Requirements affected (primary) | Cases affected (primary) | TBDs affected | Next WP |
|-------|-----|----------------------------------|----------------------------------|--------------------------|---------------|---------|
| Logic fidelity | ADR-016 | Option D; Option B min for DK-A…DK-D; EDL-001 processor | 009, 011, 012, 017, 018, 102, 103 | A-007…A-017, B-006 | — (identity map later) | Electrical architecture; platform |
| Radio fidelity | ADR-017 | Option D; Option B min for DK-B/D Service/DCPI | 010, 012, 018, 102, 103 | A-005, A-009, B-006…B-015, D-012, D-013 | TBD-DK-006 (timing only) | Electrical; Radio qual; ADR-DK-008 |
| Firmware equivalence | ADR-018 | Option D lifecycle; Option B certification model | 013; DK-GOV-009/012 | A-006, A-017, D-019, G-003; Method:Test set | — | Platform/build system |
| Represented power capabilities | ADR-019 | Min capability set Option B (+ staged D); open-load CONDITIONAL_ON_DEVKIT | 005, 014, 039–055, 026 | C-001…C-014 (C-007 conditional), A-016 | Constrains 002/003/011/018/019/022 | Electrical architecture |
| Highest-current scope | ADR-020 | Option D: external discovery + Phase E confirm | 005, 014, 041 | C-001; C-005/006 scope notes | Constrains 002/003 | Fixture; Phase E plan |
| Input / simultaneous current | ADR-021 | Option B + D distinction; numerics Open | 020, 007, 030; DK-GOV-024/025 | A-002, A-003; multi-load C; G-004 | **002, 003** method; constrains 001/012/017/018/019 | Threshold analysis |
| Kill / watchdog timing | ADR-022 | Option D hierarchical fixed safety | 021, 031–038, 034, 035, 058 | A-011…A-014, C-012, B-013, D-012/013 | **004, 005, 007, 014, 021** | Threshold analysis |
| Fault injection / fixture boundary | ADR-023 | Gate-tiered Option B + method Option D; open-load CONDITIONAL_MANDATORY; supply interruption MANDATORY_DK_A + MANDATORY_DK_D | 017, 018, 023, 035, 038, 043–048, 054, 055, 058, 060, 067, 072, 073, 079, 080, 085, 087, 099, 100 (not 114) | A-003, A-008/009/011/015; B-003/008; C-005…014 (C-007 conditional); D-007/008/012…014/017 | 011, 022; energy notes | Fixture/load-bank reqs |

## 2. Dependency graph

```text
ADR-016 Logic fidelity
    → ADR-018 firmware equivalence
    → electrical architecture (Logic)
    → DK-A / DK-B readiness

ADR-017 Radio fidelity
    → ADR-018 firmware equivalence
    → electrical architecture (Radio)
    → DK-B / DK-D readiness
    → ADR-DK-008 (OTA) sequencing [not in P0 ADRs]

ADR-019 represented capabilities
    → ADR-020 highest-current scope
    → ADR-021 input-current architecture
    → fixture requirements (with ADR-023)
    → DK-C readiness

ADR-022 safety timing
    → kill/watchdog implementation planning
    → timing threshold closure WP
    → DK-A / DK-C readiness

ADR-023 fault injection scope
    → fixture/load-bank requirements
    → DK-B / DK-C / DK-D readiness
```

## 3. Circular dependency check

| Pair | Relationship | Circular? |
|------|--------------|-----------|
| ADR-016 ↔ ADR-018 | 016 constrains whether Option A binary is possible; 018 defines build model for 016 Option B | **No cycle** — one-way constraint with documented feedback note |
| ADR-019 → ADR-020 → ADR-021 | Capability set → HC location → envelope | **No cycle** |
| ADR-021 ↔ ADR-023 | Envelope constrains fixture energy; fixture may inform envelope evidence | **Soft coupling, not a logic cycle** — threshold WP closes numbers using both |
| ADR-022 ↔ ADR-023 | Timing paths measured under fixture supervision | **Soft coupling** — policy then measurement |
| ADR-017 ↔ ADR-DK-008 | Radio fidelity vs OTA scope | **No cycle** — 008 remains open, sequenced after P0 |

No hidden circular dependencies identified. Soft couplings shall be closed by threshold/fixture WPs without re-opening P0 architecture without a superseding ADR.

## 4. Blocker state after Proposed acceptance (hypothetical)

| Area | After P0 ADRs Accepted | Still blocked by |
|------|---------------------|------------------|
| Architecture direction | Architecture blocker reduced | — |
| Electrical design start | May be authorized by Architect as next WP | Implementation not started |
| Numeric thresholds | **Not** closed | Threshold WP; TBD Open |
| Fixtures | Boundary known | Fixture WP; implementation |
| Evidence | — | Remains NOT VERIFIED |

```text
Architecture blocker resolved (Accepted)
Implementation blocker remains
Fixture blocker remains
Threshold blocker remains
Evidence remains NOT VERIFIED
```

## 5. Out-of-package decisions (sequencing)

| Request | Topic | Proposed sequence |
|---------|-------|-------------------|
| ADR-DK-008 | OTA gate scope | After ADR-017/018 Accepted |
| ADR-DK-009 | Configuration hot-reload | After ADR-018; with config WP |
| ADR-DK-011 | Environmental/thermal split | After ADR-019/021; with threshold/thermal analysis |
| ADR-DK-012 | Connector/enclosure candidates | After electrical architecture outline |

## 6. Related records

| Record | Path |
|--------|------|
| CIA | [`docs/records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md`](../records/change_impact/CIA-2026-003_wp008-devkit-p0-adrs.md) |
| RHP | [`docs/records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md`](../records/review_handoffs/RHP-2026-002_wp008-devkit-p0-adrs.md) |
| ADR index | [`docs/ADR/README.md`](../ADR/README.md) |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-008 initial crosswalk |
| 1.1 | 2026-07-20 | WP-008-R1 — open-load conditional; ADR-023 REQs without 114; supply interruption DK-A/DK-D |
| 1.2 | 2026-07-20 | Architecture Review — ADR-016…023 Accepted; WP-008 Accepted |
