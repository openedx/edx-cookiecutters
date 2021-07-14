.. {{ cookiecutter.project_name }} documentation top level file, created by
   sphinx-quickstart on {% now 'local', '%a %b %d %H:%M:%S %Y' %}.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ cookiecutter.project_name }}
{{ "=" * (cookiecutter.project_name|length) }}

{{ cookiecutter.project_short_description }}

Contents:

.. toctree::
   :maxdepth: 2

   readme
   getting_started
   testing
   internationalization
   modules
   changelog
   decisions


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
