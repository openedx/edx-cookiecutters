edx-cookiecutters
#################

This repository holds most of the Open edX public cookiecutters.



Available cookiecutters
***********************

cookiecutter-django-ida
    for creating new independently deployable apps (IDAs).

cookiecutter-django-app
    for creating reusable Django packages (installable apps).

cookiecutter-python-library
    for creating a Python package that follows Open edX standards.

cookiecutter-xblock
    for creating a XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.


Using the cookiecutters
***********************

1. One Time Setup
=================
.. code-block::

  # Clone the repository
  git clone git@github.com:openedx/edx-cookiecutters.git
  cd edx-cookiecutters

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 edx-cookiecutters

2. Create a cookiecutter Repository
===================================

These instructions assume you have cloned this repository and are currently in its head dir. You will need a virtualenv for running the cookiecutter. You can discard it once the cookiecutter has made your new repo.

Commands::

    $ make requirements  # from inside edx-cookiecutter repo
    # Replace <OUTPUT-DIRECTORY> with the base directory; your new directory will go inside.
    # Replace <COOKIECUTTER-NAME> with one of the available cookiecutters documented above.
    $ cookiecutter -o <OUTPUT-DIRECTORY> <COOKIECUTTER-NAME>

3. TODOs after running cookiecutter
===================================

- Modify project README
- Modify the "requirements upgrade workflow" at ".github/workflows/upgrade-python-requirements.yml" and add "team_reviewers" and the "email_address" of the team/person
- Modify project docs/decisions/0001-purpose-of-this-repo.rst ADR
- Commit and push to GitHub
- On GitHub, update repo's "About" description

Updating cookiecutters
**********************

If you find anything that is outdated in the cookiecutters in this repository, please create a PR with updates.


.. Note:: Some of the cookiecutters in this repository use the layered cookiecutter approach. If you are modifying these, please see "Local Debugging of the layered cookiecutters" section below.


Directions for contributing to this repository
==============================================
.. code-block::

  # Clone the repository
  git clone git@github.com:openedx/edx-cookiecutters.git
  cd edx-cookiecutters

  # Set up a virtualenv using virtualenvwrapper with the same name as the repo and activate it
  mkvirtualenv -p python3.8 edx-cookiecutters
  # Activate the virtualenv
  workon edx-cookiecutters

  # Grab the latest code
  git checkout master
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes**
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


Cookiecutters using layered approach
====================================

- cookiecutter-python-library
- cookiecutter-django-app
- cookiecutter-django-ida
- cookiecutter-xblock

If you are updating above cookiecutters, please see `0003-layered-cookiecutter ADR
<./docs/decisions/0003-layered-cookiecutter.rst>`_ and `How-to modify layered cookiecutters
<./docs/how_tos/modifying_layered_cookiecutter.rst>`_.

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
*********

See `0003-layered-cookiecutter ADR <./docs/decisions/0003-layered-cookiecutter.rst>`_ for details on layering cookiecutters to share boilerplate files.

Community
*********

Contributing
============

Contributions are very welcome. Tests can be run with `tox`_. Please ensure the coverage at least stays the same before you submit a pull request.

License
=======

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.


Reporting Security Issues
=========================

Please do not report security issues in public. Please email security@openedx.org.

Getting Help
============

If you're having trouble, we have discussion forums at https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack invitation`_, then join our `community Slack workspace`_.

For more information about these options, see the `Getting Help <https://openedx.org/getting-help>`__ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _tox: https://tox.readthedocs.io/en/latest/
