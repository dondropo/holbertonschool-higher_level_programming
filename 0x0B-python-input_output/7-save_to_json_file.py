#!/usr/bin/python3
import json
"""
save object to a file
"""


def save_to_json_file(my_obj, filename):
    """writes an object to a text file, using json"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
