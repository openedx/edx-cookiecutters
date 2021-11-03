#!/bin/bash

# This script is meant to be run as a one-off to convert old versions of setup.py in existing repositories
# to use the new standard code. If run in the root directory of a library, it will update setup.py and Manifest.in,
# and create a .git/cleanup-python-code-description file with the recommended PR description, comparing old and new versions
# of .egg-info/requires.txt. It will also create a .git/cleanup-python-code-commit-message file with the recommended commit
# message for complying with conventional commit guidelines.
# Date: 11/01/2021

mkdir update-setup-tmp;

# generate and store requires.txt file for future comparison
python setup.py bdist_wheel;
wheel_dir=$(find . -name *.egg-info | xargs basename);
cp "$(pwd)/$wheel_dir/requires.txt" ./update-setup-tmp/old_requires.txt;

# make sure os and re are imported in setup.py, and remove any direct imports of os.path.dirname to avoid conflict
isort --rm "import os.path.dirname" -a "import os re" setup.py;

# generate config files for semgrep. need to create two separate config files, one for each method being overriden,
# in order to avoid collisions when doing code replacement
echo -e "rules:
- id: fix-load_requirements
  languages:
    - python
  pattern: |
    def load_requirements(...):
        ...
  severity: INFO
  message: Updating load_requirements method with new standard
  fix: |
    # UPDATED VIA SEMGREP - if you need to remove/modify this method remove this line and add a comment specifying why.
    def load_requirements(*requirements_paths):
        \"\"\"
        Load all requirements from the specified requirements files.

        Requirements will include any constraints from files specified
        with -c in the requirements files.
        Returns a list of requirement strings.
        \"\"\"
        requirements = {}
        constraint_files = set()

        # groups \"my-package-name<=x.y.z,...\" into (\"my-package-name\", \"<=x.y.z,...\")
        requirement_line_regex = re.compile(r\"([a-zA-Z0-9-_.]+)([<>=][^#\s]+)?\")

        def add_version_constraint_or_raise(current_line, current_requirements, add_if_not_present):
            regex_match = requirement_line_regex.match(current_line)
            if regex_match:
                package = regex_match.group(1)
                version_constraints = regex_match.group(2)
                existing_version_constraints = current_requirements.get(package, None)
                # it's fine to add constraints to an unconstrained package, but raise an error if there are already
                # constraints in place
                if existing_version_constraints and existing_version_constraints != version_constraints:
                    raise BaseException(f'Multiple constraint definitions found for {package}:'
                                        f' "{existing_version_constraints}" and "{version_constraints}".'
                                        f'Combine constraints into one location with {package}'
                                        f'{existing_version_constraints},{version_constraints}.')
                if add_if_not_present or package in current_requirements:
                    current_requirements[package] = version_constraints

        # process .in files and store the path to any constraint files that are pulled in
        for path in requirements_paths:
            with open(path) as reqs:
                for line in reqs:
                    if is_requirement(line):
                        add_version_constraint_or_raise(line, requirements, True)
                    if line and line.startswith('-c') and not line.startswith('-c http'):
                        constraint_files.add(os.path.dirname(path) + '/' + line.split('#')[0].replace('-c', '').strip())

        # process constraint files and add any new constraints found to existing requirements
        for constraint_file in constraint_files:
            with open(constraint_file) as reader:
                for line in reader:
                    if is_requirement(line):
                        add_version_constraint_or_raise(line, requirements, False)

        # process back into list of pkg><=constraints strings
        return [f'{pkg}{version or \"\"}' for (pkg, version) in sorted(requirements.items())]" > ./update-setup-tmp/load_requirements.yaml;
echo -e "rules:
- id: fix-is_requirement
  languages:
    - python
  pattern: |
    def is_requirement(...):
        ...
  severity: INFO
  message: Updating is_requirement method with new standard
  fix: |
    # UPDATED VIA SEMGREP - if you need to remove/modify this method remove this line and add a comment specifying why
    def is_requirement(line):
        \"\"\"
        Return True if the requirement line is a package requirement.

        Returns:
            bool: True if the line is not blank, a comment,
            a URL, or an included file
        \"\"\"
        return line and line.strip() and not line.startswith(('-r', '#', '-e', 'git+', '-c'))" > ./update-setup-tmp/is_requirement.yaml;

# --debug will provide additional logging in case things fail
semgrep -a --config=./update-setup-tmp/load_requirements.yaml --debug setup.py;
semgrep -a --config=./update-setup-tmp/is_requirement.yaml --debug setup.py;

# rerun packaging command to generate new requires.txt file
python setup.py bdist_wheel;

# add constraints file to manifest so python tests pass
# note: this will not work for repositories where the constraints file has been changed from requirements/constraints.txt
if [ -s "MANIFEST.in" ] && [ -s "requirements/constraints.txt" ]
then
    echo "include requirements/constraints.txt" >> MANIFEST.in
fi

# Create PR description for use by cleanup-python-code jenkins job
echo -e "[ARCHBOM-1772](https://openedx.atlassian.net/browse/ARCHBOM-1772)
 Update setup.py to use constraint files when generating requirements files for packaging and distribution.
 PR generated automatically with Jenkins job cleanup-python-code. " > .git/cleanup-python-code-description;
echo -e "\nOld requirements file: \n" >> .git/cleanup-python-code-description;
cat ./update-setup-tmp/old_requires.txt >> .git/cleanup-python-code-description;
echo -e "\n New requirements file: \n" >> .git/cleanup-python-code-description;
cat "$(pwd)/$wheel_dir/requires.txt" >> .git/cleanup-python-code-description;
rm -rf update-setup-tmp
