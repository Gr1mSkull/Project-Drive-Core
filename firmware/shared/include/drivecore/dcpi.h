#ifndef DRIVECORE_DCPI_H
#define DRIVECORE_DCPI_H

#include <stdint.h>

#include "drivecore/proto.h"

#ifdef __cplusplus
extern "C" {
#endif

#define DCPI_CMD_STATE_PUSH       0x0001U
#define DCPI_CMD_EVENT_PUSH       0x0002U
#define DCPI_CMD_CONFIG_LOAD      0x0010U
#define DCPI_CMD_CONFIG_APPLY_ACK 0x0011U
#define DCPI_CMD_OUTPUT_TEST      0x0020U
#define DCPI_CMD_OTA_BEGIN        0x0030U
#define DCPI_CMD_OTA_CHUNK        0x0031U
#define DCPI_CMD_PING             0x00FFU

typedef struct __attribute__((packed)) {
    uint8_t  state;
    uint8_t  fault;
    uint16_t current_ma;
} dcpi_output_t;

typedef struct __attribute__((packed)) {
    uint8_t       vehicle_mode;
    uint16_t      battery_mv;
    uint16_t      total_current_ma;
    uint8_t       output_count;
    dcpi_output_t outputs[DCP_MAX_OUTPUTS];
    uint16_t      rpm;
    int16_t       coolant_temp_c10;
    uint16_t      oil_pressure_kpa;
    uint8_t       engine_flags;
    uint8_t       cooling_level;
} dcpi_state_v1_t;

typedef struct __attribute__((packed)) {
    uint32_t timestamp_ms;
    uint8_t  severity;
    uint8_t  source_len;
    char     source[16];
    uint8_t  msg_len;
    char     message[48];
} dcpi_event_v1_t;

typedef struct __attribute__((packed)) {
    uint8_t  magic[2];
    uint8_t  proto_ver;
    uint8_t  flags;
    uint16_t command;
    uint16_t length;
} dcpi_frame_header_t;

#ifdef __cplusplus
}
#endif

#endif
