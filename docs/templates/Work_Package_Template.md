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
| Change Impact Analysis | `docs/templates/Change_Impact_Analysis_Template.md` |
| Verification Evidence | `docs/templates/Verification_Evidence_Template.md` |
| Review Handoff Package | `docs/templates/Review_Handoff_Package_Template.md` (high-impact) |
| Traceability | `docs/traceability/TRACEABILITY_MATRIX.md` |

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

After completion **STOP**. Wait for review. Implementer self-review is Implementation Review only — not independent Critical Review.
