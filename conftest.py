import pytest
import pdb
import os

import sys
sys.path.append(os.path.join(os.getcwd(),"cookiecutter-django-app"))
sys.path.append(os.path.join(os.getcwd(),"cookiecutter-django-ida"))

def pytest_ignore_collect(path, config):
    """
    pytest hook that determines if pytest looks at specific file to collect tests
    if repo_health is set to true:
        only tests in test files with "repo_state_checks" in their path will be collected
    """
    if "{" in str(path) and "}" in str(path):
        return True
    return False