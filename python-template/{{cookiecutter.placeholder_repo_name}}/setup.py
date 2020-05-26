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
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.

    Returns:
        list: Requirements file relative path strings
    """
    requirements = set()
    for path in requirements_paths:
        requirements.update(
            line.split('#')[0].strip() for line in open(path).readlines()
            if is_requirement(line.strip())
        )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement.

    Returns:
        bool: True if the line is not blank, a comment, a URL, or an included file
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))

{%- if cookiecutter.setup_py_loading_pkg_data == "yes" %}


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
{%- endif %}

VERSION = get_version('{{ cookiecutter.sub_dir_name }}', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
CHANGELOG = open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst')).read()

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
    python_requires=">=3.5",
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    zip_safe=False,
    keywords='Python edx',
    classifiers=[
        'Development Status :: 3 - Alpha',
        {%- if cookiecutter.supports_django == "yes" %}
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
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
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.8',
    ],
{%- if cookiecutter.setup_py_keyword_args != "None" %}
    {{ cookiecutter.setup_py_keyword_args }}
{%- endif %}
)
