# BMW E30 Gen1 — Electrical Load Inventory

**Document ID:** VI-E30-LD-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-003

## 1. Purpose

Authoritative inventory of electrical loads for the BMW E30 Gen1 DriveCore integration. Defines requirements that future DCC power channels must satisfy.

This document does **not** select semiconductors, fuses, connectors, or wire sizes. It does **not** assign final channel current ratings.

## 2. Canonical data

| Artifact | Path |
|----------|------|
| Machine-readable inventory | [config/vehicles/e30_gen1_loads.yaml](../../config/vehicles/e30_gen1_loads.yaml) |
| Active DCC behavior config (unchanged) | [config/vehicles/e30_gen1.yaml](../../config/vehicles/e30_gen1.yaml) |
| Operating modes | [E30_Gen1_Operating_Modes.md](E30_Gen1_Operating_Modes.md) |
| Measurement plan | [E30_Gen1_Load_Measurement_Plan.md](E30_Gen1_Load_Measurement_Plan.md) |
| Open questions | [E30_Gen1_Open_Questions.md](E30_Gen1_Open_Questions.md) |
| Load profile template | [Load_Profile_Template.md](../templates/Load_Profile_Template.md) |

**Load ID** (`E30LD-XXX`) is the stable primary key. **Load key** (`snake_case`) aligns with `outputs` keys in active config where assigned.

## 3. Conventions

- **Presence:** Confirmed = in vehicle scope or active config; Planned = expected; Optional = regulation/series dependent; TBD = architect confirmation required.
- **Electrical values:** All load currents are **TBD** (`null` in YAML) until measured per measurement plan. Nominal supply **12 V** is vehicle system nominal (architecture reference), not a per-load measured value.
- **DCC channel** references are **hardware capacity bindings** from active config or reserve map — not qualified current ratings.
- **Evidence status:** `unknown` until bench or datasheet evidence is recorded.

## 4. Load registry summary

| Load ID | Load key | Functional name | Presence | DCC ch | Class | Criticality | Meas. req. |
|---------|----------|-----------------|----------|--------|-------|-------------|------------|
| E30LD-001 | ehps | Electric hydraulic power steering pump | Confirmed | 1 | HS60 | critical | yes |
| E30LD-002 | water_pump | Electric coolant pump | Confirmed | 5 | HS30 | critical | yes |
| E30LD-003 | fan1 | Radiator fan 1 | Confirmed | 3 | HS30 | high | yes |
| E30LD-004 | fan2 | Radiator fan 2 | Confirmed | 4 | HS30 | high | yes |
| E30LD-005 | fuel_pump | Fuel pump | Confirmed | 6 | HS30 | critical | yes |
| E30LD-006 | ecu_power | Engine ECU supply | Confirmed | 7 | HS15 | critical | yes |
| E30LD-007 | ignition_coils | Ignition coils supply | TBD | — | — | critical | yes |
| E30LD-008 | injectors | Injectors supply | TBD | — | — | critical | yes |
| E30LD-009 | starter_control | Starter control | Planned | — | — | high | yes |
| E30LD-010 | headlights_low | Low beam | Confirmed | 9 | HS15 | medium | yes |
| E30LD-011 | headlights_high | High beam | Confirmed | 10 | HS15 | medium | yes |
| E30LD-012 | parking_lights | Position lights | Confirmed | 15 | HS05 | low | yes |
| E30LD-013 | brake_lights | Brake lights | Planned | — | — | high | yes |
| E30LD-014 | rear_rain_light | Rear rain light | Optional | — | — | low | yes |
| E30LD-015 | hazard_lights | Hazard lights | Planned | — | — | medium | yes |
| E30LD-016 | indicators | Indicators | Planned | — | — | medium | yes |
| E30LD-017 | horn | Horn | Planned | — | — | medium | yes |
| E30LD-018 | wipers | Windscreen wiper motor | Confirmed | 16 | HS05 | medium | yes |
| E30LD-019 | washer_pump | Washer pump | Planned | — | — | low | yes |
| E30LD-020 | heater_blower | Heater blower | Confirmed | 11 | HS15 | medium | yes |
| E30LD-021 | interior_equipment | Interior electrical equipment | Planned | — | — | low | yes |
| E30LD-022 | tablet_supply | USB / tablet supply | Planned | — | — | low | yes |
| E30LD-023 | window_fl | Power window FL | Confirmed | 101 | HB | low | yes |
| E30LD-024 | window_fr | Power window FR | Confirmed | 102 | HB | low | yes |
| E30LD-025 | button_box | Button Box | Confirmed | — | — | high | yes |
| E30LD-026 | radio_board | DCC Radio Board | Confirmed | — | — | low | yes |
| E30LD-027 | spare_ch02 | Spare — Ch02 | Confirmed | 2 | HS60 | TBD | no |
| E30LD-028 | spare_ch08 | Spare — Ch08 | Confirmed | 8 | HS15 | TBD | no |
| E30LD-029 | spare_ch12 | Spare — Ch12 | Confirmed | 12 | HS15 | TBD | no |
| E30LD-030 | spare_ch13 | Spare — Ch13 | Confirmed | 13 | HS15 | TBD | no |
| E30LD-031 | spare_ch14 | Spare — Ch14 | Confirmed | 14 | HS15 | TBD | no |
| E30LD-032 | spare_ch17 | Spare — Ch17 | Confirmed | 17 | HS05 | TBD | no |
| E30LD-033 | spare_ch18 | Spare — Ch18 | Confirmed | 18 | HS05 | TBD | no |
| E30LD-034 | spare_ch19 | Spare — Ch19 | Confirmed | 19 | HS05 | TBD | no |
| E30LD-035 | spare_ch20 | Spare — Ch20 | Confirmed | 20 | HS05 | TBD | no |
| E30LD-036 | spare_ch21 | Spare — Ch21 | Confirmed | 21 | HS05 | TBD | no |
| E30LD-037 | spare_ch22 | Spare — Ch22 | Confirmed | 22 | HS05 | TBD | no |

