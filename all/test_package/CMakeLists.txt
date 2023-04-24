cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(masscalculator-core CONFIG REQUIRED)

add_executable(${PROJECT_NAME}
  src/example.cpp
)

target_link_libraries(${PROJECT_NAME} 
  PRIVATE
    masscalculator-base
    masscalculator-core
)

set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 17)
