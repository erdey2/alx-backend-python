#!/usr/bin/env python3
""" tpped annotation  function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function as a type annotation """
    return lambda x: x * multiplier
