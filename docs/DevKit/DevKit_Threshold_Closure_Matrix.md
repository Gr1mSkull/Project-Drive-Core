# DevKit Threshold Closure Matrix — WP-009

**Document ID:** DOC-DK-TBD-MAT-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Review date:** 2026-07-20  
**Approver role:** System Architect  
**Work Package:** WP-009 / WP-009-R1 (Accepted)  
**Date:** 2026-07-20

> Authoritative closure disposition for analyzed thresholds. **Register Status remains Open** for numeric values; analysis methods Accepted by Architecture Review (2026-07-20).

## 1. Disposition legend

| Disposition | Meaning |
|-------------|---------|
| READY_FOR_ACCEPTANCE | Evidence/model sufficient for Architect to accept value or procedure |
| BOUND_ESTABLISHED_VALUE_OPEN | Calculation model and bounds defined; numeric Open |
| BLOCKED_BY_EDL_CLARIFICATION | EDL-011 semantic ambiguity blocks numeric direction for TBD-DK-007 |
| BLOCKED_BY_ELECTRICAL_ARCHITECTURE | Needs electrical design inputs |
| BLOCKED_BY_COMPONENT_SELECTION | Needs qualified components |
| BLOCKED_BY_MEASUREMENT | Needs physical bench evidence |
| BLOCKED_BY_HAZARD_DECISION | Needs hazard/risk decision beyond WP-009 |

## 2. Primary thresholds — Architecture Review decisions (2026-07-20)

| TBD | Register Status | Methods Accepted | Numeric Open | Blocker |
|-----|-----------------|------------------|--------------|---------|
| TBD-DK-002 | Open | Limit stack; continuous/protection/transient/fault distinction; C2 calculation architecture | Certified continuous; protection rating; transient/fault envelope | Electrical architecture + measurement |
| TBD-DK-003 | Open | Profile/overlap model; instantaneous/avg/RMS/transient-overlap; unknown overlap → concurrent | All numeric simultaneous limits | Overlap profiles + P4 measurement |
| TBD-DK-004 | Open | Hardware-kill budget; normalized start/end; measurement method | Numeric response limit | Measurement |
| TBD-DK-005 | Open | Watchdog budget; measurement method | WD expiry; handler; total numeric limit | Component + measurement |
| TBD-DK-007 | Open | Control-loss budget; message-period/missed-frame method; measurement method | All numeric ms values | **BLOCKED_BY_EDL_CLARIFICATION** |
| TBD-DK-014 | Open | Commanded-OFF budget; start/end definition; measurement method | Numeric response limit | FW + component + measurement |
| TBD-DK-021 | Open | Procedural state-machine contract (see §3) | Implementation + verification evidence | FW implementation |

### Exact acceptance records

#### TBD-DK-002

```text
Accepted:
- limit-stack model;
- distinction between continuous, protection, transient and fault currents;
- Scenario C2 calculation architecture.

Retained Open:
- certified continuous current;
- protection rating;
- transient/fault envelope.

No ampere ceiling is approved.
```

#### TBD-DK-003

```text
Accepted:
- profile-based simultaneous-current closure model;
- explicit channel-overlap profiles;
- separate instantaneous, continuous/average, RMS/thermal,
  and transient-overlap quantities;
- unknown overlap treated conservatively as concurrent.

Retained Open:
- every numeric simultaneous-current limit.
```

#### TBD-DK-004

```text
Accepted:
- hardware-kill budget structure;
- normalized start/end events;
- measurement method.

Retained Open:
- numeric response limit.
```

#### TBD-DK-005

```text
Accepted:
- watchdog budget structure;
- measurement method.

Retained Open:
- watchdog expiry;
- handler contribution;
- total numeric response limit.
```

#### TBD-DK-007

```text
Accepted:
- control-loss budget;
- message-period / missed-frame analysis method;
- measurement method.

Status:
- Open;
- BLOCKED_BY_EDL_CLARIFICATION.

No >100 ms or ≤100 ms bound is approved.
```

#### TBD-DK-014

```text
Accepted:
- commanded-OFF budget;
- start/end definition;
- measurement method.

Retained Open:
- numeric response limit.
```

#### TBD-DK-021

```text
Accepted:
- deterministic post-kill state-machine contract;
- kill-release lockout;
- operator acknowledgement requirement;
- applicable fault-clear requirement;
- command epoch / generation invalidation;
- explicit new per-function enable commands;
- prohibition of Service/Tablet as sole authority.

Status:
- procedural contract Accepted;
- implementation and evidence remain absent.
```

## 3. TBD-DK-021 register note

