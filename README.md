# GIRG sampling

A Python wrapper for the [GIRGs sampling library](https://github.com/chistopher/girgs) (C++).

Currently just a direct wraper of the C++ library. See [tests](https://github.com/gavento/girg-sampling/blob/master/tests/test_basic.py) for sample usage.

Install from the wheels to get te compied version of the library.
To build locally, install Poetry package manager and run `poetry install`.

## Changelog

* 0.1.0: A direct wrapper of the C++ graph generator functions.
* 0.2.0: Minor fixes, unify `seed` param, add e2e tests, build wheels for python up to 3.10
* 0.2.1: Update urllib3 dev-dependency for twine under Python 3.10
