# web/ui

Минимальный Web UI Gen1 (vanilla JS). Контракт: `docs/006_Web_Interface.md`.

## Экраны

- **Race** — RPM, метрики, таблица выходов
- **Service** — PIN login + полная таблица каналов
- **Logger** — заглушка (данные с `/events`)

При отсутствии DCC показывает **demo data** для вёрстки.

## Деплой на ESP32

Скопировать содержимое в `firmware/dcc/radio/spiffs_image/` (TBD при сборке IDF).

Локальный просмотр:

```bash
cd web/ui && python -m http.server 8080
# открыть http://localhost:8080
```

REST/WS будут offline — сработает demo mode.
