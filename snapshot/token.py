#!/usr/bin/env python
"""
Token creating and parsing code

Contain info about:
    - repo where the file was snapshotted
    - the datetime of the last snapshot
    - the uuid used for the snapshot
    - the archive where the file is stored and it's path
    - sync uuid (for periodic backups)
"""


class Token(object):
    def __init__(self, filename, repo, time, uid):
        self.filename = filename
        self.repo = repo
        self.time = time
        self.uid = uid
