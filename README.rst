=================
edx-cookiecutters
=================

This repository will holds most of the edx's public python cookiecutters.

Available cookiecutters:
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


Experiment
----------
We are currently experimenting with a layering approach to cookiecutter. The idea is to have boiler plate files, which don't need to be changed, in bottom layer and have subsequent layers add files/modify files as necessary.

Example: python-template holds all the basic files necessary for an edx python repository. The template is used by cookiecutter-django-app, cookiecutter-django-ida and cookiecutter-python-library to create the base files necessary. cookiecutter-django-ida deletes some of the files created by python-template cause those are not necessary for its operation.
