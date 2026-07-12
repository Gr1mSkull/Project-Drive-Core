# BMW E30 Gen1 — Load Measurement Plan

**Document ID:** VI-E30-MP-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-003

## 1. Purpose

Define bench and vehicle measurements required to populate electrical fields in [e30_gen1_loads.yaml](../../config/vehicles/e30_gen1_loads.yaml). No numeric values are invented in this plan.

## 2. Scope

| In scope | Out of scope |
|----------|--------------|
| Loads with `measurement_required: true` (E30LD-001–026) | Spare channels E30LD-027–037 |
| Safe normal and startup characterization | Destructive or unsafe stall tests without approval |
| Current, voltage, timing capture | Component selection |

## 3. Common instrumentation

| Item | Specification | Notes |
|------|---------------|-------|
| DC power supply | Adjustable 9–16 V, current limit set below DCC class until characterized | Bench only |
| Ammeter / current probe | Range per load table; ≥1 kHz bandwidth for inrush | Hall or shunt |
| Oscilloscope | ≥100 kSa/s for motor inrush | Shared for PWM loads |
| Data logger | Sync voltage and current | CSV export mandatory |
| Temperature | Ambient + IR spot for motors | Record at test start/end |
| Vehicle bus monitor | Battery voltage at DCC input | In-vehicle tests |

## 4. Measurement quality acceptance

| Criterion | Requirement |
|-----------|-------------|
| Sample rate | Sufficient to capture peak inrush (≥10 samples during startup window) |
| Calibration | Probe zeroed; supply voltage recorded |
| Repeatability | Minimum 3 consecutive startups for motor loads |
| Documentation | Raw CSV + summary table in artifact |
| Evidence tag | Update YAML `evidence_status` to `measured` only after review |
| Specialist review | Required for rows marked **HAZARD — SPECIALIST REVIEW** |

## 5. Artifact storage

```
docs/Vehicle_Integration/measurements/{load_id}_{test_type}.md
docs/Vehicle_Integration/measurements/raw/{load_id}_{test_type}_{date}.csv
```

After measurement, update fields in `config/vehicles/e30_gen1_loads.yaml` with measured values and `evidence_status: measured`.

---

## 6. Per-load measurement plans

### E30LD-001 — ehps (Electric hydraulic power steering pump)

| Field | Value |
|-------|-------|
| **Objective** | Nominal, max continuous, startup inrush, duration, duty cycle at operating temperature |
| **Instrumentation** | High-current probe (range TBD until coarse bench trace), scope, logger |
| **Test connection** | In-line on DCC Ch01 feed or bench supply through OEM pump harness |
| **Sampling rate** | ≥20 kSa/s for inrush window |
| **Current range** | TBD — select probe after OQ-001 pump identification |
| **Duration** | Normal: 10 min steady; Startup: 10 cycles |
| **Normal operating test** | Engine RUN equivalent: pump at operating pressure, 12 V nominal, record I_continuous |
| **Startup test** | Cold start from OFF; capture I_peak and t_duration |
| **Stall / blocked test** | **HAZARD — SPECIALIST REVIEW** — hydraulic stall may overheat pump; do not run without architect approval |
| **Ambient** | Record °C; prefer 20–25 °C baseline + one hot-soak repeat |
| **Artifact** | `E30LD-001_normal.md`, `E30LD-001_startup.md` |

### E30LD-002 — water_pump (Electric coolant pump)

| Field | Value |
|-------|-------|
| **Objective** | I_nom, I_max continuous, inrush, PWM current vs duty curve |
| **Instrumentation** | Current probe 0–50 A range (TBD), scope for PWM |
| **Test connection** | Ch05 feed; fluid loop must be filled — no dry-run |
| **Sampling rate** | ≥10 kSa/s inrush; 1 kSa/s PWM steady |
| **Current range** | TBD |
| **Duration** | Normal: 15 min; PWM sweep: 10–100 % in 10 % steps |
| **Normal operating test** | 100 % duty, operating coolant temperature |
| **Startup test** | From 0 % PWM to target |
| **Stall test** | Not applicable if fluid coupled — blocked rotor **HAZARD — SPECIALIST REVIEW** |
| **Ambient** | Engine bay temp simulated or recorded |
| **Artifact** | `E30LD-002_normal.md`, `E30LD-002_pwm_map.md` |

