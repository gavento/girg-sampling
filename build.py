from cmaketools.cmakebuilder import CMakeBuilder
#from cmaketools.cmakecommands import generate_cmdclass
#from cmaketools import setup


def build():
    print("Heelo world!")
    cmake = CMakeBuilder()
    cmake.configure(build_dir="build/girgs_cpplib")
    cmake.run("girg_sampling/_girgs_cpplib")

#    setup_kwargs["packages"] = cmake.find_packages()
#    setup_kwargs["ext_modules"] = cmake.find_ext_modules()
#    setup_kwargs["data_files"] = cmake.get_setup_data_files()
#    setup_kwargs["cmdclass"] = {
#        **generate_cmdclass(cmake),
#    }


if __name__ == "__main__":
    build()
