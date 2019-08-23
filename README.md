# demo-python-package

[![Travis CI](https://img.shields.io/travis/astropenguin/demo-python-package/master.svg?label=Travis%20CI&style=flat-square)](https://travis-ci.org/astropenguin/demo-python-package)
[![Codecov](https://img.shields.io/codecov/c/github/astropenguin/demo-python-package?label=Codecov&style=flat-square)](https://img.shields.io/codecov/c/github/astropenguin/demo-python-package)
[![linting](https://img.shields.io/badge/Linting-Flake8-orange?style=flat-square)](http://flake8.pycqa.org/en/latest/)
[![Formatting](https://img.shields.io/badge/Formatting-Black-333?style=flat-square)](https://black.readthedocs.io/en/stable/)
[![Testing](https://img.shields.io/badge/Testing-pytest-yellow?style=flat-square)](https://black.readthedocs.io/en/stable/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](LICENSE)

:gift: A repository to demonstrate the development of a Python package

## Overview

This repository demonstrates a way to develop a well-formatted and well-tested Python package using CI/CD.
With a simple `demo` Python package, the following essential (but laborious) processes are automatically run by [Travis CI] in the cloud, which enables developers to keep focusing on the development of the package itself.

- code linting (by [Flake8])
- code formatting (by [Black])
- code testing (by [pytest])
- code coverage (by [Codecov])
- documentation building (by [Sphinx])
- documentation hosting (by [GitHub Pages])

## Local Python environment

This repository has Pipenv files (`Pipfile` and `Pipfile.lock`) which describe a specific Python version and dependent packages.
After cloning the repository to local, you can initialize a Python environment as follows:

```shell
$ git clone https://github.com/astropenguin/demo-python-package.git
$ cd demo-python-package
$ pipenv install --dev
```

Note that the following examples are assumed to be run in a virtual environment created by Pipenv.

```shell
$ pipenv shell # enter a virtual environment
(demo-python-package) $
```

## Code linting by flake8

```shell
$ flake8 demo
$ # nothing is output if no errors
```

## Code formatting by black

```shell
$ black --check demo
All done! ✨ 🍰 ✨
1 file would be left unchanged.
$
```

## Code testing by pytest

```shell
$ pip install -e .
$ pytest
========================= test session starts =========================
platform darwin -- Python 3.7.3, pytest-5.1.1, py-1.8.0, pluggy-0.12.0
rootdir: /path/to/demo-python-package
plugins: cov-2.7.1
collected 2 items

tests/test_version.py ..                                        [100%]

========================== 2 passed in 0.02s ==========================
$
```

## Code coverage by Codecov

```shell
$ pytest --cov demo
========================= test session starts =========================
platform darwin -- Python 3.7.3, pytest-5.1.1, py-1.8.0, pluggy-0.12.0
rootdir: /path/to/demo-python-package
plugins: cov-2.7.1
collected 2 items

tests/test_version.py ..                                        [100%]

---------- coverage: platform darwin, python 3.7.3-final-0 -----------
Name               Stmts   Miss  Cover
--------------------------------------
demo/__init__.py       3      0   100%

========================== 2 passed in 0.05s ==========================
$
```

## Documentation building by Sphinx

```shell
$ sphinx-apidoc -f -o docs/_apidoc demo
$ sphinx-build docs docs/_build
$ sphinx-build docs docs/_build
```

## Documentation hosting by GitHub Pages

## Useful tips

### VS Code settings

```json
{
    // auto formatting by Black
    "editor.formatOnType": true,
    "python.formatting.provider": "black",
    // auto linting by Flake8
    "python.linting.enabled": false,
    "python.linting.lintOnSave": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": false,
}
```

### Linting and formatting before commit

```yaml
repos:
  - repo: https://github.com/ambv/black
    rev: stable
    hooks:
      - id: black
        language_version: python3.7
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.7.8
    hooks:
      - id: flake8
```

```shell
$ pre-commit install
```

## References

- [Travis CI]
    - [Build Stages \- Travis CI](https://docs.travis-ci.com/user/build-stages)
    - [GitHub Pages Deployment \- Travis CI](https://docs.travis-ci.com/user/deployment/pages/)
- [Flake8]
    - [Using Version Control Hooks — flake8 3\.7\.8 documentation](http://flake8.pycqa.org/en/latest/user/using-hooks.html)
    - [black/\.flake8 at master · psf/black](https://github.com/psf/black/blob/master/.flake8)
- [Black]
    - [Version control integration — Black 19\.3b0 documentation](https://black.readthedocs.io/en/stable/version_control_integration.html)
    - [Editor integration — Black 19\.3b0 documentation](https://black.readthedocs.io/en/stable/editor_integration.html)
- [Sphinx]
    - [Getting Started — Sphinx 2\.3\.0 documentation](https://www.sphinx-doc.org/en/2.0/usage/quickstart.html)
    - [Support for NumPy and Google style docstrings — Sphinx 2\.3\.0 documentation](https://www.sphinx-doc.org/en/2.0/usage/extensions/napoleon.html)
- [Codecov]
    - [codecov/example\-python: Python coverage example](https://github.com/codecov/example-python)
- [pytest]
- [Pipenv]
- [pre-commit]
- [GitHub Pages]

[Travis CI]: https://travis-ci.org
[Flake8]: http://flake8.pycqa.org/en/latest
[Black]: https://black.readthedocs.io/en/stable
[pytest]: https://docs.pytest.org/en/latest
[Codecov]: https://codecov.io
[Sphinx]: http://www.sphinx-doc.org/en/master
[GitHub Pages]: https://pages.github.com
[Pipenv]: https://pipenv.readthedocs.io/en/latest
[pre-commit]: https://pre-commit.com/
