# 006 — Web Interface

Версия: **Gen1 v0.1** · Статус: **этап 3 — зафиксировано**

Планшет (Android / iPad) — **только клиент**. DCC работает без планшета.

> **DCC — сервер. Планшет — клиент.**

## 1. Трёхуровневая модель

| Слой | Платформа | Задачи |
|------|-----------|--------|
| Real-Time | STM32 | Автомобиль, CAN, силовые каналы, VCM |
| Service | ESP32 | HTTP, WebSocket, OTA, файлы UI, REST |
| Presentation | Планшет/ПК | Отрисовка Web UI в браузере |

STM32 не знает, как выглядит интерфейс — только отдаёт бинарный `STATE_PUSH` по SPI.

## 2. Сеть и подключение

### 2.1 Wi-Fi режимы ESP32

| Режим | SSID | Когда |
|-------|------|-------|
| **SoftAP** (default) | `DriveCore-XXXX` | В машине / на стенде; XXXX = последние 4 hex MAC |
| **STA** (опц.) | Home garage SSID | OTA из дома, сохранён в NVS |
| **AP+STA** | Оба | Планшет к AP, ESP32 к интернету для OTA |

Пароль AP по умолчанию: **печатается на наклейке DCC** (уникальный per-device). Смена — через Service mode.

### 2.2 URL

| Сервис | URL |
|--------|-----|
| Web UI | `http://192.168.4.1/` |
| REST API | `http://192.168.4.1/api/v1/` |
| WebSocket | `ws://192.168.4.1/ws/telemetry` |
| OTA upload | `POST /api/v1/ota/esp` |

mDNS (опц.): `http://drivecore.local/` — если включено в прошивке ESP32.

## 3. Режимы UI (UIMode)

UIMode — логический уровень поверх VCM. Не путать с `vehicle_mode` (OFF, RACE, …).

| UIMode | Auth | Назначение |
|--------|------|------------|
| **Race** | Нет | Приборы, предупреждения, минимум отвлечений |
| **Service** | PIN | Полная диагностика, токи, faults, конфиг read |
| **Wiring** | PIN + confirm | Тест выходов по номеру канала |
| **Logger** | Нет* | Журнал событий (*Service для export) |
| **CAN** | Service PIN | Монитор узлов, heartbeat, raw counters |
| **Config** | Service PIN | Просмотр/загрузка YAML |
| **OTA** | Service PIN | Обновление прошивок |

Переключение UIMode — только на клиенте; ESP32 проверяет права на **опасные** API.

## 4. Экраны (wireframes v0.1)

### 4.1 Race

```text
┌────────────────────────────────────────┐
│  RACE          13.8V    ENGINE_RUN  ●  │
├────────────────────────────────────────┤
│         RPM                            │
│        4120                            │
│  CLT 88°C   OIL 2.4 bar   MAP 180 kPa  │
├────────────────────────────────────────┤
│  ⚠ Low oil (если active)               │
├────────────────────────────────────────┤
│  Fan1 ON 21A │ Fan2 OFF │ FP 9.1A      │
└────────────────────────────────────────┘
     [Service]              [Logger]
```

Данные: WebSocket 20 Hz. Крупные цифры, тёмная тема, контраст для солнца.

### 4.2 Service

```text
┌────────────────────────────────────────┐
│  SERVICE                    [Logout]   │
├────────────────────────────────────────┤
│  Mode: ENGINE_RUN   ECU: OK   CAN: OK  │
├────────────────────────────────────────┤
│ Ch │ Name        │ State │ A   │Fault │
│  1 │ EHPS        │ ON    │48.2 │  —   │
│  3 │ Fan1        │ ON    │21.3 │  —   │
│  6 │ Fuel pump   │ ON    │ 9.1 │  —   │
│  7 │ ECU power   │ ON    │ 4.2 │  —   │
│ ...                                    │
├────────────────────────────────────────┤
│ [Wiring] [CAN] [Config] [OTA]          │
└────────────────────────────────────────┘
```

Таблица всех 22 каналов + HB. Сортировка по fault.

### 4.3 Wiring

