# DevKit Measurement Point Register — WP-010

**Document ID:** DOC-DK-MPR-001  
**Version:** 1.1  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-010 / WP-010-R1 (Accepted)  
**Date:** 2026-07-20

Functional IDs only — **no physical test-pad designators**. Supports [`DevKit_Threshold_Measurement_Plan.md`](DevKit_Threshold_Measurement_Plan.md).

## 1. Measurement point register

| MP ID | Quantity | Domain | Reference | Expected instrument capability | Isolation requirement | Trigger suitable | Associated threshold | Verification cases | Accessibility | Future owner |
|-------|----------|--------|-----------|-------------------------------|----------------------|------------------|---------------------|-------------------|---------------|--------------|
| **MP-IN-V** | Input voltage | DOM-LAB-SUPPLY | LOGIC_GND / POWER return | DMM; scope; UV capture | Non-isolated | UV events; input interrupt | TBD-DK-001, 012 | VER-DCC-DK-A-002, A-003, C-012 | Accessible at input entry | Schematic WP |
| **MP-IN-I** | Input current | DOM-LAB-SUPPLY | Series or clamp | Ammeter; current probe | Non-isolated | Envelope certification | TBD-DK-002, 003 | VER-DCC-DK-A-002, C-002 | Accessible at input entry | Schematic WP |
| **MP-KILL-RAW** | Physical kill switch net (pre-conditioning) | DOM-HW-KILL | LOGIC_GND | DMM; scope | Safety-critical observe-only | Kill assert edge | TBD-DK-004 | VER-DCC-DK-A-012 | Accessible at kill entry | Logic/Power layout |
| **MP-KILL-COND** | Conditioned / direct hardware-effective kill state at Power disable authority | DOM-HW-KILL | LOGIC_GND | DMM; scope | Safety-critical | Post-conditioning; direct branch timing | TBD-DK-004 | VER-DCC-DK-A-012 | Power-side disable path | Power board layout |
| **MP-KILL-OBS** | Logic-observed kill state (observation branch only) | DOM-HW-KILL | LOGIC_GND | DMM; scope; diagnostic read | Observability — not safety path | Epoch invalidation; recovery FSM | TBD-DK-021 | VER-DCC-DK-A-012 | Logic input region | Logic board layout |
| **MP-GLOBAL-ENABLE** | `nENABLE_GLOBAL` — distinct from KILL | DOM-GLOBAL-EN | LOGIC_GND | DMM; scope | Control observe | Enable/disable edges | TBD-DK-004, 005 | VER-DCC-DK-A-012, A-013 | J_LP safety region | Logic board layout |
| **MP-JLP-CMD** | J_LP command transport activity (SPI) | DOM-PWR-CTRL | LOGIC_GND | Logic analyzer | Non-isolated | Comm loss start | TBD-DK-007 | VER-DCC-DK-A-008, C-012 | Debug/header access | FW + layout |
| **MP-JLP-FAULT** | Aggregate fault indication | DOM-SENSE-DIAG | LOGIC_GND | DMM; scope | Open-drain observe | Fault events | TBD-DK-013 | VER-DCC-DK-C-005, C-006 | J_LP diagnostic region | Power board layout |
| **MP-CH-HS-VOUT** | HS channel output voltage / representative output safe-state result | DOM-HS-REP | BASE_LOAD_RETURN | DMM; scope | Channel-relative | OFF transition; decay; safe-state confirmation | TBD-DK-004, 014 | VER-DCC-DK-C-001, C-002 | Load terminal access | Power board layout |
| **MP-CH-HS-IOUT** | HS channel current | DOM-HS-REP | BASE_LOAD_RETURN | Ammeter; probe; diagnostic correlation | Non-isolated | OC; SC; envelope | TBD-DK-002, 009 | VER-DCC-DK-C-004, C-005, C-006 | Load path + sense tap | Power board layout |
| **MP-CH-BI-A** | BI terminal A voltage/current | DOM-BI-REP | BASE or EXT return | DMM; scope; ammeter | Ground/reference **Open** (OI-GND-001) | Direction conflict | Open | VER-DCC-DK-C-010 | BI terminal access | Power + fixture WP |
| **MP-CH-BI-B** | BI terminal B voltage/current | DOM-BI-REP | BASE or EXT return | DMM; scope; ammeter | Ground/reference **Open** (OI-GND-001) | Stall test | TBD-DK-022 | VER-DCC-DK-C-011 | BI terminal access | Power + fixture WP |
| **MP-LOGIC-RAIL** | Logic supply rail | DOM-LOGIC-PWR | LOGIC_GND | DMM | Non-isolated | Brownout; UV | TBD-DK-017 | VER-DCC-DK-A-003 | Logic board TP | Logic board layout |
| **MP-RADIO-RAIL** | Radio supply rail | DOM-RADIO | RADIO_GND | DMM | Non-isolated | Service reset | TBD-DK-017 | VER-DCC-DK-A-005, D-012 | Radio board TP | Radio board layout |
| **MP-POWER-CTRL-RAIL** | Power controller rail | DOM-PWR-CTRL | POWER_CTRL_GND | DMM | Non-isolated | Controller reset | TBD-DK-017 | VER-DCC-DK-A-003 | Power board TP | Power board layout |
| **MP-LOAD-BASE-RETURN** | Base load return current | DOM-BENCH-LOAD | BASE_LOAD_RETURN | Current probe | High-current path | Simultaneous profile | TBD-DK-003 | VER-DCC-DK-C-002 | Return path access | Layout WP |
| **MP-LOAD-EXT-RETURN** | External bank return | DOM-EXT-BANK | `[Open]` reference (OI-GND-001) | Current probe | Ground/reference **Open** | P6 envelope | TBD-DK-002 | Phase E / fixture | Fixture-defined | Fixture WP |

