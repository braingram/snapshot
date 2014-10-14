#!/usr/bin/env python
"""
Archives are specialized directories

They need to contain info about:
    - name and uuid
    - plugin used to compute filenames

These basically just transform filenames
"""


class Archive(object):
    def resolve_remote(self, filename):
        pass
