====================
Layered Cookiecutter
====================

To learn more about why we are using layered cookiecutters, see the decision 0003-layered-cookiecutter.rst.

Cookiecutters using this approach
---------------------------------
- cookiecutter-django-app
- cookiecutter-django-ida
- cookiecutter-python-library

How it works
------------

Cookiecutter allows you to define {pre, post}_gen_project.py files that run at beginning of the folder creation and at end of folder creation. 

For the layered approach, we use the post_gen_project.py file to add the bottom layers to the output folder. The script creates each layer in folder(s) called: placeholder_repo_name_#(num based on how many templates are created) and then moves all resulting files to the correct location. 

Emphasis: the layers are placed in high to low order, so the topmost(the most specific) layer is placed first. Each subsequent layer adds files without replace, so if the file already exists, it is not replaced by file from bottom layer. 

For example: for cookiecutter-django-app(CDA), the CDA specific files/folders are created first, then files from django-template, and then finally files from python-template.

Look at cookiecutter-django-app/hooks/post_gen_project.py for example of top to bottom layering and for functions to do the moves correctly.

When to using this approach
---------------------------

- How many files are shared between multiple cookiecutters?
    - if the number is low, layering might be overkill
- Do the shared files change often?
    - if answer is no, layering might be overkill
- If the suggested layering makes it hard to reason where a file would be located
    - Rethink your layering or don't use layering and just pay the cost of having duplicated files -> duplication is a smaller sin than complicated file structure

Layering only makes sense if there are many shared files and they change often.

What was tried during experimentation
-------------------------------------
Initially, we tried to layer from bottom up by doing most of the layering in pre_gen_project.py file. This failed cause cookiecutter folder creation does allow overlaying a folder from higher layer. If a folder {{ cookiecutter.name }} already exists from a previous layer, the cookiecutter errors out. This cookiecutter behavior resulted in us moving the layering to post_gen_project.py, which results in top-to-bottom approach to layering.
