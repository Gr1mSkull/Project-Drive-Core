#ifndef DRIVECORE_CRC16_H
#define DRIVECORE_CRC16_H

#include <stddef.h>
#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/** CRC-16/CCITT-FALSE (poly 0x1021, init 0xFFFF). */
uint16_t drivecore_crc16_ccitt(const uint8_t *data, size_t length);

#ifdef __cplusplus
}
#endif

#endif
