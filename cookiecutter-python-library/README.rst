cookiecutter-python-library
###########################

A cookiecutter_ template for edX python projects. For django related cookiecutters, see cookiecutters-django-{ida, app} located in edx-cookiecutters.

.. _cookiecutter: https://cookiecutter.readthedocs.org/en/latest/index.html

**This template produces a Python 3.8 project.**

This cookiecutter template is intended for new edX python libraries.

Usage
*****

To create a project using this cookiecutter, follow the instructions found in edx-cookiecutter's `readme`_.

.. _readme: https://github.com/openedx/edx-cookiecutters/blob/master/README.rst

After the new folder is created, you will need to:

1. ``cd <new_repo_folder>``
2. Create a python 3 virtual environment and activate it
3. ``make upgrade``

**Note** This cookiecutter repo currently has some issues with repos that use a hyphen in their name. If this is the case, some pieces of the repo will need to be changed from ``new-repo-name`` to ``new_repo_name``, particularly the Python pieces.

Requirements
============

Once you initialize your project, run ``make upgrade`` to generate
``.txt`` files in the ``requirements/`` directory,
which will contain pinned dependency versions.
Regularly re-run this command going forward in order to freshen the version pins.
Failure to do so could open your IDA to bugs, security vulnerabilities,
and other issues.

It is recommended to follow the instructions in
`Adding repositories for auto python dependency management <https://openedx.atlassian.net/wiki/spaces/TE/pages/989135321/Adding+repositories+for+auto+python+dependency+management>`_
in order to perform this process on a regular cadence.

Documentation
=============

Sphinx is set up for your project in the ``docs`` directory. All developer documentation should be added here (as opposed to a long README file). Doing this also has the added benefit of giving you a good starting point when the time comes to open source your project!

Sphinx is themed with the common edX theme `edx-sphinx-theme <https://github.com/openedx/edx-sphinx-theme>`_ by default. If you wish to publish your documentation to Read the Docs you will need to make sure to take the steps `outlined here <https://edx-sphinx-theme.readthedocs.io/en/latest/readme.html#read-the-docs-configuration>`_.

Testing
=======

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
*************************

Please do not report security issues in public. Please email security@edx.org.

Getting Help
************

If you're having trouble, we have discussion forums at https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack invitation`_, then join our `community Slack workspace`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help
