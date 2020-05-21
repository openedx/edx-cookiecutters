"""
Tests of the project generation output.
"""

import logging
import logging.config
import os
from contextlib import contextmanager
from pathlib import Path

import pytest
import sh

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


@contextmanager
def inside_dir(dirpath):
    """
    Change into a directory and change back at the end of the with-statement.

    Args:
        dirpath (str): the path of the directory to change into.

    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """
    Bake a cookiecutter, and switch into the resulting directory.

    Args:
        cookies (pytest_cookies.Cookies): the cookie to be baked.

    """
    result = cookies.bake(*args, **kwargs)
    if result.exception:
        raise result.exception
    with inside_dir(str(result.project)):
        yield


common = {
    "app_name": "cookie_lover",
    "repo_name": "cookie_repo",
}

configurations = [
    pytest.param(
        {
            **common,
        },
    )
]


@pytest.fixture(name='custom_template')
def fixture_custom_template(cookies_session, scope="module"):
    template = cookies_session._default_template + "/cookiecutter-django-app"  # pylint: disable=protected-access
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
    assert "cookie_repo" == readme_lines[0]
    assert 'The full documentation is at https://cookie_repo.readthedocs.org.' in readme_lines
    try:
        sh.python("setup.py", 'check', restructuredtext=True, strict=True)
    except sh.ErrorReturnCode as exc:
        pytest.fail(str(exc))


def test_travis(options_baked):
    """The generated .travis.yml file should pass a sanity check."""
    travis_text = Path(".travis.yml").read_text()
    assert 'pip install -r requirements/travis.txt' in travis_text


def test_quality(options_baked):
    """Run quality tests on the given generated output."""
    for dirpath, _dirnames, filenames in os.walk("."):
        for filename in filenames:
            name = os.path.join(dirpath, filename)
            if not name.endswith('.py'):
                continue
            try:
                sh.pylint(name)
                sh.pycodestyle(name)
                sh.pydocstyle(name)
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
