=================
edx-cookiecutters
=================

This repository holds most of the Open edx public python cookiecutters.

Available cookiecutters
------------------------

- cookiecutter-django-ida
    - intended for new edX independently deployable apps (IDAs)
- cookiecutter-django-app
    - for creating reusable Django packages (installable apps)
- cookiecutter-python-library
    - for creating a python package that follows edx standards
- cookiecutter-xblock
    - for createing a XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.

Cookiecutters using layered apporach
------------------------------------

- cookiecutter-python-library
- cookiecutter-django-app
- cookiecutter-django-ida

Using a cookiecutter
--------------------

Commands::

    $ make requirements  # from inside edx-cookiecutter repo
    # move to location where you want to create a new repo
    # Replace <COOKIECUTTER-NAME> with one of available cookiecutters
    $ cookiecutter https://github.com/edx/edx-cookiecutters <COOKIECUTTER-NAME>


Local Debugging of cookiecutters
--------------------------------

To debug locally, set the env variable EDX_COOKIECUTTER_ROOTDIR to the root of the edx-cookiecutters repository. For example, from inside /edx-cookiecutters, use::

    $ export EDX_COOKIECUTTER_ROOTDIR="/edx-cookiecutters"

 Without this environment variable, the cookiecutter will pull templates from github, which will not have your local changes on them.

Decisions
---------

See docs/decisions/0003-layered-cookiecutter.rst for details on layering cookiecutters to share boilerplate files.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help
.. _`file an issue`: https://github.com/edx/edx-cookiecutters/issues
.. _`tox`: https://tox.readthedocs.io/en/latest/
