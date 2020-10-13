import os
from typing import List
import random


_prev_cwd = os.getcwd()
try:
    os.chdir(__path__[0])
    import _cpplib_wrapper
except ImportError as e:
    raise ImportError("Error importing girgs CPP library wrapper.") from e
finally:
    os.chdir(_prev_cwd)
del _prev_cwd, os


def generateWeights(
    n: int, ple: float, weightSeed: int = None, parallel: bool = True
) -> List[float]:
    """
    Sample weights according to a power law distribution between [1, n)

    n: The size of the graph. Should match with size of positions.
    ple: The power law exponent to sample the new weights. Should be 2.0 to 3.0.
    weightSeed: A seed for weight sampling. Should not be equal to the position seed.
    By default, uses a random seed.

    Returns the weights according to the desired distribution.
    """
    if weightSeed is None:
        weightSeed = random.randint(0, (1 << 31) - 1)
    return _cpplib_wrapper.generateWeights(n, ple, weightSeed, parallel)


def generatePositions(
    n: int, dimension: int, positionSeed: int = None, parallel: bool = True
) -> List[List[float]]:
    if positionSeed is None:
        positionSeed = random.randint(0, (1 << 31) - 1)
    return _cpplib_wrapper.generatePositions(n, dimension, positionSeed, parallel)


def scaleWeights(
    weights: List[float], desiredAvgDegree: float, dimension: int, alpha: float
) -> float:
    return _cpplib_wrapper.scaleWeights(weights, desiredAvgDegree, dimension, alpha)


def generateEdges(
    weights: List[float],
    positions: List[List[float]],
    alpha: float,
    samplingSeed: int = None,
) -> List[(int, int)]:
    if samplingSeed is None:
        samplingSeed = random.randint(0, (1 << 31) - 1)
    return _cpplib_wrapper.generateEdges(weights, positions, alpha, samplingSeed)
