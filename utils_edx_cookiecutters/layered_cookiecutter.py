"""
    Helps create a cookiecutter using layered approach
"""
import os
import shutil

from cookiecutter.main import cookiecutter
from edx_lint.cmd.write import write_main


class LayeredCookiecutter():
    """
    Class to help facilitate usage of the layered cookiecutter approach
    """

    # cookiecutter can import a template from either github or from a location on local disk.
    # If someone is debugging this repository locally, the below block is necessary to pull in
    #   local versions of the templates
    EDX_COOKIECUTTER_ROOTDIR = os.getenv('EDX_COOKIECUTTER_ROOTDIR') or 'https://github.com/edx/edx-cookiecutters.git'

    def __init__(self, project_rootdir, edx_cookiecutter_rootdir=None):
        if edx_cookiecutter_rootdir is not None:
            self.EDX_COOKIECUTTER_ROOTDIR = edx_cookiecutter_rootdir
        self.templates = []
        self.project_rootdir = project_rootdir

    def move(self, src, dest):
        """
        Use to move files or folders without replacement.
        """
        if os.path.isfile(dest):
            os.remove(src)
            return
        if os.path.isdir(src) and os.path.isdir(dest):
            dir_contents = os.listdir(src)
            for content in dir_contents:
                self.move(os.path.join(src, content), os.path.join(dest, content))
            os.rmdir(src)
        else:
            shutil.move(src, dest)

    def remove(self, path):
        """
        Use to remove either a file or a whole directory.
        """
        full_path = os.path.join(self.project_rootdir, path)
        if os.path.isfile(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
        else:
            print("{path} not in cookiecutter output".format(path=full_path))

    def add_template(self, template_name, extra_context, remove_object=None):
        """
        Used to add templates.

        The templates will be used in order they are added.
        """
        if remove_object is None:
            remove_object = []
        template_info = {
                "extra_context": extra_context,
                "template_name": template_name,
                "remove_object": remove_object,
                }
        self.templates.append(template_info)

    def create_cookiecutter(self):
        """
        creates cookeicutter using templates added using add_template
        """
        for counter, template in enumerate(self.templates):
            template["extra_context"]["placeholder_repo_name"] = "placeholder_dir_{}".format(counter)
            cookiecutter(
                    self.EDX_COOKIECUTTER_ROOTDIR,
                    extra_context=template["extra_context"],
                    no_input=True,
                    directory=template["template_name"],
                )

            template_output_loc = os.path.join(
                                    self.project_rootdir,
                                    template["extra_context"]["placeholder_repo_name"]
                                    )
            template_files = os.listdir(template_output_loc)
            for f in template_files:
                self.move(os.path.join(template_output_loc, f), os.path.join(self.project_rootdir, f))

            for object_name in template["remove_object"]:
                self.remove(object_name)
            # Post build fixes
            write_main(['pylintrc'])
