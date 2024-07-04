#!/usr/bin/env python3
"""typed annotation mixed list """
from typing import List, Union

MixedList = List[Union[int, float]]


def sum_mixed_list(mxd_lst: MixedList) -> float:
    result: float = 0
    i: int

    for i in mxd_lst:
        result += i
    return result
