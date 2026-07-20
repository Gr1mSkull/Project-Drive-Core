# DevKit EDL-011 Clarification Proposal — WP-011

**Document ID:** DOC-DK-EDL011-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-011  
**Date:** 2026-07-20  
**Author role:** Implementation Engineer

```text
Clarification PROPOSAL only — EDL-011 file is NOT modified by this document.
No numeric timing value is Approved.
TBD-DK-007 remains BLOCKED until Architect accepts an interpretation path.
```

## 1. Purpose

Document semantic ambiguity in Accepted **EDL-011** regarding Logic↔Power control-loss / SPI fail-safe timing, analyze four interpretation options, and recommend an architecture path that:

- preserves Accepted **ADR-022** timing policy;
- preserves Accepted **WP-009** decisions (budget method Accepted; numeric Open; no `>100 ms` or `≤100 ms` bound approved);
- does **not** approve numeric thresholds;
- enables a future controlled EDL clarification CR if EDL text amendment is required.

## 2. Authoritative source text (unchanged)

From `docs/EDL/README.md` (EDL-011) — **Accepted, not edited**:

```text
Fail-safe: SPI timeout > 100 ms или nENABLE_GLOBAL=LOW → все выходы OFF.
```

Related Accepted context:

| Source | Statement |
|--------|-----------|
| EDL-011 | SPI command transport via J_LP; hardware lines include `nKILL_HW`, `nENABLE_GLOBAL`, `FAULT_N` |
| ADR-022 | Control-loss is T-Class C — distinct from kill (H) and watchdog (R); numeric Open |
| WP-009 §4 | Ambiguity documented; TBD-DK-007 **BLOCKED_BY_EDL_CLARIFICATION** |
| WP-010 §12 | Control-loss fail-safe on J_LP disconnect; numeric **BLOCKED** |
| REQ-DCC-V-DK-035 | Logic↔Power comm loss → safe de-energized (`TBD-DK-007`) |

## 3. Ambiguity statement

The phrase `SPI timeout > 100 ms` is ambiguous across at least four dimensions:

1. **Semantic role** — Is `100 ms` a detection threshold, maximum allowed silence before OFF, minimum filter interval, or historical design note?
2. **Measurement boundary** — Start/end events for "timeout" (last valid frame vs last SPI edge vs CS inactive) are not defined in EDL-011.
3. **Authority split** — Power-side hardware fail-safe vs Logic-side timeout policy vs combined end-to-end budget (WP-009 §3.3).
4. **Normative scope** — Whether the phrase binds DevKit gate evidence, production DCC Gen1, or both.

**WP-009-R1 explicitly rejected** treating EDL-011 text as an Approved numeric bound for TBD-DK-007. That disposition is retained.

## 4. Option analysis

### Option A — Control-loss timeout threshold

**Interpretation:** EDL-011 defines a nominal **control-loss detection timeout threshold** (~100 ms). Control channel lost → Power side waits until threshold → safe state.

| Aspect | Analysis |
|--------|----------|
| **Advantages** | Simple reading; aligns with common SPI watchdog patterns; gives implementers a starting candidate |
| **Risks** | Treats `>100 ms` as Approved without tolerance, measurement boundary, or safety-class proof; conflicts with WP-009 "no numeric direction"; may incorrectly bound TBD-DK-007 from below or above |
| **ADR-022 compatibility** | Partial — establishes T-Class C path but may collapse budget layers if 100 ms copied as total response |
| **WP-009 compatibility** | **Poor** — directly contradicts BLOCKED_BY_EDL_CLARIFICATION and rejected readings A/B from WP-009 §4.2 |
| **Missing information** | Filter margin; message period; missed-frame policy; Power-side vs Logic-side detection split; load-decay end condition |

### Option B — Control-loss safety requirement (timeout determined later)

**Interpretation:** EDL-011 defines that the system **must detect control loss** and reach safe state, but the **numeric timeout is determined later** by safety architecture, component capability, and verification — not by the EDL phrase alone.

| Aspect | Analysis |
|--------|----------|
| **Advantages** | Preserves ADR-022 budget model; aligns with WP-009 Accepted closure method; avoids silent numeric freeze |
| **Risks** | EDL text may be read as already fixing timing; requires explicit Architect disposition so implementers do not assume 100 ms |
| **ADR-022 compatibility** | **Good** — T-Class C remains separate; total time = sum of budget terms (Open numerics) |
| **WP-009 compatibility** | **Good** — matches Accepted budget §3.3 and measurement plan; TBD-DK-007 stays Open |
| **Missing information** | Authoritative statement that EDL phrase is non-numeric; future CR may still be needed to amend EDL wording |

### Option C — Historical implementation statement only

**Interpretation:** The `>100 ms` phrase records **historical / candidate implementation information** from early architecture (Gen1 preview, docs/002 alignment) and **cannot be treated as normative** for DevKit gate pass criteria or TBD-DK-007 closure.

