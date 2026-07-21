# DevKit Fixture Preliminary Design Architecture — WP-015

**Document ID:** DOC-DK-FPDA-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review (2026-07-21)  
**Work Package:** WP-015  
**Baseline:** WP-014 Accepted (`bc7c6b6`)  
**Date:** 2026-07-20

```text
PRELIMINARY design architecture only — functional topology and options.
No detailed electrical design · no MPN · no ratings · no numeric approval ·
no schematic/PCB/harness · no procurement · no construction · no energization · no VE.
Acceptance of WP-015 means only: "Preliminary fixture design architecture accepted."
It does NOT mean detailed design complete, safe to build, safe to energize, or requirements verified.
```

## 1. Purpose and scope

This package converts the Accepted WP-014 fixture requirements (`REQ-DCC-V-FX-*`) into a coherent **preliminary design architecture** for the Gen1 DevKit fixture and load-bank system: functional module decomposition, energy-source boundaries, base/external energy paths, operator safety controls, authorization and interlock logic, operating states, load-bank functional architecture, measurement/DAQ boundaries, fault-injection boundaries, DUT interface allocation, preliminary wiring classes, diagnostic/observation points, implementation dependencies, and readiness gates for detailed design.

It does **not** freeze physical implementation, select concrete parts, approve numeric values, create construction authority, or claim verification.

## 2. Authority hierarchy

1. Engineering Constitution · 2. Accepted EDL · 3. Accepted ADR-016…023 · 4. Accepted governance/standards · 5. Accepted WP-007…WP-014 artifacts · 6. **Proposed WP-015 preliminary design (this package)** · 7. Historical/candidate documentation (`HISTORICAL_ONLY`).

Lower-authority conflict with an Accepted source is recorded as `ARCHITECTURAL_CONFLICT` and not resolved silently. WP-015 shall not cite itself as prior Accepted authority.

## 3. Design status model

Every preliminary design element uses one status:

```text
ACCEPTED_INPUT              — an Accepted upstream requirement/constraint consumed here
PROPOSED_DESIGN            — new WP-015 design proposal (not self-approved)
PROPOSED_CONSTRAINT        — new WP-015 constraint (not self-approved)
ALTERNATIVE_UNDER_EVALUATION
BLOCKED_BY_ARCHITECTURE
BLOCKED_BY_THRESHOLD
BLOCKED_BY_COMPONENT_CLASS
BLOCKED_BY_DETAILED_DESIGN
BLOCKED_BY_MEASUREMENT
HISTORICAL_ONLY
REJECTED
```

State separation (not equivalent): Requirement Accepted → Constraint Accepted → Preliminary design proposed → **Preliminary design accepted (WP-015 Architecture Review 2026-07-21)** → Detailed design completed → Implementation authorized → Implementation completed → Physical verification completed. WP-015 preliminary design is now **Accepted at Architecture Review**; per-entry FX-PD dispositions are recorded in the decision register §0. Acceptance does not mean detailed design complete, safe to build, safe to energize, or requirements verified. The Implementation Engineer did not self-approve; acceptance is the Architect's disposition.

## 4. Document set

| Document | Scope |
|----------|-------|
| This document | Anchor: lifecycle, functional module decomposition, status model, readiness overview |
| [DevKit_Fixture_Preliminary_Block_Design.md](DevKit_Fixture_Preliminary_Block_Design.md) | Functional block diagrams (§12) |
| [DevKit_Fixture_Energy_Control_Preliminary_Design.md](DevKit_Fixture_Energy_Control_Preliminary_Design.md) | Energy/control paths, OI-GND-001 options, auth-vs-physical state, fault-injection, fault-energy governance |
| [DevKit_Fixture_Interlock_and_State_Model.md](DevKit_Fixture_Interlock_and_State_Model.md) | Fixture states, interlocks, E-stop integrity |
| [DevKit_Load_Bank_Preliminary_Design.md](DevKit_Load_Bank_Preliminary_Design.md) | Load-bank functional classes and failure behavior |
| [DevKit_Fixture_Measurement_and_DAQ_Architecture.md](DevKit_Fixture_Measurement_and_DAQ_Architecture.md) | Measurement boundaries and DAQ responsibility split |
| [DevKit_Fixture_Interface_and_Wiring_Architecture.md](DevKit_Fixture_Interface_and_Wiring_Architecture.md) | Interface groups, wiring classes, operator control/indication |
| [DevKit_Fixture_Preliminary_Design_Decision_Register.md](DevKit_Fixture_Preliminary_Design_Decision_Register.md) | `FX-PD-*` proposed decisions and options |
| [DevKit_Fixture_Implementation_Readiness_Matrix.md](DevKit_Fixture_Implementation_Readiness_Matrix.md) | Element readiness for detailed design / procurement / construction / energization |

