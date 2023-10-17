# GIRG sampling

A Python wrapper for the [GIRGs sampling library](https://github.com/chistopher/girgs) (C++).
Contains a direct wraper of the C++ library and NetworkX Graph generators (optional).
Efficiently generates Geometric Inhomogeneous Random Graphs (GIRGs) and Hyperbolic Random Graphs (HRGs).

See the paper [Efficiently Generating Geometric Inhomogeneous and Hyperbolic Random Graphs](https://arxiv.org/abs/1905.06706)
for details of the algorithm.

## Install

Install from PyPI as `girg-sampling` via `pip`, `poetry` etc.
To build the package locally, install Poetry package manager and run `poetry build`, optionally with `poetry install`.

To use `generateNetworkX` functions, you need to have the `networkx` package (not a default dependency of `girg-sampling`)

## Usage

```python
import girg_sampling

g = girg_sampling.girgs.generateNetworkX(n=135, ple=1.5, dim=4, deg=4.2, alpha=100, seed=41)
h = girg_sampling.hypergirgs.generateNetworkX(n=1001, alpha=0.75, T=0.7, deg=2.2, seed=None)
```

See [tests](https://github.com/gavento/girg-sampling/blob/master/tests/test_basic.py) for sample usage of the raw C++ wrappers.

## Changelog

* 0.1.0: A direct wrapper of the C++ graph generator functions.
* 0.2.0: Minor fixes, unify `seed` param, add e2e tests, build wheels for python up to 3.10
* 0.2.1: Update urllib3 dev-dependency for twine under Python 3.10
* 0.3.0: Add NetworkX wrapper, update python version, add docs.
