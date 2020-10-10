from cmaketools.cmakebuilder import CMakeBuilder
from cmaketools.cmakecommands import generate_cmdclass


def build(setup_kwargs):
    cmake = CMakeBuilder()
    setup_kwargs["packages"] = cmake.find_packages()
    setup_kwargs["ext_modules"] = cmake.find_ext_modules()
    setup_kwargs["data_files"] = cmake.get_setup_data_files()
    setup_kwargs["cmdclass"] = {
        **generate_cmdclass(cmake),
    }
