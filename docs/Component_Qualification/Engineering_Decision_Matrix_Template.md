# Engineering Decision Matrix Template

**Document ID:** CQP-TPL-MTX-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

Use only when a work package **explicitly authorizes** comparison of multiple qualified or candidate MPNs.

**Do not** populate with manufacturer recommendations in framework tasks.

---

## Decision Matrix: [Application / function]

| Field | Value |
|-------|-------|
| Date | YYYY-MM-DD |
| Author | |
| Work Package | WP-XXX |
| Requirement | REQ-XXX or channel class |

### Scoring scale

| Score | Meaning |
|-------|---------|
| 0 | Unacceptable / unknown |
| 1 | Poor |
| 2 | Adequate |
| 3 | Good |
| 4 | Excellent |
| **N/A** | Not applicable — exclude from weighted score |

### Candidates

| ID | MPN | Manufacturer | Qualification report |
|----|-----|--------------|----------------------|
| A | | | link |
| B | | | link |

### Criteria scores

| Criterion | Weight (1–3) | A | B | Notes |
|-----------|--------------|---|---|-------|
| Performance | | | | |
| Reliability | | | | |
| Availability | | | | |
| Lifecycle | | | | |
| Cost | | | | |
| Diagnostics | | | | |
| Ease of Assembly | | | | |
| Ease of Testing | | | | |
| Thermal Margin | | | | |
| Automotive Qualification | | | | |
| Second Source Availability | | | | |
| Documentation Quality | | | | |

### Weighted calculation

```
Overall Engineering Score = Σ (score_i × weight_i) / Σ (weight_i)
```

(Exclude N/A criteria from denominator.)

| Candidate | Overall Engineering Score |
|-----------|---------------------------|
| A | TBD |
| B | TBD |

### Decision

| Field | Value |
|-------|-------|
| Selected candidate | TBD — architect approval |
| Rationale | Evidence-based summary |
| Reviewer | |
| Review date | |

### Revision history

| Version | Date | Change |
|---------|------|--------|
| 0.1 | | Template instance created |
