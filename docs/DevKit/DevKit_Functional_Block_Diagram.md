# DevKit Functional Block Diagram — WP-010

**Document ID:** DOC-DK-FBD-001  
**Version:** 1.1  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010 / WP-010-R1  
**Date:** 2026-07-20

Companion to [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md). Diagrams are **not** substitutes for matrices.

## Legend

| Line style | Meaning |
|------------|---------|
| `==>` solid | Power / energy flow |
| `-->` dashed | Control flow |
| `-.->` dotted | Diagnostic / measurement flow |
| `==x` | Hardware safety path (kill direct branch / global disable) |
| `[Open]` | Unresolved architecture decision |

## 1. System overview

```mermaid
flowchart TB
    subgraph EXT["External boundary"]
        PSU["Lab PSU<br/>(I_PSU_limit)"]
        KILL_SW["Kill switch<br/>(IF-DK-KILL)"]
        EXT_SRC["EXT-SOURCE<br/>(fixture energy supply)"]
        EXT_LB["EXT-LOAD-BANK<br/>(controlled load)"]
        EXT_MOD["EXT-POWER-MODULE<br/>[optional]"]
        ESTOP["Fixture E-stop"]
        GND_OPEN["[Open] ground/reference<br/>OI-GND-001"]
    end

    subgraph BASE["BASE DEVKIT ENVELOPE (I_certified_cont)"]
        subgraph IN["Input chain"]
            PROT["Replaceable input protection"]
            DIST["Input distribution"]
        end

        subgraph LOGIC["Logic board — RT domain"]
            STM["STM32G474-class"]
            WD["Watchdog"]
            CAN["CAN controller"]
            KILL_OBS["KILL observation branch"]
        end

        subgraph RADIO["Radio board — Service domain"]
            ESP["ESP32-class"]
        end

        subgraph POWER["Power board — representative"]
            KILL_DIR["KILL direct branch"]
            GLOB["nENABLE_GLOBAL AND"]
            HS["HS channels CH-HS-*"]
            BI["Bidirectional CH-BI-REP"]
            SENSE["Sense aggregation"]
        end

        BENCH["Bench load<br/>(IF-DK-BASE-LOAD)"]
    end

    PSU ==>|V_IN| PROT
    PROT ==> DIST
    DIST ==> LOGIC
    DIST ==> RADIO
    DIST ==> POWER

    KILL_SW ==x KILL_DIR
    KILL_SW -.-> KILL_OBS
    KILL_OBS -.-> STM
    STM -->|nENABLE_GLOBAL| GLOB
    KILL_DIR --> GLOB
    STM -->|J_LP SPI/PWM| HS
    STM -->|J_LP SPI/PWM| BI
    STM <-.->|DCPI| ESP
    STM --> CAN

    GLOB ==> HS
    GLOB ==> BI
    HS ==> BENCH
    BI --> BENCH

    HS -.-> SENSE
    BI -.-> SENSE
    SENSE -.-> STM

    EXT_SRC ==>|"[Open] back-feed blocked"| EXT_MOD
    EXT_MOD ==> EXT_LB
    EXT_LB -.-> BI
    ESTOP ==x EXT_SRC
    EXT_LB --- GND_OPEN
    BASE --- GND_OPEN
```

## 2. Energy flow (View A)

```mermaid
flowchart LR
    A["Lab PSU"] --> B["Source limit"]
    B --> C["Replaceable protection"]
    C --> D["DevKit entry"]
    D --> E["Distribution"]
    E --> F["V_LOGIC"]
    E --> G["V_RADIO"]
    E --> H["V_POWER_CTRL"]
    H --> I["HS switch"]
    I --> J["Bench load"]

    S["EXT-SOURCE"] --> T["Fixture protection"]
    T --> U["EXT-POWER-MODULE"]
    U --> V["EXT-LOAD-BANK"]
    V --> W["Measurement"]
    W --> X["E-stop abort"]
```

