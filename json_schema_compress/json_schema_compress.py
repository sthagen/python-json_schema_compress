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
    """Initial tree visitor implementation compressing values based on predicate."""
    if isinstance(tree, (dict, list)):
        if isinstance(tree, dict):
            for key, value in tree.items():
                if predicate(key):
                    tree[key] = compressor(value)
                elif isinstance(value, (dict, list)):
                    visit(predicate, compressor, value)
        else:
            for value in tree:
                visit(predicate, compressor, value)


def process(data):
    """Model documentation ... TODO."""
    tree = json.loads(data[0])
    visit(is_description, keep_first_sentence_only, tree)
    return json.dumps(tree)
