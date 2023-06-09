"""
Tests that will be imported into other test_*.py files.

This lets us write test functions once that will run against different
cookiecutter templates.

A test_*.py file can use::

    from .common_tests import *

This will bring these tests into that file, where they will be executed by
pytest.  Each test will run once for each file it is imported into, and it will
run in the context of that file's fixtures.

"""

from .venv import all_files


def test_github_org_is_right(options_baked):
    """Make sure no one hard-coded openedx as the GitHub organization."""
    wrong_github = f"github.com/openedx/{options_baked['repo_name']}"
    for name in all_files():
        with open(name) as f:
            for line in f:
                assert wrong_github not in line
