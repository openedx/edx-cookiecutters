This is a cookiecutter template for new XBlocks.

It enables creation of the XBlock repository as well as a Dockerfile for building and running your XBlock in the xblock-sdk workbench.

To create a new XBlock using this cookiecutter template, first make sure you have cookiecutter installed.

Then run::

        $ cookiecutter https://github.com/edx/cookiecutter-xblock.git

Enter the short name and primary class name of your new XBlock when prompted.

To see your new XBlock in action, build and run a Docker image containing it::

        $ make dev.run

Your XBlock should now be available at http://localhost:8000

As a next step, you can pick up the XBlock tutorial at the `Customizing Your XBlock`_ section.

.. _Customizing Your XBlock: http://edx.readthedocs.io/projects/xblock-tutorial/en/latest/customize/index.html
