from conans import ConanFile, CMake


class MyhelloConan(ConanFile):
    name = "myPackage"
    version = "0.1"
    license = "None"
    author = "Olive 01ive@free.fr"
    url = "https://github.com/01ive/simpleConanCreationPackage.git"
    description = "This project propose a very simple example for c++ developer using Conan to create and use a package."
    topics = ("C++", "Conan", "Example", "Simple")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"
    exports_sources = "src/*"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libmyPackage.a"]
