# firmware/shared

Общие структуры DriveCore Protocol (DCP), DCPI и config blob для STM32 / ESP32 / host tools.

## Сборка (host)

```bash
cd firmware/shared
cmake -B build && cmake --build build
ctest --test-dir build
```

## Заголовки

| Путь | Содержание |
|------|------------|
| `include/drivecore/proto.h` | CAN ID, VCM, OutputState |
| `include/drivecore/dcpi.h` | STATE_PUSH, EVENT_PUSH |
| `include/drivecore/config_blob.h` | DCFG binary layout |
| `include/drivecore/crc16.h` | CRC-16/CCITT |

Генерация из `.dcmsg` — будущее (см. roadmap).
