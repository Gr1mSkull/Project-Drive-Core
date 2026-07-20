# DevKit Functional Block Diagram — WP-010

**Document ID:** DOC-DK-FBD-001  
**Version:** 1.0  
**Status:** Proposed — requires Architecture Review  
**Work Package:** WP-010  
**Date:** 2026-07-20

Companion to [`DevKit_Functional_Electrical_Architecture.md`](DevKit_Functional_Electrical_Architecture.md). Diagrams are **not** substitutes for matrices.

## Legend

| Line style | Meaning |
|------------|---------|
| `==>` solid | Power / energy flow |
| `-->` dashed | Control flow |
| `-.->` dotted | Diagnostic / measurement flow |
| `==x` | Hardware safety path (kill / global disable) |
| `[Open]` | Unresolved architecture decision |

## 1. System overview

```mermaid
flowchart TB
    subgraph EXT["External boundary"]
        PSU["Lab PSU<br/>(I_PSU_limit)"]
        KILL_SW["Kill switch<br/>(IF-DK-KILL)"]
        FIX["External load-bank / fixture<br/>(I_loadbank_limit)"]
        ESTOP["Fixture E-stop"]
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
        end

        subgraph RADIO["Radio board — Service domain"]
            ESP["ESP32-class"]
        end

        subgraph POWER["Power board — representative"]
            GLOB["Global enable AND + kill AND"]
            HS["HS channels CH-HS-*"]
            BI["Bidirectional CH-BI-REP"]
            SENSE["Sense / fault aggregation"]
        end

        BENCH["Bench load<br/>(IF-DK-BASE-LOAD)"]
    end

    PSU ==>|V_IN| PROT
    PROT ==> DIST
    DIST ==> LOGIC
    DIST ==> RADIO
    DIST ==> POWER

    KILL_SW ==x GLOB
    STM -->|nENABLE_GLOBAL| GLOB
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

    FIX ==>|"[Open] isolation"| BI
    ESTOP ==x FIX
    FIX -.-x BASE
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

    K["External source"] --> L["Fixture protection"]
    L --> M["External interface"]
    M --> N["Measurement"]
    N --> O["E-stop abort"]
```

**Constraint:** Path K→M shall not back-feed D without explicit `[Open]` isolation design.

## 3. Control flow (View B)

```mermaid
flowchart TB
    L["Logic RT"] -->|SPI commands| P["Power controller"]
    L -->|PWM| P
    L -->|nENABLE_GLOBAL| G["Enable AND gate"]
    K["nKILL_HW"] --> G
    G --> P
    P --> CH["Channel drivers"]
    CH --> OUT["Load terminals"]
    P -->|FAULT_N| L
    P -->|ISENSE mux| L
    P -->|BOARD_ID| L
```

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
        P1["KILL asserted"]
        P2["nENABLE_GLOBAL inactive"]
        P3["Control-loss timeout"]
        P4["Input protection open"]
        P5["Fixture E-stop"]
    end

    subgraph FW["Firmware-requested OFF"]
        P6["Commanded OFF"]
        P7["Config invalid"]
    end

    subgraph LOC["Local protection"]
        P8["Channel OC"]
        P9["Channel SC"]
        P10["Thermal — if implemented"]
    end

    P1 & P2 & P3 & P4 & P5 --> SAFE["Outputs safe<br/>(V safe AND I safe)"]
    P6 --> CHOFF["Channel OFF"]
    P8 & P9 & P10 --> CHOFF
```

## 6. Measurement flow (View E)

```mermaid
flowchart LR
    MP1["MP-IN-V/I"] --> LOG["Data capture"]
    MP2["MP-KILL-*"] --> LOG
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
| DOM-HW-KILL | KILL_SW → GLOB |
| DOM-GLOBAL-EN | GLOB |
| DOM-EXT-BANK | FIX |
| DOM-BENCH-LOAD | BENCH |
| DOM-DCPI | STM ↔ ESP |
| DOM-CAN | CAN |
| DOM-MEASURE | MP-* (see register) |
| DOM-FIXTURE-CTL | ESTOP |

## 8. Revision history

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-07-20 | WP-010 initial block diagrams — Proposed |
