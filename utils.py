#  Copyright (C) 2023  Cullen St-Clair
#  Licensed Under the GNU GPL v3.0 License
#  See LICENSE for more information

from argparse import ArgumentTypeError
from pathlib import Path


def get_file_size(file: Path) -> str:
    """Returns the size of a file in relevant units."""
    if not file.is_file():
        raise ValueError(f"File not found: {file}")

    size = file.stat().st_size
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{round(size / 1024, 1)} KB"
    elif size < 1024 ** 3:
        return f"{round(size / 1024 ** 2, 1)} MB"
    else:
        return f"{round(size / 1024 ** 3, 1)} GB"


def non_negative_int(value):
    """Check that the value is a non-negative integer"""
    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid non-negative int value")
    if ivalue < 0:
        raise ArgumentTypeError(f"'{value}' is an invalid non-negative int value")
    return ivalue


def positive_int(value):
    """Check that the value is a positive integer"""
    try:
        ivalue = int(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid positive int value")
    if ivalue <= 0:
        raise ArgumentTypeError(f"'{value}' is an invalid positive int value")
    return ivalue


def positive_float(value):
    """Check that the value is a positive float"""
    try:
        fvalue = float(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid positive float value")
    if fvalue <= 0:
        raise ArgumentTypeError(f"'{value}' is an invalid positive float value")
    return fvalue


def valid_alpha(value):
    """Check that the value is a float in the range [0-1]"""
    try:
        fvalue = float(value)
    except ValueError:
        raise ArgumentTypeError(f"'{value}' is an invalid value (must be in range [0-1])")
    if fvalue < 0 or fvalue > 1:
        raise ArgumentTypeError(f"'{value}' is an invalid value (must be in range [0-1])")
    return fvalue
