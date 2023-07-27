"""
Tests of the project generation output.
"""

import logging
import logging.config
from pathlib import Path

import pytest
import sh

from .bake import bake_in_temp_dir
from .common_tests import *  # pylint: disable=wildcard-import
from .venv import all_files, run_in_virtualenv

LOGGING_CONFIG = {
    'version': 1,
    'incremental': True,
    'loggers': {
        'binaryornot': {
            'level': logging.INFO,
        },
        'sh': {
            'level': logging.INFO,
        }
    }
}
logging.config.dictConfig(LOGGING_CONFIG)


common = {
    "app_name": "cookie_lover",
    "github_org": "bakery_org",
    "repo_name": "cookie_repo",
    "matrix": {}
}

configurations = [
    pytest.param(
        {
            **common,
        },
    )
]


@pytest.fixture(name='custom_template', scope="module")
def fixture_custom_template(cookies_session):
    template = cookies_session._default_template + "/cookiecutter-django-ida"  # pylint: disable=protected-access
    return template


@pytest.fixture(params=configurations, name='options_baked', scope="module")
def fixture_options_baked(cookies_session, request, custom_template):
    """
    Bake a cookie cutter, parameterized by configurations.

    Provides the configuration dict, and changes into the directory with the
    baked result.
    """
    with bake_in_temp_dir(cookies_session, extra_context=request.param, template=custom_template):
        yield request.param


# Fixture names aren't always used in test functions. Disable completely.
# pylint: disable=unused-argument

@pytest.mark.parametrize("license_name, target_string", [
    ('AGPL 3.0', 'GNU AFFERO GENERAL PUBLIC LICENSE'),
    ('Apache Software License 2.0', 'Apache'),
])
def test_bake_selecting_license(cookies, license_name, target_string, custom_template):
    """Test to check if LICENSE.txt gets the correct license selected."""
    with bake_in_temp_dir(cookies, extra_context={'open_source_license': license_name}, template=custom_template):
        assert target_string in Path("LICENSE.txt").read_text()


def test_readme(options_baked, custom_template):
    """The generated README.rst file should pass some sanity checks and validate as a PyPI long description."""
    readme_lines = [rl.strip() for rl in Path('README.rst').read_text().splitlines()]
    assert "cookie_repo" == readme_lines[0]
    assert ':target: https://pypi.python.org/pypi/cookie_repo/' in readme_lines


def test_github_actions_ci(options_baked):
    """The generated ci.yml file should pass a sanity check."""
    ci_text = Path(".github/workflows/ci.yml").read_text()
    assert 'pip install -r requirements/ci.txt' in ci_text


def test_upgrade(options_baked):
    """Make sure the upgrade target works"""
    run_in_virtualenv('make upgrade')


def test_quality(options_baked):
    """Run quality tests on the given generated output."""
    for name in all_files():
        if name.endswith('.py'):
            sh.pylint(name)
            sh.pycodestyle(name)
            # sh.pydocstyle(name)  Not running for now because there are too many violations.
            sh.isort(name, check_only=True, diff=True)
    sh.make('upgrade')
    sh.pip('install', '-r', 'requirements/test.txt')


    # Sanity check the generated Makefile
    sh.make('help')
    # quality check docs
    sh.doc8("README.rst", ignore_path="docs/_build")
    sh.doc8("docs", ignore_path="docs/_build")
