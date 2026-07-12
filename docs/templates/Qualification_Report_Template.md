# Qualification Report Template

Store completed reports in `hardware/qualification/[MPN]_qualification.md`.

---

## Qualification Report: [Manufacturer MPN]

| Field | Value |
|-------|-------|
| **MPN** | |
| **Manufacturer** | |
| **Status** | Provisional \| Qualified \| Rejected |
| **Date** | YYYY-MM-DD |
| **Author** | |
| **Work Package** | WP-XXX |
| **Datasheet** | URL, revision, date |

### 1. Application

- Module: DCC Logic / DCC Power / ECU / …
- Function: [e.g. HS30 channel driver]
- Load profile: [continuous / PWM / inrush] — TBD

### 2. Electrical analysis

| Parameter | Value | Conditions | Source (datasheet §) |
|-----------|-------|------------|----------------------|
| V_operating | | | |
| I_continuous | | T_amb, PCB | |
| I_pulse / I_limit | | | |

### 3. Thermal analysis

| Parameter | Value | Notes |
|-----------|-------|-------|
| P_loss max | | |
| Rth | | |
| T_junction est. | | |

### 4. Lifecycle and availability

| Field | Value |
|-------|-------|
| Lifecycle status | Active / NRND / EOL |
| Automotive grade | Yes / No / N/A |
| Second source | |

### 5. Alternatives considered

| MPN | Notes |
|-----|-------|

### 6. Conclusion

- [ ] Qualified for stated application
- [ ] Provisional only
- [ ] Rejected

### 7. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|

### Revision history

| Version | Date | Change |
|---------|------|--------|
