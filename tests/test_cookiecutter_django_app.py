"""
Tests of the project generation output.
"""

import logging
import logging.config
import re
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
    "author_email": "cookie@monster.org",
    "author_name": "Cookie Monster",
    "github_org": "bakery_org",
    "repo_name": "cookie_repo",
}

configurations = [
    pytest.param(
        {
            **common,
        },
        id="no models"
    ),
    pytest.param(
        {
            **common,
            "models": "ChocolateChip,Zimsterne",
        },
        id="two models"
    ),
]


@pytest.fixture(name="configuration", params=configurations, scope="module")
def fixture_configuration(request):
    return request.param


@pytest.fixture(name="custom_template_name", scope="module")
def fixture_custom_template_name():
    return "cookiecutter-django-app"


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


def test_models(options_baked, configuration):
    """The generated models.py file should pass a sanity check."""
    if "models" not in configuration:
        pytest.skip("No models to check")
    model_txt = Path("cookie_lover/models.py").read_text()
    for model_name in configuration.get("models").split(","):
        pattern = fr'^class {model_name}\(TimeStampedModel\):$'
        assert re.search(pattern, model_txt, re.MULTILINE)


def test_urls(options_baked):
    """The urls.py file should be present."""
    urls_file_txt = Path("cookie_lover/urls.py").read_text()
    basic_url = "re_path(r'', TemplateView.as_view(template_name=\"cookie_lover/base.html\"))"
    assert basic_url in urls_file_txt


def test_github_actions_ci():
    """The generated ci.yml file should pass a sanity check."""
    ci_text = Path(".github/workflows/ci.yml").read_text()
    assert 'pip install -r requirements/ci.txt' in ci_text


def test_dunder_init(options_baked):
    """The generated init file should have at least the version string."""
    init_text = Path("cookie_lover/__init__.py").read_text()
    pattern = r"^__version__ = "
    assert re.search(pattern, init_text, re.MULTILINE)


def test_app_config(options_baked):
    """The generated Django AppConfig should have an AppConfig subclass."""
    apps_text = Path("cookie_lover/apps.py").read_text()
    pattern = r'^class CookieLoverConfig\(AppConfig\):$'
    assert re.search(pattern, apps_text, re.MULTILINE)


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


def test_quality(options_baked):
    """Run quality tests on the given generated output."""
    py_files = [name for name in all_files() if name.endswith(".py")]
    sh.pylint(*py_files)
    sh.pycodestyle(*py_files)
    sh.pydocstyle(*py_files)
    sh.isort(*py_files, check_only=True, diff=True)

    # Sanity check the generated Makefile
    sh.make('help')
    # quality check docs
    sh.doc8("README.rst", ignore_path="docs/_build")
    sh.doc8("docs", ignore_path="docs/_build")


def test_tests(options_baked):
    """Make sure the tox default tests work"""
    run_in_virtualenv('pip install -r requirements/ci.txt; tox')
