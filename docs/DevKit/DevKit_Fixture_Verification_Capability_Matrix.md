# DevKit Fixture Verification Capability Matrix — WP-014

**Document ID:** DOC-DK-FVCM-001  
**Version:** 1.1  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Capability mapping only — no PASS, no VE, cases remain NOT EXECUTED / BLOCKED.
```

## 1. Matrix (representative — not exhaustive of all 93 REQs)

| Requirement / case | Required fixture capability | Load/fault class | Energy domain | Measurement points | Safety interlocks | Missing inputs | Readiness | Future evidence scope |
|--------------------|----------------------------|------------------|---------------|--------------------|-------------------|----------------|-----------|----------------------|
| REQ-DCC-V-DK-039…041 (HS base/PWM) | Base source + load | RESISTIVE/PWM | Base | ENTRY, LOAD, CH | AUTH_BASE; E-stop | ED-IN-002/010/026 | PARTIAL | Base-envelope |
| REQ-DCC-V-DK-042 (BI) | BI load + direction | MOTOR_BI / STALL | Base | CH-BI, ENTRY | AUTH_*; BI interlock | OI-BI-001; OI-FIX-002 | BLOCKED_BY_ARCHITECTURE | Base |
| REQ-DCC-V-DK-043 (sense) | Observation access | — | Base | CH-IN/LOAD | — | ED-IN-011/032; OI-SENSE-001 | BLOCKED_BY_MEASUREMENT | Base |
| REQ-DCC-V-DK-044…049 (protect) | Fault inject OC/SC | OVER/SHORT | Base | Fault MPs | AUTH_FAULT; E-stop | OI-SC-001; bounds | BLOCKED_BY_FIXTURE_DESIGN | Base |
| VER-DCC-DK-A-011 | WD stimulus | — | Base/Aux | — | AUTH_FAULT | Fixture design | BLOCKED_BY_FIXTURE_DESIGN | Base |
| VER-DCC-DK-A-012/014 | KILL fixture | KILL assert | Base | KILL-* | E-stop ≠ KILL | — | REQUIREMENT_DEFINED | Base |
| VER-DCC-DK-C-002/003 | Loads multi/single | RESISTIVE | Base | ENTRY/LOAD | AUTH_BASE | TBD-DK-003 | PARTIAL | Base |
| VER-DCC-DK-C-005 | OC fixture | OVERLOAD | Base | Fault | AUTH_FAULT | Energy bound | PARTIAL | Base |
| VER-DCC-DK-C-006 | Safe short | SHORT | Base | Fault | AUTH_FAULT; backup | OI-SC-001 | BLOCKED_BY_FIXTURE_DESIGN | Base |
| VER-DCC-DK-C-007 | Open-load | OPEN | Base | V open | Conditional claim | PWR-A-010 | PARTIAL | Base |
| VER-DCC-DK-C-008 | UV | UV boundary | Base | ENTRY-V | Source AUTH | UV TBD | PARTIAL | Base |
| VER-DCC-DK-C-009 | Thermal load | Continuous | Base | Temp class Open | Thermal inhibit | ADR-DK-011 | BLOCKED_BY_ARCHITECTURE | Base |
| VER-DCC-DK-C-012 | J_LP disconnect | Control-loss | Base | JLP | AUTH_FAULT | TBD-DK-007 | BLOCKED_BY_THRESHOLD | Base |
| VER-DCC-DK-C-013 | Stall | STALL | Base | BI MPs | AUTH_FAULT | OI-FIX-002; TBD-DK-022 | BLOCKED_BY_FIXTURE_DESIGN | Base |
| VER-DCC-DK-C-014 | Recoverable inject | Fault | Base | Fault | LOCKOUT recovery | Sequence design | PARTIAL | Base |
| ADR-020 HC discovery | EXT path | EXT load/module | External | EXT MPs | AUTH_EXT; back-feed | OI-FIX-001; OI-GND-001 | BLOCKED_BY_ARCHITECTURE | External-source / module |
| ADR-023 methods | Fault governance | Catalog §3 | Declared | Fault MPs | Default inhibit | Bounds | PARTIAL | Per envelope |
| DK-GOV evidence rules | Envelope-tagged VE | — | Declared | Envelope ID | — | — | REQUIREMENT_DEFINED | Per scope |
| REQ-DCC-V-FX-010…015 | E-stop/KILL/AUTH | — | All fixture | ESTOP/KILL/AUTH | Principles § | — | REQUIREMENT_DEFINED | Fixture safety |
| REQ-DCC-V-FX-071 | E-stop path integrity (design allocation) | — | All fixture | ESTOP integrity | AUTH inhibit if unconfirmed | Fault-tolerance allocation Open | BLOCKED_BY_ARCHITECTURE (prelim design) | Fixture design |
| REQ-DCC-V-FX-005 / P6 | EXTERNAL_ENERGY_ARMED auth-only; EXT energize | EXT classes | External | EXT | Back-feed; no simultaneous BASE+EXT while OI-GND Open | OI-GND-001 | BLOCKED_BY_ARCHITECTURE | External-* (defined only) |
| REQ-DCC-V-FX-030…034 | Ext domains | EXT classes | External | EXT | Back-feed | OI-GND-001 | BLOCKED_BY_ARCHITECTURE | External-* |
| P0–P6 profiles | Profile map | Per catalog | Per P | Per profile | State model | Numerics Open; P6 combined BLOCKED | PARTIAL | Per envelope |

## 2. Readiness legend

`REQUIREMENT_DEFINED` · `PARTIAL` · `BLOCKED_BY_ARCHITECTURE` · `BLOCKED_BY_THRESHOLD` · `BLOCKED_BY_FIXTURE_DESIGN` · `BLOCKED_BY_MEASUREMENT` · `NOT_READY`

## 3. Explicit non-claims

No case PASS. No requirement Verified. No VE created.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture verification capability matrix — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — FX-005/071 readiness; E-stop design blocked |
