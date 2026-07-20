# DevKit Current-Observation Class Comparison — WP-013

**Document ID:** DOC-DK-COCC-001  
**Version:** 1.2  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-013 / WP-013-R1  
**Date:** 2026-07-20

```text
Class comparison only — no accuracy target, MPN, or ADC Approved.
Final observation-class choice remains blocked while ED-IN-011/032 and OI-SENSE-001 are Open.
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
| Burden / loss | Low–moderate | Profile-consistent `I²R` (see SPC) | Same | Sensor supply | Compute only | Integrated + shunt — allocate once |
| Ground/reference impact | Device-referenced | High-side isolation needs | Strong GND dependence | Isolated | N/A electrical | Mixed |
| Fault survivability | Limited by device | Shunt/amp rating | Same | Sensor rating | Survives but blind | External path survivability |
| Open-load compatibility | Claim-dependent | Possible with bias | Possible | Limited | Weak | Claim + external |
| ADC / interface demand | Analog/SPI status | Diff amp + ADC | Same | Sensor IF + ADC | MCU compute | Dual IF |
| Diagnostic independence | Coupled to switch | Independent of switch die | Independent | Independent | Coupled to model | Partial independence |
| Fixture needs | Status capture | Known shunt cal fixture | Same | Sensor cal fixture | Model validation loads | Combined |

## 6. Comparison table

| Class | Capability for CH-HS-SENSE | PWM / BI fit | Main advantage | Main limitation | Main blockers | Qualification status |
|-------|----------------------------|--------------|----------------|-----------------|---------------|----------------------|
| **SENSE-INTEGRATED** | Viable if claim covers accuracy/PWM for mapped role | PWM claim-dependent; BI claim-dependent | Low parts count; channel-local | Accuracy/BW Open; coupled to switch | ED-IN-011/032; OI-SENSE-001 | **CLASS_CONDITIONALLY_VIABLE** |
| **SENSE-SHUNT-HS** | Strong for precision I_LOAD | Good with amp design; BI possible | Independent of switch die | Loss, layout, common-mode | Same + PCB | **CLASS_CONDITIONALLY_VIABLE** — retain precision class |
| **SENSE-SHUNT-LS** | Weak as **primary** HS-path observation | Poor for many HS faults; GND issues | Simple amp | Does not observe HS path under many faults | Topology mismatch for HS-primary use | **CLASS_NOT_RECOMMENDED** as primary HS observation — **not** globally rejected |
| **SENSE-MAGNETIC** | Viable for isolation / higher current / BI | BI-friendly | Galvanic isolation | Cost/BW/offset class burden; fixture cal | ED-IN-011; fixture | **CLASS_CONDITIONALLY_VIABLE** — retain |
| **SENSE-INDIRECT** | Insufficient as **sole** CH-HS-SENSE verification | Weak | No shunt loss | Not independent physical observation | Verification independence | **CLASS_NOT_RECOMMENDED** as sole verification observation |
| **SENSE-HYBRID** | Strong when independence/accuracy required | Designable | Independence + integrated fault flags | Dual path complexity; inputs Open | ED-IN-011/032; OI-SENSE-001 | **CLASS_CONDITIONALLY_VIABLE** — **not** unconditional preferred |

## 7. Recommendations (not Accepted) — WP-013-R1

While **ED-IN-011**, **ED-IN-032**, and **OI-SENSE-001** remain Open, no observation class is an unconditional preferred selection. Architect may accept **evaluation directions**; final choice remains **blocked by measurement requirements**.

| Class | Recommendation | Conditions |
|-------|----------------|------------|
| **SENSE-INTEGRATED** | **CONDITIONALLY_RECOMMENDED** | For diagnostic/protection observation when accuracy, bandwidth, PWM, and fault-state claims satisfy the mapped verification role |
| **SENSE-HYBRID** | **CONDITIONALLY_RECOMMENDED** | When an Accepted requirement demands greater accuracy, independent observation, calibration separation, or diagnostic diversity — **not** unconditional preferred |
| **SENSE-SHUNT-HS** | **RETAIN_FOR_COMPARISON** | External precision-observation class |
| **SENSE-MAGNETIC** | **RETAIN_FOR_COMPARISON** | Bidirectional, isolated, or external-envelope cases (P6 distinct — PWR-A-001) |
| **SENSE-SHUNT-LS** | **NOT_RECOMMENDED** as primary HS observation | Not globally rejected for other topologies/roles |
| **SENSE-INDIRECT** | **NOT_RECOMMENDED** | **Not permitted** as the sole verification observation |

## 8. Traceability

REQ-DCC-V-DK-043 · VER-DCC-DK-C-004 · ADR-019 · ED-IN-011/032 · OI-SENSE-001 · WP-012 measurement boundaries · PWR-A-001.

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-013 initial current-observation class comparison — Proposed |
| 1.1 | 2026-07-20 | WP-013-R1 — SENSE-HYBRID conditional only; INTEGRATED conditional for diag/protect; SHUNT-LS not globally rejected |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #17 merged (`d1698a0` / `23bdb07`); methodology Accepted; final classes/topology Open; TBD-DK-007 BLOCKED unchanged |
