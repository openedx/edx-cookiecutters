"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""

from edx_cookiecutter_lib.post_code import post_gen_project

setup_py_keyword_args = """entry_points={
        'xblock.v1': [
            '{{cookiecutter.tag_name}} = {{cookiecutter.package_name}}:{{cookiecutter.class_name}}',
        ]
    },
    package_data=package_data("{{cookiecutter.package_name}}", ["static", "public"]),
"""

post_gen_project(
    extra_context={
        "github_org": "{{cookiecutter.github_org}}",
        "repo_name": "{{cookiecutter.repo_name}}",
        "project_name": "{{cookiecutter.repo_name}}",
        "sub_dir_name": "{{cookiecutter.package_name}}",
        "project_short_description": "{{cookiecutter.project_desc}}",
        "version": "{{cookiecutter.version}}",
        "author_name": "{{cookiecutter.author_name}}",
        "author_email": "{{cookiecutter.author_email}}",
        "open_source_license": "{{cookiecutter.open_source_license}}",
        "setup_py_loading_pkg_data": "yes",
        "setup_py_keyword_args": setup_py_keyword_args,
    },
    symlink_translation=True,
)
