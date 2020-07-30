# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import json_schema_compress.cli as cli


def test_main_ok_empty_array(capsys):
    empty = '[]'
    assert cli.main(empty) is None
    out, err = capsys.readouterr()
    assert out.strip() == str(None)
