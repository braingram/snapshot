#!/usr/bin/env python
"""
File repositories are where files are stored.
These can contain files, directories, and archives.

Repos need to contain info about:
    - remote location
    - how remotes are accessed
    - prefix
    - archives (and plugins, probably keep separate)
    - uuid lookups
    - rsync options

These take two filenames or uuids and run an rsync command
"""

import uuid


class Repository(object):
    def resolve_local(self, filename):
        pass

    def resolve_remote(self, filename):
        pass
