# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import json
import pytest  # type: ignore

import json_schema_compress.json_schema_compress as jsc


def test_process_ok_empty_array():
    job = ['[]']
    assert jsc.process(job) == job[0]


def test_process_ok_empty_object():
    job = ['{}']
    assert jsc.process(job) == job[0]


def test_process_ok_direct_json_text(capsys):
    job = ['{"a": "b", "c": 42, "d": [1, true, false, null, 3.1415, -999999999999999999999]}']
    assert jsc.process(job) == job[0]


def test_process_ok_direct_json_text_single_description_member_full_stop(capsys):
    job = [r'{"a": "b", "c": 42, "description": "The thing does stuff.\n\n But not yet enough"}']
    compressed = r'{"a": "b", "c": 42, "description": "The thing does stuff."}'
    assert jsc.process(job) == compressed


def test_process_ok_direct_json_text_single_description_member_newline_only(capsys):
    job = [r'{"a": "b", "c": 42, "description": "The thing does stuff\n\n But not yet enough"}']
    compressed = r'{"a": "b", "c": 42, "description": "The thing does stuff"}'
    assert jsc.process(job) == compressed


def test_process_ok_direct_json_text_single_description_member_no_edn_token(capsys):
    job = [r'{"a": "b", "c": 42, "description": "The thing does stuff endlessly without any full stop or newline"}']
    compressed = r'{"a": "b", "c": 42, "description": "The thing does stuff endlessly without any full stop or newline"}'
    assert jsc.process(job) == compressed


def test_process_ok_direct_json_text_two_description_members(capsys):
    job = [r'{"a": {"description": "An A. Of course"}, "b": {"description": "A B. Maybe"}}']
    compressed = r'{"a": {"description": "An A."}, "b": {"description": "A B."}}'
    assert jsc.process(job) == compressed


def test_process_nok_wrong_type_string():
    bad = ["bad"]
    message = r"Expecting value: line 1 column 1 \(char 0\)"
    with pytest.raises(json.decoder.JSONDecodeError, match=message):
        jsc.process(bad)


def test_extract_paths_ok_direct_simple_json_text():
    job = [r'{"a": "b", "c": 42, "description": "The thing does stuff."}']
    assert jsc.extract_paths(json.loads(job[0])) == ['a', 'c', 'description']


def test_extract_paths_ok_direct_nested_json_text():
    job = [r'{"a": {"a1": "b1", "a2": -1}, "c": 42, "d": [1, 2, 3]}']
    assert jsc.extract_paths(json.loads(job[0])) == ['a/a1', 'a/a2', 'c', 'd']
