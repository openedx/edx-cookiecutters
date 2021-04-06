Change Log
==========

..
   This file loosely adheres to the structure of https://keepachangelog.com/,
   but in reStructuredText instead of Markdown.

2021-04-05
----------

Fixed
~~~~~

* Fixed django module documentation by using proper django settings.

Added
~~~~~

* Added "Edit on Github" button to new project's ReadTheDocs.

2020-11-25
----------

Changed
~~~~~~~

* Add a typical development workflow to the generated README

2020-11-06
----------

Changed
~~~~~~~

* All projects (including top level) use Python 3.8 and Django 2.2

2020-11-06
----------

Fixed
~~~~~

* Fix Read the Docs config to point to the correct config file.
  ``requirements/docs.txt`` should be ``requirements/doc.txt``

2020-11-05
----------

Fixed
~~~~~

* Use virtualenv to prevent flakiness in ``make upgrade`` test

2020-10-30
----------

Fixed
~~~~~

* Don't fill in a sample url pattern for Django apps, just suggest one in a comment

2020-08-26
----------

Changed
~~~~~~~

* Configure devstack Django settings to have a good JWT_AUTH and a DATABASES that point at the mysql container.
* Install mysqlclient
* The app container should accept stdin.
* Use the python dev server as the app container's command, since it can hot-reload.
* Rename containers in a more standard way.
* Clean pycrypto crap before requirements are built.
* Add devstack-themed make targets.
* Ignore emacs backup files.

2020-08-14
----------

Changed
~~~~~~~

* Ignores /healthcheck endpoint in monitoring for IDAs

2020-08-07
----------

Fixed
~~~~~

- Tweaks to the READMEs to separate using cookiecutters from updating
  cookiecutters; clarify the use of a virtualenv for running cookiecutters;
  correct the way we talk about Slack and getting help; minor formatting
  improvements.

2020-08-03
----------

Fixed
~~~~~~~

* Doc8 configs no longer have a max line length, which goes against our best practice to not use hard line breaks, as documented in `OEP-19: Developer Documentation Best Practices`_.

.. _`OEP-19: Developer Documentation Best Practices`: https://open-edx-proposals.readthedocs.io/en/latest/oep-0019-bp-developer-documentation.html#best-practices

2020-07-28
----------

Fixed
~~~~~~~

* Include ``JWT_AUTH_COOKIE`` in the base ``JWT_AUTH`` settings dict.

2020-07-15
----------

Changed
~~~~~~~

* Changed how oauth2_urlpatterns is imported in the urls.py file

2020-07-09
----------

Fixed
~~~~~

* Added csrf.urls to IDA cookiecutter so that CSRF works

(some intervening changes not captured)

2020-06-02
----------

* Adding decision to make this repo the place for all edx cookiecutters.

2020-05-27
----------

* Used the layered approach for cookiecutter-xblock
* setup.py is now only in python-template

2020-05-12
----------

Added
~~~~~

* Added cookiecutter-argocd-application
    - a cookiecutter used by devops
* Added cookiecutter-xblock


2020-05-11
----------

Added
~~~~~

* Added CHANGELOG
