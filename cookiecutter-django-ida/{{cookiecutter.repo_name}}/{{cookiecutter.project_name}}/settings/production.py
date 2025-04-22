"""Settings for production use."""

from os import environ

import yaml

from {{cookiecutter.project_name}}.settings.base import *  # pylint: disable=wildcard-import
from {{cookiecutter.project_name}}.settings.utils import get_env_setting

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

# Keep track of the names of settings that represent dicts. Instead of overriding the values in base.py,
# the values read from disk should UPDATE the pre-configured dicts.
DICT_UPDATE_KEYS = ('JWT_AUTH',)

# This may be overridden by the YAML in {{cookiecutter.project_name}}_CFG,
# but it should be here as a default.
MEDIA_STORAGE_BACKEND = {}
FILE_STORAGE_BACKEND = {}

if '{{cookiecutter.project_name|upper}}_CFG' in environ:
    CONFIG_FILE = get_env_setting('{{cookiecutter.project_name|upper}}_CFG')
    with open(CONFIG_FILE, encoding='utf-8') as f:
        config_from_yaml = yaml.safe_load(f)

        # Remove the items that should be used to update dicts, and apply them separately rather
        # than pumping them into the local vars.
        dict_updates = {key: config_from_yaml.pop(key, None) for key in DICT_UPDATE_KEYS}

        for key, value in dict_updates.items():
            if value:
                vars()[key].update(value)

        vars().update(config_from_yaml)

        # Unpack the media and files storage backend settings for django storages.
        # These dicts are not Django settings themselves, but they contain a mapping
        # of Django settings.
        vars().update(FILE_STORAGE_BACKEND)
        vars().update(MEDIA_STORAGE_BACKEND)

# Must be generated after loading config YAML because LOGGING_FORMAT_STRING might be overridden.
LOGGING = get_logger_config(format_string=LOGGING_FORMAT_STRING)

DB_OVERRIDES = {
    "PASSWORD": environ.get('DB_MIGRATION_PASS', DATABASES['default']['PASSWORD']),
    "ENGINE": environ.get('DB_MIGRATION_ENGINE', DATABASES['default']['ENGINE']),
    "USER": environ.get('DB_MIGRATION_USER', DATABASES['default']['USER']),
    "NAME": environ.get('DB_MIGRATION_NAME', DATABASES['default']['NAME']),
    "HOST": environ.get('DB_MIGRATION_HOST', DATABASES['default']['HOST']),
    "PORT": environ.get('DB_MIGRATION_PORT', DATABASES['default']['PORT']),
}

for override, value in DB_OVERRIDES.items():
    DATABASES['default'][override] = value
