# DriveCore — Architecture Summary (AI)

Concise summary of **approved** architecture. Full spec: `docs/001`.

## Topology

```
Battery → [Master contactor] → DCC → loads
                CAN FD (linear)
         DCC — ECU — Button Box
DCC — Wi-Fi — Tablet (optional)
```

## DCC internal

| Board | MCU / role |
|-------|------------|
| Logic | STM32G474 — real-time, CAN, VCM, SPI master |
| Power | PROFET + H-bridge — 22 ch + 2 HB |
| Radio | ESP32 — REST, WS, OTA, UI |

Links: J_LP (Logic↔Power SPI), J_EXP (Radio daughtercard).

## Software layers

| Layer | Platform |
|-------|----------|
| Real-Time | STM32 |
| Service | ESP32 |
| Presentation | Tablet browser |

## Protocol

- **DCP v0.1** on CAN — see `docs/004`
- **DCPI** on SPI — see `firmware/shared/`, EDL-010
- **REST/WS** — see `docs/006`

## Configuration

YAML → `tools/config_compiler` → DCFG binary → STM32 FRAM.

## Validation path

DevKit → integration bench → DCC Gen1 → E30 (`docs/008`, EDL-014).

## Key ADR/EDL

EDL-001..014 in `docs/EDL/README.md`; index in `docs/ADR/README.md`.
