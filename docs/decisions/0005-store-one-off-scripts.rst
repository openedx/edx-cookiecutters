5. Where to put one-off update scripts?
============================================

Status
------

Accepted


Context
-------
* Sometimes we want to make changes to a cookiecutter and have those changes applied retroactively to all repositories that were created with it.

* We don't currently have a location to store scripts that can be used to apply these changes to individual repositories


Decision
--------

Scripts used to update old cookiecutter code to reflect new changes will live in the scripts/ directory of this repository.


Rejected Alternatives
---------------------

Use @edx/repo-tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Rejected because repo-tools is more suited to creating CLI commands that may need to be run multiple times to
gather information or make regular updates.


Use @edx/jenkins-job-dsl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This was proposed as a containing repository since the cleanup-python-code job configured there can and will probably
often be used to run these kinds of bash scripts against multiple repositories at once. It was rejected because
the scripts would be far removed from the code they are intended to update and thus difficult to find and/or understand.

