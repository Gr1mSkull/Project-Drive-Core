#ifndef DRIVECORE_PROTO_H
#define DRIVECORE_PROTO_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define DCP_PROTO_VER           0x01U
#define DCPI_MAGIC_0            0xDCU
#define DCPI_MAGIC_1            0x01U
#define DCPI_PROTO_VER          0x01U

#define DCFG_MAGIC_0            'D'
#define DCFG_MAGIC_1            'C'
#define DCFG_MAGIC_2            'F'
#define DCFG_MAGIC_3            'G'
#define DCFG_VERSION            0x0001U

#define DCP_MAX_OUTPUTS         22U
#define DCP_MAX_RULES           16U
#define DCP_MAX_MODES           8U

/** Message Class (CAN ID bits 10..8). */
typedef enum {
    DCP_MC_HEARTBEAT   = 0,
    DCP_MC_TELEMETRY   = 1,
    DCP_MC_EVENT       = 2,
    DCP_MC_COMMAND     = 3,
    DCP_MC_DIAGNOSTIC  = 4,
    DCP_MC_CONFIG      = 5,
} dcp_message_class_t;

/** Device types (CAN ID bits 7..4). */
typedef enum {
    DCP_DT_DCC        = 0x1,
    DCP_DT_ECU        = 0x2,
    DCP_DT_BUTTON_BOX = 0x3,
} dcp_device_type_t;

/** Build 11-bit standard CAN ID. */
static inline uint16_t dcp_can_id(dcp_message_class_t mc, dcp_device_type_t dt, uint8_t instance)
{
    return (uint16_t)(((uint16_t)mc << 8) | ((uint16_t)dt << 4) | (instance & 0x0FU));
}

/** DCP CAN payload header (bytes 0..3). */
typedef struct __attribute__((packed)) {
    uint8_t  proto_ver;
    uint8_t  msg_type;
    uint16_t seq;
} dcp_can_header_t;

/** VCM mode IDs (config v0.1). */
typedef enum {
    VCM_OFF = 0,
    VCM_MASTER_ON = 1,
    VCM_IGNITION = 2,
    VCM_PRIME = 3,
    VCM_READY = 4,
    VCM_ENGINE_RUN = 5,
    VCM_RACE = 6,
    VCM_COOL_DOWN = 7,
} vcm_mode_t;

/** OutputState from docs/004. */
typedef enum {
    OUTPUT_OFF = 0,
    OUTPUT_STARTING = 1,
    OUTPUT_ON = 2,
    OUTPUT_OVERCURRENT = 3,
    OUTPUT_RETRY = 4,
    OUTPUT_FAULT = 5,
} output_state_t;

#ifdef __cplusplus
}
#endif

#endif
