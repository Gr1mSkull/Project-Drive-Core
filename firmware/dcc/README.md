# firmware/dcc

DCC прошивка: **logic** (STM32) + **radio** (ESP32).

## Статус

Скелет репозитория. Полные CubeIDE / ESP-IDF проекты — после DevKit PCB.

| Путь | Платформа | Статус |
|------|-----------|--------|
| `../shared` | C library | ✅ v0.1 |
| `logic/` | STM32G474 FreeRTOS | 🔲 |
| `radio/` | ESP32-S3 IDF | 🔲 |

Общие структуры протокола — только из `firmware/shared`.
