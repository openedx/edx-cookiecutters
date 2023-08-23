"""
File configures pytest for this repo
"""


def pytest_ignore_collect(path, config):
    """
    Pytest hook to determine if tests should be collected in `path`.
    """
    if "{" in str(path) and "}" in str(path):
        return True
    return None
