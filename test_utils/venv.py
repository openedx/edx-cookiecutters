"""
Utilities for managing virtualenvs in tests.
"""

import shutil
import subprocess
import sys

def run_in_virtualenv(shell_script):
    """
    Set up virtualenv in current directory and run provided shell script
    with virtualenv active. Virtualenv is deleted after script runs.
    """
    try:
        subprocess.check_call(['virtualenv', '-p', sys.executable, '--clear', '.venv'])
        subprocess.check_call('. .venv/bin/activate; ' + shell_script, env={}, shell=True)
    finally:
        if shutil.rmtree.avoids_symlink_attacks:
            shutil.rmtree('.venv', ignore_errors=True)
