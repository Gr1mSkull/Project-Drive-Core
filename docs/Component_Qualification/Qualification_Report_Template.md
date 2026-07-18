# Qualification Report Template

**Document ID:** CQP-TPL-RPT-001  
**Version:** 1.1  
**Status:** Proposed  
**Work Package:** WP-002 · **Change Request:** CR-001

Store completed reports at:

```
hardware/qualification/{category}/{manufacturer}_{mpn}_qualification.md
```

Normative methodology: [Qualification_Methodology.md](Qualification_Methodology.md).

---

## Evidence typing (mandatory)

Mark every technical value in one column:

| Type | Meaning |
|------|---------|
| **Datasheet** | Direct quote or table from manufacturer datasheet (cite §) |
| **Calculated** | Derived from datasheet parameters and stated assumptions |
| **Measured** | Bench or lab measurement (cite test report ID) |
| **Assumption** | Temporary until validated — requires follow-up |
| **TBD** | Unknown — blocks approval until resolved |

---

## Qualification Report

### Identification

| Field | Value |
|-------|-------|
| **Component Name** | |
| **Manufacturer** | |
| **Manufacturer Part Number (MPN)** | |
| **Category** | e.g. `{category}` = high_side, mcu, can |
| **Lifecycle** | Active / NRND / EOL / Unknown |
| **AEC Qualification** | Q100 / Q101 / Q200 / N/A / Unknown |
| **Datasheet Version** | URL, document number, date |
| **Status** | Per [Qualification_Status_Definitions.md](Qualification_Status_Definitions.md) |
| **Work Package** | WP-XXX / CR-XXX |

### Application context

| Field | Value |
|-------|-------|
| **Intended Application** | Functional role in DriveCore (e.g. DCC Ch03 fan output) |
| **Target Module** | DCC Logic / DCC Power / DCC Radio / ECU / Button Box / other |
| **Hardware Revision Compatibility** | e.g. Power Rev.A, DevKit Rev.DK — TBD |
| **Related Requirement IDs** | REQ-XXX, SRS volume § — TBD |
| **Load Type** | Resistive / inductive / motor / lamp / electronic / mixed |
| **Nominal Operating Profile** | Steady-state current, voltage, environment — TBD |
| **Startup / Inrush Profile** | Peak current, duration — TBD |
| **Duty Cycle** | Continuous / PWM % / intermittent — TBD |
| **Simultaneous Load Assumptions** | Other channels active concurrently — TBD |
| **Application-Specific Derating** | Firmware or thermal derating applied — TBD |
| **Usage Restrictions** | Conditions under which part shall not be used — TBD |
| **Required External Protection** | Fuse, TVS, snubber, etc. — TBD |

### Approval chain

| Field | Value |
|-------|-------|
| **Prepared By** | |
| **Reviewed By** | |
| **Approved By** | System Architect or authorized Reviewer only for Approved* status |
| **Approval Date** | YYYY-MM-DD |

---

### Operating Voltage

| Parameter | Min | Typ | Max | Unit | Evidence type | Datasheet § |
|-----------|-----|-----|-----|------|---------------|-------------|
| Supply | | | | V | | |

### Temperature Range

| Parameter | Min | Max | Unit | Evidence type | Datasheet § |
|-----------|-----|-----|------|---------------|-------------|
| Operating ambient | | | °C | | |
| Junction (if applicable) | | | °C | | |

### Electrical Limits

| Parameter | Value | Conditions | Evidence type | Datasheet § |
|-----------|-------|------------|---------------|-------------|
| | | | | |

### Continuous Ratings

| Parameter | Value | Conditions (V, T_amb, PCB, duty) | Evidence type | Datasheet § |
|-----------|-------|----------------------------------|---------------|-------------|
| | | | | |

### Transient Ratings

| Parameter | Value | Duration | Evidence type | Datasheet § |
|-----------|-------|----------|---------------|-------------|
| Inrush / pulse / current limit | | | | |

### Thermal Characteristics

| Parameter | Value | Notes | Evidence type | Datasheet § |
|-----------|-------|-------|---------------|-------------|
| Rth | | | | |
| P_loss (application) | | | Calculated / Measured / TBD | |

See [Thermal_Validation.md](Thermal_Validation.md).

### Protection Features

| Feature | Present | Notes | Evidence type |
|---------|---------|-------|---------------|
| | Yes / No / N/A | | |

### Diagnostics

| Capability | Present | Notes | Evidence type |
|------------|---------|-------|---------------|
| | Yes / No / N/A | | |

### Mechanical Package

| Field | Value | Evidence type |
|-------|-------|---------------|
| Package name | | Datasheet |
| Footprint compatibility | TBD | |
| Thermal pad | Yes / No | Datasheet |

### Known Alternatives

| MPN | Manufacturer | Qualification status | Notes |
|-----|--------------|----------------------|-------|
| | | Not qualified | |

Per [Second_Source_Policy.md](Second_Source_Policy.md) — listing does not imply approval.

### Supply Chain Risk

| Factor | Assessment | Evidence type |
|--------|------------|---------------|
| Single source | Yes / No / Unknown | |
| Lead time | TBD | |
| Counterfeit sensitivity | Low / Medium / High | |

### Availability

| Field | Value | Date of check | Evidence type |
|-------|-------|---------------|---------------|
| Stock / lead time | TBD | | |

### Cost Estimate

| Quantity | Unit cost | Currency | Source | Date | Evidence type |
|----------|-----------|----------|--------|------|---------------|
| TBD | | | | | TBD |

### Validation references

| Field | Value |
|-------|-------|
| **Prototype Validation References** | WP IDs, bench logs, DevKit phase — TBD |
| **Laboratory Test Report References** | Report filename, date, summary — TBD |

> Recording validation references supports **Lab Validation** status; does not authorize BOM without **Approved for Prototype** or higher.

### Engineering Notes

Evidence-based observations only. Tag assumptions and TBD items explicitly.

### Advantages

-

### Disadvantages

-

### Unresolved TBD items

| Item | Blocks status |
|------|---------------|
| | Approved for Prototype / Production |

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
| Test reports | |

---

### Revision history

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 0.1 | | | Initial draft |
