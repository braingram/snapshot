#!/usr/bin/env python
"""
Some helper functions to allow running commands

This should make running rsync easy, very easy
"""

import os
import subprocess


rsync_command = 'rsync'


def run_command(command):
    # cwd
    if isinstance(command, (str, unicode)):
        command = command.split()
    p = subprocess.Popen(
        command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        cwd=os.curdir)
    return p


def rsync(src, dst, *opts):
    cmd = [rsync_command, ]
    cmd += opts
    cmd += [src, dst]
    return run_command(cmd)
