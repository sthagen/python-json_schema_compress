# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
import sys

from json_schema_compress.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # pragma: no cover
