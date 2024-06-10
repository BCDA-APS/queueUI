# QSUI

<!-- TODO: Add badges -->
<!-- [![PyPI version](https://badge.fury.io/py/mdlearn.svg)](https://badge.fury.io/py/mdlearn) -->
<!-- [![Documentation Status](https://readthedocs.org/projects/mdlearn/badge/?version=latest)](https://mdlearn.readthedocs.io/en/latest/?badge=latest) -->

For more details and specific examples of how to use QSUI, please see our [documentation](???).

## Table of Contents
- [QSUI](#QSUI)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Development](#development)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)

## Usage

To get started with QSUI, we recommend:

- Consulting the [Documentation](??)

## Installation


## Development



### Using PDM

- [Managing Dependencies](https://pdm-project.org/latest/usage/dependency/)
- [Build and Publish](https://pdm-project.org/latest/usage/publish/)
- [Running Using PDM](https://pdm-project.org/latest/usage/scripts/)

### Using Pre-commit

- To run pre-commit checks before committing, run `pre-commit run --all-files`
- NONE OF THE FOLLOWING SHOULD BE DONE REGULARLY, AND ALL CHECKS SHOULD BE PASSING BEFORE BRANCHES ARE MERGED
    - To skip linting during commits, use `SKIP=ruff git commit ...`
    - To skip formatting during commits, use `SKIP=ruff-format git commit ...`
    - To skip all pre-commit hooks, use `git commit --no-verify ...`
- See [pre-commit documentation](https://pre-commit.com) for more

### Building Documentation

- You can install the documentation python dependencies with `pip install -e '.[docs]'` or `pdm install -G docs`
- You must install [Graphviz](https://graphviz.org/download/)
- You can build the docs with `make docs`

## Contributing

Please report **bugs**, **enhancement requests**, or **questions** through the [Issue Tracker](https://github.com/ravescovi/qsui).

If you are looking to contribute, please see [`CONTRIBUTING.md`](https://github.com/ravescovi/qsuo/blob/main/CONTRIBUTING.md).


## Citing

```bibtex
```

## License

QSUI is MIT licensed, as seen in the [LICENSE](./LICENSE) file.
