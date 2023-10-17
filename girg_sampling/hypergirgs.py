import os
from typing import List, Tuple
import random

_prev_cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(__file__))
    from . import _libhypergirgs_wrapper
except ImportError as e:
    raise ImportError("Error importing hypergirgs CPP library wrapper.") from e
finally:
    os.chdir(_prev_cwd)


def calculateRadius(n: int, alpha: float, T: float, deg: float) -> float:
    return _libhypergirgs_wrapper.calculateRadius(n, alpha, T, deg)


def calculateRadiusLikeNetworKit(n: int, alpha: float, T: float, deg: float) -> float:
    return _libhypergirgs_wrapper.calculateRadiusLikeNetworKit(n, alpha, T, deg)


def sampleRadii(
    n: int, alpha: float, R: float, *, seed: int = None, parallel: bool = True
) -> List[float]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libhypergirgs_wrapper.sampleRadii(n, alpha, R, seed, parallel)


def sampleAngles(n: int, *, seed: int = None, parallel: bool = True) -> List[float]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libhypergirgs_wrapper.sampleAngles(n, seed, parallel)


def sampleRadiiAndAngles(
    n: int, alpha: float, R: float, *, seed: int = None, parallel: bool = True
) -> Tuple[List[float], List[float]]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libhypergirgs_wrapper.sampleRadiiAndAngles(n, alpha, R, seed, parallel)


def generateEdges(
    radii: List[float],
    angles: List[float],
    T: float,
    R: float,
    *,
    seed: int = None,
) -> List[Tuple[int, int]]:
    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)
    return _libhypergirgs_wrapper.generateEdges(radii, angles, T, R, seed)


def generate_networkx_hrg(
    n: int,
    alpha: float,
    T: float,
    deg: float,
    *,
    seed: int = None,
    parallel: bool = True,
):
    """
    Generates a Hyperbolic Random Graph as a NetworkX Graph.

    Parameters:
    * `n: int` - The number of vertices of the graph.
    * `alpha: float` - Generation parameter, 0.5 < `alpha` (see the paper).
    * `T: float` - Clustering temperature, 0.0 <= `T` <= 1.0 (lower `T` means more clustering; see the paper).
    * `deg: float` - Desired average degree.
    * `seed: int` - Optional integer seed for the random generation.
    * `parallel: bool` - Run multi-threaded (default: `True`).

    See the paper [Efficiently Generating Geometric Inhomogeneous and Hyperbolic Random Graphs](https://arxiv.org/abs/1905.06706) for details.
    """
    import networkx

    if seed is None:
        seed = random.randint(0, (1 << 31) - 1)

    r = calculateRadius(n, alpha, T, deg)
    radii, angles = sampleRadiiAndAngles(n, alpha, r, seed=seed + 0, parallel=parallel)
    e = generateEdges(radii, angles, T, r, seed=seed + 1)
    g = networkx.empty_graph(n)
    g.add_edges_from(e)
    return g


del _prev_cwd, os, List, Tuple, random
