from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.scm import Git

class MassCalculatorCoreConan(ConanFile):
    name = "masscalculator-core"
    version = "0.2.0"

    license = "MIT"
    author = "Mergim Halimi m.halimi123@gmail.com"
    url = "https://github.com/MassCalculator/conan-masscalculator-core"
    description = "Core library for MassCalculator"
    topics = ("conan", "mass", "engineering", "physics")

    requires = "gtest/1.13.0", "lua/5.4.4"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def config_options(self):
        if self.settings.os == "Windows":
            self.options.remove("fPIC")

    def configure(self):
        if self.options.shared:
            self.options.remove("fPIC")

    def source(self):
        git = Git(self)
        git.clone(url="https://github.com/MassCalculator/masscalculator-core.git", target=".")
        git.checkout("v0.2.0")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_property(
            "cmake_target_name", "masscalculator::masscalculator-core")

        self.cpp_info.libs = ["masscalculator-base", "masscalculator-core"]
