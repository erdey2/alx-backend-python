#!/usr/bin/env python3
"""complex types module """

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ convert to tuple """
    return (k, v**2)
