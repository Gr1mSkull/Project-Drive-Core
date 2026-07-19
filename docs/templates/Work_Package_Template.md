# Work Package Template

Authoritative policy: `.cursor/ENGINEERING_CONSTITUTION.mdc` (§12, §19, §20).

---

# WORK PACKAGE WP-XXX

## [Title]

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | Draft \| Approved \| In progress \| Complete |
| **Author** | |
| **Date** | YYYY-MM-DD |

### Role

You are the Implementation Engineer for the DriveCore automotive platform.

Architecture is defined. Your responsibility is **implementation only**.

Do NOT make architectural decisions. If required, stop and report **ARCHITECTURAL DECISION REQUIRED**.

---

### OBJECTIVE

[Clear, measurable objective]

---

### SCOPE

#### In scope

-

#### Out of scope

-

---

### INPUTS

| Document | Purpose |
|----------|---------|
| `docs/001` | Architecture |
| … | |

---

### DELIVERABLES

| Deliverable | Path / criterion |
|-------------|------------------|
| | |

---

### ACCEPTANCE CRITERIA

| ID | Criterion | Verification |
|----|-----------|--------------|
| AC-1 | | |

---

### CONSTRAINTS

- Do not select components (unless WP authorizes)
- Do not modify architecture
- Follow Decision Hierarchy (constitution §10)
- Change Impact Analysis required before modifying shared normative artifacts (constitution §6)
- …

---

### QUALITY CONTROLS (when applicable)

| Control | Artifact |
|---------|----------|
| Impact classification | Level 0 / 1 / 2 before editing (constitution §6) |
| Level 1 Lightweight Impact Note | In this WP or Completion Report |
| Level 2 Full CIA | Template → `docs/records/change_impact/CIA-YYYY-NNN_<short-title>.md` |
| Verification Evidence | Template → `docs/records/verification/VE-YYYY-NNN_<short-title>.md` |
| Review Handoff Package | Template → `docs/records/review_handoffs/RHP-YYYY-NNN_<short-title>.md` |
| Traceability | `docs/traceability/TRACEABILITY_MATRIX.md` (atomic IDs only) |

---

### OUTPUT (mandatory completion report)

1. Task Summary  
2. Files Created  
3. Files Modified  
4. Validation Performed (commands + **actual results**; evidence references)  
5. Acceptance Criteria (PASS/FAIL/PARTIAL/NOT VERIFIED)  
6. Open Questions  
7. Risks and Observations  
8. Out-of-Scope Recommendations  
9. Final Status: Ready for Review \| Blocked \| Partially Complete \| Failed Validation  

Include: `Impact classification: Level N — …`

After completion **STOP**. Wait for review. Implementer self-review is Implementation Review only — not independent Critical Review. Implementer does not certify own high-impact verification.
