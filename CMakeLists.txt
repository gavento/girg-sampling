cmake_minimum_required(VERSION 3.5)

#project(cpython_example)
# when installing directly in CMake, redirect its intall root to dist dir
#if (CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
#    set (CMAKE_INSTALL_PREFIX "${CMAKE_SOURCE_DIR}/dist" CACHE PATH "default install path" FORCE )
#endif()
#find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

add_subdirectory(girgs_cpplib)
