"""
Post-generation cookiecutter hook.

* See docs/decisions/0003-layered-cookiecutter.rst
"""
import shutil
import os

from cookiecutter.main import cookiecutter

from edx_lint.cmd.write import write_main

# cookiecutter can import a template from either github or from a location on local disk.
# If someone is debugging this repository locally, the below block is necessary to pull in
#   local versions of the templates
EDX_COOKIECUTTER_ROOTDIR = os.getenv('EDX_COOKIECUTTER_ROOTDIR')
import_template_from_github = True
if EDX_COOKIECUTTER_ROOTDIR is not None and isinstance(EDX_COOKIECUTTER_ROOTDIR, str):
    if len(EDX_COOKIECUTTER_ROOTDIR) > 0:
        import_template_from_github = False

def move(src, dest):
    """
    Used to move files or folders without replacement
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


# Using the template to create things
extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["project_name"] = "{{cookiecutter.project_name}}"
extra_context["project_short_description"] = "{{cookiecutter.project_short_description}}"
extra_context["version"] = "{{cookiecutter.version}}"
extra_context["owner_type"] = "{{cookiecutter.owner_name}}"
extra_context["author_name"] = "{{cookiecutter.author_name}}"
extra_context["author_email"] = "{{cookiecutter.author_email}}"
extra_context["owner_name"] = "{{cookiecutter.owner_name}}"
extra_context["open_source_license"] = "{{cookiecutter.open_source_license}}"

extra_context["placeholder_repo_name"] = "placeholder_repo_name"
if import_template_from_github:
    directory = "python-template"
    cookiecutter('git@github.com:edx/edx-cookiecutters.git',
        extra_context=extra_context,
        no_input=True,
        directory=directory
        )
else:
    cookiecutter(os.path.join(EDX_COOKIECUTTER_ROOTDIR, 'python-template'),
        extra_context=extra_context,
        no_input=True
        )

# moving templated cookie-cutter output to root
project_root_dir = os.getcwd()
python_cookiecutter_output_loc = os.path.join(project_root_dir, extra_context["placeholder_repo_name"])
files = os.listdir(python_cookiecutter_output_loc)

for f in files:
    move(os.path.join(python_cookiecutter_output_loc, f), os.path.join(project_root_dir, f))

# removing temp dir created by templated cookiecutter
os.rmdir(python_cookiecutter_output_loc)

# Post build fixes
write_main(['pylintrc'])
