{{cookiecutter.project_name}}
=============================

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

The ``README.rst`` file should start with a brief description of the repository,
which sets it in the context of other repositories under the ``edx``
organization. It should make clear where this fits in to the overall edX
codebase.

{{ cookiecutter.project_short_description}}

Overview (please modify)
------------------------

The ``README.rst`` file should then provide an overview of the code in this
repository, including the main components and useful entry points for starting
to understand the code in more detail.

Documentation
-------------

The full documentation is at https://{{ cookiecutter.repo_name }}.readthedocs.org.

License
-------

The code in this repository is licensed under the {{ cookiecutter.open_source_license }} unless
otherwise noted.

Please see `LICENSE.txt <LICENSE.txt>`_ for details.

How To Contribute
-----------------

Contributions are very welcome.
Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.
Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for all Open edX projects.

The pull request description template should be automatically applied if you are creating a pull request from GitHub. Otherwise you
can find it at `PULL_REQUEST_TEMPLATE.md <.github/PULL_REQUEST_TEMPLATE.md>`_.

The issue report template should be automatically applied if you are creating an issue on GitHub as well. Otherwise you
can find it at `ISSUE_TEMPLATE.md <.github/ISSUE_TEMPLATE.md>`_.

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about the Open edX project in general?
Please refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/edx/{{ cookiecutter.repo_name }}.svg?branch=master
    :target: https://travis-ci.org/edx/{{ cookiecutter.repo_name }}
    :alt: Travis

.. |codecov-badge| image:: http://codecov.io/github/edx/{{ cookiecutter.repo_name }}/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/{{ cookiecutter.repo_name }}?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?version=latest
    :target: http://{{ cookiecutter.repo_name }}.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.repo_name }}.svg
    :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/{{ cookiecutter.repo_name }}.svg
    :target: https://github.com/edx/{{ cookiecutter.repo_name }}/blob/master/LICENSE.txt
    :alt: License