| Aspect | Analysis |
|--------|----------|
| **Advantages** | Explains candidate values in docs/008/docs/002 without elevating them; protects against gate PASS on unapproved numbers |
| **Risks** | If EDL-011 is Accepted, dismissing entire fail-safe clause as non-normative may overreach — the **requirement** (fail-safe on SPI loss) likely remains normative even if `100 ms` does not |
| **ADR-022 compatibility** | Partial — requirement preserved if fail-safe obligation retained; timing still Open |
| **WP-009 compatibility** | **Good** for numeric rejection; needs pairing with Option B/D for requirement semantics |
| **Migration implications** | DevKit verification must not PASS on `≤100 ms` or `>100 ms` alone; traceability notes EDL phrase as non-numeric; future EDL CR may clarify or relocate timing text |

### Option D — Combined interpretation (recommended architecture path)

**Interpretation:** EDL-011 **establishes the fail-safe requirement** (SPI communication loss and/or `nENABLE_GLOBAL` inactive → outputs OFF). The **exact timing contract** for TBD-DK-007 is derived from:

1. Accepted ADR-022 T-Class C budget structure (WP-009 §3.3);
2. Power-side fail-safe mechanism (WP-010);
3. Measurement on normalized start/end events (WP-009 measurement plan);
4. Future Architect acceptance of numeric value — optionally preceded by EDL text clarification CR.

The `>100 ms` phrase is **informational context only** until a separate Accepted record defines its normative role (if any).

| Aspect | Analysis |
|--------|----------|
| **Advantages** | Unifies B + C; preserves requirement without numeric approval; enables EDL CR as separate step; matches engineering constitution (no silent contradiction resolution) |
| **Risks** | Two-step closure (architecture acceptance + future numeric freeze) may delay DK-A/C cases; teams may still treat 100 ms as implicit default without governance discipline |
| **ADR-022 compatibility** | **Good** — hierarchical timing preserved |
| **WP-009 compatibility** | **Good** — extends §4 with formal option analysis; no numeric approval |

## 5. Decision table

| Option | Interpretation | Benefits | Risks | Compatibility (ADR-022 / WP-009) | Recommendation |
|--------|----------------|----------|-------|-----------------------------------|----------------|
| **A** | Timeout threshold ≈100 ms | Simple | Silent numeric freeze; WP-009 conflict | Poor / Poor | **Reject** for numeric binding |
| **B** | Safety requirement; timeout later | Budget-safe; Open numerics | EDL text ambiguity remains | Good / Good | **Accept** as partial model |
| **C** | Historical numeric only | Blocks false normative use | May over-dismiss EDL if misapplied | Partial / Good | **Accept** for numeric rejection only |
| **D** | Requirement in EDL + timing from safety arch | Complete architecture path; CR-optional | Two-step closure | Good / Good | **Recommended** |

## 6. Recommendation (Implementation Engineer — not Approved)

**Recommend Option D** for Architecture Review acceptance:

```text
1. EDL-011 normatively requires SPI-loss / nENABLE_GLOBAL fail-safe → outputs OFF.
2. EDL-011 does NOT Approved TBD-DK-007 numeric value.
3. The ">100 ms" phrase is NOT an Accepted lower bound, upper bound, or pass criterion.
4. TBD-DK-007 closure uses WP-009 budget §3.3 + measurement plan + future numeric freeze.
5. Optional follow-on: EDL clarification CR to amend EDL-011 wording (separate from WP-011).
```

**Does not:**

- modify EDL-011;
- set TBD-DK-007 numeric value;
- authorize firmware timeout implementation;
- mark VER-DCC-DK-A-008 or C-012 PASS.

## 7. Proposed EDL clarification CR content (future — not executed in WP-011)

If Architect directs EDL amendment, a future CR **may** propose text along:

```text
Fail-safe: Loss of valid Logic↔Power command transport OR nENABLE_GLOBAL inactive
→ all power outputs OFF through Power-side fail-safe mechanism.
Numeric control-loss timeout for verification: TBD-DK-007 (Open) — not defined by this EDL entry alone.
```

Exact CR wording requires System Architect authorization. **WP-011 does not create or submit this CR.**

## 8. Impact on TBD-DK-007 disposition

| Field | WP-011 proposal |
|-------|-----------------|
| Register Status | **Open** (unchanged) |
| Blocker | **BLOCKED_BY_EDL_CLARIFICATION** until Architect accepts Option D (or alternative) |
| Methods Accepted | WP-009 budget + measurement (unchanged) |
| Numeric | **Open** — no ms value Approved |
| Verification | VER-DCC-DK-A-008, C-012 remain **BLOCKED** for numeric PASS |

## 9. Traceability

| Requirement | WP-011 reference |
|-------------|------------------|
| REQ-DCC-V-DK-035 | Control-loss safe de-energize |
| REQ-DCC-V-DK-011 | J_LP interface intent |
| DK-GOV-024, 025 | Threshold freeze rules (unchanged) |
| ADR-022 | T-Class C timing policy |
| TBD-DK-007 | Primary subject |

## 10. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-011 initial EDL-011 clarification proposal — Proposed |
