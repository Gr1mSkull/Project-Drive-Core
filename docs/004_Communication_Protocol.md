# 004 — Communication Protocol

Обзор протоколов **DriveCore Gen1**. Детальная спецификация CAN ID и бинарных пакетов — 🔲 TBD.

## Уровни обмена

| Уровень | Технология | Участники |
|---------|------------|-----------|
| Vehicle bus | CAN FD | DCC, ECU, Button Box, расширения |
| Internal (DCC) | SPI 20–40 MHz | STM32 ↔ ESP32 |
| Service / UI | HTTP REST + WebSocket | ESP32 ↔ планшет/ПК |
| Debug | USB-C, SWD | Logic Board |

## CAN FD (автомобиль)

- **Топология:** линейная, терминаторы на концах
- **Gen1:** одна шина (или CAN1=ECU, CAN2=Body — уточнить)
- **DCC:** master config node
- Все модули равноправны на шине, но конфигурацию ведёт DCC

### Планируемые темы спецификации

- [ ] Адресация устройств (Node ID)
- [ ] Heartbeat / alive
- [ ] Сообщения телеметрии DCC → bus
- [ ] События Button Box → DCC
- [ ] Телеметрия ECU → bus
- [ ] Bootloader / firmware update over CAN
- [ ] Обнаружение устройств при старте

### Будущее: single source of truth

Описание сообщений в одном формате → автогенерация для STM32, ESP32, TypeScript, тестов, документации.

## SPI: STM32 ↔ ESP32 (внутри DCC)

**Не JSON** между MCU — бинарный протокол:

```
Header | Command | Length | Payload | CRC
```

- STM32 → ESP32: структура состояния (телеметрия, диагностика)
- ESP32 → STM32: команды конфигурации, OTA staging
- ESP32 преобразует в JSON **только** для браузера

Преимущества: скорость, меньше нагрузка на STM32, проще версионирование.

## REST API (ESP32 → клиент)

Для конфигурации и команд:

```http
GET  /api/config
GET  /api/outputs
POST /api/output/5
```

## WebSocket (ESP32 → клиент)

Телеметрия в реальном времени (~20 Hz):

```json
{
  "rpm": 4120,
  "battery": 13.8,
  "fuelPump": 9.1,
  "fan1": 21.3,
  "mode": "Race"
}
```

## OTA

- ESP32: обновление Radio + раздача прошивки STM32
- USB-C: восстановление после failed OTA, первая прошивка

## Button Box → CAN

События (не команды нагрузок):

- `press`, `release`, `long_press`, `hold`, `rotate` (энкодер)

## Связанные документы

- [002_DCC_Hardware.md](002_DCC_Hardware.md) — SPI, CAN трансиверы
- [006_Web_Interface.md](006_Web_Interface.md) — REST/WebSocket
- [005_Configuration_Model.md](005_Configuration_Model.md) — конфиг YAML → бинарный формат
