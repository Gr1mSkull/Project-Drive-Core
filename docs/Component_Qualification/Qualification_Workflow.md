# Qualification Workflow

**Document ID:** CQP-WF-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

## 1. Purpose

Define the sequential workflow for qualifying a single component candidate.

## 2. Scope

Applies to all categories under `hardware/qualification/`.

## 3. Responsibilities

Implementation Engineer executes stages; System Architect approves final status transitions to **Approved for Prototype** or **Approved for Production**.

## 4. Inputs

- Documented requirement (channel class, function, environment)
- Authorization to evaluate a **candidate** MPN (work package)

## 5. Outputs

- Qualification report with evidence
- Status update per [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md)

## 6. Workflow

```
Requirement
    ↓
Candidate Search          ← authorized WP only; record as Candidate
    ↓
Datasheet Review          ← primary manufacturer document
    ↓
Electrical Evaluation     ← continuous vs transient vs limit; cite §
    ↓
Thermal Evaluation        ← per Thermal_Validation.md
    ↓
Manufacturing Evaluation  ← package, solder, assembly, test access
    ↓
Supply Chain Evaluation   ← lifecycle, availability, second source
    ↓
Engineering Review        ← checklist + decision matrix if applicable
    ↓
Prototype Validation    ← bench / HIL when required
    ↓
Approval                  ← status: Approved for Prototype / Production
```

## 7. Stage gates

| Stage | Gate (shall) |
|-------|----------------|
| Datasheet Review | Datasheet URL, revision, date recorded |
| Electrical Evaluation | All limits cite datasheet; unknown = TBD |
| Thermal Evaluation | Required for power semiconductors and regulators |
| Engineering Review | [Qualification_Checklist.md](Qualification_Checklist.md) complete |
| Prototype Validation | Required before **Approved for Production** unless architect waives |
| Approval | Reviewer and date recorded |

## 8. Acceptance criteria

| ID | Criterion |
|----|-----------|
| AC-1 | Each stage has defined inputs and outputs |
| AC-2 | Workflow references status definitions |

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-002 initial |
