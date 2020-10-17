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
    n: int, ple: float, weightSeed: int = None, parallel: bool = True
) -> List[float]:
    if weightSeed is None:
        weightSeed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.generateWeights(n, ple, weightSeed, parallel)


def generatePositions(
    n: int, dimension: int, positionSeed: int = None, parallel: bool = True
) -> List[List[float]]:
    if positionSeed is None:
        positionSeed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.generatePositions(n, dimension, positionSeed, parallel)


def scaleWeights(
    weights: List[float], desiredAvgDegree: float, dimension: int, alpha: float
) -> float:
    return _libgirgs_wrapper.scaleWeights(weights, desiredAvgDegree, dimension, alpha)


def generateEdges(
    weights: List[float],
    positions: List[List[float]],
    alpha: float,
    samplingSeed: int = None,
) -> List[Tuple[int, int]]:
    if samplingSeed is None:
        samplingSeed = random.randint(0, (1 << 31) - 1)
    return _libgirgs_wrapper.G_generateEdges(weights, positions, alpha, samplingSeed)


del _prev_cwd, os, List, Tuple
