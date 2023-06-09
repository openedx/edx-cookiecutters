{{cookiecutter.project_name}}
#############################

.. note::

  This README was auto-generated. Maintainer: please review its contents and
  update all relevant sections. Instructions to you are marked with
  "PLACEHOLDER" or "TODO". Update or remove those sections, and remove this
  note when you are done.

|pypi-badge| |ci-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge| |status-badge|

Purpose
*******

{{ cookiecutter.project_short_description}}

TODO: The ``README.rst`` file should start with a brief description of the repository and its purpose.
It should be described in the context of other repositories under the ``openedx``
organization. It should make clear where this fits in to the overall Open edX
codebase and should be oriented towards people who are new to the Open edX
project.

Getting Started
***************

Developing
==========

One Time Setup
--------------
.. code-block::

  # Clone the repository
  git clone git@github.com:{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}.git
  cd {{ cookiecutter.repo_name }}

  # Set up a virtualenv with the same name as the repo and activate it
  # Here's how you might do that if you have virtualenvwrapper setup.
  mkvirtualenv -p python3.8 {{ cookiecutter.repo_name }}


Every time you develop something in this repo
---------------------------------------------
.. code-block::

  # Activate the virtualenv
  # Here's how you might do that if you're using virtualenvwrapper.
  workon {{ cookiecutter.repo_name }}

  # Grab the latest code
  git checkout main
  git pull

  # Install/update the dev requirements
  make requirements

  # Run the tests and quality checks (to verify the status before you make any changes)
  make validate

  # Make a new branch for your changes
  git checkout -b <your_github_username>/<short_description>

  # Using your favorite editor, edit the code to make your change.
  vim ...

  # Run your new tests
  pytest ./path/to/new/tests

  # Run all the tests and quality checks
  make validate

  # Commit all your changes
  git commit ...
  git push

  # Open a PR and ask for review.

Deploying
=========

TODO: How can a new user go about deploying this component? Is it just a few
commands? Is there a larger how-to that should be linked here?

PLACEHOLDER: For details on how to deploy this component, see the `deployment how-to`_

.. _deployment how-to: https://docs.openedx.org/projects/{{ cookiecutter.repo_name }}/how-tos/how-to-deploy-this-component.html

Getting Help
************

Documentation
=============

PLACEHOLDER: Start by going through `the documentation`_.  If you need more help see below.

.. _the documentation: https://docs.openedx.org/projects/{{cookiecutter.repo_name}}

(TODO: `Set up documentation <https://openedx.atlassian.net/wiki/spaces/DOC/pages/21627535/Publish+Documentation+on+Read+the+Docs>`_)

More Help
=========

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the
community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack workspace`_.

For anything non-trivial, the best path is to open an issue in this
repository with as many details about the issue you are facing as you
can provide.

https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/issues

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx.org/slack
.. _community Slack workspace: https://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help

License
*******

The code in this repository is licensed under the {{ cookiecutter.open_source_license }} unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

Contributing
************

Contributions are very welcome.
Please read `How To Contribute <https://openedx.org/r/how-to-contribute>`_ for details.

This project is currently accepting all types of contributions, bug fixes,
security fixes, maintenance work, or new features.  However, please make sure
to have a discussion about your new feature idea with the maintainers prior to
beginning development to maximize the chances of your change being accepted.
You can start a conversation by creating a new issue on this repo summarizing
your idea.

The Open edX Code of Conduct
****************************

All community members are expected to follow the `Open edX Code of Conduct`_.

.. _Open edX Code of Conduct: https://openedx.org/code-of-conduct/

People
******

The assigned maintainers for this component and other project details may be
found in `Backstage`_. Backstage pulls this data from the ``catalog-info.yaml``
file in this repo.

.. _Backstage: https://backstage.openedx.org/catalog/default/component/{{ cookiecutter.repo_name }}

Reporting Security Issues
*************************

Please do not report security issues in public. Please email security@openedx.org.

.. |pypi-badge| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/workflows/Python%20CI/badge.svg?branch=main
    :target: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/actions
    :alt: CI

.. |codecov-badge| image:: https://codecov.io/github/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/coverage.svg?branch=main
    :target: https://codecov.io/github/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}?branch=main
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest
    :target: https://docs.openedx.org/projects/{{ cookiecutter.repo_name }}
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}.svg
    :target: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.repo_name }}/blob/main/LICENSE.txt
    :alt: License

.. TODO: Choose one of the statuses below and remove the other status-badge lines.
.. |status-badge| image:: https://img.shields.io/badge/Status-Experimental-yellow
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Maintained-brightgreen
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Deprecated-orange
.. .. |status-badge| image:: https://img.shields.io/badge/Status-Unsupported-red
