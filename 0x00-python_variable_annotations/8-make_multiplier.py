#!/usr/bin/env python3
"""module containing make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function"""
    def multiply(value: float) -> float:
        """funct multiply"""
        return value * multiplier

    return multiply
