# DevKit Fixture Dependency and Readiness Matrix — WP-014

**Document ID:** DOC-DK-FDRM-001  
**Version:** 1.3  
**Status:** Accepted — Architecture Review (2026-07-20)  
**Work Package:** WP-014  
**Date:** 2026-07-20

## 1. Matrix

| Fixture capability | Architecture dependency | Numeric dependency | Component-class dependency | Fixture-design dependency | Ground/reference dependency | Measurement dependency | Construction dependency | Blocks | Recommended next WP |
|--------------------|-------------------------|--------------------|----------------------------|---------------------------|-----------------------------|-------------------------|-------------------------|--------|---------------------|
| Base source control | ADR-021 | TBD-DK-001/002 | — | Design | — | ENTRY MPs | Construction | Energize tests | Fixture prelim design |
| External source control | ADR-020; OI-FIX-001; REQ-DCC-V-FX-005 | Ext ratings Open | — | Design | OI-GND-001 — simultaneous BASE+EXT blocked while Open | EXT MPs | Construction | HC discovery; combined BASE/EXT | Fixture prelim + OI-GND |
| Load-bank control | ADR-020/021 | Sink ratings Open | — | Design | OI-GND-001 | LB MPs | Construction | Load cases | Fixture prelim design |
| Ext power-module IF | ADR-020; OI-FIX-001 | Module ratings Open | WP-013 classes | Design | OI-GND-001 | Module MPs | Construction | HC path | Fixture prelim design |
| Fixture E-stop (requirements) | WP-014 Proposed | Timing Open | — | — | — | ESTOP MP | — | All hazardous AUTH | Architecture Review |
| Fixture E-stop (preliminary design) | REQ-DCC-V-FX-071; H-FX-008 | Timing Open | — | **BLOCKED_BY_ARCHITECTURE** (fault-tolerance / residual-risk allocation) | — | Integrity check Open | Construction | Physical E-stop verification | Architect + fixture prelim design |
| Fixture E-stop (physical verification) | Design Accepted | Timing Open | — | Design complete | — | Calibrated | Constructed fixture | Physical verification | NOT_READY |
| DUT physical KILL test | PWR-A-004; ADR-022 | TBD-DK-004 area | — | Design | — | KILL MPs | Construction | A-012/014 | Fixture prelim design |
| nENABLE_GLOBAL test | PWR-A-005 | — | — | Design | — | NEN MP | Construction | Enable cases | Fixture prelim design |
| Watchdog stimulus | ADR-022 | TBD-DK-005 | — | Design | — | — | Construction | A-011 | Fixture prelim design |
| Control-loss stimulus | EDL-011 Option D | TBD-DK-007 BLOCKED | — | Design | — | JLP | Construction | C-012 numeric | Threshold / optional EDL CR |
| PWM representative load | ADR-019 | ED-IN-010 | HS class Open | Design | — | I_RMS | Construction | PWM cases | Fixture + class |
| Current-observation verification | OI-SENSE-001 | ED-IN-011/032 | Sense class Open | Design | — | Sense MPs | Construction | C-004 | Sense decision |
| Channel overload | ADR-023 | Bounds Open | CH-PROT class | Design | — | Fault MPs | Construction | C-005 | Fixture design |
| Channel hard short | OI-SC-001 | ED-IN-021; TBD-DK-011 | CH-PROT | Design | — | Fault MPs | Construction | C-006 | Fixture design |
| Input interruption | — | — | — | Design | — | ENTRY | Construction | Interrupt cases | Fixture design |
| Undervoltage test | — | UV TBD | — | Design | — | ENTRY-V | Construction | C-008 | Threshold |
| Reverse-polarity test | OI-PROT-001 | — | RP class | Design | — | ENTRY | Construction | RP cases | Architect OI-PROT-001 |
| Transient test | OI-PROT-002 | Waveform Open | Transient class | Design | — | ENTRY | Construction | Transient | Architect OI-PROT-002 |
| Bidirectional operation | OI-BI-001 | — | BI class Open | Design | — | BI MPs | Construction | BI cases | Class + OI-BI |
| Bidirectional stall | OI-FIX-002 | TBD-DK-022 | BI class | Design | — | Stall MPs | Construction | C-013 | Fixture stall boundary |
| Returned-energy handling | OI-BI-001 | Absorption Open | — | Design | OI-GND-001 | Signed I | Construction | Regen profiles | Architect |
| Thermal soak | ADR-DK-011 | ED-IN-016/017 | — | Design | — | Temp | Construction | C-009 | ADR-DK-011 |
| Back-feed challenge | PWR-A-003 | — | — | Design | OI-GND-001 | Dual ENTRY | Construction | Safety | Architect GND |
| Measurement calibration | — | Accuracy Open | Sense class | Design | OI-GND-001 | All MPs | Construction | Dependent tests | Fixture + sense |
| Fixture identity | WP-014 | — | — | Design | — | ID | Construction | All hazardous | Fixture design |
| Fixture configuration | WP-014 | — | — | Design | — | Config | Construction | All hazardous | Fixture design |

## 2. Closure gates (summary)

| Before | Must close / accept |
|--------|---------------------|
| Fixture preliminary design | WP-014 Architecture Acceptance — **delivered by WP-015 (Proposed)**; see [`DevKit_Fixture_Implementation_Readiness_Matrix.md`](DevKit_Fixture_Implementation_Readiness_Matrix.md) |
| Fixture detailed design | WP-015 acceptance + OI-GND-001 / OI-PROT / E-stop decision packages |
| Fixture construction | Design review; E-stop; AUTH; back-feed; identity; residual energy; OI-GND if combined EXT | 
| Physical testing | Constructed fixture; measurement cal; applicable AUTH; no VE until executed |
| MPN selection | Separate qualification WP; not WP-014/WP-015 |

## 3. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture dependency and readiness matrix — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — E-stop readiness split; EXTERNAL_ENERGY_ARMED / OI-GND block |
| 1.2 | 2026-07-20 | Architecture Review **Accepted** (WP-014; reviewed head `084f579`, PR #18); Open decisions retained; NOT VERIFIED |
| 1.3 | 2026-07-20 | WP-015 — cross-reference to preliminary design + implementation readiness matrix; detailed-design gate added |
