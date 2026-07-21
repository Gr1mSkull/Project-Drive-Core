# DevKit Fixture Measurement and DAQ Architecture — WP-015

**Document ID:** DOC-DK-FMDA-001  
**Version:** 1.1  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
Measurement / DAQ / observation FUNCTIONAL architecture only.
No instrument selection, bandwidth, accuracy, connector, or calibration value approved.
An instrument connection shall not become an uncontrolled energy path.
```

## 1. Measurement boundary principle

`FX-MEASUREMENT` is **observation-purpose**.

```text
A physical measurement connection shall be treated as a potential
energy / reference / fault path until its impedance, protection, reference,
isolation and fault behavior are qualified.
```

A physical measurement connection may carry fault energy, create an unintended reference path, link base and external envelopes, form a back-feed path through the instrument, or violate a later-selected ground/isolation architecture. Where a required measurement is unavailable, dependent tests are **blocked**. Measurements shall not be combined across boundaries without an explicit power-balance model. No isolation topology is selected (OI-GND-001 Open).

### 1.1 Measurement concept separation

| Concept | Meaning |
|---------|---------|
| measurement function | the quantity to be observed |
| measurement conductor | the physical wire/path (potential energy/fault path) |
| instrument input | the instrument's terminal (finite impedance; possible energy path) |
| reference connection | the reference/return the measurement is taken against (potential cross-envelope link) |
| safety observation | an observation consumed by the safety layer |
| independent reference instrument | a separate, qualified instrument used for evidence independence |

### 1.2 Per-boundary dependencies (all Open)

Each measurement boundary carries the following dependencies, all **Open**:

- maximum available fault-energy dependency — Open;
- reference-path dependency;
- input-impedance dependency;
- protection / current-limiting dependency;
- instrument ground/reference dependency;
- failure behavior (open / short / reference-fault);
- blocker `OI-GND-001` where the boundary crosses or references envelopes.

No isolation topology is selected.

## 2. Measurement boundaries (§21)

Sign convention: **positive current = draw from the associated source; negative current = return toward the associated source.**

| Measurement | Purpose | Physical boundary | Sign convention | Reference boundary | Bandwidth class | Transient capture | Accuracy dependency | Isolation dependency | DAQ consumer | Calibration dependency | Verification case mapping | Blocker |
|-------------|---------|-------------------|-----------------|--------------------|-----------------|-------------------|---------------------|----------------------|--------------|------------------------|---------------------------|---------|
| `I_LOAD_n` | Per-load current | Channel output→load | + draw / − return | per envelope | Open | may be required | Open | OI-GND-001 | FX-DAQ | Proposed | C-002…006 (future) | ratings Open |
| `I_CH_IN_n` | Source-referred channel current | Channel input (signed) | signed | — | Open | — | Open | — | FX-DAQ | Proposed | C-004/005 | OI-SENSE-001 |
| `I_DOM_IN_x` | Domain input current | Domain rail | signed | — | Open | — | Open | — | FX-DAQ | Proposed | A-002 | thresholds Open |
| `I_ENTRY_MEAS` | Envelope entry current | Fixture/DUT entry | + draw | per envelope | Open | — | Open | OI-GND-001 | FX-DAQ | Proposed | A-002/C-002 | thresholds Open |
| `V_DUT_ENTRY` | DUT entry voltage | DUT entry | — | per envelope | Open | UV/OV capture | Open | OI-GND-001 | FX-DAQ | Proposed | A-002/C-008 | UV table Open |
| `V_DOMAIN_x` | Domain rail voltage | Domain rail | — | — | Open | — | Open | — | FX-DAQ | Proposed | A-003 | thresholds Open |
| `V_CHANNEL_n` | Channel voltage | Channel node | — | — | Open | — | Open | — | FX-DAQ | Proposed | C-004 | — |
| `V_LOAD_n` | Load voltage | Load node | — | per envelope | Open | — | Open | OI-GND-001 | FX-DAQ | Proposed | C-002 | — |

Anti double-count (WP-012 R1–R5): returned/reactive/storage energy is not double-counted across `I_CH_IN_n`/`I_DOM_IN_x` and `I_STORAGE_NET`.

**Every measurement boundary above additionally inherits the §1.2 dependencies** (maximum available fault-energy — Open; reference-path; input-impedance; protection/current-limiting; instrument ground/reference; failure behavior; `OI-GND-001` blocker where it crosses/references envelopes). Each measurement conductor and instrument input is therefore treated as a **potential energy/reference/fault path** until qualified; none is classified unconditionally as non-energy.

## 3. DAQ responsibility split (§22)

| Data source | Role | May be treated as independent verification evidence? |
|-------------|------|------------------------------------------------------|
| DUT internal diagnostics | Control/diagnostic feedback | **No** (not independent) |
| Fixture measurement | Fixture-side observation | Only with defined boundary/calibration (future) |
| Independent reference instrument | Reference measurement | Candidate for independence (future, calibrated) |
| Operator UI | Presentation | **No** (never sole authority) |
| Automated test controller | Sequencing/control | **No** (control data) |
| Event logger | Record | **No** (record only) |

Data-class distinction: `control data` · `diagnostic data` · `reference measurement` · `safety observation` · `verification evidence candidate`. **No single diagnostic source is automatically independent verification evidence.** WP-015 creates **no** VE records.

## 4. Dependencies

| Dependency | Status |
|------------|--------|
| Sense topology / accuracy | OI-SENSE-001 Open; ED-IN-011/032 |
| Reference / isolation for measurement | OI-GND-001 Open ⇒ reference method Open; no isolation topology selected |
| Calibration requirements | Proposed; numeric Open |
| Instrument / DAQ class | Abstract only (no hardware selected) |

## 5. Traceability

REQ-DCC-V-FX-060/061/062 · WP-014 FIMR (FX-MP-*) · WP-010 MP-* · OI-SENSE-001 · OI-GND-001 · ED-IN-011/032.

## 6. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 measurement and DAQ architecture (boundaries + DAQ responsibility split) — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — measurement is observation-purpose; connection treated as potential energy/reference/fault path; concept separation + per-boundary Open dependencies; no unconditional non-energy classification |
