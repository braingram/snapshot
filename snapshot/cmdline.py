#!/usr/bin/env python
"""
Command line processing

Used to process command line arguments

basic usage: snapshot <files/uuids>

    -s --status
        get status of file
    -r --recover
        recover instead of upload
    -d --date
        apply (or use) a datetime
    -R --repository
        name of repository

sync arguments
    -i --interval: hour,day,week,month
        sync interval
    -b --bidirectional
        do a bidirectional sync

archive arguments
    -a --archive
        archive name
    -c --clone
        clone an archive (grab the whole thing)
"""

import argparse
import os
import time
import uuid


from . import breadcrumb


def build_argument_parser():
    # TODO add help
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'files', nargs='*',
        help="")
    parser.add_argument(
        '-s', '--status', action='store_true', default=False,
        help="get the status of a file")
    parser.add_argument(
        '-r', '--recover', default=False, const=True, nargs="?",
        help="recover a file or files")
    parser.add_argument(
        '-f', '--force', action='store_true', default=False,
        help="force overwrite of files on recovery")
    parser.add_argument(
        '-d', '--date', default=False, const=True, nargs="?",
        help="")
    parser.add_argument(
        '-R', '--repository', default='', nargs=1,
        help="repository for backup/recovery")
    # sync arguments
    parser.add_argument(
        '-i', '--interval', default=False, nargs=1,
        choices=["hour", "day", "week", "month"],
        help="")
    parser.add_argument(
        '-b', '--bidirectional', action='store_true', default=False,
        help="")
    # archive arguments
    parser.add_argument(
        '-a', '--archive', default=False, nargs=1,
        help="")
    parser.add_argument(
        '-c', '--clone', action='store_true', default=False,
        help="")
    return parser


def status(ns):
    """Process a status request

    Status requests only need the local info
    no need to load repo, archive, or sync info"""
    # TODO logging
    print 'status', vars(ns)
    for fn in ns.files:
        # then it's a filename
        mtime = os.path.getmtime(fn)
        print("{}".format(fn))
        print("\tmodified: {}".format(time.ctime(mtime)))
        bc = breadcrumb.find(fn)
        if bc is None:
            last_sync = None
            print("\tsynced: never")
            continue
        else:
            last_sync = bc.time
            print("\tsynced: {}".format(time.ctime(last_sync)))
        # TODO is it part of an archive?
        # TODO is this periodically synced?
        pass


def backup(ns):
    """Process a backup request
    Might be an archive

    all args should be filenames
    """
    print 'backup', vars(ns)
    for fn in ns.files:
        # find if files are already tracked (have breadcrumbs)
        #  if so, use those uuids
        #  if not, generate a new uuid
        # is this an archive?
        # if so, create an Archive to resolve filenames
        # resolve local and remote filenames
        # create rsync command
        # run it
        pass
    pass


def recover(ns):
    """Process a recover request
    Might be an archive

    if -r is a string and uuid then there should be 1 arg
    if -r is a string and a filename, there might not be an arg
      the previous could be ambiguous, use -f (force option) to resolve
    if -r is True, then there should be filenames (NOT uuids)
    """
    print 'recover', vars(ns)
    # if r is a uuid
    pass


def sync(ns):
    """Process a sync request

    Synchronize a directory

    all args should be files
    """
    print 'sync', vars(ns)
    pass


def clone(ns):
    """Process a clone request
    """
    print 'clone', vars(ns)
    pass


def make_uuid(fn):
    """
    Check if fn is a uuid
    if it is, then create a uuid.UUID
    """
    if os.path.exists(fn):
        return fn
    else:  # TODO make this check more robust
        return uuid.UUID(fn)


def run(args=None):
    parser = build_argument_parser()
    ns = parser.parse_args(args)
    #ns.files = map(make_uuid, ns.files)
    # TODO verify command line arguments
    # if -s, then status, process and exit
    if ns.status:
        return status(ns)
    # if -i, then sync, process and exit
    if ns.interval:
        return sync(ns)
    # if -c, then clone, process and exit
    if ns.clone:
        return clone(ns)
    # if -r, then recover, process and exit
    if ns.recover:
        return recover(ns)
    # else, process backup and exit
    return backup(ns)
