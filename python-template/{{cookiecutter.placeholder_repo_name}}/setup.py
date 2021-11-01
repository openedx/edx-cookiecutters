#!/usr/bin/env python
"""
Package metadata for {{ cookiecutter.sub_dir_name }}.
"""
import os
import re
import sys

from setuptools import setup

{%- set license_classifiers = ['AGPL 3.0', 'Apache Software License 2.0'] %}


def get_version(*file_paths):
    """
    Extract the version string from the file.

    Input:
     - file_paths: relative path fragments to file with
                   version string
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename, encoding="utf8").read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Requirements will include any constraints from files specified
    with -c in the requirements files.
    Returns a list of requirement strings.
    """
    requirements = {}
    constraint_files = set()

    # groups "pkg<=x.y.z,..." into ("pkg", "<=x.y.z,...")
    requirement_line_regex = re.compile(r"([a-zA-Z0-9-_.]+)([<>=][^#\s]+)?")

    def add_version_constraint_or_raise(current_line, current_requirements, add_if_not_present):
        regex_match = requirement_line_regex.match(current_line)
        if regex_match:
            package = regex_match.group(1)
            version_constraints = regex_match.group(2)
            existing_version_constraints = current_requirements.get(package, None)
            # fine to add constraints to an unconstrained package,
            # raise an error if there are already constraints in place
            if existing_version_constraints and existing_version_constraints != version_constraints:
                raise BaseException(f'Multiple constraint definitions found for {package}:'
                                    f' "{existing_version_constraints}" and "{version_constraints}".'
                                    f'Combine constraints into one location with {package}'
                                    f'{existing_version_constraints},{version_constraints}.')
            if add_if_not_present or package in current_requirements:
                current_requirements[package] = version_constraints

    # read requirements from .in
    # store the path to any constraint files that are pulled in
    for path in requirements_paths:
        with open(path) as reqs:
            for line in reqs:
                if is_requirement(line):
                    add_version_constraint_or_raise(line, requirements, True)
                if line and line.startswith('-c') and not line.startswith('-c http'):
                    constraint_files.add(os.path.dirname(path) + '/' + line.split('#')[0].replace('-c', '').strip())

    # process constraint files: add constraints to existing requirements
    for constraint_file in constraint_files:
        with open(constraint_file) as reader:
            for line in reader:
                if is_requirement(line):
                    add_version_constraint_or_raise(line, requirements, False)

    # process back into list of pkg><=constraints strings
    return [f'{pkg}{version or ""}' for (pkg, version) in sorted(requirements.items())]


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment,
        a URL, or an included file
    """
    return line and line.strip() and not line.startswith(("-r", "#", "-e", "git+", "-c"))

{% if cookiecutter.setup_py_loading_pkg_data == "yes" %}
def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}

{% endif %}
VERSION = get_version('{{ cookiecutter.sub_dir_name }}', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding="utf8").read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst'), encoding="utf8").read()

setup(
    name='{{ cookiecutter.repo_name }}',
    version=VERSION,
    description="""{{ cookiecutter.project_short_description }}""",
    long_description=README + '\n\n' + CHANGELOG,
    author='edX',
    author_email='oscm@edx.org',
    url='https://github.com/edx/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.sub_dir_name }}',
    ],
    include_package_data=True,
    install_requires=load_requirements('requirements/base.in'),
    python_requires=">=3.8",
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='Python edx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        {%- if cookiecutter.requires_django == "yes" %}
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        {%- endif %}
        'Intended Audience :: Developers',
        {%- if cookiecutter.open_source_license == "AGPL 3.0" %}
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        {%- elif cookiecutter.open_source_license == "Apache Software License 2.0" %}
        'License :: OSI Approved :: Apache Software License',
        {%- else %}
        'License :: Other/Proprietary License',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
{%- if cookiecutter.setup_py_keyword_args != "None" %}
    {{ cookiecutter.setup_py_keyword_args }}
{%- endif %}
)
