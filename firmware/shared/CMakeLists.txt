cmake_minimum_required(VERSION 3.16)
project(drivecore_shared C)

add_library(drivecore_shared STATIC
    src/crc16.c
)

target_include_directories(drivecore_shared PUBLIC include)

target_compile_options(drivecore_shared PRIVATE -Wall -Wextra)

enable_testing()
add_executable(test_crc16 tests/test_crc16.c)
target_link_libraries(test_crc16 drivecore_shared)
add_test(NAME crc16 COMMAND test_crc16)
