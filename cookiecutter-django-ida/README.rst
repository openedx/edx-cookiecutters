cookiecutter-django-ida  |Travis|_
==================================
.. |Travis| image:: https://travis-ci.org/edx/cookiecutter-django-ida.svg?branch=master
.. _Travis: https://travis-ci.org/edx/cookiecutter-django-ida

A cookiecutter_ template for edX Django projects.

.. _cookiecutter: http://cookiecutter.readthedocs.org/en/latest/index.html

**This template produces a Python 3.6 project.**

This cookiecutter template is intended for new edX independently deployable apps (IDAs). It includes the following packages:

* Django 1.11.x
* Django REST Framework
* Django Waffle

The necessary configuration is also in place to support:

* i18n
* Documentation (using Sphinx_)
* Authentication with OAuth2
* Loading settings from YAML (for production)
* Pylint/Pycodestyle validation
* Travis CI

.. _Sphinx: http://sphinx-doc.org/

Usage
-----

As with any new project, you will need to create a virtual environment. Once this is set up, install cookiecutter and edx-lint:

.. code-block:: bash

    $ pip install cookiecutter
    $ pip install edx-lint

cookiecutter has the ability to pull templates directly from git, so there is no need to clone this repo. To access the template, provide the repo path as an argument:

.. code-block:: bash

    $ cd <workspace>
    $ cookiecutter https://github.com/edx/edx-cookiecutters.git --directory cookiecutter-django-ida

You will be prompted for a few basic details (described below). These will be used to create the new project.

..  list-table::
    :widths: 25 75
    :header-rows: 1

    * - Variable
      - Description
    * - project_name
      - Full name of the project. (e.g., E-Commerce Service)
    * - repo_name
      - Short (Python-friendly) name of the project. This should also be the name of the repository (e.g., ecommerce, credentials).
    * - repo_port
      - Port number for the project. Should be in the form `18***` with the 3 digits being any that aren't currently in use by other services.
    * - author_name
      - The author of the documentation. Leave this as the default ("edX") unless you have a good reason to change it.
    * - description
      - A short description of the project, used to initialize the documentation.

After the new folder is created, you will need to:

1. ``cd <new_repo_folder>``
2. Create a python 3 virtual environment and activate it
3. ``make upgrade``
4. ``make docker_build``
5. ``docker-compose up``

**Note** This cookiecutter repo currently has some issues with repos that use a hyphen in their name. If this is the case, some pieces of the repo will need to be changed from ``new-repo-name`` to ``new_repo_name``, particularly the Python pieces.

Requirements
~~~~~~~~~~~~

Once you initialize your project, run ``make upgrade`` to generate
``.txt`` files in the ``requirements/`` directory,
which will contain pinned dependency versions.
Regularly re-run this command going forward in order to freshen the version pins.
Failure to do so could open your IDA to bugs, security vulnerabilities,
and other issues.

It is recommended to follow the instructions in
`Adding repositories for auto python dependency management <https://openedx.atlassian.net/wiki/spaces/TE/pages/989135321/Adding+repositories+for+auto+python+dependency+management>`_
in order to perform this process on a regular cadence.

User Model Customization
~~~~~~~~~~~~~~~~~~~~~~~~

The project includes a custom Django user model in ``core/models.py``. You must further customize this model as your IDA/service requires. You MUST generate migrations for this model before Django can start:

.. code-block:: bash

    $ python manage.py makemigrations

Documentation
~~~~~~~~~~~~~

Sphinx is set up for your project in the ``docs`` directory. All developer documentation should be added here (as opposed to a long README file). Doing this also has the added benefit of giving you a good starting point when the time comes to open source your project!

Sphinx is themed with the common edX theme `edx-sphinx-theme <https://github.com/edx/edx-sphinx-theme>`_ by default. If you wish to publish your documentation to Read the Docs you will need to make sure to take the steps `outlined here <https://edx-sphinx-theme.readthedocs.io/en/latest/readme.html#read-the-docs-configuration>`_.

How To Contribute
-----------------

Contributions are welcome. Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details. Even though it was written with ``edx-platform`` in mind, these guidelines should be followed for Open edX code in general.

Testing
~~~~~~~

The ``Makefile`` includes a ``test`` target that runs basic validation on this template. This validation includes::

    * Create a new project using the template.
    * Generate and install pinned requirements
    * Run the project's migrations and validations.
    * Extract and compile translations.
    * Compile documentation.

Run this validation using the command below.

.. code-block:: bash

    $ make test

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Get Help
--------

Ask questions and discuss this project on `Slack <https://openedx.slack.com/messages/general/>`_ or in the `edx-code Google Group <https://groups.google.com/forum/#!forum/edx-code>`_.
