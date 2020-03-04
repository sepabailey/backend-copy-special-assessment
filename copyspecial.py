#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
# import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "Sean Bailey, Koren Niles"


# +++your code here+++
def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    result = []
    file_directory = os.listdir(dirname)  # list of paths in that dir
    for file_name in file_directory:
        if re.search(r'__\w+__', file_name):
            result.append(file_name)
    return result


def copy_to(path, to_dir):
    """Copy all of the given files to the
    given dir, creating it if necessary."""
    cwd = os.getcwd()
    if not os.path.exists(path):
        create_dir = 'mkdir -p {0}'.format(path)
        os.system(create_dir)
    else:
        print("Path exists")
    for file in to_dir:
        os.chdir(cwd)
        shutil.copy(file, path)
        # could error out if already exists os.path.exists():


def zip_to(paths, zipfile):
    """Zip up all of the given files into a
    new zip file with the given name."""
    paths = list(paths)
    command = "zip -j {} {}".format(zipfile, ' '.join(paths))
    print("Command I'm going to do: ")
    print(command)
    os.system(command)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO need an argument to pick up 'from_dir'
    parser.add_argument('fromdir', help='dir to look for local files')
    args = parser.parse_args()

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.

    all_paths = get_special_paths(args.fromdir)

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with
    # any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if args.todir:
        copy_to(args.todir, all_paths)
    if args.tozip:
        zip_to(all_paths, os.path.join(os.getcwd(), args.tozip))

    if not args.todir and not args.tozip:
        for file in all_paths:
            print(os.path.abspath(file))


if __name__ == "__main__":
    main()
