# BMW E30 Gen1 — Open Questions

**Document ID:** VI-E30-OQ-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-003

## 1. Purpose

Track unresolved integration questions and items requiring System Architect decision before channel ratings, harness design, or config updates.

## 2. Open questions

| ID | Topic | Question | Blocks |
|----|-------|----------|--------|
| OQ-001 | EHPS variant | Which electric hydraulic steering pump is fitted (OEM retrofit vs aftermarket)? | E30LD-001 measurement, Ch01 rating |
| OQ-002 | Coolant pump | Electric pump model and PWM control compatibility? | E30LD-002 PWM range |
| OQ-003 | Radiator fans | Single-speed vs dual-speed fans; OEM vs aftermarket current draw? | E30LD-003, E30LD-004 |
| OQ-004 | Fuel pump | In-tank pump specification (pressure/flow vs current)? | E30LD-005 |
| OQ-005 | ECU type | DriveCore ECU vs third-party ECU with CAN adapter? | E30LD-006, 007, 008 boundaries |
| OQ-006 | Ignition feed | Are coils powered from ECU J_IGN only, or separate DCC feed per docs/001 footnote? | E30LD-007 channel assignment |
| OQ-007 | Injector feed | Total injector current at peak simultaneous injection? | E30LD-008 |
| OQ-008 | Starter | Is starter solenoid controlled by DCC, ECU, or standalone circuit? | E30LD-009 |
| OQ-009 | Lighting technology | Halogen retained vs LED retrofit per circuit? | E30LD-010–016 classification |
| OQ-010 | Brake lights | Switch type (NC/NO), dual-filament sharing, DCC channel assignment? | E30LD-013 |
| OQ-011 | Rear rain light | Required for target series/regulations? | E30LD-014 presence |
| OQ-012 | Hazard / indicators | Electronic flasher vs DCC-switched; combined filament wiring? | E30LD-015, E30LD-016 |
| OQ-013 | Horn | Single vs dual horn; reserve channel selection (Ch08–14, Ch17–22)? | E30LD-017 |
| OQ-014 | Wiper | Park circuit integration; intermittent speed control path? | E30LD-018 |
| OQ-015 | Washer | Paired with wiper stalk only or separate output? | E30LD-019 |
| OQ-016 | Interior aggregate | Decompose dome, map lights, gauges, USB into sub-loads? | E30LD-021 |
| OQ-017 | Tablet supply | Dedicated DCC channel vs USB from Radio Board vs always-on feed? | E30LD-022 |
| OQ-018 | Window stall | Anti-pinch and stall current policy for H-bridge channels? | E30LD-023, E30LD-024 |
| OQ-019 | Button Box power | DTM12 +12V pin vs dedicated fused feed from DCC spare channel? | E30LD-025 |
| OQ-020 | Radio Board inrush | ESP32 Wi-Fi/BLE peak current on 12 V input? | E30LD-026 |
| OQ-021 | Harness survey | Full wire trace from E30 OEM fuse box to planned DCC outputs? | All loads |
| OQ-022 | READY vs Cranking | Map VCM READY to cranking load table or add CRANKING mode to config v0.2? | Operating modes |
| OQ-023 | Aggregate current | Simultaneous GRP-COOLING-HIGH + GRP-ENGINE-CRITICAL ceiling at 12 V bus? | Channel class validation |

## 3. Architectural decisions required

| ID | Decision | Context | Impact |
|----|----------|---------|--------|
| ADR-E30-001 | Cranking load policy | EHPS, fans, pump during starter engagement | Mode matrix §4.5 |
| ADR-E30-002 | Emergency stop load sequence | Order of fuel pump, EHPS, ECU power cutoff | Mode matrix §4.10 |
| ADR-E30-003 | DCC degraded shedding | Priority order when channels fault | Mode matrix §4.11 |
| ADR-E30-004 | CAN loss cooling fallback | Fan/pump behavior without valid ECU telemetry | Mode matrix §4.12 |
| ADR-E30-005 | Button Box loss fallback | Manual lighting/wiper/heater without BB events | Mode matrix §4.13 |
| ADR-E30-006 | Service mode entry | Workshop energization rules and interlocks | Mode matrix §4.9 |
| ADR-E30-007 | Brake light safe state | Fail-safe behavior on DCC fault | E30LD-013 |
| ADR-E30-008 | Ignition/coils DCC feed | Separate HS channel vs ECU-internal only | E30LD-007 |
| ADR-E30-009 | Reserve channel allocation | Map horn, washer, brake, indicators to Ch02/08/12–14/17–22 | Multiple loads |
| ADR-E30-010 | Race mode derating | EHPS/fan policy distinct from ENGINE_RUN | Mode matrix §4.7 |
| ADR-E30-011 | Cool-down timeout | Maximum fan/pump run after engine stop | Mode matrix §4.8 |
| ADR-E30-012 | Window simultaneous run | Allow FL+FR concurrent or mutex | GRP-WINDOWS |

## 4. Out of scope (WP-003)

- Semiconductor or fuse selection
- Connector part numbers
- Wire gauge selection
- Merging `e30_gen1_loads.yaml` into active DCC config
- Modifying `config/vehicles/e30_gen1.yaml`

## 5. Related documents

- [E30_Gen1_Load_Inventory.md](E30_Gen1_Load_Inventory.md)
- [E30_Gen1_Operating_Modes.md](E30_Gen1_Operating_Modes.md)
- [E30_Gen1_Load_Measurement_Plan.md](E30_Gen1_Load_Measurement_Plan.md)
- [docs/ADR/README.md](../ADR/README.md)

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-003 initial open questions |
