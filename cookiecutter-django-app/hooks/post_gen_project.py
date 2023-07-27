"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""

from edx_cookiecutter_lib.post_code import post_gen_project

post_gen_project(
    extra_context={
        "github_org": "{{cookiecutter.github_org}}",
        "repo_name": "{{cookiecutter.repo_name}}",
        "project_name": "{{cookiecutter.project_name}}",
        "sub_dir_name": "{{cookiecutter.app_name}}",
        "project_short_description": "{{cookiecutter.project_short_description}}",
        "version": "{{cookiecutter.version}}",
        "author_name": "{{cookiecutter.author_name}}",
        "author_email": "{{cookiecutter.author_email}}",
        "open_source_license": "{{cookiecutter.open_source_license}}",
        "requires_django": "yes",
    }
)
