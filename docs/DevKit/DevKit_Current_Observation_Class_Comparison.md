# DevKit Current-Observation Class Comparison — WP-013

**Document ID:** DOC-DK-COCC-001  
**Version:** 1.0  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-013  
**Date:** 2026-07-20

```text
Class comparison only — no accuracy target, MPN, or ADC Approved.
```

## 1. Purpose

Compare current-observation evaluation classes against CH-HS-SENSE, measurement-boundary taxonomy (WP-012), and DK-C observation needs. Owners: **OI-SENSE-001**, **ED-IN-032**, **ED-IN-011**.

## 2. Classes under evaluation

| Class ID | Definition |
|----------|------------|
| **SENSE-INTEGRATED** | Integrated proportional / current-diagnostic output from switch or controller |
| **SENSE-SHUNT-HS** | External high-side shunt measurement |
| **SENSE-SHUNT-LS** | External low-side shunt measurement |
| **SENSE-MAGNETIC** | Isolated or magnetic current observation |
| **SENSE-INDIRECT** | Model-based or inferred current observation |
| **SENSE-HYBRID** | Integrated protection/diagnostic signal plus external precision observation |

## 3. Measurement boundary discipline

| Quantity | Boundary | Observation class role |
|----------|----------|------------------------|
| `I_LOAD_n` | Channel output | Primary load current (may be sensed at output) |
| `I_CH_IN_n` | Source-referred signed net | Derived via referral transform — **not** raw sense voltage alone |
| `I_ENTRY_MEAS` | Entry MP | Entry measurement — not channel sense |
| `I_STORAGE_NET` | Unallocated shared storage only | Not a channel-sense substitute |

**Prohibited:** treating `I_LOAD_n` as `I_CH_IN_n` without signed-net referral (WP-012 R1); double-counting regen in sense path and `I_STORAGE_NET` (R3).

## 4. Symbolic total error model (no numeric target)

```text
E_TOTAL =
f(
  gain error,
  offset,
  temperature drift,
  ADC error,
  reference error,
  calibration residual,
  layout parasitics,
  bandwidth,
  sampling phase,
  PWM state
)
```

No numeric accuracy Approved. ED-IN-011 remains **Open**.

## 5. Criterion evaluation

| Criterion | SENSE-INTEGRATED | SENSE-SHUNT-HS | SENSE-SHUNT-LS | SENSE-MAGNETIC | SENSE-INDIRECT | SENSE-HYBRID |
|-----------|------------------|----------------|----------------|----------------|----------------|--------------|
| Measurement boundary | Device-reported ≈ I_LOAD or replica | High-side I_LOAD path | Low-side return path | Isolated I_LOAD | Estimated I_LOAD / I_CH_IN | Dual: diag + precision I_LOAD |
| Source-referred meaning | Requires referral model | Same | Same + ground return caveats | Same | Model-dominated | Precision path + referral |
| Unidirectional / BI | Often uni; BI claim-dependent | Uni or BI with topology | Often uni; BI difficult | BI capable (class-dependent) | Model-dependent | Flexible |
| PWM observability | Claim-dependent bandwidth | Layout + amp BW | Same | Sensor BW | Weak during PWM edges | Precision path designable |
| Calibration | Device trim / class cal | Gain/offset cal | Gain/offset + GND | Offset/scale cal | Model identification | Dual cal |
| Burden / loss | Low–moderate | `P_SENSE = I²R_shunt` | Same | Low conduction | Software only | Shunt + integrated |
| Ground/reference impact | Device-referenced | High-side isolation needs | Strong GND dependence | Isolated | N/A electrical | Mixed |
| Fault survivability | Limited by device | Shunt/amp rating | Same | Sensor rating | Survives but blind | External path survivability |
| Open-load compatibility | Claim-dependent | Possible with bias | Possible | Limited | Weak | Claim + external |
| ADC / interface demand | Analog/SPI status | Diff amp + ADC | Same | Sensor IF + ADC | MCU compute | Dual IF |
| Diagnostic independence | Coupled to switch | Independent of switch die | Independent | Independent | Coupled to model | Partial independence |
| Fixture needs | Status capture | Known shunt cal fixture | Same | Sensor cal fixture | Model validation loads | Combined |

## 6. Comparison table

| Class | Capability for CH-HS-SENSE | PWM / BI fit | Main advantage | Main limitation | Main blockers | Qualification status |
|-------|----------------------------|--------------|----------------|-----------------|---------------|----------------------|
| **SENSE-INTEGRATED** | Viable if claim covers accuracy/PWM | PWM claim-dependent; BI claim-dependent | Low parts count; channel-local | Accuracy/BW Open; coupled to switch | ED-IN-011/032; OI-SENSE-001 | **CLASS_CONDITIONALLY_VIABLE** |
| **SENSE-SHUNT-HS** | Strong for precision I_LOAD | Good with amp design; BI possible | Independent of switch die | Loss, layout, common-mode | Same + PCB | **CLASS_CONDITIONALLY_VIABLE** |
| **SENSE-SHUNT-LS** | Weak for HS power path verification | Poor for HS; GND issues | Simple amp | Does not observe HS path current under many faults | Topology mismatch for HS-dominant DevKit | **CLASS_NOT_RECOMMENDED** as primary HS observation |
| **SENSE-MAGNETIC** | Viable for isolation / higher current | BI-friendly | Galvanic isolation | Cost/BW/offset class burden; fixture cal | ED-IN-011; fixture | **CLASS_CONDITIONALLY_VIABLE** — retain |
| **SENSE-INDIRECT** | Insufficient as sole CH-HS-SENSE | Weak | No shunt loss | Not independent physical observation | Verification independence | **CLASS_NOT_RECOMMENDED** as primary |
| **SENSE-HYBRID** | Strong (diag + precision) | Designable | Independence + integrated fault flags | Dual path complexity | ED-IN-011/032 | **CLASS_CONDITIONALLY_VIABLE** → prefer next stage |

## 7. Recommendations (not Accepted)

| Class | Recommendation | Conditions |
|-------|----------------|------------|
| **SENSE-HYBRID** | **RECOMMENDED_FOR_NEXT_STAGE** | Precision path defined at class level; integrated path used for protection/diagnostics; referral model documented; numerics Open |
| **SENSE-INTEGRATED** | **CONDITIONALLY_RECOMMENDED** | Acceptable sole path only if Architect accepts claim-limited accuracy/BW for DK-C-004 and CH-HS-SENSE |
| **SENSE-SHUNT-HS** | **RETAIN_FOR_COMPARISON** | Prefer as precision half of hybrid or fallback if integrated insufficient |
| **SENSE-MAGNETIC** | **RETAIN_FOR_COMPARISON** | Consider for isolated / external-envelope observation (P6 distinct — PWR-A-001) |
| **SENSE-SHUNT-LS** | **NOT_RECOMMENDED** | Primary HS channel observation |
| **SENSE-INDIRECT** | **NOT_RECOMMENDED** | Sole verification observation |

## 8. Traceability

REQ-DCC-V-DK-043 · VER-DCC-DK-C-004 · ADR-019 · ED-IN-011/032 · OI-SENSE-001 · WP-012 measurement boundaries · PWR-A-001.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial current-observation class comparison — Proposed |
