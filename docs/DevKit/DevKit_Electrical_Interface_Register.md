# DevKit Electrical Interface Register — WP-010

**Document ID:** DOC-DK-EIR-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010  
**Date:** 2026-07-20

Functional interface definitions — **no final pinouts**.

## 1. Interface register

| Interface ID | End A | End B | Purpose | Signal classes | Power transferred | Safe default | Disconnect behaviour | Identity/version impact | Verification |
|--------------|-------|-------|---------|----------------|-------------------|--------------|----------------------|-------------------------|--------------|
| **IF-DK-POWER-IN** | Lab PSU | DevKit input entry | Controlled energy entry | `V_IN`, GND | Yes — full input | OFF — no connection | Outputs safe when disconnected | Baseline records input harness | VER-DCC-DK-A-002, A-003 |
| **IF-DK-JLP** | Logic board | Power board | RT control of power domain | SPI, PWM, kill, enable, fault, sense, BOARD_ID | Low power (logic) | Outputs OFF — fail-safe | Comm loss → fail-safe OFF (TBD-DK-007 Open) | BOARD_ID; J_LP revision in composite baseline | VER-DCC-DK-A-007, A-008, A-015 |
| **IF-DK-DCPI** | Logic (RT) | Radio (Service) | Binary service link | DCPI frames (existing spec) | None | Service unavailable | RT continues fail-operational | DCPI protocol version in baseline | VER-DCC-DK-A-005, B-006, D-012 |
| **IF-DK-CAN** | Logic | CAN bus / test node | Vehicle bus representative | CAN FD | None | Bus loss ≠ power kill | Diagnostics degrade | CAN config version | VER-DCC-DK-A-010, B-* |
| **IF-DK-DEBUG-LOGIC** | Developer host | Logic | SWD / programming | SWD, UART | None | No output effect | Debug disconnect — no change | Toolchain version | VER-DCC-DK-A-001 |
| **IF-DK-DEBUG-RADIO** | Developer host | Radio | Service programming | UART/USB | None | No output effect | Independent from Logic debug | Toolchain version | VER-DCC-DK-B-006 |
| **IF-DK-BASE-LOAD** | Power HS/B outputs | Bench load | Representative load connection | `V_LOAD_BASE`, return | Switched load power | OFF — channel open | Safe when channel OFF (REQ-DCC-V-DK-026) | Load fixture ID in VE | VER-DCC-DK-C-001, C-002 |
| **IF-DK-BIDIRECTIONAL-LOAD** | Power BI output | Reversible load | BI verification | Bidirectional power + sense | Switched bidirectional | Both directions OFF | Conflict → OFF | Fixture ID | VER-DCC-DK-C-010, C-011 |
| **IF-DK-EXTERNAL-BANK** | External fixture | DevKit ext. interface | HC / high-energy testing | `V_LOAD_EXT`, control, sense | Fixture-supplied | OFF — de-energized | Must not back-feed base (ADR-020/021) | Fixture baseline separate | Phase E / bounded discovery |
| **IF-DK-KILL** | External kill switch | Logic/Power kill chain | Hardware emergency | Kill net | None | Asserted = safe | Kill effective independent of Service | Kill harness in baseline | VER-DCC-DK-A-012 |
| **IF-DK-MEASUREMENT** | Test equipment | MP-* points | Verification observation | Sense taps | None | N/A | Probe disconnect — no power effect | Instrument calibration records | All DK-A/C timing cases |

## 2. Interface dependency graph

```text
IF-DK-POWER-IN → (powers) → Logic, Radio, Power
IF-DK-JLP → (controls) → Power outputs
IF-DK-KILL → (disables) → Power outputs via hardware AND
IF-DK-DCPI → (services) → Radio ↔ Logic (no direct power)
IF-DK-BASE-LOAD → (loads) → CH-HS-* channels
IF-DK-BIDIRECTIONAL-LOAD → (loads) → CH-BI-REP
IF-DK-EXTERNAL-BANK → (isolated from) → base input [Open detail]
```

## 3. Production intent alignment

| DevKit interface | Production reference | Fidelity |
|------------------|---------------------|----------|
| IF-DK-JLP | J_LP (docs/002 §9) | Production-interface-conformant (ADR-016 Option B) |
| IF-DK-DCPI | DCPI (docs/004) | Contract-conformant (ADR-017 Option B) |
| IF-DK-CAN | Vehicle CAN FD | Representative node |
| IF-DK-KILL | J_DIN kill path | Electrically representative |

Connector family and pin assignment: **Open** (ADR-DK-012).

## 4. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial electrical interface register — Proposed |
