# DevKit Fixture Preliminary Block Design — WP-015

**Document ID:** DOC-DK-FPBD-001  
**Version:** 1.2  
**Status:** Proposed — Architecture Review pending  
**Work Package:** WP-015  
**Date:** 2026-07-20

```text
FUNCTIONAL blocks only. No concrete components, connector types, pinouts,
selected isolation/grounding topology, or numeric ratings shown.
```

## 1. Path legend

Every diagram distinguishes path types:

```text
[E]  ENERGY PATH            — hazardous energy flow
[C]  CONTROL PATH           — command / request
[A]  AUTHORIZATION PATH     — AUTH grant / revoke
[O]  OBSERVATION PATH       — measurement / state readback
[S]  SAFETY-EFFECTIVE PATH  — hardware-effective inhibit / removal
```

## 2. Base-energy operation

Energy path and source-control path are shown separately. `FX-SOURCE-CONTROL` is a command/control function: it does **not** originate energy, is **not** physical proof of energy removal, and does **not** replace energy-path observation.

```text
ENERGY PATH:
BASE-SOURCE --[E]--> BASE-ENERGY-CONTROL --[E]--> FX-BASE-ENERGY-PATH --[E]--> FX-DUT-INTERFACE --[E]--> DUT(base)

CONTROL / AUTHORIZATION PATH:
FX-OPERATOR-CONTROL --[C]--> FX-AUTHORIZATION --[A]--> FX-SOURCE-CONTROL --[C]--> BASE-ENERGY-CONTROL

OBSERVATION PATH:
FX-MEASUREMENT --[O]--> (entry/base MPs; ENERGY_PATH_OBSERVED_ACTIVE/INACTIVE)

SAFETY-EFFECTIVE PATH:
FX-ESTOP --[S]--> FX-ENERGY-REMOVAL --[S]--> BASE-ENERGY-CONTROL / FX-BASE-ENERGY-PATH
```

## 3. External-energy boundary

```text
ENERGY PATH:
EXT-SOURCE --[E]--> EXT-ENERGY-CONTROL --[E]--> FX-EXTERNAL-ENERGY-BOUNDARY --[E]--> {EXT-POWER-MODULE | DUT-under-EXT | FX-LOAD-BANK}

CONTROL / AUTHORIZATION PATH:
FX-AUTHORIZATION --[A]--> FX-SOURCE-CONTROL(ext) --[C]--> EXT-ENERGY-CONTROL
  (AUTH_EXT_SOURCE; simultaneous BASE+EXT blocked while OI-GND-001 Open)

SAFETY-EFFECTIVE PATH:
FX-EXTERNAL-ENERGY-BOUNDARY --[S]--> back-feed-prevention (external→base: PROHIBITED)
Boundary label: "Open decision — OI-GND-001" (no isolation/grounding topology shown)
```

## 4. Authorization and interlock flow

```text
Operator req --[C]--> FX-AUTHORIZATION
FX-INTERLOCK-CONTROLLER --[A]--> FX-AUTHORIZATION (gate/revoke)
   inputs [O]: identity, config, state, E-stop, measurement-ready, back-feed, load-bank state
FX-AUTHORIZATION --[A]--> {source, load-bank, fault, DUT-enable}
Any unmet interlock --[A]--> AUTH inhibited/revoked
```

Note: AUTH gating/revocation is `[A]`, not `[S]`. A hardware-effective `[S]` inhibit/removal for a specific interlock is a **separate Proposed design allocation** with a named blocker and future proof artifact (see decision register).

## 5. E-stop and energy-removal flow

```text
Operator E-stop --[S]--> FX-ESTOP --[S]--> FX-ENERGY-REMOVAL
FX-ENERGY-REMOVAL --[S]--> inhibit/remove {base, external, load-bank, fault}
FX-ENERGY-REMOVAL --[C]--> FX-DISCHARGE --[O]--> residual observation
FX-AUTHORIZATION --[A]--> all AUTH revoked (stale); recovery requires new epoch
(E-stop reset --[C]--> does NOT energize)
```

