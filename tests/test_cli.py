# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import json_schema_compress.cli as cli


def test_main_ok_empty_array(capsys):
    job = ['[]']
    assert cli.main(job) is None
    out, err = capsys.readouterr()
    assert out.strip() == job[0]


def test_main_ok_empty_object(capsys):
    job = ['{}']
    assert cli.main(job) is None
    out, err = capsys.readouterr()
    assert out.strip() == job[0]


def test_main_nok_wrong_type_string():
    bad = "bad"
    message = r"Expecting value: line 1 column 1 \(char 0\)"
    with pytest.raises(json.decoder.JSONDecodeError, match=message):
        cli.main(bad)
