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

edx-cookiecutters tooling will assume new repositories created using the cookiecutters will have the default name of "main".

As an additional nudge in this direction, it was decided not to provide an option that defaults to "main". If you need to use "master", you will need to manually rename references.

Consequences
------------

- Using "main" for a new repository for a library should be safe at this time, but using it for a new IDA may required additional changes to support it.

- Much of our tooling may need to be updated to handle both "main" and "master" for some transitional period.

  - Continuing to use "master" for a new repository would require manual changes after using the cookie-cutter.
