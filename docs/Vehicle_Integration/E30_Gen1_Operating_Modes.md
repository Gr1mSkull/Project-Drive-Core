# BMW E30 Gen1 — Operating Modes

**Document ID:** VI-E30-OM-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-003

## 1. Purpose

Define expected load states per vehicle operating mode for BMW E30 Gen1. Supports channel requirement analysis and simultaneous-load planning.

Does **not** define unapproved safety reactions. Unresolved behaviors are marked **ARCHITECTURAL DECISION REQUIRED**.

## 2. Relationship to active config

Active VCM modes in [config/vehicles/e30_gen1.yaml](../../config/vehicles/e30_gen1.yaml):

`OFF` → `MASTER_ON` → `IGNITION` → `PRIME` → `READY` → `ENGINE_RUN` → `RACE` → `COOL_DOWN`

WP-003 adds conceptual modes for integration planning. Mapping:

| WP-003 mode | Active config mode | Notes |
|-------------|-------------------|-------|
| Vehicle Off | OFF | Master contactor open |
| Master On | MASTER_ON | Contactor closed, pre-ignition |
| Ignition On | IGNITION | |
| Fuel Prime | PRIME | Fuel pump prime window |
| Cranking | READY (partial) | **ADR:** READY exists; cranking-specific load table not in config |
| Engine Running | ENGINE_RUN | |
| Race | RACE | |
| Cool Down | COOL_DOWN | |
| Service | — | **ADR:** not in config v0.1 |
| Emergency Stop | — | **ADR:** kill switch / contactor — see §4 |
| DCC Degraded Mode | — | **ADR** |
| CAN Communication Loss | — | **ADR** |
| Button Box Communication Loss | — | **ADR** |

## 3. Load state legend

| Symbol | Meaning |
|--------|---------|
| **OFF** | Load commanded off |
| **ON** | Load commanded on |
| **AUTO** | Per rules, inputs, or ECU telemetry |
| **PRIME** | Timed prime behavior (fuel pump) |
| **CFG** | Follow active `outputs.*.modes` table |
| **ADR** | ARCHITECTURAL DECISION REQUIRED |
| **N/A** | Not applicable (not vehicle-switched load) |

## 4. Mode definitions

### 4.1 Vehicle Off

Main contactor open. DCC unpowered or in hard OFF. All DCC-switched loads **OFF**. ECU unpowered if fed from DCC Ch7.

### 4.2 Master On

Contactor closed. DCC alive in MASTER_ON. Most loads **OFF** per active config. EHPS, cooling, lighting remain off until later modes.

### 4.3 Ignition On

IGNITION mode. ECU power **ON** per config. Fuel pump **PRIME** per `fuel_prime_on_ignition` rule. Other loads predominantly **OFF** or **AUTO** per config.

### 4.4 Fuel Prime

PRIME mode. Fuel pump **ON** per config. Purpose: build fuel pressure before start.

### 4.5 Cranking

Starter engaged, engine not yet running. **ADR** for: EHPS enable during crank, fan/pump state, ECU hold-up, starter control path, simultaneous GRP-COOLING-HIGH policy.

### 4.6 Engine Running

ENGINE_RUN. Cooling loads **AUTO/ON** per config and rules. EHPS **ON**. Cabin/lighting **AUTO**.

### 4.7 Race

RACE. Simplified UI telemetry per architecture. Load table same as ENGINE_RUN unless architect defines race-specific derating (**ADR**).

### 4.8 Cool Down

COOL_DOWN. Fans and water pump may remain active per config. EHPS **OFF** per config. **ADR** for maximum cool-down duration and forced fan policy after kill.

### 4.9 Service

Maintenance / workshop. **ADR** for which loads may be energized on bench, interlocks, and VCM entry/exit.

### 4.10 Emergency Stop

Kill switch / master contactor policy per [docs/001](../001_System_Architecture.md) §9. **ADR** for: immediate load de-energization sequence, EHPS ramp-down, fuel pump cutoff timing, brake light fail-safe.

### 4.11 DCC Degraded Mode

Single-channel fault or partial DCC failure. **ADR** for per-load shedding order using criticality from load inventory.

