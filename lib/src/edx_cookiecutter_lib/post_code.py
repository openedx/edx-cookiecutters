"""
Code for use by post_gen_project.py files.
"""

import os
import shutil

from cookiecutter.main import cookiecutter
from edx_lint.cmd.write import write_main


def move(src, dest):
    """
    Use to move files or folders without replacement.
    """
    if os.path.isfile(dest):
        os.remove(src)
        return
    if os.path.isdir(src) and os.path.isdir(dest):
        dir_contents = os.listdir(src)
        for content in dir_contents:
            move(os.path.join(src, content), os.path.join(dest, content))
        os.rmdir(src)
    else:
        shutil.move(src, dest)


# cookiecutter can import a template from either github or from a location on local disk.
# If someone is debugging this repository locally, the below block is necessary to pull in
#   local versions of the templates
EDX_COOKIECUTTER_ROOTDIR = os.getenv('EDX_COOKIECUTTER_ROOTDIR') or 'https://github.com/openedx/edx-cookiecutters.git'


def post_gen_project(extra_context):
    """
    Most of what's needed after generating a project.

    `extra_context` is a dictionary of values to pass to the cookiecutter.
    """
    # Use Python template to get python files

    # output location for python-template cookiecutter
    placeholder_repo_name = "placeholder_repo_name_0"
    extra_context["placeholder_repo_name"] = placeholder_repo_name
    cookiecutter(
        EDX_COOKIECUTTER_ROOTDIR,
        extra_context=extra_context,
        no_input=True,
        directory='python-template',
    )

    # moving templated cookie-cutter output to root
    project_root_dir = os.getcwd()
    python_cookiecutter_output_loc = os.path.join(project_root_dir, placeholder_repo_name)
    files = os.listdir(python_cookiecutter_output_loc)

    for f in files:
        move(os.path.join(python_cookiecutter_output_loc, f), os.path.join(project_root_dir, f))

    # removing temp dir created by templated cookiecutter
    os.rmdir(python_cookiecutter_output_loc)

    # Post build fixes
    write_main(['pylintrc'])
