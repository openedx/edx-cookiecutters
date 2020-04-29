from cookiecutter.main import cookiecutter
import pdb
import shutil
import os

# Using the template to create things
extra_context = {}
extra_context["placeholder_repo_name"] = "placeholder_repo_name"
cookiecutter('/Users/msingh/dev/src/cexperiments/cookdir/python-template', extra_context=extra_context, no_input=True)

# moving templated cookie-cutter output to root
project_root_dir = os.getcwd()
python_cookiecutter_output_loc = os.path.join(project_root_dir, extra_context["placeholder_repo_name"])
files = os.listdir(python_cookiecutter_output_loc)
for f in files:
    shutil.move(os.path.join(python_cookiecutter_output_loc,f), os.path.join(project_root_dir, f))

# removing temp dir created by templated cookiecutter
os.rmdir(python_cookiecutter_output_loc)
