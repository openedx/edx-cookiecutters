#!/usr/bin/env python
"""
Tests for the `{{ cookiecutter.repo_name }}` models module.
"""
{%- if cookiecutter.models != "Comma-separated list of models" -%}
{%- for model in cookiecutter.models.replace(' ', '').split(',') %}


class Test{{ model }}:
    """
    Tests of the {{ model }} model.
    """

    def test_something(self):
        """TODO: Write real test cases."""
{%- endfor -%}
{%- else %}


def test_placeholder():
    """
    Placeholder to allow pytest to succeed before real tests are in place.

    (If there are no tests, it will exit with code 5.)
    """
{%- endif %}
