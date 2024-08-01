"""TO-DO: Write a description of what this XBlock is."""

import os
from importlib import resources

from django.utils import translation
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope
from xblock.utils.resources import ResourceLoader

resource_loader = ResourceLoader(__name__)


class {{cookiecutter.class_name}}(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )

    def resource_string(self, path):
        """
        Retrieve string contents for the file path
        """
        path = os.path.join('static', path)
        return resource_loader.load_unicode(path)

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        Create primary view of the {{cookiecutter.class_name}}, shown to students when viewing courses.
        """
        if context:
            pass  # TO-DO: do something based on the context.
        html = self.resource_string("html/{{cookiecutter.package_name}}.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("css/{{cookiecutter.package_name}}.css"))

        # Add i18n js
        statici18n_js_url = self._get_statici18n_js_url()
        if statici18n_js_url:
            frag.add_javascript_url(self.runtime.local_resource_url(self, statici18n_js_url))

        frag.add_javascript(self.resource_string("js/src/{{cookiecutter.package_name}}.js"))
        frag.initialize_js('{{cookiecutter.class_name}}')
        return frag

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    @XBlock.json_handler
    def increment_count(self, data, suffix=''):
        """
        Increments data. An example handler.
        """
        if suffix:
            pass  # TO-DO: Use the suffix when storing data.
        # Just to show data coming in...
        assert data['hello'] == 'world'

        self.count += 1
        return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """Create canned scenario for display in the workbench."""
        return [
            ("{{cookiecutter.class_name}}",
             """<{{cookiecutter.tag_name|lower}}/>
             """),
            ("Multiple {{cookiecutter.class_name}}",
             """<vertical_demo>
                <{{cookiecutter.tag_name|lower}}/>
                <{{cookiecutter.tag_name|lower}}/>
                <{{cookiecutter.tag_name|lower}}/>
                </vertical_demo>
             """),
        ]

    @staticmethod
    def _get_statici18n_js_url():
        """
        Return the Javascript translation file for the currently selected language, if any.

        Defaults to English if available.
        """
        locale_code = translation.get_language()
        if locale_code is None:
            return None
        text_js = 'static/js/translations/{locale_code}/text.js'
        lang_code = locale_code.split('-')[0]
        for code in (locale_code, lang_code, 'en'):
            text_js_path = text_js.format(locale_code=code)
            if resources.files(resource_loader.module_name).joinpath(text_js_path).is_file():
                return text_js_path
        return None

    @staticmethod
    def get_dummy():
        """
        Generate initial i18n with dummy method.
        """
        return translation.gettext_noop('Dummy')
