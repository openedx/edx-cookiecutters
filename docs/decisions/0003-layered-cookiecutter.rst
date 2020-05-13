1. Layered Cookiecutters
========================

Status
------

Accepted

Context
-------

* We duplicate boilerplate files across our multiple cookiecutters.
* Historically, it's been difficult keeping the same files across the multiple cookiecutters up-to-date. 

Decision
--------

We've decided to try layering cookiecutters. Each layer would have all the basic files that are needed for its level of abstraction.

Note: In order to add clarity over flexibility, we will only allows layers to use files created by a previous layer as-is, or overwrite it completely.  Partial file overrides is not permitted.

To learn more about the layering approach, see the docs/how_tos/layered_cookicutter.rst.


Consequences
------------

Possible negatives
~~~~~~~~~~~~~~~~~~

This might make it difficult to know where to find a particular file since it could have been abstracted into any of the layers. 

To offset this, it's recommended that there be only one template layer at most. If there are multiple layers, they should be distinct enough for someone to reason where a file should be.

Note: Cookiecutter is not designed for the layered approach, so some hacking is required.


References
----------

Archived cookiecutters:

* https://github.com/edx/cookiecutter-django-app
* https://github.com/edx/cookiecutter-django-ida