### E30LD-003 — fan1 / E30LD-004 — fan2 (Radiator fans)

| Field | Value |
|-------|-------|
| **Objective** | I per speed/PWM point, inrush, simultaneous GRP-COOLING-HIGH contribution |
| **Instrumentation** | Current probe, scope, PWM generator or DCC Ch03/Ch04 |
| **Test connection** | Fan harness at radiator; test fans separately then both ON |
| **Sampling rate** | ≥10 kSa/s inrush |
| **Current range** | TBD |
| **Duration** | 5 min per speed; dual-fan 5 min combined |
| **Normal operating test** | 100 % duty steady |
| **Startup test** | 10 cold starts per fan |
| **Stall test** | Blocked blade **HAZARD — SPECIALIST REVIEW** — brief blocked test only with mechanical stop and specialist present |
| **Ambient** | Unblocked airflow required |
| **Artifact** | `E30LD-003_*.md`, `E30LD-004_*.md`, `GRP-COOLING-HIGH_dual_fan.md` |

### E30LD-005 — fuel_pump (Fuel pump)

| Field | Value |
|-------|-------|
| **Objective** | I_nom, I_prime, inrush; verify PRIME duration vs current |
| **Instrumentation** | Current probe, pressure gauge (fuel) |
| **Test connection** | Fuel pump power lead; **must have fuel / safe container** |
| **Sampling rate** | ≥5 kSa/s |
| **Current range** | TBD |
| **Duration** | Prime: per VCM timing TBD; Run: 5 min |
| **Normal operating test** | Steady delivery pressure at 12 V |
| **Startup test** | 10 primes from OFF |
| **Stall test** | **PROHIBITED** — dry-run or deadhead blocked flow **HAZARD** |
| **Ambient** | Ventilated; fire extinguisher present |
| **Artifact** | `E30LD-005_normal.md`, `E30LD-005_prime.md` |

### E30LD-006 — ecu_power (Engine ECU supply)

| Field | Value |
|-------|-------|
| **Objective** | I_nominal, I_startup, hold-up during crank voltage dip |
| **Instrumentation** | Low-current probe 0–20 A, scope on supply |
| **Test connection** | DCC Ch07 to ECU J_PWR |
| **Sampling rate** | ≥10 kSa/s during crank transient |
| **Current range** | TBD — expect low single-digit A until characterized |
| **Duration** | 30 min nominal; crank capture 10 cycles |
| **Normal operating test** | ENGINE_RUN telemetry active |
| **Startup test** | Power-on from OFF |
| **Stall test** | N/A |
| **Ambient** | Bench or vehicle |
| **Artifact** | `E30LD-006_normal.md`, `E30LD-006_crank_dip.md` |

### E30LD-007 — ignition_coils

| Field | Value |
|-------|-------|
| **Objective** | Primary/secondary current profile per firing; aggregate supply current |
| **Instrumentation** | Current probe on coil supply, scope sync to trigger |
| **Test connection** | ECU J_IGN feed — **after OQ-006 path confirmed** |
| **Sampling rate** | ≥50 kSa/s for pulse capture |
| **Current range** | TBD |
| **Duration** | 5 min at idle RPM; sweep to redline TBD |
| **Normal operating test** | Steady RPM steps |
| **Startup test** | First-fire sequence |
| **Stall test** | N/A |
| **Ambient** | Engine running — vehicle only |
| **Artifact** | `E30LD-007_firing_profile.md` |

### E30LD-008 — injectors

| Field | Value |
|-------|-------|
| **Objective** | Peak and hold current per injector; sum at max simultaneous injection |
| **Instrumentation** | Current probe, scope |
| **Test connection** | ECU injector driver bank — **after OQ-007** |
| **Sampling rate** | ≥50 kSa/s |
| **Current range** | TBD |
| **Duration** | Map across RPM/load points per ECU map |
| **Normal operating test** | Max duty injection point |
| **Startup test** | Priming pulses if applicable |
| **Stall test** | N/A |
| **Ambient** | Engine running |
| **Artifact** | `E30LD-008_peak_hold.md` |

