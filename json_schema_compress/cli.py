#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import os
import sys

from json_schema_compress.json_schema_compress import process

DEBUG = os.getenv("JSON_SCHEMA_COMPRESS_DEBUG")


# pylint: disable=expression-not-assigned
def main(argv=None):
    """Process ... TODO."""
    argv = sys.argv[1:] if argv is None else argv
    verbose = True if "-v" in argv or "--verbose" in argv else False
    verbose and print(f"No verbose mode implemented")
    print(process(argv))
