# Config binary v0.1

Конспект для `tools/config_compiler`. Официальная спека — `docs/005`.

## Header (16 bytes)

| Offset | Size | Field |
|--------|------|-------|
| 0 | 4 | `DCFG` magic |
| 4 | 2 | version `0x0001` |
| 6 | 2 | crc16 (всё после header) |
| 8 | 2 | output_count |
| 10 | 2 | rule_count |
| 12 | 2 | mode_count |
| 14 | 2 | reserved |

## Output entry (16 bytes each)

| Offset | Size | Field |
|--------|------|-------|
| 0 | 1 | channel_id (1..22, 101=HB1) |
| 1 | 1 | type (0=HS, 1=PWM, 2=HB) |
| 2 | 1 | current_limit_a |
| 3 | 1 | retry |
| 4 | 1 | flags (bit0=pwm) |
| 5 | 1 | reserved |
| 6 | 8 | mode_mask[8] | 2 bit per mode × 8 modes = 16 bit used in 64 bit

`mode_mask` encoding per mode: 00=off, 01=on, 10=auto, 11=prime (2 bits × 8 modes).

## Rule entry (variable, v0.1 simplified)

Фиксированный размер **32 bytes** в v0.1 (max 16 rules):

- `rule_id` u8
- `condition_type` u8
- `condition_param` i16
- `action_type` u8
- `action_target` u8 (output index)
- padding + reserved

Полный expression tree — config v0.2.

## Max sizes Gen1

- outputs: 22
- rules: 16
- modes: 8
- Total blob ≈ 16 + 22×16 + 16×32 = **912 bytes** + header
