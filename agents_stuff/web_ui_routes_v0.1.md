# Web UI routes & API cheat sheet v0.1

Конспект. Официально: `docs/006_Web_Interface.md`, `docs/004` §5–6.

## Wi-Fi

- SSID: `DriveCore-XXXX`
- AP IP: `192.168.4.1`
- Default: SoftAP only

## Pages (hash router)

| Route | UIMode | Auth |
|-------|--------|------|
| `#/` | Race | — |
| `#/service` | Service | PIN |
| `#/wiring` | Wiring | PIN + confirm |
| `#/logger` | Logger | — |
| `#/can` | CAN | PIN |
| `#/config` | Config | PIN |
| `#/ota` | OTA | PIN |
| `#/setup` | Setup | first boot |

## REST quick ref

```
GET  /api/v1/status
GET  /api/v1/telemetry
GET  /api/v1/outputs
GET  /api/v1/outputs/{id}
POST /api/v1/outputs/{id}     # Service/Wiring only
GET  /api/v1/config           # Service
PUT  /api/v1/config           # Service
POST /api/v1/config/apply     # Service
GET  /api/v1/events
POST /api/v1/auth/login       # {"pin":"..."}
POST /api/v1/ota/esp
POST /api/v1/ota/stm32
```

## Headers (protected)

```
Authorization: Bearer <token>
X-DriveCore-Mode: service | wiring
X-DriveCore-Confirm: 1        # Wiring only
```

## WebSocket

```
ws://192.168.4.1/ws/telemetry
```

Message types: `telemetry` (20 Hz), `event`, `ota_progress`

## DCPI → JSON mapping (ESP32)

`STATE_PUSH` fields → `/telemetry` and WS `telemetry` object. See `dcpi_structs_v0.1.md`.

## Gen1 acceptance

1. Race screen shows RPM from ECU cache
2. Service lists 22 outputs
3. Wiring can pulse ch 5 on DevKit
4. Login PIN blocks POST /outputs without token
