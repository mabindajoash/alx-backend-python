#!/usr/bin/env python3
"""module containing sum_mixed_list function"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes an argument of type float and int"""
    return sum(mxd_lst)
