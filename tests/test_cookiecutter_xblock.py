"""
Tests of the project generation output.
"""

import logging
import logging.config
import os
import re
from contextlib import contextmanager
from pathlib import Path

import pytest
import sh

from .bake import bake_in_temp_dir
from .venv import run_in_virtualenv

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
    "library_name": "cookie_lover",
    "repo_name": "cookie_repo",
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
    template = cookies_session._default_template + "/cookiecutter-xblock"  # pylint: disable=protected-access
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
        assert license_name in Path("setup.py").read_text()


def test_readme(options_baked, custom_template):
    """The generated README.rst file should pass some sanity checks and validate as a PyPI long description."""
    readme_file = Path('README.rst')
    readme_lines = [x.strip() for x in readme_file.open()]
    assert "My First XBlock" == readme_lines[0]
    assert 'Testing with Docker' in readme_lines
    try:
        os.system("python -m build --wheel")
        os.system("twine check dist/*")
    except os.ErrorReturnCode as exc:
        pytest.fail(str(exc))


def test_manifest(options_baked):
    """The generated MANIFEST.in should pass a sanity check."""
    manifest_text = Path("MANIFEST.in").read_text()
    assert 'recursive-include myxblock *.html' in manifest_text


def test_setup_py(options_baked):
    """The generated setup.py should pass a sanity check."""
    setup_text = Path("setup.py").read_text()
    assert "VERSION = get_version('myxblock', '__init__.py')" in setup_text
    assert "    author='edX'," in setup_text


def test_upgrade(options_baked):
    """Make sure the upgrade target works"""
    try:
        run_in_virtualenv('make upgrade')
    except sh.ErrorReturnCode as exc:
        pytest.fail(str(exc.stderr))


def test_quality(options_baked):
    """Run quality tests on the given generated output."""
    sh.make('upgrade')
    sh.pip('install', '-r', 'requirements/base.txt')
    for dirpath, _dirnames, filenames in os.walk("."):
        for filename in filenames:
            name = os.path.join(dirpath, filename)
            if not name.endswith('.py'):
                continue
            try:
                sh.pylint(name)
                sh.pycodestyle(name)
                # sh.pydocstyle(name)  Not running for now because there are too many violations.
                sh.isort(name, check_only=True, diff=True)
            except sh.ErrorReturnCode as exc:
                pytest.fail(str(exc))

    try:
        # Sanity check the generated Makefile
        sh.make('help')
        # quality check docs
        sh.doc8("README.rst", ignore_path="docs/_build")
        sh.doc8("docs", ignore_path="docs/_build")
    except sh.ErrorReturnCode as exc:
        pytest.fail(str(exc))
