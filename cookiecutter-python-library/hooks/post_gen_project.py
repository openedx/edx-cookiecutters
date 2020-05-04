from cookiecutter.main import cookiecutter
import pdb
import shutil
import os

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
directory = "python-template"
# TODO(jinder): change this to github link once pr is merged
cookiecutter('git@github.com:jinder1s/edx-cookiecutters.git', extra_context=extra_context, no_input=True, directory=directory)

# moving templated cookie-cutter output to root
project_root_dir = os.getcwd()
python_cookiecutter_output_loc = os.path.join(project_root_dir, extra_context["placeholder_repo_name"])
files = os.listdir(python_cookiecutter_output_loc)
for f in files:
    shutil.move(os.path.join(python_cookiecutter_output_loc,f), os.path.join(project_root_dir, f))

# removing temp dir created by templated cookiecutter
os.rmdir(python_cookiecutter_output_loc)
