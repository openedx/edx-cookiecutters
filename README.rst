=================
edx-cookiecutters
=================

This repository holds most of the Open edX public cookiecutters.

Using the cookiecutters
***********************


Available cookiecutters
------------------------

cookiecutter-django-ida
    for creating new independently deployable apps (IDAs).

cookiecutter-django-app
    for creating reusable Django packages (installable apps).

cookiecutter-python-library
    for creating a Python package that follows Open edX standards.

cookiecutter-xblock
    for creating a XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.

Development Workflow
--------------------

One Time Setup
______________
.. code-block::

  # Clone the repository
  git clone git@github.com:edx/edx-cookiecutters.git
  cd edx-cookiecutters

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  # $(basename $(pwd)) will give you the name of the current working directory, in this case ``edx-cookiecutters``
  mkvirtualenv -p python3.8 edx-cookiecutters


Every time you develop something in this repo
_____________________________________________
.. code-block::

  # Activate the virtualenv
  workon edx-cookiecutters

  # Grab the latest code
  git checkout master
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim …

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit …
  git push

  # Open a PR and ask for review.


Using a cookiecutter
--------------------

These instructions assume you have cloned this repository and are currently in its head dir. You will need a virtualenv for running the cookiecutter. You can discard it once the cookiecutter has made your new repo.

Commands::

    $ make requirements  # from inside edx-cookiecutter repo
    # Replace <OUTPUT-DIRECTORY> with the base directory; your new directory will go inside.
    $ cookiecutter -o <OUTPUT-DIRECTORY> <COOKIECUTTER-NAME>

TODOs after creating cookiecutter
--------------------------------

- Modify project README
- Modify project docs/decisions/0001-purpose-of-this-repo.rst ADR

Updating cookiecutters
**********************

If you are modifying and debugging cookiecutters on a local device, please see "Local Debugging of the layered cookiecutters" section below.

Cookiecutters using layered apporach
------------------------------------

- cookiecutter-python-library
- cookiecutter-django-app
- cookiecutter-django-ida
- cookiecutter-xblock

If you are updating above cookiecutters, please see docs/decisions/0003-layered-cookiecutter.rst and docs/how_tos/modifying_layered_cookiecutter.rst

Local Debugging of the layered cookiecutters
--------------------------------------------

To ensure that the layered cookiecutters pull from your local code,
instead of GitHub, run cookiecutter like::

    $ make cookiecutter-<TEMPLATE-NAME>

eg::

    $ make cookiecutter-django-app
    $ make cookiecutter-django-ida
    $ make cookiecutter-python-library
    $ make cookiecutter-xblock

Decisions
---------

See docs/decisions/0003-layered-cookiecutter.rst for details on layering cookiecutters to share boilerplate files.

Community
*********

Contributing
------------

Contributions are very welcome. Tests can be run with `tox`_. Please ensure the coverage at least stays the same before you submit a pull request.

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

If you're having trouble, we have discussion forums at https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack invitation`_, then join our `community Slack workspace`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx-slack-invite.herokuapp.com/
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help
.. _tox: https://tox.readthedocs.io/en/latest/
