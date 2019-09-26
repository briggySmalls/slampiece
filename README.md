# Slampiece

Quick-and-dirty python code for identifying similar strings between two lists, using the [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance).

## Installation

Dependencies are managed using pipenv, so make sure this is installed:

```bash
pip install pipenv
```

Then you can get up-and-running with:
```bash
# Only install bare-minimum
pipenv install

# Install dev dependendencies to play with notebooks and/or develop the code
pipenv install --dev
```

## Notebooks

The repo comes with a notebook that runs the software on an input CSV.

You will need to have installed the dev. dependencies (as described above) to use it.

To have a look, run:

```bash
pipenv run invoke notebook
```

## Development

You can check out the development tools that have come preinstalled with:

```bash
pipenv run invoke --list
```

For example, you can run the unit tests with:
```bash
pipenv run invoke test
```
