1. Layered Cookiecutters
========================

Status
------

Accepted

Context
-------

* We duplicate boilerplate files across our multiple cookiecutters.
* Historically, its been difficult keeping the same files across the multiple cookiecutters uptodate. 

Decision
--------

We've decided to try layer cookiecutters. Each layer would have all the basic files that are need for its level of abstraction.

Our approach relies on two categories of cookiecutters:
* *template-only*: These cookiecutters have the reusable base files, but they do not result in a workable repository output.

* *final-output*: These cookiecutters produce the final output, resulting in a working directory.

The template-only cookiecutters are used by final-output cookiecutters to create necessary base files. 

Note: The initial implementation only allows layers to use files created by a previous layer as-is, or overwrite it completely.

Examples of our layered cookiecutters would look like::

    cookiecutter-python-library---|
    cookiecutter-django-app-------|
    cookiecutter-django-ida-------|
                          python-template

Consequences
------------

Possible negatives
~~~~~~~~~~~~~~~~~~

This might make it difficult to know where to find a particular file since it could have been abstracted into any of the layer.

Note: Cookiecutter is not designed for the layered approach, so some hacking is required.



TODO

References
----------

Archived cookiecutters:

* https://github.com/edx/cookiecutter-django-app
* https://github.com/edx/cookiecutter-django-ida
