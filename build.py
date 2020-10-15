# from cmaketools.cmakecommands import generate_cmdclass
# from cmaketools.cmakebuilder import CMakeBuilder
# import pybind11
import subprocess

# from distutils.command.build_ext import build_ext, Extension

"""
ext_modules = [
    Extension(
        "girg_sampling._cpplib_wrapper",
        include_dirs=[pybind11.get_include(), "dist/include/"],
        sources=["girg_sampling/_cpplib_wrapper.cpp"],
    ),
]
"""


def build():
    print("Running build.py ...")

    #    setup_kwargs["ext_module_hint"] = r"pybind11_add_module"
    #    setup_kwargs["src_dir"] = "girgs_cpplib"

    # cmake = CMakeBuilder(src_dir=".")
    # cmake.configure(build_dir="build/girgs_cpplib")
    # cmake.run("girg_sampling/_girgs_cpplib")

    # subprocess.check_call(["gcc", "-c", "girg_sampling/_cpplib_wrapper.cpp"])
    subprocess.check_call(["make", "build"])

    # setup_kwargs["packages"] = cmake.find_packages()
    # setup_kwargs["ext_modules"] = cmake.find_ext_modules()
    # setup_kwargs["data_files"] = cmake.get_setup_data_files()
    # setup_kwargs["cmdclass"] = {
    #    **generate_cmdclass(cmake),
    # }
    # setup_kwargs["ext_modules"] += ext_modules

    # return setup_kwargs


if __name__ == "__main__":
    build()
