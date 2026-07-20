# DevKit Fixture Hazard and Interlock Register — WP-014

**Document ID:** DOC-DK-FHIR-001  
**Version:** 1.1  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Hazard/interlock REQUIREMENTS register — no quantitative risk reduction claimed.
```

## 1. Register

| Hazard ID | Hazard | Initiating condition | Energy source | Unsafe outcome | Preventive interlock | Protective layer | Detection | Safe minimum | Recovery | Open dependency | Owner |
|-----------|--------|----------------------|---------------|----------------|----------------------|------------------|-----------|--------------|----------|-----------------|-------|
| H-FX-001 | Unexpected base energization | Spurious AUTH_BASE | BASE-SOURCE | Operator/DUT damage | AUTH default inactive; identity/config | E-stop | AUTH/source sense | SAFE_OFF | Deliberate READY | — | Fixture design |
| H-FX-002 | Unexpected external energization | Spurious AUTH_EXT | EXT-SOURCE | Back-feed/exposure | AUTH_EXT inactive; separate arm | Ext removal | Ext enable sense | Ext Off | Deliberate arm | OI-FIX-001 | Fixture design |
| H-FX-003 | Back-feed into base | Ext/base conflict | EXT→BASE | Base overstress | Back-feed prohibit; no silent merge | Disconnect | Ext/base current | Base and external hazardous-energy paths inhibited or disconnected; back-feed prevented; ground/reference relationship remains Open under OI-GND-001 | ENERGY_REMOVAL | OI-GND-001 | Architect |
| H-FX-004 | Source-to-source conflict | Dual source connect | BASE+EXT | Combined envelope | Prohibit unless Accepted topology; while OI-GND-001 Open: simultaneous BASE+EXT energization prohibited | E-stop | Dual AUTH detect | Inhibit both; EXTERNAL_ENERGY_ARMED ≠ energized | SAFE_OFF | Future ADR; OI-GND-001 | Architect |
| H-FX-005 | Load-bank failure | LB stuck on | DUT out / upstream source | Overload/heat | Fail-to-remove → revoke AUTH_LOAD_BANK + inhibit/remove upstream energy → ENERGY_REMOVAL → POST_FAULT_LOCKOUT | Channel/fixture | LB state/I | AUTH revoke alone ≠ de-energized; upstream energy inhibit/remove required | Deliberate RECOVERY_VALIDATION | — | Fixture design |
| H-FX-006 | Load-bank overtemperature | Sustained sink | LB | Fire/damage | Thermal inhibit (limit Open) | LB protect | Temp class Open | Inhibit LB | Cool+reset | ADR-DK-011 | Thermal |
| H-FX-007 | Fixture AUX loss | AUX fail | — | Loss of control | Hazardous AUTH revoke | E-stop default | AUX monitor | Inhibit energy | SAFE_OFF | — | Fixture design |
| H-FX-008 | Operator E-stop failure | E-stop path fault / integrity unconfirmed | Any fixture-controlled | Continued hazard | Hazardous AUTH inhibited when E-stop integrity unconfirmed (REQ-DCC-V-FX-071) | Independent energy-removal allocation TBD — topology not selected | E-stop sense / integrity check Open | Hazardous-energy authorization inhibited when E-stop path integrity is unconfirmed | Repair + deliberate recovery | Design disposition BLOCKED_BY_ARCHITECTURE until E-stop fault-tolerance, testability and residual-risk allocation Accepted | Architect / Fixture design |
| H-FX-009 | DUT KILL observation failure | Obs path fault | DUT | False safe belief | Independent HW-effective path still required | HW KILL | Compare raw/HW/obs | Do not rely on obs alone | Repair | — | Safety |
| H-FX-010 | Fault-injection stuck active | AUTH_FAULT sticky | Fault path | Persistent fault | Default inhibit; reset clears | E-stop; ENERGY_REMOVAL | Fault state | Inhibit+LOCKOUT | Deliberate recovery | — | Fixture design |
| H-FX-011 | Invalid fixture identity | Wrong/missing ID | — | Wrong config energy | Inhibit hazardous AUTH | — | ID check | SAFE_OFF | Correct ID | — | Fixture design |
| H-FX-012 | Invalid fixture configuration | Bad config | — | Unsafe test | Inhibit execution | — | Config check | SAFE_OFF | Valid config | — | Fixture design |
| H-FX-013 | Measurement-reference fault | Sense ref error | — | Wrong control/decision | Block dependent tests | — | Plausibility Open | No energy if required MP absent | Fix ref | OI-GND-001 | Measurement |
| H-FX-014 | Ground-loop / reference conflict | Cross-envelope GND | Multi | Shock/noise/damage | OI-GND-001 unresolved ⇒ block combined | — | — | No combined energize | Architect decision | OI-GND-001 | Architect |
| H-FX-015 | Regenerative-energy return | BI return | DUT→source | Source cannot absorb | Do not assume absorb; clamp/absorb path | Clamp/fixture | I_CH_IN &lt; 0 | Controlled absorb or inhibit | Profile-specific | OI-BI-001 | Architect |
| H-FX-016 | Inductive stored energy | Open under current | L | Arc/spike | Decay/discharge confirm | Clamp | V spike | Wait decay | RECOVERY | — | Fixture design |
| H-FX-017 | Capacitive stored energy | Charged C | C | Residual shock | Discharge confirm | Bleed TBD | V residual | Confirm safe V | RECOVERY | — | Fixture design |
| H-FX-018 | Bidirectional shoot-through | Conflict cmds | Bridge | Device destroy | Interlock; AUTH sequencing | Bridge protect | Current spike | Inhibit BI | OI-BI-001 | Architect |
| H-FX-019 | Stalled load | Stall applied | Motor/BI | Thermal accum | Stall AUTH; thermal-state model | Channel protect | I_STALL | ENERGY_REMOVAL | OI-FIX-002 | Fixture |
| H-FX-020 | Exposed energized conductor | Operator access | Any | Shock | INSPECTION only de-energized | Covers TBD | — | SAFE_OFF for access | Procedure | Design | Fixture |
| H-FX-021 | Incorrect DUT connection | Miswire | BASE | Damage | Identity/config; polarity checks Open | Input protect | — | Inhibit | Correct connect | — | Fixture |
| H-FX-022 | Incorrect external-module connection | Miswire EXT | EXT | Back-feed | Separate AUTH; checks | Back-feed prevent | — | Inhibit EXT | Correct | OI-FIX-001 | Fixture |
| H-FX-023 | Loss of control communication | Link down | — | Stale AUTH risk | Revoke AUTH; no restore | E-stop available | Link monitor | ENERGY_REMOVAL/SAFE_OFF | New epoch | — | Fixture |
| H-FX-024 | Control-system reset | Reset | — | Stale cmds | Invalidate cmds | Inhibit | Reset detect | SAFE_OFF | New epoch | — | Fixture |
| H-FX-025 | Power restoration after interruption | Power returns | — | Auto resume | Force SAFE_OFF | Inhibit | Power monitor | SAFE_OFF | Deliberate start | — | Fixture |

## 2. Quantitative claim

No quantitative risk reduction or SIL/ASIL claim is made in WP-014.

## 3. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture hazard and interlock register — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — H-FX-003 isolation wording; H-FX-005 stuck-on; H-FX-008 E-stop integrity |