## 2. KILL measurement distinction (WP-010-R1)

| MP | Measures | Safety authority |
|----|----------|------------------|
| MP-KILL-RAW | Physical operator kill input | Observe only |
| MP-KILL-COND | Direct hardware-effective disable state at Power | **Safety-critical** timing path |
| MP-KILL-OBS | Logic observation branch | Diagnostic / recovery only — failure does not block direct branch |
| MP-GLOBAL-ENABLE | Logic-controlled enable — **distinct** from KILL | Control path |
| MP-CH-HS-VOUT | Representative output safe-state result | Verification end condition |

## 3. WP-009 measurement plan alignment

| WP-009 measurement | MP IDs |
|--------------------|--------|
| Kill response budget | MP-KILL-RAW, MP-KILL-COND, MP-KILL-OBS, MP-GLOBAL-ENABLE, MP-CH-HS-VOUT, MP-CH-HS-IOUT |
| Watchdog budget | MP-GLOBAL-ENABLE, MP-CH-HS-VOUT |
| Control-loss budget | MP-JLP-CMD, MP-GLOBAL-ENABLE, MP-CH-HS-VOUT |
| Commanded OFF budget | MP-JLP-CMD, MP-CH-HS-VOUT, MP-CH-HS-IOUT |
| Continuous envelope | MP-IN-I, MP-CH-HS-IOUT, MP-LOAD-BASE-RETURN |
| Simultaneous profile | MP-IN-I, multiple MP-CH-HS-IOUT |
| OC/SC fault | MP-CH-HS-IOUT, MP-JLP-FAULT |

## 4. Timestamp correlation

| Source | Use |
|--------|-----|
| Bench instrument | Authoritative for hardware timing |
| Logic diagnostic timestamp | Correlation only — future FW WP |
| CAN timestamp | Not used for kill timing (ADR-022) |

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial measurement point register — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — MP-KILL-OBS; KILL/global distinction; diagnostic topology language |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #14 merged (`c98ce56`) |
