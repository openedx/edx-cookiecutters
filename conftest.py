"""
File configures pytest for this repo
"""


def pytest_ignore_collect(collection_path, config):
    """
    Pytest hook to determine if tests should be collected in `path`.
    """
    if "{" in str(collection_path) and "}" in str(collection_path):
        return True
    return None
