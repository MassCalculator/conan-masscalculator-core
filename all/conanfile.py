import os
from conan import ConanFile
from conan.tools.files import get, copy

class MassCalculatorCoreConan(ConanFile):
    name = "masscalculator-core"
    version = "0.1.0"

    license = "MIT"
    author = "Mergim Halimi m.halimi123@gmail.com"
    url = "https://github.com/MassCalculator/conan-masscalculator-core"
    description = "Core library for MassCalculator"
    topics = ("conan", "mass", "engineering")

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

    def build(self):
      if self.settings.os == "Linux"  and self.settings.arch == "x86_64":

        url = self.conan_data["binaries"][self.version][str(self.settings.os)]["url"]
        sha256 = self.conan_data["binaries"][self.version][str(self.settings.os)]["sha256"]
        get(self, url)

      else:
        raise Exception("Binary does not exist for these settings")

    def package(self):
        src_path = os.path.join("include", "masscalculator")
        print("Copying headers from {} to {}".format(os.path.abspath(src_path), os.path.join(self.package_folder, "include", "masscalculator")))
        copy(self, "*.h", src=src_path, dst=os.path.join(self.package_folder, "include", "masscalculator"), keep_path=True)
        copy(self, "*.hpp", src=src_path, dst=os.path.join(self.package_folder, "include", "masscalculator"), keep_path=True)
        print("Copying shared libraries from {} to {}".format(os.path.abspath(os.path.join("linux-x86_64")), os.path.join(self.package_folder, "lib")))
        copy(self, "*.so", src=os.path.join("linux-x86_64"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        print("Copying static libraries from {} to {}".format(os.path.abspath(os.path.join("linux-x86_64")), os.path.join(self.package_folder, "lib")))
        copy(self, "*.a", src=os.path.join("linux-x86_64"), dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        print("Copying cmake files from {} to {}".format(os.path.abspath(os.path.join("cmake")), os.path.join(self.package_folder, "cmake")))
        copy(self, "*.cmake", src=os.path.join("cmake"), dst=os.path.join(self.package_folder, "cmake"), keep_path=True)


    def package_info(self):
        # Configure CMake imported targets
        self.cpp_info.set_property("cmake_file_name", "masscalculator-core")
        self.cpp_info.set_property("cmake_find_package", "masscalculator-core")
        self.cpp_info.set_property("cmake_find_package_file", ["masscalculator-core-config.cmake", "masscalculator-core-config-release.cmake"])
        self.cpp_info.set_property("cmake_find_package_multi", "masscalculator-core")
        self.cpp_info.set_property("cmake_target_name", "masscalculator-core")

        # Set library names
        self.cpp_info.libs = ["masscalculator-base", "masscalculator-core"]
