Cookiecutter default branch
===========================


Status
------

Accepted

Context
-------

Github now sets default branch of each new repository to main. And the software industry as a whole has been moving towards default branch name flexibility and away from naming the default branch "master".

Decision
--------

It as decided to change name of default branches to "main" for all new repositories created with cookiecutters.

Consequences
------------

Lots of tooling in Open edX ecosystem assumes the default branch has the name "master". This decision might result in necessary changes to our tooling to accommodate multiple default branch names.
