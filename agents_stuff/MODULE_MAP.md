# Module map

Карта модулей DriveCore Gen1. Каждый блок — отдельная зона ответственности.

## Системный уровень

```
[E30 Vehicle]
    │
    ├── DCC ───────────── docs/002, docs/001
    │     ├── logic/     STM32, RT layer
    │     ├── radio/     ESP32, service layer
    │     └── power/     Smart HS, H-bridge
    │
    ├── ECU ───────────── docs/003 (engine only)
    ├── Button Box ───── docs/001 (events, not loads)
    └── Tablet ────────── docs/006 (Web UI client only)
```

## DCC внутренние модули (прошивка Logic — план)

| Модуль | Документ | Зависит от |
|--------|----------|------------|
| `power_manager` | 002, 005 | config, diagnostics |
| `vehicle_state_manager` (VCM) | 001, 005 | config, can_manager |
| `can_manager` | 004 | — |
| `diagnostics` | 002, 008 | power_manager |
| `logger` | 005, 008 | FRAM/Flash |
| `config_manager` | 005 | comm_manager |
| `comm_manager` (SPI) | 004 | — |

## DCC Radio (ESP32 — план)

| Модуль | Документ |
|--------|----------|
| `spi_bridge` | 004 |
| `http_server` / `rest_api` | 006 |
| `websocket_telemetry` | 006 |
| `ota` | 004, 006 |
| `config_store` | 005 |
| `static_ui` | 006 |

## Button Box (план)

| Модуль | Документ |
|--------|----------|
| `input_scan` | 001 |
| `debounce` | 001 |
| `can_tx_events` | 004 |

## ECU (план, Фаза 2)

| Модуль | Документ |
|--------|----------|
| `engine_control` | 003 |
| `can_telemetry` | 004 |
| `cooling_request` | 003 (request only) |

## Шины и границы

| Граница | Протокол | Документ |
|---------|----------|----------|
| Vehicle | CAN FD | 004 |
| Logic ↔ Radio | SPI binary | 004 |
| Logic ↔ Power | SPI + enable (TBD) | 002 |
| Radio ↔ Tablet | HTTP/WS | 006 |
| Config human | YAML | 005 |

## Ключевые EDL (быстрые ссылки)

- EDL-001 STM32G474 → `docs/EDL/README.md`
- EDL-002 ESP32 Radio Board
- EDL-003 Smart High Side
- EDL-004 Web UI Gen1
- EDL-005 ECU ≠ body loads
- EDL-006 VCM in DCC
- EDL-007 Three-board DCC

## Именование в репозитории

| Старое имя в чате | Текущее имя |
|-------------------|-------------|
| PDM | DCC (часть функций) |
| DriveCore Controller | DCC |
| DevBoard / DevKit | DriveCore DevKit |
