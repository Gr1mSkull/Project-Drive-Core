# DCC Power Channel Classes

**Document ID:** DCC-PWR-CLASS-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-004

Abstract engineering channel classes for DCC power outputs. **No ampere ratings** are assigned in this document. Numeric limits are **TBD** until E30 load measurement (WP-003) and component qualification.

Normative cross-cutting requirements: [Power_Channel_Requirements.md](Power_Channel_Requirements.md).

---

## Class HC-A

### Purpose

Primary highest-tier unidirectional high-side channel for safety-critical or highest-draw vehicle loads requiring sustained and intermittent energization (e.g. electric hydraulic power steering class per E30LD-001).

### Supported load types

- High-draw electric motor loads (inductive / mixed)
- Continuous and intermittent DC loads where inrush exceeds steady-state **TBD**
- Non-PWM or PWM-capable loads per configuration **TBD**

### Expected operating modes

Shall support VCM modes per [E30_Gen1_Operating_Modes.md](../Vehicle_Integration/E30_Gen1_Operating_Modes.md): ENGINE_RUNNING, RACE, and OFF/COOL_DOWN transitions for assigned loads. CRANKING and degraded-mode behaviour: **ARCHITECTURAL DECISION REQUIRED**.

### Required switching behaviour

- Commanded OFF shall de-energize within time **TBD**
- Commanded ON shall energize only from Ready state
- Shall respect global enable and kill interlock (DC-DCC-PWR-003)
- Inrush behaviour shall be bounded — limit magnitude **TBD**

### Continuous operation requirement

Shall support continuous energization duration **TBD** at continuous current **TBD** without latched fault under declared ambient **TBD**.

### Intermittent operation requirement

Shall support duty cycle **TBD** with peak current **TBD** for duration **TBD** per load profile.

### PWM capability

Optional per channel configuration. PWM frequency range **TBD**. Default: on/off switching.

### Diagnostic requirements

Per [Power_Channel_Diagnostics.md](Power_Channel_Diagnostics.md): fault flags, current sense **TBD** resolution, timestamped events.

### Protection requirements

Per [Power_Channel_Protection.md](Power_Channel_Protection.md): overcurrent, short circuit, thermal, open load — thresholds **TBD**.

### Open load detection

Required capability: **TBD** (mandatory vs configurable per load assignment). Detection latency **TBD**.

### Short circuit behaviour

Shall limit energy delivery and transition to Fault Detected; shall not latched-on into sustained short. Retry policy configurable — count **TBD**.

### Current monitoring requirement

Shall provide load current observation suitable for overcurrent detection and logging — accuracy **TBD**.

### Thermal monitoring requirement

Shall participate in board-level thermal derating; channel junction estimate **TBD**.

### Retry behaviour

Configurable retry count (active config uses integer per output). Backoff duration **TBD**. Exceeded retries → Latched Fault.

### Latched fault behaviour

Shall require explicit service clear or power cycle per policy **TBD** before returning to Ready.

### Safe state

OFF (de-energized).

### Degraded behaviour

ARCHITECTURAL DECISION REQUIRED — shedding priority when DCC degraded (see ADR-E30-003).

### Logging requirements

State transitions, faults, retries, latched events with channel index and load key.

### Configuration parameters

| Parameter | Status |
|-----------|--------|
| `current_limit` | TBD |
| `retry_count` | Configurable |
| `pwm_enable` | Configurable |
| `open_load_detect_enable` | TBD |
| `inrush_profile_id` | TBD |

### Future expansion notes

May map to Gen1 HS60 tier channel 1; second HC-A instance not defined in Gen1.

---

## Class HC-B

### Purpose

Second high-tier unidirectional high-side channel for reserve or alternate high-draw load (e.g. spare_ch02 E30LD-027).

### Supported load types

Same family as HC-A. Assigned load technology **TBD** until harness and architect assignment.

### Expected operating modes

Same as HC-A. Simultaneous operation with HC-A and GRP-COOLING-HIGH: aggregate bus impact **TBD**.

### Required switching behaviour

Same as HC-A.

### Continuous operation requirement

