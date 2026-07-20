# DevKit Fixture Interlock and State Model — WP-015

**Document ID:** DOC-DK-FISM-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Functional state / interlock / E-stop-integrity model only.
No timing numerics, devices, or E-stop topology selected. No safety-integrity level claimed.
No transition depends solely on UI state or software display.
```

## 1. Fixture state model (§16)

| State | Entry conditions | Permitted energy paths | Prohibited energy paths | Permitted commands | Required observations | Interlocks | Exit conditions | Fault transition | Safe minimum | Recovery authority |
|-------|------------------|------------------------|-------------------------|--------------------|-----------------------|------------|-----------------|------------------|--------------|--------------------|
| `FX_OFF` | Power removed / initial | None | All hazardous | Power-on | — | All inhibit | Power applied → FX_SAFE | → FX_OFF | De-energized | Operator |
| `FX_SAFE` | Power-on / after removal | AUX only | All hazardous | Self-check request | AUX ok; E-stop clear | All AUTH inactive | → FX_SELF_CHECK | → FX_FAULT | AUX-only | Operator |
| `FX_SELF_CHECK` | From FX_SAFE | AUX | Hazardous | Run checks | Identity/config/interlock/measurement-ready | Integrity checks | pass → FX_READY_BASE; fail → FX_FAULT | → FX_FAULT | Inhibit | Operator |
| `FX_READY_BASE` | Self-check pass | AUX | Hazardous until AUTH | Request base AUTH | Base path valid | E-stop clear; base valid | → FX_BASE_ARMED | → FX_FAULT | Inhibit | Operator |
| `FX_BASE_ARMED` | Base AUTH requested+granted | AUX (base commanded, not yet observed) | External | Command base energy | AUTH_GRANTED | Base interlocks | observed active → FX_BASE_ENERGIZED | → FX_ENERGY_REMOVAL | Inhibit base | FX-INTERLOCK |
| `FX_BASE_ENERGIZED` | Base energy observed active | BASE-DUT-ENERGY | External (while OI-GND-001 Open) | Test start; energy remove | ENERGY_PATH_OBSERVED_ACTIVE | Base interlocks | → FX_TEST_ACTIVE / FX_ENERGY_REMOVAL | → FX_ENERGY_REMOVAL | Remove base | FX-ENERGY-REMOVAL |
| `FX_READY_EXTERNAL` | Self-check pass; base safely removed | AUX | Base + external simultaneously | Request ext AUTH | Base observed inactive | Exclusivity (OI-GND-001) | → FX_EXTERNAL_ENERGY_ARMED | → FX_FAULT | Inhibit | Operator |
| `FX_EXTERNAL_ENERGY_ARMED` | Ext AUTH requested (authorization only) | None by itself | Combined BASE+EXT | Command ext energy | Auth record; base inactive | Exclusivity; back-feed prevent | → FX_EXTERNAL_ENERGIZED | → FX_ENERGY_REMOVAL | Inhibit ext | FX-INTERLOCK |
| `FX_EXTERNAL_ENERGIZED` | Ext energy observed active | EXT paths | Base (while OI-GND-001 Open) | Test start; energy remove | ENERGY_PATH_OBSERVED_ACTIVE (ext) | Ext interlocks; back-feed | → FX_TEST_ACTIVE / FX_ENERGY_REMOVAL | → FX_ENERGY_REMOVAL | Remove ext | FX-ENERGY-REMOVAL |
| `FX_TEST_ACTIVE` | Required AUTH + measurements | Declared-profile paths (no simultaneous BASE+EXT while OI-GND-001 Open) | Undeclared paths | Test abort; fault arm | Profile MPs available | All required interlocks | controlled exit / abort | → FX_ENERGY_REMOVAL | Controlled exit | Test controller (gated) |
| `FX_ENERGY_REMOVAL` | Any hazardous exit / E-stop | Removal in progress | New AUTH grant | Confirm removal | Residual observation | Override all AUTH | → FX_DISCHARGE / FX_LOCKOUT | stay | Force removal | FX-ENERGY-REMOVAL |
| `FX_DISCHARGE` | Removal in progress | Discharge action | Hazardous | Await decay | Residual/discharge observe | Discharge interlock | DISCHARGE_COMPLETE → FX_LOCKOUT | → FX_LOCKOUT | Hold until safe decay | FX-DISCHARGE |
| `FX_LOCKOUT` | After removal/discharge | Inhibited | All hazardous | Recovery request | Safe state confirmed | Prior AUTH revoked; stale | → FX_RECOVERY_CHECK | stay | Inhibited | Operator (deliberate) |
| `FX_FAULT` | Any detected fault | Inhibited | All hazardous | Diagnose; reset req | Fault captured | Inhibit-all | → FX_ENERGY_REMOVAL / FX_LOCKOUT | stay | Inhibited | Operator |
| `FX_RECOVERY_CHECK` | Deliberate recovery | Inhibited until pass | Hazardous | Validate | Identity/config; residual safe | Recovery interlocks | pass → FX_SAFE/READY | → FX_FAULT | Inhibited | Operator + interlock |

Uncommanded startup / power restoration enters `FX_SAFE` (never resumes prior test/fault). Stale-command invalidation after E-stop, physical KILL, power/source interruption, controller reset, invalid identity/config, or loss of control authority.

## 2. Interlock architecture (§17)

| Interlock | Protected hazard | Required inputs | Logic role | Hardware-effective action | Observation | Failure behavior | Safe minimum | Recovery condition | Implementation dependency |
|-----------|------------------|-----------------|------------|---------------------------|-------------|------------------|--------------|--------------------|---------------------------|
| E-stop integrity | Uninhibited hazard on E-stop fault | E-stop path status | Gate all AUTH | Inhibit hazardous energy | E-stop state | Fail-safe inhibit | AUTH inhibited if unconfirmed | Integrity confirmed | REQ-DCC-V-FX-071 |
| Energy-removal availability | Cannot remove energy | Removal readiness | Precondition to energize | Block energize if removal unavailable | Removal-ready | Inhibit | No energize without removal | Removal available | FX-ENERGY-REMOVAL |
| DUT connection validity | Miswired DUT | DUT identity/connection | Gate DUT AUTH | Inhibit DUT energy | Connection observe | Inhibit | Inhibit if invalid | Valid connection | FX-DUT-INTERFACE |
| Source connection validity | Miswired source | Source connection | Gate source AUTH | Inhibit source | Connection observe | Inhibit | Inhibit if invalid | Valid connection | FX-SOURCE-CONTROL |
| Load-bank authorization | Uncontrolled sink | AUTH_LOAD_BANK, state | Gate load-bank | Inhibit sink | Sink state | Inhibit | Inactive | Valid AUTH | FX-LOAD-BANK |
| Load-bank stuck-on detection | Load persists | Command vs observed | Detect mismatch | Revoke + upstream removal | Load observe | Removal+lockout | Upstream energy removed | Deliberate recovery | FX-ENERGY-REMOVAL |
| External-energy exclusivity | Combined BASE+EXT | Base/ext observed state | Mutual exclusion | Block one while other active | Both observed | Inhibit both | No simultaneous (OI-GND-001) | Architect disposition | OI-GND-001 |
| Back-feed prevention | Base overstress | Ext/base state | Directional prevent | Inhibit external→base | Ext/base current | Inhibit | No uncontrolled base energization | Back-feed proof | OI-GND-001; OI-PROT-001 |
| Fault-injection authorization | Unauthorized fault | AUTH_FAULT, preconditions | Gate fault | Inhibit fault | Fault state | Inhibit+lockout | Default inhibited | Deliberate | ADR-023 |
| Measurement readiness | Test without needed data | Required MP status | Gate dependent tests | Block test | MP status | Block | Block dependent tests | MP available | FX-MEASUREMENT |
| Containment readiness | Exposed energy | Containment status | Precondition | Inhibit hazardous | Containment observe | Inhibit | Inhibit if not contained | Contained | ADR-DK-011/012 |
| Discharge completion | Residual stored energy | Residual observe | Gate recovery | Hold lockout | Residual | Hold | Hold until safe decay | DISCHARGE_COMPLETE | FX-DISCHARGE |
| Operator reset | Unintended re-energize | Deliberate reset | Require deliberate action | No energize on reset | Reset event | Remain safe | Reset ≠ energize | New epoch | FX-OPERATOR-CONTROL |
| State-observation plausibility | False safe belief | Cross-checked observations | Plausibility | Treat implausible as unsafe | Multiple observes | Inhibit | Unconfirmed = unsafe | Consistent observation | FX-MEASUREMENT |

## 3. E-stop path integrity (§18)

Carrying `REQ-DCC-V-FX-071`:

```text
If E-stop path integrity is unconfirmed:
  AUTH inhibited · Energy application prohibited · Fault recorded · Deliberate recovery required
```

Architecture options **evaluated (not selected)**:

| Option | Description | Notes |
|--------|-------------|-------|
| E-STOP-OPT-1 | Monitored single safety-effective path | Requires continuity/proof monitoring |
| E-STOP-OPT-2 | Independent dual safety-effective paths | Higher separation; more complexity |
| E-STOP-OPT-3 | Safety-effective path plus independent observation | Detects discrepancy |
| E-STOP-OPT-4 | Series safety chain with continuity monitoring | Chain integrity monitored |

No topology is selected; no safety-integrity level is claimed. Selection requires Architecture Review. Preliminary disposition: **BLOCKED_BY_ARCHITECTURE**.

## 4. Traceability

REQ-DCC-V-FX-001…005/010…015/052/071 · PWR-A-021…024 · ADR-022/023 · OI-GND-001 · OI-PROT-001.

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial interlock and state model — Proposed |
