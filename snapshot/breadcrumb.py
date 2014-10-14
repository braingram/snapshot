#!/usr/bin/env python
"""
Breadcrumb creating and parsing code

Contain info about:
    - repo where the file was snapshotted
    - the datetime of the last snapshot
    - the uuid used for the snapshot
    - the archive where the file is stored and it's path
    - sync uuid (for periodic backups)

Breadcrumb per file or subdirectory
"""

import json
import os


class Breadcrumb(object):
    def __init__(self, filename, repo, time, uid, sync):
        self.filename = filename
        self.path = path
        self.repo = repo
        self.time = time
        self.uid = uid
        self.sync = sync

    def resolve_filename(self):
        return os.path.join(self.path, self.filename)

    def resolve_remote(self):
        pass


# TODO write

def find(filename):
    """Find the breadcrumb file for a given local filename"""
    # resolve absolute path of filename
    path = os.path.abspath(filename)
    # recursively check directories (going up) for breadcrumb files
    breadcrumb = None
    breadcrumbfile = None
    post = ''
    while breadcrumbfile is None:
        dname, fname = os.path.split(path)
        if fname == '':
            # hit root
            break
        post = os.path.join(fname, post)
        fn = os.path.join(dname, '.snapshot')
        if os.path.isfile(fn):
            breadcrumbs = load(fn)
            if post in breadcrumbs:
                breadcrumbfile = fn
                breadcrumb = breadcrumbs[post]
        path = dname
    if breadcrumb is None:
        # TODO should this also throw an error
        return None
        #raise Exception("Failed to find breadcrumb for %s" % filename)
    return breadcrumb
    # TODO make the breadcrumb
    #return Breadcrumb(**breadcrumb)


def load(breadcrumb_filename):
    """
    Load breadcrumbs from a breadcrumb file
    """
    with open(breadcrumb_filename, 'r') as f:
        breadcrumbs = json.load(f)
    return breadcrumbs
