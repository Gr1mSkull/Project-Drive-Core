# DevKit Threshold Measurement Plan — WP-009

**Document ID:** DOC-DK-MEAS-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-009  
**Date:** 2026-07-20

> Measurement **plan** only — not evidence. No VE records. No physical validation claimed.

## 1. General requirements

### 1.1 DUT baseline (ADR-015)

Each session shall record:

| Field | Source |
|-------|--------|
| Composite baseline ID | ADR-015 / STD-REV-001 |
| Logic BOARD_ID | TBD-DK-020 map when available |
| Power BOARD_ID | As wired |
| Firmware build ID | Certification build per ADR-018 when available |
| Config profile hash | `devkit.yaml` compile ID |
| Analysis package version | WP-009 doc revision |

### 1.2 Instrument capability (no MPN selection)

| Capability | Requirement |
|------------|-------------|
| Oscilloscope bandwidth | ≥ required edge bandwidth for fastest expected transition (study: ≥20 MHz for switch edges; **verify against final DUT**) |
| Sample rate | Sufficient for ≤10 % timing uncertainty on smallest budget term |
| Current probe range | Above expected peak including fault tests |
| Isolation | Isolated or differential where ground reference differs |
| Time sync | Common timebase or documented skew correction between channels |
| DMM | Bench PSU monitoring; rail checks |

### 1.3 Conservative acceptance structure

```text
approved_limit ≥ t_worst_or_I_worst + uncertainty + margin
```

Minimum repetitions for timing: **≥30** captures per configuration unless hazard limits lower count (document if reduced).

Statistics: report **maximum observed**, mean, σ, outliers removed with justification.

## 2. Current measurements

### 2.1 TBD-DK-002 — Certified continuous input current

| Field | Plan |
|-------|------|
| Profile | P3 |
| Topology | PSU → protection → DUT entry → single active channel → resistive load |
| Stimulus | Ramp load current until thermal steady-state or protection trip (abort before damage) |
| Trigger | Load step command |
| Observation | `I_input_cont` at entry shunt; channel current; rail voltages |
| Sampling | ≥1 kHz logging for 60 s steady-state windows |
| Calibration | Shunt + DMM traceable; record calibration date |
| Repetitions | ≥3 steady-state plateaus per load point |
| Conditions | T_amb recorded; cold start vs warm noted |
| Raw data | CSV: timestamp, I_in, I_ch, V_in, T_amb |
| Uncertainty | Shunt tolerance + DMM + probe offset combined RSS |
| Pass criterion structure | `I_measured_cont + uncertainty ≤ I_certified_cont` (once Architect approves limit) |
| Abort | Input overcurrent; abnormal heating; kill |
| Role | Test Owner |

### 2.2 TBD-DK-003 — Simultaneous load current

| Field | Plan |
|-------|------|
| Profile | P4 |
| Topology | Multi-channel loads per declared duty table |
| Stimulus | Simultaneous ON commands per profile; explicit duty factors |
| Trigger | Second channel enable edge |
| Observation | Per-channel current + input current |
| Sampling | ≥1 kHz |
| Calibration | As §2.1 |
| Repetitions | ≥3 per channel combination |
| Conditions | Document which channels active; no implicit diversity |
| Raw data | CSV multi-channel |
| Uncertainty | RSS per channel + sum rule documented |
| Pass criterion | `Σ I_ch + uncertainty ≤ I_simultaneous` (when approved) |
| Abort | Thermal limit; protection trip |
| Role | Test Owner |

## 3. Timing measurements

### 3.1 TBD-DK-004 — Hardware kill response