Continuous current **TBD**; duration **TBD**.

### Intermittent operation requirement

Peak **TBD**; duty **TBD**.

### PWM capability

Optional — **TBD** per assignment.

### Diagnostic requirements

Same as HC-A.

### Protection requirements

Same as HC-A.

### Open load detection

**TBD** per assignment.

### Short circuit behaviour

Same as HC-A.

### Current monitoring requirement

Required — resolution **TBD**.

### Thermal monitoring requirement

Required — derating coordination with HC-A zone **TBD**.

### Retry behaviour

Configurable — default **TBD**.

### Latched fault behaviour

Same as HC-A.

### Safe state

OFF.

### Degraded behaviour

ARCHITECTURAL DECISION REQUIRED.

### Logging requirements

Same as HC-A.

### Configuration parameters

Same structure as HC-A.

### Future expansion notes

Gen1 maps to HS60 tier channel 2. May remain unassigned.

---

## Class MC-A

### Purpose

Medium-tier unidirectional high-side channel for motor-class vehicle loads: coolant pumps, radiator fans, fuel pumps (E30LD-002–005).

### Supported load types

- DC motor loads (inductive)
- PWM-controlled blower/pump/fan class
- Resistive-heater elements **TBD**

### Expected operating modes

ENGINE_RUNNING, RACE, COOL_DOWN, PRIME (fuel pump), AUTO fan rules. CAN-loss fallback: **ADR**.

### Required switching behaviour

- PWM duty update rate **TBD**
- Shall support AUTO mode via rules engine without reconfiguration

### Continuous operation requirement

Continuous current **TBD** per assigned load measurement.

### Intermittent operation requirement

Inrush **TBD**; stall current **TBD** — stall test specialist review per WP-003.

### PWM capability

**Required** for at least four logical channels in Gen1 mapping (fans, pump, heater class). Frequency range **TBD**. Resolution **TBD**.

### Diagnostic requirements

Per-channel current for fan/pump diagnostic rules; fault counters.

### Protection requirements

Inrush-tolerant operation **TBD**; blocked-rotor policy **ADR**.

### Open load detection

**TBD** — desirable for fuel pump and fan safety.

### Short circuit behaviour

Retry up to configured count; latched on persistent fault.

### Current monitoring requirement

Required for PWM closed-loop and overcurrent — accuracy **TBD**.

### Thermal monitoring requirement

Board zone derating — **TBD**.

### Retry behaviour

Active config examples: retry 2–3. Backoff **TBD**.

### Latched fault behaviour

Same as HC-A.

### Safe state

OFF.

### Degraded behaviour

ARCHITECTURAL DECISION REQUIRED — cooling loss fallback.

### Logging requirements

PWM duty changes optional; fault/retry mandatory.

### Configuration parameters

| Parameter | Status |
|-----------|--------|
| `type: pwm \| high_side` | Configurable |
| `current_limit` | TBD |
| `retry_count` | Configurable |
| `pwm_line_id` | TBD for Gen1 PWM0–3 mapping |

### Future expansion notes

Gen1 maps to four HS30-tier outputs (Ch03–06).

---

## Class LC-A

### Purpose

Standard-tier unidirectional high-side for ECU supply, headlamps, heater blower, and similar loads (E30LD-006, E30LD-010–011, E30LD-020).

### Supported load types

- Electronic control units (ECU)
- Incandescent or LED lighting **TBD**
- PWM blower motor

### Expected operating modes

IGNITION through ENGINE_RUN/RACE for ECU; lighting AUTO; degraded modes **ADR**.

### Required switching behaviour

Fast OFF on VCM transition to OFF; ECU channel hold-up during crank **TBD**.

### Continuous operation requirement

Continuous current **TBD**.

### Intermittent operation requirement

Lighting inrush **TBD**; ECU startup surge **TBD**.

### PWM capability

Required for subset (heater blower). Others on/off.

### Diagnostic requirements

Open load valuable for lighting; ECU current signature **TBD**.

### Protection requirements

Standard overcurrent/short/open — limits **TBD**.

### Open load detection

