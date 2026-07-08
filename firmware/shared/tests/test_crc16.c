#include <assert.h>
#include <stdint.h>
#include <string.h>

#include "drivecore/crc16.h"

int main(void)
{
    const uint8_t empty[] = "";
    assert(drivecore_crc16_ccitt(empty, 0) == 0xFFFFU);

    const uint8_t abc[] = "123456789";
    assert(drivecore_crc16_ccitt(abc, sizeof(abc) - 1U) == 0x29B1U);

    return 0;
}
