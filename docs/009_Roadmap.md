# 009 — Roadmap

## Фаза 0 — Foundation

- DriveCore DevKit
- Архитектура и документация (этот репозиторий)
- DriveCore Protocol (CAN FD + SPI + REST/WebSocket)
- Модель конфигурации
- Bootloader / OTA pipeline

## Фаза 1 — Первый автомобиль (E30)

- DCC Gen1 (Logic + Power + Radio)
- Button Box Gen1
- Web UI (планшет)
- Интеграция с E30
- Стенд + тесты в машине

## Фаза 2 — Силовая установка

- ECU Gen1
- Логгер / калибровка
- Анализ данных

## Фаза 3 — Экосистема

- Датчики
- Беспроводная телеметрия
- Конфигуратор
- Нативное мобильное приложение (если Web UI недостаточно)

## Фаза 4 — Gen2

- DCC Gen2 (больше каналов / другие ключи — только Power Board)
- Собственная приборная панель (Dash)
- Ethernet
- Несколько шин CAN FD

## Порядок разработки Gen1 (из диалога)

1. Архитектура и протокол
2. DevKit
3. DCC Gen1
4. Button Box
5. Web UI
6. Интеграция E30
7. ECU
8. Gen2

## Документация

| ID | Документ | Статус |
|----|----------|--------|
| 000 | Project Vision | ✅ концепция |
| 001 | System Architecture | ✅ концепция |
| 002 | DCC Hardware | ✅ концепция (тепловая модель TBD) |
| 003 | ECU Architecture | ✅ концепция (железо — Фаза 2) |
| 004 | Communication Protocol | ✅ концепция (CAN/SPI spec TBD) |
| 005 | Configuration Model | ✅ концепция (schema TBD) |
| 006 | Web Interface | ✅ концепция |
| 007 | Component Selection | ✅ |
| 008 | Testing and Validation | ✅ концепция |
| 009 | Roadmap | ✅ |
| EDL | Engineering Decision Log | ✅ начальный (7 записей) |
| — | agents_stuff/ | ✅ конспекты для агентов |

## Будущее: single source of truth для CAN

Описания сообщений → автогенерация структур для STM32, ESP32, TypeScript, документации, тестовых пакетов.
