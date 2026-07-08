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

## Заполнение документации (по этапам)

| Этап | Документы | Статус |
|------|-----------|--------|
| **1. Архитектура** | 001, 004, 005, EDL 008–010 | ✅ v0.1 |
| **2. Аппаратура** | 002, 007, EDL 011 | ✅ v0.1 |
| **3. ECU + UI** | 003, 006, EDL 012–013 | ✅ v0.1 |
| **4. Валидация** | 008 | 🔲 следующий |
| **5. Реализация** | firmware/, hardware/ | 🔲 |

Прогресс: `agents_stuff/DOC_PROGRESS.md`

## Документация

| ID | Документ | Статус |
|----|----------|--------|
| 000 | Project Vision | ✅ |
| 001 | System Architecture | ✅ **v0.1** |
| 002 | DCC Hardware | ✅ **v0.1** |
| 003 | ECU Architecture | ✅ **v0.1** |
| 004 | Communication Protocol | ✅ **DCP v0.1** |
| 005 | Configuration Model | ✅ **schema v0.1** + e30_gen1.yaml |
| 006 | Web Interface | ✅ **v0.1** |
| 007 | Component Selection | ✅ **v0.1** |
| 008 | Testing and Validation | ✅ концепция |
| 009 | Roadmap | ✅ |
| EDL | Engineering Decision Log | ✅ 13 записей |
| — | agents_stuff/ | ✅ |
| — | config/vehicles/e30_gen1.yaml | ✅ |

## Будущее: single source of truth для CAN

Описания сообщений → автогенерация структур для STM32, ESP32, TypeScript, документации, тестовых пакетов.
