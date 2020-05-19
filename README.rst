=================
edx-cookiecutters
=================

This repository holds most of the Open edx public python cookiecutters.

Available cookiecutters
------------------------

- cookiecutter-django-ida
    - intended for new edX independently deployable apps (IDAs)
- cookiecutter-django-app
    - for creating reusable Django packages (installable apps)
- cookiecutter-python-library
    - for creating a python package that follows edx standards
- cookiecutter-xblock
    - for createing a XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.


Cookiecutters using layered apporach
------------------------------------

- cookiecutter-python-library
- cookiecutter-django-app
- cookiecutter-django-ida

If you are updating above cookiecutters, please see docs/decisions/0003-layered-cookiecutter.rst and docs/how_tos/modifying_layered_cookiecutter.rst


Using a cookiecutter
--------------------

Commands::

    $ make requirements  # from inside edx-cookiecutter repo
    # move to location where you want to create a new repo
    # Replace <COOKIECUTTER-NAME> with one of available cookiecutters
    $ cookiecutter https://github.com/edx/edx-cookiecutters.git --directory <COOKIECUTTER-NAME>


Local Debugging of cookiecutters
--------------------------------

To debug locally, set the env variable EDX_COOKIECUTTER_ROOTDIR to the root of the edx-cookiecutters repository. For example, from inside /edx-cookiecutters, use::

    $ export EDX_COOKIECUTTER_ROOTDIR="/edx-cookiecutters"


 Without this environment variable, the cookiecutter will pull templates from github, which will not have your local changes on them.

Decisions
---------

See docs/decisions/0003-layered-cookiecutter.rst for details on layering cookiecutters to share boilerplate files.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

The code in this repository is licensed under the Apache Software License 2.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.


Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

If you're having trouble, we have discussion forums at
https://discuss.openedx.org where you can connect with others in the community.

Our real-time conversations are on Slack. You can request a `Slack
invitation`_, then join our `community Slack team`_.

For more information about these options, see the `Getting Help`_ page.

.. _Slack invitation: https://openedx-slack-invite.herokuapp.com/
.. _community Slack team: http://openedx.slack.com/
.. _Getting Help: https://openedx.org/getting-help
.. _`file an issue`: https://github.com/edx/edx-cookiecutters/issues
.. _`tox`: https://tox.readthedocs.io/en/latest/
