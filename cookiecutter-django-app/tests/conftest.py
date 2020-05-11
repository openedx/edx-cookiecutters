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


@pytest.fixture(params=configurations, scope="session")
def options_baked(cookies_session, request):
    """
    Bake a cookie cutter, parameterized by configurations.

    Provides the configuration dict, and changes into the directory with the
    baked result.
    """
    with bake_in_temp_dir(cookies_session, extra_context=request.param):
        yield request.param


@pytest.fixture(scope="session")
def options_upgraded(options_baked):  # pylint: disable=redefined-outer-name
    """
    Bake the cookie cutter, and run make upgrade.
    """
    sh.make('upgrade')  # first run make upgrade to populate requirements/test.txt
    yield options_baked
