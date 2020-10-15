#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <girgs/Generator.h>
#include <hypergirgs/Generator.h>

using namespace std;

PYBIND11_MODULE(_cpplib_wrapper, m)
{
    m.doc() = "C++ wrapper of libgirgs and libhypergirgs";

    m.def("generateWeights", &girgs::generateWeights,
        "PyBind11-wrapped libgirgs function");
    m.def("generatePositions", &girgs::generatePositions,
        "PyBind11-wrapped libgirgs function");
    m.def("scaleWeights", &girgs::scaleWeights,
        "PyBind11-wrapped libgirgs function");
    m.def("generateEdges", &girgs::generateEdges,
        "PyBind11-wrapped libgirgs function");
    m.def("saveDot", &girgs::saveDot,
        "PyBind11-wrapped libgirgs function");

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
