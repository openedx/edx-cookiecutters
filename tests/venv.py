"""
Utilities for managing virtualenvs in tests.
"""

import shutil
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


def _use_virtualenv(venv_path, shell_script):
    """Run `shell_script` in the already-made virtualenv at `venv_path`."""
    subprocess.check_call(f'. {venv_path}/bin/activate; {shell_script}', env={}, shell=True)


def run_in_virtualenv(shell_script):
    """
    Create a virtualenv and run the provided shell script in it.

    The virtualenv is created in the current directory and deleted after
    the script runs.
    """
    with TemporaryDirectory() as parent_dir:
        pip_txt = shutil.move("requirements/pip.txt", parent_dir)
        venv_path = str(Path(parent_dir) / 'venv')
        try:
            subprocess.check_call(['virtualenv', '-p', sys.executable, '--clear', venv_path])
            _use_virtualenv(venv_path, f'pip install -qr {pip_txt}')
            _use_virtualenv(venv_path, shell_script)
        finally:
            if shutil.rmtree.avoids_symlink_attacks:
                shutil.rmtree(venv_path, ignore_errors=True)
