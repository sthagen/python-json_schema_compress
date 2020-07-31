# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import json


def is_description(key):
    """Simple matcher."""
    return key == "description"


def keep_first_sentence_only(value):
    """Simple compressor."""
    if '.' in value:
        return f"{value.split('.', 1)[0]}."
    if '\n' in value:
        return value.split('\n', 1)[0]
    return value


def visit(predicate, compressor, tree):
    """Naive initial tree visitor compressing values based on predicate."""
    for key in tree:
        if predicate(key):
            tree[key] = compressor(tree[key])
    return tree


def process(data):
    """Model documentation ... TODO."""
    tree = json.loads(data[0])
    visit(is_description, keep_first_sentence_only, tree)
    return json.dumps(tree)
