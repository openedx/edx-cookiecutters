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

Using a cookiecutter
--------------------

Commands::

    $ make requirements
    # Replace <COOKIECUTTER-NAME> with one of available cookiecutters
    $ cookiecutter <COOKIECUTTER-NAME>

Local Debugging of cookiecutters
--------------------------------

To debug locally, set the env variable EDX_COOKIECUTTER_ROOTDIR to the root of the edx-cookiecutters repository. For example, from inside /edx-cookiecutters, use::

    $ export EDX_COOKIECUTTER_ROOTDIR="/edx-cookiecutters"

 Without this environment variable, the cookiecutter will pull templates from github, which will not have your local changes on them.

Decisions
---------

See docs/decisions/0003-layered-cookiecutter.rst for details on layering cookiecutters to share boilerplate files.
