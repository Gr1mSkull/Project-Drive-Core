# DevKit Electrical Design Input Register — WP-011

**Document ID:** DOC-DK-EDIR-001  
**Version:** 1.7  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-011  
**Date:** 2026-07-20

Controlled registry of electrical design inputs for future sizing and schematic WPs. **No invented values.** **No calculated limits.**

## 1. Register rules

| Rule | Statement |
|------|-----------|
| R1 | Every input has unique ID `ED-IN-NNN` |
| R2 | Status is **OPEN**, **BLOCKED**, or **Accepted** — only Architect/Accepted CR may set Accepted |
| R3 | Source shall reference TBD-DK-*, ADR, EDL, or Accepted architecture doc |
| R4 | WP-011 does **not** change TBD-DK register Status (remains Open) |
| R5 | Candidate values in docs/002, docs/008, yaml are **non-normative** unless Accepted elsewhere |
| R6 | **ED-IN entries are dependency references and are not approved design inputs.** |

## 2. Electrical design input register

| ID | Parameter | Symbol | Source | Status | Owner | Needed by | Closure WP |
|----|-----------|--------|--------|--------|-------|-----------|------------|
| **ED-IN-001** | Input voltage envelope | `V_IN` | TBD-DK-001 | OPEN | System Architect | Sizing; UV cases | Electrical sizing WP |
| **ED-IN-002** | Continuous current envelope (certified) | `I_certified_cont` | TBD-DK-002; ADR-021; WP-009 | OPEN | System Architect | Sizing; DK-A | Sizing + measurement |
| **ED-IN-003** | Simultaneous load profile | `I_simultaneous` | TBD-DK-003; WP-009 profile model | OPEN | System Architect | Multi-load DK-C | Sizing + P4 measurement |
| **ED-IN-004** | Kill response time | `T_KILL_MAX` | TBD-DK-004; ADR-022 | OPEN | System Architect | DK-A timing | Measurement WP |
| **ED-IN-005** | Watchdog response time | `T_WD_MAX` | TBD-DK-005; ADR-022 | OPEN | FW Architect | DK-A timing | FW BSP + measurement |
| **ED-IN-006** | Control-loss timeout | `T_CTRL_LOSS_MAX` | TBD-DK-007; EDL-011 proposal | **BLOCKED** | System Architect | DK-A/C comm-loss | WP-011 proposal + EDL CR + measurement |
| **ED-IN-007** | Commanded OFF time | `T_CMD_OFF_MAX` | TBD-DK-014; ADR-022 | OPEN | FW Architect | DK-A/C | FW BSP + measurement |
| **ED-IN-008** | Protection rating (≠ continuous) | `I_protection_rating` | TBD-DK-002; WP-009 L4 | OPEN | Implementation Engineer | Input protection sizing | Sizing WP |
| **ED-IN-009** | Fault / prospective SC envelope | `I_fault_peak` | WP-009 L14/15 | OPEN | Implementation Engineer | Protection coordination | Sizing WP |
| **ED-IN-010** | PWM frequency range | `f_PWM` | TBD-DK-008 | OPEN | System Architect | DK-C PWM | Component + sizing |
| **ED-IN-011** | Current measurement accuracy | `I_sense_accuracy` | TBD-DK-009 | OPEN | Component Engineer | DK-C-004 | Qualification WP |
| **ED-IN-012** | Temperature measurement accuracy | `T_sense_accuracy` | TBD-DK-010 | OPEN | Component Engineer | DK-C thermal | Qualification WP |
| **ED-IN-013** | UV threshold and reaction table | UV table | TBD-DK-012; OI-UV-001/002 | OPEN | System Architect | DK-C-012 | Sizing + Architect |
| **ED-IN-014** | Retry/latch policy | retry policy | TBD-DK-013 | OPEN | System Architect | DK-C-008 | FW + Architect |
| **ED-IN-015** | Rail voltage tolerances | `V_rail_tol` | TBD-DK-017 | OPEN | Implementation Engineer | DK-A rail tests | Sizing WP |
| **ED-IN-016** | Thermal test duration | `t_thermal_test` | TBD-DK-018 | OPEN | Test Engineer | DK-C thermal | ADR-DK-011 |
| **ED-IN-017** | Thermal limit / derating | thermal envelope | TBD-DK-018/019; ADR-DK-011 | OPEN | System Architect | Qualification | ADR-DK-011 + thermal WP |
| **ED-IN-018** | BOARD_ID encoding map | BOARD_ID map | TBD-DK-020 | OPEN | System Architect | DK-A-015 | Identity WP |
| **ED-IN-019** | Post-kill re-enable procedure | re-enable FSM | TBD-DK-021; WP-009 | OPEN (procedure Accepted) | FW Architect | DK-A kill cases | FW BSP WP |
| **ED-IN-020** | Stall-test fixture boundary | stall fixture | TBD-DK-022; WP-014 LFPC | OPEN | Test Engineer | DK-C-011; REQ-DCC-V-FX-053 | Fixture prelim design (after WP-014) |
| **ED-IN-021** | SC injection method | SC inject | TBD-DK-011; OI-SC-001; WP-014 fault catalog | OPEN | Test Engineer | DK-C SC; REQ-DCC-V-FX-053 | Fixture prelim design (after WP-014) |
| **ED-IN-022** | External load-bank envelope | `I_loadbank_limit` | ADR-020/021; WP-009 P6; WP-014 | OPEN | System Architect | Phase E / AUTH_LOAD_BANK | Fixture prelim design (after WP-014) |
| **ED-IN-023** | Ground/isolation base vs external | GND isolation | OI-GND-001; WP-010; WP-014 FESB | OPEN | System Architect | EXT interconnection (BLOCKED_BY_ARCHITECTURE) | Architect OI-GND-001 |
| **ED-IN-024** | Logic peak current | `I_LOGIC_PEAK` | WP-010 §19 | OPEN | Implementation Engineer | Power budget | Sizing WP |
| **ED-IN-025** | Radio peak current | `I_RADIO_PEAK` | WP-010 §19 | OPEN | Implementation Engineer | Power budget | Sizing WP |
| **ED-IN-026** | Representative channel continuous | `I_CHANNEL_CONT` | TBD-DK-002; ADR-019 | OPEN | Component Engineer | Switch class qual | Qualification WP |
| **ED-IN-027** | Channel inrush | `I_INRUSH` | TBD-DK-002 | OPEN | Implementation Engineer | Protection | Sizing WP |
| **ED-IN-028** | Connector/enclosure policy | connector class | ADR-DK-012 | OPEN | System Architect | Schematic | ADR-DK-012 |
| **ED-IN-029** | EDL-011 control-loss semantics | EDL-011 interpretation | WP-011 proposal | **BLOCKED** | System Architect | TBD-DK-007 | Architecture Review + optional EDL CR |
| **ED-IN-030** | Component class direction (HS) | HS class | WP-011 matrix; WP-013 HS comparison (methodology Accepted; final class Open) | OPEN | Component Engineer | Schematic auth | Architect class acceptance |
| **ED-IN-031** | Component class direction (BI) | BI class | WP-011 matrix; WP-013 BI comparison (methodology Accepted; final class Open) | OPEN | Component Engineer | Schematic auth | Architect class acceptance |
| **ED-IN-032** | Sense topology class | sense class | WP-011 matrix; WP-013 sense comparison (methodology Accepted; final class Open) | OPEN | Component Engineer | DK-C-004 | Architect class acceptance |
| **ED-IN-033** | Fixture identity / configuration policy | fixture ID/config | WP-014 REQ-DCC-V-FX-003/004 | OPEN | System Architect | Hazardous AUTH inhibit | Fixture prelim design + Architect |
| **ED-IN-034** | Fixture E-stop energy-removal timing bound | T_ESTOP_ENERGY | WP-014 FESB §6 | OPEN | System Architect | ENERGY_REMOVAL confirmation | Fixture design + measurement |
| **ED-IN-035** | Prospective fault-energy bounds (fixture-controlled) | E_FAULT_BOUND | WP-012; WP-014 REQ-DCC-V-FX-054/055 | OPEN | Test Engineer | AUTH_FAULT profiles | Fixture design (proven bounds only) |

