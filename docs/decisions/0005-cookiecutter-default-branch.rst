Cookiecutter default branch
===========================


Status
------

Accepted

Context
-------

Github now sets default branch of each new repository to main. And the software industry as a whole has been moving towards default branch name flexibility and away from naming the default branch "master".

There are number of places in edx-cookiecutters where we make assumption about the name of the default branch. Until now, we assumed that name was "master".

Decision
--------

edx-cookiecutters tooling will assuming new repositories created using the cookiecutters will have the default name of "main".

Consequences
------------

Lots of tooling in Open edX ecosystem assumes the default branch has the name "master". This decision might result in necessary changes to our tooling to accommodate multiple default branch names.
