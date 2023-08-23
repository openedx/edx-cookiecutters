#!/usr/bin/env python
"""
Tests for the `{{ cookiecutter.repo_name }}` models module.
"""

import pytest
{%- if cookiecutter.models != "Comma-separated list of models" -%}
{%- for model in cookiecutter.models.replace(' ', '').split(',') %}


class Test{{ model }}:
    """
    Tests of the {{ model }} model.
    """

    @pytest.mark.skip(reason="Placeholder to allow pytest to succeed before real tests are in place.")
    def test_placeholder(self):
        """
        TODO: Delete this test once there are real tests.
        """
{%- endfor -%}
{%- else %}


@pytest.mark.skip(reason="Placeholder to allow pytest to succeed before real tests are in place.")
def test_placeholder():
    """
    TODO: Delete this test once there are real tests.
    """
{%- endif %}