## 3. Dependency graph (simplified)

```text
ED-IN-029 (EDL-011 semantics) ──blocks──► ED-IN-006 (T_CTRL_LOSS_MAX)
ED-IN-002 (I_certified_cont) ◄── constrains ── ED-IN-003, ED-IN-026
ED-IN-017 (thermal) ◄── ADR-DK-011
ED-IN-030/031/032 ◄── WP-011 class matrix ──► future schematic WP
```

## 4. Relationship to TBD-DK register

| Layer | Authority |
|-------|-----------|
| `TBD-DK-*` in `DevKit_System_Requirements.md` §4 | Authoritative threshold register — Status Open |
| `ED-IN-*` (this document) | Design-input view for sizing/schematic WPs — references TBD-DK-* |

WP-011 adds **ED-IN-029..032** as architecture-prep inputs; does **not** resolve TBD-DK entries.

## 4.1 TBD-DK-007 disposition separation (WP-011-R1)

| Dimension | Disposition |
|-----------|-------------|
| **Semantics** | **Accepted architecture interpretation** — Option D (WP-011 Accepted); EDL-011 file unchanged |
| **Numeric threshold** | **Open** — TBD-DK-007 register **BLOCKED_BY_EDL_CLARIFICATION** (not Resolved) |
| **Verification** | **Not Verified** — no VE records; VER-DCC-DK-A-008 / C-012 BLOCKED for numeric PASS |

```text
WP-011 Option D is an architectural interpretation only and does not modify EDL-011.
```

## 6. WP-012 sizing integration (Proposed)

WP-012 adds sizing-method references. **ED-IN entries remain dependency references (R6) — not frozen.**

