====================
Layered Cookiecutter
====================

In an attempt to decrease dupliciation, we are attempting a layered aproach with cookiecutters.

Cookiecutter is not designed for the layered approach, so some hacking is required.


How it works
------------

Cookiecutter allows you to define a {pre, post}_gen_project.py files that run at beginning of the folder creation and at end of folder creation. 

For the layered approach, we use the post_gen_project.py file to add the bottom layers to the output folder. Emphasis: the layers are placed in high to low order, so the topmost(the most specific) layer is placed first. Each subsequent layer adds files without replace, so if the file already exists, it is not replaced by file from bottom layer. 

For example: for cookiecutter-django-app(CDA), the CDA specific files/folders are created first, then files from django-template, and then finally files from python-template.

Look at cookiecutter-django-app/hooks/post_gen_project.py for example.