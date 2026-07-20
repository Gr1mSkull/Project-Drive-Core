# DevKit Fixture Functional Architecture — WP-014

**Document ID:** DOC-DK-FFA-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review (2026-07-20)  
**Work Package:** WP-014  
**Date:** 2026-07-20

```text
Fixture FUNCTIONAL architecture only — no components, MPN, ratings, schematics, or construction Approved.
```

## 1. Purpose

Define the laboratory fixture as functional domains and authority flows supporting safe, reproducible DevKit verification. Implements Accepted ADR-020/021/023, WP-010 safe-state paths, and WP-012/013 energy accounting without selecting hardware.

## 2. Functional domains

| Domain | Role | Hazardous energy? |
|--------|------|-------------------|
| **Operator-control** | Operator commands, indications, deliberate authorization | No (commands only) |
| **Source-energy** | BASE-SOURCE control and observation | Yes (base) |
| **Fixture input-protection** | Fixture-side entry protection layers (P0/P1 complement) | Coordinating |
| **DevKit base-energy** | Energy into DUT base envelope | Yes (base) |
| **External energy** | EXT-SOURCE domain | Yes (external) |
| **Load-bank** | EXT-LOAD-BANK energy absorption | Sink (not a source) |
| **External power-module** | EXT-POWER-MODULE representative switching/protection | Yes (external) |
| **Fault-injection** | Bounded, authorized fault application | Conditional |
| **Measurement** | Envelope-aware observation | No (shall not become uncontrolled energy path) |
| **Communication/service** | Tablet/Radio/service links | **Never** hazardous-energy owner |
| **Emergency energy-removal** | Fixture E-stop and independent removal | Safety authority |
| **Evidence-acquisition** | Logging / VE consumers (future) | No |

## 3. Intended functional flow

```text
Operator authority
→ fixture state validation
→ source authorization
→ controlled energization
→ DevKit operation
→ load application
→ measurement
→ controlled de-energization
```

## 4. Fault flow

```text
Explicit fault authority
→ fixture precondition validation
→ bounded fault injection
→ protection reaction
→ energy removal or containment
→ safe-state confirmation
→ fault reset authorization
```

## 5. Required fixture states

| State | Permitted energy | Prohibited | Operator | Automated | Interlocks | Allowed from | Prohibited from | Indication | Measurement | Control-loss response | Recovery |
|-------|------------------|------------|----------|-----------|------------|--------------|-----------------|------------|-------------|---------------|----------|
| **SAFE_OFF** | FIXTURE-AUX only (if present) | BASE, EXT, fault, DUT enable | Inspect / configure | Hold inhibit | All AUTH_* inactive | Any (via ENERGY_REMOVAL) | Direct to TEST_ACTIVE | Safe/Off | Available | Remain SAFE_OFF | Explicit READY path |
| **INSPECTION** | FIXTURE-AUX | Hazardous | Visual/service | Inhibit | Same | SAFE_OFF | TEST_ACTIVE | Inspection | Available | SAFE_OFF | SAFE_OFF |
| **READY** | FIXTURE-AUX | Hazardous until AUTH | Arm request | Validate identity/config | Identity/config valid | SAFE_OFF/INSPECTION | FAULT_ACTIVE | Ready | Available | SAFE_OFF | SAFE_OFF |
| **BASE_ENERGIZED** | BASE-SOURCE + DUT base | EXT-SOURCE / EXT-POWER-MODULE physical energization; combined BASE/EXT paths | Monitor | Maintain AUTH_BASE | E-stop clear; AUTH_BASE | READY | FAULT without removal; transition to externally energized condition while OI-GND-001 Open | Base On | Entry/base MPs | ENERGY_REMOVAL | Controlled de-energize → READY/SAFE_OFF |
| **EXTERNAL_ENERGY_ARMED** | Authorization/precondition only — does **not** energize EXT-SOURCE, EXT-POWER-MODULE, or any combined BASE/EXT path | Physical EXT energization (while OI-GND-001 Open); combined BASE/EXT energization; silent common-reference/isolation implication | Record inactive external authorization request | Validate EXT path preconditions | AUTH_EXT_* may be requested but physical EXT energization blocked while OI-GND-001 Open; back-feed inhibit | READY or BASE_ENERGIZED (authorization record only) | Silent merge; interpreting ARMED as energized | Ext Auth Armed (not energized) | Ext MPs as available | ENERGY_REMOVAL; revoke AUTH | Disarm → READY |
| **TEST_ACTIVE** | Declared domains for profile — while OI-GND-001 Open: base-only **or** external-only after base safely removed; never simultaneous BASE+EXT | Unauthorized domains; combined BASE/EXT profile (BLOCKED_BY_ARCHITECTURE while OI-GND-001 Open) | Supervise | Execute profile | All required AUTH; measurements available | BASE_ENERGIZED (base-only profiles) / EXTERNAL_ENERGY_ARMED only after OI-GND-001 Accepted **or** after base safely removed for external-only profiles | Unvalidated READY; simultaneous BASE/EXT | Test Active | Profile MPs | ENERGY_REMOVAL; stale cmds | Controlled exit |
| **FAULT_INJECTION_ARMED** | As TEST + fault arm | Fault apply until AUTH_FAULT | Arm fault | Preconditions | AUTH_FAULT; E-stop clear | TEST_ACTIVE | SAFE_OFF direct apply | Fault Armed | Fault MPs | ENERGY_REMOVAL; disarm | Disarm |
| **FAULT_ACTIVE** | Bounded fault energy | Unbounded / multi-source conflict | Abort authority | Bound timer/limit | Backup protection | FAULT_INJECTION_ARMED | Auto from READY | Fault Active | Fault MPs | ENERGY_REMOVAL | ENERGY_REMOVAL → POST_FAULT_LOCKOUT |
| **ENERGY_REMOVAL** | Removal in progress | New AUTH grant | Confirm | Remove/inhibit | Override all AUTH | Any hazardous | Resume TEST | Removing | Monitor residual | Complete removal | POST_FAULT_LOCKOUT or SAFE_OFF |
| **POST_FAULT_LOCKOUT** | Inhibited | Re-arm without deliberate reset | Reset request | Hold lockout | Prior AUTH revoked; cmds stale | ENERGY_REMOVAL | Auto TEST | Lockout | Available | Remain lockout | RECOVERY_VALIDATION |
| **RECOVERY_VALIDATION** | Inhibited until pass | Hazardous | Validate | Checks | Identity/config; residual energy confirmed | POST_FAULT_LOCKOUT | Skip to TEST | Recovery | Required MPs | SAFE_OFF | READY or SAFE_OFF |

