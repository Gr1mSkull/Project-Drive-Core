# Change Impact Analysis

| Field | Value |
|-------|-------|
| **Change ID** | CIA-2026-009 |
| **Impact Level** | 2 — Full CIA |
| **Title** | WP-014 Gen1 DevKit Fixture and Load-Bank Requirements |
| **Author** | Implementation Engineer (cloud agent) |
| **Author role** | Implementation Engineer |
| **Date** | 2026-07-20 |
| **Status** | Draft — Under Architecture Review |
| **Related WP / CR** | WP-014; depends on WP-013 Accepted (`ee462fb`+); ADR-016…023 Accepted |

### Reason for Change

Accepted DevKit architecture, sizing, and class-evaluation packages lack controlled laboratory fixture and load-bank requirements. Future fixture design, procurement, construction, and physical verification require explicit energy domains, authorities, states, load/fault catalogs, measurement boundaries, and interlocks without selecting hardware or approving numerics.

### Impact Level Rationale (Level 2)

WP-014 defines requirements that will later constrain laboratory energy sources, fixture input protection, external load banks, fixture E-stop, controlled energization, fault-injection mechanisms, measurement boundaries, instrumentation interfaces, representative loads, external power modules, base versus external verification evidence, operator safety, fixture wiring, future fixture component qualification, future procurement, fixture construction, and physical verification.

### Current Behaviour

* ADR-020/021/023 define external vs base and fault-injection principles; no fixture requirements package.
* OI-FIX-001/002, OI-SC-001, OI-GND-001 Open.
* VER-DCC-DK-* fixture-dependent cases BLOCKED.
* No REQ-DCC-V-FX-* identifiers existed.

### Proposed Behaviour

* Proposed fixture functional architecture, energy/safety boundary, FX requirements, load/fault catalog, interface/measurement register, hazard/interlock register, verification capability matrix, dependency/readiness matrix.
* Distinct fixture E-stop vs DUT KILL vs nENABLE_GLOBAL.
* P0–P6 mapped without numeric currents.
* All FX requirements remain PROPOSED until Architecture Review.

### Scope exclusions (mandatory)

```text
No fixture MPN selected.
No DevKit MPN selected.
No BOM created.
No numeric threshold approved.
No fixture constructed.
No hardware energized.
No physical verification performed.
No VE created.
```

### Affected Requirements

| ID | Impact |
|----|--------|
| REQ-DCC-V-FX-001…070 (new) | Proposed — NOT VERIFIED |
| REQ-DCC-V-DK-* (consumers) | Fixture capability mapping — NOT VERIFIED unchanged |
| DK-GOV-* | Evidence envelope tagging alignment — NOT VERIFIED unchanged |
| VER-DCC-DK-A/C-* fixture-blocked | Mapping — remain NOT EXECUTED / BLOCKED |
| TBD-DK-001…022 | Remain Open |
| TBD-DK-007 | BLOCKED_BY_EDL_CLARIFICATION retained |

### Affected Verification Cases

Fixture-dependent cases (examples A-011/012/014; C-002…014) gain capability mapping only. Status remains **NOT EXECUTED / BLOCKED**. No PASS.

### Affected Interfaces / Energy Domains

IF-FX-*; BASE-SOURCE; EXT-SOURCE; EXT-LOAD-BANK; EXT-POWER-MODULE; FIXTURE-AUX; DUT KILL/ENABLE.

### Safety Impact

| Area | Impact |
|------|--------|
| Fixture E-stop | Proposed requirements |
| DUT KILL | Preserved independent |
| nENABLE_GLOBAL | Preserved distinct |
| Back-feed | Mandatory prohibit |
| OI-GND-001 | Remains Open — no isolation claim |
| Numerics | All Open |

### Traceability Impact

`TRACEABILITY_MATRIX.md` adds REQ-DCC-V-FX-* section; statuses NOT VERIFIED; no VE.

### Downstream Impact

| Stage | Impact of WP-014 alone |
|-------|------------------------|
| Fixture preliminary design | Constrained if Architect accepts WP-014 |
| Fixture procurement | Not authorized |
| Fixture construction | Not authorized |
| Physical verification | Not authorized |
| DevKit MPN / BOM / schematic / PCB | Not authorized |

### Non-impact (explicit)

No current hardware, firmware, or configuration implementation change. No EDL file change. No Accepted ADR content change. No numeric threshold Resolved. No component class becomes an MPN.

### Rollback

Revert WP-014 PR; WP-013 Accepted baseline (`ee462fb`) preserved.

### Unresolved Decisions

OI-GND-001 · OI-PROT-001/002 · OI-FIX-001/002 · OI-SC-001 · OI-COMP/SENSE/BI · ADR-DK-011/012 · TBD-DK-007 numeric · all FX still PROPOSED.

### Validation performed (WP-014 — reproducible)

#### V1 — Baseline ancestry

```bash
git merge-base --is-ancestor ee462fb3660dc0929b5c1a5b64d87b7655fdc357 HEAD
```

| Field | Value |
|-------|-------|
| stdout | *(empty)* |
| exit status | `0` |
| result | **PASS** — WP-013 acceptance commit is ancestor |

#### V2 — Forbidden paths

```bash
git diff --name-only main...HEAD -- docs/EDL docs/ADR hardware firmware config
```

| Field | Value |
|-------|-------|
| stdout | *(empty)* |
| exit status | `0` |
| result | **PASS** — no forbidden paths |

#### V3 — MPN / ratings / numeric approval patterns

```bash
rg -i 'MPN:|preferred manufacturer|BOM entry|approved (current|voltage|timing|temperature)|fuse rating [0-9]|breaker [0-9]' \
  docs/DevKit/DevKit_Fixture*.md docs/DevKit/DevKit_Load_and_Fault_Profile_Catalog.md \
  docs/DevKit/DevKit_Fixture_and_Load_Bank_Requirements.md
```

| Field | Value |
|-------|-------|
| stdout | *(empty — rg no-match)* |
| exit status | `1` |
| result | **PASS** — no selection/approval patterns |

#### V4 — TBD-DK-007 / OI-GND retention

```bash
rg 'BLOCKED_BY_EDL_CLARIFICATION' docs/DevKit/DevKit_Sizing_Dependency_and_Closure_Matrix.md docs/DevKit/DevKit_Electrical_Design_Input_Register.md
rg 'OI-GND-001' docs/DevKit/DevKit_Fixture_Energy_and_Safety_Boundary.md
```

| Field | Value |
|-------|-------|
| exit status | `0` (both) |
| result | **PASS** — blocker and Open GND retained |

#### V5 — Deliverables present

Eight DevKit fixture docs + CIA-2026-009 + RHP-2026-008.

| result | **PASS** |

#### V6 — Markdown relative links (WP-014 set)

```text
OK: 11 files, 61 relative links verified
exit status 0
```

| result | **PASS** |

#### V7 — Requirement Verified / case PASS / VE

| Check | Result |
|-------|--------|
| Requirement Verified claims in WP-014 package | Spot-check — no Verified claims (**PASS** for absence) |
| Verification case PASS | No PASS introduced (**PASS** for absence) |
| VE records created | **PASS** — no WP-014 VE created |
| Physical tests | **NOT EXECUTED** |

### Validation Required

Architecture Review. No physical tests.

### Approvals

| Field | Value |
|-------|-------|
| **ADR Required** | NO (may drive future ADR-DK) |
| **Architect Approval Required** | YES |
| **Architect approver** | TBD |
| **Architect approval date** | TBD |

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial CIA — Draft |
| 1.1 | 2026-07-20 | Reproducible validation evidence; Level 2 rationale expanded |