```text
┌────────────────────────────────────────┐
│  WIRING TEST          ⚠ Только на стенде│
├────────────────────────────────────────┤
│  Channel: [  5  ▼]  Water pump         │
│  [ ON ]  [ OFF ]  [ PULSE 2s ]         │
│  Last: 9.3A, no fault                  │
├────────────────────────────────────────┤
│  «Подтверждаю: автомобиль на подъёмнике»│
│  [ ] Checkbox    [ Apply ]             │
└────────────────────────────────────────┘
```

`POST /outputs/{id}` разрешён только при `X-DriveCore-Mode: wiring` + valid session + confirm header.

### 4.4 Logger

Список событий с фильтром severity. Export CSV через `GET /events?format=csv` (Service PIN).

### 4.5 CAN Monitor

| Node | State | Last HB | FW | Serial |
|------|-------|---------|-----|--------|
| DCC | RUN | 12 ms | 1.2 | DC-001 |
| ECU | RUN | 45 ms | 0.1 | ECU-sim |
| Button Box | RUN | 38 ms | 1.0 | BB-001 |

### 4.6 Config

- Просмотр текущего конфига как JSON (`GET /config`)
- Upload YAML (`PUT /config`) → validate → preview diff
- Apply (`POST /config/apply`) → SPI → STM32

### 4.7 OTA

```text
  ESP32:  v1.0.2  [Upload .bin]
  STM32:  v1.0.1  [Upload .bin] → relay via SPI
  Status: ████████░░ 80%
```

## 5. Аутентификация

### 5.1 Модель (Gen1)

| Уровень | Механизм |
|---------|----------|
| Wi-Fi | WPA2-PSK (уникальный пароль AP) |
| Service API | **6-digit PIN** (установлен при первом включении) |
| Session | `POST /api/v1/auth/login` → `token` (UUID, TTL 8 h, NVS на ESP32) |
| Wiring | Тот же token + header `X-DriveCore-Confirm: 1` |

PIN хранится как **SHA-256 hash** в NVS ESP32. Сброс — удержание кнопки на DevKit / `factory_reset` по USB.

### 5.2 Endpoints auth

```http
POST /api/v1/auth/login
Content-Type: application/json
{"pin": "123456"}

→ 200 {"token": "...", "expires_in": 28800}

POST /api/v1/auth/logout
Authorization: Bearer <token>

→ 204
```

Защищённые маршруты:

```http
Authorization: Bearer <token>
X-DriveCore-Mode: service | wiring
```

Race / Logger read — без token.

### 5.3 Первый запуск

1. Планшет подключается к `DriveCore-XXXX`.
2. Браузер открывает `/` → wizard «Set PIN».
3. PIN сохраняется на ESP32; повторный wizard только после factory reset.

## 6. REST API — полная карта v0.1

Base: `http://192.168.4.1/api/v1/`

| Method | Path | Auth | Описание |
|--------|------|------|----------|
| GET | `/status` | — | Версии, uptime, vehicle_mode, nodes |
| GET | `/telemetry` | — | Снимок (REST fallback) |
| GET | `/outputs` | — | Все каналы |
| GET | `/outputs/{id}` | — | Один канал (id = 1–22, 101–102 HB) |
| POST | `/outputs/{id}` | Service/Wiring | `{"state":"on","pwm":128}` |
| GET | `/config` | Service | YAML → JSON |
| PUT | `/config` | Service | Upload body YAML |
| POST | `/config/validate` | Service | Validate only |
| POST | `/config/apply` | Service | Validate → binary → SPI |
| GET | `/events` | — | `?limit=100&severity=warn` |
| GET | `/events` | Service | `?format=csv` |
| GET | `/can/nodes` | Service | Таблица узлов |
| POST | `/auth/login` | — | PIN → token |
| POST | `/auth/logout` | Bearer | Invalidate |
| POST | `/auth/pin` | Bearer | Смена PIN |
| POST | `/ota/esp` | Service | multipart .bin |
| POST | `/ota/stm32` | Service | multipart → SPI OTA |
| GET | `/ota/status` | Service | Progress |
| POST | `/system/reboot` | Service | ESP32 reboot |
| POST | `/system/factory_reset` | Service + confirm | NVS wipe |

### 6.1 Примеры

**GET /outputs/6** (fuel pump):