**Constraint:** EXT-SOURCE / EXT-LOAD-BANK path shall not back-feed D. Ground/reference at boundary: **[Open]** (OI-GND-001).

## 3. Control flow (View B)

```mermaid
flowchart TB
    subgraph KILL_TOPO["Physical KILL topology"]
        KIN["Physical KILL input"]
        KDIR["Direct hardware-effective branch"]
        KOBS["Observation branch → Logic"]
        KIN ==x KDIR
        KIN -.-> KOBS
    end

    L["Logic RT"] -->|J_LP command transport| P["Power controller"]
    L -->|PWM| P
    L -->|nENABLE_GLOBAL| G["Enable AND gate"]
    KDIR --> G
    KOBS -.-> L
    G --> P
    P --> CH["Channel drivers"]
    CH --> OUT["Load terminals"]
    P -->|diagnostic observation| L
```

KILL direct branch and `nENABLE_GLOBAL` are **distinct** authorities merged only at the enable AND gate.

## 4. Service flow (View C)

```mermaid
flowchart LR
    R["Radio Service"] <-->|DCPI binary| L["Logic RT"]
    T["Tablet / REST"] <-->|Wi-Fi| R
    L -->|CAN| BUS["CAN bus"]
    L -->|Power commands| PWR["Power outputs"]
    R -.-x PWR
```

Service path (dotted-x) has **no direct** output enable authority.

## 5. Safety flow (View D) — independent paths

```mermaid
flowchart TB
    subgraph HW["Hardware-effective OFF"]
        P1["KILL direct branch"]
        P2["nENABLE_GLOBAL inactive"]
        P3["Control-loss timeout"]
        P4["Input protection open / supply removed"]
        P5["Fixture E-stop"]
    end

    subgraph FW["Firmware-requested OFF"]
        P6["Commanded OFF"]
        P7["Config invalid → outputs inhibited"]
    end

    subgraph LOC["Local protection"]
        P8["Channel OC"]
        P9["Channel SC"]
        P10["Thermal — if implemented"]
    end

    P1 & P2 & P3 & P4 & P5 --> SAFE["Outputs safe<br/>(V safe AND I safe)"]
    P6 --> CHOFF["Channel inhibited"]
    P8 & P9 & P10 --> CHOFF
```

## 6. Measurement flow (View E)

```mermaid
flowchart LR
    MP1["MP-IN-V/I"] --> LOG["Data capture"]
    MP2["MP-KILL-RAW / COND / OBS"] --> LOG
    MP3["MP-GLOBAL-ENABLE"] --> LOG
    MP4["MP-CH-HS-IOUT"] --> LOG
    MP5["MP-JLP-FAULT"] --> LOG
    LOG --> TS["Timestamp correlation"]
    TS --> VE["Future VE package"]
```

## 7. Domain map (all major domains)

| Domain | Block in §1 |
|--------|-------------|
| DOM-LAB-SUPPLY | PSU |
| DOM-INPUT-PROTECT | PROT |
| DOM-INPUT-DIST | DIST |
| DOM-LOGIC-PWR | LOGIC |
| DOM-RADIO | RADIO |
| DOM-PWR-CTRL | POWER / GLOB |
| DOM-HS-REP | HS |
| DOM-BI-REP | BI |
| DOM-SENSE-DIAG | SENSE |
| DOM-HW-KILL | KILL_SW → KILL_DIR + KILL_OBS |
| DOM-GLOBAL-EN | GLOB |
| DOM-EXT-BANK | EXT_SRC / EXT_LB / EXT_MOD |
| DOM-BENCH-LOAD | BENCH |
| DOM-DCPI | STM ↔ ESP |
| DOM-CAN | CAN |
| DOM-MEASURE | MP-* (see register) |
| DOM-FIXTURE-CTL | ESTOP |

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial block diagrams — Proposed |
| 1.1 | 2026-07-20 | WP-010-R1 — KILL direct/observation branches; EXT-SOURCE/LOAD-BANK; ground Open marker |
