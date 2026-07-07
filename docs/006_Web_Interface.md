# 006 — Web Interface

Планшет (Android / iPad) — **только клиент**. DCC работает без планшета.

> **DCC — сервер. Планшет — клиент.**

## Трёхуровневая модель

| Слой | Платформа | Задачи |
|------|-----------|--------|
| Real-Time | STM32 | Автомобиль, CAN, силовые каналы, VCM |
| Service | ESP32 | HTTP, WebSocket, OTA, файлы UI, REST |
| Presentation | Планшет/ПК | Отрисовка Web UI в браузере |

Планшет не обязателен: двигатель, насосы, свет, вентиляторы, Button Box работают без него.

## Статика на ESP32

```
/index.html
/main.js
/style.css
/fonts/
/icons/
```

STM32 не знает, как выглядит интерфейс — только отдаёт данные по SPI.

## API

### REST — конфигурация и команды

```http
GET  /api/config
GET  /api/outputs
POST /api/output/5
```

### WebSocket — телеметрия (~20 Hz)

См. [004_Communication_Protocol.md](004_Communication_Protocol.md).

## Режимы UI

| Режим | Назначение |
|-------|------------|
| **Race** | RPM, температуры, давление, напряжение, предупреждения |
| **Service** | Полная диагностика по каналам (ток, температура, faults) |
| **Wiring** | Тест выхода по номеру — без мультиметра |
| **Logger** | Журнал событий после заезда |
| **CAN Monitor** | Состояние узлов на шине |

## OTA через Web UI

- Обновление ESP32
- Обновление STM32 (через ESP32)
- USB только для recovery / первой прошивки

## Gen1: сначала таблица, потом красота

Минимальный UI для отладки:

```text
Fuel Pump | ON | 9.3A | OK
Fan 1     | ON | 21.3A | OK
```

Красивые приборы — после стабильного железа.

## Аутентификация

ESP32: базовая аутентификация для Service/Wiring режимов (🔲 TBD).

## Нативное приложение

**DriveCore Mobile** — Gen2/3, если Web UI станет недостаточно.

## Связанные документы

- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
- [002_DCC_Hardware.md](002_DCC_Hardware.md) — Radio Board
