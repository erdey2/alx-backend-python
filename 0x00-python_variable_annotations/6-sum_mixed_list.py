#!/usr/bin/env python3
"""typed annotation mixed list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ typed annotation mixed list """
    return sum(mxd_lst)
