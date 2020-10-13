LIB_BUILD_DIR=girgs_cpplib/build
LIB_TARGET_DIR=girgs_cpplib/install
LIB_GIRGS=girg_sampling/libgirgs.so
LIB_WRAP=girg_sampling/_cpplib_wrapper.so

PYBIND11_INCLUDE=$(shell poetry run python -c "import pybind11; print(pybind11.get_include())")
PYTHON_INCLUDE=$(shell poetry run python -c "from sysconfig import get_paths; print(get_paths()['include'])")

.PHONY: all clean build

all: build

clean:
	rm -rf dist/ build/ $(LIB_BUILD_DIR) $(LIB_TARGET_DIR) girg_sampling/*.so
	rm -rf girg_sampling.egg-info/ __pycache__/

$(LIB_GIRGS):
	cmake girgs_cpplib -B $(LIB_BUILD_DIR)
	cmake --build $(LIB_BUILD_DIR)
	cmake --install $(LIB_BUILD_DIR) --prefix $(LIB_TARGET_DIR)
	cp $(LIB_TARGET_DIR)/lib/*.so girg_sampling/

$(LIB_WRAP): girg_sampling/_cpplib_wrapper.cpp $(LIB_GIRGS)
	$(CC) -fPIC -Wall -shared -g -o $@ $< -lstdc++ \
		-I$(PYBIND11_INCLUDE) -I$(LIB_TARGET_DIR)/include/ -I$(PYTHON_INCLUDE)

build: $(LIB_WRAP)
#	poetry build

test:
	poetry install
	poetry run pytest .
