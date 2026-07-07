# 008 — Testing and Validation

> **Test before track.** Ни одна новая функция не попадает в автомобиль без проверки на стенде.

## DriveCore DevKit / DevBoard

Лабораторная плата **до** DCC Gen1 для автомобиля:

- STM32 + ESP32
- CAN FD
- Несколько Smart High Side каналов
- 1× H-bridge
- USB-C, питание, LED, кнопки
- Разъёмы для нагрузок

На DevKit отлаживаются: протокол, bootloader, конфигуратор, SPI STM32↔ESP32, диагностика.

```
DriveCore DevKit → (убрать лишнее) → DCC Gen1
```

Та же платформа — для ECU, Button Box, будущих модулей.

## Инженерный стенд

Не автомобиль — стенд до интеграции в E30:

```text
БП 13.8 В → DCC (или DevKit) → лампы / резисторы / моторчики / вентилятор → осциллограф
```

Проверяем: прошивку, защиту, диагностику, retry, thermal, undervoltage.

## Уровни тестирования

| Уровень | Что | Где |
|---------|-----|-----|
| Unit | Сервисы прошивки (state machine, CRC) | Host / target |
| Module | Канал силовой, CAN node, SPI | DevKit |
| Integration | DCC + Button Box + ECU simulator | Стенд |
| Vehicle | E30 | Трек / дорога |

## Прошивка: сервисы для тестируемости

Модульная архитектура (FreeRTOS):

- Power Manager
- Vehicle State Manager
- CAN Manager
- Diagnostics
- Logger
- Configuration Manager
- Communication Manager (SPI ↔ ESP32)

Каждый сервис — отдельный модуль с чётким API.

## Диагностика на стенде

Для каждого канала проверить:

- [ ] Нормальное включение/выключение
- [ ] Overcurrent → отключение + причина
- [ ] Short / open load
- [ ] Thermal shutdown
- [ ] Undervoltage lockout
- [ ] Retry logic
- [ ] Сообщение причины отключения в CAN / Web UI

## Web UI на стенде

- Режим **Wiring**: тест каждого output по номеру
- Режим **Service**: токи, faults в реальном времени
- Режим **CAN Monitor**: heartbeat всех узлов

## Чеклист перед машиной

- [ ] Все каналы протестированы под нагрузкой на стенде
- [ ] Тепловая стабильность (длительный прогон)
- [ ] Fail operational: отказ ESP32 / планшета не останавливает авто
- [ ] Kill switch / масса по регламенту
- [ ] Конфигурация E30 загружена и проверена
- [ ] Журнал событий пишется корректно

## Связанные документы

- [009_Roadmap.md](009_Roadmap.md) — порядок фаз
- [002_DCC_Hardware.md](002_DCC_Hardware.md) — DevKit → DCC
- [001_System_Architecture.md](001_System_Architecture.md)
