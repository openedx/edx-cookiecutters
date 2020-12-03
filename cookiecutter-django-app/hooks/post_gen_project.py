"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""
import os

from edx_lint.cmd.write import write_main

from utils_edx_cookiecutters.layered_cookiecutter import LayeredCookiecutter

layered_cookiecutter = LayeredCookiecutter(os.getcwd())

extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["sub_dir_name"] = "{{cookiecutter.app_name}}"
extra_context["project_name"] = "{{cookiecutter.project_name}}"
extra_context["project_short_description"] = "{{cookiecutter.project_short_description}}"
extra_context["version"] = "{{cookiecutter.version}}"
extra_context["author_name"] = "{{cookiecutter.author_name}}"
extra_context["author_email"] = "{{cookiecutter.author_email}}"
extra_context["open_source_license"] = "{{cookiecutter.open_source_license}}"
extra_context["requires_django"] = "yes"

extra_context["placeholder_repo_name"] = python_placeholder_repo_name

layered_cookiecutter.add_template(template_name='python-template', extra_context=extra_context)

layered_cookiecutter.create_cookiecutter()

write_main(['pylintrc'])