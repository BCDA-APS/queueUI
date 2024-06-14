# QSUI

## Table of Contents
- [QSUI](#QSUI)
  - [Table of Contents](#table-of-contents)
  - [Usage](#usage)
  - [Installation](#installation)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)
  - [License](#license)


## Installation
On a terminal:
```bash
git clone git@github.com:BCDA-APS/qsui.git
cd qsui
conda env create --force -n qsui -f ./env.yml
conda activate qsui
pip install -e .
```
## Usage
On a terminal:
```bash
conda activate qsui
qsui &
```

### Using Pre-commit

- To run pre-commit checks before committing, run `pre-commit run --all-files`
- NONE OF THE FOLLOWING SHOULD BE DONE REGULARLY, AND ALL CHECKS SHOULD BE PASSING BEFORE BRANCHES ARE MERGED
    - To skip linting during commits, use `SKIP=ruff git commit ...`
    - To skip formatting during commits, use `SKIP=ruff-format git commit ...`
    - To skip all pre-commit hooks, use `git commit --no-verify ...`
- See [pre-commit documentation](https://pre-commit.com) for more

## Contributing

Please report **bugs**, **enhancement requests**, or **questions** through the [Issue Tracker](https://github.com/bcda-APS/qsui).

If you are looking to contribute, please see [`CONTRIBUTING.md`](https://github.com/bcda-APS/qsui/blob/main/CONTRIBUTING.md).


## Citing

```bibtex
```

## License

QSUI is MIT licensed, as seen in the [LICENSE](./LICENSE) file.
