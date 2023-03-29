# Set the minimum version of cmake required to build this project
cmake_minimum_required(VERSION 3.15)
project(masscalculator-core CXX)

# Add library for masscalculator-core
add_library(masscalculator-core src/masscalculator-core.cpp)

# Set include directory for masscalculator-core
target_include_directories(masscalculator-core PUBLIC include)

# Set public header for masscalculator-core
set_target_properties(masscalculator-core PROPERTIES PUBLIC_HEADER "include/masscalculator-core.h")

# Install target for masscalculator-core
install(TARGETS masscalculator-core)

# Set the minimum version of cmake required to build this project
cmake_minimum_required(VERSION 2.8.11)
project(cmake_wrapper)

# Include conanbuildinfo.cmake
include(conanbuildinfo.cmake)

# Setup conan
conan_basic_setup()

# Check for include file
include(CheckIncludeFile)

# Add source subfolder
add_subdirectory("source_subfolder")