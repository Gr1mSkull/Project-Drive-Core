# DevKit Fixture Preliminary Safety Allocation Matrix — WP-016

**Document ID:** DOC-DK-FPSAM-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-016  
**Date:** 2026-07-21

```text
Proposed safety allocations only. No allocation is marked demonstrated; no proof is claimed where none exists.
Status legend: PROPOSED_ALLOCATION · BLOCKED_BY_ARCHITECTURE · BLOCKED_BY_INPUT · BLOCKED_BY_DETAILED_DESIGN.
```

## 1. Allocation matrix

| Hazard | Initiating event | Energy source | Preventive function | Safety-effective function | Observation | Backup function | Safe minimum | Recovery guard | Proposed status | Proof artifact |
|--------|------------------|---------------|---------------------|---------------------------|-------------|-----------------|--------------|----------------|-----------------|----------------|
| Unexpected base energization | Spurious AUTH_BASE | BASE-SOURCE | AUTH default inactive; identity/config gate | E-stop inhibit [S] | AUTH/source-state observe | Energy removal | SAFE_OFF/de-energized | New epoch from LOCKOUT_SAFE | PROPOSED_ALLOCATION | E-stop integrity + energy-removal proof |
| Unexpected external energization | Spurious AUTH_EXT | EXT-SOURCE | AUTH_EXT inactive; base/ext exclusivity | E-stop inhibit [S] | Ext enable/state observe | Independent ext removal | Ext off | Deliberate arm | BLOCKED_BY_ARCHITECTURE | OI-GND-001 disposition |
| Simultaneous BASE+EXT | Dual AUTH grant | BASE+EXT | Mutual-exclusion interlock [A] | Inhibit second while first active | Both-envelope observe | E-stop inhibit | Inhibit both | Architect disposition | BLOCKED_BY_ARCHITECTURE | OI-GND-001 |
| External-to-base back-feed | Wrong interconnection | EXT→BASE | Back-feed-prevention function (P1/P2) | Disconnect/inhibit [S] | Ext/base current observe | External/upstream removal | No uncontrolled base energization | Confirm before recovery | BLOCKED_BY_ARCHITECTURE | OI-GND-001; OI-PROT-001; back-feed evidence |
| E-stop path failure | Path fault/integrity loss | Any fixture-controlled | Integrity monitoring | Inhibit hazardous AUTH if unconfirmed [S] | E-stop integrity observe | Independent removal | AUTH inhibited | Integrity confirmed | BLOCKED_BY_ARCHITECTURE | E-stop topology + proof test (REQ-DCC-V-FX-071) |
| Source-control stuck ON | Control fault | BASE/EXT source | Independent energy removal | Energy-removal path [S] | Command-vs-observed | E-stop | De-energize | Confirm removal | BLOCKED_BY_DETAILED_DESIGN | Energy-removal design + proof |
| Load-bank stuck ON | Control/switch fault | Upstream source | Revoke AUTH_LOAD_BANK | Upstream inhibit/remove [S] | Load command-vs-observed | E-stop | Upstream energy removed | LOCKOUT_SAFE after confirm | BLOCKED_BY_DETAILED_DESIGN | Upstream containment design |
| Returned-energy overvoltage | Regenerative return | DUT/bridge | Gen1 regen prohibited (policy D) | Exclusion interlock [A]/[S] | Signed-I observe | Removal | No regen commanded | Confirm | BLOCKED_BY_ARCHITECTURE | OI-BI-001; exclusion interlock proof |
| Measurement-reference fault | Reference error | Measurement path | Reference boundary req | Block dependent test [C/A] | Plausibility/reference observe | Inhibit AUTH | No energy if required MP absent | Fix + confirm | BLOCKED_BY_ARCHITECTURE | OI-GND-001; OI-SENSE-001 |
| Measurement-input short | Probe/input fault | Measurement conductor | Input limiting/protection req | Contain via limiting [S/design] | Fault observe | Inhibit | High-Z/safe on fail | Fix + confirm | BLOCKED_BY_DETAILED_DESIGN | Input-limiting/protection design |
| Residual stored energy | Post-removal residual | L/C stored | Discharge function | Hold LOCKOUT_UNCONFIRMED [C] | Residual observe | Bleed/discharge | Recovery prohibited until confirmed | DISCHARGE_COMPLETE | BLOCKED_BY_DETAILED_DESIGN | Discharge design + timing (Open) |
| Failed discharge | Discharge fault | Residual energy | Residual observation | Hold LOCKOUT_UNCONFIRMED [C] | Residual observe | Manual procedure | Recovery prohibited | Confirm safe decay | BLOCKED_BY_DETAILED_DESIGN | Discharge proof |
| Unauthorized fault injection | Spurious AUTH_FAULT | Fault path | AUTH_FAULT default inhibited | E-stop inhibit [S] | Fault-state observe | Removal + lockout | Inhibited | Deliberate recovery | PROPOSED_ALLOCATION | ADR-023 alignment; fault design |
| Loss of interlock controller | Controller fault | — | Fail-safe inhibit | Default-inhibit on loss [S] | Controller health observe | E-stop | Inhibit all AUTH | Restore + confirm | BLOCKED_BY_DETAILED_DESIGN | Controller fail-safe design |
| Loss of observation | Sensor/DAQ loss | — | Block dependent tests | Inhibit dependent AUTH [C/A] | Health observe | E-stop | Unconfirmed = unsafe | Restore observation | PROPOSED_ALLOCATION | Observation-health design |
| Stale command after reset | Reset/restore | — | Stale-command invalidation | New command epoch required [C] | Reset/epoch observe | E-stop | No auto-resume | New epoch | PROPOSED_ALLOCATION | Epoch design |
| Incorrect DUT identity/config | Wrong DUT/config | BASE | Identity/config validation | Inhibit hazardous AUTH [A] | Identity/config observe | E-stop | Inhibit | Correct + revalidate | PROPOSED_ALLOCATION | Identity/config design |

## 2. Notes

- `[S]` = hardware-effective safety allocation (Proposed; requires proof artifact per FX-PD-020).
- No allocation is claimed demonstrated. Items dependent on Open architecture are `BLOCKED_BY_ARCHITECTURE`; items needing numeric/energy bounds are `BLOCKED_BY_INPUT`; items needing detailed design are `BLOCKED_BY_DETAILED_DESIGN`.

## 3. Traceability

WP-014 hazard/interlock register (H-FX-*) · WP-015 interlock/state model · FX-PD-005/006/009/018/019/020 · OI-GND-001 · OI-PROT-001/002 · OI-BI-001 · OI-SENSE-001 · REQ-DCC-V-FX-071.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-21 | WP-016 initial preliminary safety allocation matrix — Proposed |
