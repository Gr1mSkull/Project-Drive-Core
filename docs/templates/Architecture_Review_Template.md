# Architecture Review Template

Use when a change may affect system architecture, safety, or module boundaries.

---

## Architecture Review: [Title]

| Field | Value |
|-------|-------|
| **Date** | YYYY-MM-DD |
| **Work Package** | WP-XXX |
| **Presenter** | Implementation Engineer |
| **Reviewers** | System Architect, … |
| **Status** | Scheduled \| In progress \| Accepted \| Rejected \| Deferred |

### 1. Summary

Brief description of proposed change.

### 2. Scope

What is in scope / out of scope.

### 3. Architecture impact assessment

| Area | Impact (none / low / high) | Notes |
|------|---------------------------|-------|
| Module boundaries | | |
| Safety | | |
| Communication | | |
| Hardware topology | | |
| Configuration model | | |

### 4. ADR required?

- [ ] Yes — new ADR-NNN drafted
- [ ] No — implementation only

### 5. Contradictions with existing docs

| Document | Section | Conflict description |
|----------|---------|----------------------|

### 6. Open questions

| ID | Question | Owner |
|----|----------|-------|

### 7. Review checklist

- [ ] Aligns with `docs/001`
- [ ] No undocumented protocol changes
- [ ] Safety ownership unchanged (STM32 / not ESP32)
- [ ] Traceability to SRS (when populated)

### 8. Decision

| Outcome | Conditions |
|---------|------------|
| Accept / Reject / Defer | |

### 9. Action items

| Action | Owner | Due |
|--------|-------|-----|
