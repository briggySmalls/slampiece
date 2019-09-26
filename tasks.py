"""
Invoke tasks for the project
"""

from pathlib import Path

from invoke import task

_ROOT_DIR = Path(__file__).parent
_PACKAGE_DIR = _ROOT_DIR.joinpath('src')
_TESTS_DIR = _PACKAGE_DIR.joinpath('tests')
_NOTEBOOK_DIR = _ROOT_DIR.joinpath('notebooks')

_LINT_DIRS = [str(d) for d in [_PACKAGE_DIR, Path(__file__)]]

# pylint: disable=invalid-name


@task
def lint(c):
    """
    Lints source and tests
    """
    c.run("flake8 {}".format(' '.join(_LINT_DIRS)))
    c.run("pylint {}".format(' '.join(_LINT_DIRS)))


@task
def test(c):
    """
    Runs tests on source
    """
    # Test source
    c.run("pytest {} -v".format(str(_TESTS_DIR)))


@task
def format(c, check_only=False):  # pylint: disable=redefined-builtin
    """
    Formats source and tests
    """

    # Create space-separated list of lint directories
    lint_dir_string = ' '.join(_LINT_DIRS)
    # Format source
    c.run("yapf --recursive {} {}".format(
        '--diff' if check_only else '--in-place', lint_dir_string))

    # Check imports (don't exit on failure, we want to format)
    c.run("isort --recursive {} {}".format(
        '--check-only' if check_only else '', lint_dir_string))


@task()
def clean(c):
    """
    Clean notebook output
    """
    notebooks = [f"'{n}'" for n in _NOTEBOOK_DIR.glob('*.ipynb')]
    c.run(("jupyter nbconvert"
           " --ClearOutputPreprocessor.enabled=True"
           " --inplace {}").format(" ".join(notebooks)))


@task()
def notebook(c):
    """
    Start notebook server
    """
    c.run(f"jupyter notebook --notebook-dir {_NOTEBOOK_DIR}")
