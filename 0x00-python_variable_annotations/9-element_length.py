#!/usr/bin/env python3
"""module demonstrating duck typing"""
from typing import Sequence, Tuple, Any, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function to demonstrate duck typing"""
    return [(i, len(i)) for i in lst]