**TBD** — recommended for lighting channels.

### Short circuit behaviour

Retry then latch — count **TBD**.

### Current monitoring requirement

Recommended minimum **TBD** accuracy for ECU feed.

### Thermal monitoring requirement

Participate in aggregate board monitoring.

### Retry behaviour

Configurable (ECU retry 2 in active config).

### Latched fault behaviour

ECU channel latch policy **ADR** — impacts engine control.

### Safe state

OFF.

### Degraded behaviour

ARCHITECTURAL DECISION REQUIRED for ECU power during partial fault.

### Logging requirements

Mandatory for ECU channel state changes.

### Configuration parameters

`current_limit` TBD; `pwm` per output.

### Future expansion notes

Gen1 maps to eight HS15-tier outputs (Ch07–14).

---

## Class LC-B

### Purpose

Auxiliary low-tier unidirectional high-side for parking lights, wipers, horn-class loads, and reserve channels (E30LD-012, E30LD-018, spares Ch15–22).

### Supported load types

- Resistive lighting
- Intermittent motor (wipers)
- Low-duty accessories

### Expected operating modes

IGNITION/ENGINE_RUN AUTO; SERVICE **ADR**.

### Required switching behaviour

On/off; wiper intermittent pattern via rules **TBD**.

### Continuous operation requirement

Continuous current **TBD**; parking lights long-duration **TBD**.

### Intermittent operation requirement

Wiper stall — specialist review; duration **TBD**.

### PWM capability

Not required by default; optional **TBD**.

### Diagnostic requirements

Basic fault flags; open load for lighting **TBD**.

### Protection requirements

Standard — thresholds **TBD**.

### Open load detection

**TBD** per channel.

### Short circuit behaviour

Retry **TBD** then latch.

### Current monitoring requirement

Optional minimum — **TBD** per assignment.

### Thermal monitoring requirement

Aggregate board only.

### Retry behaviour

Configurable — default **TBD**.

### Latched fault behaviour

Standard latched fault model.

### Safe state

OFF.

### Degraded behaviour

Non-critical shedding candidate — priority **ADR**.

### Logging requirements

Faults and latch events.

### Configuration parameters

`current_limit` TBD.

### Future expansion notes

Gen1 maps to eight HS05-tier outputs (Ch15–22).

---

## Class BD-A

### Purpose

Bidirectional bridge class for reversible DC motor loads (power windows E30LD-023, E30LD-024).

### Supported load types

- Bidirectional DC motors
- Regenerative reverse current possible — clamp energy **TBD**

### Expected operating modes

ENGINE_RUN AUTO; manual command via rules **TBD**; SERVICE **ADR**.

### Required switching behaviour

Direction command (forward / reverse / brake / off) — timing **TBD**
Mutual exclusion with second BD-A channel simultaneous run **ADR-E30-012**

### Continuous operation requirement

Run current **TBD**; travel time **TBD**.

### Intermittent operation requirement

Stall at end-stop — duration limit **TBD**; specialist review mandatory.

### PWM capability

Optional speed control **TBD**; Gen1 on/off bridge assumed until **ADR**.

### Diagnostic requirements

Direction, stall detection, overcurrent — **TBD**.

### Protection requirements

Shoot-through prevention required (implementation TBD); overcurrent **TBD**.

### Open load detection

**TBD**.

### Short circuit behaviour

Immediate disable both half-bridge outputs; latch policy **TBD**.

### Current monitoring requirement

Required for stall detection — **TBD**.

### Thermal monitoring requirement

Bridge switch thermal **TBD**.

### Retry behaviour

Limited auto-retry on stall — count **TBD**.

### Latched fault behaviour

Manual clear in Service Mode.

### Safe state

OFF (both outputs off / high-impedance safe state **TBD**).

### Degraded behaviour

Non-critical — disable on DCC degraded **TBD**.

### Logging requirements

Direction changes, stall events, faults.

### Configuration parameters

`current_limit` TBD; travel timeout **TBD**.

### Future expansion notes

Gen1 maps to HB1/HB2 (channels 101, 102).

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-004 abstract class definitions |
