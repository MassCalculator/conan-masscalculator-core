cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(masscalculator-core CONFIG REQUIRED)

add_executable(${PROJECT_NAME}  
  src/example.cpp
)

target_link_libraries(${PROJECT_NAME} 
PRIVATE
  masscalculator::masscalculator-base
  masscalculator::masscalculator-core
  masscalculator::third_party::units
)

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 11)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)
