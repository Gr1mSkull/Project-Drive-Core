# DCPI binary structs v0.1

Конспект для реализации `firmware/shared`. Официальная спека — `docs/004`.

## STATE_PUSH (0x0001) — STM32 → ESP32, 50 ms

```c
typedef struct __attribute__((packed)) {
    uint8_t  vehicle_mode;      // VCM id
    uint16_t battery_mv;
    uint16_t total_current_ma;
    uint8_t  output_count;      // 22
    struct {
        uint8_t  state;         // OutputState
        uint8_t  fault;
        uint16_t current_ma;
    } outputs[22];
    // ECU cache
    uint16_t rpm;
    int16_t  coolant_temp_c10;  // 0.1°C
    uint16_t oil_pressure_kpa;
    uint8_t  engine_flags;
    uint8_t  cooling_level;
} dcpi_state_v1_t;
```

Размер: 4 + 22×4 + 8 = **100 байт** (проверить alignment при порте).

## EVENT_PUSH (0x0002)

```c
typedef struct __attribute__((packed)) {
    uint32_t timestamp_ms;
    uint8_t  severity;  // 0=info, 1=warn, 2=error
    uint8_t  source_len;
    char     source[16];
    uint8_t  msg_len;
    char     message[48];
} dcpi_event_v1_t;
```

## CONFIG_LOAD (0x0010) — ESP32 → STM32

Payload = полный `DCFG` blob из `config_binary_v0.1.md`.