### E30LD-009 — starter_control

| Field | Value |
|-------|-------|
| **Objective** | Solenoid hold current; separate measurement of starter motor inrush (if accessible) |
| **Instrumentation** | High-current probe, voltage at battery |
| **Test connection** | **ADR** — path undefined |
| **Sampling rate** | ≥50 kSa/s for inrush |
| **Current range** | TBD — likely hundreds of A on motor circuit |
| **Duration** | Minimal crank cycles for data capture |
| **Normal operating test** | N/A — intermittent |
| **Startup test** | Crank event capture |
| **Stall test** | **HAZARD — SPECIALIST REVIEW** — extended crank prohibited |
| **Ambient** | Vehicle, secured, wheels chocked |
| **Artifact** | `E30LD-009_crank_event.md` |

### E30LD-010 — headlights_low / E30LD-011 — headlights_high

| Field | Value |
|-------|-------|
| **Objective** | Steady current per lamp set; dual ON simultaneous (GRP-LIGHTING-FRONT) |
| **Instrumentation** | 0–30 A probe |
| **Test connection** | Ch09, Ch10 feeds |
| **Sampling rate** | 1 kSa/s |
| **Current range** | TBD |
| **Duration** | 10 min each; 10 min both |
| **Normal operating test** | 12 V steady |
| **Startup test** | Inrush negligible — single capture |
| **Stall test** | N/A |
| **Ambient** | Thermal stabilization 5 min before log |
| **Artifact** | `E30LD-010_normal.md`, `E30LD-011_normal.md` |

### E30LD-012 — parking_lights

| Field | Value |
|-------|-------|
| **Objective** | Total current all position lamps on circuit |
| **Instrumentation** | 0–10 A probe |
| **Test connection** | Ch15 |
| **Sampling rate** | 1 kSa/s |
| **Current range** | TBD |
| **Duration** | 30 min |
| **Normal / startup** | Single steady capture |
| **Stall test** | N/A |
| **Artifact** | `E30LD-012_normal.md` |

### E30LD-013 — brake_lights / E30LD-015 — hazard_lights / E30LD-016 — indicators

| Field | Value |
|-------|-------|
| **Objective** | Steady current per circuit; flash duty for indicators/hazard |
| **Instrumentation** | 0–20 A probe, scope for flash profile |
| **Test connection** | **TBD** — harness survey OQ-021 |
| **Sampling rate** | 5 kSa/s for flash; 1 kSa/s steady |
| **Current range** | TBD |
| **Duration** | 15 min per mode |
| **Normal operating test** | Brake applied steady; indicator flash logged |
| **Startup test** | Lamp cold inrush |
| **Stall test** | N/A |
| **Artifact** | `E30LD-013_normal.md`, `E30LD-015_flash.md`, `E30LD-016_flash.md` |

### E30LD-014 — rear_rain_light (Optional)

| Field | Value |
|-------|-------|
| **Objective** | Confirm presence and steady current |
| **Instrumentation** | 0–5 A probe |
| **Test connection** | TBD after OQ-011 |
| **Sampling rate** | 1 kSa/s |
| **Duration** | 10 min if fitted |
| **Artifact** | `E30LD-014_normal.md` or presence-not-fitted record |

### E30LD-017 — horn

| Field | Value |
|-------|-------|
| **Objective** | I_steady while energized |
| **Instrumentation** | 0–30 A probe |
| **Test connection** | TBD channel |
| **Sampling rate** | 5 kSa/s |
| **Duration** | Short bursts — avoid thermal damage |
| **Normal operating test** | 2 s on / 5 s off × 10 |
| **Startup test** | Inrush capture |
| **Stall test** | N/A |
| **Artifact** | `E30LD-017_burst.md` |

### E30LD-018 — wipers / E30LD-019 — washer_pump

| Field | Value |
|-------|-------|
| **Objective** | Wiper: I per speed; stall at park; Washer: I_steady |
| **Instrumentation** | 0–30 A probe |
| **Test connection** | Ch16 wiper; washer TBD |
| **Sampling rate** | 5 kSa/s |
| **Duration** | Wiper: 5 min per speed; Washer: 30 s bursts |
| **Normal operating test** | Low/high wiper speed |
| **Startup test** | Park-to-sweep |
| **Stall test** | Wiper mechanical stop **HAZARD — SPECIALIST REVIEW** |
| **Artifact** | `E30LD-018_speeds.md`, `E30LD-019_burst.md` |