Full field records: see YAML (37 loads, all mandatory fields populated).

## 5. Simultaneous-operation groups

| Group ID | Members | Notes |
|----------|---------|-------|
| GRP-COOLING-HIGH | ehps, water_pump, fan1, fan2 | Worst-case overlap in ENGINE_RUN / RACE — aggregate current TBD |
| GRP-ENGINE-CRITICAL | ecu_power, fuel_pump, ignition_coils, injectors | Fuel pump + ECU during crank/run — timing TBD |
| GRP-LIGHTING-FRONT | headlights_low, headlights_high, parking_lights | Dual-beam simultaneous use TBD |
| GRP-LIGHTING-REAR | brake_lights, indicators, hazard_lights, rear_rain_light | Regulatory combinations TBD |
| GRP-CABIN | heater_blower, wipers, washer_pump, interior_equipment | Cabin comfort aggregate TBD |
| GRP-WINDOWS | window_fl, window_fr | Concurrent operation policy TBD |
| GRP-AUX | horn, tablet_supply | Non-safety auxiliary |
| GRP-CAN-NODES | button_box, radio_board | Peripheral node power — not DCC HS outputs |

## 6. DCC assignment status (WP-003)

| Status | Count | Load keys |
|--------|-------|-----------|
| Assigned in active config | 14 | ehps, fan1, fan2, water_pump, fuel_pump, ecu_power, headlights_low, headlights_high, parking_lights, heater_blower, wipers, window_fl, window_fr |
| Reserve channel only | 11 | spare_ch02, spare_ch08, spare_ch12–14, spare_ch17–22 |
| Not DCC-switched / TBD channel | 12 | ignition_coils, injectors, starter_control, brake_lights, rear_rain_light, hazard_lights, indicators, horn, washer_pump, interior_equipment, tablet_supply, button_box, radio_board |

## 7. Field reference

Every load record in YAML includes:

Load ID, functional name, presence, physical location, load technology, inductive/resistive/electronic classification, nominal supply voltage, nominal current, maximum continuous current, startup/inrush current, startup duration, stall current, PWM requirement, PWM frequency range, reverse-current behavior, regenerative behavior, switching frequency, operating duty cycle, maximum continuous operating time, simultaneous-operation group, criticality, required degraded behavior, safe state, diagnostic requirements, open-load detection requirement, current measurement requirement, retry policy requirement, external fuse requirement, connector requirement status, wire requirement status, data source, evidence status, measurement required, notes.

## 8. Related documents

- [docs/001_System_Architecture.md](../001_System_Architecture.md) — E30 electrical architecture
- [docs/002_DCC_Hardware.md](../002_DCC_Hardware.md) — channel hardware capacity (not load ratings)
- [docs/003_ECU_Architecture.md](../003_ECU_Architecture.md) — ECU power boundary
- [docs/005_Configuration_Model.md](../005_Configuration_Model.md) — active config schema

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-003 initial inventory |
