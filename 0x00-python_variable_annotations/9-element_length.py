#!/usr/bin/env python3
"""module demonstrating duck typing"""
from typing import Sequence, Tuple, Any, List


def element_length(lst: Sequence[Any]) -> List[Tuple[Any, int]]:
    """function to demonstrate duck typing"""
    return [(i, len(i)) for i in lst]
