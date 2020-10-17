LIB_BUILD_DIR=girgs_cpplib/build
LIB_TARGET_DIR=girgs_cpplib/install
LIB_GIRGS=girg_sampling/libgirgs.so.1
LIB_HYPERGIRGS=girg_sampling/libhypergirgs.so.1
LIB_GIRGS_WRAP=girg_sampling/_libgirgs_wrapper.so
LIB_HYPERGIRGS_WRAP=girg_sampling/_libhypergirgs_wrapper.so

PYBIND11_INCLUDE=$(shell poetry run python -c "import pybind11; print(pybind11.get_include())")
PYTHON_INCLUDE=$(shell poetry run python -c "from sysconfig import get_paths; print(get_paths()['include'])")

.PHONY: all clean build submodules test

all: build

clean:
	rm -rf dist/ build/ $(LIB_BUILD_DIR) $(LIB_TARGET_DIR)
	rm -rf girg_sampling/*.so girg_sampling/*.so.*
	rm -rf girg_sampling.egg-info/ __pycache__/

$(LIB_GIRGS) $(LIB_HYPERGIRGS): submodules
	cmake girgs_cpplib -B $(LIB_BUILD_DIR)
	cmake --build $(LIB_BUILD_DIR)
	cmake --install $(LIB_BUILD_DIR) --prefix $(LIB_TARGET_DIR)
	# NOTE: renaming to prevent conflicts with other installs of lib(hyper)girgs
	cp -L $(LIB_TARGET_DIR)/lib/libgirgs.so $(LIB_GIRGS)
	cp -L $(LIB_TARGET_DIR)/lib/libhypergirgs.so $(LIB_HYPERGIRGS)

$(LIB_GIRGS_WRAP): girg_sampling/_libgirgs_wrapper.cpp $(LIB_GIRGS)
	$(CC) -fPIC -Wall -shared -g -o $@ $< \
		-I$(PYBIND11_INCLUDE) -I$(LIB_TARGET_DIR)/include/ -I$(PYTHON_INCLUDE) \
		-lstdc++ $(LIB_GIRGS) -Wl,-rpath=.

$(LIB_HYPERGIRGS_WRAP): girg_sampling/_libhypergirgs_wrapper.cpp $(LIB_HYPERGIRGS)
	$(CC) -fPIC -Wall -shared -g -o $@ $< \
		-I$(PYBIND11_INCLUDE) -I$(LIB_TARGET_DIR)/include/ -I$(PYTHON_INCLUDE) \
		-lstdc++ $(LIB_HYPERGIRGS) -Wl,-rpath=.

build: submodules $(LIB_GIRGS_WRAP) $(LIB_HYPERGIRGS_WRAP)

submodules:
	git submodule init
	git submodule update

test:
	poetry install
	poetry run pytest .
