from conan import ConanFile

class MassCalculatorCoreConan(ConanFile):
    name = "masscalculator-core"
    version = "0.1.0"

    # Optional metadata
    license = "MIT"
    author = "Mergim Halimi m.halimi123@gmail.com"
    url = "https://github.com/MassCalculator/conan-masscalculator-core"
    description = "Core library for MassCalculator"
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
            
    def build(self):
      if self.settings.os == "Linux"  and self.settings.arch == "x86_64":

        url= self.conan_data["binaries"][self.version][str(self.settings.os)]["url"]
        sha256= self.conan_data["binaries"][self.version][str(self.settings.os)]["sha256"] 

      else:
        raise Exception("Binary does not exist for these settings")

    def package(self):
      self.copy("*")

    def package_info(self):
        self.cpp_info.libs = ["masscalculator-core"]
