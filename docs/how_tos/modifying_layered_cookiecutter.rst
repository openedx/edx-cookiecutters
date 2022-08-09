How to modify layered cookiecutters
###################################

First, read docs/decisions/0003-layered-cookiecutter.rst to understand why we are using layers and how they have been implemented.

Adding a new file
*****************

* Search this repo for the file name to see if it already exists in the any template-only or final-output cookiecutters.
* Determine if the file should be shared and added to a template-only cookiecutter layer.
* If the file is added to a template-only cookiecutter, you may need to edit a hook script to remove the file from any final-output cookiecutter that doesn't want it.
* Test all affected final-output cookiecutters.

Modifying a file
****************

* Search the repo for the file name to find all locations of the file.
* Even if the file is not shared across cookiecutters, it may be similar enough to copies of a file where the modification might be needed in multiple locations.
* If the file is shared across cookiecutters, it still may have been overwritten in a final-output cookiecutter. Ensure that your modification is made in all copies where it belongs.
* Test all affected final-output cookiecutters.

Adding a new template-only cookiecutter
***************************************

Think hard before adding a new layer (template-only cookiecutter). They add lots of complexity and it is unlikely to be worth it. We are hoping for a single shared layer to simplify things.

Questions to consider:

* How many files are shared between multiple cookiecutters?
    * if the number is low, layering is probably overkill
* Do the shared files change often?
    * if answer is no, layering might be overkill
* Would new layering make it hard to reason where a file would be located?
    * Don't add the layer and just pay the cost of having duplicated files

Layering only makes sense where there are many shared files and they change often.