## 5. Preliminary design lifecycle

| Stage | Required inputs | Permitted outputs | Responsible role | Approval authority | Downstream consumer | Prohibited claims |
|-------|-----------------|-------------------|------------------|--------------------|--------------------|-------------------|
| Accepted fixture requirement | WP-014 REQ-DCC-V-FX-* | Requirement trace | System Architect (done) | Architect | Functional allocation | — |
| Functional allocation | Requirements | Module map | Impl. Engineer | Architect | Preliminary module architecture | Not a design |
| Preliminary module architecture | Allocation | `FX-*` modules | Impl. Engineer | Architect | Boundaries | Not detailed design |
| Energy/control/measurement boundary | Modules | Path/boundary defs | Impl. Engineer | Architect | State/interlock model | Not energization-ready |
| Preliminary state & interlock model | Boundaries | States/interlocks | Impl. Engineer | Architect | Option comparison | Not a safety-integrity claim |
| Architecture option comparison | Open issues | Options (`FX-PD-*`) | Impl. Engineer | Architect | Architect acceptance | No self-approval |
| **Architect acceptance (WP-015 end)** | Package | Accepted prelim architecture | System Architect | Architect | Detailed design inputs | Not "safe to build" |
| Detailed design inputs | Accepted prelim | Design inputs | (future WP) | Architect | Component qualification | — |
| Component qualification | Class methodology | Qualified classes | Component Eng. | Architect | Detailed schematic/mechanical | — |
| Detailed schematic/mechanical design | Qualified inputs | Schematic/PCB/mech | (future WP) | Architect | Safety review | — |
| Safety review | Detailed design | Review record | Safety role | Architect | Procurement authorization | — |
| Procurement authorization | Safety-reviewed design | Purchase authority | System Architect | Architect | Construction | — |
| Construction | Procured parts | Built fixture | Build role | Architect | Commissioning | — |
| Commissioning | Built fixture | Commissioned fixture | Test Eng. | Architect | Controlled energization | — |
| Controlled energization | Commissioned fixture | Energized fixture | Test Eng. | Architect | Physical verification | — |
| Physical verification | Energized fixture | Results | Test Eng. | Architect | VE | Only then PASS/Verified |
| VE | Verified results | VE records | Test Eng. | Architect | Gate evidence | — |

**WP-015 ends at:** Architect acceptance of the preliminary design architecture.

## 6. Functional module decomposition (§11)

Modules are functional; a module does **not** imply a separate enclosure or PCB.