## 6. Load-bank control and energy flow

```text
FX-AUTHORIZATION --[A]--> FX-LOAD-BANK   (AUTH_LOAD_BANK)
DUT/ext output --[E]--> FX-LOAD-BANK (sink-function; independent energy origination prohibited)
Regenerative/bidirectional return --[E, reverse]--> requires explicit containment
  (does NOT reclassify load bank as EXT-SOURCE; BLOCKED_BY_ARCHITECTURE until OI-BI-001 / OI-GND-001 dispositioned)
FX-MEASUREMENT --[O]--> sink state / load current
Stuck-on --[S]--> revoke AUTH + inhibit/remove UPSTREAM energy --> FX-ENERGY-REMOVAL --> FX_LOCKOUT_UNCONFIRMED (→ FX_LOCKOUT_SAFE after confirmation)
```

## 7. Measurement and DAQ flow

```text
Energy/signal nodes --[O]--> FX-MEASUREMENT --[O]--> FX-DAQ --> {logger, operator UI, test controller}
FX-MEASUREMENT is observation-purpose. A physical measurement connection shall be treated as a
  potential energy/reference/fault path until its impedance, protection, reference, isolation, and
  fault behavior are qualified (dependency Open; OI-GND-001 where applicable).
Required measurement absent --[C/A]--> dependent test blocked / AUTH inhibited
```

## 8. Fault-injection authority

```text
FX-AUTHORIZATION --[A]--> FX-FAULT-INJECTION (AUTH_FAULT_INJECTION; default inhibited)
FX-FAULT-INJECTION --[E/C]--> bounded fault stimulus (within TEST_ACTIVE + backup protection armed)
FX-ESTOP --[S]--> inhibit fault at any point
Fault active --[S]--> FX-ENERGY-REMOVAL --> FX_LOCKOUT_UNCONFIRMED --> (confirmation) --> FX_LOCKOUT_SAFE --> deliberate recovery
```

## 9. DUT interface

```text
FX-DUT-INTERFACE groups: [E] DUT power · [C] logic · [S] KILL (observe raw/HW/logic) · [A/C] nENABLE · [C] comm
KILL and nENABLE observed independently ([O]); distinct from FX-ESTOP
```

## 10. Recovery flow

Recovery is not direct from `FX_FAULT`. The required sequence:

```text
FX_FAULT
  --[S]--> FX_ENERGY_REMOVAL
  --[C]--> FX_DISCHARGE (when applicable)
  --[O]--> FX_LOCKOUT_UNCONFIRMED
  --[O: all paths observed inactive + removal confirmed + discharge complete/proven N/A]-->
           FX_LOCKOUT_SAFE
  --[C: deliberate]--> operator RECOVERY CONFIRM
  --> FX_RECOVERY_CHECK
  --> FX_SAFE / READY (new command epoch)

Guarded shortcut (only if, on entry to FX_FAULT, all safe-state confirmations
already hold):
FX_FAULT --> FX_LOCKOUT_SAFE

PROHIBITED:
FX_FAULT --> FX_RECOVERY_CHECK   (direct)
FX_LOCKOUT_UNCONFIRMED --> FX_RECOVERY_CHECK

No transition depends solely on UI state or software display.
```

## 11. Non-shown items

Concrete components, final connectors/pinouts, selected isolation topology, selected grounding topology, and numeric ratings are intentionally **not** shown (WP-015 non-goals).

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial preliminary block design — Proposed |
| 1.1 | 2026-07-21 | WP-015-R1 — energy vs source-control paths separated; measurement as potential energy/fault path; regenerative reverse-flow containment; [S] legend misuse corrected to [A]/[C] |
| 1.2 | 2026-07-21 | WP-015-R2 — recovery diagram routes FX_FAULT via energy-removal/discharge/lockout substates; no direct fault→recovery |
