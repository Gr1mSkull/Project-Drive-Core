# DevKit Electrical Interface Register — WP-010

**Document ID:** DOC-DK-EIR-001  
**Version:** 1.1  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-010 / WP-010-R1 (Accepted)  
**Date:** 2026-07-20

Functional interface definitions — **no final pinouts**.

## 1. Interface register

| Interface ID | End A | End B | Purpose | Signal classes | Power transferred | Safe default | Disconnect behaviour | Identity/version impact | Verification |
|--------------|-------|-------|---------|----------------|-------------------|--------------|----------------------|-------------------------|--------------|
| **IF-DK-POWER-IN** | Lab PSU | DevKit input entry | Controlled energy entry | `V_IN`, GND | Yes — full input | OFF — no connection | Outputs inhibited; stale commands on restoration | Baseline records input harness | VER-DCC-DK-A-002, A-003 |
| **IF-DK-JLP-CMD** | Logic board | Power board | RT command transport | SPI; PWM | None (control) | No valid commands | Comm loss → fail-safe OFF (TBD-DK-007 Open) | J_LP revision in composite baseline | VER-DCC-DK-A-007, A-008 |
| **IF-DK-JLP-SAFETY** | Logic / external | Power board | Hardwired safety signals | `nENABLE_GLOBAL`; `nRESET_PWR`; `nKILL_HW` (if on J_LP) | None (control) | Outputs inhibited | KILL direct branch effective without Logic CPU | Safety net revision | VER-DCC-DK-A-012 |
| **IF-DK-JLP-DIAG** | Power board | Logic board | Diagnostic/sense | Fault; current-observation path; VBATT; TEMP; BOARD_ID | None (sense) | Observability only | Degraded diagnostics | BOARD_ID map (TBD-DK-020) | VER-DCC-DK-A-015, C-004 |
| **IF-DK-DCPI** | Logic (RT) | Radio (Service) | Binary service link | DCPI frames (existing spec) | None | Service unavailable | RT continues fail-operational | DCPI protocol version in baseline | VER-DCC-DK-A-005, B-006, D-012 |
| **IF-DK-CAN** | Logic | CAN bus / test node | Vehicle bus representative | CAN FD | None | Bus loss ≠ power kill | Diagnostics degrade | CAN config version | VER-DCC-DK-A-010, B-* |
| **IF-DK-DEBUG-LOGIC** | Developer host | Logic | SWD / programming | SWD, UART | None | No output effect | Debug disconnect — no change | Toolchain version | VER-DCC-DK-A-001 |
| **IF-DK-DEBUG-RADIO** | Developer host | Radio | Service programming | UART/USB | None | No output effect | Independent from Logic debug | Toolchain version | VER-DCC-DK-B-006 |
| **IF-DK-BASE-LOAD** | Power HS/B outputs | Bench load | Representative load connection | `V_LOAD_BASE`, return | Switched load power | OFF — channel open | Safe when channel OFF (REQ-DCC-V-DK-026) | Load fixture ID in VE | VER-DCC-DK-C-001, C-002 |
| **IF-DK-BIDIRECTIONAL-LOAD** | Power BI output | Reversible load | BI verification | Bidirectional power + sense | Switched bidirectional | Both directions OFF | Conflict → both inhibited | Fixture ID | VER-DCC-DK-C-010, C-011 |
| **IF-DK-EXTERNAL-BANK** | EXT-SOURCE / EXT-LOAD-BANK / fixture | DevKit ext. interface | HC / high-energy testing | `V_LOAD_EXT`, control, sense | Fixture-supplied | OFF — de-energized | Back-feed into base distribution **prohibited**; ground/reference Open (OI-GND-001) | Fixture baseline separate | Phase E / bounded discovery |
| **IF-DK-KILL** | External kill switch | Power (direct branch) + Logic (observation) | Hardware emergency | Kill net — hardwired safety | None | Direct branch asserted = outputs inhibited | Direct branch independent of Service, Logic CPU, DCPI | Kill harness in baseline | VER-DCC-DK-A-012 |
| **IF-DK-MEASUREMENT** | Test equipment | MP-* points | Verification observation | Sense taps | None | N/A | Probe disconnect — no power effect | Instrument calibration records | All DK-A/C timing cases |

**J_LP aggregate:** IF-DK-JLP-CMD + IF-DK-JLP-SAFETY + IF-DK-JLP-DIAG compose the production J_LP boundary. `nKILL_HW` on J_LP is **hardwired safety signal carried by the interface** — not Logic-generated command transport.

## 2. Interface dependency graph

```text
IF-DK-POWER-IN → (powers) → Logic, Radio, Power
IF-DK-JLP-CMD + IF-DK-JLP-SAFETY → (controls) → Power outputs
IF-DK-KILL → (direct branch disables) → Power outputs — independent of Logic CPU
IF-DK-KILL → (observation branch) → Logic logging / recovery FSM
IF-DK-DCPI → (services) → Radio ↔ Logic (no direct power)
IF-DK-BASE-LOAD → (loads) → CH-HS-* channels
IF-DK-BIDIRECTIONAL-LOAD → (loads) → CH-BI-REP
IF-DK-EXTERNAL-BANK → (functionally separated from) → base distribution [ground/reference Open — OI-GND-001]
```

## 3. Production intent alignment

| DevKit interface | Production reference | Fidelity |
|------------------|---------------------|----------|
| IF-DK-JLP-* (aggregate) | J_LP (docs/002 §9) | Production-interface-conformant (ADR-016 Option B) |
| IF-DK-DCPI | DCPI (docs/004) | Contract-conformant (ADR-017 Option B) |
| IF-DK-CAN | Vehicle CAN FD | Representative node |
| IF-DK-KILL | J_DIN kill path + direct branch | Electrically representative |

Connector family and pin assignment: **Open** (ADR-DK-012).

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial electrical interface register — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — J_LP signal-class split; KILL direct branch; external energy boundary |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #14 merged (`c98ce56`) |
