=================
edx-cookiecutters
=================

This repository will holds most of the cookiecutters relavant to developers at edx.

Available cookiecutters:
------------------------
- cookiecutter-django-ida
- cookiecutter-django-app
- cookiecutter-python-library
- cookiecutter-xblock

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

Example: python-template holds all the basic files necessary for a edx python repository. The template is used by django-template, cookiecutter-django-app, cookiecutter-django-ida to create the base files necessary. cookiecutter-django-ida also deletes some of the files created by python-template cause those are not necessary for its operation.

Further info docs are WIP.

