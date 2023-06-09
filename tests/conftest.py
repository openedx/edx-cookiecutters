"""Pytest configuration."""

import pytest

# Pytest will rewrite assertions in test modules, but not elsewhere.
# This tells pytest to also rewrite assertions in these modules.
pytest.register_assert_rewrite("tests.common_tests")
