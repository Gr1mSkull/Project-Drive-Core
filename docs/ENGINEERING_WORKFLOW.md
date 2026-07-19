# Engineering Workflow

**Document ID:** DOC-WF-001  
**Version:** 1.1  
**Status:** Proposed  
**Work Package:** WP-001 · **Change Request:** CR-002

## 1. Purpose

Define the lifecycle for DriveCore engineering work.

**Authoritative policy:** [.cursor/ENGINEERING_CONSTITUTION.mdc](../.cursor/ENGINEERING_CONSTITUTION.mdc) — this document is a navigation aid and shall not redefine policy.

## 2. Lifecycle

```
Idea → Requirements → Architecture → Interfaces → Qualification → Implementation → Testing → Optimization
```

Per constitution §10 Decision Hierarchy. Implementation shall never bypass this order.

## 3. Work packages

Work is assigned via **Work Packages** (see `docs/templates/Work_Package_Template.md`).

Implementation Engineer executes approved packages only.

## 4. Task execution (agents and engineers)

```
Read → Implement → Validate → Report → Stop
```

Defined in `.cursor/ENGINEERING_CONSTITUTION.mdc` §12.

Before shared normative changes: Change Impact Analysis (constitution §6; template `docs/templates/Change_Impact_Analysis_Template.md`).

Validation claims require reproducible evidence (constitution §6; template `docs/templates/Verification_Evidence_Template.md`).

## 5. Documentation stages (Gen1 completed scaffold)

| Stage | Artifacts |
|-------|-----------|
| 1 | Architecture: 001, 004, 005 |
| 2 | Hardware: 002, 007 |
| 3 | ECU + UI: 003, 006 |
| 4 | Validation: 008 |
| 5 | Code scaffold: firmware/shared, tools, web |

## 6. Decision recording

Architectural decisions → `docs/ADR/` and `docs/EDL/`.

## 7. Validation gate

DevKit and bench per `docs/008` before vehicle install (EDL-014).

Traceability scaffold: `docs/traceability/`.

## 8. Related documents

- [REVIEW_PROCESS.md](REVIEW_PROCESS.md)
- [009_Roadmap.md](009_Roadmap.md)
- [.ai/current_phase.md](../.ai/current_phase.md)
- [.cursor/ENGINEERING_CONSTITUTION.mdc](../.cursor/ENGINEERING_CONSTITUTION.mdc)

## 9. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-12 | WP-001 foundation |
| 1.1 | 2026-07-19 | CR-002 — reference CIA, evidence, decision hierarchy |
