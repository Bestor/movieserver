#!/usr/bin/env python
'''
(C) Copyright 2013-2015 Hewlett Packard Enterprise Development LP
'''

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    os.environ["DJANGO_LOG_FILE"] = "datastore_cli"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movieserver.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
