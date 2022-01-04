import os
from typing import List, Tuple
import random

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


del _prev_cwd, os, List, Tuple
