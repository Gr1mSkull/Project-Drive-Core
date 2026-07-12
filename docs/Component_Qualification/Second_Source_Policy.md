# Second Source Policy

**Document ID:** CQP-SS-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define when and how alternate manufacturers or MPNs are documented for DriveCore components.

## 2. Scope

All categories. Second-source qualification is a separate report per MPN.

## 3. Responsibilities

Implementation Engineer documents **known alternatives** field; does not select preferred alternate without authorization.

## 4. Inputs

- Datasheet and footprint compatibility analysis (when tasked)
- Architect direction on single-source acceptance

## 5. Outputs

- **Known Alternatives** section in qualification report
- Separate qualification record per alternate if approved for use

## 6. Policy

1. **Form-fit-function** alternates shall be listed when identified during review.
2. Pin-compatible ≠ qualified — each MPN requires its own qualification report.
3. Single-source components shall be flagged as supply chain risk in [Risk_Assessment.md](Risk_Assessment.md).
4. Critical path components (MCU, main PROFET classes, CAN transceiver) shall prioritize second-source documentation when architect requires.
5. This policy does not recommend specific alternate MPNs.

## 7. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Distinction between listed alternate and qualified alternate |
| AC-2 | No alternate MPN recommended in framework docs |

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
