# DevKit Component-Class Matrix — WP-011

**Document ID:** DOC-DK-CCM-001  
**Version:** 1.3  
**Status:** Accepted — Architecture Review  
**Work Package:** WP-011 (Accepted); WP-013 comparison package Proposed  
**Date:** 2026-07-20

Evaluation **classes** only — no MPN, no manufacturer, no BOM. Component class definitions are evaluation criteria, not procurement shortlist.

## 1. Component-class matrix

| Function | Required capability | Evaluation classes | Forbidden assumptions | Open questions |
|----------|-------------------|-------------------|----------------------|----------------|
| **High-side switching** | ON/OFF; PWM; OC/SC reaction; control-loss OFF; retry/latch | **Class HS-INT-DIAG** — integrated smart switch with diagnostics; **Class HS-GATE-DISCRETE** — discrete FET + gate driver + separate protection; **Class HS-HYBRID** — integrated switch + external shunt | Assuming headline `I_D` equals continuous DevKit rating; assuming open-load on all channels; assuming single class covers all HS aliases | Which class supports PWM + sense + P5 fault without invalidating P3 envelope? Thermal simultaneous profile (TBD-DK-003)? |
| **Bidirectional channel** | Forward/reverse; conflict prevention; shoot-through prevention; safe OFF | **Class BI-HB-FULL** — full-bridge topology; **Class BI-HB-HALF** — half-bridge + routing; **Class BI-DUAL-SW** — dual independent switches with interlock | Assuming Gen1 production H-bridge MPN applies to DevKit; assuming stall test without fixture | OI-BI-001 topology; TBD-DK-022 stall fixture; shoot-through proof method |
| **Current sensing** | Observation for diagnostics; VER-DCC-DK-C-004 | **Class SENSE-INTEGRATED** — switch-reported current; **Class SENSE-SHUNT** — external shunt + amplifier; **Class SENSE-MIRROR** — current mirror/replica; **Class SENSE-HYBRID** — integrated + external calibration reference | Assuming TBD-DK-009 accuracy without calibration procedure; assuming mux topology from docs/002 preview | Accuracy target (TBD-DK-009); observation topology (OI-SENSE-001); per-channel vs shared sense |
| **Protection (input)** | RP; transient; OCP; UV behaviour | **Class PROT-FUSE** — replaceable fuse/OCP device; **Class PROT-ELECTRONIC** — electronic limit + disconnect; **Class PROT-HYBRID** — fuse + TVS/clamp layer | Selecting 30 A or any fuse rating as Approved; assuming LM74700 or specific OR-ing device | OI-PROT-001/002; TBD-DK-002 protection vs continuous distinction |
| **Protection (channel)** | OC; SC; energy limitation | **Class CH-PROT-INTEGRATED** — switch-internal protection; **Class CH-PROT-EXTERNAL** — external comparator + disable; **Class CH-PROT-COORD** — channel + input coordination | Channel SC always contained without upstream action | Channel vs system containment on SC (WP-010-R1); TBD-DK-011 injection method |
| **Controller interface** | J_LP SPI slave; PWM; fail-safe; BOARD_ID | **Class CTRL-SPI-ASIC** — dedicated Power controller IC; **Class CTRL-SPI-FPGA-CPLD** — programmable slave; **Class CTRL-SPI-MCU** — small MCU on Power board | Assuming shift-register topology from docs/002 is mandatory for DevKit | Control-loss fail-safe implementation; TBD-DK-007; message period vs timeout |
| **Kill / global enable** | Direct hardware branch; distinct from Logic command | **Class SAFE-HW-AND** — discrete AND/discrete enable chain; **Class SAFE-INTEGRATED** — integrated enable in switch/controller | KILL routed only through Logic GPIO without direct branch | OI-KILL-001 conditioning; timing TBD-DK-004 |
| **Measurement / bench** | MP-* accessibility | **Class FIX-BENCH-LOAD** — passive switched loads; **Class FIX-ACTIVE-LOAD** — programmable electronic load; **Class FIX-INJECT** — fault injection adapter | Using fixture energy to expand base envelope | OI-FIX-001/002; ADR-020 external path |

## 2. Mapping to WP-010 capability aliases

| WP-010 alias | Functions requiring class coverage |
|--------------|-----------------------------------|
| CH-HS-BASE | High-side switching |
| CH-HS-PWM | High-side switching (PWM mandatory) |
| CH-HS-SENSE | Current sensing |
| CH-HS-PROTECTED | High-side switching + channel protection |
| CH-BI-REP | Bidirectional channel |
| CH-HC-EXTERNAL | External fixture classes — not base PCB switch class |

Physical channel sharing (WP-010-R1) may combine aliases on one switch class **only if** qualification proves independent verification per framework §4.

## 3. Class selection rules (future WP)

1. Evaluation class must cover all **mandatory** ADR-019 capabilities claimed for DevKit.
2. Class must not require violating Accepted WP-010 safe-state or KILL topology.
3. Class thermal and current claims remain **Open** until sizing + qualification evidence.
4. Multiple evaluation classes may remain in parallel until Architect narrows scope.
5. No class selection authorizes schematic capture.
6. Class selection gated per [`DevKit_Component_Class_Qualification_Framework.md`](DevKit_Component_Class_Qualification_Framework.md) §3.1 (current envelope, thermal assumptions, protection philosophy, verification boundary).

## 4. WP-013 comparison note

WP-013 extends evaluation with additional comparison IDs (e.g. HS-INT-BASIC, HS-ARRAY, SENSE-SHUNT-HS/LS, RP-*, TRANSIENT-*, INPUT-*, BI-HB-DISCRETE/HYBRID/RELAY/DUAL-HSLS, CTRL-MIXED-HARDWIRED). See:

* [`DevKit_Component_Class_Qualification_Report.md`](DevKit_Component_Class_Qualification_Report.md)
* [`DevKit_Class_Recommendation_and_Readiness_Matrix.md`](DevKit_Class_Recommendation_and_Readiness_Matrix.md)

Recommendations remain **Proposed** — not Architecture Accepted. No MPN selected.

## 5. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-011 initial component-class matrix — Proposed |
| 1.1 | 2026-07-20 | WP-011-R1 — evaluation-class terminology; selection gating reference |
| 1.2 | 2026-07-20 | Architecture Review Accepted — PR #15 |
| 1.3 | 2026-07-20 | WP-013 — cross-ref class comparison package (matrix IDs retained; recommendations Proposed) |