### E30LD-020 — heater_blower

| Field | Value |
|-------|-------|
| **Objective** | I vs PWM duty; audible noise baseline optional |
| **Instrumentation** | 0–30 A probe, PWM capture |
| **Test connection** | Ch11 |
| **Sampling rate** | 1 kSa/s steady; 10 kSa/s inrush |
| **Duration** | PWM 0–100 % sweep |
| **Normal operating test** | Max blower speed 10 min |
| **Startup test** | From 0 % PWM |
| **Stall test** | Blocked rotor **HAZARD — SPECIALIST REVIEW** |
| **Artifact** | `E30LD-020_pwm_map.md` |

### E30LD-021 — interior_equipment

| Field | Value |
|-------|-------|
| **Objective** | Aggregate current with sub-load checklist after harness survey |
| **Instrumentation** | 0–20 A probe |
| **Test connection** | TBD fused circuit |
| **Sampling rate** | 1 kSa/s |
| **Duration** | All interior loads ON 30 min |
| **Artifact** | `E30LD-021_aggregate.md` |

### E30LD-022 — tablet_supply

| Field | Value |
|-------|-------|
| **Objective** | Charge current profile; peak with tablet active |
| **Instrumentation** | 0–5 A probe |
| **Test connection** | TBD per OQ-017 |
| **Sampling rate** | 1 kSa/s |
| **Duration** | 60 min charge cycle |
| **Artifact** | `E30LD-022_charge.md` |

### E30LD-023 — window_fl / E30LD-024 — window_fr

| Field | Value |
|-------|-------|
| **Objective** | I_run, I_stall (brief), inrush up/down |
| **Instrumentation** | 0–30 A probe on HB1/HB2 |
| **Test connection** | Ch101, Ch102 |
| **Sampling rate** | 10 kSa/s |
| **Duration** | 10 full travel cycles each direction |
| **Normal operating test** | Mid-travel steady |
| **Startup test** | Direction reversal inrush |
| **Stall test** | End-stop **HAZARD — SPECIALIST REVIEW** — ≤500 ms captures only |
| **Artifact** | `E30LD-023_travel.md`, `E30LD-024_travel.md` |

### E30LD-025 — button_box

| Field | Value |
|-------|-------|
| **Objective** | I_nominal CAN node; inrush at power-on |
| **Instrumentation** | 0–2 A probe |
| **Test connection** | DTM12 +12V feed |
| **Sampling rate** | 5 kSa/s |
| **Duration** | 8 h soak optional for sleep current TBD |
| **Artifact** | `E30LD-025_power.md` |

### E30LD-026 — radio_board

| Field | Value |
|-------|-------|
| **Objective** | I_idle, I_WiFi_TX burst, I_BLE burst |
| **Instrumentation** | 0–5 A probe on Radio Board 12 V input |
| **Test connection** | Internal DCC bench harness |
| **Sampling rate** | ≥20 kSa/s for TX bursts |
| **Duration** | 30 min with scripted OTA/WiFi traffic |
| **Artifact** | `E30LD-026_tx_burst.md` |

---

## 7. Execution order (recommended)

1. Harness survey (OQ-021) — confirms test connection for unassigned loads  
2. Bench characterization: lights, horn, blower, windows (vehicle removed)  
3. Fluid-coupled: fuel, coolant pump (safety protocols)  
4. Vehicle running: ECU, coils, injectors, fans, EHPS  
5. Communication nodes: Button Box, Radio Board  
6. Update YAML and re-run simultaneous-group aggregation (GRP-*)

## 8. Related documents

- [E30_Gen1_Load_Inventory.md](E30_Gen1_Load_Inventory.md)
- [E30_Gen1_Open_Questions.md](E30_Gen1_Open_Questions.md)
- [config/vehicles/e30_gen1_loads.yaml](../../config/vehicles/e30_gen1_loads.yaml)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-003 initial measurement plan |
