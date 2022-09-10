1. Combined Cookiecutter Repo
#############################

Status
******

Accepted

Context
*******

There were multiple Python cookiecutter repositories with lots of overlap, and it was difficult to keep even one always up to date.

Some examples:
* cookiecutter-django-app
* cookiecutter-django-ida
* cookiecutter-xblock

Decision
********

Move the edx's public python cookiecutters into edx-cookiecutters repository. This repository might one day be a place for all of edx's cookiecutters, but this decision is only relevant to our python cookiecutters.

Consequences
************

Find all of edx's python cookiecutters, move them to this repositories, and archive the previous repositories.

References
**********

Archived cookiecutters:

* https://github.com/openedx/cookiecutter-django-app
* https://github.com/openedx/cookiecutter-django-ida
* https://github.com/openedx/cookiecutter-xblock
