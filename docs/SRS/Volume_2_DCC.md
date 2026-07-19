# SRS — Volume 2: DCC Requirements

**Document ID:** SRS-V2  
**Version:** 0.2  
**Status:** Proposed  
**Work Package:** WP-001 · **Update:** WP-007

> **Note:** Chapter structure with selective population. Full requirement text lives in linked normative sources where noted.

## Document control

| Field | Value |
|-------|-------|
| Module | DriveCore Controller (DCC) |
| Related | `docs/002`, `docs/004`, `docs/005`, `docs/006`, `docs/007` |

---

## 1. Introduction

### 1.1 Purpose  
### 1.2 Scope  
### 1.3 References  

---

## 2. DCC overview

### 2.1 Three-board architecture  
<!-- Logic, Power, Radio — docs/002 -->

### 2.2 Internal interfaces  
<!-- J_LP, J_EXP — EDL-011 -->

### 2.3 External interfaces  
<!-- CAN, vehicle loads, kill, USB -->

---

## 3. Hardware requirements

### 3.1 Logic board  
<!-- REQ-DCC-HW-L-NNN -->

### 3.2 Power board  
<!-- REQ-DCC-HW-P-NNN: channel classes, not MPN -->

### 3.3 Radio board  
<!-- REQ-DCC-HW-R-NNN -->

### 3.4 Enclosure and environmental  
<!-- REQ-DCC-HW-E-NNN -->

---

## 4. Functional requirements

### 4.1 Power distribution  
<!-- REQ-DCC-F-PD-NNN -->

### 4.2 Vehicle state management (VCM)  
<!-- REQ-DCC-F-VCM-NNN -->

### 4.3 Load control and PWM  
<!-- REQ-DCC-F-LC-NNN -->

### 4.4 Rules engine  
<!-- REQ-DCC-F-RULE-NNN -->

### 4.5 Diagnostics and logging  
<!-- REQ-DCC-F-DIAG-NNN -->

---

## 5. Communication requirements

### 5.1 CAN (DCP)  
<!-- REQ-DCC-C-CAN-NNN -->

### 5.2 DCPI (SPI to ESP32)  
<!-- REQ-DCC-C-SPI-NNN -->

### 5.3 REST / WebSocket  
<!-- REQ-DCC-C-API-NNN -->

---

## 6. Configuration requirements

### 6.1 YAML schema  
<!-- REQ-DCC-CFG-NNN -->

### 6.2 Binary config (DCFG)  
<!-- REQ-DCC-CFG-BIN-NNN -->

---

## 7. Safety and failure requirements

### 7.1 Fail-safe behavior  
<!-- REQ-DCC-S-NNN -->

### 7.2 Kill and enable chain  
<!-- REQ-DCC-S-KILL-NNN -->

### 7.3 Thermal management  
<!-- REQ-DCC-S-TH-NNN -->

---

## 8. Verification

### 8.1 DevKit requirements

**Normative DevKit requirements (Proposed):**

```text
docs/DevKit/DevKit_System_Requirements.md
```

| Field | Value |
|-------|-------|
| Atomic identifier range | `REQ-DCC-V-DK-001` … `REQ-DCC-V-DK-118` |
| Status | Proposed — requires Architecture Review |
| Scope | Gen1 DevKit verification platform: boundary, fidelity, bench safety, kill/enable, representative power capability, RT/Service, CAN/sim, configuration, testability, revision identity, maintainability |
| Verification plan | `docs/DevKit/DevKit_Verification_Plan.md` (Gates DK-A…DK-D) |
| Relationship to EDL-014 | DevKit gates support but do **not** replace Phase E on full DCC Gen1; vehicle install still gated by EDL-014 |
| System validation overview | `docs/008_Testing_and_Validation.md` |
| Traceability | Primary matrix rows in `docs/traceability/TRACEABILITY_MATRIX.md` — status `NOT VERIFIED` |

Do not duplicate full requirement text in this SRS volume.

### 8.2 Test traceability

See `docs/traceability/TRACEABILITY_MATRIX.md` and `docs/DevKit/DevKit_Verification_Plan.md`.

---

## Revision history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-07-12 | WP-001 chapter structure only |
| 0.2 | 2026-07-19 | WP-007 — §8.1 DevKit requirements pointer and ID range |