| Module ID | Purpose | Inputs (symbolic) | Outputs (symbolic) | Energy authority | Control authority | Observation role | Safe default | Safe minimum on failure | Upstream dep | Downstream dep | Open issue | Design status |
|-----------|---------|-------------------|--------------------|--------------------|-------------------|------------------|--------------|-------------------------|--------------|----------------|------------|---------------|
| `FX-SOURCE-CONTROL` | Command/control of source enablement (issues enable commands) | AUTH grants, operator req | Source-enable **command** (`[C]`) | **None — command/control only; originates no energy; not proof of energy removal; does not replace energy-path observation** | Command only under AUTH | Source-state observe | Command inactive | Inhibit source-enable command | FX-AUTHORIZATION | BASE-ENERGY-CONTROL / EXT-ENERGY-CONTROL (energy-control elements) | — | PROPOSED_DESIGN |
| `FX-BASE-ENERGY-PATH` | Base envelope energy delivery to DUT (via BASE-ENERGY-CONTROL) | Base source energy (from BASE-SOURCE→BASE-ENERGY-CONTROL) | DUT base energy | Base | None (path) | Entry/base MPs | De-energized | Inhibit/remove base energy | BASE-ENERGY-CONTROL | FX-DUT-INTERFACE | — | PROPOSED_DESIGN |
| `FX-EXTERNAL-ENERGY-BOUNDARY` | External envelope boundary + back-feed prevention (via EXT-ENERGY-CONTROL) | Ext source energy (from EXT-SOURCE→EXT-ENERGY-CONTROL) | Ext energy (bounded) | External | None (function) | Ext MPs; back-feed observe | De-energized; functionally separated; no uncontrolled interconnection; ground/isolation topology Open | Inhibit ext energy; prevent back-feed | EXT-ENERGY-CONTROL | FX-LOAD-BANK / DUT-under-EXT | OI-GND-001 | BLOCKED_BY_ARCHITECTURE |
| `FX-ENERGY-REMOVAL` | Remove/inhibit hazardous energy | Removal request, E-stop | Removal action | Overrides all AUTH | Removal command | Residual observe | Removal-capable | Force removal/inhibit | FX-ESTOP, FX-INTERLOCK-CONTROLLER | FX-DISCHARGE | Timing Open | PROPOSED_DESIGN |
| `FX-ESTOP` | Emergency energy inhibit independent of DUT firmware | Operator E-stop | Inhibit-all | Inhibits all fixture hazardous AUTH | Highest override | E-stop state | Asserted-safe on loss | Inhibit hazardous energy | Operator | FX-ENERGY-REMOVAL, FX-AUTHORIZATION | REQ-DCC-V-FX-071 | BLOCKED_BY_ARCHITECTURE (topology) |
| `FX-AUTHORIZATION` | Grant/revoke `AUTH_*` | Identity/config/state, E-stop | AUTH grants | Sole grantor | Arbitration | AUTH-state observe | All AUTH inactive | Revoke all AUTH | FX-INTERLOCK-CONTROLLER | Source/sink/fault/DUT modules | — | PROPOSED_DESIGN |
| `FX-INTERLOCK-CONTROLLER` | Evaluate interlocks and state | All safety inputs | Interlock verdicts | None (logic) | Gates AUTH | Interlock observe | Fail-safe inhibit | Inhibit on any unmet interlock | Observations | FX-AUTHORIZATION | — | PROPOSED_DESIGN |
| `FX-DUT-INTERFACE` | Allocate DUT power/logic/KILL/enable/comm | Fixture energy/signals | DUT connections | Base (gated) | Under AUTH | KILL/nENABLE observe | Disconnected/inactive | Inhibit DUT energy | FX-BASE-ENERGY-PATH | DUT | — | PROPOSED_DESIGN |
| `FX-LOAD-BANK` | Controlled energy sink-function (no independent origination); returned-energy reverse-flow separately contained | DUT output, AUTH | Load control | Sink-function; independent energy origination prohibited; returned-energy reverse-flow BLOCKED_BY_ARCHITECTURE | Under `AUTH_LOAD_BANK` | Sink/load observe | Inactive | Revoke + upstream removal | FX-AUTHORIZATION | FX-ENERGY-REMOVAL | OI-BI-001, OI-GND-001 | PROPOSED_DESIGN / BLOCKED (returned energy) |
| `FX-FAULT-INJECTION` | Bounded authorized fault application | AUTH, preconditions | Fault stimulus | Conditional | Under `AUTH_FAULT_INJECTION` | Fault-state observe | Inhibited | Inhibit + lockout | FX-AUTHORIZATION | FX-ENERGY-REMOVAL | OI-SC-001, OI-FIX-002 | BLOCKED_BY_DETAILED_DESIGN |
| `FX-MEASUREMENT` | Observation-purpose (a physical connection is a potential energy/reference/fault path until qualified) | Signals | Measured quantities | None **as designed**; physical connection treated as potential energy/reference/fault path (impedance/protection/reference/isolation/fault behavior Open) | None | Primary observer | High-Z/safe (impedance/protection Open) | Block dependent tests | Energy paths | FX-DAQ | OI-SENSE-001, OI-GND-001 | PROPOSED_DESIGN / PARTIAL |
| `FX-DAQ` | Acquire/log measured/derived data | Measurements | Data records | None | None | Logger | Passive | Continue logging or flag loss | FX-MEASUREMENT | FX-OPERATOR-CONTROL, evidence | Accuracy/BW Open | PROPOSED_DESIGN |
| `FX-OPERATOR-CONTROL` | Operator commands/requests | Operator input | Requests | None (request-only) | Request-only | — | No hazardous request honored by default | Requests ignored if unsafe | Operator | FX-AUTHORIZATION | — | PROPOSED_DESIGN |
| `FX-STATUS-INDICATION` | Indicate fixture state | Observations | Indications | None | None | Indicator | Safe/off indication | Indicate unknown/unsafe | Observations | Operator | — | PROPOSED_DESIGN |
| `FX-DISCHARGE` | Controlled discharge of stored energy | Removal state | Discharge action | Discharge (removal) | Under removal | Residual observe | Discharge-capable | Confirm safe decay or hold lockout | FX-ENERGY-REMOVAL | FX-INTERLOCK-CONTROLLER | Timing Open | PROPOSED_DESIGN |
| `FX-CONTAINMENT` | Physical/energy containment boundary | Hazard energy | Containment | Passive barrier | None | — | Contained | Maintain containment | Energy paths | Operator safety | ADR-DK-011/012 | BLOCKED_BY_DETAILED_DESIGN |
| `FX-SERVICE-INTERFACE` | Service/UI/logging link | Service comms | Service data | None (never hazardous) | Request-only | — | No AUTH | No energy authority | — | FX-DAQ | — | PROPOSED_DESIGN |

