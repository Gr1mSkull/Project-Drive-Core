# 002 — DCC Hardware

Аппаратная часть **DriveCore Controller (DCC)** — Gen1.

## Корпус

- Алюминиевый корпус (Hammond / CNC)
- Платы крепятся через термопрокладки — корпус = радиатор
- Силовая часть отделена от логики физически и по разводке

## Трёхплатная структура

```
┌─────────────────────────────────────────┐
│            DriveCore Controller         │
│  ┌──────────┐  Logic  — STM32, CAN     │
│  ┌──────────┐  Radio   — ESP32 module   │
│  ┌──────────┐  Power   — Smart High Side│
└─────────────────────────────────────────┘
```

| Плата | Меняется в Gen2? | Назначение |
|-------|------------------|------------|
| Logic Board | Редко | MCU, CAN, память, USB, watchdog |
| Power Board | Да | Силовые ключи, H-мосты, силовые разъёмы |
| Radio Board | Да (Rev.A→B) | Wi-Fi, BLE, Web UI, OTA |

DCC Gen2 = новая Power Board при той же Logic Board.

## Logic Board

См. [007_Component_Selection.md](007_Component_Selection.md).

- STM32G474RET6
- CAN FD ×2 (TCAN1042HG)
- FM24CL64B (FRAM), W25Q128JV (Flash)
- TPS3430 (watchdog)
- USB-C + TUSB320
- Питание логики: TPS54560 → TPS7A1633-Q1
- SWD (Tag-Connect или разъём)

## Power Board

### Каналы

| Класс | Кол-во | Ток | Назначение (пример E30) |
|-------|--------|-----|-------------------------|
| High | 2 | 60 A | EHPS, резерв high |
| Medium | 4 | 30 A | Вентиляторы, помпа |
| Standard | 8 | 15 A | ECU, свет, насос |
| Low | 8 | 5 A | Салон, габариты |
| H-bridge | 2 | — | Стеклоподъёмники |

+ 20% запас каналов.

### Силовые ключи

Smart High Side (Infineon PROFET+ / BTS). H-bridge: BTN8982TA ×2.

Каждый канал: ток, защита, диагностика, состояние (OFF/STARTING/ON/OVERCURRENT/RETRY/FAULT).

### Питание входа

```
АКБ → TVS (SM8S36A) → LM74700-Q1 → Buck → LDO → логика
```

Мониторинг: TPS3702, INA228 (общий ток).

## Radio Board

- Готовый модуль ESP32-S3-WROOM или ESP32-C6-WROOM
- Дочерняя плата на едином expansion-разъёме
- Связь с Logic: **SPI 20–40 MHz** (не CAN внутри корпуса)

### Expansion header (единый для дочерних плат)

Питание: 12V, 5V, 3.3V. Шины: SPI, UART. Сигналы: RESET, BOOT, INT, GPIO, GND.

В будущем в слот: LTE, GNSS, LoRa, IMU, доп. CAN, Ethernet.

## Внутренние интерфейсы

| Связь | Протокол |
|-------|----------|
| Logic ↔ Radio | SPI + бинарный протокол |
| Logic ↔ Power | Внутренняя шина (SPI + enable lines) — уточнить на схеме |

Силовая плата сменяема без замены Logic Board (ремонт в паддоке).

## Разъёмы наружу

Deutsch DTM (сигналы/CAN), DT (средние), DTP (силовые). См. [001_System_Architecture.md](001_System_Architecture.md).

## Тепловая модель

> **Статус:** 🔲 не выполнена — следующий инженерный шаг.

Нужно разложить потери на EHPS / fans / pump и спроектировать охлаждение корпуса.

## Связанные документы

- [007_Component_Selection.md](007_Component_Selection.md)
- [004_Communication_Protocol.md](004_Communication_Protocol.md) — SPI STM32↔ESP32
