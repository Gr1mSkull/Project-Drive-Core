# DevKit Power Domain Matrix — WP-010

**Document ID:** DOC-DK-PDM-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010  
**Date:** 2026-07-20

Symbolic rails only — **no voltage values Approved**.

## 1. Power domain matrix

| Domain | Source | Nominal voltage symbol | Enabled by | Disabled by | Safe state | Isolation relation | Back-feed risk | Measurement points | Numeric status |
|--------|--------|------------------------|------------|-------------|------------|--------------------|----------------|--------------------|----------------|
| **DOM-LAB-SUPPLY** | External PSU | `V_IN` | Operator connects PSU | Operator disconnect; OCP trip | OFF — no energy | External to DevKit | N/A — source | MP-IN-V, MP-IN-I | TBD-DK-001 Open |
| **DOM-INPUT-PROTECT** | Upstream `V_IN` | `V_IN` | Upstream present; protection intact | Fuse/device open; operator replace | Open circuit — no downstream energy | Inline series | None downstream when open | MP-IN-V, MP-IN-I | TBD-DK-002 Open |
| **DOM-INPUT-DIST** | Post-protection `V_IN` | `V_IN` | Protection closed | Protection open; UV shutdown | De-energized | Non-isolated internal | Low if protection intact | MP-IN-V | Open |
| **DOM-LOGIC-PWR** | `V_IN` via local DC-DC | `V_LOGIC` | `V_IN` above UV threshold | `V_IN` removed; UV; Logic reset | OFF — RT stopped | Single-point GND with Radio | None | MP-LOGIC-RAIL | TBD-DK-017 Open |
| **DOM-RADIO** | `V_IN` via local regulation | `V_RADIO` | `V_IN` present | `V_IN` removed; Radio reset | Service unavailable; RT unaffected | GND single-point with Logic | None to power outputs | MP-RADIO-RAIL | TBD-DK-017 Open |
| **DOM-PWR-CTRL** | `V_IN` distributed | `V_POWER_CTRL` | `V_IN` present; controller awake | UV; reset; kill; global disable | All channels OFF | Common return with load domain | None if kill effective | MP-POWER-CTRL-RAIL | Open |
| **DOM-HS-REP** | `V_IN` switched | `V_LOAD_BASE` | Channel command + global enable + kill released | KILL; global disable; control-loss; local fault | Channel OFF | Return via BASE_LOAD_RETURN | None to input if switch OFF | MP-CH-HS-VOUT, MP-CH-HS-IOUT | TBD-DK-002/009 Open |
| **DOM-BI-REP** | `V_IN` bidirectional | `V_LOAD_BASE` / `V_LOAD_EXT` | Valid direction command + enables | Conflict; kill; fault; disable | Both directions OFF | `[Open]` ext return relation | **Open** — OI-GND-001 | MP-CH-BI-A, MP-CH-BI-B | Open |
| **DOM-SENSE-DIAG** | Derived from monitored domains | `V_SENSE_REF` | Domain energized | Domain OFF | Observability only | Referenced to LOGIC_GND | None | All MP-* sense points | TBD-DK-009/010 Open |
| **DOM-HW-KILL** | External switch + conditioning | Signal domain | Always observable when powered | N/A | Asserted = disable | Control signal — not power rail | None | MP-KILL-RAW, MP-KILL-COND | TBD-DK-004 Open |
| **DOM-GLOBAL-EN** | Logic GPIO | Enable signal | Logic drives active | Reset; kill; WD; comm loss | **Inactive = safe** | Control — AND with kill | None | MP-GLOBAL-ENABLE | Open |
| **DOM-EXT-BANK** | Fixture supply | `V_LOAD_EXT` | Fixture enable + procedure | E-stop; abort; KILL | OFF | **Open decision** — isolated vs shared | **High if miswired** — must block back-feed | MP-LOAD-EXT-RETURN, fixture MP | TBD-DK-002 Open |
| **DOM-BENCH-LOAD** | Channel output | `V_LOAD_BASE` | Channel ON | Channel OFF; kill | De-energized | BASE_LOAD_RETURN | None | MP-CH-HS-VOUT, MP-HS-IOUT | Open |
| **DOM-MEASURE** | Instrument reference | `MEASUREMENT_REFERENCE` | Test setup | Disconnect | N/A | Fixture-defined | Ground loop risk — procedure | All MP-* | Open |

## 2. Rail classification

| Rail symbol | Classification | Notes |
|-------------|----------------|-------|
| `V_IN` | conditionally enabled | Present when lab PSU connected |
| `V_LOGIC` | switched (regulator enable) | Always-on when `V_IN` valid — exact UV Open |
| `V_RADIO` | switched | Independent reset from Logic |
| `V_POWER_CTRL` | conditionally enabled | Follows input and controller state |
| `V_LOAD_BASE` | switched | Per-channel HS/BI switching |
| `V_LOAD_EXT` | fixture supplied | External bank only |
| `V_SENSE_REF` | always present when Logic powered | ADC reference domain |

## 3. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial power domain matrix — Proposed |
