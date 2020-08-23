#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import json
import os
import sys

from json_schema_compress.json_schema_compress import process, extract_paths

DEBUG = os.getenv("JSON_SCHEMA_COMPRESS_DEBUG")
ENCODING = "utf-8"


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process ... TODO."""
    argv = sys.argv[1:] if argv is None else argv
    verbose = True if "-v" in argv or "--verbose" in argv else False
    verbose and print(f"No verbose mode implemented")
    extract_mode = True if "-x" in argv or "--extract" in argv else False
    if extract_mode:
        argv = [arg for arg in argv if arg not in ("-x", "--extract")]
        if argv:
            paths = []
            with open(argv[0], "r", encoding=ENCODING) as handle:
                paths = extract_paths(json.load(handle))
            for path in paths:
                print(path)
    else:
        print(process(argv))
