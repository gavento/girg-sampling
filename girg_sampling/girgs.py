import os
import random
from typing import List, Tuple

_prev_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(__file__))
    from . import _libgirgs_wrapper
except ImportError as e:
    raise ImportError("Error importing girgs CPP library wrapper.") from e
finally:
    os.chdir(_prev_cwd)


def generateWeights(
    n: int, ple: float, *, seed: int = None, parallel: bool = True
) -> List[float]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.generateWeights(n, ple, seed, parallel)


def generatePositions(
    n: int, dimension: int, *, seed: int = None, parallel: bool = True
) -> List[List[float]]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.generatePositions(n, dimension, seed, parallel)


def scaleWeights(
    weights: List[float], desiredAvgDegree: float, dimension: int, alpha: float
) -> float:
    return _libgirgs_wrapper.scaleWeights(weights, desiredAvgDegree, dimension, alpha)


def generateEdges(
    weights: List[float],
    positions: List[List[float]],
    alpha: float,
    *,
    seed: int = None,
) -> List[Tuple[int, int]]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.generateEdges(weights, positions, alpha, seed)


def generate_networkx_girg(
    n,
    ple: float,
    dim: int,
    deg: float,
    alpha: float,
    *,
    seed: int = None,
    parallel: bool = True,
):
    """
    Generates a GIRG as a NetworkX Graph.

    Parameters:
    * `n: int` - The number of vertices of the graph.
    * `ple: float` - The power law exponent to sample the new weights. Should be 2.0 to 3.0.
    * `dim: int` - Dimension of the geometry.
    * `deg: float` - The desired average degree.
    * `alpha: float` - Edge probability exponent parameter (see paper).
    * `seed: int` - Optional integer seed for the random generation.
    * `parallel: bool` - Run multi-threaded (default: `True`).

    An edge between node `u` and `v` is formed with probability $\left(\frac{w_u w_v / W}{|| x_u - x_v ||^{dim}}\right)^\alpha$
    or 1.0 if the term exceeds 1.0.

    See the paper [Efficiently Generating Geometric Inhomogeneous and Hyperbolic Random Graphs](https://arxiv.org/abs/1905.06706) for details.
    """
    import networkx

    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)

    w = generateWeights(n, ple, seed=seed + 0, parallel=parallel)
    p = generatePositions(n, dim, seed=seed + 1, parallel=parallel)
    ws = scaleWeights(w, deg, dim, alpha)
    w = [x * ws for x in w]
    e = generateEdges(w, p, alpha, seed=seed + 2)
    g = networkx.empty_graph(n)
    g.add_edges_from(e)
    return g


del _prev_cwd, os, List, Tuple
