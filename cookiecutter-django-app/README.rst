Cookiecutter Django Package
###########################

A `cookiecutter`_ template for creating reusable Django packages (installable apps) quickly.
If you're creating a standalone Django service, you should probably use
`cookiecutter-django-ida`_ instead.


.. _cookiecutter: https://cookiecutter.readthedocs.org/en/latest/index.html
.. _cookiecutter-django-ida: https://github.com/openedx/edx-cookiecutters/tree/master/cookiecutter-django-ida


Features
********

* Sane setup.py for easy PyPI registration/distribution
* Github Actions for CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* AGPL licensed by default
* Basic model generation

Usage
*****

First, create your empty repo on Github (in our example below, we would call
it ``blogging_for_humans``) and set up your virtual environment with your
favorite method.  If you are an edX employee, request a new repo in the
``edx`` organization by submitting an ITSUPPORT ticket.  Details are in the
`How to request a new GitHub repo`_ wiki page. This ticket should also
request that GitHub Actions and Codecov be enabled for the new repository.

.. _How to request a new GitHub repo: https://openedx.atlassian.net/wiki/pages/viewpage.action?pageId=70385719

**Note**: Your project will be created with a ``README.rst`` file containing a Pypi
badge, a GitHub Actions CI badge, and a link to documentation on `readthedocs.org`_. You
don't need to have these accounts set up before using Cookiecutter or
``cookiecutter-django-app``.

To create a project using this cookiecutter, follow the instructions found in edx-cookiecutter's `readme`_.

.. _readthedocs.org: https://readthedocs.org
.. _readme: https://github.com/openedx/edx-cookiecutters/blob/master/README.rst


After the new folder is created, you will need to:

Enter the project and take a look around:

.. code-block:: bash

    cd blogging_for_humans/
    ls

Generate a virtualenv and generate requirements files with dependencies
pinned to current versions (make sure you're using pip 9.0.2+ and Python 3.8):

.. code-block:: bash

    mkvirtualenv Blogging-for-humans
    make upgrade

Create a GitHub repo and push it there:

.. code-block:: bash

    git init
    git add .
    git commit -m "first awesome commit"
    git remote add origin git@github.com:edx/blogging_for_humans.git
    git push -u origin master

Now take a look at your repo. Awesome, right?

Address TODOs
=============

Look around in the new repo for sections marked `TODO`.  Here are a few known
places where they may appear:

* ``openedx.yaml``: Various OEP states need to be updated.  See `OEP-2 - Repository Metadata`_ for more information.
* ``{{cookiecutter.app_name}}/models.py``: If you specified any models to generate, the various docstrings need to be filled in, and PII annotations need to be added.  See `OEP-30 - PII Markup and Auditing`_ for more information on PII annotations.
* ``tests/test_models.py``: Fill in docstrings here too.

.. _OEP-2 - Repository Metadata: https://docs.openedx.org/projects/openedx-proposals/en/latest/archived/oep-0002-bp-repo-metadata.html
.. _OEP-30 - PII Markup and Auditing: https://docs.openedx.org/projects/openedx-proposals/en/latest/architectural-decisions/oep-0030-arch-pii-markup-and-auditing.html

Finally, it's time to write the code!!!


Running Tests
=============

Code has been written, but does it actually work? Let's find out!

.. code-block:: bash

    workon <YOURVIRTUALENV>
    (myenv) $ make requirements
    (myenv) $ make test-all


GitHub Checks
=============

On your first PR, ensure Github Actions and Codecov checks are running.

If Github Actions are not running, you can look at their state here https://github.com/openedx/edx-cookiecutters/actions

If Codecov is not running, complete an ITSUPPORT ticket.

Register on PyPI
================

Once you have at least a prototype working and tests running, it's time to
register the application on PyPI.

You should use PyPa's official Github action: https://github.com/marketplace/actions/pypi-publish
to publish your package to PyPi in your Github workflow file you'd need to add the following

.. code-block:: yaml

    - name: Publish the package to PyPi
      uses: pypa/gh-action-pypi-publish@master
      with:
        user: __token__
        password: ${{ secrets.PYPI_UPLOAD_TOKEN }}


``PY_UPLOAD_TOKEN`` is available organization-wide Open edX repos via Github secrets.

Releasing on PyPI
=================

Time to release a new version? Update the version number in the application
module's ``__init__.py`` file, update ``CHANGELOG.rst`` accordingly, and run:

.. code-block:: bash

    python setup.py tag

and create a Github release with a new tag, your GitHub workflow should automatically run once a new release is
created and should publish the package to PyPi.

Add to Django Packages
======================

Once you have a release, and assuming you have an account there, just go to https://www.djangopackages.com/packages/add/ and add it there.
