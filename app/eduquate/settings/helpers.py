from pathlib import Path

import environ

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent


def _insert_with_offset(elements, target_element, new_element, offset):
    try:
        idx = elements.index(target_element) + offset
    except ValueError:
        idx = 0
    elements[idx:idx] = [new_element]


def insert_after(elements, target_element, new_element):
    return _insert_with_offset(elements, target_element, new_element, offset=1)


def insert_before(elements, target_element, new_element):
    return _insert_with_offset(elements, target_element, new_element, offset=0)
