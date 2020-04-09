#!/usr/bin/env python3
import json
import sys
from typing import Any, Dict, List, Union

def traverse(path: str, obj: Any) -> None:
    """
    Traverse the object recursively and print every path / value pair.
    """
    if isinstance(obj, list):
        for i, subnode in enumerate(obj):
            traverse(path + f'[{i!r}]', subnode)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            traverse(path + f'[{k!r}]', v)
    else:
        print(path + ' => ' + f'{obj!r}')

def read_file(fpath: str) -> Dict:
    """
    Read the JSON file and return its content as a Python data structure.
    """
    with open(fpath, encoding='utf8') as f:
        return json.load(f)    # type: ignore

def process(fname: str) -> None:
    """
    Process the given JSON file.
    """
    d: Dict = read_file(fname)
    traverse("root", d)

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: jsonpath <input.json>")
        sys.exit(1)
    #
    fname = sys.argv[1]
    process(fname)