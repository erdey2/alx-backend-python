#!/usr/bin/env python3
"""iterating object module """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ typed annotation for object """
    return [(i, len(i)) for i in lst]