### 4.12 CAN Communication Loss

ECU or Button Box heartbeat timeout. **ADR** for: cooling fallback without `engine_running`, fuel pump policy, lighting defaults.

### 4.13 Button Box Communication Loss

Button Box HEARTBEAT lost. **ADR** for: headlight/wiper/heater manual fallback, fan override loss, mode change restrictions.

## 5. Mode versus load matrix

Loads with DCC assignment or integration criticality. Spare channels omitted (expected **OFF** in all modes until assigned).

| Load key | Vehicle Off | Master On | Ignition On | Fuel Prime | Cranking | Engine Running | Race | Cool Down | Service | Emergency Stop | DCC Degraded | CAN Loss | BB Loss |
|----------|-------------|-----------|-------------|------------|----------|----------------|------|-----------|---------|----------------|--------------|----------|---------|
| ehps | OFF | OFF | OFF | OFF | ADR | ON | ON | OFF | ADR | ADR | ADR | ADR | ADR |
| water_pump | OFF | OFF | OFF | OFF | ADR | ON | ON | ON | ADR | ADR | ADR | ADR | ADR |
| fan1 | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | AUTO | ADR | ADR | ADR | ADR | ADR |
| fan2 | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | AUTO | ADR | ADR | ADR | ADR | ADR |
| fuel_pump | OFF | OFF | PRIME | ON | ADR | ON | ON | OFF | ADR | ADR | ADR | ADR | ADR |
| ecu_power | OFF | OFF | ON | ON | ON | ON | ON | ADR | ADR | ADR | ADR | ADR | ADR |
| ignition_coils | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | N/A |
| injectors | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | N/A |
| starter_control | OFF | OFF | ADR | OFF | ADR | OFF | OFF | OFF | ADR | ADR | ADR | ADR | ADR |
| headlights_low | OFF | OFF | AUTO | AUTO | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| headlights_high | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| parking_lights | OFF | OFF | AUTO | AUTO | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| brake_lights | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| rear_rain_light | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| hazard_lights | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| indicators | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| horn | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| wipers | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| washer_pump | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| heater_blower | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| interior_equipment | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | ADR | ADR | ADR |
| tablet_supply | OFF | OFF | ADR | ADR | ADR | ADR | ADR | OFF | ADR | OFF | ADR | ADR | ADR |
| window_fl | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| window_fr | OFF | OFF | OFF | OFF | ADR | AUTO | AUTO | OFF | ADR | ADR | ADR | ADR | ADR |
| button_box | OFF | ADR | ADR | ADR | ADR | ON | ON | ADR | ADR | ADR | ADR | ADR | ADR |
| radio_board | OFF | ADR | ADR | ADR | ADR | ADR | ADR | ADR | ADR | OFF | ADR | ADR | N/A |

**CFG note:** Where active config defines `outputs.*.modes`, ENGINE_RUNNING / RACE / COOL_DOWN / IGNITION columns reflect that table. Loads marked **AUTO** inherit rules in `e30_gen1.yaml` (fans, lights, wipers, heater, windows).

## 6. Simultaneous-load notes by mode

| Mode | Groups likely concurrent | Status |
|------|--------------------------|--------|
| Engine Running | GRP-COOLING-HIGH + GRP-ENGINE-CRITICAL + GRP-LIGHTING | Aggregate current **TBD** — measurement required |
| Race | Same as Engine Running | Race-specific derating **ADR** |
| Cranking | GRP-ENGINE-CRITICAL + starter | **ADR** — highest inrush risk |
| Cool Down | GRP-COOLING-HIGH without EHPS | Duration limit **ADR** |
| Emergency Stop | All → safe state | Reaction sequence **ADR** |

## 7. Related documents

- [E30_Gen1_Load_Inventory.md](E30_Gen1_Load_Inventory.md)
- [E30_Gen1_Open_Questions.md](E30_Gen1_Open_Questions.md)
- [docs/001_System_Architecture.md](../001_System_Architecture.md) §6 VCM
- [docs/005_Configuration_Model.md](../005_Configuration_Model.md)

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-003 initial mode matrix |
