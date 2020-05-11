1. Layered Cookiecutters
========================

Status
------

Accepted

Context
-------

We duplicate boilerplate files accross our multiple cookiecutters. Historically, its been difficult keeping the same files accross the multiple cookiecutters uptodate. We've decided to try layer cookiecutters. Each layer would have all the basic files that are need for that level of abstraction.

Our approach splits our cookiecutters into two categorites: template, final_use. The template cookiecutters have all the base files, but they do not result in a workable repository output. They need to be used by final_use cookiecutters. The final_use cookiecutters are meant for final output and should result in a working directory for the users.

Clarification: if a subsequent layer needs to modify a file that was created by previous layers, it will need to overwrite the file completely. Changing only segments of a file are thought to be outside the scope of this current work(though doing something like this is recommended in the future).

Our first use case will be our python cookiecutters. "python-template" cookiecutter basic files that should be in each python cookiecutters. It is used by cookiecutter-{python-library, django-app, django-ida}.


Possible negatives
------------------
This might make it difficult to know where to find a particular file since it could have been abstracted into any of the layer.


Consequences
------------


TODO

References
----------

Archived cookiecutters:

* https://github.com/edx/cookiecutter-django-app
* https://github.com/edx/cookiecutter-django-ida
