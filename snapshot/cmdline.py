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
        '-r', '--recover', action='store_true', default=False,
        help="recover a file or files")
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
    # TODO verify command line arguments
    # TODO TODO TODO TODO
    print 'status', vars(ns)
    # args are either local filenames or uuids
    # load token
    # check file
    # - where is it synced
    # - is it part of an archive?
    # - when was it synced
    # - when was it modified
    pass


def backup(ns):
    """Process a backup request
    Might be an archive
    """
    print 'backup', vars(ns)
    pass


def recover(ns):
    """Process a recover request
    Might be an archive
    """
    print 'recover', vars(ns)
    pass


def sync(ns):
    """Process a sync request

    Synchronize a directory
    """
    print 'sync', vars(ns)
    pass


def clone(ns):
    """Process a clone request
    """
    print 'clone', vars(ns)
    pass


def run(args=None):
    parser = build_argument_parser()
    ns = parser.parse_args(args)
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
