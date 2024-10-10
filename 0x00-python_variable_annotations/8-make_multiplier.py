#!/usr/bin/env python3
""" functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiplies a float """
    def multiplies(n: float):
        """ multiply two number """
        return n * multiplier
    return multiplies
