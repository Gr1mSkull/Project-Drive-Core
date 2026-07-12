# SRS — Volume 3: ECU Requirements

**Document ID:** SRS-V3  
**Version:** 0.1 (structure only)  
**Status:** Proposed  
**Work Package:** WP-001

> **Note:** Chapter structure only. Engine control requirements are Phase 2. Boundary requirements only where architecture is fixed.

## Document control

| Field | Value |
|-------|-------|
| Module | DriveCore ECU |
| Related | `docs/003`, `docs/004`, EDL-005, EDL-012 |

---

## 1. Introduction

### 1.1 Purpose  
### 1.2 Scope  
<!-- Engine only; not body controller -->

### 1.3 References  

---

## 2. ECU overview

### 2.1 Responsibility boundary  
<!-- vs DCC — EDL-005 -->

### 2.2 Interaction with DCC  
<!-- Request-don't-control, cooling_request -->

---

## 3. Hardware requirements

### 3.1 ECU platform outline  
<!-- REQ-ECU-HW-NNN — TBD Phase 2 -->

### 3.2 Sensors and actuators  
<!-- REQ-ECU-HW-SENS-NNN -->

### 3.3 Connectors and power  
<!-- REQ-ECU-HW-CONN-NNN -->

---

## 4. Functional requirements

### 4.1 Engine control  
<!-- REQ-ECU-F-ENG-NNN — Phase 2, placeholders -->

### 4.2 Engine protection  
<!-- REQ-ECU-F-PROT-NNN -->

### 4.3 Cooling request  
<!-- REQ-ECU-F-COOL-NNN -->

---

## 5. Communication requirements

### 5.1 CAN telemetry  
<!-- REQ-ECU-C-TEL-NNN, msg 0x20 -->

### 5.2 CAN commands (receive)  
<!-- REQ-ECU-C-CMD-NNN -->

### 5.3 Heartbeat and node health  
<!-- REQ-ECU-C-HB-NNN -->

---

## 6. Configuration and calibration

### 6.1 ECU profile  
<!-- config/ecu/ — TBD -->

### 6.2 Calibration storage  
<!-- REQ-ECU-CFG-NNN -->

---

## 7. Safety requirements

### 7.1 Limp modes  
<!-- REQ-ECU-S-NNN -->

### 7.2 CAN loss behavior  
<!-- REQ-ECU-S-CAN-NNN -->

---

## 8. Verification

### 8.1 Simulator / third-party ECU (Gen1)  
<!-- EDL-012 -->

### 8.2 Test traceability  

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-07-12 | WP-001 chapter structure only |
