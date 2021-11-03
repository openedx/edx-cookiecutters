===================================
How to use the scripts in /scripts
===================================

First, read docs/decisions/0005-store-one-off-scripts.rst to understand why scripts of this nature are stored in this repository.

To apply the changes from a script to your repository
-----------------

1. (for edx.org): Run the cleanup-python-code job in Jenkins with the contents of the script (minus the #!) as the input.
This will automatically create a PR against the repositories you specify in the configuration.

2. Copy the script to the root directory of the repository you wish to update and run it from there using.
This will modify the code in place and you can then commit or create a PR.
