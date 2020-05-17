"""Pytest fixtures."""

import pytest
import sh

from .helpers import bake_in_temp_dir

common = {
    "app_name": "cookie_lover",
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

@pytest.fixture
def custom_template(cookies_session):
    template = cookies_session._default_template + "/cookiecutter-django-app"
    return template

@pytest.fixture(params=configurations)
def options_baked(cookies_session, request, custom_template):
    """
    Bake a cookie cutter, parameterized by configurations.

    Provides the configuration dict, and changes into the directory with the
    baked result.
    """
    with bake_in_temp_dir(cookies_session, extra_context=request.param, template=custom_template):
        yield request.param