```json
{
  "id": 6,
  "name": "fuel_pump",
  "state": "ON",
  "current_a": 9.1,
  "fault": null,
  "pwm_duty": null,
  "channel_class": "hs30"
}
```

**POST /outputs/5** (Wiring test):

```http
POST /api/v1/outputs/5
Authorization: Bearer ...
X-DriveCore-Mode: wiring
X-DriveCore-Confirm: 1
Content-Type: application/json

{"state": "on", "timeout_ms": 2000}
```

**PUT /config** — body = raw YAML file.

## 7. WebSocket

### 7.1 Endpoint

`ws://192.168.4.1/ws/telemetry`

При подключении сервер шлёт `hello`; клиент может слать `subscribe` (опц. фильтр).

### 7.2 Сообщения server → client (20 Hz)

```json
{
  "type": "telemetry",
  "ts": 1719876543210,
  "vehicle_mode": "ENGINE_RUN",
  "battery_v": 13.82,
  "total_a": 87.4,
  "ecu": {
    "rpm": 4120,
    "coolant_c": 88.2,
    "oil_kpa": 240,
    "running": true
  },
  "outputs": {
    "fuel_pump": {"state": "ON", "a": 9.1, "fault": null},
    "fan1": {"state": "ON", "a": 21.3, "fault": null}
  },
  "warnings": []
}
```

### 7.3 Event push (по событию)

```json
{
  "type": "event",
  "severity": "warning",
  "source": "rules",
  "message": "Low oil pressure",
  "ts": 1719876544000
}
```

ESP32 формирует JSON из `STATE_PUSH` + `EVENT_PUSH` (DCPI). STM32 JSON не строит.

## 8. Статика на ESP32

```
web/ui/
├── index.html          # SPA shell
├── main.js             # Router, WS client, API
├── style.css
├── manifest.json       # PWA (опц.)
├── icons/
│   └── ...
└── fonts/
```

Сборка: `web/ui` → `firmware/dcc/radio/spiffs_image/` (или embed в flash).

Минимальный Gen1 UI — **одна HTML + vanilla JS**, без React (меньше RAM на ESP32).

## 9. Навигация (client-side router)

```text
/              → Race (default)
/service       → Service table
/wiring        → Wiring test
/logger        → Event log
/can           → CAN monitor
/config        → Config editor
/ota           → OTA
/setup         → First-run PIN wizard
```

Hash-router (`#/service`) для совместимости без server-side routes.

## 10. OTA через Web UI

| Цель | Поток |
|------|-------|
| ESP32 | Browser → POST `/ota/esp` → `esp_ota` partition |
| STM32 | Browser → POST `/ota/stm32` → ESP32 буфер → DCPI `OTA_BEGIN`/`OTA_CHUNK` → STM32 bootloader |

Прогресс: WebSocket `type: ota_progress` или polling `GET /ota/status`.

USB-C + SWD — recovery если OTA сломала обе прошивки.

## 11. Gen1: сначала таблица, потом красота

Минимальный приемочный UI:

```text
Fuel Pump | ON | 9.3A | OK
Fan 1     | ON | 21.3A | OK
```

Критерий готовности Gen1:
- [ ] WebSocket telemetry стабильно 20 Hz
- [ ] Service table все 22 ch
- [ ] Wiring test с confirm на стенде
- [ ] OTA ESP32 с планшета
- [ ] PIN login работает

Красивые gauge / анимации — после стабильного железа (Gen1.1).

## 12. Нативное приложение

**DriveCore Mobile** — Gen2/3, если Web UI станет недостаточно (фон, CarPlay, push).

## 13. Статус

- [x] UIMode, экраны, навигация
- [x] Auth: PIN + Bearer token
- [x] REST полная карта v0.1
- [x] WebSocket форматы
- [x] Wi-Fi SoftAP/STA
- [ ] Реализация `web/ui/`
- [ ] PWA / offline cache (опц.)

## Связанные документы

- [004_Communication_Protocol.md](004_Communication_Protocol.md)
- [005_Configuration_Model.md](005_Configuration_Model.md)
- [002_DCC_Hardware.md](002_DCC_Hardware.md) — Radio Board
- [agents_stuff/web_ui_routes_v0.1.md](../agents_stuff/web_ui_routes_v0.1.md)