| ED-IN | WP-012 sizing method | Required calculation | Closure readiness | Missing input | Downstream consumer |
|-------|---------------------|----------------------|-------------------|---------------|---------------------|
| ED-IN-001 | Input domain §4.1 | V_IN envelope | INPUTS_INCOMPLETE | TBD-DK-001 numeric | Sizing WP |
| ED-IN-002 | Budget §5; limit stack | I_certified_cont min() | BLOCKED_BY_THRESHOLD | L2–L13 terms | Component qual |
| ED-IN-003 | Profile P4; overlap | I_simultaneous peak/avg | BLOCKED_BY_THRESHOLD | Overlap profiles | DK-C P4 |
| ED-IN-006 | Protection P5; timing | T_CTRL_LOSS budget | BLOCKED | TBD-DK-007 numeric | DK-A-008 |
| ED-IN-008 | Protection P2 | I_protection vs I_certified | BLOCKED_BY_THRESHOLD | Protection class | Schematic WP |
| ED-IN-009 | E_FAULT model | Fault energy | INPUTS_INCOMPLETE | Injection fixture | Fixture WP |
| ED-IN-017 | Thermal framework | R_th / derating | BLOCKED_BY_ARCHITECTURE | ADR-DK-011 | Thermal WP |
| ED-IN-024/025 | Domain budget §4 | I_LOGIC/RADIO peaks | INPUTS_INCOMPLETE | Load analysis | Sizing WP |
| ED-IN-026/027 | Channel domain §4.5 | I_CHANNEL_CONT/inrush | BLOCKED_BY_THRESHOLD | Class + thermal | Qualification WP |
| ED-IN-030/031/032 | Evaluation readiness §2 | Class comparison | PARTIAL / NOT_READY | ED-IN-002, 017 | Qualification WP |

Full matrix: [`DevKit_Sizing_Dependency_and_Closure_Matrix.md`](DevKit_Sizing_Dependency_and_Closure_Matrix.md).

## 7. WP-014 fixture consumer integration

ED-IN-020…023, ED-IN-033…035 are consumed by Proposed WP-014 fixture requirements. **R6 retained:** ED-IN entries are dependency references and are **not** approved design inputs. No numeric values invented.

| Consumer | ED-IN | Notes |
|----------|-------|-------|
| EXT envelope / back-feed | ED-IN-022, ED-IN-023 | OI-GND-001 Open |
| Stall / SC injection | ED-IN-020, ED-IN-021 | OI-FIX-002 / OI-SC-001 Open |
| Fault-energy governance | ED-IN-009, ED-IN-035 | Bounds required before execution |
| Identity/config inhibit | ED-IN-033 | No retention policy Approved |
| E-stop residual energy | ED-IN-034 | Timing Open |

## 7.1 WP-015 preliminary-design consumers

WP-015 preliminary design references ED-IN entries as **dependency references (R6)** — not approved inputs. Fixture-relevant consumers: ED-IN-011/032 (sense topology/accuracy → measurement architecture), ED-IN-021 (SC injection → fault-injection), ED-IN-022 (external load-bank envelope → load-bank preliminary design), ED-IN-023 (base/external ground/isolation → OI-GND-001 option comparison), ED-IN-033…035 (fixture identity/config; E-stop energy-removal timing; fault-energy bounds). No numeric value invented; all remain OPEN/BLOCKED.

## 7.2 WP-016 detailed-design input linkage

WP-016 introduces a fixture **detailed-design input register** (`FX-DD-IN-*`, `DevKit_Fixture_Detailed_Design_Input_Register.md`) that references ED-IN entries as dependency references (R6 retained). ED-IN consumers: ED-IN-002/008/009 (source/protection envelopes → FX-DD-IN-011/020), ED-IN-011/012 (measurement accuracy → FX-DD-IN-018), ED-IN-016/017 (thermal → FX-DD-IN-017), ED-IN-021/022 (SC/load-bank → returned-energy/fault), ED-IN-028 (connector → FX-DD-IN-016). No numeric value Approved by WP-016.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-011 initial electrical design input register — Proposed |
| 1.1 | 2026-07-20 | WP-011-R1 — R6 dependency-reference rule; TBD-DK-007 disposition separation |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #15; TBD-DK-007 BLOCKED retained |
| 1.3 | 2026-07-20 | WP-012 — sizing method cross-reference (ED-IN not frozen) |
| 1.4 | 2026-07-20 | WP-013 — ED-IN-030/031/032 reference Proposed class comparisons (Status Open unchanged) |
| 1.5 | 2026-07-20 | WP-014 — fixture consumers; ED-IN-033…035 added (OPEN; no numerics); R6 retained |
| 1.6 | 2026-07-20 | WP-015 — preliminary-design consumers noted (R6 retained; no value changes) |
| 1.7 | 2026-07-21 | WP-016 — FX-DD-IN linkage (dependency references; R6 retained; no values Approved) |