| Field | Plan |
|-------|------|
| Profile | P3 with representative load |
| Topology | Kill inject at DUT kill connector; scope on kill, `nENABLE_GLOBAL`, output voltage, load current |
| Stimulus | Kill assert edge generator or manual switch with documented bounce |
| Trigger | Kill rising/falling edge (active level per schematic when available) |
| Observation channels | CH0 kill; CH1 enable; CH2 V_out; CH3 I_load |
| Sampling | Scope ≥ minimum for 10 % uncertainty on `t_kill_total` |
| Bandwidth | Per instrument capability §1.2 |
| Sync | Single scope; common ground at DUT reference |
| Calibration | Scope timebase accuracy; probe delay matching |
| Repetitions | ≥30 |
| Load states | Resistive minimum; inductive representative (**load model required**) |
| Raw data | Waveform capture + exported CSV markers for start/end |
| Start marker | Kill active edge |
| End marker | All `V_out < V_off_threshold` AND `I_load < I_safe` for ≥10 ms holdoff (holdoff subject to Architect approval) |
| Uncertainty | Trigger jitter + probe skew + marker placement |
| Pass criterion | `t_worst + uncertainty + margin ≤ TBD-DK-004` (when approved) |
| Abort | Unexpected re-enable; oscillation |
| Role | Test Owner |

### 3.2 TBD-DK-005 — Watchdog response

| Field | Plan |
|-------|------|
| Profile | P3 |
| Stimulus | Induced watchdog expiry (test hook or FW test mode when available) |
| Trigger | WD expiry indication or last fed timestamp |
| Observation | WD flag; global disable; output voltage/current |
| Sampling | As §3.1 |
| Repetitions | ≥30 |
| Pass criterion | `t_worst + uncertainty + margin ≤ TBD-DK-005` |
| Abort | Reset loop unbounded |
| Role | Test Owner |

### 3.3 TBD-DK-007 — Logic↔Power control loss

| Field | Plan |
|-------|------|
| Profile | P3 |
| Stimulus | Stop DCPI/SPI traffic while outputs commanded ON |
| Trigger | Last valid frame timestamp |
| Observation | SPI CS/SCK activity; `nENABLE_GLOBAL`; outputs |
| Message period | Record `T_msg`, missed-frame policy |
| Repetitions | ≥30 |
| Pass criterion | `t_worst + uncertainty + margin ≤ TBD-DK-007` AND `>100 ms` lower bound check |
| Abort | Outputs remain ON beyond fail-safe expectation |
| Role | Test Owner |

### 3.4 TBD-DK-014 — Commanded safe-OFF

| Field | Plan |
|-------|------|
| Profile | P2/P3 single channel |
| Stimulus | Valid OFF command via RT path |
| Trigger | Command accept timestamp (log + scope on command GPIO if exposed) |
| Observation | Channel `V_out`, `I_load` |
| Repetitions | ≥30 per load type |
| Pass criterion | `t_worst + uncertainty + margin ≤ TBD-DK-014` |
| Abort | Channel remains ON |
| Role | Test Owner |

### 3.5 TBD-DK-021 — Post-kill re-enable sequence

| Field | Plan |
|-------|------|
| Profile | P3 |
| Stimulus | Kill assert → release → attempt enable without ack → full valid sequence |
| Trigger | Kill release edge |
| Observation | State machine log; output enables; kill line |
| Measurement type | **Procedural** — verify no output energization until EXPLICIT_FUNCTION_ENABLE |
| Repetitions | ≥10 full sequences |
| Pass criterion | Zero unauthorized energization events |
| Abort | Any auto-re-enable |
| Role | Test Owner |

## 4. Related measurements (referenced)

| TBD | Brief plan pointer |
|-----|-------------------|
| TBD-DK-001/012 | PSU programmable UV step; capture output states — UV table BLOCKED |
| TBD-DK-017 | Rail probe at Logic/Power test points — BLOCKED_BY_ELECTRICAL_ARCHITECTURE |
| TBD-DK-018/019 | Thermal soak duration + surface TC/IR — BLOCKED_BY_HAZARD_DECISION |
| TBD-DK-022 | Stall fixture with current/time capture — BLOCKED_BY_COMPONENT_SELECTION |

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial measurement plan |
