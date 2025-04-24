#!/usr/bin/env python3
"""module containing function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return the square of v"""
    return (k, v*v)
