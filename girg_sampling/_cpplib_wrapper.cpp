#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <girgs/Generator.h>

using namespace std;
using namespace girgs;

PYBIND11_MODULE(_cpplib_wrapper, m)
{
    m.doc() = "C++ wrapper of libgirgs";

    m.def("generateWeights", &generateWeights, "");
    m.def("generatePositions", &generatePositions, "");
    m.def("scaleWeights", &scaleWeights, "");
    m.def("generateEdges", &generateEdges, "");
    m.def("saveDot", &saveDot, "");
}