# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import json_schema_compress.cli as cli


def test_main_ok_empty_array(capsys):
    job = ['[]']
    assert cli.main(job) is None
    out, err = capsys.readouterr()
    assert out.strip() == job[0]
