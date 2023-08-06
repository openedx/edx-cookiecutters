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
    "author_email": "cookie@monster.org",
    "author_name": "Cookie Monster",
    "library_name": "cookie_lover",
    "github_org": "openedx",
    "repo_name": "cookie_repo",
}

configurations = [
    pytest.param(
        {
            **common,
        },
    )
]


@pytest.fixture(name="configuration", params=configurations, scope="module")
def fixture_configuration(request):
    return request.param


@pytest.fixture(name="custom_template_name", scope="module")
def fixture_custom_template_name():
    return "cookiecutter-python-library"


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
        assert license_name in Path("setup.py").read_text()


def test_readme(options_baked, custom_template):
    """The generated README.rst file should pass some sanity checks and validate as a PyPI long description."""
    readme_lines = [rl.strip() for rl in Path('README.rst').read_text().splitlines()]
    assert "cookie_repo" == readme_lines[0]
    assert ':target: https://pypi.python.org/pypi/cookie_repo/' in readme_lines
    sh.python("-m", "build", "--wheel")
    sh.twine("check", "dist/*")


def test_github_actions_ci(options_baked):
    """The generated ci.yml file should pass a sanity check."""
    ci_text = Path(".github/workflows/ci.yml").read_text()
    assert 'pip install -r requirements/ci.txt' in ci_text


def test_manifest(options_baked):
    """The generated MANIFEST.in should pass a sanity check."""
    manifest_text = Path("MANIFEST.in").read_text()
    assert 'recursive-include cookie_lover *.html' in manifest_text


def test_setup_py(options_baked):
    """The generated setup.py should pass a sanity check."""
    setup_text = Path("setup.py").read_text()
    assert "VERSION = get_version('cookie_lover', '__init__.py')" in setup_text
    assert "    author='Cookie Monster'," in setup_text
    assert "    author_email='cookie@monster.org'," in setup_text


def test_tests_and_quality(options_baked):
    """
    Run generated tests and quality checks.
    """
    run_in_virtualenv('make requirements test-all')
