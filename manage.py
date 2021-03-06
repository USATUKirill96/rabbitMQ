#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import sys

import environ

PROJECT_DIR = environ.Path(__file__) - 1
env = environ.Env()
env.read_env(env_file=PROJECT_DIR(".env"))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
