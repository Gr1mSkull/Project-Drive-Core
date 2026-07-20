# DevKit Fixture Preliminary Block Design — WP-015

**Document ID:** DOC-DK-FPBD-001  
**Version:** 1.0  
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

```text
FX-OPERATOR-CONTROL --[C]--> FX-AUTHORIZATION --[A]--> FX-SOURCE-CONTROL
FX-SOURCE-CONTROL   --[E]--> FX-BASE-ENERGY-PATH --[E]--> FX-DUT-INTERFACE --[E]--> DUT(base)
FX-MEASUREMENT      --[O]--> (entry/base MPs)
FX-ESTOP            --[S]--> FX-ENERGY-REMOVAL --[S]--> FX-SOURCE-CONTROL / FX-BASE-ENERGY-PATH
```

## 3. External-energy boundary

```text
FX-AUTHORIZATION --[A]--> FX-SOURCE-CONTROL(ext)  (AUTH_EXT_SOURCE; blocked simultaneous with base while OI-GND-001 Open)
FX-SOURCE-CONTROL(ext) --[E]--> FX-EXTERNAL-ENERGY-BOUNDARY --[E]--> {EXT-POWER-MODULE | DUT-under-EXT | FX-LOAD-BANK}
FX-EXTERNAL-ENERGY-BOUNDARY --[S]--> back-feed-prevention (toward base distribution: PROHIBITED)
Boundary label: "Open decision — OI-GND-001" (no isolation/grounding topology shown)
```

## 4. Authorization and interlock flow

```text
Operator req --[C]--> FX-AUTHORIZATION
FX-INTERLOCK-CONTROLLER --[A-gate]--> FX-AUTHORIZATION
   inputs [O]: identity, config, state, E-stop, measurement-ready, back-feed, load-bank state
FX-AUTHORIZATION --[A]--> {source, load-bank, fault, DUT-enable}
Any unmet interlock --[S]--> inhibit (fail-safe)
```

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
DUT/ext output --[E]--> FX-LOAD-BANK (sink; energy absorbed, never sourced)
FX-MEASUREMENT --[O]--> sink state / load current
Stuck-on --[S]--> revoke AUTH + inhibit/remove UPSTREAM energy --> FX-ENERGY-REMOVAL --> LOCKOUT
```

## 7. Measurement and DAQ flow

```text
Energy/signal nodes --[O]--> FX-MEASUREMENT --[O]--> FX-DAQ --> {logger, operator UI, test controller}
FX-MEASUREMENT is non-energy-bearing ([O] only; never [E])
Required measurement absent --[S]--> block dependent tests
```

## 8. Fault-injection authority

```text
FX-AUTHORIZATION --[A]--> FX-FAULT-INJECTION (AUTH_FAULT_INJECTION; default inhibited)
FX-FAULT-INJECTION --[E/C]--> bounded fault stimulus (within TEST_ACTIVE + backup protection armed)
FX-ESTOP --[S]--> inhibit fault at any point
Fault active --[S]--> FX-ENERGY-REMOVAL --> LOCKOUT --> deliberate recovery
```

## 9. DUT interface

```text
FX-DUT-INTERFACE groups: [E] DUT power · [C] logic · [S] KILL (observe raw/HW/logic) · [A/C] nENABLE · [C] comm
KILL and nENABLE observed independently ([O]); distinct from FX-ESTOP
```

## 10. Recovery flow

```text
FAULT/LOCKOUT --[C]--> operator RECOVERY CONFIRM (deliberate)
FX-INTERLOCK-CONTROLLER --[O]--> residual/discharge confirmed + identity/config valid
--> FX_RECOVERY_CHECK --> FX_SAFE/READY (new command epoch)
No transition depends solely on UI state or software display.
```

## 11. Non-shown items

Concrete components, final connectors/pinouts, selected isolation topology, selected grounding topology, and numeric ratings are intentionally **not** shown (WP-015 non-goals).

## 12. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-015 initial preliminary block design — Proposed |
