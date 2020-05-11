from cookiecutter.main import cookiecutter
import pdb
import shutil
import os

def move(src, dest):
    if os.path.isfile(dest):
        os.remove(src)
        return
    if os.path.isdir(src) and os.path.isdir(dest):
        files = os.listdir(src)
        for f in files:
            move(os.path.join(src,f), os.path.join(dest,f))
        os.rmdir(src)
    else:
        shutil.move(src, dest)

def combine_templates(layer1, layer2, output_dest):
    """
    layer2 will overwrite files in layer1
    """
    move(layer2, output_dest)
    move(layer1, output_dest)


python_placeholder_repo_name = "placeholder_repo_name_0"


# Use Python template to get python files
extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["sub_dir_name"] = "{{cookiecutter.app_name}}"
extra_context["project_name"] = "{{cookiecutter.project_name}}"
extra_context["project_short_description"] = "{{cookiecutter.project_short_description}}"
extra_context["version"] = "{{cookiecutter.version}}"
extra_context["owner_type"] = "{{cookiecutter.owner_name}}"
extra_context["author_name"] = "{{cookiecutter.author_name}}"
extra_context["author_email"] = "{{cookiecutter.author_email}}"
extra_context["owner_name"] = "{{cookiecutter.owner_name}}"
extra_context["open_source_license"] = "{{cookiecutter.open_source_license}}"

extra_context["placeholder_repo_name"] = python_placeholder_repo_name
directory = "python-template"
#TODO(jinder): fix this before next
# cookiecutter('git@github.com:edx/edx-cookiecutters.git', extra_context=extra_context, no_input=True, directory=directory, checkout="msingh/django_app")
cookiecutter('/Users/msingh/dev/src/cexperiments/edx-cookiecutters/python-template', extra_context=extra_context, no_input=True)


django_placeholder_repo_name = "placeholder_repo_name_1"

# Use Django template to get common django files shared between ida and app
extra_context = {}
extra_context["repo_name"] = "{{cookiecutter.repo_name}}"
extra_context["sub_dir_name"] = "{{cookiecutter.app_name}}"
extra_context["placeholder_repo_name"] = django_placeholder_repo_name
directory = "django-template"
# TODO(jinder): change this to github link once pr is merged
cookiecutter('/Users/msingh/dev/src/cexperiments/edx-cookiecutters/django-template', extra_context=extra_context, no_input=True)

project_root_dir = os.getcwd()
python_template_cookiecutter_output_loc = os.path.join(project_root_dir, python_placeholder_repo_name)
django_template_cookiecutter_output_loc = os.path.join(project_root_dir, django_placeholder_repo_name)
templates_output_dir = os.path.join(project_root_dir, 'template_outputs')
os.mkdir(templates_output_dir)

combine_templates(python_template_cookiecutter_output_loc, django_template_cookiecutter_output_loc, templates_output_dir)

files = os.listdir(templates_output_dir)
for f in files:
    move(os.path.join(templates_output_dir,f), os.path.join(project_root_dir, f))

os.rmdir(templates_output_dir)

