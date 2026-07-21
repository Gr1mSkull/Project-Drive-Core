# DevKit Load-Bank Preliminary Design — WP-015

**Document ID:** DOC-DK-LBPD-001  
**Version:** 1.3  
**Status:** Accepted — Architecture Review (2026-07-21)  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Load-bank FUNCTIONAL preliminary design — sink-function architecture.
No physical load-bank technology, device, rating, power, thermal, or cooling value selected.
```

## 0. Source / sink / regenerative semantics (WP-015-R1)

```text
The load bank does not originate an independent source envelope.

A regenerative or bidirectional load may return energy toward its
associated source or absorption path. Such returned energy does not
reclassify the load bank as EXT-SOURCE, but it is an energy-bearing
reverse-flow condition requiring explicit containment.
```

Accordingly:

```text
sink-function architecture;
independent energy origination prohibited;
returned-energy behavior separately controlled and BLOCKED_BY_ARCHITECTURE
until OI-BI-001 and OI-GND-001 are dispositioned.
```

`PWR-A-023` (EXT-LOAD-BANK is a sink, not an independent source) is unchanged.

## 1. Functional load classes (§19)

| Class | Test purpose | Energy source | Current direction | Control boundary | Authorization boundary | Observation boundary | Shutdown mechanism | Energy-removal mechanism | Stored-energy concern | Failure modes | Safe minimum | Measurement needs | Blocked inputs | Readiness |
|-------|--------------|---------------|-------------------|------------------|------------------------|----------------------|--------------------|--------------------------|-----------------------|---------------|--------------|-------------------|----------------|-----------|
| `LB-RESISTIVE` | Continuous/steady load | DUT/ext output | Draw (+) | AUTH_LOAD_BANK gated | FX-AUTHORIZATION | I_LOAD, V_LOAD | Command removal | Upstream inhibit/remove | Low | stuck-on; open | Sink inactive | I/V load | Ratings Open | PARTIAL |
| `LB-INDUCTIVE` | Inductive turn-off | DUT output + stored | Draw; clamp on interrupt | AUTH gated | FX-AUTHORIZATION | V spike, I | Command + clamp | Removal + decay | High (L energy) | arc/spike; clamp fail | Controlled decay | V spike capture | Clamp energy Open | PARTIAL |
| `LB-ELECTRONIC` | Programmable profile | DUT/ext output | Draw (+) | AUTH gated | FX-AUTHORIZATION | I command/actual | Command removal | Upstream inhibit/remove | Device-dependent | fail-to-remove | Sink inactive | I profile | Ratings Open | PARTIAL |
| `LB-MOTOR_OR_ACTUATOR` | Motor/actuator load | DUT output | Draw; possible return | AUTH gated | FX-AUTHORIZATION | I, direction | Command removal | Upstream inhibit/remove | Mechanical/inductive | stall; reverse current | Sink inactive | I, direction | OI-FIX-002; TBD-DK-022 | BLOCKED_BY_DETAILED_DESIGN |
| `LB-BIDIRECTIONAL_OR_REGENERATIVE` | Bidirectional / returning energy (returned-energy reverse-flow, not independent origination) | DUT/bridge (upstream origin; load bank never originates) | Both (+/−) | AUTH gated | FX-AUTHORIZATION | signed I | Command + clamp/absorb | Removal + absorb path | Returned energy (reverse-flow) | source cannot absorb | Inhibit; do not assume absorb; explicit containment | signed I; bridge/load split | OI-BI-001; OI-GND-001 | BLOCKED_BY_ARCHITECTURE |
| `LB-FAULT-SIMULATION` | Fault emulation (open/overload/short) | DUT/ext output | Fault-dependent | AUTH_FAULT gated | FX-AUTHORIZATION | fault MPs | Abort + removal | Upstream inhibit/remove | Fault energy | uncontrolled fault | Inhibit + lockout | fault MPs | OI-SC-001; ED-IN-021; bounds Open | BLOCKED_BY_DETAILED_DESIGN |

No physical load-bank technology is selected. `I_loadbank_limit` remains Open (ED-IN-022) and does not increase `I_certified_cont`. The "Energy source" column identifies the **upstream** energy origin (DUT/ext/bridge); the load bank itself never originates an independent source envelope. Returned/regenerative energy is a reverse-flow condition requiring explicit containment (BLOCKED_BY_ARCHITECTURE until OI-BI-001 and OI-GND-001 are dispositioned).

## 2. Load-bank failure behavior (§20)

Stuck-on / uncontrolled condition requires:

```text
Revoke authorization
+ Inhibit or remove upstream energy
+ Enter ENERGY_REMOVAL
+ Confirm safe electrical state where possible
+ Enter FX_LOCKOUT_UNCONFIRMED (→ FX_LOCKOUT_SAFE only after removal/discharge confirmed)
+ Require deliberate recovery (from FX_LOCKOUT_SAFE only)
```

```text
Authorization revoke alone does not prove de-energization.
```

Analyzed failure modes:

| Failure mode | Detection (functional) | Safe-minimum response |
|--------------|------------------------|-----------------------|
| control stuck ON | command vs observed mismatch | revoke + upstream removal + FX_LOCKOUT_UNCONFIRMED (→ SAFE after confirm) |
| switching element shorted | current persists after removal command | upstream inhibit/remove + FX_LOCKOUT_UNCONFIRMED (→ SAFE after confirm) |
| switching element open | expected load absent | flag; safe (no hazardous energy added) |
| load disconnected | load current absent under command | flag; verify no arc; safe |
| unexpected reverse current | signed-I sign anomaly | inhibit; do not assume source absorbs (OI-BI-001) |
| stored-energy persistence | residual V/I after removal | discharge/confirm safe decay before recovery |
| measurement disagreement | cross-check implausible | treat as unsafe; block dependent tests |
| thermal fault | thermal observe (limits Open) | inhibit load; lockout |
| cooling unavailable | cooling status | inhibit load before thermal risk |
| communication loss | link monitor | revoke AUTH; energy removal; no stale restore |

No automatic stale-command restoration is permitted.

## 3. Traceability

REQ-DCC-V-FX-032/050/056/060 · PWR-A-002/023 · OI-BI-001 · OI-SC-001 · OI-FIX-002 · TBD-DK-022 · ED-IN-021/022.

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial load-bank preliminary design — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — source/sink/regenerative semantics reconciled; absolute "never sourced / sink-only" removed; returned-energy reverse-flow containment BLOCKED_BY_ARCHITECTURE; PWR-A-023 unchanged |
| 1.2 | 2026-07-21 | WP-015-R2 — lockout substate references (UNCONFIRMED→SAFE) in stuck-on sequence |
| 1.3 | 2026-07-21 | Architecture Review **Accepted** (WP-015 / R1 / R2 / R3; reviewed head `227ea78`, PR #19); Open decisions retained; NOT VERIFIED |
