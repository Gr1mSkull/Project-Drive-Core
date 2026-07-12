# Qualification Report Template

**Document ID:** CQP-TPL-RPT-001  
**Version:** 1.0  
**Status:** Proposed  
**Work Package:** WP-002

Store completed reports in:

```
hardware/qualification/<category>/<Manufacturer>_<MPN>_qualification.md
```

---

## Qualification Report

| Field | Value |
|-------|-------|
| **Component Name** | |
| **Manufacturer** | |
| **Manufacturer Part Number (MPN)** | |
| **Category** | e.g. high_side, mcu, can |
| **Lifecycle** | Active / NRND / EOL / Unknown |
| **AEC Qualification** | Q100 / Q101 / Q200 / N/A / Unknown |
| **Datasheet Version** | URL, document number, date |
| **Status** | Per [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md) |
| **Work Package** | WP-XXX |
| **Author** | |
| **Review Date** | YYYY-MM-DD |
| **Reviewer** | |

---

### Operating Voltage

| Parameter | Min | Typ | Max | Unit | Datasheet § |
|-----------|-----|-----|-----|------|-------------|
| Supply | | | | V | |

### Temperature Range

| Parameter | Min | Max | Unit | Datasheet § |
|-----------|-----|-----|------|-------------|
| Operating ambient | | | °C | |
| Junction (if applicable) | | | °C | |

### Electrical Limits

| Parameter | Value | Conditions | Datasheet § |
|-----------|-------|------------|-------------|
| | | | |

### Continuous Ratings

| Parameter | Value | Conditions (V, T_amb, PCB, duty) | Datasheet § |
|-----------|-------|----------------------------------|-------------|
| | | | |

### Transient Ratings

| Parameter | Value | Duration | Datasheet § |
|-----------|-------|----------|-------------|
| Inrush / pulse / current limit | | | |

### Thermal Characteristics

| Parameter | Value | Notes | Datasheet § |
|-----------|-------|-------|-------------|
| Rth | | | |
| P_loss (application) | | TBD until calculated | |

See [Thermal_Validation.md](Thermal_Validation.md).

### Protection Features

| Feature | Present | Notes |
|---------|---------|-------|
| | Yes / No / N/A | |

### Diagnostics

| Capability | Present | Notes |
|------------|---------|-------|
| | Yes / No / N/A | |

### Mechanical Package

| Field | Value |
|-------|-------|
| Package name | |
| Footprint compatibility | TBD |
| Thermal pad | Yes / No |

### Known Alternatives

| MPN | Manufacturer | Qualification status | Notes |
|-----|--------------|----------------------|-------|
| | | Not qualified | |

Per [Second_Source_Policy.md](Second_Source_Policy.md) — listing does not imply approval.

### Supply Chain Risk

| Factor | Assessment |
|--------|------------|
| Single source | Yes / No / Unknown |
| Lead time | TBD |
| Counterfeit sensitivity | Low / Medium / High |

### Availability

| Field | Value | Date of check |
|-------|-------|---------------|
| Stock / lead time | TBD | |

### Cost Estimate

| Quantity | Unit cost | Currency | Source | Date |
|----------|-----------|----------|--------|------|
| TBD | | | | |

### Engineering Notes

<!-- Evidence-based observations only -->

### Advantages

-

### Disadvantages

-

### Decision

| Field | Value |
|-------|-------|
| Recommendation | Approve prototype / Approve production / Reject / Defer |
| Conditions | |

### References

| Type | Reference |
|------|-----------|
| Datasheet | |
| Requirement | REQ-XXX |
| Related ADR/EDL | |

---

### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | | | Initial draft |
