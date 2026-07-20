# DevKit Fixture Energy and Safety Boundary — WP-014

**Document ID:** DOC-DK-FESB-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Energy-boundary REQUIREMENTS only — no ratings, MPN, isolation topology, or construction Approved.
OI-GND-001 remains Open.
```

## 1. Energy-domain definitions (Accepted terminology)

| Domain | Definition |
|--------|------------|
| **BASE-SOURCE** | Energy source for the base DevKit envelope |
| **EXT-SOURCE** | Independent external source of electrical energy |
| **EXT-LOAD-BANK** | Controlled external load that **absorbs** energy (not a source) |
| **EXT-POWER-MODULE** | External representative switching/protection module |
| **DUT** | DevKit or controlled subassembly under test |
| **FIXTURE-AUX** | Fixture-local control and measurement power |

**Prohibited descriptions:** load bank as energy source; combining external and base envelopes into one rating.

## 2. Mandatory envelope constraints (carry-forward)

| Constraint | Status | Source |
|------------|--------|--------|
| Base and external energy envelopes remain distinct | ACCEPTED_CONSTRAINT | PWR-A-001; ADR-021 |
| External ratings do not increase `I_certified_cont` | ACCEPTED_CONSTRAINT | PWR-A-002; ADR-021 |
| External verification does not certify the base distribution path | ACCEPTED_CONSTRAINT | ADR-020/021 |
| Back-feed into base distribution is prohibited | ACCEPTED_CONSTRAINT | PWR-A-003 |
| External energization requires explicit fixture authority | **PROPOSED_CONSTRAINT** (WP-014) | — |
| External energy has an independent removal path | **PROPOSED_CONSTRAINT** (WP-014) | — |
| Measurement points identify the applicable energy envelope | **PROPOSED_CONSTRAINT** (WP-014) | WP-012 MP discipline |
| Verification evidence identifies the applicable envelope | ACCEPTED_CONSTRAINT (governance) | DK-GOV / ADR-020 |
| Fixture failure shall not silently combine energy sources | **PROPOSED_CONSTRAINT** (WP-014) | — |

## 3. Evidence scopes (distinct)

```text
Base-envelope evidence
External-source evidence
External-load-bank evidence
External-power-module evidence
Combined-interface evidence
```

**Combined-interface testing shall not imply combined electrical certification.**

## 4. Ground and reference boundary

**OI-GND-001** remains **Open** (ARCHITECTURE_OPEN).

WP-014 does **not** select: galvanic isolation · controlled common reference · single-point reference · fixture-defined differential interface.

**Boundary statement:**

```text
Functionally separated and protected against back-feed;
ground/reference relationship remains Open under OI-GND-001.
```

Diagrams shall label:

```text
Open decision — OI-GND-001
```

Do **not** imply isolation merely because sources are functionally separated.

Requirements dependent on grounding/reference decision: **BLOCKED_BY_ARCHITECTURE**.

## 5. Emergency energy removal vs DUT KILL

### 5.1 Fixture E-stop

Shall:

- remove or inhibit fixture-controlled hazardous energy;
- remove external energy independently of DevKit firmware;
- not require Radio, Tablet, SPI/DCPI, or DUT firmware;
- default to energy-inhibited state;
- require deliberate reset;
- invalidate previous test commands;
- prevent automatic test resumption.

### 5.2 DUT physical KILL (Accepted)

```text
Physical KILL
├── direct hardware-effective Power-disable path
└── parallel Logic observation path
```

Fixture E-stop **shall not** replace DUT physical KILL.  
DUT physical KILL **shall not** replace fixture E-stop.

### 5.3 Non-merged authorities

```text
Fixture E-stop
DUT physical KILL
nENABLE_GLOBAL
source output enable
fault-injection enable
load-bank enable
```

Remain distinct. `nENABLE_GLOBAL` defaults inactive (PWR-A-005).

## 6. Residual / stored energy

Energy-removal timing is:

```text
energy-removal / rail-collapse / stored-energy-decay dependent;
numeric limit Open
```

Do **not** claim instantaneous energy removal. Inductive and capacitive stored energy require controlled discharge or confirmed safe decay before RECOVERY_VALIDATION exit where the profile depends on it.

## 7. Traceability

ADR-020/021 · PWR-A-001…005/009 · OI-GND-001 · OI-FIX-001 · WP-012 envelopes · REQ-DCC-V-FX-*.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture energy and safety boundary — Proposed |
