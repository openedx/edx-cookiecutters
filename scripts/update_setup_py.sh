#!/bin/bash

# This script is meant to be run as a one-off to convert old versions of setup.py in existing repositories
# to use the new standard code. If run in the root directory of a library, it will update setup.py and Manifest.in,
# and create a .git/cleanup-python-code-description file with the recommended PR description, comparing old and new versions
# of .egg-info/requires.txt. It will also create a .git/cleanup-python-code-commit-message file with the recommended commit
# message for complying with conventional commit guidelines.
# Date: 11/01/2021

set -eu -o pipefail

script_home=$(dirname -- "${BASH_SOURCE[0]}")

# Need semgrep, and also want to ensure we're only installing it into
# a virtualenv and not unexpectedly into the user's home dir.
"$VIRTUAL_ENV"/bin/pip install semgrep

mkdir -p update-setup-tmp

# generate and store requires.txt file for future comparison
python setup.py bdist_wheel
wheel_dir=$(find . -name *.egg-info | xargs basename)
cp "$(pwd)/$wheel_dir/requires.txt" ./update-setup-tmp/old_requires.txt

# make sure os and re are imported in setup.py, and remove any direct imports of os.path.dirname to avoid conflict
isort --rm "import os.path.dirname" -a "import os re" setup.py

# Need two separate config files, one for each method being overriden,
# in order to avoid collisions when doing code replacement
# --debug will provide additional logging in case things fail
semgrep -a --config="$script_home"/update_setup_py_load_requirements.yaml --debug setup.py
semgrep -a --config="$script_home"/update_setup_py_is_requirement.yaml --debug setup.py

# rerun packaging command to generate new requires.txt file
python setup.py bdist_wheel

# add constraints file to manifest so python tests pass
# note: this will not work for repositories where the constraints file has been changed from requirements/constraints.txt
if [ -s "MANIFEST.in" ] && [ -s "requirements/constraints.txt" ] && [ -z "$(grep 'requirements/constraints.txt' MANIFEST.in)" ]
then
    # bash magic to check if Manifest file does not end with a newline
    if [[ $(tail -c1 "MANIFEST.in" | wc -l) -eq 0 ]]
    then
        echo -e "" >> MANIFEST.in
    fi
    echo "include requirements/constraints.txt" >> MANIFEST.in
fi

# Create PR description for use by cleanup-python-code jenkins job
echo -e "[ARCHBOM-1772](https://openedx.atlassian.net/browse/ARCHBOM-1772)
 Update setup.py to use constraint files when generating requirements files for packaging and distribution.
 PR generated automatically with Jenkins job cleanup-python-code. " > .git/cleanup-python-code-description
echo -e "\nResult of running \`python setup.py bdist_wheel\` before applying fix (in .egg-info/requires.txt): \n" >> .git/cleanup-python-code-description
cat ./update-setup-tmp/old_requires.txt >> .git/cleanup-python-code-description
echo -e "\nResult of running \`python setup.py bdist_wheel\` after applying fix (in .egg-info/requires.txt): \n" >> .git/cleanup-python-code-description
cat "$(pwd)/$wheel_dir/requires.txt" >> .git/cleanup-python-code-description
rm -rf update-setup-tmp
