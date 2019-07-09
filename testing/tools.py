# -*- coding: utf-8 -*-
import ast
import string
import sys


def convert_list(item):
    item = str(item)
    item = item.translate(string.maketrans("", ""), "[]")
    item = item.split(",")
    return [int(value) for value in item]


def normalize_data(data):
    """Receives a dict and returns normalized data."""

    clean_data = dict()
    for key, value in data.items():
        clean_data[key] = value
        if hasattr(value, "pk"):
            clean_data[key] = value.pk
            continue
        if isinstance(value, float):
            clean_data[key] = round(value, 2)
            continue
        if sys.version_info >= (3, 0, 0):
            # for Python 3
            if not isinstance(value, (str, bytes)):
                continue
        else:
            # for Python 2
            if not isinstance(value, (str, unicode)):  # pylint: disable=E0602
                continue
        if (
            value.replace(".", "", 1).isdigit()
            or value.replace("-", "", 1).isdigit()
            or value in ("True", "False")
        ):
            eval_value = ast.literal_eval(value)
            if isinstance(eval_value, float):
                eval_value = round(eval_value, 2)
            clean_data[key] = eval_value
            continue
        if value in ("", "null", None):
            clean_data[key] = None
            continue
        try:
            clean_data[key] = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            clean_data[key] = value
    return clean_data


def del_key_by_value(item, clean="null"):
    if isinstance(item, (str, int, float)):
        return item

    for key, value in item.copy().items():
        if isinstance(value, list):
            for item_value in value:
                del_key_by_value(item_value)
            continue
        if isinstance(value, dict):
            continue
        if value in (None, clean):
            del item[key]
    return item
