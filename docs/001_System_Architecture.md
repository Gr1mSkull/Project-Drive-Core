# 001 — System Architecture

## Обзор Gen1

```
                    CAN FD (линейная шина)
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    DCC (master)          ECU           Button Box
  PDM+VCM+diag         двигатель      умная клавиатура
         │
    Wi-Fi / BLE (Radio Board)
         │
   Android / iPad (Web UI — только клиент)
```

Три основных устройства в автомобиле:

1. **DCC** — DriveCore Controller (мозг кузовной электроники)
2. **ECU** — только силовая установка
3. **Button Box** — HMI, события кнопок

Планшет — внешний клиент, не узел CAN.

## DCC — DriveCore Controller

Три платы внутри одного корпуса:

| Плата | Назначение |
|-------|------------|
| **Logic Board** | STM32G474, CAN FD ×2, FRAM, Flash, USB-C, watchdog, SWD |
| **Power Board** | Smart High Side, H-мосты, TVS, измерение токов, силовые разъёмы |
| **Radio Board** | ESP32-S3/C6 модуль — Wi-Fi, BLE, Web UI, OTA |

DCC = сервер данных. Планшет = клиент.

### Функции DCC

- PDM (распределение питания)
- VCM (режимы автомобиля)
- Диагностика всех цепей
- CAN gateway
- Data logging (FRAM + Flash)
- Конфигурируемая логика «если → то»

### Управляемые нагрузки (E30)

EHPS, электропомпа, 2× вентиляторы, бензонасос, ECU, свет, салон (печка, дворники), стеклоподъёмники, резерв.

## ECU

Только двигатель: впрыск, зажигание, DBW, турбина, антилаг, launch, VVT. Не коммутирует силовые цепи кузова.

## Button Box

- STM32 + CAN FD
- Механические кнопки + энкодеры
- События: press, release, long press, hold, rotate
- **Не управляет нагрузками** — только отправляет события в DCC
- Управление: свет, дворники, печка, режимы, вспомогательные функции

## Режимная модель (VCM)

```
OFF → MASTER ON → IGNITION → PRIME → READY → ENGINE RUN → RACE → COOL DOWN → OFF
```

Каждый выход активируется по таблице режимов, а не жёсткой прошивкой.

## CAN

- 1 шина CAN FD (Gen1)
- Линейная топология, терминаторы на концах
- DCC = master config node
- CAN1: ECU, CAN2: Body Network (или один общий bus — уточнить на этапе протокола)

## Выключатель массы

Физический контактор обязателен (регламент). DCC мониторит состояние, но не заменяет kill switch.

## Силовая архитектура проводки

```
АКБ → Главный контактор массы → DCC → [ECU, EHPS, Pump, Fans, Fuel, Lights, ...]
```

Один центральный силовой хаб. Без реле (только smart switches).

## Канальная структура Power Board

| Класс | Каналы |
|-------|--------|
| High power | 2 × 60 A |
| Medium | 4 × 30 A |
| Standard | 8 × 15 A |
| Low | 8 × 5 A |
| H-bridge | 2 (стеклоподъёмники / актуаторы) |

+ 20% запас + 4 универсальных IO + expansion port (SPI/I2C/UART).

## Диагностика (на каждый канал)

Ток, напряжение, состояние, причина отключения: overcurrent, short, open load, thermal, undervoltage, command off.

## DevKit

DCC производный от DevKit, а не наоборот:

```
DriveCore DevKit → убрать лишнее → DCC Gen1
```

DevKit — лабораторная плата для разработки протокола, bootloader, конфигурации, Button Box, Web UI.
