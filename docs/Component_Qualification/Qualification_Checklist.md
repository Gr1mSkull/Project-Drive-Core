# Qualification Checklist

**Document ID:** CQP-CHK-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Provide a repeatable checklist for reviewing a component qualification report before status advancement.

## 2. Scope

One checklist instance per MPN per application.

## 3. Responsibilities

Reviewer completes checklist at Engineering Review stage.

## 4. Inputs

- [Qualification_Report_Template.md](Qualification_Report_Template.md) (draft or final)
- Manufacturer datasheet

## 5. Outputs

- Checklist attached to report or referenced by WP ID
- Pass / fail / conditional for stage gate

## 6. Checklist

### 6.1 Identity

- [ ] Component name and category recorded
- [ ] Manufacturer and exact MPN recorded
- [ ] Datasheet URL, revision, date recorded

### 6.2 Electrical

- [ ] Operating voltage range cited with datasheet reference
- [ ] Continuous rating distinguished from pulse/limit/inrush
- [ ] Application load profile documented
- [ ] No invented electrical parameters

### 6.3 Thermal

- [ ] Thermal section complete or marked N/A with justification
- [ ] Power semiconductors: [Thermal_Validation.md](Thermal_Validation.md) criteria addressed

### 6.4 Protection and diagnostics

- [ ] Protection features documented or N/A
- [ ] Diagnostics capability documented or N/A

### 6.5 Lifecycle and supply chain

- [ ] Lifecycle per [Component_Lifecycle_Policy.md](Component_Lifecycle_Policy.md)
- [ ] Availability per [Availability_Policy.md](Availability_Policy.md)
- [ ] Second source per [Second_Source_Policy.md](Second_Source_Policy.md)
- [ ] Risk per [Risk_Assessment.md](Risk_Assessment.md)

### 6.6 Manufacturing

- [ ] Package and PCB footprint feasibility noted
- [ ] Assembly and test considerations noted

### 6.7 Decision

- [ ] Advantages and disadvantages evidence-based
- [ ] Decision and status align with [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md)
- [ ] Reviewer and review date recorded

## 7. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Checklist covers electrical, thermal, lifecycle, supply, manufacturing |
| AC-2 | Usable with empty candidate (process-only verification) |

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
