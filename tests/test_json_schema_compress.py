# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest  # type: ignore

import json_schema_compress.json_schema_compress as jsc

def test_walk_ok_empty_array():
    job = ['[]']
    assert jsc.process(job) == job[0]


def test_walk_ok_empty_object():
    job = ['{}']
    assert jsc.process(job) == job[0]