**Uncommanded startup / power restoration:** enter **SAFE_OFF**. Shall **not** automatically resume previous test or fault condition.

### 5.1 EXTERNAL_ENERGY_ARMED semantics (WP-014-R1)

```text
EXTERNAL_ENERGY_ARMED is an authorization/precondition state only.
It does not by itself energize EXT-SOURCE, EXT-POWER-MODULE,
or any combined BASE/EXT path.
```

While **OI-GND-001** remains Open:

```text
- simultaneous BASE-SOURCE and EXT-SOURCE energization is prohibited;
- a combined BASE/EXT test profile is BLOCKED_BY_ARCHITECTURE;
- transition from BASE_ENERGIZED to an externally energized condition is prohibited;
- EXTERNAL_ENERGY_ARMED reachable from BASE_ENERGIZED records an inactive external
  authorization request only — actual external energization remains blocked;
- combined-interface evidence may be defined, but cannot be executed;
- no authority state may silently imply a common reference or galvanic isolation.
```

Ground/reference options are **not** selected by this document.

## 6. Stale-command rule

Prior fixture commands are **stale** after: E-stop · physical KILL · fixture power interruption · source interruption · controller reset · invalid fixture identity · invalid fixture configuration · loss of fixture-control authority.

Recovery requires a **new command epoch** after deliberate authorization.

## 7. Authority inventory (see requirements doc)

`AUTH_BASE_SOURCE` · `AUTH_EXT_SOURCE` · `AUTH_LOAD_BANK` · `AUTH_EXT_POWER_MODULE` · `AUTH_FAULT_INJECTION` · `AUTH_DUT_ENABLE`

Defaults: **inactive**. Radio/Tablet: **request only** — never direct hazardous-energy owners.

## 8. Traceability

ADR-020/021/023 · PWR-A-001…005 · OI-FIX-001/002 · OI-GND-001 · WP-010 SSM · REQ-DCC-V-FX-* (Proposed).

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-014 initial fixture functional architecture — Proposed |
| 1.1 | 2026-07-20 | WP-014-R1 — EXTERNAL_ENERGY_ARMED authorization-only; OI-GND-001 combined BASE/EXT block |
| 1.2 | 2026-07-20 | Architecture Review **Accepted** (WP-014; reviewed head `084f579`, PR #18); Open decisions retained; NOT VERIFIED |
