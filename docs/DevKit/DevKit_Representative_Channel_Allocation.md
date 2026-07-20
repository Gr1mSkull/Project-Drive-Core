# DevKit Representative Channel Allocation — WP-010

**Document ID:** DOC-DK-RCA-001  
**Version:** 1.1  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010 / WP-010-R1  
**Date:** 2026-07-20

Functional aliases — **not** final connector labels. No MPNs. No ampere ratings Approved.

Per ADR-019 minimum capability set and ADR-020 external HC separation.

## 1. Capability alias rule

```text
CH-HS-BASE
CH-HS-PWM
CH-HS-SENSE
CH-HS-PROTECTED
```

are **capability and verification-role aliases**. They do **not** imply four physical channels.

One physical representative channel may satisfy several or all of these aliases when:

1. every claimed capability is physically present;
2. every verification case remains independently executable;
3. fault injection does not invalidate another capability claim;
4. measurement access supports each case;
5. the test baseline records the actual physical-channel mapping;
6. the future sizing and schematic WPs confirm electrical compatibility.

**Physical channel count is not frozen in WP-010.** Final population is deferred to sizing and schematic WPs.

## 2. Channel summary

| Channel ID | ADR-019 mapping | Mandatory | Physical sharing |
|------------|-----------------|-----------|------------------|
| **CH-HS-BASE** | Switched HS (REQ-DCC-V-DK-039) | Yes | **CONDITIONAL** — may share when independent verification remains possible |
| **CH-HS-PWM** | PWM-capable HS (REQ-DCC-V-DK-040) | Yes — unconditional ADR-019 minimum | **CONDITIONAL** — may share when independent verification remains possible |
| **CH-HS-SENSE** | Current-sensed (REQ-DCC-V-DK-043) | Yes | **CONDITIONAL** — may share when sense remains independently verifiable |
| **CH-HS-PROTECTED** | OC + SC + retry/latch (REQ-DCC-V-DK-044–049) | Yes | **CONDITIONAL** — protection tests may use dedicated or shared channel with injection access |
| **CH-BI-REP** | Bidirectional (REQ-DCC-V-DK-042) | Yes (or DK-C BI cases BLOCKED) | No — BI conflict prevention requires distinct path |
| **CH-HC-EXTERNAL** | Highest-current continuous (ADR-020) | External fixture | No — not on base Power PCB continuous rating |

**PWM policy:** PWM capability remains part of the ADR-019 unconditional minimum set. If PWM is not implemented, record:

```text
architecture requirement not satisfied;
associated verification remains BLOCKED.
```

Do not classify PWM as `N/A` merely because it shares a physical channel.

**Note:** `config/vehicles/devkit.yaml` maps logical functions to candidate channels — **candidate `current_limit_a` values are not Approved**.

## 3. Channel detail

### CH-HS-BASE

| Field | Value |
|-------|-------|
| **Represented capability** | ON/OFF high-side switch; medium-current class |
| **Classification** | Mandatory capability alias |
| **Control path** | Logic RT → J_LP command transport → Power HS driver |
| **Diagnostic path** | Current-observation path → diagnostic observation path |
| **Safe state** | OFF — switch open |
| **Load type** | Resistive bench load (P2/P3 profile) |
| **Energy class** | Base envelope — `I_CHANNEL_CONT` Open |
| **Operating profiles** | P2, P3 |
| **Fault injections** | OC (ADR-023 DK-C); comm loss (DK-A) |
| **Verification cases** | VER-DCC-DK-C-001, C-002 |
| **Measurement points** | MP-CH-HS-VOUT, MP-CH-HS-IOUT |
| **Unresolved** | Switch class; `I_CHANNEL_CONT`; connector; physical channel assignment |

### CH-HS-PWM

| Field | Value |
|-------|-------|
| **Represented capability** | PWM-modulated HS switching |
| **Classification** | Mandatory — ADR-019 unconditional minimum |
| **Control path** | Logic timer PWM → J_LP command transport → Power driver |
| **Diagnostic path** | Current-observation path (shared or dedicated per physical mapping) |
| **Safe state** | OFF (0% duty or enable withdrawn) |
| **Load type** | Inductive/resistive bench load with current ripple |
| **Energy class** | Base envelope |
| **Operating profiles** | P2, P3 |
| **Fault injections** | PWM during kill (timing); OC |
| **Verification cases** | VER-DCC-DK-C-003 — **BLOCKED** if PWM not implemented |
| **Measurement points** | MP-CH-HS-VOUT, MP-CH-HS-IOUT, scope on PWM |
| **Unresolved** | `f_PWM` (TBD-DK-008); duty limits; physical channel assignment |

### CH-HS-SENSE

