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
{%- endif %}
