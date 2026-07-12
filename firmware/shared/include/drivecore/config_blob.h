#ifndef DRIVECORE_CONFIG_BLOB_H
#define DRIVECORE_CONFIG_BLOB_H

#include <stdint.h>

#include "drivecore/proto.h"

#ifdef __cplusplus
extern "C" {
#endif

#define DCFG_HEADER_SIZE   16U
#define DCFG_OUTPUT_SIZE   16U
#define DCFG_RULE_SIZE     32U

typedef enum {
    DCFG_OUTPUT_HS = 0,
    DCFG_OUTPUT_PWM = 1,
    DCFG_OUTPUT_HB = 2,
} dcfg_output_type_t;

typedef enum {
    DCFG_MODE_OFF = 0,
    DCFG_MODE_ON = 1,
    DCFG_MODE_AUTO = 2,
    DCFG_MODE_PRIME = 3,
} dcfg_mode_action_t;

typedef struct __attribute__((packed)) {
    uint8_t magic[4];
    uint16_t version;
    uint16_t crc16;
    uint16_t output_count;
    uint16_t rule_count;
    uint16_t mode_count;
    uint16_t reserved;
} dcfg_header_t;

typedef struct __attribute__((packed)) {
    uint8_t channel_id;
    uint8_t type;
    uint8_t current_limit_a;
    uint8_t retry;
    uint8_t flags;
    uint8_t reserved;
    uint64_t mode_mask;
} dcfg_output_entry_t;

typedef enum {
    DCFG_COND_VEHICLE_MODE = 1,
    DCFG_COND_ENGINE_RUNNING = 2,
    DCFG_COND_COOLANT_TEMP_GT = 3,
    DCFG_COND_OIL_PRESSURE_LT = 4,
    DCFG_COND_BATTERY_GT = 5,
    DCFG_COND_BATTERY_LT = 6,
    DCFG_COND_RPM_GT = 7,
    DCFG_COND_BUTTON_EVENT = 8,
} dcfg_condition_type_t;

typedef enum {
    DCFG_ACT_OUTPUT_ON = 1,
    DCFG_ACT_LOG_EVENT = 2,
    DCFG_ACT_NOTIFY = 3,
} dcfg_action_type_t;

typedef struct __attribute__((packed)) {
    uint8_t rule_id;
    uint8_t condition_type;
    int16_t condition_param;
    uint8_t action_type;
    uint8_t action_target;
    uint8_t action_param;
    uint8_t reserved[25];
} dcfg_rule_entry_t;

#ifdef __cplusplus
}
#endif

#endif
