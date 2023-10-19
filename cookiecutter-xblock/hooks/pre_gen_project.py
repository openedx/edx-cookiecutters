"""
Verify that project info is valid.
"""
import sys

if '{{ cookiecutter.package_name }}' == 'xblock':  # pylint: disable=comparison-of-constants
    print('ERROR: xblock is not a valid Python module name!')
    sys.exit(1)

if '{{ cookiecutter.i18n_namespace }}' == '{{ cookiecutter.package_name }}':  # pylint: disable=comparison-of-constants
    print('ERROR: (i18n_namespace) cannot be the same as (package_name)!')
    sys.exit(1)
