#!/usr/bin/env python
"""
A django manage.py file.

It eases running django related commands with the correct settings already
imported.
"""
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "translation_settings"
    )

    execute_from_command_line(sys.argv)
