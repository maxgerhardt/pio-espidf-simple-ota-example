cmake_minimum_required(VERSION 3.16.0)
# This example uses an extra component for common functions such as Wi-Fi and Ethernet connection.
list(APPEND EXTRA_COMPONENT_DIRS $ENV{IDF_PATH}/examples/common_components/protocol_examples_common)
include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(espidf_ota_example)
