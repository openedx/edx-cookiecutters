"""Pytest configuration."""

import pytest
import sh

from .bake import bake_in_temp_dir

# Pytest will rewrite assertions in test modules, but not elsewhere.
# This tells pytest to also rewrite assertions in these modules.
pytest.register_assert_rewrite("tests.common_tests")


@pytest.fixture(name="custom_template", scope="module")
def fixture_custom_template(cookies_session, custom_template_name):
    """
    Produce the template directory to use with tests.

    Each test_cookiecutter_*.py file uses a different cookiecutter directory.
    It gives the base name with the `custom_template_name` fixture.  This makes
    a full path for use with `bake_in_temp_dir`.
    """
    template = cookies_session._default_template + "/" + custom_template_name  # pylint: disable=protected-access
    return template


@pytest.fixture(scope="module")
def options_baked(cookies_session, configuration, custom_template):
    """
    Bake a cookie cutter, parameterized by configurations.

    Provides the configuration dict, and changes into the directory with the
    baked result.
    """
    with bake_in_temp_dir(cookies_session, extra_context=configuration, template=custom_template):
        sh.make('upgrade')
        sh.pip('install', '-r', 'requirements/test.txt')
        yield configuration
