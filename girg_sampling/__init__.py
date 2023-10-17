"""
A Python wrapper for the GIRGs sampling library (https://github.com/chistopher/girgs).
Contains a direct wraper of the C++ library and NetworkX Graph generators (optional).

See the paper "Efficiently Generating Geometric Inhomogeneous and Hyperbolic
Random Graphs" (https://arxiv.org/abs/1905.06706) for details of the algorithm.

Use `generate_networkx_girg` and `generate_networkx_hrg` to generate NetworkX
graphs directly, or use the low-level C++ library wrappers in `girgs` and
`hypergirgs` submodules.
"""

from . import girgs, hypergirgs

from .girgs import generate_networkx_girg
from .hypergirgs import generate_networkx_hrg
