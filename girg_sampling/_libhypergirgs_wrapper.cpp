#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <hypergirgs/Generator.h>

using namespace std;

PYBIND11_MODULE(_libhypergirgs_wrapper, m)
{
    m.doc() = "C++ wrapper of libgirgs and libhypergirgs";

    m.def("calculateRadius", &hypergirgs::calculateRadius,
          "PyBind11-wrapped libhypergirgs function");
    m.def("calculateRadiusLikeNetworKit", &hypergirgs::calculateRadiusLikeNetworKit,
          "PyBind11-wrapped libhypergirgs function ");
    m.def("sampleRadii", &hypergirgs::sampleRadii,
          "PyBind11-wrapped libhypergirgs function");
    m.def("sampleAngles", &hypergirgs::sampleAngles,
          "PyBind11-wrapped libhypergirgs function");
    m.def("sampleRadiiAndAngles", &hypergirgs::sampleRadiiAndAngles,
          "PyBind11-wrapped libhypergirgs function");
    m.def("generateEdges", &hypergirgs::generateEdges,
          "PyBind11-wrapped libhypergirgs function");
}
