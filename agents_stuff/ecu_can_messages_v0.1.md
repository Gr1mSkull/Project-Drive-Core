# ECU CAN messages v0.1

Конспект. Официально: `docs/003_ECU_Architecture.md`, `docs/004_Communication_Protocol.md`.

## Node

- Device Type: `0x2`
- Instance: `0`
- Base: `0x20`

## ID table

| Message | MC | msg_type | CAN ID (hex) | Period |
|---------|-----|----------|--------------|--------|
| HEARTBEAT | 0 | 0x01 | 0x020 | 100 ms |
| ENGINE_TELEM | 1 | 0x20 | 0x120 | 20 ms |
| COOLING_REQ | 1 | 0x21 | 0x120 | 100 ms |
| DIAG (in) | 3 | 0x40 | 0x320 | on req |
| VEHICLE_MODE (in) | 3 | 0x44 | 0x320 | 200 ms from DCC |

Formula: `CAN_ID = (MC << 8) | 0x20`

## ENGINE_TELEM decode (C)

```c
// payload after DCP header (offset 4)
uint16_t rpm = rd_u16(buf + 4);
int16_t  clt_c10 = rd_i16(buf + 6);  // divide by 10.0
uint16_t oil_kpa = rd_u16(buf + 8);
uint8_t  throttle = buf[10];
uint8_t  flags = buf[11];
bool running = flags & 1;
```

## Cooling levels

| Level | Meaning | Typical DCC action |
|-------|---------|------------------|
| 0 | Off | Rules may still run fans by CLT |
| 1 | Stage 1 | fan1 |
| 2 | Stage 2 | fan1 + fan2 |
| 3 | Max | fan1 + fan2 full duty |

## Timeouts

- ECU HB missing > 500 ms → LOST
- ENGINE_TELEM stale > 100 ms → use last value, flag stale in UI

## Simulator

`tools/can_sim` should emit 0x120 @ 20 ms with incrementing RPM for bench tests.
