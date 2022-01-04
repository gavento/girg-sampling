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


del _prev_cwd, os, List, Tuple