| Field | Value |
|-------|-------|
| **Represented capability** | Current observation with diagnostic reporting |
| **Classification** | Mandatory capability alias |
| **Control path** | Shared command path with HS channel under test |
| **Diagnostic path** | Sense aggregation function → diagnostic observation path |
| **Safe state** | N/A — observability |
| **Load type** | Known bench load for calibration |
| **Energy class** | Base envelope |
| **Operating profiles** | P2, P3 |
| **Fault injections** | Sense disconnect (if accessible) |
| **Verification cases** | VER-DCC-DK-C-004 |
| **Measurement points** | MP-CH-HS-IOUT; external ammeter correlation |
| **Unresolved** | Accuracy (TBD-DK-009); shunt/mirror/integrated-diagnostic topology — Component/Schematic scope |

### CH-HS-PROTECTED

| Field | Value |
|-------|-------|
| **Represented capability** | OC detection; SC reaction; retry/latch behaviour |
| **Classification** | Mandatory capability alias |
| **Control path** | Logic RT → J_LP command transport → protected driver |
| **Diagnostic path** | Sense aggregation function; aggregate fault indication |
| **Safe state** | OFF; latched until retry policy |
| **Load type** | Programmable load + fault injection fixture |
| **Energy class** | P5 fault profile — energy limited |
| **Operating profiles** | P5 |
| **Fault injections** | OC, SC (ADR-023 DK-C); method TBD-DK-011 |
| **Verification cases** | VER-DCC-DK-C-005, C-006, C-008 |
| **Measurement points** | MP-CH-HS-IOUT, MP-JLP-FAULT |
| **Unresolved** | SC injection method; retry limits (TBD-DK-013) |

### CH-BI-REP

| Field | Value |
|-------|-------|
| **Represented capability** | Bidirectional energy transfer; direction conflict prevention |
| **Classification** | Mandatory (or BI verification BLOCKED) |
| **Control path** | Logic RT → J_LP command transport → BI switching function |
| **Diagnostic path** | Current-observation path both directions; fault reporting |
| **Safe state** | Both directions OFF |
| **Load type** | Reversible bench load; stall fixture when available |
| **Energy class** | Base for low-energy; external for stall (TBD-DK-022) |
| **Operating profiles** | P2, P3, P5 (stall) |
| **Fault injections** | Conflicting direction; stall |
| **Verification cases** | VER-DCC-DK-C-010, C-011 |
| **Measurement points** | MP-CH-BI-A, MP-CH-BI-B |
| **Unresolved** | Shoot-through prevention topology; stall fixture |

### CH-HC-EXTERNAL

| Field | Value |
|-------|-------|
| **Represented capability** | Highest-current continuous representation (ADR-020) |
| **Classification** | External fixture — not base PCB continuous |
| **Control path** | Logic + fixture controller — **Open** detail |
| **Diagnostic path** | Fixture instrumentation + representative feedback |
| **Safe state** | Fixture de-energized |
| **Load type** | EXT-LOAD-BANK (controlled external load absorbing energy) |
| **Energy class** | P6 — `I_loadbank_limit` Open |
| **Operating profiles** | P6 only |
| **Fault injections** | HC overload → Phase E only |
| **Verification cases** | Bounded discovery; Phase E for continuous HC |
| **Measurement points** | Fixture MP; MP-LOAD-EXT-RETURN |
| **Unresolved** | Fixture interface; ground/reference (OI-GND-001) |

## 4. Physical channel sharing rules

One physical channel may represent multiple **capability aliases** only if all six conditions in §1 are met.

Diagnostic topology selection (shunt, current mirror, integrated diagnostic output, ADC routing, mux) remains **Component/Schematic scope** — not frozen by WP-010.

## 5. Mapping to devkit.yaml (informative, non-normative)

| Functional alias | Candidate logical mapping | Notes |
|------------------|---------------------------|-------|
| CH-HS-PWM | fan1 (ch1), water_pump (ch2) | Candidate limits not Approved; may map to one physical channel |
| CH-HS-BASE | fuel_pump (ch3), ecu_power (ch4) | May share physical channel with PWM alias if §1 conditions met |
| CH-HS-SENSE | All HS channels with current observation | Per-channel sense required |
| CH-HS-PROTECTED | test_load_5/6 (ch5/6) | Fault injection access preferred |
| CH-BI-REP | motor_hb1 (ch101) | Single BI |
| CH-HC-EXTERNAL | No on-board mapping | Fixture only |

Final population deferred to sizing/schematic WP.

## 6. Open-load policy

Open-load diagnostics (REQ-DCC-V-DK-046): **conditional** — required only if selected switch implementation claims open-load detection (ADR-019). Architecture does **not** require open-load universally.

## 7. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial representative channel allocation — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — capability alias rule; conditional physical sharing; diagnostic topology language; PWM BLOCKED not N/A |