`Status: Open` retained in authoritative register. Additional note:

```text
Procedure accepted by WP-009 Architecture Review;
implementation and verification closure remain Open.
```

## 4. EDL-011 clarification follow-up

```text
EDL-011 clarification required.
```

Proposed clarification question (no answer selected):

```text
Does EDL-011 intend:

A. a nominal communication-loss detection timeout of 100 ms;
B. a maximum elapsed communication-loss interval before outputs are OFF;
C. a minimum filtering interval before declaring communication loss;
D. another explicitly defined timing contract?
```

Do not modify `docs/EDL/` until clarification CR completes.

## 5. Related thresholds (inspected)

| TBD | Proposed disposition | Candidate value/range | Bound | Evidence available | Missing evidence | Architecture dependency | Component dependency | Fixture dependency | Measurement dependency | Gate blocked | Next artifact |
|-----|---------------------|----------------------|-------|-------------------|------------------|------------------------|---------------------|-------------------|------------------------|--------------|---------------|
| TBD-DK-001 | BLOCKED_BY_ELECTRICAL_ARCHITECTURE | 13.8 V nominal **CANDIDATE** | Automotive bench range | docs/008 candidate | UV coordination with 012 | ADR-021 entry | PSU class | N/A | DMM at entry | DK-A A-003 | Architect range decision |
| TBD-DK-012 | BLOCKED_BY_HAZARD_DECISION | 10.5 V **CANDIDATE** (docs/008) | Reaction table required | REQ UV behaviour | Full reaction table | ADR-019/021 | Sense path | UV stim | UV step test | DK-C UV cases | Hazard + table WP |
| TBD-DK-017 | BLOCKED_BY_ELECTRICAL_ARCHITECTURE | ±5 % **CANDIDATE** | Per-rail table | REQ rails measurable | Regulator spec | Logic/Power arch | LDO/DC-DC | N/A | Rail capture | DK-A | Electrical architecture |
| TBD-DK-018 | BLOCKED_BY_MEASUREMENT | Not defined | Thermal case duration | REQ thermal cases | Channel class + load | ADR-019 thermal | NTC/switch | Thermal load | Duration log | DK-C C-009 | Thermal analysis |
| TBD-DK-019 | BLOCKED_BY_HAZARD_DECISION | Surface max **CANDIDATE** | Operator safety | REQ thermal | Touch hazard policy | ADR-DK-011 seq | Thermal paths | Enclosure | IR/TC | DK-C | Hazard decision |
| TBD-DK-022 | BLOCKED_BY_COMPONENT_SELECTION | Stall A/ms **CANDIDATE** | P5 fault class | REQ-042/054/055 | H-bridge + fixture | ADR-019 bidirectional | H-bridge MPN | Stall fixture | Stall capture | DK-C C-010–013 | Component + fixture WP |

## 6. Closure stage separation

For each primary TBD:

| Stage | TBD-DK-002 | TBD-DK-003 | TBD-DK-004 | TBD-DK-005 | TBD-DK-007 | TBD-DK-014 | TBD-DK-021 |
|-------|------------|------------|------------|------------|------------|------------|------------|
| Architecture direction established | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Calculation model established | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (procedure) |
| Candidate value proposed | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Procedure only |
| Numeric value acceptable now | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Procedure only |
| Numeric value requires hardware | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | FW impl |
| Procedure acceptable now | ✅ (002–007, 014 methods; 003 profile; 021 procedure) | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Evidence remains NOT VERIFIED | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

## 7. Authorized next work boundary

Architecture Review authorizes the next Work Package:

```text
Functional DevKit electrical architecture
```

**Authorized scope:**

- functional block decomposition;
- Logic / Power / Radio boundaries;
- base DevKit versus external load-bank separation;
- power-entry functional chain;
- protection-layer responsibilities;
- safe-state signal topology;
- measurement points;
- test points;
- interface and isolation requirements;
- representative channel-class allocation;
- symbolic current and timing parameters.

**Not authorized:**

- final conductor sizing;
- final connector sizing;
- final fuse rating;
- final PCB copper sizing;
- final switch current rating;
- thermal freeze;
- watchdog-period freeze;
- timing component freeze;
- PCB layout;
- firmware implementation;
- fixture construction.

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-009 initial closure matrix |
| 1.1 | 2026-07-20 | WP-009-R1 — EDL clarification block; removed ampere/timing bands; profile model for TBD-DK-003 |
| 1.2 | 2026-07-20 | Architecture Review — methods Accepted; numeric values Open; authorized functional electrical architecture WP |
