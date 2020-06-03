4. Which Cookiecutters in edx-cookiecutters?
============================================

Status
------

Accepted


Context
-------

* Currently, the only cookiecutters in this repository are the Open edx public python cookiecutters.

* Since the creation of this repo, others have tried adding public non-python cookiecutters to this repository.

* The name of this repository suggests all public edx cookiecutters will be in this repository.

* We want to make it easier to find a cookiecutter and create a new project. This would encourage community contributions.


Decision
--------

edx-cookiecutter should be the central point for public edx cookiecutters. Most Open edx public cookiecutters should be placed in this repository.

If there is a complelling case why a cookiecutter should be elsewhere, a link to it should be added the edx-cookiecutter/README.rst.


Consequences
------------

All edx cookiecutters should be moved to this repository.

Rejected Alternatives
---------------------

Seperate Repos for frontend and backend cookiecutters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rejected because of the very real possiblity of creating a cookiecutter that deals with both frontend and backend.
