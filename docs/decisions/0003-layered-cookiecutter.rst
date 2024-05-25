1. Layered Cookiecutters
########################

Status
******

Accepted

Context
*******

* We duplicate boilerplate files across our multiple cookiecutters.
* Historically, it's been difficult keeping the same files across the multiple cookiecutters up-to-date.

Decision
********

We will layer cookiecutters in order to share boilerplate code. This approach requires two categories of cookiecutters:

* *template-only*: These cookiecutters contain files used as boilerplate across other cookiecutters, but do not result in a workable repository output.
* *final-output*: These cookiecutters produce the final output, resulting in a working directory.

When a cookiecutter gets boilerplate from another layer, it can either:

  * Use the file as-is, or
  * Overwrite the entire file, or
  * Discard the unneeded file.
  * For clarity over flexibility, partial overwrites of files is not allowed without an ADR explaining why the exception is required.

Here is an example of 3 final-output cookiecutters layered with one shared template-only cookiecutter::

    cookiecutter-python-library---|
    cookiecutter-django-app-------|
    cookiecutter-django-ida-------|
                          python-template

Implementation Details
======================

Cookiecutter allows you to define ``pre_gen_project.py`` and ``post_gen_project.py`` files that run at the beginning and end of folder creation.

For the layered approach, we use the ``post_gen_project.py`` file to add the bottom layers to the output folder. The script creates each layer in folder(s) called: ``placeholder_repo_name_#`` (num based on how many template-only cookiecutters are used) and then moves all resulting files to the correct location.

The layers are copied in high to low order, so the top-most (the most specific) layer is placed first. Each subsequent layer adds files without replace, so if a file already exists, it would not be replaced by a file from the bottom layer.

For example: for cookiecutter-django-ida (CDI), the CDI specific files/folders are created first. To avoid conflicts, ``post_gen_project.py`` uses the python-template to create files/folders in ``placeholder_repo_name_0``. After file creation, the files are moved to the correct location. Finally, CDI can delete any unnecessary files created by python-template.

Consequences
************

Possible drawbacks
==================

This approach of layers and shared files may make it difficult to know where to find a particular file since it could have been abstracted into any of the layers.

It also may make it difficult to know what final-output cookiecutters will be affected by a template-only change.

To offset this, it is recommended that there be only one template-only layer. If there are multiple layers, they should be distinct enough for someone to reason where a file would be.

Additionally, the decision to not allow partial file overwrites should help someone more quickly find the correct location for a change.

Rejected Alternatives
*********************

No sharing of boilerplate code
==============================

As noted in the `Context`_, we had a maintenance problem when not sharing boilerplate code. It remains to be seen if the potential drawbacks of this approach will outweigh the drawbacks of the original maintenance problem.

Failed alternative layering implementation
==========================================

Initially, we tried to layer from bottom up by doing most of the layering in pre_gen_project.py file. This failed because cookiecutter folder creation does allow overlaying a folder from a higher layer. If a folder ``{{ cookiecutter.name }}`` already exists from a previous layer, the cookiecutter would error out. This cookiecutter behavior resulted in us moving the layering to ``post_gen_project.py``, which results in a top-to-bottom approach to layering.

References
**********

Archived cookiecutters:

* https://github.com/edx-unsupported/cookiecutter-django-app
* https://github.com/edx-unsupported/cookiecutter-django-ida
