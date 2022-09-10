This is a cookiecutter template for new XBlocks.

It enables creation of the XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.

To create a new XBlock using this cookiecutter template, follow the instructions found in edx-cookiecutter's `readme`_.

.. _readme: https://github.com/openedx/edx-cookiecutters/blob/master/README.rst


Enter the short name and primary class name of your new XBlock when prompted.

To see your new XBlock in action, build and run a Docker image containing it::

        $ make dev.run

Your XBlock should now be available at http://localhost:8000

As a next step, you can pick up the XBlock tutorial at the `Customizing Your XBlock`_ section.

.. _Customizing Your XBlock: https://edx.readthedocs.io/projects/xblock-tutorial/en/latest/customize/index.html
