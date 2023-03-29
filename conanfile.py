import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps
from conan.tools.scm.git import Git


class libmasscalculator_coreRecipe(ConanFile):
    name = "libmasscalculator-core"
    version = "1.0.0"

    # Optional metadata
    license = "MIT"
    author = "Mergim Halimi m.halimi123@gmail.com"
    url = "https://github.com/MassCalculator/conan-masscalculator-core"
    description = "Core library for mass calculator"
    topics = ("conan", "mass", "engineering")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*", "include/*"
    requires = "gtest/1.8.1"

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.rm_safe("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def source(self):
        git = Git(self)
        git.clone(
            "git@github.com:MassCalculator/libmasscalculator.git")
            
    def build(self):
        cmake = CMake(self)
        cmake.configure(build_script_folder="libmasscalculator")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["libmasscalculator-core"]
