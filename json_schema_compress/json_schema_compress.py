# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Add logical documentation here later TODO."""
import json


def process(data):
    """Model documentation ... TODO."""
    hosted = json.loads(data[0])
    for key in hosted:
        if key == "description":
            value = hosted[key]
            if '.' in value:
                hosted[key] = f"{value.split('.', 1)[0]}."
            elif '\n' in value:
                hosted[key] = value.split('\n', 1)[0]
    return json.dumps(hosted)
