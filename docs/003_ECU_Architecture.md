# 003 — ECU Architecture

**DriveCore ECU** — отдельный модуль платформы. Только силовая установка.

## Принцип

> **ECU управляет двигателем. DCC управляет автомобилем.**

ECU не знает о фарах, дворниках, стеклоподъёмниках. Не коммутирует силовые цепи кузова.

## Зона ответственности ECU

- Впрыск, зажигание
- DBW (если будет)
- Турбина, антилаг, launch
- VVT, детонация
- Телеметрия двигателя по CAN
- Опционально: **запрос** охлаждения (не прямое управление вентиляторами)

## Зона ответственности DCC (не ECU)

Питание, режимы, кнопки, свет, дворники, печка, вентиляторы, помпа, EHPS, стеклоподъёмники, диагностика, журнал, конфигурация.

## Взаимодействие ECU ↔ DCC

### ECU публикует (пример)

- RPM, Coolant Temp, Oil Pressure
- Engine Running, Throttle, MAP, Lambda

### Принцип «Request, don't control»

ECU не включает вентилятор напрямую. Публикует, например:

```text
Cooling Request = Level 2
```

DCC решает, какой канал и когда включить.

### DCC использует данные ECU для логики

Примеры:

- ОЖ ≥ 92 °C → вентилятор ступень 1
- Напряжение < 11 V при EHPS → ограничить второстепенные нагрузки

DCC не вмешивается в алгоритмы управления двигателем.

## Аппаратура ECU (Gen1 — outline)

> Детальная компонентная база ECU — отдельная фаза (см. [009_Roadmap.md](009_Roadmap.md) Фаза 2).

- Отдельная плата / модуль на CAN FD
- Разработка на том же **DriveCore DevKit**, что и DCC
- Те же протокол, bootloader, модель конфигурации

## Прошивка ECU (планируемые сервисы)

Аналогично DCC — модульно, FreeRTOS:

- Engine Control
- CAN Manager (DriveCore Protocol)
- Configuration Manager
- Diagnostics / Logger

## Связанные документы

- [001_System_Architecture.md](001_System_Architecture.md)
- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