Detail per module in the block/energy/state/interface documents.

**WP-015-R1 notes:**
- `FX-SOURCE-CONTROL` is a command/control function only; it originates no energy, is not proof of energy removal, and does not replace energy-path observation. Energy control is performed by `BASE-ENERGY-CONTROL` / `EXT-ENERGY-CONTROL` in the energy path (see energy-control document §1).
- `FX-MEASUREMENT` is observation-purpose; a physical measurement connection is treated as a potential energy/reference/fault path until qualified (no unconditional non-energy classification).
- `FX-LOAD-BANK` uses a **sink-function** architecture; independent energy origination is prohibited. Regenerative/bidirectional **returned energy** is an energy-bearing reverse-flow condition requiring explicit containment; it does not reclassify the load bank as `EXT-SOURCE`, and remains `BLOCKED_BY_ARCHITECTURE` until OI-BI-001 and OI-GND-001 are dispositioned.

## 7. Readiness overview

| Aspect | Readiness |
|--------|-----------|
| Functional module decomposition | PRELIMINARY_DEFINED |
| Energy/control/authorization/observation/safety path separation | PRELIMINARY_DEFINED |
| Ground/reference-dependent interconnection | BLOCKED_BY_ARCHITECTURE (OI-GND-001) |
| Protection realization | BLOCKED_BY_ARCHITECTURE / COMPONENT (OI-PROT-001/002) |
| Fault-injection realization (SC/stall) | BLOCKED_BY_DETAILED_DESIGN (OI-SC-001 / OI-FIX-002) |
| Bidirectional / returned-energy topology | BLOCKED_BY_ARCHITECTURE (OI-BI-001) |
| Numeric envelopes / ratings | BLOCKED_BY_THRESHOLD (Open) |
| Detailed design / schematic / PCB / harness | NOT_STARTED / NOT_AUTHORIZED |
| Procurement / construction / energization | NOT_AUTHORIZED |

Detail: [DevKit_Fixture_Implementation_Readiness_Matrix.md](DevKit_Fixture_Implementation_Readiness_Matrix.md).

## 8. Preserved statuses

`REQ-DCC-V-FX-*` ACCEPTED / NOT VERIFIED; fixture NOT IMPLEMENTED; `PWR-A-017/018/021…024` ACCEPTED_CONSTRAINT; OI-GND-001, OI-PROT-001/002, OI-FIX-001/002, OI-SC-001, OI-BI-001 OPEN; TBD-DK-007 OPEN / BLOCKED_BY_EDL_CLARIFICATION / NOT VERIFIED; numeric thresholds OPEN; verification cases NOT EXECUTED / BLOCKED; VE NONE; procurement/construction/energization NOT AUTHORIZED.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial preliminary design architecture anchor — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — source-control vs energy path separated; measurement as potential energy/fault path; load-bank sink-function + returned-energy containment; isolated-by-function removed |
| 1.2 | 2026-07-21 | Architecture Review **Accepted** (WP-015 / R1 / R2 / R3; reviewed head `227ea78`, PR #19); Open decisions retained; NOT VERIFIED |
